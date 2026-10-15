# Design Tokens und Komponenten

## Warum Tokens?

Tokens verbinden Figma, Code und Dokumentation. Ein Farbwert wie `#2563EB` erklärt nicht, wofür er verwendet wird. `color.action.primary` schon.

## Token-Ebenen

### 1. Primitive Tokens

Technische Rohwerte:

```text
blue.600 = #2563EB
neutral.950 = #0A0A0A
space.4 = 16px
radius.3 = 12px
```

### 2. Semantische Tokens

Bedeutung im Produkt:

```text
color.text.primary = neutral.950
color.action.primary = blue.600
color.border.danger = red.600
space.component.card = space.4
```

### 3. Komponenten-Tokens

Spezifische Zuordnung:

```text
button.primary.background.default = color.action.primary
button.primary.text.default = color.text.on-primary
input.border.error = color.border.danger
```

## Basissystem

### Farbe

- Background
- Surface
- Text
- Border
- Action
- Status
- Overlay
- Focus

Für jede Rolle mindestens:

- default
- subtle
- strong
- disabled
- hover/pressed, sofern Plattform relevant

### Typografie

| Rolle | Zweck |
|---|---|
| Display | seltene große Hero-Inhalte |
| Heading 1–4 | klare Inhaltsstruktur |
| Body Large/Medium/Small | Fließtext |
| Label | Eingaben und kompakte UI |
| Caption | Zusatzinformation |
| Numeric | Zahlen, Timer, Finanzen |

Definiere Schriftfamilie, Größe, Zeilenhöhe, Gewicht und Buchstabenabstand.

### Abstände

Ein mögliches Raster:

```text
2, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64
```

Nicht jeder Wert muss benutzt werden. Wichtig ist die konsequente Auswahl.

### Bewegung

Definiere:

- Dauer: sofort, kurz, normal, lang
- Easing
- erlaubte Übergänge
- reduzierte Bewegung
- keine Animation, die eine Aktion künstlich verzögert

## Komponenten-Spezifikation

Für jede Komponente dokumentieren:

```text
Name
Zweck
Anatomie
Varianten
Größen
Zustände
Inhaltregeln
Accessibility
Responsive Verhalten
Do/Don't
Code-API
Tests
```

## Beispiel: Primärer Button

### Zweck

Löst die wichtigste Aktion eines Bereichs aus.

### Zustände

- Default
- Hover, falls Maus
- Pressed
- Focus Visible
- Loading
- Disabled
- Error nur über zugehörige Meldung, nicht als unklarer Farbwechsel

### Regeln

- pro Bereich nur eine klar dominierende Hauptaktion;
- Label beschreibt Handlung, z. B. „Projekt erstellen“;
- kein unbestimmtes „Weiter“, wenn die Folge unklar ist;
- Loading verhindert Doppelabsendung;
- Disabled nur mit erkennbarer Ursache.

## Beispiel: Textfeld

Benötigt:

- dauerhaft erkennbare Bezeichnung;
- optionalen Hilfetext;
- konkreten Fehlertext;
- Eingabetyp und Autocomplete;
- Zeichenlimit, falls fachlich nötig;
- Fokus-/Tastaturverhalten;
- sichere Behandlung sensibler Eingaben.

## Code-Abgleich

Eine Änderung gilt erst als abgeschlossen, wenn:

- Figma-Token aktualisiert;
- Code-Token aktualisiert;
- betroffene Komponenten geprüft;
- visuelle Regression geprüft;
- Dark Mode und Accessibility geprüft;
- Changelog ergänzt wurde.

## Definition of Done

- [ ] keine zufälligen Einzelwerte in neuen Screens
- [ ] semantische Tokens für Light und Dark
- [ ] Komponenten besitzen alle relevanten Zustände
- [ ] Design und Code verwenden dieselben Namen oder eine dokumentierte Zuordnung
- [ ] große Schrift und kleine Displays getestet
- [ ] Fokus und Screenreader geprüft
- [ ] visuelle Regression vorhanden
