# FocusFlow – Komponentenvertrag

Diese Datei zeigt, wie Figma-Komponenten so beschrieben werden, dass Claude Code, Codex oder ein Entwickler sie zuverlässig umsetzen kann.

## Button

### Varianten
- `primary`: wichtigste Aktion eines Bereichs;
- `secondary`: alternative sichere Aktion;
- `danger`: irreversible oder schädliche Aktion;
- `ghost`: kleine kontextbezogene Aktion.

### Zustände
- default;
- hover, falls Zeigegerät;
- focus-visible;
- pressed;
- disabled;
- loading;
- error nur als umgebender Formularzustand, nicht durch rote Buttonfarbe allein.

### Vertrag

```text
Name: Button
Props: variant, size, disabled, loading, iconBefore, iconAfter
Pflicht: sichtbarer Text oder zugänglicher Name
Touchziel: mindestens projektspezifische Accessibility-Baseline
Loading: Aktion nicht doppelt auslösen; Text bleibt verständlich
Danger: Bestätigung oder Undo entsprechend Auswirkung
```

## Textfeld

```text
Name: TextField
Props: label, value, hint, error, required, autocomplete, inputMode
Pflicht: dauerhaftes Label; Placeholder ist kein Label
Fehler: konkret, programmatisch verknüpft und nicht nur farblich
Zustände: empty, filled, focused, invalid, disabled, read-only, loading
```

## Aufgabenzeile

```text
Name: TaskRow
Inhalt: Statuskontrolle, Titel, Auswahlaktion, Löschaktion
Zustände: open, selected, completed, disabled, syncing, error
Regeln:
- Titel darf umbrechen;
- Auswahl und Abschluss sind getrennte Aktionen;
- Löschung benötigt Bestätigung oder Undo;
- Status wird Screenreadern mitgeteilt;
- keine gesamte Zeile als unklare Mehrfachaktion.
```

## Timer

```text
Name: FocusTimer
Inhalt: ausgewählte Aufgabe, Restzeit, Status, Start/Pause, Reset
Zustände: ready, running, paused, completed, unavailable
Regeln:
- Zeit nutzt tabellarische Ziffern;
- Status ist nicht nur Farbe;
- Hintergrund/Neustart-Verhalten ist dokumentiert;
- kein mehrfacher Timer durch wiederholtes Tippen;
- Screenreader wird nicht jede Sekunde störend unterbrochen.
```

## Feedback

- Feldfehler direkt am Feld;
- Seiten-/Systemfehler als persistente Meldung mit Aktion;
- Erfolgsmeldung kurz in einer Live Region;
- kritische Fehler nicht automatisch ausblenden;
- Offlinezustand erklärt, was gespeichert, ausstehend oder nicht möglich ist.

## Handoff-Nachweis

Für jede Komponente existieren:

- Figma-Name und Varianten;
- Tokenreferenzen;
- Inhaltsregeln;
- Zustände;
- Accessibility-Vertrag;
- responsive Verhalten;
- Test-IDs nur bei echtem Testbedarf;
- Beispiel und Gegenbeispiel;
- Screenshotvergleich nach Umsetzung.
