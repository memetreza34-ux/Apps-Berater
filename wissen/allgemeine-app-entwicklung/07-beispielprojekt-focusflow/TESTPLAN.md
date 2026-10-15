# FocusFlow – Testplan

## 1. Kernablauf

### E2E-01 – Erste Fokus-Session

**Vorbedingung:** neues bestätigtes Konto.

1. anmelden;
2. Aufgabe erstellen;
3. Fokusdauer wählen;
4. Session starten;
5. App schließen und erneut öffnen;
6. Session fortsetzen;
7. Session abschließen;
8. Tagesstatistik prüfen.

**Erwartung:** Session bleibt konsistent, wird genau einmal gezählt und gehört nur dem angemeldeten Nutzer.

### E2E-02 – Offline beim Erstellen

1. Netzwerk trennen;
2. Aufgabe erstellen;
3. verständliche Rückmeldung prüfen;
4. Netzwerk aktivieren;
5. Retry ausführen.

**Erwartung:** keine stille Datenvernichtung, kein doppelter Datensatz.

## 2. Autorisierung

| ID | Aktion | Erwartung |
|---|---|---|
| AUTH-01 | Nutzer A liest Projekt-ID von B direkt | keine Daten |
| AUTH-02 | A setzt beim Insert `user_id` von B | blockiert |
| AUTH-03 | A ändert eigenes Projekt auf B | blockiert |
| AUTH-04 | A ordnet Aufgabe einem Projekt von B zu | blockiert |
| AUTH-05 | ohne Login Data API aufrufen | blockiert |
| AUTH-06 | normaler Client schreibt `ai_usage` | blockiert |

## 3. Session-Logik

- Start mit Minimum/Maximum-Dauer
- ungültige Dauer
- doppelter Abschluss
- Abschluss nach App-Neustart
- Abbruch
- Client-Uhrzeit deutlich falsch
- parallele Geräte
- Netzwerkabbruch während Abschluss
- Retry desselben Requests
- gelöschte Aufgabe während aktiver Session

## 4. KI-Funktion

### Normal

- kurze klare Aufgabe
- lange zulässige Aufgabe
- deutsche und englische Eingabe
- strukturierte Schritte
- Nutzer lehnt Vorschlag ab
- Nutzer bestätigt Vorschlag

### Sicherheit und Robustheit

- Prompt Injection
- Aufforderung zur Ausgabe von Systemanweisungen
- personenbezogene/sensible Inhalte
- extrem lange Eingabe
- ungültiges Ausgabeformat
- Timeout
- Providerfehler
- Rate Limit
- Kostenlimit
- doppelte Anfrage

**Erwartung:** Kern-App bleibt nutzbar; keine ungeprüfte automatische Speicherung oder Aktion.

## 5. Export und Löschung

### Export

- leerer Account
- normaler Account
- großer Account
- Sonderzeichen/Emojis
- Datenbeziehungen nachvollziehbar
- kein Inhalt anderer Nutzer
- Download läuft ab

### Löschung

- normale Löschung
- zweiter Aufruf
- aktive Session
- offener KI-Auftrag
- externer Anbieter nicht erreichbar
- Auth-Sessions widerrufen
- Datenbank leer
- Storage/Vektoren/Drittanbieter geprüft
- Restore aus Backup respektiert Löschjournal

## 6. Accessibility

- Screenreader-Namen
- Fokusreihenfolge
- Hardware-/Bildschirmtastatur
- Textvergrößerung
- Dark Mode und Kontrast
- Reduced Motion
- Touch-Ziele
- Fehler nicht nur durch Farbe
- Timerstatus verständlich ohne Animation

## 7. Performance

- kalter und warmer Start
- 1, 100 und 10.000 Aufgaben im Testaccount
- Listenpagination
- p95 API-Latenz
- Realtime nur bei tatsächlichem Bedarf
- KI-Latenz und Timeout
- Speicherverbrauch bei langer Session
- Hintergrund-/Akkubelastung

## 8. Migration und Recovery

- leere Datenbank migrieren
- vorherige Staging-Version migrieren
- Migration erneut ausführen, soweit vorgesehen
- fehlerhafte Migration erkennen
- Backup wiederherstellen
- App-Version N-1 gegen neues Schema
- Löschjournal nach Restore anwenden

## 9. Release-Blocker

- fremder Zugriff
- doppelte/fehlende Sessionzählung
- Datenverlust im Kernablauf
- nicht funktionierende Kontolöschung
- Secret im Client
- keine Backup-Wiederherstellung
- unkontrollierte KI-Kosten
- kritischer Crash oder Migrationsfehler

## 10. Testbericht

```text
Version/Build:
Umgebung:
Geräte/OS:
Migration:
Kern-E2E:
Autorisierung:
KI:
Export/Löschung:
Accessibility:
Performance:
Restore:
Offene Fehler:
Akzeptierte Risiken:
Go/No-Go:
Tester/Datum:
```
