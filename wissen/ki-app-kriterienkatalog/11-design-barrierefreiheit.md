# 11 – Design und Barrierefreiheit

Viele Vibe-Coding-Apps sehen gleich aus: lila Farbverlauf, Emojis als Icons, zentrierte Karten, überall runde Ecken. Ein eigenes, sauberes Design macht die App glaubwürdig. Barrierefreiheit ist für viele Apps Pflicht (BFSG) und macht sie für alle besser bedienbar.

Vertiefung: [Design-Tokens und Komponenten](../allgemeine-app-entwicklung/02-design/design-tokens-und-komponenten.md).

## A. Designsystem

- [ ] `SOLLTE` **Design-Tokens festlegen:** Farben (mit Bedeutung wie Primär, Fehler, Erfolg), Abstände (4er- oder 8er-Raster), Radien, Schatten, Schriftgrößen.
- [ ] `SOLLTE` **Eine Komponentenbibliothek** konsequent nutzen (z. B. shadcn/ui, Radix, React Native Paper), statt jeden Button neu zu bauen.
- [ ] `SOLLTE` **Höchstens zwei Schriftarten** und eine feste Größenskala.
- [ ] `SOLLTE` **Jede Komponente mit allen Zuständen:** normal, Hover, Fokus, aktiv, deaktiviert, lädt, Fehler.
- [ ] `SOLLTE` **Eigene visuelle Identität** passend zur Zielgruppe. Typischen KI-Einheitslook vermeiden.
- [ ] `SOLLTE` **Dunkler Modus sauber gestaltet,** nicht nur Farben umgedreht. Kontraste in beiden Modi prüfen.
- [ ] `SOLLTE` **Design-Regeln für den Coding-Agenten** in der Agenten-Regeldatei festhalten (Tokens, Komponenten, Verbote).
- [ ] `SOLLTE` **Neues iOS-Design (Liquid Glass) prüfen.** Seit 28. April 2026 werden iOS-Apps mit dem iOS-26-SDK gebaut, Standard-Elemente bekommen dadurch den Glas-Effekt. Den Effekt nur für Navigation nutzen, nicht für Inhalte, und die Lesbarkeit mit „Transparenz reduzieren“ und „Kontrast erhöhen“ testen. Ab April 2027 müssen Uploads mit dem iOS-27-SDK gebaut sein.

## B. Layout und Geräte

- [ ] `PFLICHT` **Funktioniert auf kleinen Bildschirmen** (ab 320 px Breite) ohne seitliches Scrollen.
- [ ] `SOLLTE` **Touch-Flächen groß genug:** mindestens 44 × 44 pt (iOS) bzw. 48 × 48 dp (Android). Das Web-Minimum steht in Abschnitt D.
- [ ] `SOLLTE` **Sichere Bereiche beachten** (Notch, Home-Indikator, Tastatur überdeckt keine Eingabefelder).
- [ ] `SOLLTE` **Einheitliche Navigation,** höchstens fünf Hauptpunkte in einer Tab-Leiste.
- [ ] `SOLLTE` **Plattform-Konventionen respektieren** (iOS Human Interface Guidelines, Android Material Design) bei nativen Apps.
- [ ] `SOLLTE` **Auf echten Geräten testen,** auch auf einem älteren, langsameren Handy.
- [ ] `SOLLTE` **Lange Texte einplanen.** Deutsche Wörter und Übersetzungen sind oft länger als englische – Buttons und Karten dürfen nicht abschneiden.
- [ ] `SOLLTE` **Faltbare iPhones einplanen.** Ab dem iPhone Duo (erhältlich ab 23. Oktober 2026) ändert sich die App-Größe beim Auf- und Zuklappen: keine festen Bildschirmgrößen, kein Layout nach Ausrichtung oder Gerätetyp, mit dem größenveränderbaren Simulator testen.
- [ ] `PFLICHT` **Android 16: randlos, große Bildschirme, Zurück-Geste.** Seit 31. August 2026 müssen neue Apps und Updates bei Google Play Android 16 (API 36) als Ziel haben (auf Antrag Verlängerung bis 1. November 2026). Die App zeichnet dann immer hinter Status- und Navigationsleiste (Abstände einplanen), muss auf Tablets und Faltgeräten jede Größe und Ausrichtung können und die neue Zurück-Geste unterstützen.

## C. Barrierefreiheit – Grundlagen (WCAG 2.2, Stufe AA)

Pflicht, wenn das BFSG gilt (siehe [03](./03-verbraucherrecht-und-weitere-gesetze.md)). Sonst dringend empfohlen. Maßstab ist die Norm EN 301 549. Die Fassung V4.1.1 (2. September 2026) verlangt WCAG 2.2 AA; rechtlich gilt die Vermutung, dass du die Pflicht erfüllst, erst ab ihrer Fundstelle im EU-Amtsblatt (erwartet Ende November 2026). Trotzdem schon jetzt danach bauen.

- [ ] `PFLICHT` **Kontrast:** normaler Text mindestens 4,5 : 1, großer Text und Bedienelemente mindestens 3 : 1.
- [ ] `PFLICHT` **Vollständig per Tastatur bedienbar** (Web), logische Reihenfolge, keine Tastaturfallen.
- [ ] `PFLICHT` **Sichtbarer Fokus** bei Tastaturbedienung.
- [ ] `PFLICHT` **Alternativtexte** für informative Bilder und Icons ohne Text.
- [ ] `PFLICHT` **Beschriftungen für alle Eingabefelder** (nicht nur Platzhalter).
- [ ] `PFLICHT` **Fehlermeldungen verständlich,** am Feld und für Screenreader verknüpft.
- [ ] `PFLICHT` **Screenreader-Test** mit VoiceOver (iOS/macOS) und TalkBack (Android) für den Kernablauf.
- [ ] `PFLICHT` **Textvergrößerung bis 200 %** ohne Funktionsverlust (Dynamic Type, Schriftgrößen-Einstellung).
- [ ] `PFLICHT` **Informationen nicht nur über Farbe** vermitteln (z. B. Fehler auch mit Text oder Icon).
- [ ] `PFLICHT` **Nichts blinkt öfter als dreimal pro Sekunde.** Flackernde Inhalte können Anfälle auslösen.
- [ ] `SOLLTE` **Reduzierte Bewegung respektieren** (`prefers-reduced-motion`).
- [ ] `PFLICHT` **Untertitel und Alternativen für Videos und Audios.** Aufgezeichnete Videos mit Ton brauchen Untertitel, reine Audios ein Transkript, wichtige Bildinhalte zusätzlich eine Beschreibung; Live-Übertragungen brauchen Live-Untertitel.
- [ ] `PFLICHT` **Sprache festlegen.** Seite bzw. App mit der richtigen Sprache auszeichnen (`lang="de"`) und Abschnitte in anderer Sprache – auch KI-Antworten – eigens kennzeichnen, damit Screenreader richtig vorlesen.
- [ ] `PFLICHT` **Zeitlimits verlängerbar.** Nutzer können Zeitlimits abschalten, anpassen oder verlängern, z. B. bei automatischer Abmeldung.
- [ ] `PFLICHT` **Systemeinstellungen der Nutzer respektieren.** Die App übernimmt Schriftgröße, fette Schrift, erhöhten Kontrast, reduzierte Transparenz, Farbfilter und reduzierte Bewegung aus den Geräteeinstellungen und blockiert sie nicht. Den Kernablauf mit jeder dieser Einstellungen einmal testen.
- [ ] `SOLLTE` **Automatische Prüfung** mit axe oder Lighthouse im CI, plus manuelle Prüfung (Tools finden nur einen Teil der Probleme).
- [ ] `SOLLTE` **Apps nach dem Software-Kapitel der EN 301 549 prüfen.** Für native Apps gilt WCAG über Kapitel 11 der Norm; die W3C-Hilfe WCAG2ICT erklärt, wie jede Regel auf Apps übertragen wird.
- [ ] `SOLLTE` **Web: Kontrast- und Farbeinstellungen nicht aushebeln.** Die Website blockiert keine Kontrastdesigns, Farbfilter oder Schriftgrößen der Nutzer; `forced-color-adjust: none` nur, wo es unverzichtbar ist (EN 301 549 V4.1.1, Abschnitt 9.7).
- [ ] `KANN` **WCAG 3 nur beobachten.** WCAG 3 ist ein Entwurf (Stand 10. September 2026) und ersetzt WCAG 2 nicht; geprüft wird weiter nach WCAG 2.2 AA.

## D. Barrierefreiheit – weitere WCAG-2.2-Regeln

Ebenfalls Pflicht, wenn das BFSG gilt. Diese Regeln fehlen in KI-generierten Oberflächen besonders oft.

- [ ] `PFLICHT` **Barrierefreie Anmeldung und Bezahlung.** Die Anmeldung erzwingt keine Merk- oder Rätselaufgabe: Einfügen und Passwort-Manager erlauben, Codes kopierbar machen, Bilder-Captchas nur mit Alternative; Magic Link oder Passkey sind gute Wege. Auch Bezahl- und Sicherheitsschritte, inklusive eingebundener Anbieter wie Checkout-Seiten, müssen barrierefrei sein.
- [ ] `PFLICHT` **Fokus nicht verdeckt.** Ein per Tastatur ausgewähltes Element darf nicht vollständig verdeckt sein, z. B. von fester Kopfleiste, Cookie-Banner, Chat-Eingabeleiste oder Bildschirmtastatur.
- [ ] `PFLICHT` **Klickflächen mindestens 24 × 24 Pixel.** Im Web braucht jedes Bedienelement mindestens 24 × 24 CSS-Pixel oder genug Abstand zum Nachbarn.
- [ ] `PFLICHT` **Ziehen und Wischen immer mit Alternative.** Alles, was per Ziehen, Wischen oder Mehrfinger-Geste geht (Liste sortieren, Schieberegler, Wischen zum Löschen), funktioniert auch mit einfachem Tippen oder Klicken.
- [ ] `PFLICHT` **Hilfe immer an derselben Stelle.** Hilfe, Kontakt, FAQ oder Support-Chat stehen auf allen Seiten am gleichen Ort und in derselben Reihenfolge.
- [ ] `PFLICHT` **Nichts doppelt eingeben lassen.** Angaben, die Nutzer im selben Ablauf schon gemacht haben (z. B. Adresse im Checkout, Prompt nach einem Fehler), werden vorausgefüllt oder zur Auswahl angeboten. Ausnahme: aus Sicherheitsgründen nötige Wiederholung.
- [ ] `PFLICHT` **Saubere Struktur für Screenreader.** Überschriften, Listen, Tabellen und Seitenbereiche technisch richtig auszeichnen, nicht nur optisch, und in sinnvoller Lesereihenfolge. Jede Seite und jeder Screen hat einen eindeutigen Titel, auch beim Seitenwechsel in Single-Page-Apps; Überschriften und Beschriftungen beschreiben den Inhalt.
- [ ] `PFLICHT` **Name, Rolle und Zustand für jedes Bedienelement.** Eigene Buttons, Schalter und Menüs sagen dem Screenreader, was sie sind und ob sie an oder aus sind. Der sichtbare Text steckt auch im technischen Namen, damit Sprachsteuerung funktioniert.
- [ ] `PFLICHT` **Statusmeldungen ansagen.** Meldungen wie „Gespeichert“, „3 Ergebnisse“ oder „Limit erreicht“ liest der Screenreader vor, ohne dass der Fokus springt.
- [ ] `PFLICHT` **Hoch- und Querformat erlauben.** Die App nicht auf eine Bildschirmausrichtung sperren, außer es ist unverzichtbar.
- [ ] `PFLICHT` **Eingabezweck kennzeichnen.** Felder für Name, E-Mail, Adresse und Passwort bekommen den passenden `autocomplete`-Wert, damit Browser und Passwort-Manager sie ausfüllen können.
- [ ] `PFLICHT` **Tooltips und Einblendungen bedienbar.** Was bei Mauszeiger oder Fokus erscheint, lässt sich mit Esc schließen, mit der Maus erreichen und bleibt sichtbar, bis man es schließt.
- [ ] `PFLICHT` **Größere Textabstände aushalten.** Vergrößern Nutzer Zeilen-, Absatz-, Wort- oder Buchstabenabstand, wird nichts abgeschnitten.
- [ ] `PFLICHT` **Keine Überraschungen bei Fokus und Eingabe.** Ein Feld anzuklicken oder auszufüllen darf nicht automatisch absenden oder die Seite wechseln.
- [ ] `PFLICHT` **Bewegtes und Ton stoppbar.** Automatische Animationen, Karussells, Ticker und Ton über drei Sekunden lassen sich pausieren oder stoppen – auch automatisch vorgelesene KI-Antworten.
- [ ] `PFLICHT` **Gesten und Tastenkürzel sicher.** Aktionen lösen erst beim Loslassen aus und lassen sich abbrechen. Schütteln oder Neigen hat eine Alternative und ist abschaltbar; Tastenkürzel mit nur einem Buchstaben sind abschaltbar oder änderbar.
- [ ] `PFLICHT` **Links und Anleitungen ohne Farbe oder Position verständlich.** Linktexte sagen, wohin sie führen („Preise ansehen“ statt „hier“). Anleitungen verweisen nicht nur auf Farbe, Form oder Lage („der grüne Knopf rechts“).
- [ ] `PFLICHT` **Web: Inhalt überspringen und mehrere Wege.** Ein Link „Zum Inhalt springen“ und mindestens zwei Wege zu jeder Seite, z. B. Menü und Suche.
- [ ] `PFLICHT` **Text nicht als Bild.** Text als echten Text darstellen. KI-generierte Bilder mit wichtigem Text bekommen diesen Text zusätzlich als Alternativtext.
- [ ] `PFLICHT` **Einheitliche Navigation, Bezeichnungen und Fehlerhilfen.** Navigation und gleiche Funktionen sehen überall gleich aus und heißen gleich; Fehlermeldungen schlagen eine Lösung vor, wenn sie bekannt ist.
- [ ] `PFLICHT` **Fehler bei wichtigen Aktionen vermeiden.** Bei Kauf, Vertragsabschluss oder Löschen von Daten können Nutzer vorher prüfen und korrigieren oder die Aktion rückgängig machen.

## E. Barrierefreiheitsinformationen und Support

- [ ] `PFLICHT` **Barrierefreiheitsinformationen nach BFSG.** In den AGB oder an anderer gut sichtbarer Stelle steht: was die Dienstleistung ist, wie man sie nutzt, wie sie die Barrierefreiheitsanforderungen erfüllt und welche Marktüberwachungsbehörde zuständig ist (MLBF in Magdeburg) – so verlangen es § 14 BFSG und Anlage 3. Werden Anforderungen nicht erfüllt, musst du nachbessern und die Behörde informieren.
- [ ] `SOLLTE` **Kontaktweg für Hinweise auf Barrieren** anbieten und Meldungen zügig bearbeiten.
- [ ] `PFLICHT` **Support barrierefrei.** Wenn du Support anbietest (E-Mail, Chat, Hilfe-Center), ist er über barrierefreie Wege erreichbar und kann erklären, wie die App mit Hilfsmitteln wie Screenreadern funktioniert.
- [ ] `SOLLTE` **KI-Generatoren erzeugen barrierefreie Ergebnisse.** Erstellt deine App Webseiten, Dokumente oder Präsentationen, gilt sie als Autorenwerkzeug: Sie soll barrierefreie Ergebnisse erzeugen (Überschriften, Alternativtexte, Kontrast) und auf Lücken hinweisen.

## F. Texte (UX-Writing)

- [ ] `SOLLTE` **Buttons sagen, was passiert** („Entwurf speichern“ statt „OK“).
- [ ] `SOLLTE` **Fehlermeldungen erklären Problem und Lösung,** ohne Schuldzuweisung.
- [ ] `SOLLTE` **Einheitliche Anrede** (du oder Sie) und einheitliche Begriffe.
- [ ] `SOLLTE` **Keine Fachbegriffe** aus dem Code in der Oberfläche („Token“, „Webhook“, „Null“).
- [ ] `SOLLTE` **Kurze Sätze,** wichtige Information zuerst.
- [ ] `SOLLTE` **Formulare bequem:** passende Tastatur (E-Mail, Zahl, Telefon), Autovervollständigung, Passwort-Manager-freundlich, Fehler erst nach Verlassen des Feldes anzeigen.

## G. Gefühlte Geschwindigkeit

- [ ] `SOLLTE` **Skeleton-Platzhalter** statt leerer Flächen beim Laden.
- [ ] `SOLLTE` **Optimistische Aktualisierung** bei einfachen Aktionen (sofort anzeigen, im Hintergrund speichern, bei Fehler zurücksetzen).
- [ ] `SOLLTE` **Keine Layout-Sprünge** beim Nachladen.

## H. Vertrauen und faire Gestaltung

- [ ] `PFLICHT` **Keine Dark Patterns** (siehe [03](./03-verbraucherrecht-und-weitere-gesetze.md)).
- [ ] `PFLICHT` **Berechtigungen begründen,** bevor das System fragt (Kamera, Mikrofon, Standort). In iOS sind Begründungstexte (Purpose Strings) Pflicht.
- [ ] `SOLLTE` **Datenschutz-Hinweise im passenden Moment** statt nur in der Datenschutzerklärung.
- [ ] `SOLLTE` **Gleichwertige Buttons** für Zustimmen und Ablehnen.

## I. Assets

- [ ] `PFLICHT` **Lizenzen für Schriften, Icons, Bilder, Illustrationen** (siehe [04](./04-rechte-urheberrecht-lizenzen.md)).
- [ ] `SOLLTE` **App-Icon, Favicon, Vorschaubild für geteilte Links (Open Graph), Startbildschirm** in allen nötigen Größen.
- [ ] `SOLLTE` **Store-Screenshots** zeigen echte Funktionen, keine irreführenden Darstellungen.

## Typische Fehler beim Vibe-Coding

- Graue Schrift auf grauem Hintergrund, Kontrast zu niedrig.
- Icons ohne Beschriftung, Screenreader sagt nur „Button“.
- Platzhalter statt Label – nach dem Tippen weiß niemand mehr, was ins Feld gehört.
- Fokus verschwindet hinter Cookie-Banner oder fester Chat-Eingabeleiste.
- Wischen zum Löschen ohne Button-Alternative.
- Jede Seite mit anderen Abständen und Button-Stilen.
- Kamera-Berechtigung direkt beim App-Start ohne Erklärung.

## Nachweis

Design-Token-Datei, Komponentenübersicht, Kontrastprüfung, axe- oder Lighthouse-Bericht, Screenreader-Testprotokoll, Test mit Systemeinstellungen (große Schrift, Kontrast, reduzierte Bewegung), ggf. Barrierefreiheitsinformationen nach BFSG.
