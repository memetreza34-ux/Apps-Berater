# Verifizierter Rechts- und Plattformstand – August 2026

**Prüfdatum:** 4. August 2026  
**Zweck:** Zeitabhängige Kernaussagen für die erste Ausgabe. Vor jedem Release erneut anhand der verlinkten Primärquellen prüfen.

## AI Act

Offizielle EU-Kommissionsquellen nennen aktuell:

- allgemeine Anwendbarkeit seit 2. August 2026, mit gestaffelten Ausnahmen;
- Verbote, Definitionen und KI-Kompetenzpflichten seit 2. Februar 2025;
- Governance und Pflichten für General-Purpose-AI seit 2. August 2025;
- Regeln für bestimmte Hochrisiko-Anwendungsfälle ab 2. Dezember 2027;
- Regeln für Hochrisiko-KI in regulierten physischen Produkten ab 2. August 2028.

Primärquellen:

- https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- https://digital-strategy.ec.europa.eu/en/faqs/navigating-ai-act
- https://eur-lex.europa.eu/eli/reg/2024/1689/oj

Projektfolge:

- jede KI-Funktion einzeln klassifizieren;
- Rolle des Betreibers/Anbieters bestimmen;
- Transparenz, Kompetenz, Daten, Aufsicht und Risikokontrollen dokumentieren;
- bei Hochrisiko- oder unklarer Einordnung Fachprüfung einholen;
- Zeitplan und spätere Leitlinien/Normen regelmäßig aktualisieren.

## Cyber Resilience Act

Die EU-Kommission nennt für Produkte mit digitalen Elementen, soweit die App/Software in den Anwendungsbereich fällt:

- Meldepflichten für aktiv ausgenutzte Schwachstellen und schwere Sicherheitsvorfälle ab 11. September 2026;
- Frühwarnung grundsätzlich innerhalb von 24 Stunden nach Kenntnis;
- vollständige Meldung grundsätzlich innerhalb von 72 Stunden;
- weitere Abschlussberichte nach den aktuellen Vorgaben.

Primärquellen:

- https://digital-strategy.ec.europa.eu/en/policies/cra-reporting
- https://eur-lex.europa.eu/eli/reg/2024/2847/oj

Projektfolge:

- Scope/Herstellerrolle prüfen;
- Schwachstellen- und Incidentprozess;
- Kontakt- und Meldeverantwortung;
- Update-/Supportzeitraum;
- SBOM/Abhängigkeiten;
- sichere Updates;
- Nachweise und Runbooks.

## Apple – Konten und Löschung

Die aktuellen App Review Guidelines verlangen grundsätzlich:

- Apps ohne wesentliche kontobasierte Funktion sollen nicht unnötig Login erzwingen;
- Apps mit Kontenerstellung müssen Kontolöschung innerhalb der App anbieten;
- personenbezogene Daten dürfen nur verlangt werden, wenn sie für Kernfunktion oder Recht erforderlich sind.

Primärquelle:

- https://developer.apple.com/app-store/review/guidelines/
- https://developer.apple.com/support/offering-account-deletion-in-your-app

Projektfolge:

- In-App-Löschweg;
- Löschung der zugehörigen Appdaten;
- verständliche Ausnahmen/Aufbewahrung;
- aktives Store-Abo getrennt erklären und verwalten;
- Review- und Datenschutzangaben mit realem Ablauf abgleichen.

## Google Play – Konten und Löschung

Die aktuelle Google-Play-User-Data-Policy verlangt bei Apps, die Kontenerstellung ermöglichen:

- auffindbaren Löschweg in der App;
- zusätzlich eine externe Webressource für die Löschanfrage;
- Löschung der mit dem Konto verbundenen Appdaten;
- Deaktivieren oder Einfrieren gilt nicht als Kontolöschung;
- zulässige Aufbewahrung muss transparent erklärt werden;
- Data-Safety-Angaben müssen dem tatsächlichen Datenfluss entsprechen.

Primärquellen:

- https://support.google.com/googleplay/android-developer/answer/10144311
- https://support.google.com/googleplay/android-developer/answer/13327111

Projektfolge:

- In-App- und Webweg testen;
- Drittanbieter/Serviceprovider in Löschung einbeziehen;
- Support- und Identitätsprüfung;
- aktive Abos getrennt behandeln;
- funktionierende URL in Play Console;
- regelmäßiger Abgleich mit Data Safety.

## Pflegehinweis

Diese Datei ist eine Momentaufnahme. Bei Änderungen werden:

```text
Quelle und Datum aktualisiert
→ betroffene Kapitel markieren
→ Produkt-/Technikfolge bestimmen
→ Vorlagen und Tests anpassen
→ Release-/Storeangaben prüfen
→ Änderungsnotiz ergänzen
```
