# Vollständigkeitsstandard – woran sich die gesamte App-Master-Anleitung messen lassen muss

Diese Datei ist der verbindliche Umfang des Handbuchs. Sie verhindert, dass nur Programmierung erklärt wird und wichtige Bereiche wie Rechte, Normen, Daten, Veröffentlichung, Marketing oder Betrieb fehlen.

## Ziel

Das Handbuch soll eine Person durch den vollständigen Lebenszyklus einer App führen:

```text
Voraussetzungen
→ Idee und Problem
→ Markt und Geschäftsmodell
→ Rechte und Machbarkeit
→ Produktstruktur und Funktionen
→ UX/UI und Inhalte
→ Architektur und Daten
→ Entwicklung mit KI
→ Tests und Produktionsreife
→ Veröffentlichung
→ Marketing und Nutzergewinnung
→ Betrieb, Updates und Support
→ Skalierung, Verkauf oder Produktende
```

Es soll als Orientierungs- und Kontrollsystem funktionieren. Für jede konkrete App muss erkennbar sein:

- was benötigt wird;
- welche Entscheidungen getroffen werden müssen;
- welche Unterlagen entstehen;
- welche Regeln gelten können;
- welche Funktionen und Datenflüsse geplant werden müssen;
- was KI übernehmen darf;
- was ein Mensch prüfen und freigeben muss;
- welche Nachweise vor dem nächsten Schritt vorliegen müssen.

## 1. Orientierung und Voraussetzungen

Das Handbuch behandelt mindestens:

- App-Arten: Web-App, PWA, iOS, Android, Desktop, Embedded/IoT, Plattform, SaaS;
- lokale, Cloud- und hybride Apps;
- Einzelentwickler, Team, Agentur und Unternehmen;
- benötigte Geräte und Testgeräte;
- Entwicklungsrechner, Betriebssysteme und Browser;
- GitHub, lokale Entwicklungsumgebung und Versionsverwaltung;
- Apple-, Google-, Hosting-, Domain-, E-Mail-, Datenbank- und Zahlungsanbieter-Konten;
- KI-Modelle, Coding-Agenten und Designwerkzeuge;
- monatliche und einmalige Kosten;
- notwendige Kenntnisse und externe Fachpersonen;
- Schnellweg, Standardweg und Hochrisikoweg.

## 2. Idee, Nutzer, Markt und Geschäft

Pflichtinhalte:

- persönliche Ziele, Zeit und Budget;
- Problemstatement und Zielgruppe;
- Nutzerinterviews und Problembelege;
- direkte und indirekte Alternativen;
- Wettbewerbsanalyse;
- Marktgröße nur dort, wo sie für eine Entscheidung nötig ist;
- Positionierung und Nutzenversprechen;
- Geschäftsmodelle: kostenlos, Kauf, Abo, Credits, Werbung, Provision, B2B, Lizenz;
- Kostenmodell bei verschiedenen Nutzerzahlen;
- Preisfindung und Profitabilität;
- Erfolgsmetriken, Kill-Kriterien und Stop-/Go-Entscheidung.

## 3. Recht, Rechte, Regeln und Normen

Das Handbuch muss zwischen vier Ebenen unterscheiden:

1. **Gesetze und Verordnungen** – verbindlich, abhängig von Land, Markt, App-Art und Funktion.
2. **Plattform- und Store-Regeln** – vertragliche Bedingungen für Apple, Google, Webhosting, Zahlungs- und KI-Anbieter.
3. **Normen und Sicherheitsstandards** – teilweise freiwillig, teilweise durch Vertrag, Branche oder Gesetz relevant.
4. **Eigene Produktregeln und Verträge** – Nutzungsbedingungen, Community-Regeln, Lizenzen, Auftragsverarbeitung und Anbietervereinbarungen.

Mindestens zu prüfen:

- Datenschutz, Rechtsgrundlagen, Datenminimierung und Betroffenenrechte;
- Cookies, Tracking, Gerätezugriff und Einwilligung;
- Impressum, Anbieterinformationen und kommerzielle Kommunikation;
- Verbraucherinformationen, Preise, Verlängerung, Kündigung und Widerruf;
- Digitale-Dienste- und Plattformpflichten;
- KI-Transparenz, Risikoklassen und menschliche Aufsicht;
- Cybersicherheits- und Updatepflichten;
- Barrierefreiheit;
- Urheberrecht, Markenrecht, Designschutz und Datenbankrechte;
- Open-Source-, Font-, Icon-, Bild-, Musik-, Video- und Datensatzlizenzen;
- Rechte an KI-Eingaben und KI-Ausgaben;
- Minderjährige und Altersgruppen;
- Community, Nutzerinhalte, Moderation, Meldung und Sperrung;
- Gesundheit, Medizin, Finanzen, Versicherungen, Kredit, Steuer und Recht;
- Biometrie, Standort, Kontakte, Kamera, Mikrofon und besondere Daten;
- Hardware, IoT, Bluetooth, Fahrzeuge und physische Risiken;
- Werbung, Influencer-Marketing, Empfehlungen und Gewinnspiele;
- internationale Veröffentlichung, Datenübertragung und Lokalisierung;
- Aufbewahrung, Export, Löschung, Backup und Produktende.

Jede rechtliche oder normative Aussage erhält:

```text
Quellen-ID
Titel
Typ: Gesetz / Store-Regel / Norm / Vertrag / Empfehlung
Land oder Markt
betroffene App-Arten und Funktionen
verbindlich oder Orientierung
aktuelle Version
letztes Prüfdatum
nächstes Prüfdatum
verantwortliche Person
Auswirkung auf Produkt, Technik und Betrieb
Nachweis der Umsetzung
```

## 4. Produktaufbau und Funktionsstruktur

Das Handbuch erklärt nicht nur eine Funktionsliste, sondern den vollständigen Produktaufbau:

- Produktvision, Ziele und Nicht-Ziele;
- Nutzerrollen und Rechte;
- Kernablauf und Nebenabläufe;
- MVP, spätere Releases und bewusst ausgeschlossene Funktionen;
- Funktionsbaum und Modulstruktur;
- Navigation und Informationsarchitektur;
- Screen-Inventar;
- Abhängigkeiten zwischen Funktionen;
- Fehler-, Lade-, Leer-, Erfolg- und Offlinezustände;
- Onboarding, Aktivierung und Wiederkehr;
- Suche, Filter, Sortierung und Pagination;
- Erstellen, Lesen, Ändern, Löschen, Archivieren und Wiederherstellen;
- Uploads, Medien, Benachrichtigungen und Hintergrundaufgaben;
- Einstellungen, Support, Export und Kontolöschung;
- Admin-, Moderations- und Supportbereich;
- Analytics- und Experimentfunktionen;
- Abrechnung, Abos und Berechtigungen;
- KI-Funktionen, RAG, Agenten und menschliche Eskalation.

Für jede Funktion entsteht ein **Funktionsdossier**:

```text
Name und Zweck
Nutzerrolle
Auslöser
Vorbedingungen
Normalablauf
Grenz- und Fehlerfälle
Daten und Berechtigungen
UI-Zustände
Offline-/Retry-Verhalten
Security- und Datenschutzrisiken
Analytics
Kosten
Akzeptanzkriterien
Tests
Rollback oder Abschaltung
verantwortliche Person
```

## 5. UX, UI, Inhalte und Marke

Pflichtumfang:

- Informationsarchitektur und Navigation;
- User Flows;
- Wireframes und Prototyp;
- Designreferenzen ohne Kopieren geschützter Gestaltung;
- Design Tokens;
- Komponenten und Varianten;
- Responsive und adaptive Darstellung;
- Light/Dark Mode;
- Textskalierung, Kontrast, Fokus, Screenreader und Tastatur;
- Touch-Ziele, Gestenalternativen und Reduced Motion;
- Formulare, Validierung und Fehlermeldungen;
- Mikrocopy, Sprache und Ton;
- Mehrsprachigkeit, Übersetzung und Lokalisierung;
- reale Inhalte und lange Texte;
- Icon, Logo, Bilder, Illustrationen und Animationen;
- Developer Handoff und Screenshotvergleich;
- Usability-Tests und Designfreigabe.

## 6. Systemaufbau und Architektur

Das Handbuch erklärt die Zusammenhänge zwischen:

- Client und Benutzeroberfläche;
- Frontend-Logik;
- Backend und API;
- Datenbank;
- Authentifizierung und Autorisierung;
- Datei- und Medienspeicher;
- Suchsystem;
- Realtime und Synchronisation;
- Queue, Jobs und Hintergrundverarbeitung;
- E-Mail, Push und SMS;
- Zahlungsanbieter und Store-Käufe;
- KI-Gateway und Modellanbieter;
- Analytics, Logs, Metriken und Traces;
- Admin- und Supportsystem;
- Backup, Restore und Disaster Recovery;
- Dev, Staging und Production.

Zu jeder Architekturentscheidung gehören Kontext, Alternativen, Entscheidung, Folgen, Kosten, Risiken, Migration, Exit-Plan und Prüfdatum.

## 7. Daten – vollständig von Entstehung bis Löschung

Pflichtinhalte:

- Datenobjekte, Tabellen, Felder und Beziehungen;
- Primär- und Fremdschlüssel;
- Constraints, Indizes und Versionen;
- Nutzer-, Organisations- und Mandantenzuordnung;
- Rollen- und Berechtigungsmatrix;
- Datenentstehung und Datenquellen;
- Datenflussdiagramme;
- Datenvalidierung;
- lokale Speicherung und sichere Gerätespeicherung;
- Server- und Drittanbieterspeicherung;
- Realtime und Synchronisation;
- Konfliktlösung;
- Offline-Verhalten;
- Import, Export und Portabilität;
- Aufbewahrungsfristen;
- Löschung, Anonymisierung und Sperrung;
- Backups und Löschung aus Sicherungen;
- Datenmigration und Anbieterwechsel;
- Protokolle und Auditdaten;
- Analytics- und Marketingdaten;
- KI-Prompts, Antworten, Embeddings und Vektordaten;
- Testdaten und Produktionsdaten;
- sensible und besondere Daten;
- Datenqualität, Herkunft und Aktualität.

## 8. Entwicklung mit KI

Das Handbuch zeigt:

- wie Anforderungen für KI verständlich geschrieben werden;
- wie Repository-Kontext aufgebaut wird;
- wie Claude Code, Codex oder andere Agenten zuerst analysieren und planen;
- wie Aufgaben in kleine vertikale Schritte zerlegt werden;
- wie bestehende Architektur und Designsysteme geschützt werden;
- wie Codeänderungen, Migrationen und Abhängigkeiten geprüft werden;
- wie Prompts, Regeln und Entscheidungsdateien versioniert werden;
- wie Halluzinationen, erfundene APIs und Fake-Erfolge erkannt werden;
- wie Agenten Tests, Screenshots und Dokumentation liefern müssen;
- welche Entscheidungen nicht an KI delegiert werden dürfen;
- wie mehrere Agenten oder Review-Rollen kontrolliert eingesetzt werden;
- wie Modellwechsel, Kosten und Anbieterabhängigkeit behandelt werden.

## 9. Qualität, Tests und Normen

Mindestens:

- funktionale Anforderungen und Akzeptanzkriterien;
- Unit-, Integrations-, Contract- und E2E-Tests;
- manuelle explorative Tests;
- Browser-, Geräte- und Betriebssystemmatrix;
- Accessibility-Tests;
- Security- und Missbrauchstests;
- Auth-, Rollen- und Zwei-Nutzer-Negativtests;
- Performance, Speicher, Akku und Netz;
- große Datenmengen und Last;
- Offline, Retry, Doppelaktionen und Idempotenz;
- Migration, Backup, Restore und Rollback;
- Zahlungs- und Abozustände;
- KI-Evaluation, Prompt Injection und Datenexfiltration;
- Datenschutz-, Lösch- und Exporttests;
- Release Candidate und Definition of Done;
- unabhängige zweite Prüfung bei kritischen Bereichen.

## 10. Veröffentlichung

Das Handbuch muss den vollständigen Weg erklären für:

- Domain, DNS, Hosting und HTTPS;
- Web-App und PWA;
- Apple Developer, Signierung, Provisioning, TestFlight und App Store;
- Google Play Console, App Signing, Testtracks und Veröffentlichung;
- Desktop- und alternative Stores, soweit relevant;
- App-Name, Bundle-/Package-ID und Versionierung;
- App-Icon, Screenshots, Vorschauvideo und Store-Texte;
- Keywords und App Store Optimization;
- Altersfreigabe, Zielgruppe und Berechtigungen;
- Datenschutz- und Datenangaben;
- Kauf- und Aboinformationen;
- Review-Konto und Review Notes;
- Support-, Datenschutz- und Lösch-URLs;
- Beta, Release Candidate und gestaffelter Rollout;
- Monitoring, Support und Rollback am Veröffentlichungstag.

## 11. Marketing und Nutzergewinnung

Marketing ist ein gleichwertiger Hauptteil, kein kurzer Anhang:

- Positionierung und Botschaft;
- Name, Marke und Landingpage;
- Pre-Launch-Warteliste;
- Zielgruppenkanäle;
- Contentstrategie;
- Social Media;
- Demo, Erklärvideo und Screenshots;
- ASO und Web-SEO;
- Communities und Partnerschaften;
- Influencer und Creator;
- Presse und Verzeichnisse;
- Empfehlungs- und Einladungssysteme;
- E-Mail und Lifecycle-Kommunikation;
- bezahlte Werbung und Testbudgets;
- Launchkalender;
- Conversion, CAC und Payback;
- Bewertungen und Rezensionen;
- Retention, Reaktivierung und Churn;
- rechtliche Regeln für Werbung und kommerzielle Kommunikation.

## 12. Betrieb über Jahre

Pflichtumfang:

- Verantwortlichkeiten und Kontaktwege;
- Monitoring, Alarme und Runbooks;
- Support, Tickets und Wissensdatenbank;
- Statusseite und Vorfallkommunikation;
- Kosten, Quoten und Limits;
- Abhängigkeiten, Frameworks und Plattformversionen;
- Security-Patches und Schwachstellenprozess;
- Backups und regelmäßige Restore-Übungen;
- Store- und Rechtsänderungen;
- Datenschutz- und Anbieterprüfung;
- neue Geräte und Betriebssysteme;
- Produktmetriken und Nutzerfeedback;
- Roadmap und technische Schulden;
- Internationalisierung und neue Märkte;
- Team, Zugriffsrechte und Übergaben;
- Finanzierung, Verkauf oder Lizenzierung;
- Anbieterwechsel, Datenmigration und Exit;
- Produktende, Datenexport, Löschung und Kommunikation.

## 13. Langfristige Nutzbarkeit über 15 Jahre

Zeitlose Grundlagen und aktuelle Details werden getrennt:

```text
Grundprinzip – bleibt langfristig
aktuelle Umsetzung – wird versioniert
Quelle und Prüfdatum – zeigt den Stand
Migrationshinweis – erklärt den Wechsel
```

Keine Anleitung darf dauerhaft von einem einzelnen Anbieter oder Modell abhängen. Bei jedem Werkzeug wird erklärt:

- welche Aufgabe es erfüllt;
- welche Mindestfähigkeiten ein Ersatz braucht;
- welche Daten und Formate exportierbar sein müssen;
- wie ein Anbieterwechsel erfolgt;
- wann der Abschnitt erneut geprüft werden muss.

## 14. Fertig-Kriterium des gesamten Handbuchs

Das Handbuch ist erst fertig, wenn:

- alle oben genannten Bereiche in eigenen Kapiteln erklärt sind;
- ein Anfänger die Fachbegriffe und Zusammenhänge versteht;
- jeder Schritt Ziel, Voraussetzungen, Ablauf, KI-Aufgabe, menschliche Entscheidung, Ergebnis und Gate enthält;
- alle Phasen ausfüllbare Vorlagen besitzen;
- mindestens drei vollständige Beispielprojekte den gesamten Weg durchlaufen;
- Recht, Regeln und Normen in einem versionierten Register stehen;
- Funktionen, System und Daten in nachvollziehbaren Musterdokumenten gezeigt werden;
- Entwicklung, Veröffentlichung, Marketing und Betrieb gleichwertig behandelt werden;
- interne Links, Beispiele und Prüfskripte funktionieren;
- zeitabhängige Inhalte Quellen und Prüfdaten besitzen;
- eine unabhängige zweite Prüfung offene Lücken dokumentiert;
- eine lesbare PDF-/DOCX-Ausgabe aus der Repository-Version erzeugt wurde.

Bis diese Punkte erfüllt und nachgewiesen sind, wird keine feste 9,x-Endbewertung vergeben.
