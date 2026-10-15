# FocusFlow – Release und Betrieb

## Releasephasen

### Interne Alpha

- Entwickler-/Testkonten
- keine bezahlte Werbung
- Kernablauf und Datenmodell stabilisieren
- negative RLS-Tests
- Crash- und Kostenmonitoring

### Geschlossene Beta

- kleine reale Zielgruppe
- Feedbackinterviews
- Aktivierung und Abbruch messen
- Support manuell auswerten
- KI-Funktion zunächst begrenzen oder separat freischalten

### Produktionsrelease

- Release Candidate einfrieren
- Staging-Migration und E2E
- Backup/Restore
- Store-Datenabgleich
- gestaffelter Rollout

## Releasecheckliste

### Produkt

- [ ] PRD-Akzeptanzkriterien
- [ ] Onboarding und Kernablauf
- [ ] echte Inhalte und Fehlermeldungen
- [ ] keine medizinischen Claims

### Technik

- [ ] produktiver Build
- [ ] Migrationen versioniert
- [ ] RLS/Grants geprüft
- [ ] App-Version N-1 berücksichtigt
- [ ] Offline/Retry
- [ ] Backup/Restore

### Security/Datenschutz

- [ ] Threat Model
- [ ] Admin-MFA
- [ ] Secrets/Dependencies geprüft
- [ ] Export und Löschung
- [ ] Anbieter-/SDK-Register
- [ ] Breach-/Incident-Prozess

### KI

- [ ] Gateway und Rate Limit
- [ ] Modell-/Prompt-Version
- [ ] Goldenset
- [ ] Kostenlimit
- [ ] Fallback/Kill Switch
- [ ] Transparenzhinweis

### Store

- [ ] Beschreibung entspricht Funktion
- [ ] Screenshots echte UI
- [ ] Datenschutzangaben abgeglichen
- [ ] Altersfreigabe
- [ ] Support-/Privacy-URLs
- [ ] Review-Konto und Notes
- [ ] Kontolöschung auffindbar

## Rollout

```text
interne Nutzer
→ 5 %
→ 20 %
→ 50 %
→ 100 %
```

Zwischen den Stufen prüfen:

- Crash-/Fehlerquote
- Login und Kernablauf
- Migration
- API-/KI-Kosten
- Supporttickets
- Datenschutz-/Security-Meldungen

## Rollback-Auslöser

- Fremdzugriff oder Datenleck
- Datenverlust
- fehlerhafte Migration
- Login/Kernablauf großflächig gestört
- unkontrollierte Kosten
- kritischer Store-/Compliance-Fehler

Rollback kann bedeuten:

- Release stoppen
- Feature Flag/Kill Switch
- vorherigen Client/Serverstand aktivieren
- schreibende Funktion deaktivieren
- Migration per Roll-forward korrigieren

## Monitoring

### Technisch

- Verfügbarkeit
- p95 API-Latenz
- Error-/Crashrate
- Authfehler
- Datenbank-/Storage-Auslastung
- Backupstatus

### Produkt

- Zeit bis erste Session
- Sessionstart/-abschluss
- Abbrüche
- D1/D7/D30 Retention
- Export-/Löschanfragen

### KI

- Erfolgsquote
- Schemafehler
- Latenz
- Token/Kosten
- Rate-Limit-Treffer
- Sicherheits-/Moderationsfälle

## Betriebsrhythmus

| Rhythmus | Fokus |
|---|---|
| täglich | Crash, Auth, Kernablauf, Kosten, offene Incidents |
| wöchentlich | Supportmuster, KI-Qualität, Jobs/Webhooks |
| monatlich | Abhängigkeiten, Adminrechte, RLS-Stichprobe, Löschjobs |
| quartalsweise | Restore-Test, Threat Model, Anbieter- und Kostenreview |
| halbjährlich | Accessibility, Datenflüsse, Exit-/Migrationsfähigkeit |
| jährlich | Recht, Stores, OS/API, Verträge, Supportzeitraum |

## Support

Support benötigt:

- klare Kontaktmöglichkeit
- Kategorien und Prioritäten
- keine Anforderung von Passwörtern oder Secrets
- Identitätsprüfung bei Kontodaten
- Eskalationsweg für Security/Datenschutz
- dokumentierte Reaktionsziele

## Fünf-Jahres-Plan

### Jahr 1

Produktfit, Stabilität, Support und Kosten verstehen.

### Jahr 2

Abhängigkeiten und Designsystem konsolidieren, Automatisierung erhöhen.

### Jahr 3

größere Framework-/OS-Upgrades, Architektur und Anbieter erneut bewerten.

### Jahr 4

Datenmodell, Performance, Accessibility und Security extern oder unabhängig prüfen.

### Jahr 5

bewusste Entscheidung: weiterentwickeln, migrieren, verkaufen oder geordnet beenden.

## Produktende

- neue Registrierungen stoppen
- Nutzer früh informieren
- Export ermöglichen
- Abos beenden
- Store-Einträge aktualisieren
- Daten nach Konzept löschen/aufbewahren
- Domains und Supporthinweise sichern
- Abschluss und Verantwortliche dokumentieren
