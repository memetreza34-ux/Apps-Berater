# Master-Checkliste – App mit KI von der Idee bis zum langfristigen Erfolg

Diese Checkliste zeigt, ob alle wesentlichen Bereiche berücksichtigt wurden. Ein Haken zählt nur, wenn ein Ergebnis oder Nachweis vorhanden ist.

## 0. Ziel und Voraussetzungen

- [ ] Zweck des Projekts festgelegt
- [ ] Verantwortlicher benannt
- [ ] verfügbare Zeit realistisch geplant
- [ ] Anfangs- und Monatsbudget festgelegt
- [ ] Zielplattformen vorläufig bestimmt
- [ ] Projekt-E-Mail eingerichtet
- [ ] Passwortmanager und Zwei-Faktor-Authentifizierung eingerichtet
- [ ] GitHub-Repository vorhanden
- [ ] Entwicklungs- und Testgeräte geklärt
- [ ] KI-/Coding-Agent ausgewählt

**Nachweis:** App-Steckbrief.

## 1. Problem und Zielgruppe

- [ ] konkretes Problem formuliert
- [ ] enge Zielgruppe definiert
- [ ] heutige Alternative verstanden
- [ ] passende Personen befragt oder beobachtet
- [ ] Häufigkeit und Schwere belegt
- [ ] Gegenargumente dokumentiert
- [ ] Stop-/Go-Kriterien angewendet

**Nachweis:** Research-Protokoll und Problemstatement.

## 2. Markt und Positionierung

- [ ] direkte Wettbewerber geprüft
- [ ] indirekte Lösungen geprüft
- [ ] Preise und Geschäftsmodelle verglichen
- [ ] Bewertungen und häufige Beschwerden analysiert
- [ ] eigener Unterschied klar beschrieben
- [ ] Nutzenversprechen getestet
- [ ] erreichbarer Einstiegsmarkt definiert

**Nachweis:** Wettbewerbs- und Positionierungsdokument.

## 3. Geschäftsmodell und Kosten

- [ ] Geschäftsmodell gewählt
- [ ] Preisannahmen dokumentiert
- [ ] Entwicklungskosten geschätzt
- [ ] laufende Anbieter- und API-Kosten geschätzt
- [ ] Store-, Zahlungs-, Steuer- und Supportkosten berücksichtigt
- [ ] Kosten bei 100, 1.000 und 10.000 aktiven Nutzern modelliert
- [ ] Kostenlimit und Abschaltstrategie geplant
- [ ] wirtschaftliche Stop-Kriterien definiert

**Nachweis:** Kosten- und Umsatzmodell.

## 4. Machbarkeit, Recht und Risiken

- [ ] Kernfunktion technisch geprüft
- [ ] Datenquellen und APIs geklärt
- [ ] Nutzungsrechte an Texten, Bildern, Icons, Sounds und Designs dokumentiert
- [ ] Marken- und Namensrisiken geprüft
- [ ] personenbezogene Daten inventarisiert
- [ ] Drittanbieter und Datenregionen erfasst
- [ ] Medizin-, Finanz-, Kinder-, Biometrie-, Community- und Hardware-Risiken geprüft
- [ ] Store-/Plattformverträglichkeit geprüft
- [ ] Anbieterwechsel oder Exit grundsätzlich möglich
- [ ] notwendige Fachprüfung eingeplant

**Nachweis:** App-Risikoprofil, Rechte- und Anbieterregister.

## 5. Produktplanung

- [ ] Produktvision vorhanden
- [ ] Ziele und Nicht-Ziele festgelegt
- [ ] Nutzerrollen definiert
- [ ] Kernablauf beschrieben
- [ ] Funktionen priorisiert
- [ ] MVP klar vom späteren Ausbau getrennt
- [ ] PRD vollständig
- [ ] Akzeptanzkriterien messbar
- [ ] Roadmap und Release-Stufen vorhanden

**Nachweis:** PRD, MVP-Backlog und Roadmap.

## 6. UX und Inhalte

- [ ] Informationsarchitektur vorhanden
- [ ] Navigation verständlich
- [ ] Kernflows dokumentiert
- [ ] Screen-Inventar vollständig
- [ ] Loading-, Empty-, Error-, Offline- und Success-Zustände geplant
- [ ] Onboarding und Aktivierung geplant
- [ ] Texte und Fehlermeldungen geschrieben
- [ ] Accessibility-Anforderungen definiert
- [ ] Mehrsprachigkeit berücksichtigt
- [ ] Export, Löschung und Support im Flow vorhanden

**Nachweis:** User Flows, Screen-Inventar und Content-Plan.

## 7. Design und Prototyp

- [ ] eigene visuelle Richtung vorhanden
- [ ] Referenzen analysiert statt kopiert
- [ ] Wireframes erstellt
- [ ] semantische Design Tokens definiert
- [ ] Komponenten mit Zuständen dokumentiert
- [ ] wichtigster Screen vollständig gestaltet
- [ ] responsive Größen geprüft
- [ ] Dark Mode und Textskalierung geprüft
- [ ] klickbarer Kernflow vorhanden
- [ ] Usability-Test durchgeführt
- [ ] schwere UX-Probleme behoben
- [ ] Entwickler-/Agenten-Handoff vollständig

**Nachweis:** Designsystem, Prototyp und Usability-Bericht.

## 8. Plattform und Architektur

- [ ] Plattformentscheidung begründet
- [ ] Frontend- und Backend-Aufgaben getrennt verstanden
- [ ] Authentifizierung und Sessionmodell geplant
- [ ] Datenmodell vorhanden
- [ ] Rollen und Berechtigungen dokumentiert
- [ ] Storage und Uploads geplant
- [ ] Offline- und Synchronisationsstrategie geklärt
- [ ] APIs und Drittanbieter dokumentiert
- [ ] KI-Gateway geplant, falls anwendbar
- [ ] Zahlungsarchitektur geplant, falls anwendbar
- [ ] Analytics und Monitoring geplant
- [ ] Backup, Restore und Exit-Plan vorhanden
- [ ] große Entscheidungen als ADR dokumentiert

**Nachweis:** Systemdiagramm, Datenmodell, Berechtigungsmatrix und ADRs.

## 9. Entwicklungsumgebung und KI-Workflow

- [ ] Repository-Struktur verständlich
- [ ] Setup reproduzierbar
- [ ] `.env.example` ohne echte Secrets
- [ ] Dev, Staging und Production getrennt
- [ ] Migrationen versioniert
- [ ] Formatter, Lint und Typecheck eingerichtet
- [ ] Test- und Buildbefehle dokumentiert
- [ ] Branch-, Commit- und Reviewregeln vorhanden
- [ ] Agenten-Masterprompt vorhanden
- [ ] KI liest Produkt-, Design- und Architekturdokumente
- [ ] Änderungen werden klein und prüfbar umgesetzt
- [ ] Migration und Rollback werden mitgedacht
- [ ] Dokumentation wird bei Änderungen aktualisiert

**Nachweis:** Repository-Setup, CI-Konfiguration und Agentenregeln.

## 10. Umsetzung

- [ ] App-Grundgerüst stabil
- [ ] vollständiger vertikaler Kernablauf funktioniert
- [ ] Eingaben serverseitig validiert
- [ ] Autorisierung nicht nur im UI
- [ ] Nutzer A kann Daten von Nutzer B nicht lesen oder ändern
- [ ] ungültige und doppelte Aktionen behandelt
- [ ] abgelaufene Session behandelt
- [ ] Netzwerkfehler und Retry behandelt
- [ ] Zustand bleibt nach Neustart korrekt
- [ ] Datenbankmigrationen sicher
- [ ] Uploadgrenzen und Dateitypen geprüft
- [ ] Suche, Filter und Pagination stabil
- [ ] Fehler verständlich angezeigt
- [ ] Monitoring für Kernfehler vorhanden

**Nachweis:** funktionierende App, Testläufe und technische Dokumentation.

## 11. KI-Funktionen

- [ ] konkreter Nutzen jeder KI-Funktion definiert
- [ ] Modell- und Promptversion dokumentiert
- [ ] Schlüssel nur serverseitig
- [ ] Eingaben und Ausgaben validiert
- [ ] strukturierte Ausgaben genutzt, wo sinnvoll
- [ ] RAG-Berechtigungen vor Retrieval geprüft
- [ ] Prompt-Injection- und Datenexfiltrationstests vorhanden
- [ ] Halluzinationen und fachliche Grenzen berücksichtigt
- [ ] Rate-, Kosten- und Zeitlimits vorhanden
- [ ] Transparenzhinweis vorhanden
- [ ] Fallback und menschliche Eskalation geplant
- [ ] Kill Switch vorhanden
- [ ] Modellwechsel und Rollback testbar

**Nachweis:** KI-Systemregister, Goldenset und Sicherheits-/Kostenbericht.

## 12. Qualität, Security und Datenschutz

- [ ] Unit-Tests für wichtige Logik
- [ ] Integrationstests für Datenflüsse
- [ ] E2E-Test für Kernablauf
- [ ] Tests auf echten Geräten und Browsern
- [ ] Accessibility automatisch und manuell geprüft
- [ ] Threat Model aktuell
- [ ] keine Secrets in Client, Repository oder Logs
- [ ] Admin-MFA vorhanden
- [ ] Rate Limits und Missbrauchsschutz vorhanden
- [ ] Abhängigkeiten und Lizenzen geprüft
- [ ] Dateninventar aktuell
- [ ] Privacy Policy entspricht echter Technik
- [ ] Export und Kontolöschung Ende-zu-Ende getestet
- [ ] Backup und Restore getestet
- [ ] Rollback getestet
- [ ] Performancebudgets eingehalten
- [ ] mindestens ein Alarm mit Runbook getestet

**Nachweis:** vollständiges Evidenzpaket.

## 13. Monetarisierung

- [ ] Preis und Leistungsumfang klar
- [ ] Abo bietet wiederkehrenden Wert
- [ ] Preise in App, Store und Backend identisch
- [ ] Entitlements serverseitig verwaltet
- [ ] Webhooks signiert und idempotent
- [ ] Kauf und Abbruch getestet
- [ ] Verlängerung und fehlgeschlagene Zahlung getestet
- [ ] Grace Period getestet
- [ ] Kündigung getestet
- [ ] Restore getestet
- [ ] Refund und Chargeback berücksichtigt
- [ ] Geräte- und Accountwechsel getestet
- [ ] Kontolöschung mit aktivem Abo verständlich
- [ ] Steuer-, Rechnungs- und Supportweg geklärt

**Nachweis:** Zahlungs-Testbericht und Kostenmodell.

## 14. Veröffentlichungsvorbereitung

- [ ] App-Name final
- [ ] Icon und visuelle Assets final
- [ ] Landingpage online
- [ ] Supportseite online
- [ ] Datenschutzerklärung erreichbar
- [ ] Anbieterinformationen/Impressum geprüft
- [ ] externer Kontolöschweg vorhanden, falls erforderlich
- [ ] Store-Beschreibung final
- [ ] Keywords und Kategorie gewählt
- [ ] Screenshots aktuell
- [ ] Vorschauvideo vorhanden, falls sinnvoll
- [ ] Altersfreigabe korrekt
- [ ] Berechtigungen begründet
- [ ] App Privacy/Data Safety korrekt
- [ ] Review-Konto verfügbar
- [ ] Review Notes vollständig
- [ ] Version und Buildnummer korrekt
- [ ] Signierung und Produktionskonfiguration geprüft
- [ ] Rollout-, Rollback- und Supportplan fertig

**Nachweis:** Release-Dossier und Store-Paket.

## 15. Beta und Release

- [ ] interner Test abgeschlossen
- [ ] geschlossene Beta durchgeführt
- [ ] Feedback priorisiert
- [ ] kritische Fehler geschlossen
- [ ] Release Candidate eingefroren
- [ ] Produktionsmigration auf Staging getestet
- [ ] Backup unmittelbar vor Release geprüft
- [ ] Web-/Store-Einreichung durchgeführt
- [ ] Reviewfragen verantwortlich beantwortet
- [ ] gestaffelter Rollout eingerichtet
- [ ] Kernmetriken während Rollout beobachtet
- [ ] Notfallstopp und Rollback möglich

**Nachweis:** Beta-Bericht und signierte Go-/No-Go-Entscheidung.

## 16. Marketing und Launch

- [ ] klare Zielgruppe und Botschaft
- [ ] Landingpage mit messbarer Hauptaktion
- [ ] Warteliste oder Beta-Community vorhanden
- [ ] Content-Säulen und Redaktionsplan vorhanden
- [ ] Demo und Erklärmaterial erstellt
- [ ] App Store Optimization durchgeführt
- [ ] passende Communities und Partner identifiziert
- [ ] Empfehlungsmechanismus geprüft
- [ ] Launchkalender vorhanden
- [ ] Tracking für Quellen und Conversion eingerichtet
- [ ] Werbebudget und Stop-Kriterien festgelegt
- [ ] Anzeigen zuerst klein getestet
- [ ] Marketingversprechen entsprechen echter Funktion

**Nachweis:** Marketingstrategie, Contentplan und Launchdashboard.

## 17. Nach dem Launch

- [ ] Aktivierung wird gemessen
- [ ] Kernablauf-Erfolg wird gemessen
- [ ] Retention wird gemessen
- [ ] Abbruchstellen sichtbar
- [ ] Crash- und Fehlerquote sichtbar
- [ ] Conversion und Kündigung sichtbar
- [ ] Supportfälle kategorisiert
- [ ] Rezensionen werden beantwortet
- [ ] Nutzerfeedback hat einen festen Prozess
- [ ] Experimente besitzen Hypothese und Erfolgsmetrik
- [ ] Roadmap basiert auf Daten und Produktziel
- [ ] Updates werden verständlich kommuniziert

**Nachweis:** Produktdashboard und Verbesserungsrhythmus.

## 18. Langfristiger Betrieb

- [ ] verantwortliche Person für Betrieb und Vorfälle
- [ ] Kostenwarnungen und harte Limits
- [ ] Abhängigkeiten regelmäßig aktualisiert
- [ ] Security-Patches zeitnah
- [ ] Backups regelmäßig geprüft
- [ ] Restore regelmäßig geübt
- [ ] Zugriffsrechte regelmäßig geprüft
- [ ] Anbieter und Verträge überprüft
- [ ] Store- und Datenschutzangaben aktuell
- [ ] Geräte- und Betriebssystemsupport definiert
- [ ] Support-Wissensbasis gepflegt
- [ ] monatliche, quartalsweise und jährliche Prüfung terminiert
- [ ] End-of-Life-Kriterien festgelegt

**Nachweis:** Betriebshandbuch und Wartungskalender.

## 19. Skalierung oder Produktende

- [ ] Produkt-Markt-Fit anhand Daten bewertet
- [ ] Skalierung durch Bedarf statt Vermutung begründet
- [ ] Architekturengpässe gemessen
- [ ] Teamrollen und Verantwortungen definiert
- [ ] Internationalisierung vollständig geplant
- [ ] Partnerschaften und B2B geprüft
- [ ] Anbieterwechsel und Datenmigration vorbereitet
- [ ] Finanzierung, Lizenzierung oder Verkauf dokumentierbar
- [ ] Produktende mit Export, Kommunikation und Löschung möglich

**Nachweis:** Skalierungs-, Exit- oder End-of-Life-Plan.

# Endgültige Release-Regel

Kein öffentlicher Release bei:

- fremdem Datenzugriff;
- möglichem Datenverlust ohne getesteten Restore;
- Secrets im Client oder Repository;
- manipulierbarer Abrechnung;
- fehlender erforderlicher Löschung;
- kritischem Fehler im Kernablauf;
- falschen Store- oder Datenschutzangaben;
- ungeklärter Hochrisiko-/Zulassungsfrage;
- fehlendem verantwortlichen Betreiber;
- Marketingversprechen, die die App nicht erfüllt.
