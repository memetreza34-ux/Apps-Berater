# 09 – Performance, Analytics und Observability

Eine App kann funktional korrekt und trotzdem unbrauchbar sein. Performance, Messbarkeit und Fehlererkennung gehören deshalb in die Produktarchitektur.

## Performance-Budgets vor der Optimierung

Lege je Plattform messbare Ziele fest:

| Bereich | Beispielhafte Messgröße |
|---|---|
| Start | Zeit bis nutzbarer Kernscreen |
| Interaktion | Reaktion auf Tap/Klick |
| Navigation | Screenwechsel ohne sichtbares Stocken |
| API | p50/p95-Latenz und Fehlerrate |
| Bilder | maximale Dateigröße und responsive Varianten |
| Bundle | Download- und Parse-Größe |
| Speicher | typische und maximale Nutzung |
| Akku/Netz | Hintergrundaktivität und Übertragungsmenge |
| KI | Zeit bis erstes Ergebnis, Gesamtlatenz, Abbruchrate |

Die konkreten Grenzwerte hängen vom Produkt ab. Entscheidend ist: messen, budgetieren und Regressionen blockieren.

## Typische Performance-Ursachen

- zu viele Requests beim Start;
- große Bilder oder Fonts;
- nicht paginierte Listen;
- N+1-Abfragen;
- fehlende Indizes;
- unnötige Re-Renders;
- synchroner schwerer Code im UI-Thread;
- zu große lokale Datenbestände;
- KI-Aufruf ohne Streaming, Timeout oder Abbruch;
- unkontrolliertes Logging und Analytics.

## Optimierungsreihenfolge

1. echtes Nutzerproblem messen;
2. reproduzierbaren Benchmark bauen;
3. größte Ursache finden;
4. kleinste wirksame Änderung;
5. vorher/nachher messen;
6. Regressionstest oder Budget ergänzen.

## Produktanalytics

Nur Ereignisse erfassen, die eine Entscheidung unterstützen.

Gutes Event-Schema:

```text
object_action_result
project_created_success
focus_session_started_success
account_deletion_failed
```

Für jedes Event dokumentieren:
- Produktfrage;
- Auslöser;
- Eigenschaften;
- personenbezogene Daten;
- Aufbewahrung;
- Einwilligung/Rechtsgrundlage;
- Besitzer des Dashboards.

## Kernmetriken

- Aktivierung
- D1/D7/D30-Retention
- Erfolg des Kernablaufs
- Abbruch je Schritt
- Crash- und Fehlerquote
- Conversion/Churn
- Supportfälle pro 1.000 Nutzer
- Kosten pro aktivem Nutzer
- KI-Kosten pro erfolgreichem Ergebnis

## Observability

Drei Ebenen getrennt betrachten:

### Logs
Für konkrete technische Ereignisse. Keine Passwörter, Tokens, vollständigen Prompts, Zahlungsdaten oder unnötigen personenbezogenen Inhalte.

### Metriken
Aggregierte Zustände wie Latenz, Fehlerrate, Queue-Länge, Kosten und Erfolgsquote.

### Traces
Zusammenhang eines Ablaufs über Client, API, Datenbank und Drittanbieter.

## Alarmregeln

Ein Alarm braucht:
- klare Schwelle;
- Zeitraum;
- Schweregrad;
- verantwortliche Person;
- Runbook;
- Eskalation;
- Entwarnungskriterium.

Keine Alarme für alles. Alarmieren, wenn Nutzer oder Daten gefährdet sind oder rasches Handeln erforderlich ist.

## SLOs

Beispiele:
- 99,9 % erfolgreiche Authentifizierungsanfragen;
- 99,5 % erfolgreicher Kernablauf;
- p95-API-Latenz unter projektspezifischem Ziel;
- Kontolöschjob innerhalb definierter Frist;
- kritischer Alarm innerhalb definierter Reaktionszeit bestätigt.

## Kostenkontrolle

- Budgets je Anbieter;
- Warnung bei ungewöhnlichem Wachstum;
- harte Limits für KI/Medien;
- Kosten pro Nutzer und Feature;
- automatische Abschaltung nichtkritischer teurer Funktionen;
- manueller Notfall-Schalter.

## Release-Gate

- Performance-Budgets dokumentiert und auf echten Geräten gemessen.
- Kernmetriken und Event-Schema freigegeben.
- Datenschutzabgleich für Analytics erfolgt.
- Crash-, API-, Auth-, Zahlungs- und KI-Fehler sichtbar.
- mindestens ein Alarm mit Runbook getestet.
- Kostenlimit und Rollback vorhanden.
