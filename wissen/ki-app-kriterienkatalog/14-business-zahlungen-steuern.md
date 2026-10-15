# 14 – Business, Zahlungen und Steuern

Sobald eine App Geld einnimmt oder regelmäßig angeboten wird, bist du Unternehmer – mit Pflichten gegenüber Finanzamt, Kunden und Anbietern. Dieses Kapitel ersetzt keine Steuerberatung. Es zeigt, woran du denken musst.

## A. Gründung und Anmeldung

- [ ] `PFLICHT` **Tätigkeit anmelden.** Gewerbe beim Gewerbeamt anmelden oder – falls freiberuflich – direkt beim Finanzamt melden. Die Abgrenzung mit einem Steuerberater klären.
- [ ] `PFLICHT` **Innerhalb eines Monats anmelden.** Die Gewerbe- oder Tätigkeitsanzeige und der Fragebogen zur steuerlichen Erfassung (über ELSTER) sind innerhalb eines Monats nach Start fällig (§ 138 AO).
- [ ] `SOLLTE` **Rechtsform bewusst wählen.** Als Einzelunternehmer haftest du mit deinem Privatvermögen. Bei höheren Risiken (sensible Daten, Geschäftskunden, Haftungsfragen) eine UG oder GmbH erwägen.
- [ ] `PFLICHT` **Bei UG oder GmbH: Transparenzregister.** Die Gesellschaft muss ihre wirtschaftlich Berechtigten (z. B. Gesellschafter mit mehr als 25 %) selbst im Transparenzregister eintragen (§ 20 GwG). Sonst drohen Bußgelder.
- [ ] `PFLICHT` **Wenn du unter 18 bist: Geschäftsfähigkeit klären.** Ein eigenes Geschäft darfst du nur mit Zustimmung der Eltern und Genehmigung des Familiengerichts selbstständig betreiben (§ 112 BGB). Apple verlangt für das kostenpflichtige Developer Program die Volljährigkeit; Zahlungsanbieter und andere Stores prüfen ebenfalls das Alter. Bis dahin über die Eltern oder eine Firma planen.
- [ ] `SOLLTE` **Neben Job, Studium oder Sozialleistungen gründen: Folgen klären.** Arbeitsvertrag auf Nebentätigkeits- und Wettbewerbsklauseln prüfen und den Arbeitgeber wenn nötig informieren. Gewinne können die kostenlose Familienversicherung, BAföG oder Bürgergeld beeinflussen – vorher bei Krankenkasse oder Amt nachfragen.
- [ ] `SOLLTE` **Getrenntes Geschäftskonto.**
- [ ] `SOLLTE` **Rücklagen für Steuern bilden** (Einkommen- bzw. Körperschaftsteuer, Gewerbesteuer, Vorauszahlungen).
- [ ] `KANN` **Förderungen prüfen** (z. B. Gründungszuschuss, EXIST, Landesprogramme).

## B. Umsatzsteuer

- [ ] `SOLLTE` **Kleinunternehmerregelung prüfen** (§ 19 UStG): Umsatz im Vorjahr höchstens 25.000 €, im laufenden Jahr höchstens 100.000 €; im Gründungsjahr gilt nur die Grenze von 25.000 €. Wer eine Grenze überschreitet, muss schon für den Umsatz, mit dem sie überschritten wird, Umsatzsteuer abführen. Dann keine Umsatzsteuer auf Rechnungen – aber auch kein Vorsteuerabzug.
- [ ] `KANN` **EU-Kleinunternehmerregelung nutzen.** Seit 2025 kannst du die Steuerbefreiung über das Bundeszentralamt für Steuern auch in anderen EU-Ländern nutzen, wenn dein EU-weiter Umsatz höchstens 100.000 € beträgt. Dafür brauchst du eine eigene Kennnummer und musst jedes Quartal melden.
- [ ] `PFLICHT` **Digitale Leistungen an Verbraucher in anderen EU-Ländern:** Ab 10.000 € Auslandsumsatz pro Jahr gilt die Umsatzsteuer des Kundenlandes. Abwicklung über das One-Stop-Shop-Verfahren (OSS).
- [ ] `SOLLTE` **Merchant of Record erwägen** (z. B. Paddle oder die App Stores). Sie verkaufen im eigenen Namen und führen die Umsatzsteuer gegenüber den Endkunden ab – gegen höhere Gebühren. Deine Einnahmen von ihnen sind trotzdem eine eigene steuerliche Leistung (siehe nächste Punkte).
- [ ] `PFLICHT` **Reverse Charge bei Auslandsrechnungen.** Kaufst du KI-API, Hosting, Werkzeuge oder Werbung bei Firmen im Ausland ein (z. B. Irland, USA), schuldest du selbst die deutsche Umsatzsteuer (§ 13b UStG) – auch als Kleinunternehmer und ohne Vorsteuerabzug. Eine USt-IdNr. beantragen und die Steuer melden.
- [ ] `PFLICHT` **Store-Einnahmen umsatzsteuerlich richtig behandeln.** Über App Store und Google Play verkaufst du rechtlich an Apple bzw. Google (meist deren Gesellschaften in Irland). Dafür brauchst du in der Regel eine USt-IdNr. und eine Gutschrift oder Rechnung; ohne Kleinunternehmerregelung kommt eine Zusammenfassende Meldung dazu. Details mit Steuerberatung klären.
- [ ] `PFLICHT` **Monatliche Voranmeldung für Gründer ab 2027.** Wer ab 2027 gründet und keine Kleinunternehmerregelung nutzt, muss im Gründungs- und im Folgejahr jeden Monat eine Umsatzsteuer-Voranmeldung abgeben. Stand Oktober 2026 ist keine Verlängerung der Aussetzung geplant; vor Jahresende prüfen, ob das Jahressteuergesetz 2026 noch etwas ändert.
- [ ] `SOLLTE` **Steuerberechnung automatisieren,** wenn du selbst verkaufst (z. B. Stripe Tax).

## C. Rechnungen und Buchhaltung

- [ ] `PFLICHT` **Rechnungen mit allen Pflichtangaben** (Name und Anschrift beider Seiten, Steuernummer oder USt-ID, Datum, fortlaufende Nummer, Leistung, Entgelt, Steuersatz oder Hinweis auf Kleinunternehmerregelung).
- [ ] `PFLICHT` **E-Rechnungen empfangen und ausstellen.** Empfangen müssen alle Unternehmen schon seit 1. Januar 2025 können. Rechnungen an Firmen müssen ab 1. Januar 2027 elektronisch sein (strukturiertes Format wie XRechnung oder ZUGFeRD), wenn der Vorjahresumsatz über 800.000 € lag, ab 1. Januar 2028 für alle. Kleinunternehmer sind beim Ausstellen ausgenommen, Rechnungen an Privatkunden nicht betroffen. Rechnungen bis 250 € brutto (Kleinbetragsrechnungen) dürfen weiter als PDF oder auf Papier gehen (§ 33 UStDV).
- [ ] `PFLICHT` **Ordnungsgemäße Buchführung** (GoBD) und Aufbewahrungsfristen: Bücher 10 Jahre, Rechnungen und Buchungsbelege 8 Jahre, sonstige geschäftliche Unterlagen 6 Jahre (§ 147 AO). Diese Daten dürfen trotz Löschanfrage nicht vorher gelöscht werden.
- [ ] `PFLICHT` **Meldepflicht für Marktplatz-Apps (DAC7).** Verkaufen Nutzer über deine App Waren, bieten Dienstleistungen an oder vermieten etwas, musst du ihre Daten erheben und jährlich bis 31. Januar an das Bundeszentralamt für Steuern melden. Ausgenommen sind Verkäufer mit weniger als 30 Warenverkäufen und höchstens 2.000 € im Jahr.
- [ ] `SOLLTE` **Buchhaltungs-Tool** mit Bankanbindung und Belegerfassung.
- [ ] `SOLLTE` **Einnahmen aus Stores, Stripe und Co.** monatlich abgleichen (Auszahlungen, Gebühren, Erstattungen, Rückbuchungen).
- [ ] `SOLLTE` **US-Steuerformular bei Stores und Zahlungsanbietern ausfüllen.** Apple, Google und US-Zahlungsanbieter fragen nach einem Steuerformular (meist W-8BEN für Personen, W-8BEN-E für Firmen). Ohne es kann auf Einnahmen aus den USA bis zu 30 % US-Quellensteuer einbehalten werden; mit dem Formular greift das Doppelbesteuerungsabkommen.
- [ ] `PFLICHT` **Künstlersozialabgabe prüfen.** Beauftragst du für deine App nicht nur gelegentlich selbstständige Designer, Illustratorinnen, Texter, Fotografen oder Sprecher und zahlst ihnen mehr als 1.000 € im Jahr (Grenze 2026), musst du dich meist bei der Künstlersozialkasse melden und eine Abgabe zahlen (2026: 4,9 %, 2027: 5,0 % der Honorare; Meldung bis 31. März für das Vorjahr). Das gilt auch für Aufträge an Freelancer im Ausland.

## D. Zahlungsanbieter

- [ ] `SOLLTE` **Store-Gebühren aktuell vergleichen.** Google Play verlangt in der EU seit 30. Juni 2026 bei neuen Installationen 20 % für Einmalkäufe und 10 % für Abos, auf die ersten 1 Mio. US-Dollar Jahreserlös 10 % – jeweils plus Gebühr, wenn Google Play Billing genutzt wird. Apple verlangt außerhalb der EU 30 % bzw. 15 % (Small Business Program, Abos ab dem zweiten Jahr), in der EU ab 1. Oktober 2026 26 % bzw. 15 %. Dazu kommen Stripe- oder Paddle-Gebühren beim Web-Verkauf.
- [ ] `PFLICHT` **Betrugsschutz aktivieren** (z. B. Stripe Radar, 3-D Secure).
- [ ] `SOLLTE` **Zahlungskonto früh einrichten.** Zahlungsanbieter verlangen vor der ersten Auszahlung Identitäts- und Geschäftsangaben (Know Your Customer). Das kann Tage dauern.
- [ ] `SOLLTE` **Test- und Live-Modus trennen:** Testschlüssel nur in Entwicklung und Vorschau, Live-Schlüssel nur in der Produktion.
- [ ] `SOLLTE` **Umgang mit Rückbuchungen und Erstattungen** festlegen.
- [ ] `PFLICHT` **Store-Regeln für digitale Güter** beachten (siehe [13](./13-app-stores-plattformen.md)).
- [ ] `SOLLTE` **Ein zentrales Abo-Modell im Backend,** auch wenn Käufe aus mehreren Quellen kommen (Web, iOS, Android), z. B. mit RevenueCat oder eigener Logik.

## E. Kosten und Preise

- [ ] `SOLLTE` **Kosten der Entwicklerkonten einplanen:** Apple verlangt eine jährliche Gebühr (Apple Developer Program), Google eine einmalige Registrierungsgebühr. Aktuelle Preise vor dem Start prüfen.
- [ ] `PFLICHT` **Laufende Kosten kennen:** KI-API, Hosting, Datenbank, Speicher, E-Mail, Domains, Store-Gebühren, Tools, Versicherung, Steuerberater.
- [ ] `SOLLTE` **Preis so kalkulieren,** dass auch Vielnutzer profitabel sind (siehe [07](./07-ki-api-modelle-kosten-qualitaet.md)).
- [ ] `SOLLTE` **Gratis-Angebot begrenzen,** damit es dich nicht ruiniert.
- [ ] `SOLLTE` **Stop-Kriterien festlegen:** Ab welchem Verlust oder welcher Nutzerzahl änderst du Preise oder stellst ein?

## F. Versicherung und Haftung

- [ ] `SOLLTE` **Berufs- oder Vermögensschadenhaftpflicht für IT** prüfen.
- [ ] `SOLLTE` **Cyber-Versicherung** prüfen (Datenleck, Erpressung, Betriebsunterbrechung).
- [ ] `SOLLTE` **Ausdrücklich klären, ob Schäden durch KI-Fehler** mitversichert sind.

## G. Verträge

- [ ] `PFLICHT` **Bedingungen aller Anbieter einhalten** (KI-Anbieter, Hosting, Stores, Plattform-APIs).
- [ ] `PFLICHT` **Geschäftskunden:** Du bist oft deren Auftragsverarbeiter. Einen eigenen AVV und eine Beschreibung deiner Sicherheitsmaßnahmen bereithalten.
- [ ] `SOLLTE` **Verträge mit Freelancern und Mitgründern** schriftlich: Nutzungsrechte, Anteile, Vertraulichkeit, Ausstieg.
- [ ] `PFLICHT` **Scheinselbstständigkeit vermeiden.** Arbeitet ein Freelancer dauerhaft nur für dich, nach deinen Weisungen und eingebunden wie ein Angestellter, kann er rechtlich Arbeitnehmer sein; dann drohen Nachzahlungen der Sozialversicherungsbeiträge für mehrere Jahre (§ 7 SGB IV). Im Zweifel ein Statusfeststellungsverfahren bei der Deutschen Rentenversicherung beantragen (§ 7a SGB IV).
- [ ] `PFLICHT` **Wenn du Mitarbeiter einstellst: Arbeitgeberpflichten erfüllen.** Anmeldung bei der Krankenkasse bzw. Minijob-Zentrale, Betriebsnummer, Unfallversicherung bei der Berufsgenossenschaft, Mindestlohn (MiLoG), schriftlicher Nachweis der wesentlichen Arbeitsbedingungen (Nachweisgesetz) und Arbeitszeiterfassung. Auch für Werkstudenten und Minijobber; am besten mit Lohnbüro oder Steuerberatung.
- [ ] `SOLLTE` **Service-Zusagen (SLA)** nur machen, wenn du sie einhalten kannst.
- [ ] `PFLICHT` **Sanktionen beachten.** Keine Leistungen an Personen, Firmen oder Länder, die EU-Sanktionen unterliegen. Zahlungsanbieter prüfen mit, die Verantwortung bleibt bei dir.
- [ ] `KANN` **Saubere Rechtekette für Investoren oder Verkauf:** Code, Marke, Domains und Inhalte gehören nachweisbar der Firma.
- [ ] `SOLLTE` **Beim Verkauf der App Nutzerdaten nur rechtmäßig übergeben.** Werden App und Kundendaten an jemand anderen verkauft, dürfen die Daten nicht einfach mitgehen. Laut Datenschutzkonferenz (Beschluss vom 11. September 2024) braucht es je nach Fall Zustimmung der Kunden, eine Widerspruchsmöglichkeit oder bei Gesundheits- und anderen sensiblen Daten eine Einwilligung. Rechtzeitig mit Fachleuten planen.

## H. Team und Zugänge

- [ ] `SOLLTE` **Eigene Konten für jede Person** bei allen Diensten, keine geteilten Passwörter.
- [ ] `SOLLTE` **Rechte nach Rolle vergeben** (nicht jeder braucht Admin-Zugang zu Produktion und Zahlungen).
- [ ] `PFLICHT` **Zugänge sofort entziehen,** wenn jemand das Projekt verlässt, und betroffene Keys austauschen.
- [ ] `SOLLTE` **Übergabe dokumentieren,** damit das Projekt nicht an einer Person hängt.

## I. Abhängigkeit von Anbietern

- [ ] `SOLLTE` **Wechselmöglichkeit planen:** Datenexport aus Datenbank und Auth, austauschbare KI-Anbieter, keine Logik, die nur in einem proprietären Tool existiert.
- [ ] `PFLICHT` **Entwickler-Konten mit Passkey oder Sicherheitsschlüssel schützen.** GitHub, npm, Hosting, Datenbank, KI-Anbieter, Domain-Registrar, App Stores und Zahlungsanbieter mit phishing-resistenter Mehr-Faktor-Anmeldung absichern: Passkey oder Hardware-Schlüssel statt SMS-Code. Große Paket-Angriffe 2025 und 2026 begannen mit gefälschten Login- oder „2FA-Reset“-Mails.
- [ ] `SOLLTE` **Zugänge im Passwortmanager** speichern und einen Notfallzugang für eine Vertrauensperson einrichten.
- [ ] `SOLLTE` **Projekt-E-Mail** statt privater Adresse für alle Anbieterkonten.

## Typische Fehler beim Vibe-Coding

- Einnahmen über Stripe, aber kein Gewerbe angemeldet.
- Kunden in Österreich und Frankreich, OSS ignoriert.
- Rechnungen ohne fortlaufende Nummer aus einem selbstgebauten Generator.
- Alle Anbieterkonten auf die private Gmail-Adresse ohne Mehr-Faktor-Anmeldung.
- Preis „Flatrate unbegrenzt“ bei teurem Modell.

## Nachweis

Gewerbeanmeldung oder Finanzamt-Bestätigung, Umsatzsteuer-Entscheidung, Kostenrechnung, Versicherungsübersicht, Anbieterliste mit Konten und Verträgen.
