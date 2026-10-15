# 13 – App Stores und Plattformen

Apple und Google prüfen Apps vor der Veröffentlichung. Viele Ablehnungen betreffen dieselben Punkte: Konto löschen, Datenschutzangaben, Kaufsystem, Login-Pflicht und Nutzerinhalte. Für KI-Apps kommen eigene Regeln hinzu. Store-Regeln ändern sich oft – vor jedem Release die aktuelle Fassung prüfen.

## A. Apple App Store

- [ ] `PFLICHT` **Konto löschen in der App,** wenn Konten angelegt werden können.
- [ ] `PFLICHT` **Datenschutzangaben (App Privacy) korrekt:** alle erhobenen Daten, auch durch SDKs und den KI-Anbieter.
- [ ] `PFLICHT` **Privacy Manifest** (`PrivacyInfo.xcprivacy`) für App und SDKs, inklusive Begründung für bestimmte System-APIs.
- [ ] `PFLICHT` **Datenweitergabe an Drittanbieter-KI offenlegen und ausdrücklich erlauben lassen,** bevor personenbezogene Daten an sie gehen (App Review Guideline 5.1.2(i), seit November 2025). Den Anbieter namentlich nennen (z. B. OpenAI, Anthropic, Google) und aktiv zustimmen lassen – bloßes Weiternutzen der App gilt nicht als Zustimmung. Beispiel: Dialog beim ersten Nutzen „Deine Eingaben werden zur Verarbeitung an [Anbieter] gesendet“ mit Button „Zustimmen“.
- [ ] `PFLICHT` **App Tracking Transparency (ATT):** Wenn die App Nutzer über Apps und Websites anderer Firmen hinweg verfolgt (z. B. Werbe-ID, Meta- oder Werbe-SDKs), vorher über den ATT-Dialog fragen. Die ATT-Antwort hat Vorrang vor dem eigenen Consent-Banner. Für die EU hat Apple ab iOS 27.2 eine alternative ATT-Abfrage mit „Weitere Informationen“ angekündigt, die in Deutschland die einzige sein soll – vor dem Release die aktuelle Umsetzung prüfen.
- [ ] `PFLICHT` **Digitale Inhalte, Abos und KI-Credits in der iOS-App über In-App-Kauf.** In der EU gelten ab 1. Oktober 2026 neue einheitliche Apple-Bedingungen: Alternative Zahlungsabwicklung (20 % bzw. 10 %) oder Links zum Kauf im Web (15 % bzw. 10 %) sind möglich, kosten aber ebenfalls Provision, und die gewählte Variante gilt laut Apple jeweils zwölf Monate. In den USA sind Links zu Web-Käufen erlaubt, andere Länder haben eigene Regeln – vor dem Release prüfen.
- [ ] `PFLICHT` **Kinderschutz bei alternativen Zahlungen in der EU** (seit 1. Oktober 2026, wenn genutzt). Alternative Zahlung oder Links zum Web-Kauf für 13- bis 17-Jährige nur hinter einer Elternschranke; für unter 13-Jährige und Kids-Apps keine Web-Kauf-Links und alternative Zahlung nur hinter Elternschranke. Alternative Zahlungen monatlich bis zum 15. an Apple melden.
- [ ] `PFLICHT` **Gekaufte KI-Credits dürfen nicht verfallen** (3.1.1). Credits oder Guthaben aus einem In-App-Kauf haben kein Ablaufdatum; begrenzte Monatskontingente nur als Teil eines Abos anbieten und klar beschreiben.
- [ ] `PFLICHT` **Im Web gekaufte Abos auch als In-App-Kauf anbieten** (3.1.3(b)). Wer ein Abo z. B. über Stripe auf der Website verkauft und es in der iOS-App freischaltet, muss es in der App zusätzlich per In-App-Kauf anbieten. Ausnahmen gelten nur für bestimmte App-Arten (z. B. Reader-Apps) und regionale Sonderregeln wie in den USA.
- [ ] `PFLICHT` **Gleichwertige Login-Option** (z. B. „Mit Apple anmelden“), wenn Login über Drittanbieter angeboten wird.
- [ ] `PFLICHT` **Nutzerinhalte und KI-Chats mit anderen Nutzern:** Filter, Melden, Blockieren, veröffentlichte Kontaktmöglichkeit. Verstoßende Inhalte entfernst du selbst zeitnah; findet Apple solche Inhalte, verlangt es einen Verbesserungsplan und kann die App, bei groben Verstößen auch das Konto, sperren (1.2, seit Juni 2026).
- [ ] `PFLICHT` **Keine Funktion nur gegen Freigabe von Systemfunktionen.** Push-Mitteilungen, Standort oder Tracking dürfen keine Bedingung für Funktionen, Inhalte oder Belohnungen (z. B. Gratis-Credits) sein (5.1.2(i)).
- [ ] `PFLICHT` **Altersfreigabe ehrlich ausfüllen.** Apple nutzt die Stufen 4+, 9+, 13+, 16+ und 18+ und fragt u. a. nach Nutzerinhalten, Social-Media-Funktionen (Feed mit Inhalten anderer Nutzer, Pflichtangabe seit September 2026), Nachrichten und Chat, uneingeschränktem Webzugriff, Werbung, Elternkontrollen, Altersprüfung sowie medizinischen und Wellness-Themen. Eine eigene KI-Frage gibt es nicht: Wenn der KI-Chat solche Inhalte liefern kann, die Antworten entsprechend wählen.
- [ ] `PFLICHT` **Begründungstexte für Berechtigungen** (Kamera, Mikrofon, Fotos, Standort) in verständlicher Sprache.
- [ ] `PFLICHT` **Abo-Informationen im Kaufbildschirm:** Preis, Laufzeit, automatische Verlängerung, Links zu Nutzungsbedingungen und Datenschutz, „Käufe wiederherstellen“.
- [ ] `PFLICHT` **Kaufbildschirm klar gestalten.** Der Betrag, der wirklich abgebucht wird, ist das auffälligste Preiselement; Umrechnungen pro Woche oder Monat stehen nur kleiner daneben. Bei Testphasen Dauer und Preis danach nennen und keinen Schalter „Testphase an/aus“ verwenden – solche Paywalls lehnt Apple laut Berichten seit Januar 2026 ab.
- [ ] `PFLICHT` **Demo-Zugang für die Prüfung** und funktionierendes Backend während der Prüfung.
- [ ] `PFLICHT` **Datenschutz-URL und Support-URL** im App Store Connect.
- [ ] `PFLICHT` **Händlerstatus nach DSA in App Store Connect** für die EU angeben. Als Händler werden Name, Adresse und Kontakt öffentlich angezeigt.
- [ ] `SOLLTE` **Mehr als eine verpackte Website.** Reine Web-Hüllen ohne App-Mehrwert werden oft abgelehnt.
- [ ] `PFLICHT` **Keine Nachahmung anderer Apps** (Name, Icon, Oberfläche) und keine Icons, Marken oder Produktnamen anderer Entwickler ohne Erlaubnis (4.1).
- [ ] `PFLICHT` **Keine Duplikat- und Massen-Apps** (4.3). Mehrere fast gleiche Apps oder Apps ohne Unterschied zu vorhandenen lehnt Apple ab; seit Juni 2026 kann Apple solche Apps auch nachträglich entfernen, und wiederholte Einreichungen können zum Ausschluss aus dem Developer Program führen. Eine KI-App braucht deshalb einen klaren eigenen Nutzen gegenüber einem allgemeinen Chatbot.
- [ ] `PFLICHT` **Keine Apps aus Vorlagen oder App-Generatoren ohne eigenen Inhalt** (4.2.6). Apps aus kommerziellen Baukästen werden abgelehnt, wenn nicht der Inhaber des Inhalts sie selbst einreicht. Mit KI-Baukästen erstellte Apps im eigenen Konto einreichen und klar eigenständig gestalten.
- [ ] `PFLICHT` **Kein nachgeladener oder KI-erzeugter Code, der die iOS-App verändert** (2.5.2). Die App darf keinen Code herunterladen oder ausführen, der neue Funktionen bringt; laut Presseberichten hat Apple deshalb im März 2026 Updates von Vibe-Coding-Apps zurückgehalten. Over-the-Air-Updates nicht für neue Funktionen nutzen.
- [ ] `PFLICHT` **Creator-Apps** (Nutzer oder KI erzeugen Inhalte): Zugang zu Inhalten über der Altersfreigabe anhand bestätigten oder angegebenen Alters beschränken (1.2.1(a)).
- [ ] `PFLICHT` **Mehrere oder von Nutzern erstellte Chatbots** (4.7). Bietet die App auswählbare oder von Nutzern erstellte Chatbots an, bist du für jeden verantwortlich: Filter, Melden, Blockieren, ein Verzeichnis aller Bots und eine Altersbeschränkung für Bots über der Altersfreigabe. Daten gehen an einzelne Bots nur mit ausdrücklicher Zustimmung im Einzelfall.
- [ ] `PFLICHT` **Keine Apps für zufällige oder anonyme Chats.** Apps, die vor allem für zufällige oder anonyme Chats mit Fremden genutzt werden, gehören laut Apple (1.2, seit Februar 2026) nicht in den App Store und können ohne Vorwarnung entfernt werden.
- [ ] `PFLICHT` **Regulierte Bereiche als passende Firma einreichen** (5.1.1(ix)). Apps für Bank- und Finanzdienste, Gesundheitsversorgung, Glücksspiel, Krypto-Börsen oder Flugreisen sollen von der Organisation eingereicht werden, die den Dienst erbringt – als Privatperson drohen hier Ablehnungen.
- [ ] `KANN` **Declared Age Range API** von Apple nutzen, um die Altersgruppe datensparsam abzufragen.
- [ ] `PFLICHT` **Gesundheits- und Messfunktionen:** Genauigkeit nachweisen können; keine Diagnosen versprechen, die nicht belegt sind.
- [ ] `PFLICHT` **Medizinprodukt-Status in App Store Connect angeben,** wenn die App in „Gesundheit und Fitness“ oder „Medizin“ eingeordnet ist oder laut Altersfragebogen häufig medizinische Informationen enthält (EWR, UK, USA). Kein Medizinprodukt: „Nein“ wählen. Neue Apps seit 26. März 2026, bestehende bis Anfang 2027 – sonst sind keine Updates mehr möglich.
- [ ] `PFLICHT` **Bewertungen nur über die offizielle Bewertungsfunktion anfragen.** Keine eigenen Bewertungs-Pop-ups, keine Belohnung, kein Vorfiltern („Gefällt dir die App?“ und nur Zufriedene weiterleiten). Nicht beim ersten Start und nicht mitten in einer Aufgabe; Apple zeigt den Dialog höchstens dreimal in 365 Tagen.
- [ ] `SOLLTE` **Barrierefreiheitsangaben im App Store** (Accessibility Nutrition Labels) in App Store Connect ausfüllen. Eine Funktion wie VoiceOver nur angeben, wenn erster Start, Anmeldung, Kauf, Einstellungen und Kernfunktion damit vollständig klappen; Apple will die Angaben später verpflichtend machen.
- [ ] `SOLLTE` **Tracking-Domains im Privacy Manifest eintragen** (`NSPrivacyTrackingDomains`). Ohne ATT-Zustimmung blockiert iOS Verbindungen dorthin – prüfen, ob Analytics- und Werbe-SDKs sich ohne Zustimmung richtig verhalten.
- [ ] `SOLLTE` **Keine Hinweise auf andere Plattformen oder externe Käufe,** außer wo ausdrücklich erlaubt.
- [ ] `SOLLTE` **Apple Small Business Program vor dem ersten Verkauf beantragen.** Bis 1 Mio. US-Dollar Jahreserlös sinkt die Provision von 30 % auf 15 % (in der EU ab 1. Oktober 2026 von 26 % auf 15 %); der niedrige Satz gilt erst ab Aufnahme ins Programm.

## B. Google Play

- [ ] `PFLICHT` **Konto löschen in der App und zusätzlich über eine Webseite** (Link in der Play Console).
- [ ] `PFLICHT` **Formular zur Datensicherheit (Data Safety)** passend zu App, SDKs und Datenschutzerklärung.
- [ ] `PFLICHT` **Nutzerdaten-Richtlinie gilt auch für KI-Integrationen von Drittanbietern** (Klarstellung Juli 2026): Daten nur begrenzt nutzen, offenlegen und Einwilligung einholen.
- [ ] `PFLICHT` **Richtlinie für KI-generierte Inhalte:** Schutz vor verbotenen Inhalten und eine Möglichkeit in der App, anstößige KI-Inhalte zu melden oder zu markieren.
- [ ] `PFLICHT` **Ziel-API-Level aktuell halten.** Seit 31. August 2026 müssen neue Apps und Updates Android 16 (API 36) als Ziel haben; Apps unter Android 15 (API 35) sehen neue Nutzer auf neueren Geräten nicht mehr. Die Grenze steigt jedes Jahr Ende August. Wer mehr Zeit braucht, kann in der Play Console eine Verlängerung bis 1. November 2026 beantragen.
- [ ] `PFLICHT` **Android-Entwicklerverifizierung und App-Registrierung.** Google-Play-Apps mussten bis 30. September 2026 in der Play Console registriert sein, sonst droht die weltweite Entfernung – den Status in der Play Console prüfen. Für Apps außerhalb von Google Play gilt die Verifizierung seit 30. September 2026 in Brasilien, Indonesien, Singapur und Thailand, weltweit ab 2027; für Hobby-Projekte gibt es Konten mit begrenzter Verteilung (bis 20 Geräte, ohne Gebühr).
- [ ] `PFLICHT` **Geschlossener Test vor dem ersten Produktions-Release.** Private Entwicklerkonten, die nach dem 13. November 2023 erstellt wurden, brauchen mindestens 12 Tester, die 14 Tage ohne Unterbrechung teilnehmen; erst danach kann der Produktionszugang beantragt werden.
- [ ] `PFLICHT` **Google Play Billing** für digitale Güter, mit regionalen Ausnahmen.
- [ ] `PFLICHT` **Inhaltsbewertung (IARC) und Zielgruppe** korrekt. Bei Kindern als Zielgruppe gilt die Families-Richtlinie.
- [ ] `PFLICHT` **Händlerstatus nach DSA in der Play Console** angeben.
- [ ] `PFLICHT` **Daten der Age Signals API** nur für altersgerechte Inhalte verwenden, nicht für Werbung, Profiling oder Analytics (seit 1. Januar 2026).
- [ ] `PFLICHT` **Anonyme oder zufällige Chats.** Seit 26. August 2026 gelten für solche Apps die Regeln für altersbeschränkte Inhalte: Minderjährige mit der Funktion „Restrict Minor Access“ in der Play Console ausschließen. Solche Apps dürfen sich nicht an Kinder richten.
- [ ] `SOLLTE` **Kein reiner Modell-Wrapper.** Apps ohne eigene Funktion außer dem Weiterreichen an ein Sprachmodell riskieren Ablehnung nach den Spam- und Mindestfunktions-Regeln.
- [ ] `PFLICHT` **Sensible Berechtigungen nur mit genehmigtem Zweck,** z. B. Bedienungshilfen, Standort im Hintergrund, SMS, Anrufliste sowie Fotos und Videos. Wer nur gelegentlich Bilder hochladen lässt (z. B. für KI-Bildbearbeitung), nutzt die Android-Fotoauswahl (Photo Picker) statt Vollzugriff; ab 27. Januar 2027 gilt Ähnliches für Kontakte. Ab dann außerdem: für genauen Standort möglichst den Standort-Button und keine Anrufliste für die Verifizierung per Anruf (stattdessen SMS Retriever oder Digital Credentials API).
- [ ] `PFLICHT` **Google-Play-Abo-Regeln.** Preis, Abrechnungszeitraum, automatische Verlängerung und Bedingungen der Testphase vor dem Kauf in Sprache und Währung der Nutzer zeigen. Kein versteckter Schließen-Button, keine Monatsumrechnung statt des echten Betrags, Link zur Abo-Verwaltung von Google Play.
- [ ] `PFLICHT` **Erklärungen zu Finanz- und Gesundheitsfunktionen** in der Play Console ausfüllen – für **alle** Apps, auch wenn sie keine solchen Funktionen haben (dann das bestätigen).
- [ ] `PFLICHT` **Bewertungen nur über die In-App-Review-Schnittstelle anfragen.** Keine Belohnung, kein Vorfiltern mit Vorab-Fragen und kein eigener Button, der den Dialog auslöst – das verbietet Google ausdrücklich.
- [ ] `PFLICHT` **Werbe-ID richtig nutzen und angeben.** Die Werbe-ID (Advertising ID) nur für Werbung und Analyse verwenden, den Widerspruch gegen personalisierte Werbung bei jedem Zugriff beachten und die Nutzung in der Datenschutzerklärung nennen. Apps ab Android 13 brauchen dafür die Berechtigung `AD_ID` im Manifest; die Angaben zu Werbung und Werbe-ID in der Play Console (App-Inhalte) müssen dazu passen.
- [ ] `SOLLTE` **Vorab-Bericht** (Pre-launch report) auswerten.

## C. Web und PWA

- [ ] `SOLLTE` **Grundlagen für Suchmaschinen:** Titel, Beschreibung, Open-Graph-Bild, `sitemap.xml`, `robots.txt`.
- [ ] `SOLLTE` **PWA-Manifest und Icons,** wenn die Web-App installierbar sein soll.
- [ ] `SOLLTE` **Strukturierte Daten** (Schema.org) für Landingpage und App-Informationen.
- [ ] `SOLLTE` **Test- und Vorschau-Versionen nicht bei Google.** Staging- und Vorschau-Adressen mit `noindex` sperren (bei eigenen Domains für Vorschauen selbst einstellen) und eine hilfreiche 404-Fehlerseite mit Link zur Startseite anbieten.
- [ ] `SOLLTE` **iOS-PWA auf einem echten iPhone testen.** Safari zeigt keinen Installations-Knopf; Nutzer wählen „Teilen > Zum Home-Bildschirm“, seit iOS 26 öffnet sich die Seite dann als Web-App. Push-Nachrichten gibt es nur für installierte Web-Apps nach Erlaubnis – eine kurze Anleitung einbauen.
- [ ] `SOLLTE` **Landingpage mit Rechtsseiten,** Preisen, Kontakt und Datenschutzhinweisen.

## D. Social-Media-Plattformen (für KI-Inhalte)

Wichtig, wenn deine App Inhalte für YouTube, TikTok, Instagram oder ähnliche Plattformen erstellt oder veröffentlicht.

- [ ] `PFLICHT` **Kennzeichnungsregeln der Plattformen:** YouTube verlangt die Offenlegung realistisch wirkender veränderter oder synthetischer Inhalte, TikTok und Meta verlangen bzw. setzen KI-Labels für realistische KI-Inhalte.
- [ ] `PFLICHT` **Automatisches Posten erst nach Plattform-Prüfung öffentlich.** Ungeprüfte TikTok-Apps posten nur privat und für höchstens 5 Nutzer in 24 Stunden, zusätzlich gilt meist ein Limit von rund 15 Posts pro Tag und Konto. YouTube setzte Uploads aus ungeprüften API-Projekten bisher auf privat; die Dokumentation ist seit Oktober 2026 widersprüchlich – die Prüfung trotzdem beantragen. Die Prüfung früh beantragen und die Vorgaben einhalten: Vorschau zeigen, Nutzer wählen Titel und Sichtbarkeit selbst, Upload erst nach ausdrücklicher Zustimmung.
- [ ] `SOLLTE` **KI-Kennzeichnung beim Posten über die API mitsenden.** YouTube bietet dafür das Feld `containsSyntheticMedia`, TikTok das Feld `is_aigc`; bei realistischen KI-Inhalten automatisch setzen.
- [ ] `SOLLTE` **Automatisierte Konten auf X kennzeichnen.** Postet die App automatisch auf X, braucht das Konto das Label „Automatisiert“ und eine Verknüpfung mit einem Konto, das ein Mensch führt. Inhalte aus der X-API dürfen nicht zum Training großer KI-Modelle genutzt werden.
- [ ] `SOLLTE` **Monetarisierungsregeln beachten.** YouTube schließt seit 15. Juli 2025 „inauthentische“ Inhalte (massenhaft produziert, sich wiederholend, ohne eigenen Beitrag) von der Monetarisierung aus; andere Plattformen haben ähnliche Regeln. KI-Clips brauchen einen erkennbaren eigenen Beitrag wie Kommentar, Schnitt oder Idee.
- [ ] `PFLICHT` **Musik- und Bildrechte** auch in automatisch erstellten Clips (siehe [04](./04-rechte-urheberrecht-lizenzen.md)).
- [ ] `PFLICHT` **Social Bots in Deutschland kennzeichnen.** Postet oder antwortet ein Programm automatisch über ein Konto, das wie das Konto eines Menschen aussieht, muss jeder automatisch erstellte Beitrag gut lesbar einen Hinweis auf die Automatisierung tragen (§ 18 Abs. 3 Medienstaatsvertrag). Das gilt auch für vorgefertigte, automatisch versendete Antworten.
- [ ] `PFLICHT` **Bots in Messengern nur nach deren Regeln.** WhatsApp, Telegram, Discord und Slack haben eigene Bedingungen für Bots. Meta hat allgemeine KI-Assistenten über die WhatsApp-Business-Schnittstelle seit 15. Januar 2026 ausgeschlossen; die EU-Kommission hat am 9. Juni 2026 einstweilige Maßnahmen dagegen angeordnet, das Verfahren läuft noch. Aufgabenbezogene Bots (Support, Termine, Bestellstatus) sind erlaubt – vor dem Start die aktuellen Business-Bedingungen prüfen.

## E. Konten, Signierung und Versionen

- [ ] `PFLICHT` **Signierschlüssel sicher aufbewahren.** Android: Upload-Key und Keystore-Passwort sicher sichern, Play App Signing nutzen. Apple: Zertifikate und Profile über das Entwicklerkonto verwalten. Wer den Schlüssel verliert, kann Updates nur mit Aufwand oder gar nicht mehr veröffentlichen.
- [ ] `SOLLTE` **Bundle-ID bzw. Paketname dauerhaft wählen** – er lässt sich nach der Veröffentlichung nicht ändern.
- [ ] `SOLLTE` **Versionen sauber zählen** (Versionsnummer für Nutzer, Build-Nummer steigt bei jedem Upload).
- [ ] `SOLLTE` **Entwicklerkonto als Organisation** früh anlegen, wenn eine Firma dahintersteht. Dafür wird eine D-U-N-S-Nummer verlangt – die Vergabe kann dauern.
- [ ] `SOLLTE` **Store-Konten absichern:** Rollen für Teammitglieder, keine geteilten Passwörter, Anmeldung per Passkey oder Sicherheitsschlüssel (Pflicht für alle Entwicklerkonten, siehe [14](./14-business-zahlungen-steuern.md)).
- [ ] `PFLICHT` **Store-Konto nicht durch wiederholte Verstöße riskieren.** Bei Google Play zählt jede App-Sperre als Verwarnung; mehrere führen zur Kündigung des Entwicklerkontos, auch verknüpfter und neuer Konten. Apple kann bei wiederholten Spam-Einreichungen, schweren Verstößen bei Nutzerinhalten oder vielen Beschwerden aus dem Developer Program ausschließen – Ablehnungen beheben, nie mit einem neuen Konto umgehen.
- [ ] `SOLLTE` **Google-Play-Entwicklerkonto aktiv halten.** Google schließt inaktive Konten, z. B. wenn ein Konto älter als ein Jahr ist und nie eine App eingereicht hat; die Registrierungsgebühr wird nicht erstattet.
- [ ] `SOLLTE` **iOS-Build einplanen:** Zum Bauen und Signieren von iOS-Apps brauchst du einen Mac mit Xcode oder einen Cloud-Build-Dienst (z. B. EAS Build bei Expo).
- [ ] `PFLICHT` **iOS-App mit aktuellem Xcode und SDK bauen.** Seit 28. April 2026 nimmt App Store Connect nur Builds an, die mit Xcode 26 und dem iOS-26-SDK erstellt wurden. Ab April 2027 nimmt Apple nur noch Builds mit dem iOS-27-SDK an. Bei Cloud-Builds (z. B. EAS) die Xcode-Version prüfen.
- [ ] `SOLLTE` **Vertriebsländer bewusst auswählen.** App Store Connect und Play Console bieten Apps standardmäßig in allen Ländern an, damit gelten auch deren Gesetze. Beispiel USA: Für neue Konten in Texas (seit 4. Juni 2026), Utah (seit 6. Mai 2026) und Louisiana (seit 1. Juli 2026) verlangt Apple eine Altersabfrage über die Declared Age Range API und Elternzustimmung bei wesentlichen Änderungen; Google Play setzt Texas über die Play Age Signals API um. Wer das nicht umsetzt, schließt die USA zunächst aus.
- [ ] `KANN` **Alternative Vertriebswege in der EU prüfen.** Alternative Marktplätze und Web-Vertrieb für iOS haben eigene Zugangsvoraussetzungen, die Apple zum 1. Oktober 2026 erweitert hat – aktuell prüfen. Apple prüft die App trotzdem (Notarisierung) und verlangt 5 % Provision (Core Technology Commission). Für Einsteiger ist meist der App Store der realistische Weg.

## F. Vor dem Einreichen

- [ ] `SOLLTE` **Store-Texte ehrlich:** keine Funktionen versprechen, die es nicht gibt, keine falschen Bewertungen, keine fremden Marken.
- [ ] `SOLLTE` **Screenshots aktuell** und für alle geforderten Gerätegrößen. Ab April 2027 verlangt Apple zusätzlich Screenshots für das iPhone Duo.
- [ ] `PFLICHT` **In-App-Käufe für die Prüfung bereitstellen** (Apple 2.1(b)). Alle Kaufoptionen müssen vollständig, für Prüfer sichtbar und funktionsfähig sein und mit der App-Version eingereicht werden.
- [ ] `SOLLTE` **Hinweise für die Prüfer:** wie die KI-Funktion getestet werden kann, Demo-Zugang, besondere Berechtigungen.
- [ ] `SOLLTE` **Alle Angaben mit dem echten Datenfluss abgleichen** (Datenschutzerklärung, Store-Formulare, SDK-Liste).
- [ ] `PFLICHT` **Fragen zur Verschlüsselung (Exportkontrolle) richtig beantworten.** App Store Connect fragt bei jedem Build, ob die App Verschlüsselung nutzt. Nutzt sie nur die eingebaute Verschlüsselung des Systems (z. B. HTTPS), ist sie meist befreit; eigene oder mitgelieferte Krypto-Bibliotheken können Unterlagen erfordern. Den Schlüssel `ITSAppUsesNonExemptEncryption` in der `Info.plist` setzen, damit die Frage nicht bei jedem Upload kommt.

## G. Desktop-Apps und Browser-Erweiterungen

- [ ] `PFLICHT` **macOS-Apps signieren und notarisieren.** Außerhalb des Mac App Store vertriebene Apps mit einer Developer ID signieren und bei Apple notarisieren lassen. Sonst blockiert macOS (Gatekeeper) den Start.
- [ ] `PFLICHT` **Developer-ID-Zertifikat rechtzeitig erneuern** (wenn du Mac-Apps oder Installer außerhalb des Mac App Store vertreibst). Die alte Zertifizierungsstelle läuft am 1. Februar 2027 ab: vorher ein neues Zertifikat erstellen und `.pkg`-Installer neu signieren.
- [ ] `SOLLTE` **Mac-Apps für Apple Silicon bauen.** macOS 27 ist die letzte Version mit Rosetta; reine Intel-Apps laufen danach nicht mehr. Als Universal-Binary oder arm64 ausliefern, auch bei Electron.
- [ ] `SOLLTE` **Windows-Apps und Installer signieren.** Ohne Code-Signatur zeigt Windows (SmartScreen) Warnungen und viele Nutzer brechen ab. Signatur über ein Zertifikat, einen Signierdienst von Microsoft oder den Microsoft Store.
- [ ] `PFLICHT` **Electron-Apps nach der Sicherheits-Checkliste bauen.** Kontextisolierung und Sandbox an, Node.js-Zugriff für Webinhalte aus, keine fremden Webseiten mit vollen Rechten laden, Absender jeder IPC-Nachricht prüfen, `shell.openExternal` nur mit geprüften Adressen und Electron aktuell halten. Sonst kann eine präparierte Webseite oder KI-Antwort Programme auf dem Rechner starten.
- [ ] `PFLICHT` **Browser-Erweiterungen nach den Regeln des Chrome Web Store.** Ein klar umrissener Zweck, nur die nötigsten Berechtigungen, Datenschutzerklärung und deutliche Offenlegung vor der Installation, Nutzerdaten nur für diesen Zweck (kein Verkauf, keine Werbung) und kein nachgeladener Code. Seit 1. August 2026 nur Daten, die für diesen Zweck unbedingt nötig sind, Änderungen nach der Installation aktiv mitteilen; Erweiterungen, die Schutzfilter von KI-Diensten umgehen, sind verboten. Andere Browser-Stores haben ähnliche Regeln.
- [ ] `KANN` **Microsoft Store als Vertriebsweg prüfen.** Die Registrierung ist für Einzelentwickler kostenlos (mit Identitätsprüfung); auch Web-Apps (PWA) lassen sich dort einreichen.
- [ ] `SOLLTE` **Erweiterungen mit KI vor fremden Webseiten schützen.** Liest eine Erweiterung Seiteninhalte und gibt sie an eine KI, können versteckte Anweisungen auf der Seite die KI steuern (indirekte Prompt Injection, siehe [06](./06-ki-sicherheit-llm-risiken.md)). Aktionen nur nach Bestätigung, keine Zugangsdaten oder Cookies an die KI.

## Typische Fehler beim Vibe-Coding

- Expo- oder Capacitor-App ohne Konto-Löschung eingereicht.
- KI-Anbieter fehlt in den Datenschutzangaben.
- Stripe-Checkout für digitale Inhalte in der iOS-App.
- Google-Login ohne Apple-Login-Alternative.
- Kein Melden-Button für KI-Inhalte in der Android-App.
- KI-erzeugter Code wird in der iOS-App nachgeladen oder per Over-the-Air-Update neue Funktion ausgeliefert.
- Paywall mit Schalter „Testphase an/aus“ oder Monatspreis größer als der echte Abbuchungsbetrag.

## Nachweis

Checkliste pro Store mit Datum, Screenshots der Store-Formulare, Prüfernotizen, Ablehnungsgründe und deren Behebung.
