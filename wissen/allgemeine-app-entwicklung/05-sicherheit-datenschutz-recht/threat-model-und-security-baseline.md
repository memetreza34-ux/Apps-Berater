# Threat Model und Security-Baseline

## Ziel

Security wird vor der Implementierung kritischer Funktionen geplant und anschließend durch konkrete Tests nachgewiesen.

## Assets bestimmen

Typische Assets:

- Nutzerkonten und Sessions
- personenbezogene Inhalte
- Zahlungs- und Abodaten
- Admin- und Supportrechte
- API-Schlüssel und Signing Keys
- Quellcode und CI/CD
- Backups
- KI-Werkzeuge und Kostenbudget
- Ruf und Verfügbarkeit des Produkts

## Bedrohungsanalyse

Für jedes Asset dokumentieren:

| Feld | Frage |
|---|---|
| Angreifer | Wer könnte angreifen? |
| Einstieg | Über welchen Client, API, Upload, Anbieter oder Mitarbeiter? |
| Ziel | Lesen, Ändern, Löschen, Missbrauchen oder Ausfallen lassen? |
| Auswirkung | Nutzer, Geld, Recht, Betrieb, Vertrauen? |
| Prävention | Welche Kontrolle verhindert den Angriff? |
| Erkennung | Woran wird der Angriff bemerkt? |
| Reaktion | Wie wird eingedämmt und wiederhergestellt? |
| Test | Wie wird die Kontrolle nachgewiesen? |

## STRIDE als Denkstütze

- **Spoofing:** Identität vortäuschen
- **Tampering:** Daten verändern
- **Repudiation:** Aktion abstreiten
- **Information Disclosure:** Daten offenlegen
- **Denial of Service:** Dienst stören
- **Elevation of Privilege:** Rechte ausweiten

STRIDE ist kein Pflichtformat. Entscheidend ist, dass reale Produkt- und Datenflüsse vollständig betrachtet werden.

## Mindestbaseline

### Identität

- E-Mail-/Telefonverifikation entsprechend Risiko
- MFA für Admins
- sichere Passwort-/Account-Recovery
- Rate Limits und Bot-Schutz
- Sessions widerrufbar
- keine unnötige Nutzererkennung durch Fehlermeldungen

### Autorisierung

- serverseitig oder in der Datenbank
- pro Ressource und Aktion
- Mandant und Eigentümer prüfen
- negative Tests mit mehreren Rollen
- Supportzugriff zeitlich und nachvollziehbar

### Eingaben und Dateien

- Typ, Länge und Wertebereich validieren
- serverseitige Prüfung
- Uploadgröße und Dateityp begrenzen
- Dateinamen nicht vertrauen
- aktive Inhalte und Malware entsprechend Risiko prüfen
- Inhalte sicher ausgeben

### Secrets

- keine Secrets in Repository, Client-Bundle, Chat, Screenshot oder Log
- getrennte Schlüssel pro Umgebung
- minimale Rechte
- Rotation und Widerruf
- automatische Secret-Scans

### Abhängigkeiten

- Lockfiles
- bekannte Herkunft
- aktive Wartung
- Lizenzprüfung
- Schwachstellenscan
- Updates mit Tests statt blindem Auto-Merge

### Logs

- Ereignis, Zeitpunkt, System und technische Kennung
- keine unnötigen Inhaltsdaten
- Schutz vor Manipulation
- Zugriff begrenzen
- Aufbewahrung festlegen
- Alarmierung für kritische Muster

## Abuse Cases

Neben technischen Angriffen prüfen:

- Spam und Bot-Accounts
- Belästigung und illegale Inhalte
- Gutschein-/Abo-Missbrauch
- Massenscraping
- KI-Kostenmissbrauch
- automatisierte Accountübernahme
- absichtliche Falschmeldungen
- Support-Manipulation

## Incident-Ablauf

```text
Erkennen
→ Schweregrad bestimmen
→ Eindämmen
→ Beweise sichern
→ Daten-/Meldepflicht bewerten
→ Nutzer/Partner informieren
→ Beheben
→ Wiederherstellen
→ Postmortem
→ Regressionstest
```

## Release-Blocker

- fremder Datenzugriff möglich
- Secret im Client/Repository
- keine Wiederherstellung kritischer Daten
- Admin ohne MFA
- unkontrollierter öffentlicher Upload
- keine Rate Limits für teure Aktionen
- kritische bekannte Schwachstelle
- fehlender Incident-Owner

## Security-Gate

- [ ] Threat Model aktuell
- [ ] Rollen-/Berechtigungsmatrix
- [ ] Auth- und Recoverytests
- [ ] Autorisierungs-Negativtests
- [ ] Secret- und Dependency-Scan
- [ ] Upload-/Missbrauchstests
- [ ] Logging und Alarmierung
- [ ] Backup/Restore
- [ ] Incident-Prozess und Kontakte
- [ ] offene Restrisiken akzeptiert und dokumentiert
