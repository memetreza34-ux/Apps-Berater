#!/usr/bin/env python3
"""Deterministische Prüfung des KI-App-Kriterienkatalogs.

Aufruf: python3 pruefer/katalog-pruefen/katalog_check.py [Pfad zum Repo Apps-Berater]
Exit-Code 0 = keine Fehler, 1 = Fehler gefunden.
"""
from __future__ import annotations

import collections
import datetime as dt
import re
import sys
from pathlib import Path

REPO = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[2]).expanduser()
KAT = REPO / "wissen" / "ki-app-kriterienkatalog"

ERRORS: list[str] = []
WARNINGS: list[str] = []

# Pflichtthemen: Jedes Thema muss irgendwo im Katalog vorkommen.
# Format: Thema -> Regex (ohne Groß-/Kleinschreibung). Neue Themen hier ergänzen.
THEMEN = {
    # AI Act
    "AI Act Rolle Anbieter/Betreiber": r"\bAnbieter\b.*\bBetreiber\b|\bBetreiber\b.*\bAnbieter\b",
    "AI Act verbotene Praktiken (Art. 5)": r"Art\. 5\b",
    "AI Act KI-Kompetenz (Art. 4)": r"KI-Kompetenz",
    "AI Act Transparenz (Art. 50)": r"Art\. 50",
    "AI Act Hochrisiko Anhang III": r"Anhang III",
    "AI Act Anhang I": r"Anhang I\b",
    "AI Act Wertschöpfungskette (Art. 25)": r"Art\. 25\)",
    "AI Act GPAI": r"GPAI",
    "AI Act Digital Omnibus": r"Omnibus",
    "AI Act Kennzeichnungskodex": r"Verhaltenskodex",
    "AI Act Bußgelder": r"35 Mio",
    "Deutsche KI-Aufsicht (KI-MIG)": r"KI-MIG|Bundesnetzagentur",
    "Deepfakes": r"Deepfake",
    "Maschinenlesbare Kennzeichnung / C2PA": r"C2PA|maschinenlesbar",
    "Emotionserkennung": r"Emotionserkennung",
    "Nudify-/Missbrauchsverbot": r"Nacktbilder|intimer Darstellungen|Missbrauchsdarstellung",
    # Datenschutz
    "DSGVO Rechtsgrundlage": r"Rechtsgrundlage",
    "Auftragsverarbeitungsvertrag": r"Auftragsverarbeitungsvertrag|AVV",
    "Drittlandübermittlung": r"Drittland|Data Privacy Framework",
    "DSFA": r"DSFA|Folgenabschätzung",
    "Datenschutzbeauftragter": r"Datenschutzbeauftragte",
    "Betroffenenrechte Auskunft/Löschung/Export": r"Auskunft.*\n(?:.*\n)*?.*Löschung|Datenübertragbarkeit",
    "Art. 22 automatisierte Entscheidungen": r"Art\. 22",
    "Besondere Kategorien (Art. 9)": r"Art\. 9",
    "Cookies/TDDDG": r"TDDDG",
    "Consent-Banner fair": r"Ablehnen",
    "Datenpanne 72 Stunden": r"72 Stunden",
    "Kinder Einwilligung unter 16": r"unter 16",
    "Training mit Nutzerdaten": r"Training",
    "Zero-Data-Retention / Aufbewahrung Anbieter": r"Zero-Data-Retention|Aufbewahrung",
    # Verbraucherrecht und weitere Gesetze
    "Impressum DDG": r"§ 5 DDG",
    "AGB / Nutzungsbedingungen": r"Nutzungsbedingungen",
    "Button-Lösung": r"zahlungspflichtig bestellen",
    "Widerrufsbutton": r"Widerrufsbutton",
    "Kündigungsbutton": r"Kündigungsbutton",
    "Preisangaben PAngV": r"PAngV",
    "Aktualisierungspflicht digitale Produkte": r"327",
    "Dark Patterns": r"Dark Pattern",
    "BFSG Barrierefreiheit": r"BFSG",
    "Cyber Resilience Act": r"Cyber Resilience Act|\bCRA\b",
    "Produkthaftung": r"Produkthaftung",
    "Digital Services Act": r"\bDSA\b",
    "Data Act": r"Data Act",
    "Digital Fairness Act": r"Digital Fairness Act",
    "Jugendschutz": r"Jugendschutz",
    "Geoblocking": r"Geoblocking",
    "Werbung kennzeichnen / UWG": r"Werbung kennzeichnen|UWG",
    # Rechte und Lizenzen
    "Urheberrecht KI-Output": r"urheberrechtlich geschützt",
    "Text- und Data-Mining": r"44b",
    "Datenbankherstellerrecht": r"Datenbankhersteller",
    "Open-Source-Lizenzen / AGPL": r"AGPL",
    "Recht am eigenen Bild / Stimme": r"KUG|Stimm",
    "Marke / Markenrecherche": r"Markenrecherche",
    "Schriftlizenzen": r"Schriftlizenz",
    # Sicherheit
    "Secrets nicht im Client": r"NEXT_PUBLIC_",
    "Secret-Scanning": r"Secret-Scan",
    "Row Level Security": r"Row Level Security|\bRLS\b",
    "IDOR / fremde IDs": r"IDOR",
    "XSS / HTML-Ausgabe": r"dangerouslySetInnerHTML|XSS",
    "SSRF": r"SSRF",
    "CORS": r"CORS",
    "Security-Header / CSP": r"Content-Security-Policy|CSP",
    "Rate-Limits": r"Rate-Limit",
    "Slopsquatting / erfundene Pakete": r"Slopsquatting",
    "Lockfile": r"Lockfile",
    "Webhook-Signatur": r"Webhook-Signatur",
    "Mobile sicherer Speicher": r"Keychain|Keystore",
    "App-Echtheit (App Attest / Play Integrity)": r"App Attest|Play Integrity",
    "Mehr-Faktor-Anmeldung": r"Mehr-Faktor",
    # KI-Sicherheit
    "Prompt Injection direkt/indirekt": r"Indirekte Prompt Injection|indirekt",
    "Verborgener Kontext / Systemprompt": r"verborgene[rn]? Kontext",
    "Datenabfluss über Markdown-Bilder": r"Markdown-Bilder",
    "Ausgabe nie ausführen": r"eval",
    "Sandbox für Code-Ausführung": r"Sandbox",
    "Agenten minimale Rechte": r"Minimale Rechte",
    "Menschliche Bestätigung": r"Bestätigung",
    "RAG Mandantentrennung": r"Mandantentrennung",
    "Moderation": r"Moderation",
    "Gefährliche Anleitungen": r"Gefährliche Anleitungen",
    "Halluzinationen": r"Halluzination",
    "Agenten-Risiken (OWASP Agentic)": r"agentische",
    "Modell-Lieferkette / safetensors": r"safetensors",
    "Coding-Agent ohne Produktionszugriff": r"Produktionsdatenbank",
    # KI-API und Kosten
    "max_tokens": r"max_tokens",
    "Timeouts und Retries": r"Timeout",
    "Ausgabenlimit Anbieter": r"Ausgabenlimit",
    "Kontingent pro Nutzer": r"Kontingent",
    "Modellversion festlegen": r"Modellversion",
    "Fallback-Anbieter": r"Ersatzmodell|Ersatzanbieter",
    "Evals / Testsammlung": r"Evals|Testsammlung",
    "Prompt-Caching": r"Prompt-Caching",
    "Fairness / Bias": r"Fairness",
    "Streaming": r"Streaming",
    # Architektur und Code
    "Migrationen versioniert": r"Migrationen",
    "Getrennte Umgebungen": r"Staging",
    "CI bei jedem Push": r"GitHub Actions|\bCI\b",
    "Agenten-Regeldatei": r"CLAUDE\.md|AGENTS\.md",
    "Geld als Ganzzahl": r"Ganzzahl",
    "Offline / Synchronisation": r"Offline",
    # Pflichtfunktionen und UX
    "Konto löschen": r"Konto löschen",
    "Datenexport": r"Datenexport",
    "KI-Hinweis im Chat": r"KI-Hinweis",
    "Lade-/Leer-/Fehlerzustände": r"Leer",
    "Melden-Funktion": r"Melden",
    "Admin-Bereich": r"Admin",
    "E-Mail SPF/DKIM/DMARC": r"DKIM",
    "Automation Bias / blindes Vertrauen": r"Automation Bias|blindes Vertrauen",
    "Quellen anzeigen": r"Quellen anzeigen",
    # Design und Barrierefreiheit
    "WCAG": r"WCAG",
    "Kontrast": r"Kontrast",
    "Screenreader": r"Screenreader",
    "Touch-Flächen": r"Touch-Fl",
    "Design-Tokens": r"Design-Tokens",
    # Betrieb
    "Backups und Restore-Test": r"Wiederherstellung mindestens einmal testen|Restore",
    "Fehler-Tracking": r"Fehler-Tracking",
    "Rollback": r"Zurückrollen|Rollback",
    "Gestaffelter Rollout": r"[Gg]estaffelt",
    "Notfallplan": r"Notfallplan",
    # Stores und Plattformen
    "Apple 5.1.2 Drittanbieter-KI": r"5\.1\.2",
    "Apple ATT": r"App Tracking Transparency",
    "Apple Privacy Manifest": r"Privacy Manifest",
    "Apple 4.3 Duplikate": r"\(4\.3",
    "Google Data Safety": r"Data Safety",
    "Google KI-generierte Inhalte": r"KI-generierte Inhalte",
    "Händlerstatus DSA in Stores": r"Händlerstatus",
    "Signierschlüssel": r"Signierschl",
    "Social-Media-KI-Kennzeichnung": r"YouTube",
    # Business
    "Gewerbe anmelden": r"Gewerbe",
    "Kleinunternehmerregelung": r"Kleinunternehmer",
    "OSS / Umsatzsteuer EU": r"One-Stop-Shop|OSS",
    "E-Rechnung": r"E-Rechnung",
    "Sanktionen": r"Sanktion",
    "Versicherung": r"Versicherung",
    # Sonderfälle
    "Finanz-Apps / Anlageberatung": r"Anlageberatung",
    "Medizinprodukt / MDR": r"MDR",
    "Kinder / COPPA": r"COPPA",
    "Biometrie / Stimme": r"Biometrie",
    "Community / Nutzerinhalte": r"Community",
    "Hardware / IoT": r"IoT",
    "Glücksspiel": r"Glücksspiel",
    "Politische Werbung": r"politische Werbung",
    "Krypto / MiCA": r"MiCA",
    "Rechtsdienstleistung / RDG": r"Rechtsdienstleistung",
    "Spiele / virtuelle Währung": r"virtuelle[rn]? Währung",
    # Ergänzt bei der Prüfung am 02.10.2026
    "AI Act Registrierung Art. 6 Abs. 3": r"registrieren",
    "AI Act Leitlinien Art. 50": r"20\. Juli 2026",
    "Abmahnrisiko KI-Kennzeichnung": r"§ 3a UWG",
    "DSA Art. 18 Polizei-Meldung": r"Art\. 18 DSA",
    "DSA Art. 19 Ausnahme Kleinunternehmen": r"Art\. 19 DSA",
    "Data Act SaaS / Wechsel": r"Wechselentgelte",
    "CRA ENISA-Meldeplattform": r"ENISA",
    "SBOM": r"SBOM|Softwarestückliste",
    "Kündigungs-Bestätigungsseite (BGH)": r"Kündigungs-Bestätigungsseite",
    "Widerrufsbelehrung neu": r"Widerrufsbelehrung aktualisieren",
    "Preiserhöhungen bei Abos": r"Preiserhöhung",
    "§ 327r BGB Änderungen": r"327r",
    "Personalisierte Preise": r"[Pp]ersonalisierte Preise",
    "DSGVO abmahnbar": r"abmahnbar",
    "Scoring § 37a BDSG": r"37a BDSG",
    "Newsletter-Tracking": r"Newsletter-Tracking",
    "Werbe-Einwilligung IAB TCF": r"IAB-TCF|IAB TCF",
    "GEMA / Memorisierung": r"GEMA",
    "Supabase GRANT": r"GRANT",
    "user_metadata": r"user_metadata",
    "Server Actions": r"Server Action",
    "Fail closed": r"[Ff]ail closed|sicher schließen",
    "Installationsskripte / npm 12": r"npm 12|approve-scripts",
    "Paket-Wartezeit": r"min-release-age|Wartezeit",
    "Actions per Commit-SHA": r"Commit-SHA|Commit-Hash",
    "Tödliches Dreigespann": r"Dreigespann",
    "MCP Rug Pull": r"Rug Pull",
    "Coding-Agent ohne Rückfragen": r"ohne Rückfragen",
    "Agenten-Konfiguration prüfen": r"Regeldateien des Agenten",
    "Gemini-Bedingungen EU": r"Gemini API für EU-Nutzer",
    "Beratungs-Apps Anbieterregeln": r"Beratungs-Apps",
    "Gratis-Tarife und Training": r"Gratis-Tarif",
    "Apple 2.5.2 nachgeladener Code": r"2\.5\.2",
    "Apple 3.1.1 Credits": r"Credits dürfen nicht verfallen",
    "Apple 4.7 Chatbots": r"\(4\.7\)",
    "Apple EU-Bedingungen": r"1\. Oktober 2026",
    "Android-Entwicklerverifizierung": r"Entwicklerverifizierung",
    "Xcode-Pflicht": r"Xcode 26",
    "Google-Abo-Regeln": r"Google-Play-Abo-Regeln",
    "WCAG Fokus nicht verdeckt": r"Fokus nicht verdeckt",
    "WCAG Zielgröße 24 px": r"24 × 24",
    "WCAG Konsistente Hilfe": r"Hilfe immer an derselben Stelle",
    "WCAG Redundante Eingabe": r"Nichts doppelt eingeben",
    "WCAG Barrierefreie Anmeldung": r"Barrierefreie Anmeldung",
    "WCAG Statusmeldungen": r"Statusmeldungen ansagen",
    "BFSG Anlage 3": r"Anlage 3",
    "EN 301 549 V4": r"V4\.1\.1",
    "Systemeinstellungen respektieren": r"Systemeinstellungen",
    "Chatbot-Haftung (OLG Hamm)": r"OLG Hamm",
    "Umweltaussagen": r"Umweltversprechen",
    "KI-Kundenstimmen": r"Kundenstimmen",
    "Reverse Charge": r"Reverse Charge",
    "DAC7": r"DAC7",
    "BNPL / Verbraucherkredit": r"Jetzt kaufen, später zahlen",
    "Erotik nur mit Altersverifikation": r"geschlossenen Benutzergruppe",
    "Jugendschutz im Betriebssystem": r"Jugendschutz-Modus",
    "Phishing-resistente Anmeldung": r"[Pp]hishing-resistent",
    "Dating / Fake-Profile": r"Dating",
    "Kosten Entwicklerkonten": r"Entwicklerkonten",
    "Zahlungskonto KYC": r"Know Your Customer",
    # Vibe-Coding und Launch
    "Git und kleine Commits": r"commit",
    "Warnsignale Agent": r"Warnsignal",
    "Idee prüfen / Nutzerinterviews": r"echten Menschen|Nutzerinterview",
    "App Store Optimization": r"App Store Optimization",
    "Tracking-Plan": r"Tracking-Plan",
    "Kennzahlen CAC / Churn": r"CAC|Churn",
    # Prüfung 13.10.2026
    "Impressum Social Media": r"Impressum auch auf Social-Media",
    "DSA Behördenanordnungen (Art. 9/10)": r"Art\. 9 und 10 DSA",
    "Terroristische Inhalte (TCO-VO)": r"2021/784",
    "UrhDaG Upload-Plattformen": r"UrhDaG",
    "Abmahnung richtig behandeln": r"Unterlassungserklärung",
    "Abmahnkosten § 13 Abs. 4 UWG": r"§ 13 Abs\. 4 UWG",
    "Behördliche Auskunftsersuchen": r"Auskunftsersuchen",
    "Credits-Verfall AGB": r"Guthaben nicht verfallen",
    "Eingebettete Inhalte Zwei-Klick": r"Zwei-Klick",
    "Geleakte Passwörter": r"Geleakte Passwörter",
    "Social Bots MStV": r"§ 18 Abs\. 3 Medienstaatsvertrag",
    "Messenger-Bots / WhatsApp": r"WhatsApp",
    "Apple Exportkontrolle Verschlüsselung": r"ITSAppUsesNonExemptEncryption",
    "Google Werbe-ID": r"AD_ID",
    "Desktop-Apps Notarisierung": r"notarisieren",
    "Electron-Sicherheit": r"Electron",
    "Browser-Erweiterungen": r"Chrome Web Store",
    "KI-Telefonie § 7 UWG": r"§ 7a UWG",
    "Google CASA": r"CASA",
    "Religions-Apps Art. 9": r"Religion und Weltanschauung",
    "Transparenzregister": r"Transparenzregister",
    "Minderjährige Gründer § 112 BGB": r"§ 112 BGB",
    "Nebentätigkeit / Sozialleistungen": r"Nebentätigkeit",
    "US-Steuerformular W-8BEN": r"W-8BEN",
    "Künstlersozialabgabe": r"Künstlersozial",
    "Verkauf der App / Asset Deal": r"Verkauf der App",
    "Widerruf bei digitalen Dienstleistungen (§ 356 Abs. 5)": r"§ 356 Abs\. 5",
    "Kündigen ohne Login": r"Kündigen ohne Login",
    "Gratis-Test mit Bezahl-Button": r"C-400/22",
    "Produkthaftungsgesetz 09.12.2026": r"9\. Dezember 2026",
    "Kontaktstelle nicht nur Chatbot (Art. 12 DSA)": r"Art\. 12 DSA",
    "AI Washing": r"AI Washing",
    "KI-Agenten Art. 50": r"KI-Agenten geben sich als KI zu erkennen",
    "Kein KI-Verbraucher-Abo als Backend": r"Kein privates KI-Abo als Backend",
    "Vibe-Coding-Plattform privat": r"Vibe-Coding-Plattform privat",
    "Edge Functions verify_jwt": r"verify_jwt",
    "Versionen mit Sicherheitsupdates": r"Nur Versionen mit Sicherheitsupdates",
    "Apple Medizinprodukt-Status": r"Medizinprodukt-Status",
    "EU-Vertreter (Art. 27 DSGVO, Art. 13 DSA)": r"Art\. 13 DSA",
    "Apps einstellen: Abos beenden": r"Apple-Abos geordnet beenden",
    "Scheinselbstständigkeit": r"Scheinselbstständigkeit",
    "Arbeitgeberpflichten": r"Arbeitgeberpflichten",
    "Nachahmer und Fake-Apps": r"Fake-Apps",
    "Patentrisiko": r"Patentrisiko",
}

LEVELS = ("PFLICHT", "SOLLTE", "KANN")
ITEM_RE = re.compile(r"^- \[ \] `(PFLICHT|SOLLTE|KANN)` \*\*(.+?)\*\*", re.M)


def main() -> int:
    if not KAT.is_dir():
        print(f"FEHLER: Katalog nicht gefunden: {KAT}")
        return 1

    chapters = sorted(KAT.glob("[0-9][0-9]-*.md"))
    all_text = ""
    counts = collections.Counter()
    per_chapter = {}

    for f in chapters:
        t = f.read_text(encoding="utf-8")
        all_text += "\n" + t
        items = ITEM_RE.findall(t)
        per_chapter[f.name] = len(items)
        for lvl, _ in items:
            counts[lvl] += 1

        for line in t.splitlines():
            if line.startswith("- [ ]") and not ITEM_RE.match(line):
                ERRORS.append(f"{f.name}: Punkt ohne Standardformat: {line[:80]}")

        titles = collections.Counter(x[1].lower().rstrip(".,:") for x in items)
        for title, n in titles.items():
            if n > 1:
                ERRORS.append(f"{f.name}: doppelter Punkt '{title}'")

        letters = re.findall(r"^## ([A-Z])\. ", t, re.M)
        expected = [chr(65 + i) for i in range(len(letters))]
        if letters and letters != expected:
            ERRORS.append(f"{f.name}: Abschnitte nicht fortlaufend: {letters}")

        # Kapitel 15 (Sonderfälle) und 16 (Warnsignale statt typischer Fehler) sind bewusst anders aufgebaut.
        required_sections = ["## Nachweis"]
        if not f.name.startswith(("15-", "16-")):
            required_sections.append("## Typische Fehler beim Vibe-Coding")
        for required in required_sections:
            if required not in t:
                WARNINGS.append(f"{f.name}: Abschnitt '{required}' fehlt")

        if not t.endswith("\n"):
            ERRORS.append(f"{f.name}: kein Zeilenumbruch am Dateiende")

    for extra in ("README.md", "PRUEF-PROMPTS.md", "QUELLEN-UND-STAND.md", "VOLLSTAENDIGKEITSPRUEFUNG.md"):
        p = KAT / extra
        if not p.exists():
            ERRORS.append(f"Pflichtdatei fehlt: {extra}")
        else:
            all_text += "\n" + p.read_text(encoding="utf-8")

    # Themenabdeckung (nur Kapiteltexte zählen für Inhalte, Zusatzdateien helfen bei Rahmenwerken)
    missing = [name for name, rx in THEMEN.items() if not re.search(rx, all_text, re.I)]
    for name in missing:
        ERRORS.append(f"Thema fehlt im Katalog: {name}")

    # README-Zahlen gegen tatsächliche Anzahl
    total = sum(counts.values())
    readme = (KAT / "README.md").read_text(encoding="utf-8") if (KAT / "README.md").exists() else ""
    m = re.search(r"über (\d[\d.]*) abhakbare Prüfpunkte in (\d+) Kapiteln", readme)
    if m:
        claimed = int(m.group(1).replace(".", ""))
        if not (claimed <= total < claimed + 100):
            ERRORS.append(f"README nennt 'über {claimed}' Punkte, tatsächlich {total}")
        if int(m.group(2)) != len(chapters):
            ERRORS.append(f"README nennt {m.group(2)} Kapitel, tatsächlich {len(chapters)}")
    else:
        WARNINGS.append("README: Satz 'über N abhakbare Prüfpunkte in K Kapiteln' nicht gefunden")
    for f in chapters:
        if f"./{f.name}" not in readme:
            ERRORS.append(f"README verlinkt Kapitel nicht: {f.name}")

    # Alter des Prüfdatums
    q = (KAT / "QUELLEN-UND-STAND.md").read_text(encoding="utf-8") if (KAT / "QUELLEN-UND-STAND.md").exists() else ""
    months = {"Januar": 1, "Februar": 2, "März": 3, "April": 4, "Mai": 5, "Juni": 6, "Juli": 7,
              "August": 8, "September": 9, "Oktober": 10, "November": 11, "Dezember": 12}
    dm = re.search(r"\*\*Letzte Prüfung:\*\* (\d{1,2})\. (\w+) (\d{4})", q)
    if dm and dm.group(2) in months:
        last = dt.date(int(dm.group(3)), months[dm.group(2)], int(dm.group(1)))
        age = (dt.date.today() - last).days
        print(f"Letzte Prüfung laut QUELLEN-UND-STAND.md: {last.isoformat()} (vor {age} Tagen)")
        if age > 92:
            WARNINGS.append(f"Letzte Prüfung liegt {age} Tage zurück – Recherche fällig")
    else:
        ERRORS.append("QUELLEN-UND-STAND.md: 'Letzte Prüfung' nicht lesbar")

    print(f"Kapitel: {len(chapters)} | Prüfpunkte: {total} "
          f"(PFLICHT {counts['PFLICHT']}, SOLLTE {counts['SOLLTE']}, KANN {counts['KANN']})")
    print(f"Pflichtthemen abgedeckt: {len(THEMEN) - len(missing)} von {len(THEMEN)}")
    for w in WARNINGS:
        print(f"WARNUNG: {w}")
    for e in ERRORS:
        print(f"FEHLER: {e}")
    if ERRORS:
        return 1
    print("OK: Katalog vollständig nach Themenliste, Format und Struktur")
    return 0


if __name__ == "__main__":
    sys.exit(main())
