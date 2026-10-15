# 04 – Rechte, Urheberrecht und Lizenzen

KI-Apps berühren fremde Rechte an vielen Stellen: Trainingsdaten, generierte Inhalte, Nutzer-Uploads, Stimmen, Gesichter, Code, Schriften, Modelle und Namen. Wer hier schlampt, riskiert Abmahnungen, Store-Sperren und Schadensersatz.

## A. Rechte an KI-Ergebnissen

- [ ] `SOLLTE` **Wissen: Rein KI-generierte Inhalte sind meist nicht urheberrechtlich geschützt.** Schutz entsteht nur durch eine persönliche geistige Schöpfung eines Menschen. Andere dürfen rein generierte Texte oder Bilder dann oft kopieren.
- [ ] `SOLLTE` **Menschlichen Anteil dokumentieren,** wenn dir Schutz wichtig ist (Auswahl, Bearbeitung, Komposition, eigene Texte).
- [ ] `PFLICHT` **Nutzungsbedingungen des KI-Anbieters prüfen:** Wem gehört der Output? Ist kommerzielle Nutzung erlaubt? Welche Inhalte und Einsatzzwecke sind verboten?
- [ ] `PFLICHT` **Output auf Verletzung fremder Rechte prüfen.** KI kann bekannte Figuren, Logos, Marken, Songtexte oder Bildstile sehr nah nachbilden. Die Haftung trägt, wer den Inhalt veröffentlicht.
- [ ] `SOLLTE` **Keine geschützten Werke wörtlich aus der KI ausgeben.** Das Landgericht München I hat entschieden (GEMA gegen OpenAI, 11. November 2025; GEMA gegen Suno, 31. Juli 2026; beide nicht rechtskräftig), dass der Betreiber haftet, wenn ein Modell Songtexte oder Musik auswendig gelernt hat und wiedergibt – auch bei einfachen Nutzer-Prompts. Anfragen nach ganzen Songtexten, Buchpassagen oder Paywall-Artikeln abfangen und höchstens zusammenfassen; die Urteile sind noch nicht rechtskräftig.
- [ ] `SOLLTE` **Keine Prompts wie „im Stil von [lebender Künstler]“ oder „wie das Nike-Logo“** für kommerzielle Logos, Figuren oder Werbung.
- [ ] `SOLLTE` **Logos und App-Icons aus KI** vor Nutzung per Bild- und Markenrecherche auf Ähnlichkeiten prüfen.
- [ ] `SOLLTE` **Nutzer über Rechte am Output informieren** (in AGB: wem gehört was, keine Garantie für Schutzfähigkeit).

## B. Trainingsdaten, Scraping und RAG-Quellen

- [ ] `PFLICHT` **Nutzungsvorbehalte beim Crawlen achten** (§ 44b UrhG). Rechteinhaber können Text- und Data-Mining verbieten. Ob ein Verbot nur im Fließtext der Nutzungsbedingungen zählt, ist nach dem OLG Hamburg (Dezember 2025) fraglich und liegt beim BGH – deshalb `robots.txt`, maschinenlesbare Hinweise und auch Textvorbehalte beachten.
- [ ] `PFLICHT` **Nutzungsbedingungen von Websites und APIs beachten,** bevor du Inhalte automatisiert abrufst.
- [ ] `PFLICHT` **Personenbezogene Daten beim Scraping** nur mit Rechtsgrundlage (DSGVO gilt auch für öffentlich sichtbare Daten).
- [ ] `PFLICHT` **Inhalte für RAG (Wissensdatenbank) nur mit Nutzungsrecht.** Ganze Bücher, Kurse oder Paywall-Artikel in eine öffentliche App zu laden, ist meist eine Urheberrechtsverletzung.
- [ ] `PFLICHT` **Datenbankherstellerrecht beachten** (§§ 87a ff. UrhG). Wesentliche Teile fremder Datenbanken (z. B. Job-, Immobilien-, Preis- oder Produktportale) dürfen nicht einfach übernommen werden – auch nicht durch wiederholtes Abrufen kleiner Teile.
- [ ] `SOLLTE` **EDPB-Leitlinien zu Scraping und Anonymisierung nutzen.** Der Europäische Datenschutzausschuss hat im Juli 2026 Leitlinien zum Scraping für generative KI (03/2026) und einen Entwurf zur Anonymisierung veröffentlicht. Wer selbst Daten sammelt oder Modelle mit Nutzerdaten trainiert, prüft danach Rechtsgrundlage, Informationspflichten, Qualität der Quellen und ob Daten wirklich anonym sind.
- [ ] `SOLLTE` **Herkunft und Lizenz jedes Datensatzes dokumentieren** (Quelle, Datum, Lizenz, Einschränkungen).
- [ ] `KANN` **Eigene Inhalte maschinenlesbar schützen.** Ein Verbot nur im Impressum oder in den AGB reicht womöglich nicht. Wer KI-Trainings-Crawler aussperren will, setzt Regeln in `robots.txt` oder andere maschinenlesbare Signale und schreibt den Vorbehalt zusätzlich in die Nutzungsbedingungen. Such-Crawler von KI-Diensten nicht versehentlich mitsperren (siehe [17](./17-produkt-launch-wachstum.md)).

## C. Inhalte der Nutzer

- [ ] `PFLICHT` **Rechteeinräumung in den AGB:** Nutzer erlauben dir, ihre Uploads zu speichern, zu verarbeiten und anzuzeigen – nur soweit für die App nötig.
- [ ] `PFLICHT` **Nutzer versichern, die Rechte an Uploads zu haben,** und stellen dich bei Verstößen frei (soweit wirksam).
- [ ] `PFLICHT` **Nutzerinhalte nicht ohne Einwilligung zum Training** eigener Modelle oder für Werbung verwenden.
- [ ] `PFLICHT` **Verfahren für Rechteverletzungen** (Meldung durch Rechteinhaber, Prüfung, Entfernung), siehe DSA in [03](./03-verbraucherrecht-und-weitere-gesetze.md).

## D. Personen, Gesichter und Stimmen

- [ ] `PFLICHT` **Bilder von Personen nur mit Einwilligung** veröffentlichen (Recht am eigenen Bild, § 22 KUG), außer gesetzliche Ausnahmen.
- [ ] `PFLICHT` **Stimmen klonen nur mit ausdrücklicher, nachweisbarer Einwilligung** der Person. Missbrauch technisch erschweren, z. B. durch Sprachprobe mit zufälligem Satz, damit nur die eigene Stimme geklont wird.
- [ ] `PFLICHT` **Keine Deepfakes realer Personen,** die diese verächtlich machen, täuschen oder sexualisieren. Das verletzt Persönlichkeitsrechte und kann strafbar sein.
- [ ] `PFLICHT` **Keine heimlichen Aufnahmen anderer.** Das nichtöffentlich gesprochene Wort ohne Zustimmung aufzunehmen, ist strafbar (§ 201 StGB). Wichtig für Sprach-, Meeting- und Coaching-Apps.
- [ ] `SOLLTE` **Prominente und reale Personen** in Bild- und Stimmgeneratoren standardmäßig blockieren.

## E. Code, Open Source und Modelle

- [ ] `PFLICHT` **Lizenzen aller Abhängigkeiten kennen.** MIT, BSD und Apache sind meist unkritisch. GPL verpflichtet bei Weitergabe zur Offenlegung. **AGPL** kann schon bei Bereitstellung über das Netz (SaaS) zur Offenlegung deines Codes verpflichten.
- [ ] `PFLICHT` **Lizenzhinweise mitliefern,** wenn die Lizenz es verlangt (z. B. Seite „Open-Source-Lizenzen“ in der App).
- [ ] `SOLLTE` **Lizenz-Scan automatisieren** (z. B. `license-checker`, GitHub Dependency Review).
- [ ] `PFLICHT` **Lizenzen von Open-Weight-Modellen prüfen.** Manche Modelle haben eigene Bedingungen mit Einschränkungen für kommerzielle Nutzung, Nutzerzahlen oder Namensnennung.
- [ ] `SOLLTE` **Längere KI-generierte Code-Blöcke** auf wörtliche Übernahme fremden Codes prüfen, wenn sie verdächtig vollständig wirken.
- [ ] `PFLICHT` **Verträge mit Freelancern und Agenturen:** Nutzungsrechte am Code und Design schriftlich auf dich übertragen.

## F. Schriften, Bilder, Icons, Musik

- [ ] `PFLICHT` **Schriftlizenzen prüfen.** Eine Desktop-Lizenz erlaubt oft keine Einbettung in Apps oder Websites. Google Fonts und andere Open-Font-Lizenzen sind unkritisch.
- [ ] `PFLICHT` **Stockfotos, Icons und Illustrationen** nur mit passender Lizenz (kommerziell, App, Werbung). Lizenznachweis speichern.
- [ ] `PFLICHT` **Musik und Sounds** nur lizenziert. Auch KI-Musik hat Anbieter-Bedingungen. Bei GEMA-Repertoire gesonderte Lizenz. Ausgaben von KI-Musikgeneratoren vor der Veröffentlichung auf Nähe zu bekannten Songs prüfen – das LG München I sieht schon im Training mit auswendig gelernten Songs eine Vervielfältigung.
- [ ] `SOLLTE` **Lizenzregister führen:** Asset, Quelle, Lizenz, Datum, Nachweis.

## G. Name, Marke, Design und Domain

- [ ] `PFLICHT` **Markenrecherche vor dem Launch** (DPMA, EUIPO, WIPO) für App-Namen und Logo. Auch ähnliche Namen in derselben Branche prüfen.
- [ ] `PFLICHT` **Keine fremden Marken im App-Namen.** Namen mit „GPT“, „Claude“, „Gemini“ oder ähnlichen Marken vermeiden. Die Markenrichtlinien der Anbieter prüfen.
- [ ] `SOLLTE` **Domain, App-Store-Name und Social-Media-Handles** gleichzeitig sichern.
- [ ] `KANN` **Eigene Marke anmelden,** sobald die App ernsthaft vermarktet wird.
- [ ] `SOLLTE` **Nachahmer und Fake-Apps melden.** Taucht eine Kopie deiner App oder eine App mit deinem Namen auf, über die Rechte-Beschwerde von Apple (App Store Content Dispute) und Google (Formular für Verstöße gegen geistiges Eigentum) melden. Eine eingetragene Marke macht das deutlich leichter.
- [ ] `KANN` **Patentrisiko kennen.** In der EU sind reine Software-Ideen kaum patentierbar, technische Lösungen aber schon; in den USA sind Patentklagen gegen Apps häufiger. Bei einer Patent-Abmahnung nie selbst reagieren, sondern Fachanwalt für Patentrecht einschalten; vor einem US-Start bei Kernfunktionen kurz recherchieren lassen.

- [ ] `PFLICHT` **Keine fremden App-Designs kopieren.** Oberflächen, Icons und Screens bekannter Apps nicht 1:1 nachbauen (Designrecht, Nachahmungsschutz im UWG, Store-Regeln gegen Nachahmer-Apps). Referenzen als Inspiration nutzen, nicht als Vorlage.

## H. Vertrauliche Informationen

- [ ] `PFLICHT` **Keine Geschäftsgeheimnisse oder Kundendaten Dritter** in KI-Tools ohne passenden Vertrag eingeben (auch nicht beim Entwickeln).
- [ ] `KANN` **Eigene Geschäftsgeheimnisse schützen** (z. B. Systemprompts, Bewertungslogik, Trainingsdaten). Schutz nach dem Geschäftsgeheimnisgesetz setzt angemessene Geheimhaltungsmaßnahmen voraus: Zugriffsbeschränkung, Vertraulichkeitsvereinbarungen.

## Typische Fehler beim Vibe-Coding

- App-Icon mit KI erzeugt, das einem bekannten Logo ähnelt.
- Premium-Schrift aus einem Figma-Template übernommen, ohne Web-Lizenz.
- Wissensdatenbank mit gekauften E-Books befüllt und öffentlich angeboten.
- AGPL-Paket im Backend einer kommerziellen SaaS.
- Name „Irgendwas-GPT“ gewählt.

## Nachweis

Lizenzregister, Markenrecherche mit Datum, Einwilligungen für Stimmen und Bilder, AGB-Klauseln zu Nutzerinhalten, Lizenz-Scan-Report.
