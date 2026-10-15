# 09 – Pflichtfunktionen jeder App

Diese Funktionen werden beim Vibe-Coding oft vergessen, weil sie nicht zur „coolen“ Kernfunktion gehören. Viele davon verlangen Gesetze oder App Stores. Ohne sie wirkt eine App unfertig – und wird im Store abgelehnt.

## A. Konto und Anmeldung

- [ ] `PFLICHT` **Registrieren, Anmelden, Abmelden, Passwort vergessen** (oder passwortlos per Magic Link oder Passkey).
- [ ] `PFLICHT` **Konto löschen direkt in der App,** leicht auffindbar (Apple, Google Play, DSGVO). Deaktivieren reicht nicht. Google Play verlangt zusätzlich einen Löschweg im Web.
- [ ] `PFLICHT` **„Mit Apple anmelden“ beim Löschen widerrufen.** Wer Sign in with Apple anbietet, widerruft beim Löschen des Kontos die Anmeldedaten über die Apple-Schnittstelle. Die Löschung darf keinen Anruf und keine Support-E-Mail verlangen, außer in stark regulierten Branchen.
- [ ] `SOLLTE` **Neue Apple-Relay-Adressen akzeptieren.** Bei „Mit Apple anmelden“ vergibt Apple neue private E-Mail-Adressen unter `private.icloud.com` (alte unter `privaterelay.appleid.com` bleiben gültig). E-Mail-Prüfung, Erlaubnislisten und Kontologik müssen beide Domains annehmen, sonst scheitert die Anmeldung.
- [ ] `PFLICHT` **Löschung erklärt,** was gelöscht wird, was aus rechtlichen Gründen aufbewahrt wird (z. B. Rechnungen) und dass ein Store-Abo separat gekündigt werden muss.
- [ ] `PFLICHT` **Datenexport** (DSGVO), mindestens auf Anfrage. `SOLLTE` als Self-Service in den Einstellungen.
- [ ] `SOLLTE` **E-Mail und Passwort ändern,** mit Bestätigung.
- [ ] `PFLICHT` **Apple: gleichwertige Login-Option,** wenn du Drittanbieter-Login (z. B. Google) anbietest – z. B. „Mit Apple anmelden“.
- [ ] `SOLLTE` **Nutzung ohne Konto,** wo möglich (Apple lehnt unnötigen Login-Zwang ab).
- [ ] `SOLLTE` **Sitzungen und Geräte verwalten,** „Überall abmelden“.
- [ ] `SOLLTE` **Mindestalter abfragen,** wenn die App nicht für Kinder gedacht ist (Altersgrenze aus AGB und KI-Anbieter-Richtlinien).
- [ ] `SOLLTE` **Sicherheits-Benachrichtigungen** bei neuem Gerät, Passwort- oder E-Mail-Änderung.

## B. Rechtliche Seiten (in App und Website)

- [ ] `PFLICHT` **Impressum** (siehe [03](./03-verbraucherrecht-und-weitere-gesetze.md)).
- [ ] `PFLICHT` **Datenschutzerklärung** (siehe [02](./02-datenschutz-dsgvo.md)).
- [ ] `PFLICHT` **Nutzungsbedingungen / AGB,** sobald ein Vertrag entsteht.
- [ ] `PFLICHT` **Widerrufsbelehrung** bei Käufen und Abos von Verbrauchern.
- [ ] `PFLICHT` **Cookie- und Tracking-Einstellungen,** jederzeit wieder aufrufbar.
- [ ] `PFLICHT` **Kündigungsbutton und Widerrufsbutton** bei online abgeschlossenen Verträgen.
- [ ] `PFLICHT` **Barrierefreiheitsinformationen** nach § 14 BFSG und Anlage 3, wenn das BFSG gilt (siehe [11](./11-design-barrierefreiheit.md)).
- [ ] `PFLICHT` **Open-Source-Lizenzen,** wenn Lizenzen einen Hinweis verlangen.
- [ ] `SOLLTE` **KI-Transparenzseite:** Welche KI wird genutzt, wofür, was passiert mit Eingaben, welche Grenzen gibt es.
- [ ] `SOLLTE` **Nutzungsrichtlinie:** Was ist in der App verboten.

## C. KI-Funktionen

- [ ] `PFLICHT` **KI-Hinweis** im Chat oder Assistenten (AI Act Art. 50).
- [ ] `PFLICHT` **Kennzeichnung generierter Medien** (maschinenlesbar, bei Deepfakes sichtbar).
- [ ] `SOLLTE` **Hinweis „KI kann Fehler machen“** dort, wo Fehler Folgen haben.
- [ ] `SOLLTE` **Feedback und Melden** pro Antwort oder generiertem Inhalt.
- [ ] `SOLLTE` **Verbrauchsanzeige** (verbleibende Anfragen oder Credits).
- [ ] `SOLLTE` **Verlauf ansehen und löschen.**
- [ ] `SOLLTE` **Stoppen, neu generieren, kopieren, bearbeiten** von Antworten.
- [ ] `SOLLTE` **Gedächtnis (Memory) anzeigen und löschen,** falls vorhanden.

## D. Einstellungen

- [ ] `SOLLTE` **Sprache** (mindestens vorbereitet für weitere Sprachen).
- [ ] `SOLLTE` **Dunkles und helles Design** (System folgen).
- [ ] `SOLLTE` **Benachrichtigungen** einzeln ein- und ausschaltbar. Push erst nach Zustimmung.
- [ ] `SOLLTE` **Datenschutz-Einstellungen:** Training erlauben oder nicht, Analytics, Gedächtnis.
- [ ] `SOLLTE` **Abo verwalten** (Tarif, Rechnungen, Zahlungsmittel, Kündigung).

## E. Zahlungen und Abos

- [ ] `PFLICHT` **Preisseite mit Endpreisen** inkl. MwSt und Laufzeit.
- [ ] `PFLICHT` **Kaufstrecke nach Verbraucherrecht** (Pflichtinfos, Bestellbutton, Bestätigung per E-Mail).
- [ ] `PFLICHT` **Rechnungen** mit allen Pflichtangaben.
- [ ] `PFLICHT` **Kündigen ohne Hürden** (Kündigungsbutton bzw. Store-Aboverwaltung).
- [ ] `PFLICHT` **„Käufe wiederherstellen“** bei Store-Käufen in iOS- und Android-Apps.
- [ ] `SOLLTE` **Fehlgeschlagene Zahlungen** behandeln (Erinnerung, Kulanzzeit, dann Einschränkung).
- [ ] `SOLLTE` **Upgrade und Downgrade** mit anteiliger Verrechnung.
- [ ] `SOLLTE` **Testphase transparent** mit Erinnerung vor Ablauf.

Vertiefung: [Zahlungen und Abos](../allgemeine-app-entwicklung/08-zahlungen-und-abos/README.md).

## F. Hilfe und Support

- [ ] `PFLICHT` **Kontaktmöglichkeit** (mindestens E-Mail laut Impressum; Stores verlangen eine Support-URL).
- [ ] `PFLICHT` **Service-Hotline ohne Aufpreis.** Bietest du eine Telefonnummer für Fragen zu bestehenden Verträgen an, darf sie nicht mehr kosten als der normale Telefontarif (§ 312a Abs. 5 BGB).
- [ ] `SOLLTE` **Hilfe-Bereich oder FAQ** mit den häufigsten Fragen.
- [ ] `SOLLTE` **Feedback-Formular** in der App.
- [ ] `SOLLTE` **Statusseite** oder Hinweis bei Störungen.
- [ ] `PFLICHT` **Bei Nutzerinhalten und Kontakt zwischen Nutzern:** Inhalte melden, Nutzer blockieren, Moderation (Apple-Regel und DSA).

## G. Einstieg und Zustände

- [ ] `SOLLTE` **Onboarding bis zum ersten Erfolg** in wenigen Schritten (nicht fünf Info-Folien).
- [ ] `SOLLTE` **Beispiel-Eingaben** für KI-Funktionen.
- [ ] `PFLICHT` **Lade-, Leer-, Fehler- und Offline-Zustände** für jeden Screen. Kein weißer Bildschirm, kein ewiger Spinner.
- [ ] `SOLLTE` **Erfolgsbestätigungen** („Gespeichert“, „Gesendet“).
- [ ] `SOLLTE` **Rückgängig** bei versehentlichem Löschen.
- [ ] `SOLLTE` **Hinweis auf Neuerungen** nach Updates („Was ist neu“) und Erzwingen eines Updates bei kritischen Fehlern.
- [ ] `KANN` **Suche, Filter und Sortierung,** sobald Nutzer viele Einträge haben.
- [ ] `KANN` **Teilen und Deep Links** zu Inhalten.
- [ ] `KANN` **Bewertungsdialog** zum passenden Zeitpunkt – nur über die offizielle Store-Funktion und ohne Vorfiltern (siehe [13](./13-app-stores-plattformen.md)).

## H. Admin-Bereich

- [ ] `SOLLTE` **Nutzer suchen, sperren und löschen.**
- [ ] `SOLLTE` **Verbrauch und Kosten** je Nutzer und gesamt.
- [ ] `SOLLTE` **Moderation:** gemeldete Inhalte prüfen und bearbeiten.
- [ ] `SOLLTE` **Feature-Flags und Not-Aus für KI.**
- [ ] `SOLLTE` **Auskunfts- und Löschanfragen** bearbeiten.
- [ ] `PFLICHT` **Admin-Zugang geschützt:** serverseitige Rollenprüfung, Mehr-Faktor-Anmeldung, Protokoll aller Admin-Aktionen.

## I. E-Mails und Benachrichtigungen

- [ ] `PFLICHT` **Transaktions-E-Mails:** Konto bestätigen, Passwort zurücksetzen, Kauf, Kündigung, Widerruf.
- [ ] `PFLICHT` **Newsletter nur mit nachweisbarer Einwilligung** (in der Praxis Double-Opt-in) und Abmeldelink.
- [ ] `SOLLTE` **Ein-Klick-Abmeldung im Mail-Header.** Newsletter mit `List-Unsubscribe` und `List-Unsubscribe-Post` senden und die Spam-Beschwerderate unter 0,3 % halten; Gmail verlangt das ab 5.000 Mails pro Tag.
- [ ] `SOLLTE` **Eigene Absender-Domain mit SPF, DKIM und DMARC,** sonst landen Mails im Spam. Große Postfach-Anbieter verlangen das für Massenversender.
- [ ] `SOLLTE` **Push-Benachrichtigungen sparsam** und mit Mehrwert.

## J. Sprache und Region

- [ ] `SOLLTE` **Texte nicht fest im Code,** sondern in Sprachdateien (i18n), auch wenn es zunächst nur Deutsch gibt.
- [ ] `SOLLTE` **Sprachversionen sauber verknüpfen und prüfen.** Jede Sprachversion der Website per `hreflang` (mit `x-default`) verknüpfen und KI-Übersetzungen von Rechtstexten, Preisen und Kaufablauf von einem Menschen prüfen lassen.
- [ ] `SOLLTE` **Datum, Uhrzeit, Zahlen und Währung** nach Region formatieren, Zeitzonen beachten.

## Typische Fehler beim Vibe-Coding

- „Konto löschen“ fehlt – häufigster Grund für Store-Ablehnungen bei Konto-Apps.
- Keine Fehleranzeige, wenn die KI nicht antwortet.
- Rechtstexte nur auf der Landingpage, nicht in der App.
- Admin-Seite unter `/admin` ohne serverseitige Prüfung.
- E-Mails von `noreply@gmail.com` oder ohne DKIM.

## Nachweis

Screen-Inventar mit allen Pflichtfunktionen ([Vorlage](../allgemeine-app-entwicklung/vorlagen/screen-inventar.md)), Testprotokoll für Konto löschen und Export, Screenshots der Rechtsseiten in der App.
