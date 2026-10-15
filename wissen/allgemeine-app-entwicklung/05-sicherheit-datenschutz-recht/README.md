# 05 – Security, Datenschutz und Recht

## Ziel

Sicherheit und Datenschutz werden als technische Systeme gebaut. Ein Impressum oder eine Datenschutzerklärung allein macht keine App sicher oder compliant.

## 1. Threat Model

Für jedes wichtige Asset dokumentieren:

- möglicher Angreifer
- Angriffsweg
- Auswirkung
- Wahrscheinlichkeit
- Prävention
- Erkennung
- Reaktion
- Test

Wichtige Assets sind unter anderem Accounts, personenbezogene Daten, Zahlungsstatus, Adminfunktionen, API-Schlüssel, KI-Budgets und Backups.

## 2. Security-Baseline

### Identität

- MFA für Admins
- sichere Account-Recovery
- Rate Limits und Brute-Force-Schutz
- Sessions und Gerätewechsel testen

### Autorisierung

- serverseitig pro Ressource
- Eigentums- und Mandantenprüfung
- negative Tests
- minimale Adminrechte

### Secrets

- Secret Manager oder geschützte Servervariablen
- Rotation
- keine Secrets in Git, App-Bundle, Screenshots oder Logs

### API und Uploads

- Eingabevalidierung
- Größen- und Dateityplimits
- sichere Fehlerausgaben
- Rate Limits
- Idempotenz bei Zahlungen und Aktionen
- Missbrauchsschutz

### Lieferkette

- Lockfiles
- gepflegte Abhängigkeiten
- Schwachstellen- und Lizenzprüfung
- reproduzierbare Builds soweit praktikabel

## 3. Datenschutz by Design

Für jede Datenart dokumentieren:

- betroffene Person
- Quelle
- Zweck
- Rechtsgrundlage
- Empfänger
- Region/Transfer
- Aufbewahrung
- Löschung
- Schutz
- besonderes Risiko

Prüfe jedes Datenfeld: Ist es für die aktuelle Funktion wirklich erforderlich?

## 4. Betroffenenrechte technisch vorbereiten

- Auskunft
- Berichtigung
- Export
- Löschung
- Einschränkung/Widerspruch
- Einwilligungswiderruf
- nachvollziehbare Identitätsprüfung

Kontolöschung umfasst auch Storage, Suchindizes, Caches, KI-/Analytics-/E-Mail-Anbieter, abgeleitete Daten und dokumentierte Backup-Fristen.

## 5. SDK- und Anbieterregister

Für jeden Anbieter:

- Dienst und Zweck
- Daten
- Berechtigungen
- Startzeitpunkt
- Einwilligung
- Region
- Vertrag/DPA
- Subprozessoren
- Löschung
- Store-Angaben
- Exit-Plan

## 6. Rechtliche Klassifizierung

Nicht jedes Regelwerk trifft jede App. Für jedes relevante Thema wird `Ja`, `Nein` oder `Offen` mit Begründung, Maßnahme, Verantwortlichem, Beleg und Prüfdatum dokumentiert.

Typische Trigger:

| Bereich | Auslöser |
|---|---|
| DSGVO | personenbezogene Daten |
| Endgerätezugriff/Tracking | nicht notwendige SDKs, Identifier, Cookies oder ähnliche Zugriffe |
| Anbieterkennzeichnung | geschäftsmäßiger digitaler Dienst |
| Verbraucherrecht | B2C-Vertrag, Abo oder digitale Leistung |
| Barrierefreiheit | bestimmte Verbraucherdienste und E-Commerce-Funktionen |
| EU AI Act | KI-Systeme |
| DSA | Hosting, Nutzerinhalte oder Plattformfunktionen |
| CRA | Produkte mit digitalen Elementen im Anwendungsbereich |
| Medizinrecht | medizinische Zweckbestimmung |
| Finanzaufsicht | regulierte Zahlungs-, Kredit- oder Anlageleistung |

## 7. Hochrisikobereiche

Vor Entwicklung fachkundig prüfen:

- Diagnose, Therapie, Dosierung oder medizinische Überwachung
- personalisierte Anlage-/Kreditentscheidung
- Biometrie und Emotionserkennung
- Kinder und Minderjährige
- Arbeitgeber- oder Leistungsüberwachung
- sicherheitskritische Hardware
- Hochrisiko-KI

Ein Disclaimer ändert nicht automatisch die tatsächliche Zweckbestimmung einer App.

## 8. Incident-Prozess

```text
Erkennen → Triage → Eindämmen → Bewerten → Melden → Beheben → Postmortem
```

Vor dem Vorfall müssen Owner, Kontakte, Beweissicherung, Kommunikationsvorlagen und gesetzliche Entscheidungswege feststehen.

## Gate 4 – Sicherheits- und Compliance-Freigabe

- [ ] Threat Model aktuell
- [ ] Autorisierungs-Negativtests bestanden
- [ ] Secrets und Abhängigkeiten geprüft
- [ ] Dateninventar und Löschkonzept aktuell
- [ ] Anbieter und SDKs vollständig dokumentiert
- [ ] Datenschutzerklärung und Store-Angaben entsprechen der realen App
- [ ] Incident-Prozess und Kontakte vorhanden
- [ ] offene Rechtsfragen mit Verantwortlichem und Frist dokumentiert
