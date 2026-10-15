# Datenlebenszyklus, Export und Löschung

## Ziel

Jede Datenart muss von der Erhebung bis zur endgültigen Löschung nachvollziehbar sein. Ein Datenschutzerklärungstext ersetzt diesen technischen Prozess nicht.

## Dateninventar

Für jedes Feld und jedes externe System dokumentieren:

| Feld | Beschreibung |
|---|---|
| Datenart | z. B. E-Mail, Standort, Datei, Nutzungsereignis |
| betroffene Person | Nutzer, Gast, Kontakt, Mitarbeiter |
| Quelle | Eingabe, Gerät, Import, Anbieter |
| Zweck | konkrete aktuelle Funktion |
| Rechtsgrundlage | projektspezifische Prüfung |
| Speicherort | DB, Storage, Cache, Anbieter |
| Empfänger/Region | interne und externe Verarbeitung |
| Dauer | feste Frist oder nachvollziehbares Kriterium |
| Export | Format und Umfang |
| Löschung | Auslöser, Job und Nachweis |

## Datenminimierung

Vor jedem neuen Feld:

1. Wird es für eine bestehende Funktion wirklich benötigt?
2. Kann die Funktion ohne dauerhafte Speicherung arbeiten?
3. Kann der Wert lokal, aggregiert oder pseudonymisiert werden?
4. Muss der externe Anbieter den Rohwert erhalten?
5. Wie wird der Wert exportiert, korrigiert und gelöscht?

## Aufbewahrung

Eine Aufbewahrungsregel enthält:

```text
Datenart
Startpunkt der Frist
Dauer/Kriterium
Ausnahme
technischer Löschjob
Kontrolle
Nachweis
```

„Unbegrenzt“ oder „solange nötig“ ohne konkrete Kriterien ist kein belastbares Löschkonzept.

## Export

Ein brauchbarer Export:

- ist ohne Spezialsoftware lesbar;
- verwendet dokumentierte Formate wie JSON/CSV und Originaldateien;
- enthält Zeitstempel und Beziehungen;
- vermeidet Daten anderer Personen;
- wird sicher bereitgestellt;
- läuft auch bei größeren Accounts;
- besitzt Ablaufzeit und Zugriffsschutz.

## Kontolöschung

### Vor der Löschung

- Nutzer erneut authentifizieren entsprechend Risiko;
- Folgen verständlich erklären;
- aktive Abos/Verträge behandeln;
- Export anbieten, falls sinnvoll;
- Bedenkzeit nur verwenden, wenn transparent und widerrufbar.

### Zu löschende Bereiche

- Auth-Account und Sessions
- fachliche Tabellen
- Join-/Mitgliedschaftsdaten
- Storage und Vorschaudateien
- Suchindizes
- Caches
- Realtime-/Queue-Aufträge
- KI-Rohdaten und Vektoren
- Analytics-/CRM-/E-Mail-Systeme
- Supportdaten, soweit keine begründete Aufbewahrung besteht
- öffentliche Inhalte entsprechend Produktregeln

### Backups

Backups werden meist nicht einzeln umgeschrieben. Dokumentiere:

- wie lange Backups bestehen;
- dass gelöschte Daten nicht wieder in Produktion übernommen werden dürfen;
- wie ein Restore mit nachgelagertem Löschjournal funktioniert;
- wer den Prozess getestet hat.

## Löschworkflow

```text
Anfrage
→ Identität prüfen
→ Auftrag mit eindeutiger ID
→ neue Verarbeitung stoppen
→ Primärdaten löschen/anonymisieren
→ Storage/Indizes/Drittanbieter
→ Auth und Sessions
→ Ergebnis prüfen
→ Nachweis ohne unnötige Inhaltsdaten
```

Der Prozess muss wiederholbar und idempotent sein.

## Fehlerbehandlung

Wenn ein Anbieter nicht erreichbar ist:

- Löschauftrag bleibt offen;
- Retry mit Backoff;
- Alarm nach Frist;
- manueller Eskalationsweg;
- Abschluss erst, wenn alle erforderlichen Systeme bestätigt sind.

## Testfälle

- leerer Account
- normaler Account
- sehr großer Account
- aktive Freigaben/Teams
- aktive KI-/Queue-Aufträge
- aktives Abo
- externer Anbieter fällt aus
- zweiter Löschaufruf
- Restore aus Backup

## Freigabe

- [ ] Dateninventar vollständig
- [ ] konkrete Aufbewahrungsregeln
- [ ] Export getestet
- [ ] Kontolöschung über alle Systeme
- [ ] Drittanbieter und Vektoren enthalten
- [ ] Backup-/Restore-Löschjournal
- [ ] Fehler und Retry
- [ ] Store- und Datenschutzhinweise entsprechen dem echten Ablauf
