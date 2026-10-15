# Runbook – KI-Anbieter-Ausfall und Kostenanomalie

## Auslöser

- stark erhöhte Latenz oder Fehlerrate;
- ungültige oder sicherheitskritische Ausgaben;
- Kosten steigen ungewöhnlich;
- Modell-/Provideränderung verändert Verhalten;
- Rate Limits oder Kontingente sind ausgeschöpft;
- Verdacht auf Schlüsselmissbrauch.

## Erste fünf Minuten

1. KI-Funktion über Kill Switch oder Feature Flag begrenzen.
2. Kernapp ohne KI weiter nutzbar halten.
3. Kosten-, Token-, Nutzer- und Endpointdaten prüfen.
4. Schlüsselmissbrauch ausschließen; bei Verdacht Schlüssel rotieren.
5. Modell-/Promptversion und letzte Änderungen festhalten.

## Eindämmung

- harte Nutzer-, Zeit-, Token- und Kostenlimits aktivieren;
- teure nichtkritische Funktionen deaktivieren;
- Fallback-Modell nur verwenden, wenn zuvor evaluiert;
- Schreib-/Agentenaktionen auf Bestätigung oder Read-only setzen;
- fehlerhafte Ergebnisse nicht automatisch dauerhaft speichern.

## Diagnose

- Providerstatus und API-Fehler;
- Modell- oder Promptänderung;
- ungewöhnliche Eingabelängen oder Bots;
- Endlosschleifen bei Agenten;
- Cache-Miss-/Retry-Sturm;
- doppelte Requests;
- RAG-Ausfall oder fehlende Berechtigungsfilter;
- Kosten pro erfolgreichem Nutzerergebnis.

## Wiederherstellung

1. Goldenset und Sicherheitstests gegen die geplante Konfiguration ausführen.
2. Kosten/Latenz mit Baseline vergleichen.
3. Kleine Nutzergruppe aktivieren.
4. Qualitäts-, Fehler- und Kostenmetriken beobachten.
5. Schrittweise freigeben oder Fallback beibehalten.

## Nutzerkommunikation

- KI-Funktion klar als vorübergehend eingeschränkt kennzeichnen;
- keine falschen Erfolgsmeldungen;
- alternative manuelle Funktion anbieten;
- bei potenziell falschen Hochrisikoausgaben betroffene Ergebnisse identifizieren und fachlich bewerten.

## Nacharbeit

- Limits und Alarme anpassen;
- Regressionstest ergänzen;
- Modell-/Promptregister aktualisieren;
- Anbieter- und Exitstrategie prüfen;
- Ursache für fehlenden Kill Switch, Fallback oder Kostenalarm beheben.
