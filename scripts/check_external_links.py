from __future__ import annotations

import concurrent.futures
import os
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STRICT = os.environ.get("STRICT_LINKS") == "1"
TIMEOUT = 15

MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\((https?://[^)\s]+)\)")
PLAIN_URL = re.compile(r"(?<!\()https?://[^\s<>]+")


@dataclass(frozen=True)
class Result:
    url: str
    status: int | None
    level: str
    message: str


def collect_urls() -> list[str]:
    urls: set[str] = set()
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        urls.update(MARKDOWN_LINK.findall(text))
        urls.update(PLAIN_URL.findall(text))
    cleaned = {
        url.rstrip(".,;:!?'\"")
        for url in urls
        if not url.startswith(("http://localhost", "http://127.0.0.1"))
    }
    return sorted(cleaned)


def request(url: str, method: str) -> int:
    req = urllib.request.Request(
        url,
        method=method,
        headers={
            "User-Agent": "apps-berater-link-check/1.1",
            "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
        },
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
        return int(response.status)


def check(url: str) -> Result:
    try:
        status = request(url, "HEAD")
    except urllib.error.HTTPError as exc:
        if exc.code in {405, 501}:
            try:
                status = request(url, "GET")
            except urllib.error.HTTPError as get_exc:
                status = get_exc.code
            except Exception as get_exc:  # noqa: BLE001
                return Result(url, None, "warning", f"GET nicht prüfbar: {get_exc}")
        else:
            status = exc.code
    except Exception as exc:  # noqa: BLE001
        return Result(url, None, "warning", f"nicht prüfbar: {exc}")

    if 200 <= status < 400:
        return Result(url, status, "ok", "erreichbar")
    if status in {401, 403, 429}:
        return Result(url, status, "warning", "Zugriff/Rate-Limit; nicht als defekt gewertet")
    if status in {404, 410}:
        return Result(url, status, "error", "Quelle nicht gefunden")
    return Result(url, status, "warning", "unerwarteter Status")


def main() -> int:
    urls = collect_urls()
    print(f"Externe Links: {len(urls)}")
    if not urls:
        return 0

    workers = min(8, len(urls))
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        results = list(executor.map(check, urls))

    errors = []
    warnings = []
    for result in results:
        line = f"{result.status or '-'} {result.url} – {result.message}"
        if result.level == "error":
            errors.append(line)
        elif result.level == "warning":
            warnings.append(line)

    for line in warnings:
        print(f"WARNUNG: {line}")
    for line in errors:
        print(f"FEHLER: {line}")

    if errors:
        return 1
    if STRICT and warnings:
        return 1
    print("OK: Keine eindeutig defekten externen Links gefunden")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
