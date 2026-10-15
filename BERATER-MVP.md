# Apps-Berater – Produktentscheidung und MVP

Stand: 15. Oktober 2026 · Strategie und Spezifikation, noch keine fertige Web-App

## Entscheidung

**Ja: zuerst einen kleinen, praktisch einsetzbaren KI-App-Berater fertigstellen und sofort mit Secret Circle erproben. Nein: nicht zuerst ein mehrmonatiges eigenständiges SaaS bauen.**

Der vorhandene Wissensunterbau (14 Schritte, Kriterienkatalog, Prüfer, Vorlagen) ist die Wissensbasis. Das Produkt muss daraus **situative, nachweisbare Entscheidungen** für ein bestimmtes GitHub-App-Projekt machen.

## Zielgruppe und Nutzen

Startzielgruppe: ein Solo-Gründer, der App-Produkte mit ChatGPT, Claude Code und Codex entwickelt, die technische Qualität nicht selbst komplett überprüfen kann und einen roten Faden von der Idee bis zum Release braucht.

Der Berater weiß nicht automatisch alles. Er muss den **aktuellen Repository-Zustand** lesen, das Ziel und die Phase ermitteln, relevante Regeln und Belege auswählen, Risiken benennen, die nächste beste Aufgabe festlegen und sie einem geeigneten Agenten zuweisen. Das System darf ohne echte Prüfung kein „fertig“, „sicher“, „rechtskonform“ oder „releasebereit“ behaupten.

## Abgrenzung der Versionen

### V0 – Sofort nutzbarer Berater innerhalb von ChatGPT/Claude Code (jetzt)

Kein eigenes UI und kein Login nötig. `BERATER-ARBEITSMODUS.md` steuert einen KI-Agenten mit Zugriff auf dieses Wissen und nach Berechtigung auf das App-Repository.

Sechs Kommandos (natürliche Sprache, keine Pflicht-Syntax):

| Anliegen | Verhalten |
| --- | --- |
| „Neue App planen“ | Problem, Zielgruppe, MVP, Geschäft, Risiken, Architektur |
| „App übernehmen“ | Brownfield-Audit: bestehende Implementierung, Dokumentation, CI, PRs, offene Blocker |
| „Status“ | belegter IST-Zustand, Unbekanntes, Unterschiede zu Roadmap und Release-Gates |
| „Was als Nächstes?“ | genau ein priorisierter Arbeitsschritt samt Akzeptanzkriterien und Owner |
| „Design prüfen“ | UX, Zugänglichkeit, Konsistenz, Screens, echte Benutzungsprobleme |
| „Release prüfen“ | passende Kriterien, tatsächliche Tests, Geräte/Operator/Legal, GO nur nach Belegen |

Für technische Umsetzung Claude Code, für Bildwelt Codex und für Geschäftsentscheidungen den Produktinhaber/ChatGPT einsetzen (pro Projekt konfigurierbar; nicht als allgemeines Gesetz festschreiben). **Ein Modell ist nicht automatisch das beste für jede Aufgabe**: leistungsfähigstes verfügbares und zweckmäßiges Modell wählen, Kosten und Limits prüfen.

### V1 – Benutzeroberfläche, erst nach V0-Pilot

Web-App mit Projektübersicht und KI-Chat. Hauptansichten:
1. **Projekte** – GitHub-Repository hinzufügen, Zweck, Zielgruppe, Plattform, Phase.
2. **Cockpit** – nächster Schritt, kritische Blocker, letzte verifizierte Checks, offene Entscheidungen und Kostenrisiken.
3. **Berater-Chat** – kontextbezogene Antworten mit Links zu Repo-Dateien/Commits/Tests und zum eigenen Wissenskatalog.
4. **Aufgaben** – priorisierte Issues für Claude/Codex; Freigaben durch den Nutzer.
5. **Design** – Screen-/Screenshot-Feedback anhand eines projektspezifischen Designsystems.
6. **Release** – versionsgebundene Evidence-Matrix; GO/NO_GO und Gründe.
7. **Lernen** – jedes Feature erklärt: Was, Warum, Welche Dateien, Wie getestet, Was offen.

V1 muss nicht selbst programmieren, Bilder generieren oder ohne Nutzerfreigabe Änderungen schreiben. Auf Wunsch können zunächst nur lesende GitHub-Rechte erteilt werden.

### V2 – Nur bei nachgewiesenem Bedarf

Automatische zeitgesteuerte Repo-Checks, Notifications, Teams, mehrere Projekte, Kosten-/Umsatzdashboard, öffentliche SaaS-Monetarisierung. Eine laufende autonome Beobachtung erfordert eine echte geplante Ausführung und Berechtigungen; reine Markdown-Anweisungen oder eine Chat-Sitzung beobachten **nicht** ständig im Hintergrund.

## Technische Zielarchitektur für eine mögliche V1

- **Frontend:** responsive Web-App; bewusst einfache, barrierearme Navigation.
- **Backend:** serverseitige API, GitHub OAuth/App-Integration mit minimalen Scopes, sichere Credentials, Repos getrennt pro Nutzer, Rate-Limits und Kostenbudgets.
- **Wissensbasis:** die vorhandenen Markdown-Dateien; nur relevante Abschnitte je Frage laden, Quellenbezug, Gültigkeitsdatum und Version erfassen.
- **Projektzustand:** Repository-Stand/Commit-SHA, aktuelle Phase, offene Issues/PRs, Testnachweise, Entscheidungen, Risiken und nächste Aufgabe. Projektspezifische Zustände getrennt speichern.
- **KI:** austauschbare Anbieter/Modelle über kontrollierten Server; Tool-Ausgaben untrusted, keine ungeprüften Tools/Code-Ausführung aus Dokumenten; keine Secrets in Prompts oder Client.
- **Belege:** Status (belegt / teilweise / offen / nicht anwendbar / unbekannt), Quelle, Commit-SHA, Zeitpunkt, Testumgebung, Reviewer.
- **Schreibaktionen:** Branch/Issue/PR nur nach bewusstem Auftrag. Niemals direkt unbestätigt deployen, mergen, löschen, bezahlen oder produktive Daten migrieren.
- **Betrieb:** Monitoring, Löschung/Export, Zugriffsschutz, Backups, Datenschutz, Kostenalarm und Sicherheitsprüfungen, bevor V1 echte Kundendaten erhält.

Die Stackwahl (beispielsweise Next.js/React, Postgres und Auth) erfolgt erst nach einer kurzen Architekturentscheidung. Keine neuen Dienste nur wegen eines Trends.

## Prinzip für die 1.100+ Prüfpunkte

Nicht jeden Katalogpunkt für jede App blind als Pflicht ausgeben. Profil → betroffene Produktarten und Plattformen → **zutreffende bedingte Regeln** → Priorität anhand Schaden und tatsächlicher Releasesituation. Der Katalog ist eine umfassende Hilfestellung, **keine automatische Rechtszertifizierung**.

Bei einer bestehenden App startet der Berater nicht von vorn. Er prüft vorhandene Artefakte und Beweise, identifiziert den aktuellen Stand und erstellt nur fehlende Grundlagen nach.

## Pilot & klare Erfolgskriterien

**Pilot-App:** Secret Circle (offline-first PWA). Siehe `PILOT-SECRET-CIRCLE.md`.

V0 gilt als hilfreich, wenn:
1. Der Berater Secret Circle aus dem echten GitHub-Repo korrekt als bestehendes, noch nicht releasefreies Produkt erkennt.
2. Die nächste Aufgabe von einer Testperson als sinnvoll bestätigt wird und keine unkontrollierte Neuentwicklung auslöst.
3. Der Berater Claude/Codex-Aufträge passend trennt und Akzeptanzkriterien/Testnachweise nennt.
4. Bereits erledigte Arbeiten nicht als neu ausgegeben und laufende PRs nicht blind gemergt werden.
5. Der Berater ohne belegte CI, reale Gerätetests und Betreiberangaben keine Veröffentlichung freigibt.
6. Der Nutzer jedes technische Arbeitspaket in einfachen Worten erklärt bekommt.

Bewertet werden: Korrektheit der Statusmeldung, Anzahl falscher Erfolgsaussagen (Ziel **null**), Aufwand bis zur nächsten nutzbaren Aufgabe und Verständlichkeit. Kein erfundener Prozentwert ohne definierte Berechnungsgrundlage.

## In diesem MVP ausdrücklich nicht

Keine komplette Neuschreibung des Wissenskatalogs; keine automatisch generierte „100 % rechtskonform“-Bewertung; kein unnötiges Abo-/Login-System; keine mobile Store-App; kein autonomer Agent mit unkontrollierten Produktionsrechten; keine Unterbrechung der Secret-Circle-P0-Arbeit durch neue Design-Experimente.

## Weiterarbeit

**Schritt 1:** Diesen Konzept-PR prüfen und V0 mit echtem Secret-Circle-Zustand testen.  
**Schritt 2:** Zu den sechs Kommandos konkrete Musterfälle und echte Ergebnisse dokumentieren; Widersprüche im Katalog korrigieren.  
**Schritt 3:** Erst bei erkennbarem Nutzen V1 mit einem minimalen Projektcockpit und Chat technisch implementieren.  
**Schritt 4:** Monetarisierung für Dritte erst nach Nutzerinterviews, Sicherheits-/Rechtsprüfung und messbarem Mehrwert.
