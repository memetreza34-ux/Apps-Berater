from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class FocusFlowStaticTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        for name in [
            "index.html",
            "styles.css",
            "app.js",
            "sw.js",
            "manifest.webmanifest",
            "icon.svg",
        ]:
            self.assertTrue((ROOT / name).exists(), name)

    def test_html_has_accessible_core_controls(self) -> None:
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        for required in [
            'lang="de"',
            'href="#main"',
            'id="task-form"',
            'id="task-title"',
            'id="task-list"',
            'id="start-pause"',
            'id="delete-data"',
            'role="status"',
            'aria-live="polite"',
        ]:
            self.assertIn(required, html)

        ids = re.findall(r'id="([^"]+)"', html)
        self.assertEqual(len(ids), len(set(ids)), "HTML-IDs müssen eindeutig sein")

    def test_javascript_has_data_controls(self) -> None:
        script = (ROOT / "app.js").read_text(encoding="utf-8")
        for required in [
            "localStorage.setItem",
            "localStorage.removeItem",
            "JSON.stringify",
            "URL.createObjectURL",
            "navigator.serviceWorker.register",
            "window.confirm",
        ]:
            self.assertIn(required, script)

    def test_manifest_is_valid_and_scoped(self) -> None:
        manifest = json.loads((ROOT / "manifest.webmanifest").read_text(encoding="utf-8"))
        self.assertEqual(manifest["start_url"], "./")
        self.assertEqual(manifest["scope"], "./")
        self.assertEqual(manifest["display"], "standalone")
        self.assertTrue(manifest["icons"])

    def test_service_worker_caches_app_shell(self) -> None:
        worker = (ROOT / "sw.js").read_text(encoding="utf-8")
        for asset in ["index.html", "styles.css", "app.js", "manifest.webmanifest"]:
            self.assertIn(asset, worker)
        self.assertIn('event.request.method !== "GET"', worker)
        self.assertIn("url.origin !== self.location.origin", worker)

    def test_css_has_accessibility_states(self) -> None:
        css = (ROOT / "styles.css").read_text(encoding="utf-8")
        self.assertIn(":focus-visible", css)
        self.assertIn("prefers-reduced-motion", css)
        self.assertIn("prefers-color-scheme: dark", css)


if __name__ == "__main__":
    unittest.main()
