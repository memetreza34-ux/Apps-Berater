# 08 – Architektur, Aufbau und Code

Eine Vibe-Coding-App wächst schnell. Ohne klare Struktur verliert irgendwann auch der KI-Agent den Überblick: Er dupliziert Code, bricht bestehende Funktionen und findet Fehler nicht mehr. Dieses Kapitel beschreibt einen Aufbau, der auch nach Monaten wartbar bleibt.

Vertiefung: [Architektur-Entscheidungsleitfaden](../allgemeine-app-entwicklung/03-technik/architektur-entscheidungsleitfaden.md).

## A. Grundaufbau

```text
App / Browser (nur Anzeige und Eingaben, keine Geheimnisse)
        │
        ▼
Eigener Server (API-Routen, Edge Functions, Hintergrundjobs)
  – Anmeldung und Berechtigungen prüfen
  – Eingaben validieren
  – Limits und Kosten kontrollieren
        │
        ├──► KI-Anbieter (Modelle)
        ├──► Datenbank und Dateispeicher (mit RLS)
        ├──► Zahlungsanbieter (Webhooks zurück an den Server)
        └──► E-Mail, Push, Analytics, Monitoring
```

- [ ] `PFLICHT` **Client und Server trennen.** Geheimnisse, Preise, Limits, Berechtigungen und Geschäftslogik liegen auf dem Server.
- [ ] `SOLLTE` **Bewährten Stack wählen** statt Experimente (z. B. Next.js oder Expo mit Supabase und Stripe). Je bekannter der Stack, desto besser kennt ihn auch die KI.
- [ ] `SOLLTE` **Wichtige Entscheidungen festhalten** als Architecture Decision Record: [Vorlage ADR](../allgemeine-app-entwicklung/vorlagen/architecture-decision-record.md).
- [ ] `SOLLTE` **Datenfluss-Diagramm** zeichnen: Welche Daten gehen wohin? Grundlage für Datenschutz und Security.

## B. Ordnerstruktur

Beispiel für eine Web-App mit KI (anpassbar an Expo, Flutter oder andere Frameworks):

```text
app/                  Seiten und Routen
components/
  ui/                 Basis-Komponenten (Button, Input, Dialog)
  features/           Komponenten je Funktion (chat/, billing/, settings/)
lib/                  Clients und Helfer (supabase, ai, stripe, validation)
server/               Geschäftslogik, nur serverseitig
ai/
  prompts/            versionierte Prompts
  tools/              Tool-Definitionen für Agenten
  evals/              Testsammlungen und Auswertung
db/
  migrations/         versionierte Datenbank-Migrationen
  seed.sql            Testdaten (keine echten Daten)
tests/
  unit/  e2e/         automatische Tests
docs/                 PRD, Architektur, Entscheidungen, Rechtliches
.env.example          alle Variablen ohne Werte
README.md             Setup und Start
CLAUDE.md / AGENTS.md Regeln für Coding-Agenten
```

- [ ] `SOLLTE` **Nach Funktionen gliedern,** nicht alles in einen Ordner.
- [ ] `SOLLTE` **Kleine Dateien** (Richtwert unter 300–400 Zeilen). KI-Agenten arbeiten mit kleinen, klar benannten Dateien deutlich besser.
- [ ] `SOLLTE` **Einheitliche Namen** für Dateien, Funktionen, Tabellen und Spalten.
- [ ] `SOLLTE` **Server-Code klar markieren** (z. B. `server-only`-Import in Next.js), damit er nie im Browser landet.

## C. Umgebungen

- [ ] `PFLICHT` **Getrennte Umgebungen:** Entwicklung, Vorschau/Staging, Produktion – jeweils mit eigener Datenbank und eigenen Keys.
- [ ] `PFLICHT` **Nie in der Produktionsdatenbank entwickeln oder testen.**
- [ ] `SOLLTE` **Vorschau-Deployments pro Branch** oder Pull Request.
- [ ] `SOLLTE` **Vorschau-Deployments schützen.** Vorschau-Links nur mit Anmeldung erreichbar machen (z. B. Vercel Deployment Protection) und dort nie Produktionsdaten oder Produktions-Keys verwenden.
- [ ] `SOLLTE` **Lokale Entwicklung** mit lokaler Datenbank (z. B. Supabase CLI) statt direkt gegen die Cloud.

## D. Datenbank

- [ ] `PFLICHT` **Migrationen im Repository** versionieren. Änderungen nicht nur im Dashboard klicken – sonst weiß niemand, wie die Produktion aussieht.
- [ ] `SOLLTE` **Standardspalten:** `id` (UUID), `created_at`, `updated_at`, Besitzer (`user_id` oder `org_id`), ggf. `deleted_at`.
- [ ] `SOLLTE` **Fremdschlüssel, Pflichtfelder und Prüfregeln** in der Datenbank (`FOREIGN KEY`, `NOT NULL`, `CHECK`), nicht nur im Code.
- [ ] `SOLLTE` **Indizes** für häufige Abfragen und Filter.
- [ ] `SOLLTE` **Mandantenfähigkeit früh planen,** wenn Teams oder Firmen die App nutzen sollen (`org_id` statt nur `user_id`).
- [ ] `SOLLTE` **Geldbeträge als Ganzzahl in Cent** (oder als Dezimaltyp) speichern, nie als Fließkommazahl, und Rundungsregeln festlegen.
- [ ] `SOLLTE` **Zeitangaben in UTC speichern** und erst in der Oberfläche in die lokale Zeitzone umrechnen.
- [ ] `SOLLTE` **Weiches Löschen bewusst einsetzen.** `deleted_at` ist praktisch für „Rückgängig“, ersetzt aber nicht die echte Löschung nach DSGVO – eine Frist für endgültiges Löschen festlegen.
- [ ] `SOLLTE` **Typen aus dem Schema generieren** (z. B. `supabase gen types`), damit Code und Datenbank zusammenpassen.
- [ ] `SOLLTE` **Migrationen rückwärtskompatibel** gestalten (erst neue Spalte hinzufügen, dann Code umstellen, dann alte entfernen). Vertiefung: [Runbook Datenbankmigration und Rollback](../allgemeine-app-entwicklung/15-runbooks/datenbankmigration-und-rollback.md).

## E. Code-Qualität

- [ ] `SOLLTE` **TypeScript im strikten Modus** (oder die typsichere Variante deiner Sprache).
- [ ] `SOLLTE` **Linter und Formatter** (z. B. ESLint, Biome, Prettier) automatisch bei jedem Commit.
- [ ] `SOLLTE` **Keine Duplikate.** KI kopiert gern Code. Gemeinsame Logik in zentrale Helfer.
- [ ] `SOLLTE` **Einheitliche Fehlerbehandlung** (Fehlergrenzen im UI, einheitliches Fehlerformat in der API).
- [ ] `SOLLTE` **Kein toter Code,** keine auskommentierten Blöcke, keine Test-Dateien wie `test2-final-neu.ts`.
- [ ] `SOLLTE` **Konfiguration zentral** (Limits, Preise, Feature-Flags) statt verstreuter fester Werte.
- [ ] `SOLLTE` **Keine leeren `catch`-Blöcke** und kein `any`, um Fehler zu verstecken.

## F. API-Gestaltung

- [ ] `SOLLTE` **Einheitliche Endpunkte, HTTP-Statuscodes und Fehlerformate.**
- [ ] `SOLLTE` **Eingaben am Eingang validieren,** Ausgaben auf das Nötige begrenzen (keine kompletten Datenbankzeilen mit internen Feldern zurückgeben).
- [ ] `SOLLTE` **Antworten fremder Dienste prüfen.** Antworten von Dritt-APIs sind ungeprüfte Eingaben: gegen ein Schema prüfen, Größe und Zeit begrenzen und nicht ungeprüft speichern oder anzeigen (OWASP API Security Top 10, API10).
- [ ] `SOLLTE` **Seitenweise Ausgabe** (Pagination) bei Listen.
- [ ] `SOLLTE` **Idempotenz-Schlüssel** bei Zahlungen und Erstellungen.
- [ ] `KANN` **Versionierung und OpenAPI-Dokumentation,** sobald Dritte deine API nutzen.

## G. Hintergrundjobs und Zeitpläne

- [ ] `SOLLTE` **Warteschlange für lange Aufgaben** (KI-Verarbeitung, E-Mails, Exporte), z. B. mit Inngest, Trigger.dev oder Datenbank-Cron.
- [ ] `SOLLTE` **Geplante Aufräumjobs:** alte Uploads, abgelaufene Daten, Logs nach Frist löschen.
- [ ] `SOLLTE` **Fehlgeschlagene Jobs sichtbar** machen und wiederholen können.

## H. Echtzeit, Synchronisation und Offline

- [ ] `SOLLTE` **Offline-Verhalten festlegen:** Was geht ohne Netz, was wird zwischengespeichert, was wird später gesendet?
- [ ] `SOLLTE` **Konflikte lösen,** wenn dieselben Daten auf zwei Geräten geändert wurden (z. B. letzte Änderung gewinnt, Zusammenführen oder Nachfrage).
- [ ] `SOLLTE` **Echtzeit-Kanäle absichern:** Abonnements nur auf Daten, die der Nutzer sehen darf (z. B. Supabase Realtime mit RLS).
- [ ] `KANN` **Lokale Datenbank** auf dem Gerät für Apps, die offline voll funktionieren sollen.

## I. Automatische Prüfungen (CI)

- [ ] `PFLICHT` **Bei jedem Push:** Build, Typprüfung und Linter automatisch (z. B. GitHub Actions). Vorlagen: [CI-Templates](../allgemeine-app-entwicklung/13-automatisierung/README.md).
- [ ] `SOLLTE` **Tests für kritische Wege:** Anmeldung, Berechtigungen, Zahlung, Limits, Datenlöschung.
- [ ] `SOLLTE` **End-to-End-Test des Kernablaufs** (z. B. Playwright, Maestro oder Detox).
- [ ] `SOLLTE` **Datenbank-Policies testen** (zwei Nutzer, siehe [05](./05-sicherheit-grundlagen.md)).
- [ ] `SOLLTE` **Merge nur bei grünen Prüfungen** (Branch-Schutz für `main`).

## J. Dokumentation

- [ ] `PFLICHT` **README:** Was ist die App, wie startet man sie lokal, welche Umgebungsvariablen braucht sie, wie wird deployt.
- [ ] `SOLLTE` **Regeln für Coding-Agenten** in `CLAUDE.md` oder `AGENTS.md`: Stack, Ordnerstruktur, Konventionen, Befehle für Tests, Verbote (z. B. „nie RLS deaktivieren“, „nie Keys im Client“, „Datenbankänderungen nur als Migration“).
- [ ] `SOLLTE` **PRD und Architektur** in `docs/` – kurz, aber aktuell.
- [ ] `SOLLTE` **Datenmodell** als Diagramm oder Tabelle.
- [ ] `SOLLTE` **Änderungsprotokoll** (CHANGELOG) für Releases.

## K. Leistung

- [ ] `SOLLTE` **Bilder optimieren** (moderne Formate, passende Größen, Lazy Loading).
- [ ] `SOLLTE` **Code aufteilen** (nur laden, was die Seite braucht).
- [ ] `SOLLTE` **Keine Abfragen in Schleifen** (N+1-Problem).
- [ ] `SOLLTE` **Caching** für statische Inhalte und häufige Abfragen (CDN).
- [ ] `SOLLTE` **Core Web Vitals mit festen Grenzwerten.** Für 75 % der Besuche gilt: größter Inhalt in höchstens 2,5 Sekunden sichtbar (LCP), Reaktion auf Eingaben in höchstens 200 ms (INP), Layout-Verschiebung höchstens 0,1 (CLS). Prüfen mit PageSpeed Insights oder der Search Console.

## Typische Fehler beim Vibe-Coding

- Tabellen im Supabase-Dashboard angelegt, keine Migrationen vorhanden.
- Eine 2.000-Zeilen-Datei `page.tsx`, die alles enthält.
- Kein CI – Fehler fallen erst in Produktion auf.
- Dieselbe Hilfsfunktion fünfmal leicht anders.
- Kein README, niemand weiß mehr, welche Variablen nötig sind.

## Nachweis

Architekturdiagramm, Migrationsordner, grüner CI-Lauf, README mit Setup, Agenten-Regeldatei.
