# Betriebshandbuch

## Produkt und Verantwortung

- App/Version:
- Betreiber:
- Product Owner:
- technische Verantwortung:
- Security/Privacy:
- Support:
- Zahlungs-/Finanzkontakt:
- externe Anbieter/Fachkontakte:
- Bereitschaft/Eskalation:

## Systemübersicht

```text
Client
→ Backend/API
→ Auth
→ Datenbank/Storage
→ Jobs/Webhooks
→ KI/Zahlung/E-Mail/Push
→ Analytics/Monitoring
```

- Architekturdiagramm:
- Produktions-URLs:
- Statusseite:
- Dashboards:
- Repositories:
- Runbooks:
- Anbieterregister:

## SLOs und Kernmetriken

| Metrik/SLO | Ziel | Alarm | Zeitraum | Dashboard | Verantwortlicher |
|---|---:|---:|---|---|---|
| | | | | | |

## Tägliche Kontrolle

- Crashes/Fehler;
- Auth;
- Kernablauf;
- Zahlungen/Webhooks;
- KI/Jobs;
- Missbrauch/Safety;
- Kosten;
- offene Incidents.

## Wöchentliche Kontrolle

- Supportmuster;
- Reviews;
- fehlgeschlagene Jobs;
- Aktivierung/Retention;
- Refunds/Churn;
- Security-/Anbieterhinweise;
- offene technische Schulden.

## Monatliche Kontrolle

- Abhängigkeiten/Updates;
- Adminrechte/MFA;
- Daten-/RLS-/Autorisierungstest;
- Lösch-/Exportjobs;
- Backups;
- Kosten/Profitabilität;
- Anbieterlimits;
- Dokumentation/Runbooks.

## Quartalsweise Kontrolle

- Restore-Test;
- Incident-Übung;
- Threat Model;
- Anbieter-/Exit-Review;
- Performance-/Kapazitätsreview;
- Datenschutz-/Datenflussabgleich;
- Marketing-/Produktmetriken.

## Jährliche Kontrolle

- Recht/Normen/Store-Regeln;
- Framework-/OS-/Browser-Support;
- Verträge/DPAs;
- Gesamtarchitektur;
- End-of-Life-/Migration;
- Supportzeitraum;
- vollständige Qualitätsbewertung.

## Backups und Recovery

- Systeme:
- Frequenz:
- Aufbewahrung:
- Verschlüsselung:
- RPO:
- RTO:
- Restore-Schritte:
- letzter Test:
- Ergebnis:
- Verantwortlicher:

## Deployment und Rollback

- Umgebungen:
- Freigabeschritte:
- Migrationen:
- Feature Flags:
- gestaffelter Rollout:
- Rollback:
- Kommunikationsweg:
- Nachkontrolle:

## Incident-Prozess

```text
Erkennen
→ eindämmen
→ Auswirkung bewerten
→ Verantwortung/Eskalation
→ beheben/wiederherstellen
→ Kommunikation/Meldung
→ Ursachenanalyse
→ Maßnahmen
```

| Incidenttyp | Alarm/Quelle | erste Maßnahme | Verantwortlicher | Runbook | externe Meldung/Kommunikation |
|---|---|---|---|---|---|
| | | | | | |

## Support

- Kanäle:
- Servicezeiten:
- Prioritäten:
- Antwortziele:
- Identitätsprüfung:
- zulässiger Datenzugriff:
- Refund-/Zahlungsfälle:
- Moderation/Safety:
- Wissensdatenbank:
- Eskalation:

## Kosten und Limits

| Anbieter/Feature | Budget | Warnschwelle | hartes Limit | Notfallaktion | Verantwortlicher |
|---|---:|---:|---:|---|---|
| | | | | | |

## Updates und Abhängigkeiten

| Komponente | Version | Supportende | Risiko | Testplan | Upgrade-/Ersatztermin |
|---|---|---|---|---|---|
| | | | | | |

## Daten und Löschung

- Dateninventar:
- Exportprozess:
- Löschprozess:
- Backups:
- Anbieter:
- Audit:
- Aufbewahrungsjobs:
- regelmäßiger Test:

## Skalierung

- aktuelle Grenzen:
- gemessener Engpass:
- Kapazitätsmodell:
- Kostenfolge:
- geplante Änderung:
- Test/Rollback:

## Anbieterwechsel

- kritische Abhängigkeiten:
- Exportformate:
- Alternativen:
- Migrationszeit:
- Doppelbetrieb:
- Vertrags-/Löschabschluss:

## End-of-Life

- Auslöser:
- Entscheidungsverantwortlicher:
- Kommunikationsfrist:
- Kündigung/Refund:
- Datenexport:
- Datenlöschung:
- Store-/Domainstatus:
- Quellcode/Archiv:
- Sicherheitsupdates bis:
- Abschlussnachweis:
