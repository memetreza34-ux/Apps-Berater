# Runbook – Datenbankmigration und Rollback

## Auslöser

- Migration schlägt fehl;
- erhöhte DB-Fehler oder Latenz;
- Daten fehlen oder sind falsch transformiert;
- alte App-Versionen funktionieren nicht mehr;
- RLS/Grants verhalten sich unerwartet.

## Vor jeder Migration

- Backup und Wiederherstellungsweg geprüft;
- Migration auf realistischem Staging-Datensatz;
- erwartete Laufzeit und Locks;
- Vorwärts- und Rückwärtskompatibilität;
- Backfill getrennt von Schemaänderung, wenn riskant;
- Stop-/Rollbackkriterium;
- verantwortliche Person und Beobachtungsfenster.

## Erste fünf Minuten bei Fehler

1. Weitere Deployments stoppen.
2. Schreibintensive oder betroffene Funktion per Feature Flag begrenzen.
3. Zeitpunkt, Migration und beobachtete Symptome sichern.
4. Datenbank nicht durch spontane manuelle Änderungen weiter verändern.
5. Prüfen, ob Roll-forward sicherer ist als Rollback.

## Entscheidung

### Roll-forward
Geeignet, wenn:
- Schema bereits von neuen Writes genutzt wird;
- Rücknahme Daten verlieren würde;
- ein kleiner korrigierender Patch genügt.

### Rollback
Geeignet, wenn:
- alte Version weiterhin kompatibel ist;
- keine irreversiblen Writes stattgefunden haben;
- Wiederherstellung getestet ist;
- Ausfallzeit und Datenverlust innerhalb RPO/RTO bleiben.

## Wiederherstellung

- Schema und Datenkonsistenz prüfen;
- RLS/Grants mit Nutzer A/B negativ testen;
- Kernablauf und alte Clientversion testen;
- Queue/Webhooks/Jobs kontrolliert wieder starten;
- Datenabgleich und Stichproben dokumentieren;
- Monitoring bis nach Beobachtungsfenster erhöhen.

## Beweise

- Backup-ID und Zeitpunkt;
- Migrations-/Rollback-Logs;
- Datenkonsistenzabfragen;
- Testprotokolle;
- gemessener Datenverlust und Ausfall;
- Freigabe zur Wiederaufnahme.

## Nacharbeit

- fehlender Test oder falsche Annahme;
- neue Guardrail/CI-Prüfung;
- verbesserte Expand-Migrate-Contract-Reihenfolge;
- aktualisierte RPO/RTO- und Kapazitätsplanung.
