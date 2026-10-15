# Beispiel B – Team-Aufgaben-SaaS mit Konten und Abonnement

## 1. Ausgangslage

Eine Web-App hilft kleinen Teams, Aufgaben zu planen, Verantwortliche zuzuweisen und Fortschritt zu verfolgen. Nutzer besitzen Konten, Projekte haben mehrere Mitglieder und ein kostenpflichtiger Teamplan schaltet zusätzliche Funktionen frei.

## 2. Risikoklasse

Erhöht gegenüber einer Offline-App, weil:

- personenbezogene Kontodaten;
- Team-/Mandantentrennung;
- Rollen;
- Cloud-Daten;
- E-Mail und Einladungen;
- Abonnement und Webhooks;
- Admin-/Supportzugriffe;
- laufender Betrieb.

## 3. Problem und Zielgruppe

### Zielgruppe

- kleine Teams mit 2–20 Personen;
- bisherige Nutzung von Tabellen, Chat und E-Mail;
- keine komplexe Enterprise-Projektsteuerung;
- klarer Bedarf an Verantwortlichkeit und Übersicht.

### Problemstatement

Kleine Teams verlieren Aufgaben und Entscheidungen, weil Kommunikation, Dateien und Zuständigkeiten über mehrere Werkzeuge verteilt sind. Bestehende Systeme sind häufig zu komplex oder zu teuer.

### Problembelege

- mindestens zehn Interviews mit Teamverantwortlichen und Mitgliedern;
- reale Beispiele verlorener Aufgaben;
- Konkurrenzreviews;
- Test eines manuellen/No-Code-Prozesses;
- Pilotzusagen von zwei Teams.

## 4. Positionierung

```text
Eine einfache Aufgaben- und Verantwortlichkeitsplattform für kleine Teams, die ohne komplexe Projektmanagement-Einrichtung startet.
```

Nicht-Ziele im MVP:

- Gantt;
- Zeiterfassung;
- Chatersatz;
- offene Community;
- Enterprise-SSO;
- KI-Automation;
- native Apps.

## 5. Geschäftsmodell

### Free

- ein Projekt;
- begrenzte Mitglieder;
- Kernaufgaben;
- Export.

### Team

- mehrere Projekte;
- mehr Mitglieder;
- Rollen;
- erweiterte Historie;
- priorisierter Support.

### Wirtschaftlichkeit

Berechnen für 100, 1.000 und 10.000 aktive Nutzer:

- Datenbank;
- Storage;
- E-Mail;
- Monitoring;
- Zahlungsgebühren;
- Support;
- Backups;
- Marketing;
- Steuern/Verwaltung.

## 6. Recht, Regeln und Verträge

Prüfen:

- Betreiber und Märkte;
- Datenschutz und Auftragsverarbeitung;
- Unterauftragnehmer;
- Einladungs-E-Mails;
- Cookies/Analytics;
- Nutzungsbedingungen;
- B2B-/B2C-Einordnung;
- Preise, Laufzeit, Kündigung und Refunds;
- Marken-/Assetrechte;
- Löschung und Export;
- Store-Regeln erst bei späterer Mobile-App.

## 7. Rollen

| Rolle | Rechte |
|---|---|
| Gast | Landingpage, Einladung annehmen |
| Mitglied | erlaubte Projekte sehen, Aufgaben bearbeiten |
| Projektadmin | Mitglieder/Rollen im Projekt verwalten |
| Organisationsinhaber | Plan, Abrechnung und Organisation verwalten |
| Support | minimaler, protokollierter Supportzugriff |
| Systemadmin | Betrieb, keine unbegrenzte Produktdatennutzung |

Rollenserverseitig durchsetzen.

## 8. Datenmodell

```text
users
organizations
organization_members
projects
project_members
tasks
comments
invitations
subscriptions
entitlements
audit_events
```

Jede nutzerbezogene Ressource besitzt eindeutige Organisations-/Projektzuordnung.

## 9. Kernabläufe

### Organisation starten

```text
Registrieren
→ Organisation erstellen
→ Projekt erstellen
→ Mitglied einladen
→ Aufgabe erstellen
→ zuweisen
→ Status ändern
```

### Zahlung

```text
Plan auswählen
→ Checkout
→ Zahlungsanbieter bestätigt
→ Webhook verifizieren
→ Entitlement setzen
→ UI aktualisiert Plan
```

### Löschung

```text
Anfrage
→ Identität/Rolle prüfen
→ Abrechnungsfolgen zeigen
→ Export anbieten
→ Organisations-/Kontodaten nach Regel löschen
→ Anbieterjobs verfolgen
→ Abschluss bestätigen
```

## 10. UX/UI

Pflichtscreens:

- Landingpage;
- Registrierung/Login/Recovery;
- Organisation erstellen;
- Projektliste;
- Aufgabenliste/Board;
- Aufgabe Detail;
- Mitglieder/Rollen;
- Einladungen;
- Plan/Abrechnung;
- Datenschutz/Export/Löschung;
- Support;
- Admin intern.

Zustände:

- keine Organisation;
- keine Projekte;
- keine Aufgaben;
- Einladung abgelaufen;
- keine Berechtigung;
- Zahlung ausstehend/fehlgeschlagen;
- Offline/Netzfehler;
- große Listen;
- gelöschtes/gesperrtes Konto.

## 11. Architektur

```text
Web/PWA-Client
→ API/Backend
→ Auth
→ relationale Datenbank
→ Storage
→ E-Mail
→ Zahlungsanbieter
→ Analytics/Monitoring
→ Jobs/Queues
```

Spätere Mobile-App nutzt dieselbe vertrauenswürdige Backend-/Entitlement-Schicht.

## 12. KI-Entwicklung

Reihenfolge:

1. Repository/CI/Umgebungen;
2. Auth;
3. Organisation und Mitgliedschaft;
4. Projekt und Aufgabe;
5. Zwei-Nutzer-/Zwei-Organisationen-RLS/Autorisierungstests;
6. Einladungen;
7. Export/Löschung;
8. Zahlung/Entitlements;
9. Monitoring/Backups;
10. UI-Politur und Beta.

Agentenregel:

```text
Keine Ressource ohne Eigentümer-/Mandantenbeziehung. Keine Autorisierung nur im UI. Keine Zahlung ohne serverseitige Verifikation und idempotente Webhooks.
```

## 13. Tests

### Funktional

- Organisation erstellen;
- Mitglieder einladen;
- Einladung annehmen/ablaufen;
- Aufgabe CRUD;
- Rollenwechsel;
- Projekt verlassen;
- Konto-/Organisationslöschung.

### Security

- Nutzer A sieht keine Organisation B;
- Mitglied kann Ownerrechte nicht setzen;
- Supportzugriff protokolliert;
- direkte API-Anfragen;
- Rate Limits;
- Secret-Scan;
- Uploadprüfung.

### Zahlung

- Kauf;
- Kündigung;
- Verlängerung;
- fehlgeschlagen;
- Grace Period;
- Upgrade/Downgrade;
- Refund/Chargeback;
- doppelte/verspätete Webhooks;
- Kontolöschung.

### Recovery

- Stagingmigration;
- Restore;
- Rollback;
- E-Mail-/Zahlungsanbieter-Ausfall.

## 14. Beta

- zwei bis fünf echte Teams;
- getrennte Testorganisationen;
- wöchentliche Interviews;
- Supportkanal;
- Aktivierung messen: Organisation + Projekt + erste zugewiesene Aufgabe;
- keine öffentliche Werbung vor stabiler Mandantentrennung und Recovery.

## 15. Veröffentlichung

### Web

- Domain/HTTPS;
- Landingpage;
- Preis-/Nutzungsbedingungen;
- Datenschutz;
- Support-/Statusseite;
- Löschweg;
- Monitoring;
- Rollback.

### Mobile später

Erst bei belegtem Bedarf. Storetexte, Zahlungsregeln, Berechtigungen, Signierung und Gerätetests zusätzlich durchlaufen.

## 16. Marketing

### Botschaft

```text
Klare Zuständigkeiten für kleine Teams – ohne kompliziertes Projektmanagement.
```

### Kanäle

- Pilotkunden;
- kleine Unternehmen/Communities;
- problemorientierte Inhalte;
- Demo-Video;
- Vergleichs-/Alternative-Landingpages;
- Partnerschaften mit Beratern/Agenturen;
- Empfehlungsmechanismus;
- gezielte Suchanzeigen erst nach Conversion-Nachweis.

### Funnel

```text
Besuch
→ Demo/Registrierung
→ Organisation
→ Projekt
→ Mitglied eingeladen
→ Aufgabe zugewiesen
→ wiederkehrende Teamnutzung
→ Upgrade
```

## 17. Betrieb

Täglich:

- Auth, Fehler, Zahlungen, Jobs, Kosten.

Wöchentlich:

- Support, Einladungsfehler, Conversion, Churn, Reviews.

Monatlich:

- Abhängigkeiten;
- Rechte/Adminzugriffe;
- RLS-/Autorisierungstest;
- Löschjobs;
- Backups;
- Kosten/Profitabilität.

Quartalsweise:

- Restore;
- Incident-Übung;
- Anbieterreview;
- Preis-/Produktreview.

Jährlich:

- Recht/Stores/Verträge;
- Endgeräte/Frameworks;
- End-of-Life-/Migrationsplan.

## 18. Fertignachweise

- Problem-/Marktbelege;
- Geschäftsmodell;
- PRD/MVP;
- Rollen-/Berechtigungsmatrix;
- Datenmodell und Datenfluss;
- UX-/Usability-Test;
- Staging-Kernablauf;
- Zwei-Organisationen-Negativtests;
- Zahlungs-/Löschtests;
- Restore/Rollback;
- Release-Dossier;
- Marketing-/Betriebsplan.
