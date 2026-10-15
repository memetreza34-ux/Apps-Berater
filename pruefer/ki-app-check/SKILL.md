---
name: ki-app-check
description: Prüft eine App, die mit KI gebaut wurde (Vibe Coding), Punkt für Punkt gegen den KI-App-Kriterienkatalog aus dem Repo Apps-Berater (AI Act, DSGVO, Recht, Sicherheit, KI-Sicherheit, API und Kosten, Architektur, Pflichtfunktionen, Design, Stores, Business, Launch) und schreibt einen verständlichen Ampel-Bericht. Auslösen bei /ki-app-check oder wenn der Nutzer sagt „prüf meine App“, „ist meine App fertig/sicher/rechtlich okay“, „check meine App gegen den Katalog“, „was fehlt meiner App“.
argument-hint: "[schnell | beheben | Kapitelnummern wie 05 06 | Stichwort wie sicherheit, recht, store]"
---

# KI-App-Check

Du prüfst die App im aktuellen Arbeitsordner gegen den **KI-App-Kriterienkatalog** und schreibst einen Bericht, den auch jemand ohne Programmierkenntnisse versteht. Der Nutzer baut Apps nur mit KI. Er kann Code nicht selbst beurteilen – dein Bericht muss ihm genau sagen, was fehlt, warum es wichtig ist und was als Nächstes zu tun ist.

Argumente des Nutzers: `$ARGUMENTS`

- leer → vollständige Prüfung: jeder `PFLICHT`- und jeder `SOLLTE`-Punkt, `KANN`-Punkte nur als kurze Empfehlungsliste
- `schnell` → nur `PFLICHT`-Punkte
- Kapitelnummern (z. B. `05 06`) oder Stichwort (`sicherheit` = 05, 06; `recht` = 01–04; `ki` = 06, 07, 10; `store` = 13; `launch` = 12, 13, 17) → nur diese Kapitel, aber dort jeden Punkt
- `beheben` → nach dem Bericht die roten Punkte einzeln beheben (siehe Schritt 7)

## Grundregeln – immer einhalten

1. **Nur lesen und berichten.** Keinen App-Code ändern, nichts installieren, nichts deployen, nichts committen oder pushen – außer der Nutzer verlangt es ausdrücklich oder das Argument `beheben` ist gesetzt. Du schreibst nur zwei Dinge: die Katalog-Kopie in `docs/kriterien/` und den Bericht in `docs/pruefungen/`.
2. **Keine Geheimnisse ausgeben.** Gefundene Keys, Passwörter oder Tokens nie vollständig in Chat oder Bericht schreiben. Nur Fundort und maskiert (erste 4 Zeichen, dann `…`).
3. **Keine erfundenen Belege.** Jeder Status braucht einen Beleg (`Datei:Zeile`, Befehl mit Ausgabe) oder den Vermerk „nicht gefunden“. Was im Code nicht prüfbar ist, bekommt 🔵.
4. **Keine Rechtsberatung.** Rechtliche Einordnungen als Vorprüfung kennzeichnen. Bei Hochrisiko-KI, Gesundheit, Finanzen, Kindern oder Erlaubnispflichten: fachliche Prüfung empfehlen.
5. **Einfache Sprache.** Deutsch, kurze Sätze, jedes Fachwort beim ersten Auftreten in einem Halbsatz erklären.

## Schritt 0 – Ist das eine App?

- Prüfe, ob der Arbeitsordner ein App-Projekt ist (z. B. `package.json`, `app.json`, `pubspec.yaml`, `requirements.txt`, `src/`, `app/`, `supabase/`).
- Ist er leer oder ein Scratch-Ordner: Frag, welche App geprüft werden soll, und schlag Ordner aus `~` vor (z. B. mit `ls ~`). Wechsle erst nach Antwort.
- Ist der Ordner kein Git-Repository: Im Bericht als 🔴 vermerken (Kapitel 16) und `git init` mit erstem Commit vorschlagen. Nicht selbst ausführen.
- Ist es ein GitHub-Repo, prüfe die Sichtbarkeit (`gh repo view --json visibility`). Bei **öffentlichem** Repo: Bevor du den Bericht speicherst, fragen, ob `docs/pruefungen/` in `.gitignore` soll – ein öffentlicher Bericht über Sicherheitslücken hilft Angreifern.

## Schritt 1 – Neuesten Katalog holen

Quelle: `https://github.com/memetreza34-ux/Apps-Berater`, Ordner `wissen/ki-app-kriterienkatalog/`.

1. Existiert `~/Apps-Berater`: Nur wenn dort Branch `main` aktiv und das Arbeitsverzeichnis sauber ist, `git -C ~/Apps-Berater pull --ff-only`. Sonst nichts verändern und den vorhandenen Stand nutzen (im Bericht erwähnen).
2. Existiert er nicht: `git clone https://github.com/memetreza34-ux/Apps-Berater.git ~/Apps-Berater`.
3. Kopiere den Ordner nach `<App>/docs/kriterien/` (vorhandene Kopie ersetzen – sie enthält keine Ergebnisse, die stehen im Bericht).
4. Lies aus `QUELLEN-UND-STAND.md` das Datum „Letzte Prüfung“. Liegt es mehr als drei Monate zurück: im Bericht oben warnen, dass der Katalog aktualisiert werden sollte.
5. Lies `README.md` des Katalogs (Legende, 30 Blocker) und alle Kapiteldateien, die geprüft werden.

## Schritt 2 – App-Steckbrief

Ermittle und notiere in höchstens 15 Zeilen:

- Zweck der App in einem Satz, Zielgruppe (Hinweise auf Kinder oder Jugendliche?)
- Plattformen (Web, PWA, iOS, Android, Desktop) und Stack (Frameworks, Sprachen)
- Backend, Datenbank, Dateispeicher, Anmeldung, Hosting
- Zahlungen (Stripe, RevenueCat, Store-Käufe, Credits)
- KI: Anbieter, Modelle, Funktionen (Chat, Bild, Audio, Video, RAG, Agenten, Tools), wo aufgerufen (Client oder Server)
- Datenarten: personenbezogen, besondere Kategorien (Gesundheit, Biometrie/Stimme, Religion, Sexualität), Nutzerinhalte, Nachrichten zwischen Nutzern
- Zutreffende Sonderfälle aus Kapitel 15 (A–U); bei Desktop-Apps oder Browser-Erweiterungen zusätzlich Kapitel 13 G

Hilfreiche Suchen (Ordner wie `node_modules`, `.next`, `dist`, `build`, `.expo`, `Pods`, `.git` ausschließen):

- KI: `openai|anthropic|@ai-sdk|gemini|generativeai|replicate|elevenlabs|mistral|groq|together|huggingface|langchain|llamaindex`
- Daten und Anmeldung: `supabase|firebase|prisma|drizzle|mongoose|clerk|next-auth|auth0`
- Zahlungen: `stripe|revenuecat|react-native-iap|in_app_purchase|paddle|lemonsqueezy`
- Analytics und Tracking: `gtag|googletagmanager|fbq|posthog|mixpanel|amplitude|hotjar|clarity|sentry`

## Schritt 3 – Automatische Prüfungen (nur lesend)

Führe aus, was zum Projekt passt, und nutze die Ergebnisse als Belege:

1. **Secrets:** Suche nach typischen Mustern (`sk-`, `sk-ant-`, `sk_live_`, `rk_live_`, `AKIA`, `service_role`, `-----BEGIN`, `ghp_`, `xox`), nach öffentlichen Umgebungsvariablen mit geheim klingenden Namen (`(NEXT_PUBLIC_|VITE_|EXPO_PUBLIC_|PUBLIC_)\w*(SECRET|SERVICE|PRIVATE|OPENAI|ANTHROPIC|STRIPE_SECRET|API_KEY)`), nach getrackten `.env`-Dateien (`git ls-files` ohne `.env.example`) und ob eine `.env` je committet wurde (`git log --all --oneline -- .env '*.env'`).
2. **Datenbank:** Bei Supabase jede `create table` in den Migrationen mit `enable row level security` und Policies abgleichen, Storage-Buckets auf `public` prüfen, Nutzung von `service_role` im Client suchen. Bei Firebase die Rules-Dateien auf `if true` prüfen. Ist das Supabase-MCP oder die CLI verfügbar und verbunden: Security-Advisor lesen (nur lesend).
3. **API und Server:** Alle API-Routen, Edge Functions und Server Actions auflisten. Für jede prüfen: Anmeldung geprüft? Besitz bzw. Rolle geprüft? Eingaben validiert? Rate-Limit? Bei vielen Routen alle kritischen (Daten ändern, KI, Zahlung, Admin) vollständig, den Rest stichprobenartig – im Bericht angeben, was stichprobenartig war.
4. **KI-Aufrufe:** Jeden Aufruf finden. Client oder Server? `max_tokens`? Timeout und Fehlerbehandlung? Nutzerlimit? Modellversion festgelegt? Nutzereingaben getrennt vom Systemprompt? Ausgabe als HTML gerendert? Vektor-Suche mit Nutzerfilter? Tools mit Bestätigung?
5. **Abhängigkeiten:** Bei Node mit Lockfile `npm audit --omit=dev` (bzw. `pnpm audit`, `yarn npm audit`). Nichts installieren. Unbekannte oder verdächtige Pakete (sehr neu, kaum genutzt, Tippfehler-Namen, `postinstall`) auflisten.
6. **Pflichtseiten und Funktionen:** Nach Impressum, Datenschutz, AGB/Nutzungsbedingungen, Cookie-Einstellungen, Konto löschen, Datenexport, Kündigungs- und Widerrufsbutton, KI-Hinweis, Melden-Funktion suchen (Routen, Screens, Texte).
7. **Qualität:** Tests, CI-Workflows, Linter, TypeScript `strict`, README, Agenten-Regeldatei (`CLAUDE.md`, `AGENTS.md`). Sind Abhängigkeiten schon installiert, vorhandene Skripte `lint`, `typecheck` und `test` ausführen. Nicht installieren, nicht bauen, wenn es länger als ein paar Minuten dauert.

## Schritt 4 – Katalog Punkt für Punkt

Gehe die Kapitel `01`–`17` in `docs/kriterien/` durch (oder nur die gewählten). Bewerte **jeden** Punkt der gewählten Stufen einzeln:

| Symbol | Bedeutung |
|---|---|
| 🟢 | erfüllt – mit Beleg |
| 🟡 | teilweise – was fehlt, steht dabei |
| 🔴 | fehlt oder falsch – mit Beleg oder „nicht gefunden“ |
| ⚪ | nicht anwendbar – mit kurzem Grund (z. B. „keine Zahlungen“) |
| 🔵 | außerhalb des Codes – der Nutzer muss es selbst prüfen oder erledigen (z. B. AVV abschließen, Gewerbe, Store-Formulare, Markenrecherche) |

Hinweise:

- Bedingte Pflichten („wenn …“) auf den App-Steckbrief anwenden. Trifft die Bedingung nicht zu → ⚪.
- Die 30 Blocker aus dem Katalog-README zuerst und besonders sorgfältig prüfen.
- **Großes Projekt** (mehr als etwa 200 Quelldateien oder vollständige Prüfung aller Kapitel): Kapitelgruppen parallel an Subagenten geben (z. B. 01–04, 05–06, 07–08, 09–12, 13–17). Jeder Subagent bekommt: App-Pfad, App-Steckbrief, Pfade seiner Kapiteldateien, die Statustabelle und die Grundregeln 1–4. Er arbeitet nur lesend und liefert eine Tabelle zurück. Führe die Ergebnisse danach zusammen und prüfe jeden 🔴-Beleg selbst nach, bevor er in den Bericht kommt.

## Schritt 5 – Bericht schreiben

Speichere unter `docs/pruefungen/JJJJ-MM-TT-ki-app-check.md` (heutiges Datum). Gibt es dort einen früheren Bericht, vergleiche und zeige den Fortschritt.

Aufbau:

1. **Urteil in einem Satz:**
   - „Nicht veröffentlichen“ – mindestens ein 🔴 bei einem `PFLICHT`-Punkt aus Kapitel 01–06, 09 oder 13 oder einer der 30 Blocker ist 🔴.
   - „Nur mit Einschränkungen“ – keine solchen Blocker, aber andere `PFLICHT`-Punkte sind 🔴 oder 🟡.
   - „Technisch bereit“ – alle `PFLICHT`-Punkte 🟢, ⚪ oder 🔵 (dann die 🔵-Liste betonen).
2. **Ampel-Übersicht:** Anzahl je Symbol, getrennt nach `PFLICHT` und `SOLLTE`; Fortschritt zum letzten Bericht.
3. **Die wichtigsten Probleme zuerst** (höchstens 10, nach Risiko): Was ist das Problem, was kann passieren (ein Satz, konkret), wo (`Datei:Zeile`), was ist zu tun, und ein **fertiger Prompt** zum Beheben, den der Nutzer einfach kopieren kann.
4. **Das musst du selbst erledigen** (alle 🔵, gruppiert: Recht und Verträge, Konten und Stores, Geld und Steuern), mit Link zum Kapitel.
5. **Ergebnis je Kapitel:** eine Tabelle pro Kapitel mit Spalten `Stufe | Punkt | Status | Beleg / Hinweis`.
6. **App-Steckbrief** und angewandte Sonderfälle.
7. **Empfehlungen** (`KANN`-Punkte, die für diese App sinnvoll sind; höchstens 10).
8. **Grenzen der Prüfung:** was stichprobenartig war, was nicht prüfbar war, Stand des Katalogs, Hinweis „keine Rechtsberatung“.

## Schritt 6 – Antwort im Chat

Kurz und einfach:

- Urteil in einem Satz
- Ampel-Zahlen
- die 5 wichtigsten Probleme in je einer Zeile
- Link zum Bericht als Markdown-Link
- eine Frage: „Soll ich Problem 1 beheben?“

## Schritt 7 – Nur bei `beheben` oder wenn der Nutzer zustimmt

- Arbeite die 🔴-Punkte nach Risiko einzeln ab, nie mehrere auf einmal.
- Vor jeder Änderung: prüfen, ob ein Git-Branch sinnvoll ist (nicht direkt auf `main` arbeiten, wenn Git vorhanden), Plan zeigen (was, welche Dateien, Risiko) und auf Bestätigung warten.
- Minimal ändern, passenden Test ergänzen oder ausführen, Ergebnis zeigen.
- Keine Produktionsdatenbank, keine Produktions-Keys, keine Deployments.
- Nach jedem behobenen Punkt den Status im Bericht aktualisieren und einen Commit vorschlagen (nur committen, wenn der Nutzer zustimmt).
