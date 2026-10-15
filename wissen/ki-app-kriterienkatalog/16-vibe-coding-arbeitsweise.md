# 16 – Vibe-Coding-Arbeitsweise

Mit KI-Agenten zu entwickeln ist schnell – aber nur sicher, wenn du den Prozess steuerst. Die KI schreibt Code. **Du** bist verantwortlich für das, was live geht. Vertiefung: [Claude-Code- und Codex-Playbook](../allgemeine-app-entwicklung/04-ki-agenten/claude-code-und-codex-playbook.md) und [Masterprompt](../allgemeine-app-entwicklung/12-agenten-masterprompt/CLAUDE-CODE-APP-MASTERPROMPT.md).

## A. Vor dem ersten Prompt

- [ ] `SOLLTE` **Eine Seite Plan (Mini-PRD):** Problem, Zielgruppe, Kernfunktion, was *nicht* gebaut wird, Erfolgskriterium.
- [ ] `SOLLTE` **Stack festlegen** und nicht ständig wechseln.
- [ ] `SOLLTE` **Kapitel 1–4 und 15 dieses Katalogs prüfen,** bevor du Zeit in eine Idee steckst, die rechtlich schwierig ist.
- [ ] `SOLLTE` **Regeldatei für den Agenten anlegen** (`CLAUDE.md`, `AGENTS.md` oder `.cursor/rules`): Stack, Ordnerstruktur, Befehle für Tests, Sicherheitsregeln, Designregeln.

Beispiel für Sicherheitsregeln in der Regeldatei:

```text
- Niemals Secrets im Client-Code oder in öffentlichen Umgebungsvariablen.
- Jede neue Tabelle bekommt RLS, Policies und nur die nötigen GRANTs in derselben Migration. Nie GRANT ALL an anon.
- Datenbankänderungen nur als Migration im Ordner db/migrations.
- Jede API-Route prüft Anmeldung UND Besitz des Datensatzes.
- Alle Eingaben serverseitig mit zod validieren.
- KI-Aufrufe nur serverseitig, immer mit max_tokens, Timeout und Nutzerlimit.
- Keine neuen Pakete ohne Rückfrage.
- Nie RLS deaktivieren, Tests löschen oder TypeScript-Fehler mit any verstecken.
- Vor „fertig“: Build, Typprüfung, Linter und Tests ausführen.
```

## B. Beim Bauen

- [ ] `PFLICHT` **Git von Anfang an.** Nach jedem funktionierenden Schritt committen. So kannst du jederzeit zurück.
- [ ] `SOLLTE` **Kleine Schritte:** eine Funktion pro Auftrag, nicht „bau mir die ganze App“.
- [ ] `SOLLTE` **Erst planen lassen, dann umsetzen** (Plan-Modus). Den Plan lesen und korrigieren, bevor Code entsteht.
- [ ] `SOLLTE` **Branches für Experimente.** Was nicht klappt, wird verworfen statt repariert.
- [ ] `SOLLTE` **Fehler vollständig weitergeben:** komplette Fehlermeldung, Logs, Schritte zum Nachstellen, Screenshot – nicht nur „geht nicht“.
- [ ] `SOLLTE` **Aktuelle Dokumentation mitgeben** (Links oder Doku-Tools), weil das Wissen des Modells veraltet sein kann.
- [ ] `SOLLTE` **Bei Schleifen stoppen:** Wenn der Agent dreimal dasselbe Problem nicht löst, zum letzten Commit zurück, Problem neu und kleiner beschreiben.
- [ ] `SOLLTE` **Design-Referenzen geben** (Screenshots, Tokens, Komponentenbibliothek) statt „mach es schön“.
- [ ] `KANN` **Mehrere Agenten parallel** nur in getrennten Branches oder Worktrees.

## C. Prüfen, was die KI gebaut hat

- [ ] `PFLICHT` **Änderungen lesen,** besonders bei Anmeldung, Berechtigungen, Datenbank-Policies, Zahlungen, Umgebungsvariablen und Löschfunktionen.
- [ ] `PFLICHT` **Selbst testen,** nicht nur der Aussage „fertig“ glauben. Den Ablauf in der App wirklich durchklicken.
- [ ] `SOLLTE` **Tests mitschreiben lassen** und selbst ausführen.
- [ ] `SOLLTE` **Getrennte Review-Sitzung:** Eine frische KI-Sitzung prüft den Code als Security- oder Code-Reviewer (siehe [Prüf-Prompts](./PRUEF-PROMPTS.md)).
- [ ] `SOLLTE` **Automatische Werkzeuge ergänzen** (Linter, Secret-Scan, Abhängigkeits-Scan, Supabase Advisor).
- [ ] `PFLICHT` **Security-Review nach jeder riskanten Änderung.** Änderungen an Anmeldung, Berechtigungen, Datenbank-Policies, Uploads, Zahlungen, KI-Tools und Integrationen vor dem Merge prüfen lassen – durch eine frische KI-Sitzung oder ein Werkzeug wie `/security-review`. Studien finden in rund 45 % der KI-Code-Proben Sicherheitslücken.
- [ ] `SOLLTE` **Neue Pakete prüfen,** bevor sie installiert werden (Existenz, Seriosität, Lizenz).

## D. Sicherheit der Arbeitsumgebung

- [ ] `PFLICHT` **Agent ohne Zugriff auf Produktionsdaten und Produktions-Keys.**
- [ ] `PFLICHT` **Coding-Agent nie ohne Rückfragen auf dem eigenen Rechner.** Modi, die alle Rückfragen abschalten (z. B. „skip permissions“, „YOLO“, „trust all tools“), nur in einer Sandbox, einem Devcontainer oder einer virtuellen Maschine ohne private Schlüssel nutzen. Wo vorhanden, die eingebaute Sandbox einschalten, die Datei- und Netzwerkzugriffe begrenzt. Automatische Modi, in denen eine zweite KI über Rückfragen entscheidet (bei Claude Code seit August 2026 der Startmodus), ersetzen keine Prüfung: Für Arbeiten an Anmeldung, Datenbank, Zahlungen und Deployments in den manuellen Modus wechseln oder Sperr- und Rückfrageregeln (z. B. für `git push` und Migrationen) setzen.
- [ ] `PFLICHT` **Konfiguration und Regeldateien des Agenten wie Code prüfen.** Änderungen an `.claude/`, `.cursor/`, `.vscode/settings.json`, `.vscode/tasks.json`, `.mcp.json`, Hooks, unbekannten `setup`-Skripten in diesen Ordnern, `CLAUDE.md` oder `AGENTS.md` können dem Agenten unbemerkt mehr Rechte geben oder versteckte Anweisungen (auch in unsichtbaren Unicode-Zeichen) enthalten. Nie ungelesen übernehmen; der Agent darf seine eigenen Berechtigungen nicht ändern.
- [ ] `PFLICHT` **Secrets vor dem Coding-Agenten verbergen.** `.env`-Dateien und Schlüsselordner (z. B. `~/.ssh`, Cloud-Zugangsdaten) per Sperrregel für den Agenten unlesbar machen und lokal nur Entwicklungs-Keys verwenden. Tokens für MCP-Server nicht im Klartext in Dateien speichern, die ins Repository gelangen können.
- [ ] `PFLICHT` **Datenbank-MCP nur lesend und nur für das Entwicklungsprojekt.** Den Supabase-MCP-Server (und ähnliche) auf Lesezugriff und ein Entwicklungsprojekt beschränken, ungenutzte Werkzeuge abschalten und jeden Aufruf bestätigen. Für MCP, CLI und CI ein Zugriffstoken nur für dieses Projekt, nur mit Leserechten und mit Ablaufdatum anlegen (bei Supabase „scoped personal access tokens“), nicht ein Token für das ganze Konto. Inhalte aus der Datenbank können Prompt Injection enthalten.
- [ ] `PFLICHT` **Projekt und App auf der Vibe-Coding-Plattform privat stellen, wenn echte Daten im Spiel sind.** Bei Lovable, Replit, Base44 und ähnlichen Diensten prüfen, wer Projekt (Code und KI-Chatverlauf) und veröffentlichte App sehen kann; interne Apps nur mit Anmeldung veröffentlichen. 2026 waren bei einer Plattform Code und KI-Chats öffentlicher Projekte für Fremde lesbar, und Forscher fanden Tausende Vibe-Coding-Apps mit offenen Firmen- oder Personendaten. Keys, die je in Chat oder Code eines öffentlichen Projekts standen, austauschen.
- [ ] `PFLICHT` **KI-Agenten in GitHub Actions absichern (wenn genutzt).** Nur Maintainer dürfen den Agenten auslösen. Sein Job bekommt nur Leserechte und keine weiteren Secrets, läuft nie mit `pull_request_target`, und Schreibaktionen gibt ein Mensch frei. In Issues, PR-Titeln und Kommentaren versteckte Anweisungen brachten 2026 mehrere Coding-Agenten dazu, Schlüssel preiszugeben.
- [ ] `PFLICHT` **Bestätigung für gefährliche Befehle** (Löschen, Migrationen auf entfernten Datenbanken, Force-Push, Deployments).
- [ ] `SOLLTE` **Berechtigungen des Agenten einschränken** (erlaubte Befehle, Ordner).
- [ ] `SOLLTE` **Keine echten Kundendaten** in Prompts an Coding-Agenten.
- [ ] `SOLLTE` **MCP-Server, Plugins, Skills und Erweiterungen** des Coding-Agenten nur aus vertrauenswürdigen Quellen und vor der Installation prüfen. Sie sind Code mit deinen Rechten: nur feste, geprüfte Versionen mit Wartezeit nutzen – ein kompromittiertes Gedächtnis-Plugin gab im September 2026 Prompts an Angreifer weiter.
- [ ] `SOLLTE` **Liste aller MCP-Server und Agenten-Erweiterungen führen:** Herkunft, feste Version, Rechte, verwendetes Token. Was nicht auf der Liste steht, wird entfernt (OWASP MCP Top 10, „Schatten-MCP-Server“).
- [ ] `SOLLTE` **Datenschutz-Einstellungen des Coding-Tools prüfen:** Wird dein Code zum Training verwendet? Wo werden Sitzungen gespeichert?
- [ ] `SOLLTE` **Erfundene Funktionen erkennen.** KI nutzt manchmal APIs, Parameter oder Konfigurationen, die es nicht gibt. Bei Unbekanntem in der offiziellen Dokumentation gegenprüfen.

## E. Verstehen, was du betreibst

Du musst nicht jede Zeile verstehen. Diese Punkte aber schon:

- [ ] `PFLICHT` **Wo liegen die Daten** und wer kann sie lesen?
- [ ] `PFLICHT` **Wo liegen die Secrets** und wie tauschst du sie aus?
- [ ] `PFLICHT` **Wie funktioniert die Anmeldung** und wo wird geprüft, wer was darf?
- [ ] `PFLICHT` **Wie wird deployt** und wie rollst du zurück?
- [ ] `PFLICHT` **Was kostet die App pro Monat** und wo sind die Limits eingestellt?

## F. Pflege

- [ ] `SOLLTE` **Regelmäßig aufräumen lassen:** Duplikate, tote Dateien, zu große Dateien.
- [ ] `SOLLTE` **Regeldatei aktuell halten,** wenn sich Stack oder Konventionen ändern.
- [ ] `SOLLTE` **Kosten der KI-Werkzeuge** im Blick behalten.

## G. Warnsignale – sofort stoppen und prüfen

Wenn der Agent eines davon tut, ist das ein Warnsignal:

- RLS oder Security Rules deaktiviert, „damit es funktioniert“.
- Tests gelöscht oder übersprungen, „damit sie grün sind“.
- Fehler mit `any`, `@ts-ignore`, leerem `catch` oder `eslint-disable` versteckt.
- Keys oder Passwörter direkt in den Code geschrieben.
- Öffentliche Umgebungsvariable für einen geheimen Key angelegt.
- Pakete installiert, die du nicht kennst.
- Viele Dateien geändert, obwohl eine kleine Änderung verlangt war.
- Behauptet „fertig und getestet“, ohne Testausgabe zu zeigen.
- Datenbank direkt geändert statt über Migration.
- CORS auf `*` gesetzt oder Berechtigungsprüfungen entfernt.
- Nutzt Funktionen, Parameter oder Pakete, die in der offiziellen Dokumentation nicht vorkommen.
- Ändert eigene Berechtigungs- oder Konfigurationsdateien (`.claude/`, `.vscode/`, `.mcp.json`) oder schlägt einen Modus ohne Rückfragen vor.
- Gibt bei „permission denied“ in der Datenbank einfach alles frei.

## Nachweis

Git-Historie mit kleinen, verständlichen Commits; Regeldatei für Agenten; Review-Protokolle; Liste der fünf Grundfragen aus Abschnitt E mit deinen Antworten.
