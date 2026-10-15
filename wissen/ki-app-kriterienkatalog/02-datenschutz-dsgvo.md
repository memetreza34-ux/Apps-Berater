# 02 – Datenschutz (DSGVO und TDDDG)

Sobald deine App Namen, E-Mail-Adressen, IP-Adressen, Chatverläufe, Fotos, Stimmen oder Nutzungsdaten verarbeitet, gilt die DSGVO. Bei KI-Apps kommt hinzu: Eingaben gehen an einen KI-Anbieter, oft in die USA. Das TDDDG regelt in Deutschland zusätzlich Cookies und den Zugriff auf Endgeräte.

## A. Grundlagen

- [ ] `PFLICHT` **Dateninventar erstellen.** Welche personenbezogenen Daten, wofür, wo gespeichert, an wen übermittelt, wie lange. Vorlage: [Daten- und Anbieterregister](../allgemeine-app-entwicklung/vorlagen/daten-und-anbieterregister.md).
- [ ] `PFLICHT` **Rechtsgrundlage je Zweck festlegen** (Art. 6): Vertrag, Einwilligung, berechtigtes Interesse oder rechtliche Pflicht. Ohne Rechtsgrundlage keine Verarbeitung. Die Rechtsgrundlage je Zweck konkret benennen – die italienische Aufsicht verhängte 2025 gegen die KI-Begleiter-App Replika 5 Mio. €, u. a. weil die Rechtsgrundlagen nur vage genannt waren und die Altersgrenze nicht technisch durchgesetzt wurde.
- [ ] `PFLICHT` **Datenminimierung.** Nur Daten erheben, die für die Funktion nötig sind. Kein Geburtsdatum „für später“.
- [ ] `PFLICHT` **Zweckbindung.** Daten für die App-Funktion nicht einfach für andere Zwecke nutzen, z. B. zum Trainieren eigener Modelle.
- [ ] `PFLICHT` **Speicherdauer festlegen** und technisch umsetzen (automatisches Löschen alter Chats, Logs, Uploads).
- [ ] `PFLICHT` **Verzeichnis von Verarbeitungstätigkeiten** führen (Art. 30). Die Ausnahme für kleine Firmen greift bei regelmäßiger Verarbeitung praktisch nie.
- [ ] `PFLICHT` **Datenschutzerklärung** vollständig und verständlich: Verantwortlicher, Zwecke, Rechtsgrundlagen, Empfänger mit Namen (auch KI-Anbieter), Drittlandübermittlung, Speicherdauer, Rechte, Beschwerderecht, Kontakt. In App und Website leicht erreichbar.
- [ ] `PFLICHT` **Datenschutzfehler sind abmahnbar.** Seit einem Urteil des Bundesgerichtshofs (27. März 2025) dürfen Konkurrenten und Verbraucherverbände Mängel in Datenschutzerklärung (Art. 12, 13 DSGVO), Einwilligung (Art. 7) und bei sensiblen Daten (Art. 9) abmahnen. Datenschutzerklärung und Einwilligungen deshalb genauso sorgfältig prüfen wie das Impressum.
- [ ] `SOLLTE` **Schadensersatz bei Datenschutzverstößen kennen.** Schon ein kurzer Kontrollverlust über Daten gilt als Schaden (BGH, November 2024). Gerichte sprachen bei Tracking ohne Einwilligung teils hohe Beträge pro Person zu, und viele Betroffene können gemeinsam klagen.
- [ ] `SOLLTE` **Datenschutzhinweise verständlich schichten.** 2026 prüfen 25 europäische Aufsichtsbehörden gezielt, ob Datenschutzhinweise klar, vollständig und rechtzeitig sind. Kurzinfo im Moment der Datenerhebung und ausführliche Erklärung per Link verbinden.
- [ ] `PFLICHT` **Auftragsverarbeitungsvertrag (AVV) mit jedem Dienstleister** (Art. 28): Hosting, Datenbank, KI-API, E-Mail-Versand, Analytics, Fehler-Tracking, Support-Tool. Bei großen Anbietern meist online abschließbar (Data Processing Addendum).
- [ ] `PFLICHT` **Drittlandübermittlung absichern.** Bei US-Anbietern prüfen: Zertifizierung nach dem EU-US Data Privacy Framework oder Standardvertragsklauseln. Dokumentieren.
- [ ] `SOLLTE` **Rückfallebene für US-Anbieter bereithalten.** Das EU-US Data Privacy Framework wurde 2025 vom EU-Gericht bestätigt, ist aber vor dem EuGH angefochten (C-703/25 P). Seit Juni 2026 wächst das Risiko durch Entwicklungen in den USA (FTC-Mitglieder frei entlassbar, Streit um Section 702 FISA). Mit KI- und Hosting-Anbietern zusätzlich Standardvertragsklauseln vereinbaren und den Wechselweg dokumentieren. Prüfen, ob der KI- oder Hosting-Anbieter auch Standardvertragsklauseln anbietet, damit ein Wechsel schnell möglich ist.
- [ ] `SOLLTE` **EU-Regionen wählen,** wo möglich: Datenbank und Hosting in der EU, KI-Modelle über EU-Rechenzentren oder EU-Datenresidenz des Anbieters.
- [ ] `PFLICHT` **Datenschutz-Folgenabschätzung (DSFA) prüfen** (Art. 35). Oft nötig bei neuer Technik mit sensiblen Daten, umfangreichem Profiling, Überwachung oder Kindern. KI mit personenbezogenen Daten ist ein typischer Auslöser. Die Muss-Liste der Datenschutzkonferenz prüfen.
- [ ] `PFLICHT` **Datenschutzbeauftragten prüfen.** In Deutschland Pflicht ab 20 Personen, die ständig mit automatisierter Datenverarbeitung arbeiten – und unabhängig davon, wenn eine DSFA-pflichtige Verarbeitung stattfindet.
- [ ] `PFLICHT` **Besondere Kategorien schützen** (Art. 9): Gesundheit, Religion, Sexualleben, politische Meinung, biometrische Daten zur Identifizierung. Meist nur mit ausdrücklicher Einwilligung. Achtung: Nutzer schreiben solche Daten oft ungefragt in einen Chat.
- [ ] `PFLICHT` **Datenschutz durch Technikgestaltung und datenschutzfreundliche Voreinstellungen** (Art. 25): Standardmäßig so wenig Daten wie möglich, Profile nicht öffentlich, optionale Funktionen ausgeschaltet.
- [ ] `PFLICHT` **Einwilligungen nachweisen können** (Art. 7): Zeitpunkt, Wortlaut bzw. Version des Textes und Art der Zustimmung speichern.
- [ ] `PFLICHT` **Daten Dritter beachten.** Nutzer laden oft Inhalte über andere Menschen hoch (E-Mails, Kontakte, Fotos, Gesprächsnotizen). Rechtsgrundlage und Informationspflichten (Art. 14) für diese Personen prüfen und in den Nutzungsregeln festlegen, was erlaubt ist.
- [ ] `SOLLTE` **Gemeinsame Verantwortlichkeit prüfen** (Art. 26), z. B. bei eingebundenen Social-Media-Plugins oder Fanpages.
- [ ] `PFLICHT` **Keine rein automatisierten Entscheidungen mit rechtlicher oder ähnlich erheblicher Wirkung** (Art. 22) ohne Ausnahme und ohne Recht auf menschliche Prüfung. Auch ein Score, der die Entscheidung maßgeblich bestimmt, kann darunter fallen.
- [ ] `PFLICHT` **Automatische Entscheidungen erklären können.** Wer per KI oder Score über Personen entscheidet, muss auf Anfrage im Einzelfall verständlich erklären, wie das Ergebnis zustande kam (EuGH, 27. Februar 2025). „Geschäftsgeheimnis“ ist kein Grund, die Auskunft ganz zu verweigern.
- [ ] `PFLICHT` **Regeln für Scoring ab 20. November 2026 beachten.** Wer Wahrscheinlichkeitswerte (Scores) nutzt, um über Abschluss, Durchführung oder Ende eines Vertrags zu entscheiden, muss die neuen Regeln des § 37a BDSG einhalten: u. a. keine Scores über Minderjährige, bestimmte Daten wie die Anschrift nicht verwenden, Betroffene informieren und eine Entscheidung durch einen Menschen ermöglichen.

## B. KI-spezifischer Datenschutz

- [ ] `PFLICHT` **Nutzer informieren, dass Eingaben an einen KI-Anbieter gehen.** In der Datenschutzerklärung und kurz im UI, z. B. beim ersten Upload.
- [ ] `PFLICHT` **Training durch den Anbieter prüfen.** Bei den meisten Business-APIs werden Daten standardmäßig nicht zum Training genutzt – Vertrag und Einstellungen trotzdem kontrollieren. Consumer-Versionen (z. B. Chat-Apps) haben andere Regeln.
- [ ] `SOLLTE` **Herkunft des KI-Modells prüfen.** Der Europäische Datenschutzausschuss erwartet, dass du vor dem Einsatz eines fremden Modells prüfst, ob es rechtmäßig mit personenbezogenen Daten trainiert wurde (Stellungnahme 28/2024). Angaben des Anbieters zu Datenquellen und bekannte Behörden- oder Gerichtsentscheidungen kurz dokumentieren.
- [ ] `SOLLTE` **Aufbewahrung beim KI-Anbieter minimieren.** Zero-Data-Retention oder kurze Speicherfristen nutzen, wenn verfügbar und nötig.
- [ ] `SOLLTE` **Personenbezug vor dem Senden entfernen.** Namen, E-Mails, Telefonnummern pseudonymisieren, wenn die KI sie nicht braucht.
- [ ] `PFLICHT` **Nur Daten des aktuellen Nutzers in den Kontext.** Keine fremden Chats, Dokumente oder Profile im Prompt (siehe [06](./06-ki-sicherheit-llm-risiken.md)).
- [ ] `PFLICHT` **Chat-Inhalte nicht ohne ausdrückliche Einwilligung für Werbung nutzen.** Eingaben in einen KI-Chat können Gesundheit, Religion oder Sexualität verraten (Art. 9 DSGVO). Ein Hinweis mit „Okay“-Button oder vorangekreuzte Werbeoptionen reichen nicht (LG Köln, 17. September 2026, 33 O 120/24, nicht rechtskräftig).
- [ ] `SOLLTE` **Chatverläufe: Speicherdauer festlegen** und Löschen durch Nutzer ermöglichen.
- [ ] `SOLLTE` **KI-Gedächtnis (Memory) steuerbar machen:** anzeigen, bearbeiten, löschen, ausschalten.
- [ ] `PFLICHT` **Eigene Nutzung von Nutzerdaten zum Training nur transparent** und mit passender Rechtsgrundlage, meist Einwilligung (Opt-in) oder mindestens klarer Widerspruchsmöglichkeit.
- [ ] `PFLICHT` **Falsche KI-Aussagen über Personen berichtigen können.** KI-Ausgaben über reale Menschen nicht ungeprüft als Fakten speichern.
- [ ] `SOLLTE` **Observability-Tools datenschutzkonform nutzen.** Tracing-Dienste (z. B. Langfuse, Helicone) sehen komplette Prompts. PII maskieren, kurze Aufbewahrung, AVV abschließen.
- [ ] `SOLLTE` **Aktuelle Hilfen der Aufsichtsbehörden nutzen.** Die Datenschutzkonferenz hat 2025 Orientierungshilfen zu technischen und organisatorischen Maßnahmen bei KI-Systemen und zu RAG (KI mit eigener Wissensdatenbank) veröffentlicht, aus dem Expertenpool des Europäischen Datenschutzausschusses kam ein Bericht zu Risiken von Sprachmodellen. Im Juli 2026 hat der Ausschuss Leitlinien zum Scraping für generative KI (03/2026) und einen Entwurf zur Anonymisierung veröffentlicht. Diese als Prüfliste verwenden.
- [ ] `SOLLTE` **Nicht auf den Digital Omnibus vorgreifen.** Die geplanten Erleichterungen bei DSGVO und Cookies (z. B. berechtigtes Interesse für KI-Training, Browser-Signale für Einwilligungen) sind noch nicht beschlossen. Bis 12. Oktober 2026 gab es weder ein Mandat des Rates noch eine Position des Parlaments; ein Abschluss ist nicht vor 2027 zu erwarten. Bis zum Inkrafttreten gelten DSGVO und TDDDG unverändert.
- [ ] `SOLLTE` **Uploads nach Verarbeitung löschen,** wenn sie nicht dauerhaft gebraucht werden.
- [ ] `SOLLTE` **Kein Fine-Tuning mit personenbezogenen Nutzerdaten ohne Konzept.** Daten lassen sich aus einem trainierten Modell praktisch nicht mehr gezielt löschen.
- [ ] `SOLLTE` **Embeddings wie Originaldaten behandeln.** Vektoren können Rückschlüsse auf den Ursprungstext erlauben – gleiche Zugriffs-, Speicher- und Löschregeln.

## C. Rechte der Nutzer

- [ ] `PFLICHT` **Auskunft** (Art. 15) innerhalb eines Monats, inklusive Kopie der Daten.
- [ ] `PFLICHT` **Löschung** (Art. 17) überall: Datenbank, Datei-Speicher, Vektor-Datenbank, Logs, Analytics, Dienstleister. Konzept für Backups (werden nach Ablauf überschrieben). Vertiefung: [Datenlebenszyklus, Export und Löschung](../allgemeine-app-entwicklung/05-sicherheit-datenschutz-recht/datenlebenszyklus-export-und-loeschung.md).
- [ ] `PFLICHT` **Datenübertragbarkeit** (Art. 20): Export in einem gängigen, maschinenlesbaren Format (z. B. JSON, CSV).
- [ ] `PFLICHT` **Berichtigung, Einschränkung und Widerspruch** ermöglichen.
- [ ] `PFLICHT` **Auf das Widerspruchsrecht gesondert hinweisen.** Stützt du Verarbeitungen auf berechtigtes Interesse (z. B. Analyse, KI-Verbesserung) oder nutzt du Daten für Direktwerbung, weist du spätestens bei der ersten Kommunikation ausdrücklich und getrennt von anderen Texten auf das Widerspruchsrecht hin (Art. 21 Abs. 4 DSGVO).
- [ ] `SOLLTE` **Auskunftsanfragen nicht vorschnell als Missbrauch ablehnen.** Nach dem EuGH (19. März 2026, C-526/24) kann zwar schon eine erste Anfrage missbräuchlich sein, du musst die Missbrauchsabsicht aber beweisen. Eine zu Unrecht verweigerte Auskunft kann Schadensersatz nach Art. 82 DSGVO auslösen.
- [ ] `PFLICHT` **Einwilligungen widerrufbar,** genauso einfach wie erteilt.
- [ ] `SOLLTE` **Self-Service in den Einstellungen** für Export und Löschung. Spart Support und erfüllt Store-Regeln.
- [ ] `SOLLTE` **Anfragen protokollieren** (Eingang, Frist, Erledigung).

## D. Cookies, Tracking und Endgeräte (TDDDG)

- [ ] `PFLICHT` **Einwilligung vor nicht notwendigen Cookies, Local Storage und SDKs.** Gilt für Websites und Apps (§ 25 TDDDG). Analytics, Marketing-Pixel und Werbe-IDs brauchen in der Regel eine Einwilligung.
- [ ] `PFLICHT` **Consent-Banner fair gestalten.** „Ablehnen“ gleich gut erreichbar wie „Akzeptieren“, keine vorausgewählten Häkchen, App auch ohne Zustimmung nutzbar.
- [ ] `PFLICHT` **Nichts vor der Einwilligung laden.** Kein Google Tag, kein Meta Pixel, keine Tracking-SDKs beim ersten Start.
- [ ] `PFLICHT` **Eingebettete Inhalte erst nach Klick oder Einwilligung laden.** YouTube-Videos, Karten, Social-Media-Beiträge, Chat-Widgets und manche Captchas (z. B. Google reCAPTCHA) senden schon beim Laden IP-Adresse und Gerätedaten an den Anbieter. Deshalb einen Platzhalter zeigen und erst nach Klick laden (Zwei-Klick-Lösung) oder datensparsame Alternativen nutzen.
- [ ] `PFLICHT` **Einstellungen jederzeit änderbar** (Link „Cookie-Einstellungen“ im Footer oder in den App-Einstellungen).
- [ ] `PFLICHT` **Newsletter-Tracking nur mit Einwilligung.** Unsichtbare Zählpixel und Klick-Tracking-Links in E-Mails gelten nach Auffassung der Aufsichtsbehörden als Zugriff auf das Endgerät (§ 25 TDDDG). Öffnungs- und Klickraten nur messen, wenn Empfänger das erlaubt haben, sonst im Versand-Tool abschalten.
- [ ] `PFLICHT` **Werbung in der App nur mit zertifizierter Einwilligungslösung.** Wer AdMob, AdSense oder Ad Manager nutzt, braucht für Nutzer in EWR, Großbritannien und der Schweiz eine von Google zertifizierte Consent-Plattform nach dem IAB-TCF-Standard (z. B. Googles UMP-SDK), sonst werden nur eingeschränkte Anzeigen ausgeliefert.
- [ ] `KANN` **Anerkannten Einwilligungsdienst einbinden.** Seit April 2025 können Dienste anerkannt werden, die Cookie-Entscheidungen der Nutzer zentral speichern (§ 26 TDDDG). Die Einbindung ist freiwillig; wer einbindet, muss die gespeicherten Entscheidungen beachten.
- [ ] `PFLICHT` **Schriften und Ressourcen lokal einbinden.** Google Fonts direkt von Google-Servern zu laden, überträgt IP-Adressen und wurde abgemahnt.
- [ ] `SOLLTE` **DSK-Orientierungshilfe „Digitale Dienste“ als Cookie-Prüfliste nutzen.** Die Datenschutzkonferenz erklärt darin (Stand November 2024), wann Zugriffe auf das Endgerät ohne Einwilligung erlaubt sind und wie Einwilligungen aussehen müssen. Danach prüfen die deutschen Aufsichtsbehörden.
- [ ] `SOLLTE` **Analyse ohne Cookie-Banner nur eng.** Datensparsame Tools (z. B. Plausible, Umami, PostHog mit EU-Hosting) helfen, ersetzen aber nicht automatisch die Einwilligung. Ohne Einwilligung kommt laut deutscher Aufsicht höchstens eine reine Zählung infrage, z. B. aus Server-Logs ohne Personenbezug; „cookielose“ Tools, Zählpixel, Fingerprinting oder lokale Speicherung brauchen meist eine Einwilligung (§ 25 TDDDG, EDSA-Leitlinien 2/2023).
- [ ] `PFLICHT` **Session-Replay und Heatmaps** (z. B. Hotjar, Microsoft Clarity, LogRocket) nur mit Einwilligung und mit Maskierung aller Eingabefelder.
- [ ] `SOLLTE` **Kamera, Mikrofon, Standort, Kontakte** nur anfragen, wenn die Funktion sie braucht, und im Moment der Nutzung begründen.

## E. Sicherheit und Datenpannen

- [ ] `PFLICHT` **Technische und organisatorische Maßnahmen (TOMs)** umsetzen und beschreiben (Art. 32): Verschlüsselung, Zugriffskontrolle, Backups, Protokolle.
- [ ] `PFLICHT` **Datenpannen innerhalb von 72 Stunden** an die Aufsichtsbehörde melden, bei hohem Risiko auch Betroffene informieren. Ablauf vorher festlegen: [Runbook Security- und Datenschutzvorfall](../allgemeine-app-entwicklung/15-runbooks/security-und-datenschutzvorfall.md).
- [ ] `PFLICHT` **Jede Datenpanne dokumentieren.** Auch Vorfälle, die du nicht melden musst, mit Fakten, Folgen und Maßnahmen festhalten (Art. 33 Abs. 5 DSGVO). Die Aufsicht kann diese Liste verlangen.
- [ ] `PFLICHT` **Technischen Schutz nach § 19 TDDDG umsetzen.** Wer geschäftsmäßig digitale Dienste anbietet, schützt seine Systeme nach dem Stand der Technik gegen unerlaubten Zugriff, z. B. mit anerkannter Verschlüsselung (§ 19 Abs. 4 TDDDG). Wo zumutbar, ermöglichst du auch anonyme oder pseudonyme Nutzung und informierst darüber (§ 19 Abs. 2).
- [ ] `SOLLTE` **Zugriff auf Produktionsdaten minimal halten** und protokollieren. Auch du selbst schaust nicht ohne Anlass in Nutzerchats.

## F. Kinder

- [ ] `PFLICHT` **Einwilligung der Eltern unter 16 Jahren** (Art. 8 DSGVO, Altersgrenze in Deutschland), wenn die Verarbeitung auf Einwilligung beruht. Mehr in [15 – Sonderfälle](./15-sonderfaelle-nach-app-typ.md).

## Typische Fehler beim Vibe-Coding

- Datenschutzerklärung aus einem Generator, in der der KI-Anbieter fehlt.
- Analytics-Skript im `<head>` des Templates, das vor dem Banner lädt.
- „Konto löschen“ setzt nur `deleted = true`, Uploads und Embeddings bleiben liegen.
- Komplette Prompts mit Nutzerdaten werden dauerhaft in Logs gespeichert.
- Testdaten sind echte Kundendaten.

## Nachweis

Daten- und Anbieterregister, Verzeichnis von Verarbeitungstätigkeiten, abgeschlossene AVVs, Datenschutzerklärung mit Datum, getesteter Export- und Löschweg, Consent-Test (Netzwerk-Tab ohne Tracking vor Zustimmung).
