# Apps-Berater

**Wissensbasis und praktischer Arbeitsmodus für einen KI-App-Berater – von der Idee bis zum Release.**

Dieses Repository enthält eine umfangreiche Wissensbasis für KI-gestützte App-Entwicklung: den roten Faden von der Idee bis zum Betrieb, über 1.100 dokumentierte Prüfpunkte zu Recht, Sicherheit, Design und Tests, Vorlagen, Notfallpläne, Beispiele und zwei **agentengeführte** Prüfabläufe. Die Inhalte allein sind noch kein eigenständig laufender KI-Berater und garantieren weder Fehlerfreiheit noch Rechtskonformität.

## Wofür ist das?

Du baust Apps mit KI – mit ChatGPT, Claude, Claude Code, Cursor, Codex, Lovable, Bolt, Replit oder anderen Werkzeugen. Diese Werkzeuge schreiben schnell Code. Sie vergessen aber oft, was eine App wirklich braucht:

- dass ein API-Schlüssel nie in die App gehört,
- dass Nutzer A die Daten von Nutzer B nicht sehen darf,
- dass ein Chatbot als KI gekennzeichnet sein muss,
- dass ein Abo einen Kündigungs- und einen Widerrufsbutton braucht,
- dass Apple und Google eigene Regeln haben,
- dass man Backups nicht nur macht, sondern auch einmal zurückspielt.

Hier steht all das an einem Ort. Die KI liest es **vor** dem ersten Code und arbeitet dann Schritt für Schritt danach.

## Warum?

- **Risiken früh erkennen:** Datenschutz-, Sicherheits-, Store- und Kostenprobleme vor einer Veröffentlichung prüfen; Risiken können dadurch reduziert, aber nicht ausgeschlossen werden.
- **Damit jede App gleich gut wird:** Jede neue App folgt demselben Weg und denselben Prüfungen, egal welche KI du gerade nutzt.
- **Damit du KI gezielt steuerst:** Du musst nicht alles selbst programmieren, kannst aber Aufgaben, Nachweise und Risiken besser beurteilen.

## Praktischer Berater (V0)

**[MVP und Ausbauplan](./BERATER-MVP.md)** · **[Arbeitsmodus für KI](./BERATER-ARBEITSMODUS.md)** · **[Pilot mit Secret Circle](./PILOT-SECRET-CIRCLE.md)**

Die erste Version funktioniert **innerhalb eines aktiven ChatGPT-/Claude-Code-Workflows**, wenn der Agent die Dokumente und – mit Erlaubnis – das aktuelle App-Repository lesen kann. Sie ermittelt den tatsächlichen Stand, den nächsten wichtigsten Schritt und die nötige Prüfung. Eine eigene Weboberfläche oder automatische Hintergrundüberwachung existiert damit noch nicht.

## So benutzt du es

| Situation | Was du tust |
|---|---|
| **Neue App mit einem Coding-Agenten** (Claude Code, Cursor, Codex, Copilot) | Repository in den Projektordner legen oder öffnen. Der Agent liest automatisch [`AGENTS.md`](./AGENTS.md) bzw. [`CLAUDE.md`](./CLAUDE.md). Sag ihm: „Lies den Apps-Berater und begleite mich nach dem roten Faden.“ |
| **Chat ohne Dateizugriff** (ChatGPT, Claude im Browser, Gemini) | Den Link zu diesem Repository oder zu [`llms.txt`](./llms.txt) in den Chat geben und sagen: „Lies das zuerst und arbeite danach.“ Oder die benötigten Dateien hochladen. |
| **Vorhandene App begleiten** | [`BERATER-ARBEITSMODUS.md`](./BERATER-ARBEITSMODUS.md) lesen und aktuelles Repository, offene PRs, CI und Release-Gates prüfen; nur belegten Status melden. |
| **Vorhandene App prüfen** | Den Prüfer [`pruefer/ki-app-check`](./pruefer/README.md) laufen lassen. Er schreibt einen Ampel-Bericht: was fehlt, warum, was zu tun ist. |
| **Den Berater selbst aktuell halten** | Alle drei Monate den Prüfer [`pruefer/katalog-pruefen`](./pruefer/README.md) laufen lassen. Er recherchiert neue Gesetze und Regeln und ergänzt den Katalog. |

## Aufbau

| Datei oder Ordner | Inhalt |
|---|---|
| [`BERATER-MVP.md`](./BERATER-MVP.md) | Produktidee und Roadmap für den interaktiven Berater |
| [`BERATER-ARBEITSMODUS.md`](./BERATER-ARBEITSMODUS.md) | Konkreter Ablauf für Projektübernahme, Status, nächsten Schritt und Nachweise |
| [`PILOT-SECRET-CIRCLE.md`](./PILOT-SECRET-CIRCLE.md) | Praxisfall für ein vorhandenes App-Repository |
| [`AGENTS.md`](./AGENTS.md) | Arbeitsanweisung für **jede** KI: was sie zuerst liest, wie sie vorgeht, was sie nie tun darf |
| [`ROTER-FADEN.md`](./ROTER-FADEN.md) | Der Weg in 14 Schritten von der Idee bis zum Betrieb – mit Lesestoff, Prüfpunkten, Tests und Abschlusskriterium je Schritt |
| [`TESTEN.md`](./TESTEN.md) | Alle Testmöglichkeiten: was, wann, womit, und der Mindestumfang vor jedem Release |
| [`wissen/ki-app-kriterienkatalog/`](./wissen/ki-app-kriterienkatalog/README.md) | Der Prüfkatalog: über 1.100 Punkte in 17 Kapiteln (AI Act, Datenschutz, Verbraucherrecht, Urheberrecht, Sicherheit, KI-Sicherheit, Kosten, Architektur, Pflichtfunktionen, KI-UX, Design und Barrierefreiheit, Tests, Stores, Steuern, Sonderfälle, Vibe-Coding, Launch) |
| [`wissen/app-master-anleitung/`](./wissen/app-master-anleitung/README.md) | Die ausführliche Anleitung von der Idee bis zum langfristigen Betrieb mit Beispielwegen und Vorlagen |
| [`wissen/allgemeine-app-entwicklung/`](./wissen/allgemeine-app-entwicklung/README.md) | Das technische Handbuch: Design, Architektur, Supabase, KI-Agenten, Sicherheit, Teststrategie, Plattformen, Zahlungen, Runbooks, Vorlagen, Masterprompt |
| [`pruefer/`](./pruefer/README.md) | Die zwei Prüfer: App gegen den Katalog prüfen (`ki-app-check`) und Katalog aktuell halten (`katalog-pruefen`) |
| [`beispiel-apps/`](./beispiel-apps/) | Eine lauffähige Beispiel-App (Offline-PWA) und ein Supabase-Beispiel mit Zwei-Nutzer-Test für Zugriffsregeln |
| [`scripts/`](./scripts/) | Prüfskripte für Struktur und Links sowie ein Entscheidungsassistent |
| [`llms.txt`](./llms.txt) | Kurzes Inhaltsverzeichnis für KI-Chats, die Links lesen können |

## Die wichtigste Regel

Nichts gilt als fertig, nur weil die KI es sagt. Ein Punkt ist erst erledigt, wenn es einen **Nachweis** gibt: einen Test, einen Screenshot, ein Dokument oder einen Commit.

## Prüfen, ob alles in Ordnung ist

```bash
python3 pruefer/katalog-pruefen/katalog_check.py
```

```bash
python3 scripts/validate_handbook.py
```

```bash
python3 scripts/validate_master_guide.py
```

## Grenzen

- **Keine Rechtsberatung.** Der Berater zeigt, **was** du prüfen musst. Bei Hochrisiko-KI, Gesundheit, Finanzen, Kindern oder sensiblen Daten (z. B. Religion) holst du dir fachliche Hilfe.
- **Regeln ändern sich.** Gesetze, Store-Regeln und KI-Anbieter ändern sich laufend. Den Stand siehst du in [Quellen und Stand](./wissen/ki-app-kriterienkatalog/QUELLEN-UND-STAND.md). Letzte vollständige Prüfung: 13. Oktober 2026.
- **Schwerpunkt Deutschland und EU.** Andere Länder sind nur im Überblick enthalten.

## Herkunft

Die Inhalte stammen aus dem Repository [von-idee-bis-fertig](https://github.com/memetreza34-ux/von-idee-bis-fertig) und werden hier als eigener, KI-freundlicher Berater gepflegt.
