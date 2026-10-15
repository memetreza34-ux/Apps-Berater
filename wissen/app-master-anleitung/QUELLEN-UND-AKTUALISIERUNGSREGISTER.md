# Quellen- und Aktualisierungsregister

**Letzte Grundprüfung:** 4. August 2026

Dieses Register führt zeitabhängige Gesetze, Plattformregeln, Normen, technische Dokumentationen und Anbieterbedingungen. Es ist ein Startregister und wird pro App um die tatsächlich anwendbaren Quellen ergänzt.

## Grundregeln

- zeitabhängige Aussagen nur mit Primärquelle;
- Quelle, Version oder Abrufdatum dokumentieren;
- Gesetz, Plattformregel, Norm und Empfehlung klar trennen;
- alte Screenshots oder Blogartikel nicht als alleinige Grundlage verwenden;
- Änderungen auf Produkt, Technik, Daten, Rechtstexte und Betrieb übertragen;
- bei Unsicherheit fachkundige Prüfung einholen.

## Registerfelder

| ID | Thema | Quelle | Typ | geprüft am | nächste Prüfung | betroffene Kapitel | Status/Änderung |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## EU- und deutsches Recht – Startquellen

| ID | Thema | Offizielle Quelle | Hinweis |
|---|---|---|---|
| EU-DSGVO | Datenschutz-Grundverordnung | https://eur-lex.europa.eu/eli/reg/2016/679/oj | Zwecke, Rechtsgrundlagen, Betroffenenrechte, Sicherheit und Nachweise |
| EU-AIA | AI Act | https://eur-lex.europa.eu/eli/reg/2024/1689/oj | Anwendbarkeit und Zeitplan je KI-Funktion prüfen |
| EU-DSA | Digital Services Act | https://eur-lex.europa.eu/eli/reg/2022/2065/oj | relevant insbesondere bei Vermittlungsdiensten und Nutzerinhalten |
| EU-CRA | Cyber Resilience Act | https://digital-strategy.ec.europa.eu/en/policies/cra-reporting | Meldepflichten und weitere Produktpflichten nur bei Anwendbarkeit; EU-Kommission nennt Start der Meldepflichten am 11. September 2026 |
| DE-GESETZE | Deutsche Bundesgesetze | https://www.gesetze-im-internet.de/ | BDSG, DDG, TDDDG, BFSG und weitere anwendbare Gesetze in aktueller Fassung prüfen |
| EU-VERBRAUCHER | EU-Verbraucherrecht | https://commission.europa.eu/law/law-topic/consumer-protection-law_en | digitale Inhalte, Fernabsatz und Verbraucherinformationen je Geschäftsmodell prüfen |

Dieses Register ersetzt keine individuelle rechtliche Bewertung.

## Apple – Startquellen

| ID | Thema | Offizielle Quelle | Prüffrage |
|---|---|---|---|
| APPLE-REVIEW | App Review Guidelines | https://developer.apple.com/app-store/review/guidelines/ | Welche Funktionen, Inhalte, Käufe, Konten und Berechtigungen lösen Regeln aus? |
| APPLE-DELETE | Kontolöschung | https://developer.apple.com/support/offering-account-deletion-in-your-app | Erlaubt die App Konten, muss der aktuelle Löschweg geprüft werden? |
| APPLE-HIG | Human Interface Guidelines | https://developer.apple.com/design/human-interface-guidelines/ | Plattformkonventionen und Accessibility berücksichtigen |
| APPLE-PRIVACY | App Privacy | https://developer.apple.com/app-store/app-privacy-details/ | Stimmen Angaben mit realen SDKs und Datenflüssen überein? |
| APPLE-SUBSCRIPTIONS | Abonnements | https://developer.apple.com/app-store/subscriptions/ | Produkte, Laufzeiten, Restore, Kündigung und Serverstatus prüfen |

Bei Kontolöschung und aktivem Apple-Abo sind App-Konto und Store-Abonnement getrennt zu behandeln. Die aktuelle Apple-Dokumentation verlangt eine klare Information und einen erreichbaren Weg zur Aboverwaltung.

## Google Play – Startquellen

| ID | Thema | Offizielle Quelle | Prüffrage |
|---|---|---|---|
| GOOGLE-POLICY | Developer Program Policies | https://play.google.com/about/developer-content-policy/ | Welche Richtlinien gelten für Inhalt, Daten, Werbung und Monetarisierung? |
| GOOGLE-DATA | User Data Policy | https://support.google.com/googleplay/android-developer/answer/10144311 | Sind Datenschutz, Einwilligung, Datenangaben und Löschung korrekt? |
| GOOGLE-DELETE | Account Deletion | https://support.google.com/googleplay/android-developer/answer/13327111 | Gibt es den geforderten In-App- und externen Löschweg? |
| GOOGLE-DATA-SAFETY | Data Safety | https://support.google.com/googleplay/android-developer/answer/10787469 | Stimmen Console-Angaben mit App, SDKs und Datenschutztext überein? |
| GOOGLE-BILLING | Play Billing | https://developer.android.com/google/play/billing | Kauf-, Abo-, Restore- und Serverprozesse aktuell prüfen |

Google Play verlangt bei Apps mit Kontenerstellung einen auffindbaren Löschweg in der App und eine externe Webressource. Die zugehörigen Daten müssen grundsätzlich mitbehandelt werden; zulässige Aufbewahrung ist transparent zu erklären.

## Barrierefreiheit und UX

| ID | Thema | Offizielle Quelle | Nutzung |
|---|---|---|---|
| WCAG | Web Content Accessibility Guidelines 2.2 | https://www.w3.org/TR/WCAG22/ | Web- und allgemeine Accessibility-Prüfung |
| WAI-ARIA | ARIA Authoring Practices | https://www.w3.org/WAI/ARIA/apg/ | zugängliche Web-Komponentenmuster |
| EN-301-549 | Accessibility für ICT | aktuelle offizielle Ausgabe und nationale Umsetzung prüfen | Relevanz durch Markt, Vertrag oder Barrierefreiheitsrecht bestimmen |
| ISO-9241-210 | menschzentrierte Gestaltung | aktuelle ISO-Ausgabe prüfen | Prozessreferenz für nutzerzentrierte Entwicklung |

## Softwarequalität und Sicherheit

| ID | Thema | Offizielle Quelle | Nutzung |
|---|---|---|---|
| OWASP-ASVS | Application Security Verification Standard | https://owasp.org/www-project-application-security-verification-standard/ | Web-/Backend-Sicherheitsanforderungen risikobasiert auswählen |
| OWASP-MASVS | Mobile Application Security Verification Standard | https://mas.owasp.org/MASVS/ | mobile Sicherheitsanforderungen und Prüfbereiche |
| OWASP-MASTG | Mobile Application Security Testing Guide | https://mas.owasp.org/MASTG/ | konkrete mobile Testmethoden |
| NIST-SSDF | Secure Software Development Framework | https://csrc.nist.gov/Projects/ssdf | sicherer Entwicklungslebenszyklus |
| ISO-25010 | System- und Softwarequalität | aktuelle ISO-Ausgabe prüfen | Qualitätsmerkmale und Produktbewertung |
| ISO-27001 | Informationssicherheitsmanagement | aktuelle ISO-Ausgabe prüfen | je Risiko, Vertrag und Organisation relevant |
| ISO-27701 | Datenschutz-Informationsmanagement | aktuelle ISO-Ausgabe prüfen | je Datenumfang, Vertrag und Organisation relevant |

Normen werden nur dann als verpflichtend bezeichnet, wenn Gesetz, Vertrag, Ausschreibung, Branche oder interne Entscheidung dies tatsächlich auslöst.

## Technische Primärquellen

Für jedes verwendete Framework, SDK und Backend werden ausschließlich die aktuellen offiziellen Dokumentationen registriert:

| Komponente | Version | offizielle Dokumentation | Supportende | Upgradeprüfung | Ersatzweg |
|---|---|---|---|---|---|
| | | | | | |

Mindestens erfassen:

- Programmiersprache und Laufzeit;
- App-Framework;
- Build- und Paketwerkzeuge;
- Datenbank und Backend;
- Authentifizierung;
- Storage;
- KI-Modelle und APIs;
- Zahlungsanbieter;
- Analytics und Monitoring;
- E-Mail, Push und SMS;
- zentrale Abhängigkeiten.

## Prüfintervalle

- **vor jedem Release:** Store-, Daten-, Zahlungs- und Berechtigungsangaben;
- **monatlich:** kritische technische Abhängigkeiten und Security-Hinweise;
- **quartalsweise:** Anbieter, Kosten, Datenschutz, Export und Exit-Fähigkeit;
- **jährlich:** vollständige Rechts-, Normen-, Store- und Architekturprüfung;
- **anlassbezogen:** neue Länder, Zielgruppen, Funktionen, Datenarten, KI, Zahlungen oder Hardware.

## Änderungsprozess

```text
Quelle ändert sich
→ Änderung klassifizieren
→ betroffene App-Funktionen und Daten bestimmen
→ Produkt-/Technik-/Rechtstexte anpassen
→ Tests und Nachweise aktualisieren
→ gestaffelt veröffentlichen
→ Register mit Datum und Entscheidung ergänzen
```
