# Runbook – Security- und Datenschutzvorfall

## Auslöser

- unbefugter Datenzugriff oder Datenabfluss;
- verlorene oder veröffentlichte Secrets;
- manipulierte Accounts oder Adminzugänge;
- ungewöhnliche Exporte, Löschungen oder Rechteänderungen;
- aktiv ausgenutzte Schwachstelle;
- Sicherheitsmeldung eines Nutzers oder Forschers.

## Erste fünf Minuten

1. Incident Lead bestimmen und Zeitlinie starten.
2. Beweise sichern, ohne Systeme unnötig zu verändern.
3. Zugang oder Funktion gezielt eindämmen.
4. kompromittierte Secrets/Tokens rotieren oder widerrufen.
5. Datenschutz-, Security- und Geschäftsverantwortliche informieren.
6. Keine voreilige öffentliche Ursache behaupten.

## Eindämmung

- betroffene Konten/Sessions sperren;
- Adminrechte prüfen und reduzieren;
- Feature oder Endpoint per Kill Switch abschalten;
- Netzwerk-, RLS-, Storage- oder API-Regel korrigieren;
- Audit- und Providerlogs sichern;
- betroffene Datenarten, Personen, Länder und Zeiträume bestimmen.

## Bewertung

Dokumentiere:
- Art und Umfang der Daten;
- Anzahl und Gruppen Betroffener;
- Vertraulichkeits-, Integritäts- und Verfügbarkeitsfolgen;
- mögliche physische, finanzielle oder soziale Folgen;
- laufende Ausnutzung;
- gesetzliche, vertragliche, Store- oder CRA-Meldewege;
- Fristen und verantwortliche Entscheider.

Meldepflichten niemals anhand einer pauschalen Checkliste allein entscheiden. Bei relevantem Risiko fachkundige Datenschutz-/Rechtsprüfung einbeziehen.

## Kommunikation

- eine verifizierte Quelle der Wahrheit;
- Status, Auswirkung, sichere Nutzermaßnahmen und nächstes Update;
- keine sensiblen technischen Details veröffentlichen, die Missbrauch erleichtern;
- Support erhält abgestimmte Antworten;
- Behörden, Anbieter und Partner nach dokumentierter Entscheidung informieren.

## Wiederherstellung

1. Ursache beheben und Regressionstest erstellen.
2. kompromittierte Identitäten/Keys vollständig rotieren.
3. Datenintegrität und Berechtigungen prüfen.
4. Staging- und negative Autorisierungstests.
5. gestaffelte Wiederaufnahme mit erhöhtem Monitoring.
6. Betroffene Schutzmaßnahmen und Support bereitstellen.

## Postmortem

- sachliche Zeitlinie;
- technische und organisatorische Ursachen;
- warum Prävention/Erkennung/Reaktion nicht genügte;
- Daten- und Nutzerfolgen;
- verbindliche Maßnahmen mit Termin und Owner;
- aktualisiertes Threat Model, Tests und Runbook;
- Prüfung, ob frühere ähnliche Ereignisse betroffen waren.
