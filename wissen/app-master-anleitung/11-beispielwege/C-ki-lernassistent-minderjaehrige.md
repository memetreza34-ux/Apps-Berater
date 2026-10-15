# Beispiel C – KI-Lernassistent für Minderjährige

## 1. Ausgangslage

Eine App erklärt Lerninhalte, erstellt Übungsfragen und beantwortet Fragen anhand geprüfter Quellen. Ein Teil der Zielgruppe ist minderjährig. Die App verwendet Konten, KI, RAG, Nutzereingaben und optional ein Abonnement oder Schullizenzen.

## 2. Warum Hochrisikoweg?

Nicht automatisch ein gesetzlich definiertes Hochrisiko-System, aber ein Produkt mit erhöhtem Schadens- und Schutzpotenzial wegen:

- Minderjährigen;
- KI-Ausgaben;
- möglicher falscher Bildungsaussagen;
- personenbezogenen Lernprofilen;
- Interaktions-/Engagementdesign;
- Inhalten und Moderation;
- Eltern-/Schulrollen;
- potenziellen automatisierten Empfehlungen;
- Abos und Werbung;
- mehreren Ländern/Schulsystemen.

Vor Umsetzung des Kernprodukts ist eine fachliche, Datenschutz-, Jugend- und KI-Anwendbarkeitsprüfung erforderlich.

## 3. Problem und Zielgruppe

### Problemstatement

Lernende verstehen einzelne Themen nicht, erhalten aber außerhalb von Unterricht oder Nachhilfe keine sofortige, verständliche und quellenbasierte Erklärung. Allgemeine Chatbots können falsche oder ungeeignete Antworten liefern.

### Segmente

- Lernende nach Alters-/Klassenstufe;
- Eltern;
- Lehrkräfte/Schulen;
- Moderation/Content-Team;
- Support/Admin.

Die Zielaltersgruppe muss präzise festgelegt werden. „Alle Schüler“ ist zu breit.

## 4. Produktgrenzen

Im MVP:

- begrenztes Fach/Themengebiet;
- geprüfte Quellen;
- Erklärungen und Übungsfragen;
- keine Notenentscheidung;
- keine Diagnose von Lernstörungen;
- keine psychologische/medizinische Beratung;
- keine offene Community;
- keine automatische Sanktion oder Schulentscheidung.

## 5. Evidenz

- Interviews mit Lernenden in geeigneter, erlaubter Form;
- Eltern/Lehrkräfte;
- beobachtete Lernprobleme;
- fachliche Inhaltsprüfung;
- beaufsichtigter Prototyptest;
- dokumentierte Einwilligungs-/Teilnahmeprozesse;
- Pilot mit klaren Sicherheitsregeln.

## 6. Recht, Regeln und Normen

Projektbezogen prüfen:

- Betreiber und aktive Märkte;
- Altersgrenzen und Einwilligungsanforderungen;
- Datenschutz und besondere Schutzbedürfnisse;
- Profiling/automatisierte Entscheidungen;
- AI-Act-Einordnung;
- Transparenz gegenüber Lernenden/Eltern;
- Jugendschutz und Inhalte;
- Werbung/Tracking bei Minderjährigen;
- Verbraucherrecht/Abos;
- Urheber-/Datenbankrechte an Lernmaterial;
- Schul-/B2B-Verträge;
- Accessibility;
- Store-Zielgruppe und Datenangaben;
- Moderation/Meldewege;
- fachliche Qualität und Haftungsrisiken.

Externe Prüfer dokumentieren Scope, Entscheidung, Kontrollen und Restrisiko.

## 7. Rollen

| Rolle | Hauptrechte |
|---|---|
| Lernender | eigene Fragen, Lernfortschritt, sichere Einstellungen |
| Elternteil | je nach Modell zulässige Übersicht/Verwaltung |
| Lehrkraft | zugewiesene Inhalte/Gruppen, keine unnötigen privaten Chats |
| Content-Reviewer | Quellen und fachliche Inhalte freigeben |
| Moderator/Safety | Meldungen und Sicherheitsfälle |
| Support | minimaler protokollierter Zugriff |
| Admin | Betrieb, Rollen, Kill Switch |

Keine Rolle darf mehr Daten sehen, als für ihren Zweck erforderlich.

## 8. Kernablauf

```text
Thema auswählen
→ Frage stellen
→ Eingabe prüfen
→ Berechtigung/Kostenlimit
→ relevante freigegebene Quellen abrufen
→ Modell erzeugt strukturierte Antwort
→ Quellen/Unsicherheit anzeigen
→ Lernender bewertet Verständnis
→ optional Übung
```

Bei Unsicherheit:

```text
keine sichere Antwort
→ transparent begrenzen
→ passende Quelle/Lehrkraft/Support empfehlen
```

## 9. Datenmodell

Mögliche Objekte:

```text
users
profiles
parent_links
school_tenants
courses
topics
approved_sources
source_versions
conversations
messages
learning_events
quiz_attempts
ai_runs
safety_events
consents
subscriptions
audit_events
```

Datenminimierung:

- keine unnötigen Klarnamen;
- keine freien sensiblen Profile ohne Bedarf;
- Rohprompts nur wenn notwendig und mit Aufbewahrung;
- Embeddings/Lernprofile in Löschung und Export einbeziehen;
- getrennte Mandanten bei Schulen.

## 10. KI-/RAG-Architektur

```text
Client
→ Auth und Alters-/Rollenlogik
→ KI-Gateway
→ Input- und Safety-Prüfung
→ Rate-/Kostenlimit
→ berechtigungsgefiltertes Retrieval
→ Modell mit versionierter Anweisung
→ strukturiertes Schema
→ Quellen-/Unsicherheitsprüfung
→ Antwort oder sichere Begrenzung
→ Monitoring/Evaluation
```

## 11. Quellenprozess

Für jede Quelle:

- Eigentümer/Lizenz;
- Fachgebiet;
- Alters-/Klassenstufe;
- Version;
- Gültigkeit;
- Reviewer;
- Freigabedatum;
- Chunking/Metadaten;
- Löschung/Ersetzung;
- Zitat-/Anzeigeanforderung.

RAG darf keine unfreigegebenen oder fremden Mandanteninhalte abrufen.

## 12. KI-Evaluation

Goldenset nach Thema und Altersstufe:

- richtige Standardfälle;
- typische Missverständnisse;
- mehrdeutige Frage;
- fehlende Quelle;
- widersprüchliche Quellen;
- falsche Behauptung des Nutzers;
- Prompt Injection;
- Versuch, System-/Quellinhalte auszulesen;
- unangemessene Inhalte;
- persönliche Krisen-/Gefahrensituation;
- hohe Kosten/Latenz;
- Modellwechsel.

Bewertung durch geeignete Fachpersonen und Safety-/Produktreview.

## 13. UX für Minderjährige

- altersgerechte Sprache;
- keine manipulativen Streaks/Kaufdruck;
- sichere Standardwerte;
- klare KI-Kennzeichnung;
- Quellen und Unsicherheit;
- einfache Meldung;
- Blockieren/Beenden;
- keine unnötigen öffentlichen Profile;
- verständliche Datenschutzinformationen;
- Eltern-/Lehrkraftfunktionen ohne unverhältnismäßige Überwachung;
- Accessibility.

## 14. Monetarisierung

Mögliche Wege:

- Schullizenz;
- Eltern-Abo;
- begrenzter kostenloser Zugang;
- keine personalisierte Werbung als Standard;
- klare Kostenlimits für KI.

Prüfen:

- Wer ist Vertragspartner?
- Wer stimmt Kauf zu?
- Wie funktioniert Kündigung/Refund?
- Welche Lerninhalte bleiben nach Ablauf?
- Wie werden Schul-/Privatkonten getrennt?
- Gibt es faire kostenlose Alternativen?

## 15. Entwicklung mit KI-Agenten

Agenten dürfen:

- UI/Backend nach freigegebenem PRD umsetzen;
- Tests und Schemas vorbereiten;
- Quellenpipeline entwickeln;
- Evaluation automatisieren;
- Sicherheitsfälle ergänzen.

Agenten dürfen nicht:

- fachliche Inhalte selbst freigeben;
- Alters-/Rechtsentscheidung erfinden;
- Moderations-/Krisenregeln ohne Fachprüfung festlegen;
- Datenumfang erweitern;
- Modellwechsel ohne Regressionstest ausrollen.

## 16. Teststrategie

### Produkt

- versteht Lernender die Erklärung?
- verbessert Übung das Ziel?
- werden Quellen verstanden?
- erkennt Nutzer Unsicherheit?

### Fachlich

- Richtigkeit;
- Vollständigkeit;
- Altersangemessenheit;
- Quellenbezug;
- keine erfundenen Belege.

### Safety

- Selbstgefährdung/Krisenfälle entsprechend Scope;
- Belästigung/sexuelle Inhalte;
- Manipulation;
- Prompt Injection;
- Datenexfiltration;
- Umgehung von Alters-/Rollenregeln;
- unangemessene Kaufanreize.

### Datenschutz/Security

- Mandantentrennung;
- Eltern-/Lehrkraftrechte;
- Export/Löschung;
- Embeddings/AI-Logs;
- Consent/Widerruf;
- Adminzugriff;
- Rate Limits.

## 17. Pilot

Kein sofortiger öffentlicher Massenlaunch.

```text
interner Test
→ fachlicher Test
→ beaufsichtigter kleiner Pilot
→ Eltern/Lehrkräfte/Lernende Feedback
→ Safety-/Datenschutzreview
→ begrenzte Beta
→ gestaffelter Release
```

Klare Stopkriterien:

- gefährliche falsche Antworten;
- unklare Daten-/Alterslage;
- fremder Datenzugriff;
- fehlende Moderation/Eskalation;
- nicht tragfähige KI-Kosten;
- manipulative UX;
- ungeklärte Lizenzrechte.

## 18. Veröffentlichung

Zusätzlich zum normalen Release-Dossier:

- Zielalters- und Marktentscheidung;
- fachliche Freigabe;
- KI-Systemregister;
- Quellenregister;
- Safety- und Moderationshandbuch;
- Eltern-/Schulinformationen;
- Datenschutz-/Consent-Flows;
- Store-Zielgruppe/Datenangaben;
- Krisen-/Meldewege;
- Modell-/Prompt-Kill-Switch;
- Pilotnachweise.

## 19. Marketing

Keine unbelegten Aussagen wie:

- garantiert bessere Noten;
- ersetzt Lehrkräfte;
- immer richtige Antworten;
- vollständig sicher.

Bessere Kommunikation:

- klarer begrenzter Fachbereich;
- geprüfte Quellen;
- Lernhilfe, nicht Entscheidungssystem;
- transparente Grenzen;
- Schutz- und Kontrollprozesse;
- Pilot-/Testnachweise.

Kanäle:

- Schulen/Lehrkräfte;
- Elterncommunities;
- Bildungsorganisationen;
- fachliche Partnerschaften;
- erklärende Inhalte;
- beaufsichtigte Demos.

## 20. Betrieb

- tägliche Safety-/Fehler-/Kostenkontrolle;
- fachliche Inhaltskorrekturen;
- Meldungen/Eskalationen;
- Modell-/Promptversionen;
- Lösch-/Exportjobs;
- Support;
- regelmäßige Evaluation;
- Quellenaktualisierung;
- Recht-/Store-/Altersprüfung;
- Incident-Übungen;
- externe Reviewtermine.

## 21. Fertignachweise

- Problem-/Zielgruppenbelege;
- externe Anwendbarkeitsentscheidungen;
- PRD/MVP;
- Rollen-/Daten-/Consentmodell;
- Quellen- und KI-Systemregister;
- fachliches Goldenset;
- Safety-/Injection-/RAG-Rechtetests;
- Usability/Accessibility mit Zielgruppe;
- Pilotbericht;
- Export/Löschung;
- Kosten-/Monetarisierungsplan;
- Release-/Marketing-/Betriebspaket;
- benannte Verantwortliche und Kill Switch.
