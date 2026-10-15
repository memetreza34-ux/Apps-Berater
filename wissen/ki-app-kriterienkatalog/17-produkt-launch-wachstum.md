# 17 – Produkt, Launch und Wachstum

Die sicherste App bringt nichts, wenn niemand sie braucht oder findet. Mit KI lassen sich Apps schnell bauen – deshalb gibt es viele ähnliche. Dieses Kapitel prüft, ob die Idee trägt, ob die App gefunden wird und ob Nutzer bleiben. Vertiefung: [Idee, Markt und Geschäft](../app-master-anleitung/04-idee-markt-geschaeft/README.md) und [Marketing und Launch](../app-master-anleitung/06-marketing-launch/README.md).

## A. Idee prüfen, bevor du baust

- [ ] `SOLLTE` **Problem in einem Satz:** Wer hat welches Problem, wie oft, und wie löst er es heute?
- [ ] `SOLLTE` **Mit fünf bis zehn echten Menschen aus der Zielgruppe sprechen,** bevor du viel Zeit investierst. Nach ihrem Verhalten fragen, nicht nach ihrer Meinung zur Idee.
- [ ] `SOLLTE` **Wettbewerber und Alternativen ansehen** – auch „einfach ChatGPT benutzen“ ist eine Alternative. Was kann deine App, was ein allgemeiner Chatbot nicht kann?
- [ ] `SOLLTE` **Eigenen Vorteil benennen:** eigene Daten, bessere Bedienung, Spezialwissen, Integration, Community, Vertrauen.
- [ ] `SOLLTE` **Abhängigkeit prüfen:** Kann der KI-Anbieter deine Kernfunktion morgen selbst kostenlos anbieten?
- [ ] `SOLLTE` **Stop-Kriterien vorher festlegen** (z. B. „Wenn nach 8 Wochen weniger als 20 aktive Nutzer, ändere ich die Richtung“).

## B. Produkt und MVP

- [ ] `SOLLTE` **Kleinste sinnvolle Version (MVP)** mit einer Kernfunktion, die richtig gut funktioniert.
- [ ] `SOLLTE` **Nicht-Ziele aufschreiben,** damit der Umfang nicht ausufert.
- [ ] `SOLLTE` **Erfolgskennzahl festlegen** (z. B. Anteil der Nutzer, die in der ersten Woche die Kernfunktion dreimal nutzen).
- [ ] `SOLLTE` **Geschäftsmodell wählen:** kostenlos mit Limit, Abo, Credits, Einmalkauf, B2B-Lizenz. KI-Kosten pro Nutzer mitdenken (siehe [07](./07-ki-api-modelle-kosten-qualitaet.md)).

## C. Vor dem Launch

- [ ] `SOLLTE` **Landingpage** mit klarem Nutzenversprechen, Screenshots oder Demo-Video, Preisen, FAQ, Rechtsseiten.
- [ ] `SOLLTE` **Warteliste** mit Double-Opt-in, um schon vor dem Launch Interessenten zu sammeln.
- [ ] `SOLLTE` **Beta-Nutzer** früh einbinden und Feedback sammeln.
- [ ] `SOLLTE` **Analyse-Plan (Tracking-Plan):** Welche Ereignisse misst du (Registrierung, erste Nutzung der Kernfunktion, Kauf, Kündigung)? Datenschutzkonform (siehe [02](./02-datenschutz-dsgvo.md)).
- [ ] `SOLLTE` **Support vorbereiten:** FAQ, Antwortvorlagen, Kontaktweg.
- [ ] `SOLLTE` **Launch-Kalender:** Wann, wo, mit welchem Material.

## D. Gefunden werden

- [ ] `SOLLTE` **App Store Optimization.** Apple durchsucht App-Name (30 Zeichen), Untertitel (30) und Keyword-Feld (100 Bytes – Umlaute zählen doppelt; keine Namen anderer Apps oder Firmen), Google Play Titel (30), Kurzbeschreibung (80) und Beschreibung. Store-Eintrag auf Deutsch anbieten; im Titel keine Wörter wie „Nr. 1“ oder „Beste“, keine Preis- oder Rabatthinweise und keine Emojis (Google-Richtlinie); für wichtige Suchbegriffe eigene Produktseiten anlegen.
- [ ] `KANN` **Vorbestellung und Vorregistrierung.** Neue Apps können im App Store bis zu 180 Tage vorher vorbestellt und bei Google Play bis zu 90 Tage vorregistriert werden; Interessenten werden zum Start automatisch benachrichtigt.
- [ ] `SOLLTE` **Web-SEO:** Seiten zu den Problemen deiner Zielgruppe, saubere Technik (siehe [13](./13-app-stores-plattformen.md)).
- [ ] `SOLLTE` **In KI-Antworten auftauchen.** Klare, faktenreiche Seiten mit eigenem Wissen schreiben (Produktbeschreibung, Vergleich, FAQ, strukturierte Daten); laut Google braucht es dafür keine `llms.txt` und keine Spezial-Auszeichnung. KI-Such-Crawler (z. B. `OAI-SearchBot`, `Claude-SearchBot`) weder in der `robots.txt` noch im Bot-Schutz des CDN sperren (Cloudflare blockt KI-Crawler seit Juli 2025 standardmäßig). Trainings-Crawler (z. B. `GPTBot`, `ClaudeBot`, `Google-Extended`) lassen sich getrennt ausschließen; `Google-Extended` wirkt aber nicht auf Googles KI-Übersichten (dafür `nosnippet`). Strukturierte Daten müssen zum sichtbaren Text passen.
- [ ] `SOLLTE` **Keine KI-Massenseiten für SEO.** Viele KI-generierte oder automatisch übersetzte Seiten ohne eigenen Mehrwert wertet Google als Spam („scaled content abuse“) und kann die ganze Website abwerten.
- [ ] `KANN` **KI-Nutzungssignale beobachten.** Die IETF entwickelt Angaben für `robots.txt`, ob Inhalte für KI-Training oder KI-Suche genutzt werden dürfen (noch Entwurf, Stand September 2026).
- [ ] `SOLLTE` **Neue App-Store-Werbeflächen nutzen.** Seit Oktober 2026 zeigt der App Store eigene Bilder und Videos im Kopf der Produktseite und in Suchergebnissen; vor dem Einreichen mit der Vorschau in App Store Connect prüfen.
- [ ] `SOLLTE` **Kanäle wählen, wo die Zielgruppe ist** (Communities, Foren, Social Media, Newsletter, Verzeichnisse, Launch-Plattformen).
- [ ] `SOLLTE` **Inhalte, die echten Nutzen zeigen** (Demo-Videos, Vorher-nachher, Anleitungen) statt reiner Werbung.
- [ ] `KANN` **Partnerschaften, Creator und Presse.**
- [ ] `SOLLTE` **Regeln der Launch-Plattformen einhalten.** Product Hunt: nicht direkt um Upvotes bitten, keine Firmenkonten; „Show HN“ bei Hacker News: nur ausprobierbare, nicht schnell zusammengeklickte Projekte und keine reine Landingpage.
- [ ] `KANN` **Bezahlte Werbung** erst mit kleinem Testbudget und klarer Messung.

## E. Werberecht beim Marketing

- [ ] `PFLICHT` **Werbung und Kooperationen kennzeichnen.** Gut sichtbar und gleich am Anfang mit „Werbung“ oder „Anzeige“, auch bei Creatorn, Affiliate-Links, Mitarbeitern und Bekannten. Schon ein kostenloser Premium-Zugang oder geschenkte Credits zählen als Gegenleistung.
- [ ] `PFLICHT` **Keine irreführenden Aussagen** über KI-Fähigkeiten, Ergebnisse oder Nutzerzahlen.
- [ ] `PFLICHT` **Kein „AI Washing“.** Mit „KI-basiert“ oder „mit KI“ nur werben, wenn wirklich ein KI-System die beworbene Leistung erbringt; sonst ist das irreführende Werbung (§ 5 UWG; so auch der Leitfaden der Wettbewerbszentrale vom Juli 2026).
- [ ] `PFLICHT` **Aussagen deines KI-Chatbots gelten als deine Werbung.** Falsche Angaben eines Website- oder Support-Chatbots zu Preisen, Leistungen oder Qualifikationen werden dir zugerechnet (OLG Hamm, 12. Mai 2026). Den Chatbot auf geprüfte Inhalte beschränken, regelmäßig testen und bei Unsicherheit an einen Menschen verweisen.
- [ ] `PFLICHT` **Gesetzliche Pflichten nicht als Besonderheit bewerben.** „DSGVO-konform“, „AI-Act-konform“ oder „14 Tage Widerrufsrecht“ nicht als besonderen Vorteil herausstellen, weil das jeder Anbieter erfüllen muss. „Deine Daten bleiben in Deutschland“ nur sagen, wenn das auch für den KI-Anbieter stimmt.
- [ ] `PFLICHT` **Keine pauschalen Umweltversprechen.** Seit 27. September 2026 sind Aussagen wie „grüne KI“, „klimaneutral“ oder „umweltfreundlich“ ohne anerkannten Nachweis verboten; „klimaneutral“ allein durch CO2-Ausgleichszahlungen ist immer verboten.
- [ ] `PFLICHT` **Keine KI-erfundenen Kundenstimmen.** Testimonials, Bewertungen, „Nutzerfotos“ oder Avatare, die wie echte Kunden wirken, nicht mit KI erzeugen. Das gilt als gefälschte Empfehlung und ist immer verboten.
- [ ] `SOLLTE` **KI-Kennzeichnung der Werbeplattformen nutzen.** Meta und TikTok verlangen oder setzen Hinweise für Anzeigen mit realistischen KI-Bildern, -Stimmen oder -Personen; ohne Kennzeichnung droht die Ablehnung. Die Regeln vor jeder Kampagne prüfen.
- [ ] `PFLICHT` **Keine gekauften oder gefälschten Bewertungen, Likes oder Upvotes,** keine Belohnung nur für positive Bewertungen (UWG-Anhang Nr. 23c, gilt auch für Empfehlungen in sozialen Medien).
- [ ] `SOLLTE` **Sterne-Durchschnitt nur mit Anzahl und Zeitraum.** Wer mit „4,8 Sterne“ wirbt, nennt Zahl der Bewertungen, Zeitraum und Quelle und sagt, ob und wie die Echtheit geprüft wird (§ 5a, § 5b Abs. 3 UWG; LG Deggendorf, März 2026).
- [ ] `PFLICHT` **Keine anonymen Nutzerzitate im Play-Store-Text.** Google Play verbietet nicht zugeordnete oder anonyme Kundenstimmen in der App-Beschreibung.
- [ ] `PFLICHT` **E-Mail-Marketing nur mit Einwilligung** (Double-Opt-in) und Abmeldelink.
- [ ] `PFLICHT` **KI-Werbung als Deepfake kennzeichnen, wenn sie echt wirkt.** Das gilt für realistische Personen, synthetische Influencer und Avatare, laut Leitlinien zu Art. 50 aber auch für KI-Produktbilder, die das Produkt anders oder besser zeigen als in echt. Bei Videos den Hinweis wiederholen, wenn Zuschauer später einsteigen können (siehe [01](./01-eu-ai-act.md)).
- [ ] `PFLICHT` **Gewinnspiele** mit Teilnahmebedingungen (siehe [03](./03-verbraucherrecht-und-weitere-gesetze.md)).
- [ ] `PFLICHT` **Vergleichende Werbung** nur sachlich und belegbar.

## F. Nutzer halten

- [ ] `SOLLTE` **Aktivierung messen:** Wie viele Neue erreichen den ersten Erfolg?
- [ ] `SOLLTE` **Wiederkehr messen** (nach 1, 7 und 30 Tagen) und verbessern.
- [ ] `SOLLTE` **Lifecycle-E-Mails** mit echtem Mehrwert (Willkommen, Tipps, Erinnerung an unvollendete Aufgaben) – mit Rechtsgrundlage und Abmeldemöglichkeit.
- [ ] `SOLLTE` **Kündigungsgründe erfragen** – freiwillig und erst nach abgeschlossener Kündigung (z. B. in der Bestätigungs-E-Mail), nie auf der Bestätigungsseite des Kündigungsbuttons (siehe [03](./03-verbraucherrecht-und-weitere-gesetze.md)).
- [ ] `SOLLTE` **Regelmäßig mit Nutzern sprechen** und Feedback in die Roadmap übernehmen.
- [ ] `KANN` **Empfehlungsprogramm** (Einladen gegen Credits) mit klaren und fairen Regeln. Die App verschickt selbst keine Einladungs-E-Mails an Dritte; Nutzer teilen stattdessen einen Link (solche Mails sind laut BGH unerlaubte Werbung).
- [ ] `KANN` **Werbe-E-Mails an Bestandskunden** ohne Einwilligung nur für eigene ähnliche Angebote, wenn die Adresse beim Kauf oder bei der Registrierung erhoben wurde, kein Widerspruch vorliegt und bei der Erhebung sowie in jeder Mail auf das Widerspruchsrecht hingewiesen wird (§ 7 Abs. 3 UWG). Auch ein kostenloses Konto kann dafür als „Verkauf“ zählen (EuGH, 13. November 2025, C-654/23).

## G. Zahlen, die du kennen solltest

- [ ] `SOLLTE` **Kosten pro gewonnenem Nutzer** (CAC) und Zeit, bis er sie wieder einbringt (Payback).
- [ ] `SOLLTE` **Umsatz pro Nutzer** und **KI-Kosten pro Nutzer** im Verhältnis.
- [ ] `SOLLTE` **Umwandlungsrate** von Gratis zu zahlend.
- [ ] `SOLLTE` **Kündigungsrate** (Churn) pro Monat.
- [ ] `SOLLTE` **Ein Dashboard** mit diesen Zahlen, wöchentlich angesehen.

## H. Langfristig

- [ ] `SOLLTE` **Roadmap** mit wenigen, klar priorisierten Themen.
- [ ] `SOLLTE` **Technische Schulden und Sicherheit** fest einplanen, nicht nur neue Funktionen.
- [ ] `KANN` **Finanzierung, Verkauf oder Lizenzierung** vorbereiten: saubere Rechte, Zahlen, Dokumentation (siehe [14](./14-business-zahlungen-steuern.md)).

## Typische Fehler beim Vibe-Coding

- Wochen gebaut, nie mit einem echten Nutzer gesprochen.
- „Wrapper“ um ein Sprachmodell ohne eigenen Vorteil.
- Launch ohne Landingpage, ohne Tracking, ohne Support-Weg.
- Werbung mit „100 % genau“ oder erfundenen Nutzerzahlen.
- Keine Ahnung, was ein Nutzer kostet und einbringt.

## Nachweis

Problemstatement mit Interview-Notizen, MVP-Umfang und Nicht-Ziele, Tracking-Plan, Launch-Kalender, Kennzahlen-Dashboard.
