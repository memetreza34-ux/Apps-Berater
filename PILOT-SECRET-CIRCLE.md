# V0-Pilot – Secret Circle mit Apps-Berater begleiten

Stand der Ausgangsinformationen: 14.–15. Oktober 2026. **Momentaufnahme, keine Live-Freigabe.** Vor jeder neuen Entscheidung GitHub erneut lesen.

**App-Repo:** https://github.com/memetreza34-ux/Secret-Circle  
**Wissens-Repo:** https://github.com/memetreza34-ux/Apps-Berater

## Warum dieses Pilotprojekt?

Secret Circle ist eine bereits umfangreich entwickelte **offline-first Partyspiel-PWA**. Dokumentierter Stand: 55 Built-ins, davon 15 Kernspiele. Es gibt echten Quellcode, Playwright- und Vertragstests, GitHub Issues und mehrere offene Release-/Design-PRs. Das Produkt zeigt, ob der Berater mit einem bestehenden, komplexen Projekt umgehen kann, statt ein leeres Demo-Projekt zu kommentieren.

## Produktziel

Zuerst eine stabile, verständliche, deutschsprachige **Web-/PWA-Version** mit 15 belastbaren Kernspielen veröffentlichen. Native Store-Apps und Monetarisierung sind separate spätere Entscheidungen, keine stillen neuen Release-Abhängigkeiten. Ein fertiges UI oder viele Spiele bedeuten nicht, dass reale Geräte- und Gruppenprüfungen bereits bestanden wurden.

## Rollen – verbindlich für diesen Pilot

- **ChatGPT:** Projektleitung, Planung, IST-/Risikoanalyse, Review, Business.
- **Claude Code:** Technik, Gameplay, PWA, Routing, Speicherung, Tests, Sicherheit und technische Designimplementierung.
- **Codex:** Bildideen, Bildprompts, Bildvarianten und nur nötige Assetintegration (keine Spiellogik).
- **Arman:** Produktauswahl, Abnahme von Bildern, echte Nutzer-/Gerätetests, Hosting/Betreiberangaben, Veröffentlichung.

Wo eine Modellwahl möglich ist, das beste zum Auftrag passende verfügbare Modell nutzen; keine fixe Modellversion.

## Bekannte Prüfpunkte beim Start

- **Release:** NO_GO bis zu echten Abnahmen.
- **Technische Prioritäten:** https://github.com/memetreza34-ux/Secret-Circle/issues/24
- **Geräte-/Gruppennachweise:** https://github.com/memetreza34-ux/Secret-Circle/issues/8
- **Hosting/Operator/Legal/Support:** https://github.com/memetreza34-ux/Secret-Circle/issues/14
- **KI-Rollen-/Workflow-Einführung:** https://github.com/memetreza34-ux/Secret-Circle/pull/31 (bei Erstellung Draft; aktuellen Status nachprüfen).
- **Bildwelt:** https://github.com/memetreza34-ux/Secret-Circle/pull/30 – bei Sichtung Änderungsliste nicht nur Dokumentation, sondern auch JS/CSS/SW/Bilder/Audits/Tests. Deshalb **Diff und CI des neuen Head-SHA** vor Merge prüfen.
- **Routing:** Webroot `/` und `index.html` zeigen laut bestehender technischer Dokumentation Word Imposter, während Manifest `v2-hub.html` als Einstieg nennt. Aktuellen Code neu prüfen, bevor daraus ein neuer Defekt oder eine Aufgabe abgeleitet wird.

## Erste Beratersitzung – prüfbarer Ablauf

1. Aktuelles `main`-SHA, offene PRs und Issues, letzte wirklich ausgeführten CI-Jobs abrufen.
2. Die Produkt-/Release-Regeln aus `AGENTS.md`, `RELEASE_CHECKLIST.md`, `release-evidence.json` und Issue #24 lesen.
3. Dokumentation gegen den **tatsächlichen** Code und die betroffenen PR-Diffs abgleichen.
4. Einen einzelnen P0-Blocker auswählen, dessen Behebung für den Release nachweisbar ist.
5. Claude einen kleinen technischen Auftrag geben (Problem, Dateien, Schutzverträge, Akzeptanztests, Branch, Rollback).
6. Codex **nur** zur Bildarbeit beauftragen, wenn dies mit dem jeweiligen technischen Release-Gate und der Bildabnahme vereinbar ist.
7. Nach Review: tatsächlichen CI-/Gerätebeleg notieren, Fortschritt aktualisieren, nächsten Schritt auswählen.

## Beispiel-Ausgabe (muss bei echter Sitzung aktualisiert werden)

**IST:** Secret Circle existiert bereits und hat ein umfangreiches Spiel- und Testsystem. Die Dokumente führen noch offene technische und reale Release-Gates.  
**Größter zuerst zu prüfender Blocker:** Sind Branches/PRs und aktueller CI-Stand konsolidiert, bevor wir weitere Änderungen mergen?  
**Nächste Aufgabe:** Aktuelle offenen PR-Diffs + CI-SHA prüfen, fehlerhafte Scope-/Testbehauptungen berichtigen, sicheren Integrationspfad nennen.  
**Owner:** Claude für technische Analyse/PR, ChatGPT für Review, Codex nicht erforderlich.  
**Abnahme:** präzise Liste aller betroffenen PRs und Head-SHAs, CI-Beweise pro relevantem SHA, dokumentierte Merge-Reihenfolge, keine ungeprüften Commits.

Dieses Beispiel stellt **keine** tatsächlich durchgeführte Prüfung der aktuellen GitHub-Daten dar.

## Pilot-Abnahme

Berater kann an drei aufeinanderfolgenden Sitzungen einen neuen Commit-/PR-Stand aufnehmen, zwischen BELEGT/UNBEKANNT unterscheiden, ein relevantes Issue priorisieren, korrekte Agent-Aufträge geben und keine neue Funktion oder Bildarbeit anstoßen, die kritische Tests blockiert.

Nach Abschluss des Pilots entscheiden wir, ob ein eigenständiges UI für Projekt-Cockpit und Beratung den zusätzlichen Aufwand wert ist.
