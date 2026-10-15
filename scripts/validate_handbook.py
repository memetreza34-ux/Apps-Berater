from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "wissen" / "allgemeine-app-entwicklung"
ERRORS: list[str] = []
WARNINGS: list[str] = []

REQUIRED = [
    ROOT / "README.md",
    ROOT / ".github" / "workflows" / "qualitaet.yml",
    ROOT / "scripts" / "app_decision_assistant.py",
    APP / "START-HIER-V1.1.md",
    APP / "INHALTSVERZEICHNIS-V1.1.md",
    APP / "STATUS-V1.1.md",
    APP / "11-masterprozess" / "APP-VON-0-BIS-RELEASE.md",
    APP / "11-masterprozess" / "QUALITAETSSYSTEM.md",
    APP / "CHECKLISTE-VOR-JEDEM-RELEASE.md",
    APP / "QUELLEN-UND-RECHTSSTAND.md",
    APP / "vorlagen" / "produktionspaket-v1.md",
    APP / "vorlagen" / "evidenz-matrix.md",
    APP / "14-plattform-playbooks" / "README.md",
    APP / "15-runbooks" / "README.md",
    ROOT / "beispiel-apps" / "focusflow-pwa" / "index.html",
    ROOT / "beispiel-apps" / "focusflow-pwa" / "app.js",
    ROOT / "beispiel-apps" / "focusflow-supabase" / "rls-smoke.mjs",
]

for path in REQUIRED:
    if not path.exists():
        ERRORS.append(f"Pflichtdatei fehlt: {path.relative_to(ROOT)}")

md_files = sorted(ROOT.rglob("*.md"))
link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
heading_pattern = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)

for path in md_files:
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)

    if text and not text.endswith("\n"):
        WARNINGS.append(f"Kein abschließender Zeilenumbruch: {rel}")
    if "\t" in text:
        WARNINGS.append(f"Tabulator gefunden: {rel}")
    if re.search(r"\b(TODO|TBD|FIXME)\b", text) and "ROADMAP" not in path.name:
        WARNINGS.append(f"Unfertig-Marker gefunden: {rel}")

    seen_headings: set[tuple[int, str]] = set()
    for match in heading_pattern.finditer(text):
        key = (len(match.group(1)), match.group(2).strip().lower())
        if key in seen_headings:
            WARNINGS.append(f"Doppelte Überschrift '{match.group(2)}': {rel}")
        seen_headings.add(key)

    for target in link_pattern.findall(text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        clean = target.split("#", 1)[0]
        if not clean:
            continue
        resolved = (path.parent / clean).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            ERRORS.append(f"Relativer Link verlässt das Repository in {rel}: {target}")
            continue
        if not resolved.exists():
            ERRORS.append(f"Defekter relativer Link in {rel}: {target}")

sources = APP / "QUELLEN-UND-RECHTSSTAND.md"
if sources.exists():
    text = sources.read_text(encoding="utf-8")
    if "Letzte Prüfung" not in text:
        ERRORS.append("Quellenregister enthält kein Prüfdatum")

quality = APP / "11-masterprozess" / "QUALITAETSSYSTEM.md"
if quality.exists():
    text = quality.read_text(encoding="utf-8")
    # Groß-/Kleinschreibung ignorieren: Begriffe stehen je nach Satzposition
    # groß (Überschrift) oder klein (Fließtext).
    text_lower = text.lower()
    for required_term in [
        "Blocker",
        "Nachweis",
        "Evidenzstufen",
        "Qualitätsquote",
        "Definition of Done",
        "risikobasierte Mindestwerte",
    ]:
        if required_term.lower() not in text_lower:
            ERRORS.append(f"Qualitätssystem enthält '{required_term}' nicht")

start = APP / "START-HIER-V1.1.md"
if start.exists():
    text = start.read_text(encoding="utf-8")
    gates = re.findall(r"^\|\s*([0-9]+)\s+[–-]", text, re.MULTILINE)
    if len(gates) != 7 or set(gates) != {str(i) for i in range(7)}:
        ERRORS.append(f"Startguide muss genau Gate 0 bis 6 enthalten; gefunden: {gates}")
    if "Sieben Freigabe-Gates" not in text:
        ERRORS.append("Startguide muss die sieben Freigabe-Gates korrekt benennen")

json_files = [
    APP / "02-design" / "beispiele" / "focusflow-design-tokens.json",
    ROOT / "beispiel-apps" / "focusflow-pwa" / "manifest.webmanifest",
]
for path in json_files:
    if not path.exists():
        ERRORS.append(f"JSON-Pflichtdatei fehlt: {path.relative_to(ROOT)}")
        continue
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        ERRORS.append(f"Ungültiges JSON in {path.relative_to(ROOT)}: {exc}")

manifest = ROOT / "beispiel-apps" / "focusflow-pwa" / "manifest.webmanifest"
if manifest.exists():
    data = json.loads(manifest.read_text(encoding="utf-8"))
    for key in ["name", "short_name", "start_url", "scope", "display", "icons"]:
        if key not in data:
            ERRORS.append(f"PWA-Manifest enthält '{key}' nicht")

print(f"Geprüft: {len(md_files)} Markdown-Dateien")
for warning in WARNINGS:
    print(f"WARNUNG: {warning}")
for error in ERRORS:
    print(f"FEHLER: {error}")

if ERRORS:
    sys.exit(1)
print("OK: Struktur- und Inhaltsprüfung bestanden")
