# 06 – Tests, Release und langfristiger Betrieb

## 1. Testebenen

| Ebene | Zweck |
|---|---|
| Unit | Regeln, Berechnungen und Validierung |
| Integration | Datenbank, Auth, Storage, APIs, Zahlungen und KI |
| E2E | vollständige reale Nutzerabläufe |
| Security | Autorisierung, Secrets, Uploads und Missbrauch |
| Accessibility | Screenreader, Fokus, Textgröße und Kontrast |
| Performance | Start, Interaktion, Netzwerk, Speicher und Akku |
| Recovery | Offline, Retry, Backup, Restore und Rollback |

## 2. Testdaten

Testdaten müssen synthetisch, reproduzierbar und rollenübergreifend sein. Prüfe zusätzlich:

- leere und sehr große Accounts
- verschiedene Sprachen und Zeitzonen
- lange Texte, Emojis und Sonderzeichen
- schlechte oder fehlende Netzwerkverbindung
- abgelaufene Sessions
- Gerätewechsel
- fehlgeschlagene Zahlungen und Webhooks

## 3. Pflicht-Negativtests

- Nutzer A liest Daten von Nutzer B.
- Nutzer A ändert oder löscht Daten von Nutzer B.
- unauthentifizierter direkter API-Aufruf.
- manipulierte Nutzer- oder Mandanten-ID.
- normale Rolle ruft Adminfunktion auf.
- Upload mit falschem Typ oder zu großer Datei.
- KI-Endpunkt ohne Budget oder Rate Limit.

## 4. Produktionsreife

Ein Release Candidate benötigt:

- versionierte Migrationen
- Staging-Test
- Backup und tatsächlichen Restore-Test
- vollständigen Kernablauf
- Security-/Datenschutzprüfung
- Accessibility-Review
- Performance-Budget
- Monitoring und Alarme
- Supportprozess
- Rollback

## 5. Store-Release

### Apple

- Signierung und Entitlements
- App-Privacy-Angaben
- Datenschutzerklärung
- Kontolöschung in der App, wenn Konten erstellt werden
- Käufe und Abos
- Altersfreigabe
- Review Notes und Review-Konto
- funktionierende Support- und Datenschutz-URLs

### Google Play

- App Signing und AAB
- aktuelle Target-API-Anforderung
- Data Safety
- In-App- und externer Löschweg
- Zielgruppe und Content Rating
- aktuelle Testanforderungen des Kontos
- Play Billing
- Pre-Launch-Report

### Web

- HTTPS und Security Header
- Domain- und Account-Recovery
- Impressum und Datenschutz
- Consent entsprechend den tatsächlich aktiven Technologien
- Kündigungs- und Vertragsprozesse
- Status- und Supportweg

Store-Regeln werden vor jedem Release neu geprüft und nicht aus alten Erinnerungen übernommen.

## 6. Gestaffelter Rollout

1. interne Tester
2. kleine geschlossene Beta
3. kleiner Produktionsanteil
4. Fehler-, Auth-, Kosten- und Supportdaten beobachten
5. nur bei Stabilität ausweiten
6. bei kritischem Fehler stoppen oder zurückrollen

## 7. Betriebskalender

| Rhythmus | Prüfung |
|---|---|
| täglich | Crashes, Kernablauf, Auth, Zahlungen, Missbrauch, Kosten |
| wöchentlich | Supportmuster, Jobs, Webhooks, Reviews und Backlog |
| monatlich | Abhängigkeiten, Adminrechte, RLS, Löschjobs, Kosten |
| quartalsweise | Restore-Test, Anbieterreview, Threat Model, Incident-Übung |
| halbjährlich | Datenflüsse, Accessibility, Export und Anbieterwechsel |
| jährlich | Gesetze, Store-Regeln, OS/API, Verträge und Gesamtrisiko |

## 8. Skalierungsstufen

### Bis 100 aktive Nutzer

- Produktlernen und direkter Support
- einfache Architektur
- manuelle Kontrollen möglich

### Bis 1.000

- Kostenalarme
- saubere Pagination und Indizes
- Background Jobs
- strukturierter Support

### Bis 10.000

- Lasttests
- Serviceziele
- Kapazitätsplanung
- automatisierter Missbrauchsschutz
- klarer Incident-Dienst

### Darüber

Nur nach Messdaten zusätzliche Komplexität einführen: Read Scaling, Partitionierung, Redundanz, formale Change-Prozesse und externe Security-Prüfungen.

## 9. Produktende

Auch eine Abschaltung wird geplant:

- Ankündigungsfrist
- Datenexport
- Ende von Abos und Registrierungen
- Datenlöschung oder Migration
- Supportende
- gesetzliche Aufbewahrung
- Store-, Domain- und Statushinweise
