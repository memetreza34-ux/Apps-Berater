# 15 – Betriebs- und Notfall-Runbooks

Ein Alarm ohne Handlungsanweisung ist nur Lärm. Für jeden kritischen Systemteil existiert ein kurzes, getestetes Runbook.

## Verfügbare Runbooks

- [Auth-Ausfall](./auth-ausfall.md)
- [Datenbankmigration und Rollback](./datenbankmigration-und-rollback.md)
- [KI-Anbieter-Ausfall und Kostenanomalie](./ki-anbieter-ausfall.md)
- [Security- und Datenschutzvorfall](./security-und-datenschutzvorfall.md)

## Standardaufbau

Jedes Runbook enthält:

1. Auslöser und Schweregrad;
2. erste fünf Minuten;
3. Eindämmung;
4. Diagnose;
5. Kommunikation;
6. Wiederherstellung;
7. Nachweis und Postmortem;
8. Testintervall.

## Verantwortlichkeiten

| Rolle | Aufgabe |
|---|---|
| Incident Lead | koordiniert und entscheidet |
| Technical Lead | Diagnose, Eindämmung, Wiederherstellung |
| Privacy/Security | Daten- und Meldebewertung |
| Communications | Nutzer-, Partner- und Statusinformation |
| Scribe | Zeitlinie, Entscheidungen und Belege |

Bei Einzelentwicklern bleiben die Rollen getrennte Prüfperspektiven, auch wenn eine Person mehrere Aufgaben übernimmt.

## Übungsregel

- kritische Runbooks mindestens quartalsweise als Tabletop-Übung;
- Backup/Restore und Rollback praktisch testen;
- Kontaktdaten, Zugänge und Anbieterwege nach jeder Änderung aktualisieren;
- jede Übung endet mit konkreten Verbesserungen und Verantwortlichen.
