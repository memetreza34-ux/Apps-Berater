from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "wissen" / "app-master-anleitung"
ERRORS: list[str] = []
WARNINGS: list[str] = []

REQUIRED = [
    GUIDE / "README.md",
    GUIDE / "INHALTSVERZEICHNIS.md",
    GUIDE / "VOLLSTAENDIGKEITSSTANDARD.md",
    GUIDE / "MASTER-CHECKLISTE.md",
    GUIDE / "STATUS-UND-ROADMAP.md",
    GUIDE / "QUELLEN-UND-AKTUALISIERUNGSREGISTER.md",
    GUIDE / "01-orientierung-voraussetzungen" / "README.md",
    GUIDE / "02-recht-regeln-normen" / "README.md",
    GUIDE / "02-recht-regeln-normen" / "AKTUELLER-RECHTSSTAND-2026-08.md",
    GUIDE / "03-funktionen-system-daten" / "README.md",
    GUIDE / "04-entwicklung-mit-ki" / "README.md",
    GUIDE / "04-idee-markt-geschaeft" / "README.md",
    GUIDE / "05-produkt-prd-mvp" / "README.md",
    GUIDE / "05-veroeffentlichung" / "README.md",
    GUIDE / "06-marketing-launch" / "README.md",
    GUIDE / "06-ux-ui-design" / "README.md",
    GUIDE / "07-betrieb-skalierung" / "README.md",
    GUIDE / "07-technik-grundlagen" / "README.md",
    GUIDE / "08-umsetzung-kernfunktionen" / "README.md",
    GUIDE / "09-qualitaet-security-datenschutz" / "README.md",
    GUIDE / "10-monetarisierung-zahlungen" / "README.md",
    GUIDE / "11-beispielwege" / "README.md",
    GUIDE / "11-beispielwege" / "A-offline-fokus-pwa.md",
    GUIDE / "11-beispielwege" / "B-team-aufgaben-saas.md",
    GUIDE / "11-beispielwege" / "C-ki-lernassistent-minderjaehrige.md",
    GUIDE / "12-werkzeuge-anbieter" / "README.md",
    GUIDE / "13-langfristige-pflege" / "README.md",
    GUIDE / "14-abschlusspruefung" / "PRUEFRUBRIK.md",
    GUIDE / "vorlagen" / "README.md",
    GUIDE / "vorlagen" / "MASTER-PROJEKTPAKET.md",
    GUIDE / "vorlagen" / "PRD-UND-MVP.md",
    GUIDE / "vorlagen" / "FUNKTIONSDOSSIER.md",
    GUIDE / "vorlagen" / "RECHT-REGELN-NORMEN-MATRIX.md",
    GUIDE / "vorlagen" / "TEST-UND-RELEASE-DOSSIER.md",
    GUIDE / "vorlagen" / "MARKETING-UND-LAUNCHPLAN.md",
    GUIDE / "vorlagen" / "BETRIEBSHANDBUCH.md",
]

for path in REQUIRED:
    if not path.exists():
        ERRORS.append(f"Pflichtdatei fehlt: {path.relative_to(ROOT)}")

link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
md_files = sorted(GUIDE.rglob("*.md"))

for path in md_files:
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    if text and not text.endswith("\n"):
        ERRORS.append(f"Kein abschließender Zeilenumbruch: {rel}")
    if re.search(r"\b(TODO|TBD|FIXME)\b", text):
        WARNINGS.append(f"Unfertig-Marker: {rel}")
    if len(text.strip()) < 300 and path.name != "README.md":
        WARNINGS.append(f"Sehr kurze Inhaltsdatei: {rel}")

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
            ERRORS.append(f"Link verlässt Repository: {rel} -> {target}")
            continue
        if not resolved.exists():
            ERRORS.append(f"Defekter relativer Link: {rel} -> {target}")

fullness = GUIDE / "VOLLSTAENDIGKEITSSTANDARD.md"
if fullness.exists():
    text = fullness.read_text(encoding="utf-8")
    for term in [
        "Recht",
        "Normen",
        "Funktionen",
        "Daten",
        "Marketing",
        "Veröffentlichung",
        "Betrieb",
        "Produktende",
    ]:
        if term not in text:
            ERRORS.append(f"Vollständigkeitsstandard enthält '{term}' nicht")

rubric = GUIDE / "14-abschlusspruefung" / "PRUEFRUBRIK.md"
if rubric.exists():
    text = rubric.read_text(encoding="utf-8")
    if "125 Punkte" not in text or "FERTIG / NICHT FERTIG" not in text:
        ERRORS.append("Prüfrubrik enthält Abschlusskriterien nicht")

examples = list((GUIDE / "11-beispielwege").glob("[ABC]-*.md"))
if len(examples) != 3:
    ERRORS.append(f"Es werden genau drei Beispielwege erwartet; gefunden: {len(examples)}")

print(f"Geprüft: {len(md_files)} Markdown-Dateien der Master-Anleitung")
for warning in WARNINGS:
    print(f"WARNUNG: {warning}")
for error in ERRORS:
    print(f"FEHLER: {error}")

if ERRORS:
    sys.exit(1)
print("OK: Master-Anleitung erfüllt die strukturelle Vollständigkeitsprüfung")
