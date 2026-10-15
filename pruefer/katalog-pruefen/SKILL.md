---
name: katalog-pruefen
description: Prüft und aktualisiert den KI-App-Kriterienkatalog im Repo Apps-Berater (wissen/ki-app-kriterienkatalog) vollständig – recherchiert neue Gesetze, Store-Regeln, Sicherheitsstandards und Best Practices, gleicht jeden Punkt ab, ergänzt alles Fehlende mit Quelle, korrigiert Veraltetes, prüft Struktur und Themenabdeckung automatisch und öffnet einen PR. Auslösen bei /katalog-pruefen oder wenn der Nutzer sagt „prüf den Katalog nochmal“, „ist der Katalog vollständig“, „aktualisiere die Liste“, „was fehlt im Katalog“.
argument-hint: "[schnell | mergen | Thema wie recht, stores, sicherheit, ki]"
---

# Katalog prüfen und vervollständigen

Ziel: Der KI-App-Kriterienkatalog soll **jedes** Kriterium enthalten, das eine App braucht, die jemand ohne Programmierkenntnisse nur mit KI baut – aktuell, belegt und fehlerfrei. Du arbeitest gründlich, nicht schnell. Lieber eine Stunde Recherche als ein vergessener Pflichtpunkt.

Argumente: `$ARGUMENTS`

- leer → vollständiger Durchlauf (Schritte 1–8)
- `schnell` → nur Schritt 1, 2 und 6 (Struktur und Themenabdeckung, keine Webrecherche)
- `mergen` → am Ende PR ohne weitere Rückfrage mergen, wenn alle Prüfungen grün sind
- Thema (`recht`, `datenschutz`, `stores`, `sicherheit`, `ki`, `ux`, `business`, `launch`) → Recherche nur für diesen Bereich, Strukturprüfung trotzdem komplett

Wichtige Pfade:

- Repo: `~/Apps-Berater` (GitHub `memetreza34-ux/Apps-Berater`)
- Katalog: `~/Apps-Berater/wissen/ki-app-kriterienkatalog/`
- Prüfskript: `python3 ~/Apps-Berater/pruefer/katalog-pruefen/katalog_check.py ~/Apps-Berater`

## Grundregeln

1. **Nichts raten.** Jede neue oder geänderte Aussage zu Gesetzen, Fristen, Zahlen oder Store-Regeln braucht eine Quelle – möglichst die Primärquelle (EUR-Lex, gesetze-im-internet.de, Apple/Google-Dokumentation, OWASP, Behörden). Ohne Primärquelle mindestens zwei unabhängige seriöse Fachquellen. Unsichere Punkte vorsichtig formulieren („aktuelle Fassung prüfen“) statt Details zu erfinden.
2. **Format einhalten:** `- [ ] \`PFLICHT|SOLLTE|KANN\` **Kurzer Titel** – Erklärung in ein bis zwei einfachen Sätzen.` Deutsch, kurze Sätze, keine Emojis, Fachwörter kurz erklären.
3. **Stufen richtig wählen:** `PFLICHT` nur bei Gesetz, verbindlicher Store-Regel oder kritischem Sicherheitsrisiko (bedingte Pflichten mit „wenn …“ kennzeichnen). `SOLLTE` für bewährte Praxis. `KANN` für Profi-Niveau.
4. **Keine Dopplungen.** Vor jedem neuen Punkt im ganzen Katalog suchen (`grep -ri`), ob er schon existiert. Dann lieber den bestehenden Punkt präzisieren.
5. **Nicht auf `main` arbeiten.** Eigener Branch, Commit, PR. Nur mergen, wenn der Nutzer es sagt oder `mergen` als Argument gesetzt ist.
6. **Ehrlich berichten.** 100 % Vollständigkeit kann niemand garantieren. Du lieferst belegte Abdeckung: welche Rahmenwerke geprüft, welche Themen abgedeckt, was offen bleibt.

## Schritt 1 – Repo vorbereiten

1. Existiert `~/Apps-Berater` nicht: `git clone https://github.com/memetreza34-ux/Apps-Berater.git ~/Apps-Berater`.
2. Hat das Repo uncommittete Änderungen: nicht überschreiben – den Nutzer fragen.
3. `git checkout main && git pull --ff-only`, dann Branch `docs/katalog-pruefung-JJJJ-MM-TT` anlegen.
4. Offene PRs zum Katalog prüfen (`gh pr list`). Gibt es welche, den Nutzer darauf hinweisen, bevor du weiterarbeitest.

## Schritt 2 – Ausgangslage messen

1. Prüfskript ausführen und Ergebnis notieren (Punkte je Stufe, Themenabdeckung, Fehler).
2. `python3 scripts/validate_handbook.py` und `python3 scripts/validate_master_guide.py` im Repo ausführen.
3. Katalog vollständig lesen: `README.md`, alle Kapitel `01`–`17`, `QUELLEN-UND-STAND.md`, `VOLLSTAENDIGKEITSPRUEFUNG.md`, `PRUEF-PROMPTS.md`.
4. Aus `QUELLEN-UND-STAND.md` das Datum der letzten Prüfung lesen. Die Recherche deckt mindestens den Zeitraum seit diesem Datum ab.

## Schritt 3 – Recherche (parallel mit Subagenten)

Starte fünf Subagenten parallel (Typ `general-purpose`, im Hintergrund). Jeder bekommt: das Datum der letzten Prüfung, heutiges Datum, Pfad zum Katalog, die Grundregeln 1–3 und seinen Bereich. Jeder soll **nur recherchieren und nichts ändern** und eine Tabelle zurückgeben:

`Thema | Neue oder geänderte Regel (1–2 Sätze) | gilt ab | Quelle(n) mit URL | Primärquelle ja/nein | betroffenes Kapitel | Vorschlag: neuer Punkt / Änderung / Löschung | Stufe | Sicherheit hoch/mittel/niedrig`

Außerdem soll jeder mit `grep` prüfen, ob sein Fund schon im Katalog steht, und das in der Tabelle vermerken.

**Bereich A – KI-Recht EU und Deutschland:** AI Act (Änderungen, Durchführungsrechtsakte, Leitlinien und Verhaltenskodizes des AI Office, harmonisierte Normen, Fristen), KI-MIG und Bundesnetzagentur, Produkthaftung (deutsche Umsetzung), Cyber Resilience Act, DSA, DMA, Data Act, Digital Fairness Act, politische Werbung, neue Gerichtsurteile zu KI.

**Bereich B – Datenschutz, Verbraucher, Urheber, Steuern:** DSGVO-Änderungen (auch Digital-Omnibus-Vorschläge zur DSGVO und zu Cookies), EDPB und DSK zu KI, TDDDG, BGB, UWG, PAngV, DDG, VSBG, BFSG, Jugendschutz (JuSchG, JMStV), Urheberrecht und KI-Urteile (z. B. zu Trainingsdaten und Songtexten), UStG, E-Rechnung, Kleinunternehmer.

**Bereich C – Plattformen und Anbieter:** Apple App Review Guidelines und Developer News, Google-Play-Richtlinienankündigungen, Alters- und Kinderschutz-Schnittstellen der Stores, Kennzeichnungsregeln von YouTube, TikTok und Meta für KI-Inhalte, Nutzungsrichtlinien von OpenAI, Anthropic und Google für Apps, typische Modell-Abkündigungsregeln.

**Bereich D – Sicherheit:** OWASP (LLM Top 10, Agentic Top 10, Web Top 10, ASVS, MASVS, MCP-Sicherheit), NIST (AI RMF, GenAI-Profil), BSI-Veröffentlichungen zu KI und Webanwendungen, aktuelle Studien und Vorfälle zu Vibe-Coding-Apps, Angriffe auf npm und PyPI, MCP- und Agenten-Sicherheit, Supabase- und Firebase-Sicherheitshinweise.

**Bereich E – Produkt, UX, Barrierefreiheit, Launch:** WCAG und EN 301 549 (neue Versionen), EU-Barrierefreiheitsrecht, Best Practices für KI-UX (Transparenz, Vertrauen, Fehler), App Store Optimization, Auffindbarkeit in KI-Suchen, Werberecht im Marketing, aktuelle Checklisten für den Launch von KI-Apps.

Bei Argument `schnell` diesen Schritt überspringen. Bei einem Thema-Argument nur den passenden Bereich starten.

## Schritt 4 – Systematischer Lückenabgleich

Zusätzlich zur Recherche selbst prüfen:

1. **Rahmenwerke:** Jede Tabelle in `VOLLSTAENDIGKEITSPRUEFUNG.md` Zeile für Zeile gegen die aktuellen Fassungen der Rahmenwerke abgleichen (neue Artikel, neue Einträge, geänderte Nummern). Fehlt ein Rahmenwerk, das für KI-Apps inzwischen wichtig ist: neue Tabelle ergänzen.
2. **Lebenszyklus einer App:** Gedanklich eine KI-App von der Idee bis zur Einstellung durchgehen (Idee → Recht → Design → Bauen → KI → Daten → Zahlung → Tests → Store → Launch → Betrieb → Wachstum → Ende). Für jeden Schritt fragen: Was muss ein Anfänger hier wissen, was nicht im Katalog steht?
3. **App-Typen:** Für jede Art in Kapitel 15 und weitere verbreitete Arten (z. B. Chat-Apps, Bild-/Video-Generatoren, Coaching, Lernen, Finanzen, Gesundheit, Produktivität, Social, Spiele, B2B-SaaS, Agenten) prüfen, ob eigene Pflichten fehlen.
4. **Aktualität:** Jede Zeile der Tabelle „Zeitabhängige Kernaussagen“ in `QUELLEN-UND-STAND.md` prüfen: Gilt die Aussage noch? Ist eine Frist abgelaufen, sodass der Text angepasst werden muss (z. B. „ab“ statt „bis“)?
5. **Themenliste des Prüfskripts:** Für jedes neue Thema, das in den Katalog kommt, einen Eintrag in `THEMEN` in `pruefer/katalog-pruefen/katalog_check.py` ergänzen, damit es künftig automatisch überwacht wird.

## Schritt 5 – Einarbeiten

1. Funde nach Sicherheit filtern: Nur `hoch` direkt übernehmen. `mittel` vorsichtig formuliert übernehmen. `niedrig` nur als Beobachtungspunkt in `VOLLSTAENDIGKEITSPRUEFUNG.md` („Beobachten“).
2. Jeden Fund im passenden Kapitel und Abschnitt einfügen, bestehende Punkte präzisieren, veraltete Punkte korrigieren oder entfernen.
3. Neue Abschnitte fortlaufend benennen (A, B, C …) und nachfolgende Buchstaben anpassen. Verweise auf Abschnitte in anderen Dateien mitziehen.
4. Aktualisieren:
   - `README.md`: Anzahl („über N abhakbare Prüfpunkte in K Kapiteln“, N auf volle Hundert abrunden), Stand-Datum, Kapiteltabelle, ggf. die 30 Blocker
   - `QUELLEN-UND-STAND.md`: „Letzte Prüfung“, „Nächste planmäßige Prüfung“ (drei Monate später), neue Zeilen in der Tabelle, neue Primärquellen, Änderungsprotokoll
   - `VOLLSTAENDIGKEITSPRUEFUNG.md`: Prüfdatum, neue Tabellen oder Zeilen, neuer Abschnitt „Prüfung vom JJJJ-MM-TT“ mit allen Ergänzungen je Kapitel, Liste „Beobachten“
   - `PRUEF-PROMPTS.md`, falls neue Kapitel oder Prüfbereiche entstanden sind
   - `pruefer/ki-app-check/SKILL.md`, falls sich Kapitelnummern oder Stichwort-Zuordnungen geändert haben

## Schritt 6 – Automatisch prüfen

Alle drei müssen fehlerfrei sein, sonst beheben und erneut ausführen:

1. `python3 ~/Apps-Berater/pruefer/katalog-pruefen/katalog_check.py ~/Apps-Berater`
2. `python3 scripts/validate_handbook.py`
3. `python3 scripts/validate_master_guide.py`

Danach jede in dieser Runde geänderte Datei einmal vollständig lesen: Stimmen Grammatik, Stufen, Verweise und Reihenfolge?

## Schritt 7 – Commit und PR

1. Commit mit aussagekräftiger Nachricht (was recherchiert, was ergänzt, neue Punktzahl). Die Attribution-Zeilen aus dem System verwenden.
2. Push, PR gegen `main` öffnen. PR-Beschreibung: Zusammenfassung, Liste der Ergänzungen je Kapitel, neue Quellen, Ergebnis der drei Prüfungen.
3. Nur bei Argument `mergen` (oder ausdrücklicher Zustimmung des Nutzers) mergen, danach lokal `main` aktualisieren und Schritt 6 auf `main` wiederholen.

Hat die Recherche nichts Neues ergeben und das Prüfskript ist grün: trotzdem `QUELLEN-UND-STAND.md` und `VOLLSTAENDIGKEITSPRUEFUNG.md` mit dem Prüfdatum und „keine Änderungen nötig“ aktualisieren, damit die Prüfung dokumentiert ist.

## Schritt 8 – Bericht an den Nutzer

Kurz, einfach, auf Deutsch:

1. **Ergebnis in einem Satz** (z. B. „14 neue Punkte, 3 korrigiert, alle 160 Pflichtthemen abgedeckt, alle Prüfungen fehlerfrei.“)
2. **Was sich geändert hatte** (neue Gesetze oder Regeln, die wichtigsten zuerst)
3. **Was gefehlt hat** (nach Kapitel)
4. **Was offen bleibt** (Beobachten-Liste, unsichere Funde)
5. **PR-Link** und ob gemergt wurde
6. **Quellen** als Markdown-Links
