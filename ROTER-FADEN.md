# Roter Faden – von der Idee bis zum Betrieb

Jede App geht diesen Weg. Die KI arbeitet immer in **einem** Schritt und geht erst weiter, wenn „Fertig, wenn“ erfüllt und nachgewiesen ist. Schritte dürfen kurz sein – überspringen darf man sie nicht.

| Nr. | Schritt | Ergebnis |
|---|---|---|
| 1 | Idee prüfen | Problem, Zielgruppe, Stop-Kriterien |
| 2 | Recht und Risiko einordnen | Risikoprofil und Sonderfälle |
| 3 | Geschäftsmodell und Kosten | Preis und Kosten pro Nutzer |
| 4 | Produkt festlegen (PRD und MVP) | kleinste sinnvolle Version |
| 5 | Abläufe, Funktionen und Daten | Nutzerabläufe, Screen-Liste, Datenliste |
| 6 | Design und Prototyp | getesteter Klick-Prototyp, Designsystem |
| 7 | Plattform und Architektur | Aufbau, Datenmodell, Berechtigungen |
| 8 | Arbeitsumgebung und KI-Agent | Repository, Umgebungen, Regeln, automatische Prüfungen |
| 9 | Ersten Kernablauf bauen | ein Ablauf vollständig, sicher und getestet |
| 10 | Weitere Funktionen | jede Funktion mit Test und Nachweis |
| 11 | Produktionsreife | Sicherheit, Datenschutz, Barrierefreiheit, Leistung, Wiederherstellung |
| 12 | Zahlungen und Veröffentlichungspaket | Kaufstrecke, Rechtstexte, Store-Angaben |
| 13 | Beta und Launch | echte Nutzer, Freigabe, Launch-Plan |
| 14 | Betrieb, Pflege und Ende | Überwachung, Updates, Notfallpläne |

Ausführliche Fassung: [Gesamtfahrplan der Master-Anleitung](./wissen/app-master-anleitung/01-gesamtfahrplan.md) und [App-Masterprozess](./wissen/allgemeine-app-entwicklung/11-masterprozess/APP-VON-0-BIS-RELEASE.md).

---

## 1. Idee prüfen

- **Ziel:** Nur bauen, was ein echtes Problem löst.
- **Tun:** Problem in einem Satz, Zielgruppe benennen, mit fünf bis zehn echten Menschen sprechen, Wettbewerber ansehen, eigenen Vorteil benennen, Stop-Kriterien festlegen.
- **Lesen:** [Idee, Markt, Geschäft](./wissen/app-master-anleitung/04-idee-markt-geschaeft/README.md), [Produkt](./wissen/allgemeine-app-entwicklung/01-produkt/README.md), Katalog [17 A](./wissen/ki-app-kriterienkatalog/17-produkt-launch-wachstum.md).
- **Vorlage:** [App-Risikoprofil](./wissen/allgemeine-app-entwicklung/vorlagen/app-risikoprofil.md).
- **Fertig, wenn:** Problemsatz, Notizen aus den Gesprächen und Stop-Kriterien schriftlich vorliegen.

## 2. Recht und Risiko einordnen

- **Ziel:** Vor dem ersten Code wissen, welche Gesetze und Sonderregeln gelten.
- **Tun:** Rolle nach AI Act bestimmen, jede KI-Funktion einordnen (verboten, hochriskant, Transparenzpflicht), Datenarten bestimmen, Sonderfälle wählen (Kinder, Gesundheit, Finanzen, Religion, Community, Agenten …), Erlaubnispflichten prüfen.
- **Lesen:** Katalog [01](./wissen/ki-app-kriterienkatalog/01-eu-ai-act.md), [02](./wissen/ki-app-kriterienkatalog/02-datenschutz-dsgvo.md), [03](./wissen/ki-app-kriterienkatalog/03-verbraucherrecht-und-weitere-gesetze.md), [04](./wissen/ki-app-kriterienkatalog/04-rechte-urheberrecht-lizenzen.md), [15](./wissen/ki-app-kriterienkatalog/15-sonderfaelle-nach-app-typ.md); [Recht, Regeln, Normen](./wissen/app-master-anleitung/02-recht-regeln-normen/README.md).
- **Vorlagen:** [Recht-Regeln-Normen-Matrix](./wissen/app-master-anleitung/vorlagen/RECHT-REGELN-NORMEN-MATRIX.md), [KI-Systemregister](./wissen/allgemeine-app-entwicklung/vorlagen/ki-systemregister.md).
- **Fertig, wenn:** Einordnung je KI-Funktion, Liste der zutreffenden Sonderfälle und offene Fragen für eine Fachperson dokumentiert sind.

## 3. Geschäftsmodell und Kosten

- **Ziel:** Die App trägt sich, auch bei Vielnutzern.
- **Tun:** Modell wählen (gratis, Abo, Credits, Einmalkauf), laufende Kosten auflisten (KI-API, Hosting, Datenbank, Stores, Tools), Kosten pro Nutzer durchrechnen, Gratis-Angebot begrenzen, Gewerbe und Steuern klären.
- **Lesen:** Katalog [14](./wissen/ki-app-kriterienkatalog/14-business-zahlungen-steuern.md), [07 D](./wissen/ki-app-kriterienkatalog/07-ki-api-modelle-kosten-qualitaet.md); [Monetarisierung](./wissen/app-master-anleitung/10-monetarisierung-zahlungen/README.md).
- **Fertig, wenn:** Preis, Kostenrechnung und Plan für Gewerbe und Umsatzsteuer vorliegen.

## 4. Produkt festlegen (PRD und MVP)

- **Ziel:** Klar beschreiben, was gebaut wird – und was nicht.
- **Tun:** PRD schreiben (Ziel, Nutzer, Funktionen, Nicht-Ziele, Erfolgskennzahl), kleinste sinnvolle Version festlegen, Pflichtfunktionen einplanen (Konto löschen, Rechtsseiten, KI-Hinweis, Support).
- **Lesen:** [Produkt, PRD und MVP](./wissen/app-master-anleitung/05-produkt-prd-mvp/README.md), Katalog [09](./wissen/ki-app-kriterienkatalog/09-pflichtfunktionen.md), [17 B](./wissen/ki-app-kriterienkatalog/17-produkt-launch-wachstum.md).
- **Vorlagen:** [PRD und MVP](./wissen/app-master-anleitung/vorlagen/PRD-UND-MVP.md), [PRD](./wissen/allgemeine-app-entwicklung/vorlagen/prd.md).
- **Fertig, wenn:** Das PRD ist freigegeben und jede MVP-Funktion hat ein Abnahmekriterium.

## 5. Abläufe, Funktionen und Daten

- **Ziel:** Jeder Weg durch die App und jedes Datum ist bekannt.
- **Tun:** Nutzerabläufe zeichnen (inklusive Fehler-, Leer-, Lade- und Offline-Zustände), Screen-Liste anlegen, Dateninventar erstellen (welche Daten, wozu, wie lange, wohin), Anbieter auflisten.
- **Lesen:** [Funktionen, System, Daten](./wissen/app-master-anleitung/03-funktionen-system-daten/README.md), [Datenlebenszyklus](./wissen/allgemeine-app-entwicklung/05-sicherheit-datenschutz-recht/datenlebenszyklus-export-und-loeschung.md), Katalog [02 A](./wissen/ki-app-kriterienkatalog/02-datenschutz-dsgvo.md).
- **Vorlagen:** [Screen-Inventar](./wissen/allgemeine-app-entwicklung/vorlagen/screen-inventar.md), [Daten- und Anbieterregister](./wissen/allgemeine-app-entwicklung/vorlagen/daten-und-anbieterregister.md), [Funktionsdossier](./wissen/app-master-anleitung/vorlagen/FUNKTIONSDOSSIER.md).
- **Fertig, wenn:** Abläufe, Screen-Liste und Dateninventar vollständig sind.

## 6. Design und Prototyp

- **Ziel:** Die App ist verständlich, barrierefrei und sieht eigenständig aus, bevor sie gebaut wird.
- **Tun:** Designsystem festlegen (Farben, Schriften, Abstände, Komponenten mit allen Zuständen), Klick-Prototyp bauen, mit fünf Menschen testen, KI-UX planen (Erwartungen, Streaming, Fehler, Kosten, Quellen).
- **Lesen:** [UX und UI](./wissen/app-master-anleitung/06-ux-ui-design/README.md), [Design-Handbuch](./wissen/allgemeine-app-entwicklung/02-design/README.md), [Design-Tokens](./wissen/allgemeine-app-entwicklung/02-design/design-tokens-und-komponenten.md), [Figma- und Mobbin-Workflow](./wissen/allgemeine-app-entwicklung/02-design/figma-und-mobbin-workflow.md), Katalog [10](./wissen/ki-app-kriterienkatalog/10-ki-ux.md), [11](./wissen/ki-app-kriterienkatalog/11-design-barrierefreiheit.md).
- **Testen:** Usability-Test, Kontrastprüfung, Prüfung der Klickflächen (siehe [`TESTEN.md`](./TESTEN.md)).
- **Fertig, wenn:** Prototyp getestet, Erkenntnisse eingearbeitet, Designsystem dokumentiert.

## 7. Plattform und Architektur

- **Ziel:** Ein Aufbau, der sicher, bezahlbar und wartbar ist.
- **Tun:** Plattform wählen (Web, PWA, iOS, Android, Desktop), bewährten Stack festlegen, Client und Server trennen, Datenmodell mit Zugriffsregeln entwerfen, Berechtigungsmatrix schreiben, Bedrohungen durchdenken, Entscheidungen festhalten.
- **Lesen:** [Technik-Grundlagen](./wissen/app-master-anleitung/07-technik-grundlagen/README.md), [Architektur-Leitfaden](./wissen/allgemeine-app-entwicklung/03-technik/architektur-entscheidungsleitfaden.md), [Supabase-Leitfaden](./wissen/allgemeine-app-entwicklung/03-technik/supabase-produktionsleitfaden.md), [Plattformen](./wissen/allgemeine-app-entwicklung/07-plattformen/README.md), [Plattform-Playbooks](./wissen/allgemeine-app-entwicklung/14-plattform-playbooks/README.md), Katalog [05](./wissen/ki-app-kriterienkatalog/05-sicherheit-grundlagen.md), [08](./wissen/ki-app-kriterienkatalog/08-architektur-aufbau-code.md).
- **Vorlagen:** [Architektur-Entscheidung](./wissen/allgemeine-app-entwicklung/vorlagen/architecture-decision-record.md), [Berechtigungsmatrix](./wissen/allgemeine-app-entwicklung/vorlagen/berechtigungsmatrix.md), [Threat Model](./wissen/allgemeine-app-entwicklung/vorlagen/threat-model.md).
- **Fertig, wenn:** Architektur, Datenmodell, Berechtigungsmatrix und Threat Model schriftlich vorliegen.

## 8. Arbeitsumgebung und KI-Agent

- **Ziel:** Sicher und nachvollziehbar mit KI entwickeln.
- **Tun:** Git-Repository, getrennte Umgebungen (Entwicklung, Vorschau, Produktion), Secrets im Secret-Manager, `.env` in `.gitignore`, Regeldatei für den Agenten (`AGENTS.md`/`CLAUDE.md`), automatische Prüfungen bei jedem Push (Lint, Typen, Tests, Secret-Scan), Agent ohne Zugriff auf Produktion.
- **Lesen:** [Entwicklung mit KI](./wissen/app-master-anleitung/04-entwicklung-mit-ki/README.md), [Claude-Code- und Codex-Playbook](./wissen/allgemeine-app-entwicklung/04-ki-agenten/claude-code-und-codex-playbook.md), [Masterprompt](./wissen/allgemeine-app-entwicklung/12-agenten-masterprompt/CLAUDE-CODE-APP-MASTERPROMPT.md), [Automatisierung](./wissen/allgemeine-app-entwicklung/13-automatisierung/README.md), Katalog [16](./wissen/ki-app-kriterienkatalog/16-vibe-coding-arbeitsweise.md).
- **Fertig, wenn:** Ein leerer Push läuft grün durch alle automatischen Prüfungen.

## 9. Ersten Kernablauf bauen

- **Ziel:** Ein wichtiger Ablauf funktioniert vollständig – von der Anmeldung bis zum gespeicherten Ergebnis – und ist sicher.
- **Tun:** Anmeldung, Datenzugriff mit Zugriffsregeln, ein KI-Aufruf über den Server mit Limits, Fehler- und Ladezustände, Tests.
- **Lesen:** [Umsetzung Kernfunktionen](./wissen/app-master-anleitung/08-umsetzung-kernfunktionen/README.md), [Supabase-RLS-Testmatrix](./wissen/allgemeine-app-entwicklung/03-technik/supabase-rls-testmatrix.md), [KI-Produktionsleitfaden](./wissen/allgemeine-app-entwicklung/04-ki-agenten/ki-produktionsleitfaden.md), Katalog [05](./wissen/ki-app-kriterienkatalog/05-sicherheit-grundlagen.md), [06](./wissen/ki-app-kriterienkatalog/06-ki-sicherheit-llm-risiken.md), [07](./wissen/ki-app-kriterienkatalog/07-ki-api-modelle-kosten-qualitaet.md).
- **Testen:** Zwei-Konten-Test, Unit- und End-to-End-Test des Ablaufs, Prompt-Injection-Test, Limit-Test.
- **Beispiel:** [Supabase-Beispiel mit Zwei-Nutzer-Test](./beispiel-apps/focusflow-supabase/README.md).
- **Fertig, wenn:** Der Ablauf läuft auf einem echten Gerät, alle Tests sind grün und der Zwei-Konten-Test ist bestanden.

## 10. Weitere Funktionen

- **Ziel:** Die App wächst, ohne unsicher oder chaotisch zu werden.
- **Tun:** Je Funktion: kurz planen, klein bauen, Test schreiben, prüfen, committen. Nach jeder riskanten Änderung (Anmeldung, Datenbank, Zahlung, KI-Werkzeuge) eine getrennte Sicherheitsprüfung.
- **Lesen:** Katalog [09](./wissen/ki-app-kriterienkatalog/09-pflichtfunktionen.md), [10](./wissen/ki-app-kriterienkatalog/10-ki-ux.md), [16 C](./wissen/ki-app-kriterienkatalog/16-vibe-coding-arbeitsweise.md), [Prüf-Prompts](./wissen/ki-app-kriterienkatalog/PRUEF-PROMPTS.md).
- **Fertig, wenn:** Jede MVP-Funktion ihr Abnahmekriterium mit Nachweis erfüllt.

## 11. Produktionsreife

- **Ziel:** Die App ist bereit für echte Nutzer und echte Daten.
- **Tun:** Sicherheit, Datenschutz, Barrierefreiheit, Leistung, Fehlerüberwachung, Backups mit getesteter Wiederherstellung, Rückroll-Plan, Kostenalarme. Prüfer `ki-app-check` laufen lassen und alle roten `PFLICHT`-Punkte beheben.
- **Lesen:** [Qualität, Security, Datenschutz](./wissen/app-master-anleitung/09-qualitaet-security-datenschutz/README.md), [Teststrategie und Release-Gates](./wissen/allgemeine-app-entwicklung/06-tests-release-betrieb/teststrategie-und-release-gates.md), Katalog [12](./wissen/ki-app-kriterienkatalog/12-tests-release-betrieb.md), [`TESTEN.md`](./TESTEN.md), [Prüfer](./pruefer/README.md).
- **Vorlagen:** [Evidenz-Matrix](./wissen/allgemeine-app-entwicklung/vorlagen/evidenz-matrix.md), [Plattform-Testmatrix](./wissen/allgemeine-app-entwicklung/vorlagen/plattform-testmatrix.md).
- **Fertig, wenn:** Der Prüfbericht zeigt bei keinem `PFLICHT`-Punkt Rot und der Mindestumfang aus `TESTEN.md` ist nachgewiesen.

## 12. Zahlungen und Veröffentlichungspaket

- **Ziel:** Rechtssicher Geld verdienen und alles für die Stores bereit haben.
- **Tun:** Kaufstrecke nach Verbraucherrecht (Bestellbutton, Widerruf, Kündigungs- und Widerrufsbutton), Store-Käufe nach Apple- und Google-Regeln, Rechnungen, Rechtstexte (Impressum, Datenschutz, AGB, Barrierefreiheitsinformationen), Store-Angaben (Datenschutz, Altersfreigabe, Screenshots, Demo-Zugang).
- **Lesen:** [Zahlungen und Abos](./wissen/allgemeine-app-entwicklung/08-zahlungen-und-abos/README.md), [Veröffentlichung](./wissen/app-master-anleitung/05-veroeffentlichung/README.md), Katalog [03 C](./wissen/ki-app-kriterienkatalog/03-verbraucherrecht-und-weitere-gesetze.md), [13](./wissen/ki-app-kriterienkatalog/13-app-stores-plattformen.md), [14](./wissen/ki-app-kriterienkatalog/14-business-zahlungen-steuern.md).
- **Testen:** Zahlungen im Testmodus komplett, Kündigen und Widerrufen, Käufe wiederherstellen.
- **Vorlage:** [Test- und Release-Dossier](./wissen/app-master-anleitung/vorlagen/TEST-UND-RELEASE-DOSSIER.md).
- **Fertig, wenn:** Testkauf, Kündigung und Widerruf funktionieren und alle Store-Angaben mit dem echten Datenfluss übereinstimmen.

## 13. Beta und Launch

- **Ziel:** Mit echten Nutzern starten, ohne böse Überraschungen.
- **Tun:** Beta (TestFlight, geschlossener Test bei Google Play), Feedback einarbeiten, Release-Freigabe, gestaffelt veröffentlichen, Launch-Plan umsetzen, Werberecht beachten, am Release-Tag erreichbar sein.
- **Lesen:** [Marketing und Launch](./wissen/app-master-anleitung/06-marketing-launch/README.md), Katalog [17 C–E](./wissen/ki-app-kriterienkatalog/17-produkt-launch-wachstum.md), [Checkliste vor jedem Release](./wissen/allgemeine-app-entwicklung/CHECKLISTE-VOR-JEDEM-RELEASE.md).
- **Vorlagen:** [Release-Freigabe](./wissen/allgemeine-app-entwicklung/vorlagen/release-freigabe.md), [Marketing- und Launchplan](./wissen/app-master-anleitung/vorlagen/MARKETING-UND-LAUNCHPLAN.md).
- **Fertig, wenn:** Die Release-Freigabe ist unterschrieben (Go/No-Go) und die App ist live.

## 14. Betrieb, Pflege und Ende

- **Ziel:** Die App bleibt über Jahre sicher, rechtlich aktuell und bezahlbar.
- **Tun:** Fehler, Verfügbarkeit, KI-Kosten und Qualität überwachen; Sicherheitsupdates sofort, Abhängigkeiten monatlich; Abkündigungen von KI-Modellen und Store-Vorgaben verfolgen; Notfallpläne üben; den Katalog alle drei Monate mit `katalog-pruefen` aktualisieren. Für das Ende: Nutzer rechtzeitig informieren, Export ermöglichen, Abos geordnet beenden, Daten löschen.
- **Lesen:** [Betrieb und Skalierung](./wissen/app-master-anleitung/07-betrieb-skalierung/README.md), [Langfristige Pflege](./wissen/app-master-anleitung/13-langfristige-pflege/README.md), [Performance, Analytics, Betrieb](./wissen/allgemeine-app-entwicklung/09-performance-analytics-betrieb/README.md), [Runbooks](./wissen/allgemeine-app-entwicklung/15-runbooks/README.md), Katalog [12 C–G](./wissen/ki-app-kriterienkatalog/12-tests-release-betrieb.md).
- **Vorlagen:** [Betriebshandbuch](./wissen/app-master-anleitung/vorlagen/BETRIEBSHANDBUCH.md), [Incident-Report](./wissen/allgemeine-app-entwicklung/vorlagen/incident-report.md).
- **Fertig:** nie – Betrieb ist ein Kreislauf. Monatlich Kapitel 12 durchgehen, vor jedem Release `ki-app-check`.
