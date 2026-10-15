# 12 – Tests, Release und Betrieb

Eine App ist mit dem Launch nicht fertig. Ab dann zählt: Merkst du Fehler vor den Nutzern? Kannst du eine kaputte Version zurückrollen? Sind die Daten nach einem Unfall wiederherstellbar? Weißt du, was bei einem Datenleck zu tun ist?

Kurze Freigabeliste: [Checkliste vor jedem Release](../allgemeine-app-entwicklung/CHECKLISTE-VOR-JEDEM-RELEASE.md). Vertiefung: [Teststrategie und Release-Gates](../allgemeine-app-entwicklung/06-tests-release-betrieb/teststrategie-und-release-gates.md).

## A. Tests vor jedem Release

- [ ] `PFLICHT` **Kernablauf auf echten Geräten** durchspielen: iPhone, Android, Desktop-Browser, Safari (verhält sich oft anders).
- [ ] `PFLICHT` **Zwei-Konten-Test:** Nutzer A sieht und ändert keine Daten von Nutzer B.
- [ ] `PFLICHT` **Zahlungen im Testmodus komplett:** Kauf, Verlängerung, Kündigung, Widerruf, fehlgeschlagene Zahlung, Webhook kommt doppelt oder verspätet.
- [ ] `PFLICHT` **Konto löschen testen:** Sind danach wirklich alle Daten weg (Datenbank, Dateien, Vektor-Datenbank, Drittanbieter)?
- [ ] `PFLICHT` **Rechtsseiten und Pflichtfunktionen** erreichbar (siehe [09](./09-pflichtfunktionen.md)).
- [ ] `SOLLTE` **Fehlerfälle testen:** kein Internet, KI-API antwortet nicht, Upload zu groß, Limit erreicht.
- [ ] `SOLLTE` **Limits testen:** Greifen Rate-Limits und Kontingente wirklich?
- [ ] `SOLLTE` **KI-Evals grün** (siehe [07](./07-ki-api-modelle-kosten-qualitaet.md)).
- [ ] `SOLLTE` **Barrierefreiheit prüfen** (siehe [11](./11-design-barrierefreiheit.md)).
- [ ] `SOLLTE` **Beta-Test mit echten Nutzern** (TestFlight, Google Play Closed Testing, Vorschau-Link).
- [ ] `SOLLTE` **Keine bekannten ausnutzbaren Schwachstellen ausliefern.** Vor jedem Release `npm audit --omit=dev` oder einen OSV-Scan laufen lassen und kritische sowie aktiv ausgenutzte Lücken beheben. Für Produkte unter dem CRA ist das ab 11. Dezember 2027 Pflicht.
- [ ] `SOLLTE` **Langsames Netz und ältere Geräte testen:** Ladezeiten, Akku, Speicherverbrauch, Verhalten bei Verbindungsabbruch.
- [ ] `SOLLTE` **Grenzwerte testen:** leere und sehr lange Eingaben, Sonderzeichen, Emojis, HTML- und SQL-artige Texte, ungültige Daten, unbekannte Auswahlwerte, Beträge mit Rundung.
- [ ] `SOLLTE` **Doppelte Aktionen testen:** Doppelklick, Zurück-Taste, zweimal Absenden, zwei Tabs gleichzeitig.
- [ ] `KANN` **Lasttest** der wichtigsten Endpunkte vor großem Marketing-Push.

## B. Deployment

- [ ] `SOLLTE` **Automatisches Deployment** aus `main`, nur wenn alle Prüfungen grün sind.
- [ ] `PFLICHT` **Zurückrollen möglich:** vorherige Version mit wenigen Klicks wiederherstellbar.
- [ ] `SOLLTE` **Migrationen vor dem Deployment testen** (in Staging mit realistischen Datenmengen).
- [ ] `SOLLTE` **Feature-Flags** für riskante neue Funktionen (erst für wenige Nutzer, dann für alle).
- [ ] `SOLLTE` **Mobile Apps:** Store-Prüfzeit einplanen, Over-the-Air-Updates nur für erlaubte Änderungen, Mindestversion erzwingen können (für kritische Fixes).
- [ ] `SOLLTE` **Release-Notizen** für Nutzer und ein internes Änderungsprotokoll.
- [ ] `SOLLTE` **Gestaffelt veröffentlichen** (Phased Release bei Apple, gestaffeltes Rollout bei Google Play), damit Fehler nur wenige Nutzer treffen.
- [ ] `SOLLTE` **Am Release-Tag erreichbar sein** und Monitoring, Support-Postfach und Kosten aktiv beobachten.
- [ ] `SOLLTE` **Domain und DNS absichern:** Registrar-Konto mit Mehr-Faktor-Anmeldung, Transfersperre, automatische Verlängerung.

## C. Überwachung (Monitoring)

- [ ] `PFLICHT` **Fehler-Tracking** in App und Backend (z. B. Sentry), mit Filter für personenbezogene Daten.
- [ ] `SOLLTE` **Verfügbarkeitsüberwachung** mit Alarm aufs Handy (Website, API, wichtige Hintergrundjobs).
- [ ] `SOLLTE` **KI-Kennzahlen:** Antwortzeit, Fehlerquote, Kosten pro Tag, Tokens pro Nutzer, Anteil negativer Bewertungen.
- [ ] `PFLICHT` **Kostenalarme** bei allen Anbietern (KI, Hosting, Datenbank, E-Mail, SMS).
- [ ] `SOLLTE` **Produkt-Analyse datenschutzkonform:** Aktivierung, Nutzung der Kernfunktion, Wiederkehr, Kündigungsgründe.
- [ ] `SOLLTE` **Android-Vitals im Blick behalten.** Liegt die Absturzrate über 1,09 % oder die Rate „App reagiert nicht“ über 0,47 %, kann Google Play die App seltener zeigen und im Store warnen. Werte wöchentlich in der Play Console prüfen.
- [ ] `SOLLTE` **Logs zentral,** durchsuchbar und mit begrenzter Aufbewahrung.
- [ ] `SOLLTE` **Wöchentlicher Blick** auf Fehler, Kosten und Feedback – feste Zeit im Kalender.

## D. Backups und Wiederherstellung

- [ ] `PFLICHT` **Automatische Datenbank-Backups.** Den Tarif prüfen: Gratis-Tarife bieten oft keine oder nur eingeschränkte Backups. Beispiel Supabase: tägliche Backups erst ab dem Pro-Tarif, Dateien aus Storage sind nicht enthalten; im Gratis-Tarif per Zeitplan selbst sichern (`supabase db dump`).
- [ ] `PFLICHT` **Wiederherstellung mindestens einmal testen.** Ein Backup, das nie zurückgespielt wurde, ist nur eine Hoffnung.
- [ ] `SOLLTE` **Dateispeicher sichern** (Uploads, generierte Medien), nicht nur die Datenbank.
- [ ] `SOLLTE` **3-2-1-Regel** für wichtige Daten: drei Kopien, zwei Speicherarten, eine an einem anderen Ort – außerhalb des Hauptkontos, sodass sie mit denselben Zugangsdaten und vom Coding-Agenten nicht gelöscht werden kann.
- [ ] `SOLLTE` **Code, Konfiguration und Rechtstexte** zusätzlich außerhalb des Hosting-Anbieters sichern.
- [ ] `SOLLTE` **Wiederherstellungsziele festlegen:** Wie viel Datenverlust ist tragbar, wie lange darf die App ausfallen?

## E. Notfälle

- [ ] `PFLICHT` **Notfallplan schriftlich:** Wer macht was bei Datenleck, Ausfall, gehacktem Konto, Kostenexplosion. Vorlagen: [Runbooks](../allgemeine-app-entwicklung/15-runbooks/README.md).
- [ ] `PFLICHT` **Datenpanne:** Meldung an die Datenschutzbehörde innerhalb von 72 Stunden (siehe [02](./02-datenschutz-dsgvo.md)).
- [ ] `PFLICHT` **CRA-Meldung** bei aktiv ausgenutzten Schwachstellen und schweren Vorfällen über die ENISA-Meldeplattform: Frühwarnung in 24 Stunden, Meldung in 72 Stunden, danach Abschlussbericht (Details in [03](./03-verbraucherrecht-und-weitere-gesetze.md)).
- [ ] `PFLICHT` **Bei kompromittiertem Paket alle Zugänge tauschen.** Wurde eine bekannt bösartige Paketversion installiert, alle Keys und Tokens (GitHub, npm, Cloud, KI, Datenbank) von einem sauberen Gerät aus austauschen. Danach Paket-Caches leeren, das Projekt aus einem bekannten guten Stand neu bauen und auch Agenten- und Editor-Konfigurationen auf Änderungen prüfen.
- [ ] `SOLLTE` **Keys schnell rotieren können** (Liste aller Keys mit Ort und Anleitung).
- [ ] `SOLLTE` **Statusseite und Textvorlagen** für Nutzerinformation bei Störungen.
- [ ] `SOLLTE` **Nachbesprechung nach jedem Vorfall:** Ursache, Maßnahmen, Termin. Vorlage: [Incident-Report](../allgemeine-app-entwicklung/vorlagen/incident-report.md).

## F. Wartung

- [ ] `PFLICHT` **Sicherheitsupdates** für einen angemessenen Zeitraum bereitstellen (Aktualisierungspflicht bei digitalen Produkten, § 327f BGB).
- [ ] `PFLICHT` **Kritische Framework-Updates innerhalb von Tagen einspielen.** Sicherheitsmeldungen für Next.js, React und andere Kern-Frameworks abonnieren und kritische Patches sofort einspielen. Die Lücke „React2Shell“ (Dezember 2025) erlaubte die Übernahme von Servern ohne Anmeldung und wurde zwei Tage nach Bekanntwerden ausgenutzt. Next.js kündigt Sicherheitsreleases seit Juli 2026 vorab im Blog an – den Termin einplanen und am selben Tag aktualisieren.
- [ ] `PFLICHT` **Nur Versionen mit Sicherheitsupdates nutzen.** Node.js 20 bekommt keine Updates mehr (22 oder 24 nutzen). Next.js-Hauptversionen werden zwei Jahre nach Erscheinen nicht mehr gepflegt; Next.js 15 (erschienen am 21. Oktober 2024) fällt damit um den 21. Oktober 2026 heraus, deshalb auf 16 umsteigen. Auch die Laufzeit-Einstellung beim Hosting prüfen.
- [ ] `SOLLTE` **Monatlich Abhängigkeiten aktualisieren** und Sicherheitswarnungen abarbeiten.
- [ ] `SOLLTE` **Abkündigungen verfolgen:** KI-Modelle, SDKs, Store-Vorgaben (z. B. Mindest-API-Level bei Android), Framework-Versionen.
- [ ] `SOLLTE` **Domains und Zertifikate** automatisch verlängern, Zahlungsmittel bei Anbietern aktuell halten.
- [ ] `SOLLTE` **Rechtstexte und Quellen** quartalsweise prüfen (siehe [Quellen und Stand](./QUELLEN-UND-STAND.md)).
- [ ] `SOLLTE` **Technische Schulden** regelmäßig abbauen (Aufräum-Sprint alle paar Wochen).

## G. Produktende

- [ ] `SOLLTE` **Plan für die Einstellung der App:** Nutzer rechtzeitig informieren, Export ermöglichen, Abos beenden, Daten löschen, Store-Einträge entfernen, Anbieter kündigen.
- [ ] `PFLICHT` **Apple-Abos geordnet beenden.** Abo in App Store Connect aus dem Verkauf nehmen, den Dienst danach mindestens 31 Tage weiterbetreiben, bezahlte Laufzeiten voll liefern und Nutzer mindestens 31 Tage vorher informieren.
- [ ] `SOLLTE` **Google-Play-Abos aktiv beenden.** Ein deaktivierter Basistarif verlängert laufende Abos weiter; Abos selbst kündigen oder erstatten und in der weiter installierten App das Ende klar anzeigen.

## Typische Fehler beim Vibe-Coding

- Nur im Chrome auf dem Laptop getestet.
- Backups nie getestet – oder gar nicht vorhanden im Gratis-Tarif.
- Kein Fehler-Tracking, Probleme kommen per Ein-Stern-Bewertung.
- Kein Kostenalarm, die Rechnung kommt am Monatsende.
- Niemand weiß, wie man die letzte Version zurückholt.

## Nachweis

Testprotokoll des Releases, Screenshot der Monitoring- und Kostenalarme, Protokoll eines Restore-Tests, Notfallplan mit Kontakten, Release-Notizen.
