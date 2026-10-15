# Runbook – Auth-Ausfall

## Auslöser

- erhöhte Login-/Refresh-Fehlerrate;
- Nutzer werden ungewollt abgemeldet;
- OAuth-/E-Mail-Links schlagen fehl;
- Sessions werden nicht validiert;
- Verdacht auf kompromittierte Tokens.

## Erste fünf Minuten

1. Incident eröffnen, Uhrzeit und Schweregrad notieren.
2. Prüfen, ob nur ein Provider, eine Region, eine App-Version oder alle Nutzer betroffen sind.
3. Statusseite und Anbieterstatus prüfen.
4. Keine Auth-Sicherheitskontrolle abschalten, um Login kurzfristig zu „reparieren“.
5. Riskante Releases/Feature Flags stoppen.

## Eindämmung

- neue Registrierungen oder betroffene Loginart gezielt deaktivieren;
- bestehende sichere Sessions nur weiterverwenden, wenn die Risikobewertung dies erlaubt;
- verdächtige Tokens/Keys rotieren;
- Adminzugänge separat kontrollieren;
- Rate Limits nicht pauschal entfernen.

## Diagnose

- Fehler nach Plattform, Version, Provider und Endpoint;
- Redirect-URLs und Deep Links;
- Zertifikate, Domains, E-Mail-Provider;
- Uhrzeit-/Tokenablauf;
- Datenbank-/RLS-Änderungen;
- letzte Deployments und Konfigurationsänderungen.

## Kommunikation

Nutzerinformation enthält:
- betroffene Funktion;
- bekannte Auswirkung;
- sichere Alternative, falls vorhanden;
- nächstes Update;
- keine unbelegten Ursachen oder Sicherheitsversprechen.

## Wiederherstellung

1. Fix auf Staging reproduzieren.
2. Login, Refresh, Logout, Recovery und Kontowechsel testen.
3. Gestaffelt ausrollen.
4. Fehlerrate und Support beobachten.
5. Incident erst schließen, wenn Kernmetriken stabil sind.

## Nacharbeit

- Ursache und Zeitlinie;
- warum Kontrollen nicht früher erkannten;
- Regressionstest;
- Runbook-/Alarmverbesserung;
- mögliche Datenschutz-/Security-Auswirkung;
- verantwortliche Person und Termin.
