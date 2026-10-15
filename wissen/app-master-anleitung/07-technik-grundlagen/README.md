# Technische Grundlagen für Anfänger

Dieses Kapitel erklärt die wichtigsten Bausteine einer App ohne vorausgesetzte Entwicklerausbildung. Es ersetzt keine vollständige Programmierausbildung, schafft aber das Verständnis, das für Entscheidungen und die Kontrolle von KI-Agenten notwendig ist.

## 1. Was ist eine App technisch?

Eine App besteht meist aus mehreren Schichten:

```text
Benutzeroberfläche
→ Anwendungslogik
→ Backend/API
→ Datenbank und Storage
→ externe Dienste
→ Monitoring und Betrieb
```

Nicht jede App benötigt jede Schicht. Eine Offline-App kann vollständig lokal funktionieren. Eine Plattform mit Konten, Teams und Zahlungen benötigt dagegen meist Backend, Datenbank, Auth und mehrere Anbieter.

## 2. Frontend

Das Frontend ist der Teil, den Nutzer sehen und bedienen.

Es umfasst:

- Screens und Navigation;
- Formulare;
- Zustände;
- lokale Logik;
- Darstellung von Daten;
- Accessibility;
- Geräte- und Plattformintegration.

Frontend-Code ist nicht vertrauenswürdig für Sicherheitsentscheidungen. Nutzer können Clients verändern oder Requests direkt senden.

## 3. Backend

Das Backend läuft in einer kontrollierten Serverumgebung.

Typische Aufgaben:

- Authentifizierung prüfen;
- Autorisierung durchsetzen;
- Geschäftsregeln;
- Datenbankzugriffe;
- Zahlungen und Webhooks;
- E-Mail/Push;
- KI-Gateway;
- Jobs und Automationen;
- Audit und Monitoring.

Geheime Schlüssel gehören in das Backend oder eine gleichwertig geschützte Umgebung.

## 4. API

Eine API ist eine definierte Schnittstelle zwischen Systemen.

Ein Request enthält typischerweise:

- Methode, etwa GET/POST/PATCH/DELETE;
- URL oder Funktion;
- Authentifizierung;
- Eingabedaten;
- optionale Idempotenzkennung.

Eine Response enthält:

- Status;
- Daten;
- strukturierten Fehler;
- eventuell Pagination oder Metadaten.

APIs benötigen:

- Versionierung;
- Eingabevalidierung;
- Autorisierung;
- Rate Limits;
- Fehlervertrag;
- Dokumentation;
- Monitoring.

## 5. Datenbank

Eine Datenbank speichert strukturierte Daten.

Wichtige Begriffe:

- Tabelle/Collection;
- Zeile/Dokument;
- Spalte/Feld;
- Primärschlüssel;
- Fremdschlüssel;
- Constraint;
- Index;
- Transaktion;
- Migration;
- Abfrage.

Ein gutes Datenmodell beschreibt Beziehungen und Regeln, nicht nur Felder.

Beispiel:

```text
users
projects
project_members
sessions
subscriptions
```

## 6. Storage

Storage speichert Dateien wie Bilder, Audio, PDFs oder Videos.

Zu planen:

- public oder private;
- Dateitypen;
- maximale Größe;
- Uploadrechte;
- Malware-/Inhaltsprüfung;
- Varianten/Thumbnails;
- Zugriffstokens;
- Aufbewahrung;
- Export und Löschung;
- Kosten und Datentransfer.

## 7. Authentifizierung und Autorisierung

### Authentifizierung

Wer ist die Person oder das System?

Beispiele:

- E-Mail/Passwort;
- Passkey;
- OAuth;
- Magic Link;
- Unternehmens-SSO.

### Autorisierung

Was darf diese Identität tun?

Beispiele:

- eigene Aufgabe lesen;
- Teamprojekt bearbeiten;
- Nutzer moderieren;
- Abo verwalten;
- Adminfunktion ausführen.

Ein gültiger Login bedeutet nicht automatisch Berechtigung für alle Daten.

## 8. Session und Token

Nach Login erhält ein Client meist eine Session oder Tokens.

Zu prüfen:

- Ablauf;
- Erneuerung;
- sichere Speicherung;
- Abmeldung;
- Geräteverlust;
- widerrufene Konten;
- Rollenänderung;
- Schutz vor Weitergabe.

## 9. Migrationen

Eine Migration ist eine versionierte Änderung am Datenmodell.

Regeln:

- keine dauerhafte manuelle Änderung ohne Migration;
- zuerst Development, dann Staging, dann Production;
- Backup/Recovery beachten;
- Breaking Changes schrittweise;
- Backfill getrennt planen;
- Roll-forward oder Rollback dokumentieren.

## 10. Hosting und Deployment

Hosting stellt App oder Backend bereit.

Deployment bedeutet, eine bestimmte Version in eine Umgebung zu bringen.

Umgebungen:

```text
Development
Staging
Production
```

Sie benötigen getrennte Daten, Schlüssel, URLs und Anbieterziele.

## 11. Domain, DNS und HTTPS

- Domain: lesbarer Name;
- DNS: verbindet Domain mit Diensten;
- HTTPS/TLS: verschlüsselt die Verbindung;
- Zertifikat: bestätigt Domain und ermöglicht TLS.

Zusätzlich relevant:

- Subdomains;
- E-Mail-DNS;
- Redirects;
- HSTS/Security Headers;
- Domainverlängerung und Eigentum.

## 12. Web-App und PWA

Eine Web-App läuft im Browser.

Eine PWA kann zusätzlich bieten:

- Installierbarkeit;
- Manifest;
- Service Worker;
- Offline-App-Shell;
- Web-Push, abhängig von Plattform;
- Caching.

Grenzen gegenüber nativen Apps hängen von Plattform und benötigten Gerätefunktionen ab.

## 13. Mobile App

Mobile Apps werden für iOS und/oder Android gebaut.

Möglichkeiten:

- native Entwicklung;
- Cross-Platform;
- WebView/Hybrid;
- PWA.

Zu prüfen:

- Signierung;
- App-ID/Bundle-ID;
- Berechtigungen;
- Store-Regeln;
- Betriebssystemversionen;
- Gerätefunktionen;
- Hintergrundarbeit;
- Deep Links;
- Push;
- Offline und lokale Speicherung.

## 14. Native und Cross-Platform

### Native

Direkter Zugriff auf Plattformfunktionen und höchste Plattformspezialisierung, aber meist getrennte Codebasen.

### Cross-Platform

Gemeinsame Codebasis für mehrere Plattformen, aber native Integrationen und Plattformunterschiede bleiben.

Auswahl nach Anforderungen, Team, Budget, Gerätefunktionen und langfristigem Betrieb.

## 15. Offline und Synchronisation

Offline-Unterstützung ist mehr als Caching.

Zu entscheiden:

- Welche Aktionen funktionieren offline?
- Wo werden lokale Daten gespeichert?
- Wann wird synchronisiert?
- Was passiert bei Konflikten?
- Wie werden doppelte Aktionen verhindert?
- Wie erkennt Nutzer den Sync-Status?
- Wie wird Datenverlust vermieden?

## 16. Realtime

Realtime überträgt Änderungen schnell zwischen Clients.

Risiken:

- Rechteprüfung;
- Verbindungskosten;
- Eventflut;
- Offlinezustand;
- Reihenfolge;
- doppelte Events;
- UI verlässt sich zu stark auf Push statt Reload.

Realtime nur verwenden, wenn der Nutzerwert klar ist.

## 17. Jobs und Queues

Hintergrundjobs eignen sich für:

- E-Mails;
- Medienverarbeitung;
- KI-Auswertung;
- Exporte;
- Löschung;
- Abrechnung;
- Synchronisation.

Benötigt:

- Idempotenz;
- Retry;
- Dead-Letter-/Fehlerweg;
- Monitoring;
- Status;
- Abbruch;
- Zeit- und Kostenlimits.

## 18. Webhooks

Ein Webhook informiert ein System über ein Ereignis, etwa Zahlung oder Kündigung.

Pflichten:

- Signatur prüfen;
- Event-ID speichern;
- idempotent verarbeiten;
- Reihenfolge nicht blind voraussetzen;
- Wiederholungen akzeptieren;
- Fehler monitoren;
- Daten minimal loggen.

## 19. Push und E-Mail

Zu planen:

- Zweck;
- Einwilligung oder andere Grundlage;
- Frequenz;
- Zeitzone;
- Opt-out;
- Deep Link;
- sensible Inhalte auf Sperrbildschirm;
- Zustellfehler;
- Anbieter und Kosten.

## 20. KI-Funktionen

Sichere Grundstruktur:

```text
App
→ Backend/KI-Gateway
→ Auth und Rechte
→ Validierung
→ Kosten-/Rate-Limit
→ Modell
→ Output-Prüfung
→ Ergebnis/Fallback
```

Zusätzlich:

- Modellversion;
- Promptversion;
- Testset;
- Halluzinationen;
- Quellen;
- Prompt Injection;
- RAG-Rechte;
- Tool-Berechtigungen;
- menschliche Kontrolle;
- Kill Switch.

## 21. Git und GitHub

Git speichert Versionsgeschichte.

Wichtige Begriffe:

- Repository;
- Commit;
- Branch;
- Pull Request;
- Merge;
- Tag/Release;
- Konflikt;
- Review.

Regeln:

- kleine Commits;
- klare Nachrichten;
- keine Secrets;
- Branch für größere Änderungen;
- Review und Tests vor Merge;
- Release-Versionen markieren.

## 22. Build, Test und CI

Build erzeugt ein auslieferbares Produkt.

CI führt automatisch aus:

- Formatierung;
- Lint;
- Typecheck;
- Tests;
- Build;
- Security-/Dependency-Scans;
- eventuell Deployment.

Ein grüner Build beweist nicht automatisch gute UX, Sicherheit oder rechtliche Korrektheit.

## 23. Monitoring und Observability

- Logs: konkrete Ereignisse;
- Metriken: aggregierte Werte;
- Traces: Ablauf über mehrere Systeme;
- Alarme: handlungsrelevante Schwellen;
- Runbooks: konkrete Reaktion.

Keine Secrets oder unnötigen personenbezogenen Daten loggen.

## 24. Backup, Restore und Rollback

- Backup: Kopie;
- Restore: Wiederherstellung;
- Rollback: Rückkehr zu vorheriger Version;
- RPO: tolerierbarer Datenverlust;
- RTO: tolerierbare Wiederherstellungszeit.

Ein Backup ohne getesteten Restore ist kein belastbarer Nachweis.

## 25. Skalierung

Nicht vorsorglich komplex bauen.

Zuerst messen:

- Datenbanklast;
- API-Latenz;
- Speicher;
- Jobs;
- Kosten;
- Fehlerraten;
- Nutzerverhalten.

Dann gezielt optimieren:

- Indizes;
- Pagination;
- Caching;
- Queues;
- CDN;
- Trennung einzelner Dienste;
- horizontale Skalierung.

## 26. Anbieterabhängigkeit

Für jeden Anbieter:

- welche Daten liegen dort?
- welches Format?
- wie exportieren?
- wie löschen?
- welche Alternative?
- wie lange dauert Migration?
- welche Kosten steigen mit Nutzung?
- was passiert bei Ausfall oder Kündigung?

## KI-Einsatz

KI kann technische Begriffe erklären, Diagramme und Code vorbereiten, Fehler analysieren, Tests erzeugen und Dokumentation pflegen.

Der Mensch muss Architektur, Kosten, Rechte, Sicherheitsfolgen, Anbieterwahl, reale Builds und Tests kontrollieren.

## Ergebnis

Nach diesem Kapitel soll der Leser die Systemteile einer App erklären, technische Angebote vergleichen und die Arbeit eines Coding-Agenten kritisch prüfen können.
