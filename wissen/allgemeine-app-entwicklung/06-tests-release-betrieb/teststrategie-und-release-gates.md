# Teststrategie und Release-Gates

## Ziel

Tests sollen Produkt- und Betriebsrisiken abdecken. Eine hohe Zahl an Unit Tests reicht nicht, wenn der echte Kernablauf, Rechte oder Migrationen ungeprüft bleiben.

## Risikobasierte Testpyramide

### Unit Tests

Für:

- Berechnungen
- Validierung
- Statusübergänge
- Formatierung
- fachliche Regeln
- Datenkonvertierung

### Integrationstests

Für:

- Datenbank und Migrationen
- Authentifizierung
- RLS/Autorisierung
- Storage
- APIs und Webhooks
- Zahlungen
- KI-Gateway
- Export/Löschung

### End-to-End

Für wenige, entscheidende Abläufe:

1. Registrierung/Anmeldung
2. erster Kernnutzen
3. Wiederaufnahme nach Neustart
4. Bearbeiten/Löschen
5. Zahlung oder Abo, falls vorhanden
6. Export und Kontolöschung

## Testdimensionen

| Bereich | Pflichtfragen |
|---|---|
| Funktion | Ergebnis fachlich korrekt? |
| Rechte | Kann eine fremde Rolle zugreifen? |
| Fehler | Was passiert bei Timeout, Offline und ungültigen Daten? |
| Daten | Bleiben Beziehungen und Constraints korrekt? |
| Accessibility | Screenreader, Fokus, Textgröße, Kontrast? |
| Performance | Start, Interaktion, Netzwerk, Akku, Speicher? |
| Recovery | Retry, Rollback, Backup/Restore? |
| Kompatibilität | Geräte, OS, Browser, Zeitzone, Sprache? |

## Testdaten

- synthetisch, nicht produktiv;
- leere, normale und große Accounts;
- Nutzer A/B/Admin/Gast;
- lange Texte, Emojis und Sonderzeichen;
- verschiedene Sprachen und Zeitzonen;
- langsames/unterbrochenes Netzwerk;
- alte App-Version gegen neues Backend.

## Performance-Budget

Vor dem Release projektspezifische Grenzwerte festlegen:

```text
App-Start warm/kalt
Zeit bis Kerninteraktion
p95 API-Latenz
maximale Bild-/Bundlegröße
Speicherverbrauch
Hintergrundnetzwerk
KI-Latenz und Kosten
```

Messwerte werden auf realistischen schwächeren Geräten geprüft, nicht nur auf Entwicklerhardware.

## Gate 0 – Risiko

- [ ] App-Risikoprofil
- [ ] Rechte/Regulierung
- [ ] Daten und Anbieter
- [ ] Stop/Go

## Gate 1 – Produkt

- [ ] reale Problembelege
- [ ] PRD und Nicht-Ziele
- [ ] Kernmetrik
- [ ] MVP

## Gate 2 – UX und Architektur

- [ ] vollständiger Kernflow
- [ ] Zustände und Accessibility
- [ ] Datenmodell
- [ ] Rollen/Rechte
- [ ] ADRs und Threat Model

## Gate 3 – Sicherer vertikaler Slice

- [ ] echter Kernablauf Ende-zu-Ende
- [ ] persistente Daten
- [ ] negativer Fremdzugriffstest
- [ ] Fehler/Offline
- [ ] E2E in CI oder reproduzierbar

## Gate 4 – Produktionsreife

- [ ] Testbericht
- [ ] Security-Freigabe
- [ ] Datenschutz/Export/Löschung
- [ ] Migration/Backup/Restore
- [ ] Monitoring und Alarmierung
- [ ] Support/Incident

## Gate 5 – Store/Launch

- [ ] Store-Texte und reale App stimmen überein
- [ ] Datenschutzangaben mit SDK-/Dateninventar abgeglichen
- [ ] Review-Konto und Notes
- [ ] Signierung und Release Build
- [ ] Rollback
- [ ] gestaffelter Rollout

## Gate 6 – Betrieb

- [ ] tägliche Kernsignale
- [ ] Kostenalarme
- [ ] Update- und Supportplan
- [ ] quartalsweiser Restore-/Threat-Model-Review
- [ ] jährliche Rechts-/Store-/Anbieterprüfung

## Go/No-Go-Regel

Ein Release darf nicht erfolgen bei:

- kritischem Datenverlust- oder Fremdzugriffsrisiko;
- fehlender Kontolöschung trotz Konto;
- unbekannter Migration oder fehlendem Backup;
- nicht beherrschbarem Kosten-/Missbrauchsrisiko;
- Store-Angaben, die der tatsächlichen App widersprechen;
- offenem kritischem Crash im Kernablauf.

## Nach dem Release

In den ersten 24–72 Stunden besonders überwachen:

- Registrierung/Login
- Kernablauf-Erfolg
- Crash- und Fehlerquote
- Migrationen
- Zahlungen
- KI-/API-Kosten
- Lösch-/Supportanfragen
- Store-Reviews und Supportmuster
