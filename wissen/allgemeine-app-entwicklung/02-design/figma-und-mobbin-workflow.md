# Figma- und Mobbin-Workflow

## Ziel

Ein hochwertiges App-Design entsteht nicht dadurch, dass ein einzelner Screenshot kopiert wird. Der richtige Ablauf verbindet Nutzeraufgaben, vollständige Referenz-Flows, ein eigenes Designsystem und überprüfbare Screens.

## Phase 1 – Referenzen sammeln

Suche nicht nur nach einer schönen Startseite. Sammle für den Kernablauf:

- Einstieg und Onboarding
- Registrierung und Anmeldung
- Dashboard oder Startzustand
- Suche, Filter und Detailansicht
- Erstellen und Bearbeiten
- Laden, Leerzustand und Fehler
- Einstellungen
- Bezahlen oder Abo, falls vorhanden
- Export und Kontolöschung

Für jede Referenz notieren:

| Feld | Inhalt |
|---|---|
| Quelle | App, Website oder Pattern-Bibliothek |
| Problem | Welches UX-Problem wird gelöst? |
| Muster | Navigation, Hierarchie, Interaktion |
| Stärke | Was funktioniert besonders gut? |
| Risiko | Was passt nicht zur eigenen Zielgruppe? |
| Übernahme | Prinzip, nicht konkrete Gestaltung |

## Phase 2 – Informationsarchitektur

Vor High-Fidelity-Designs werden alle Inhalte in eine klare Struktur gebracht.

```text
Nutzerziel
→ benötigte Information
→ Entscheidung
→ Aktion
→ Rückmeldung
→ nächster sinnvoller Schritt
```

Prüfe bei jedem Element:

- Muss es auf diesem Screen stehen?
- Muss es sofort sichtbar sein?
- Ist die Bezeichnung für neue Nutzer verständlich?
- Kann eine Navigationsebene entfernt werden?
- Was passiert ohne Daten, ohne Internet oder bei einem Fehler?

## Phase 3 – Figma-Datei strukturieren

Empfohlene Seiten:

```text
00-Cover-und-Status
01-Research
02-User-Flows
03-Wireframes
04-Design-Tokens
05-Komponenten
06-Mobile-Screens
07-Web-oder-Tablet
08-Prototyp
09-Accessibility
10-Developer-Handoff
99-Archiv
```

## Phase 4 – Design Tokens

Definiere Rollen statt Einzelwerte:

- `color.background.default`
- `color.surface.primary`
- `color.text.primary`
- `color.text.secondary`
- `color.action.primary`
- `color.status.success`
- `space.1` bis `space.n`
- `radius.small`, `medium`, `large`
- `type.body`, `label`, `title`, `display`

Tokens müssen semantisch benannt und in Light/Dark Mode testbar sein.

## Phase 5 – Komponenten

Beginne mit den Elementen des Kernablaufs:

1. Button
2. Textfeld
3. Auswahl/Dropdown
4. Navigation
5. Karte oder Listenzeile
6. Dialog/Bottom Sheet
7. Status- und Fehlermeldung
8. Ladeindikator/Skeleton

Jede Komponente braucht:

- Varianten
- Größen
- Disabled/Loading/Error
- Fokus- und Tastaturzustand
- Screenreader-Name
- responsive Verhalten
- erlaubte und verbotene Nutzung

## Phase 6 – Ein Screen als Qualitätsprobe

Baue zuerst nur den wichtigsten Screen vollständig. Prüfe:

- visuelle Hierarchie
- 8-Punkt- oder anderes konsistentes Abstandsraster
- echte Texte statt Platzhalter
- lange Texte und kleine Displays
- Dark Mode
- Textvergrößerung
- Lade-, Leer-, Fehler- und Erfolgzustände
- Touch-Ziele und Fokusreihenfolge

Erst nach Freigabe werden weitere Screens abgeleitet.

## Phase 7 – Übergabe an Claude Code oder Codex

Der Agent erhält:

- exportierte Design Tokens
- Komponentenliste
- Screen-Inventar
- Referenzbilder
- exakte Zustände
- responsive Regeln
- Accessibility-Anforderungen
- Nicht-Ziele

Guter Auftrag:

```text
Setze ausschließlich den Dashboard-Screen anhand des Designsystems um.
Bewahre vorhandene Logik, Datenzugriffe und Navigation.
Verwende nur bestehende Tokens und Komponenten.
Implementiere Loading, Empty, Error und Success.
Prüfe anschließend Typecheck, Tests, Build und einen gerenderten Screenshot.
```

## Recht und Originalität

Referenzen dürfen als Lern- und Musterquelle dienen. Nicht übernehmen:

- Logos oder Markenauftritt
- geschützte Illustrationen und Fotos
- ungewöhnliche, stark wiedererkennbare Gesamtgestaltung
- Texte, Icons oder Assets ohne passende Rechte
- komplette Screens oder Flows als nahezu identische Kopie

## Abnahmecheck

- [ ] vollständiger Kernflow statt einzelner Screens
- [ ] eigene Informationsarchitektur
- [ ] eigenes Token-System
- [ ] Komponenten mit Zuständen
- [ ] Accessibility geprüft
- [ ] echte Inhalte getestet
- [ ] responsive und Dark Mode geprüft
- [ ] Rechte an allen Assets dokumentiert
- [ ] Entwickler-Handoff vollständig
