# Funktionen, Systemaufbau, Struktur und Daten

Dieses Kapitel verbindet Produktidee, Benutzeroberfläche, technische Architektur und Daten. Es verhindert, dass eine App nur aus schönen Screens oder einer ungeordneten Funktionsliste besteht.

## Ziel

Vor der großen Umsetzung muss vollständig klar sein:

- welche Nutzerrollen existieren;
- welche Aufgaben diese Rollen erledigen;
- welche Funktionen dafür benötigt werden;
- wie die Funktionen zusammenhängen;
- welche Screens und Zustände existieren;
- welche Daten entstehen, gelesen, geändert, übertragen und gelöscht werden;
- welche Systeme und Anbieter beteiligt sind;
- welche Rechte, Kosten, Risiken und Tests je Funktion gelten.

## 1. Produktstruktur

```text
Produktziel
→ Nutzerrollen
→ Nutzeraufgaben
→ Kernabläufe
→ Funktionen
→ Module
→ Screens und Zustände
→ Datenobjekte
→ Systeme und Schnittstellen
→ Tests und Betrieb
```

Keine technische Komponente wird nur eingebaut, weil sie modern ist. Jede Komponente muss einem belegten Produktbedarf dienen.

## 2. Rollenmodell

Für jede Rolle dokumentieren:

| Rolle | Ziel | darf sehen | darf erstellen | darf ändern | darf löschen | besondere Rechte | Risiken |
|---|---|---|---|---|---|---|---|
| Gast | | | | | | | |
| Nutzer | | | | | | | |
| Teammitglied | | | | | | | |
| Moderator | | | | | | | |
| Support | | | | | | | |
| Administrator | | | | | | | |

Rollen werden nicht nur in der Navigation versteckt. Berechtigungen müssen serverseitig oder in einer gleichwertig vertrauenswürdigen Schicht durchgesetzt werden.

## 3. Funktionsbaum

Jede App erhält einen Funktionsbaum. Beispiel:

```text
App
├── Einstieg
│   ├── Onboarding
│   ├── Registrierung
│   ├── Login
│   └── Recovery
├── Kernfunktion
│   ├── Übersicht
│   ├── Erstellen
│   ├── Detail
│   ├── Bearbeiten
│   ├── Löschen
│   └── Teilen
├── Suche und Organisation
│   ├── Suche
│   ├── Filter
│   ├── Sortierung
│   └── Archiv
├── Kommunikation
│   ├── Push
│   ├── E-Mail
│   └── In-App-Mitteilungen
├── Konto
│   ├── Profil
│   ├── Datenschutz
│   ├── Export
│   └── Löschung
├── Monetarisierung
│   ├── Pläne
│   ├── Kauf
│   ├── Entitlement
│   ├── Kündigung
│   └── Restore
└── Betrieb
    ├── Support
    ├── Moderation
    ├── Admin
    ├── Monitoring
    └── Feature Flags
```

Der konkrete Baum wird an die App angepasst. Nicht benötigte Module werden entfernt.

## 4. Funktionsdossier

Für jede Funktion wird dieselbe Vorlage ausgefüllt.

### Identität

- Funktions-ID:
- Name:
- Modul:
- Version:
- Verantwortlicher:
- Status: Idee / geplant / in Entwicklung / Beta / Produktion / eingestellt

### Produkt

- Nutzerproblem:
- Zielgruppe und Rolle:
- erwartetes Ergebnis:
- Erfolgsmetrik:
- Nicht-Ziele:
- Priorität:
- Abhängigkeiten:

### Ablauf

- Auslöser:
- Vorbedingungen:
- Normalablauf:
- Alternativabläufe:
- Fehlerfälle:
- Offline-Verhalten:
- Retry und Doppelaktion:
- Abbruch und Wiederaufnahme:
- Erfolg und nächster Schritt:

### Oberfläche

- betroffene Screens:
- Navigation:
- Eingaben:
- Ausgaben:
- Loading:
- Empty:
- Error:
- Offline:
- Success:
- Disabled:
- Berechtigungsfehler:
- Accessibility:
- Responsive und Plattformunterschiede:

### Daten

- gelesene Daten:
- erzeugte Daten:
- geänderte Daten:
- gelöschte Daten:
- Eigentümer oder Mandant:
- Rechtsgrundlage und Zweck:
- Aufbewahrung:
- Export:
- Drittanbieter:
- Logs und Analytics:
- KI-Daten:

### Technik

- Client-Komponenten:
- Backend/API:
- Datenbanktabellen:
- Storage:
- externe APIs:
- Hintergrundjobs:
- Realtime:
- Feature Flags:
- Migration:
- Rollback:

### Qualität

- Akzeptanzkriterien:
- Unit-Tests:
- Integrations-Tests:
- E2E-Tests:
- negative Berechtigungstests:
- Performanceziel:
- Security- und Missbrauchsfälle:
- Datenschutztest:
- manuelle Geräteprüfung:

### Betrieb

- Monitoring:
- Alarm:
- Kostenlimit:
- Supportdiagnose:
- Kill Switch:
- bekannte Restrisiken:
- nächstes Prüfdatum:

## 5. Screen-Inventar

| Screen-ID | Zweck | Rolle | Eingang | Hauptaktion | Daten | Zustände | Berechtigung | Accessibility | Test |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

Jeder Screen benötigt mindestens die anwendbaren Zustände:

- Initial;
- Loading;
- Daten vorhanden;
- leer;
- Validierungsfehler;
- Serverfehler;
- keine Berechtigung;
- offline;
- teilweise geladen;
- Erfolg;
- veraltete Daten;
- deaktivierte Funktion.

## 6. Systemkontext

Jede App erhält ein einfaches Systemdiagramm:

```text
Nutzer
→ App oder Browser
→ API/Backend
→ Authentifizierung
→ Autorisierung
→ Datenbank und Storage
→ externe Anbieter
→ Logs, Metriken und Alarme
```

Zusatzsysteme werden nur ergänzt, wenn sie tatsächlich verwendet werden:

- KI-Gateway;
- Zahlungsanbieter;
- Push-/E-Mail-Dienst;
- Suchindex;
- Queue und Worker;
- Analytics;
- Content-Management;
- Admin-Portal;
- Moderation;
- Data Warehouse;
- IoT- oder Hardware-Gateway.

## 7. Architekturschichten

### Client

- Darstellung und Interaktion;
- lokaler UI-Zustand;
- sichere lokale Speicherung;
- Offline-Cache;
- Eingabevalidierung als Nutzerhilfe;
- keine geheimen Schlüssel;
- keine alleinige Autorisierungsentscheidung.

### Backend/API

- Geschäftslogik;
- Authentifizierung und Autorisierung;
- Validierung;
- Rate Limits;
- Idempotenz;
- Orchestrierung externer Anbieter;
- strukturierte Fehler;
- Audit und Monitoring.

### Datenbank

- eindeutige Datenmodelle;
- Constraints;
- Beziehungen;
- Transaktionen;
- Indizes;
- Berechtigungen;
- Migrationen;
- Lösch- und Aufbewahrungslogik.

### Storage

- öffentliche und private Dateien;
- Dateitypen und Größen;
- Pfad- und Eigentumsmodell;
- Uploadprüfung;
- signierte Zugriffe;
- Varianten und Vorschaubilder;
- Löschung und Lebenszyklus.

### Externe Anbieter

Für jeden Anbieter:

- Zweck;
- Daten;
- Region;
- Vertrag und Bedingungen;
- Kosten;
- Limits;
- Ausfallverhalten;
- Datenschutz;
- Export und Wechsel;
- Ersatzanbieter oder Degradationsmodus.

## 8. Datenmodell

Für jedes Datenobjekt:

```text
Name und Zweck
Felder und Datentypen
Pflicht/optional
Validierung
Primärschlüssel
Fremdschlüssel
Eigentümer/Mandant
Rollen und Aktionen
Indizes
Version
Entstehungsquelle
Aufbewahrung
Löschung
Export
Audit
```

### Beispielhafte Datenklassen

- Konto- und Profildaten;
- Inhalts- und Nutzerdaten;
- Rollen und Mitgliedschaften;
- Einstellungen;
- Dateien und Medien;
- Zahlungs- und Entitlementdaten;
- Support- und Moderationsdaten;
- Benachrichtigungen;
- Analytics;
- Logs und Audit;
- KI-Prompts, Antworten und Evaluationen;
- Embeddings und Retrieval-Metadaten;
- Einwilligungen und Rechtsnachweise.

## 9. Datenflussdiagramm

Für jeden wichtigen Ablauf wird gezeigt:

```text
Quelle
→ Erfassung
→ Validierung
→ Verarbeitung
→ Speicherung
→ Weitergabe
→ Nutzung
→ Export
→ Löschung
```

Pflichtfragen:

- Wo entstehen die Daten?
- Wer kontrolliert sie?
- Welche Systeme besitzen Kopien?
- Welche Daten verlassen das Gerät oder die Region?
- Welche Daten werden in Logs, Backups oder KI-Anbietern gespeichert?
- Wie wird ein einzelner Nutzer vollständig exportiert oder gelöscht?
- Was geschieht bei Anbieterwechsel oder Produktende?

## 10. Authentifizierung und Autorisierung

Das Handbuch trennt:

- Identität: Wer ist die Person oder das System?
- Authentifizierung: Wie wird die Identität nachgewiesen?
- Session: Wie lange gilt der Nachweis?
- Autorisierung: Was darf diese Identität tun?
- Eigentum/Mandant: Zu wem gehört die Ressource?
- Adminrechte: Welche besonders starken Aktionen existieren?
- Audit: Wie werden kritische Aktionen nachvollzogen?

Zu testen:

- Gastzugriff;
- falsche oder abgelaufene Session;
- Nutzer A gegen Daten von Nutzer B;
- Rollenwechsel;
- entfernte Teammitgliedschaft;
- gesperrtes oder gelöschtes Konto;
- Adminaktion;
- API-Direktaufruf ohne UI;
- Datei- und Realtime-Zugriff.

## 11. API- und Integrationsstruktur

Für jede Schnittstelle:

- Zweck und Besitzer;
- Authentifizierung;
- Eingabe- und Ausgabeschema;
- Versionierung;
- Fehlercodes;
- Rate Limits;
- Timeout;
- Retry;
- Idempotenz;
- Webhooks und Signatur;
- Datenschutz und Logging;
- Test-/Sandboxzugang;
- Kosten;
- Abschaltung und Migration.

## 12. KI-Funktionen im System

KI wird als eigener kontrollierter Datenfluss behandelt:

```text
App
→ Authentifizierung
→ Berechtigung
→ Datenminimierung
→ KI-Gateway
→ Modell/Tools/Retrieval
→ strukturierte Prüfung
→ Ergebnis
→ Nutzerbestätigung oder sichere Aktion
```

Zu dokumentieren:

- konkreter Nutzen;
- Modell und Version;
- Systemprompt und Promptversion;
- Datenkategorien;
- Retrievalquellen und Berechtigungsfilter;
- Toolrechte;
- Ausgabeformat;
- Evaluation und Mindestqualität;
- Halluzinations- und Missbrauchsrisiko;
- Kosten- und Zeitlimit;
- Fallback;
- menschliche Kontrolle;
- Transparenz;
- Löschung und Export;
- Kill Switch und Modellwechsel.

## 13. Nichtfunktionale Anforderungen

Zusätzlich zur Funktionalität werden festgelegt:

- Sicherheit;
- Datenschutz;
- Zuverlässigkeit;
- Performance;
- Accessibility;
- Bedienbarkeit;
- Wartbarkeit;
- Kompatibilität;
- Portabilität;
- Skalierbarkeit;
- Beobachtbarkeit;
- Wiederherstellbarkeit;
- Internationalisierung;
- Kosten;
- Energie-, Netz- und Speicherbedarf;
- Support- und Updatezeitraum.

## 14. Repository-Struktur pro App

```text
/docs
  /product
  /design
  /architecture
  /data
  /security
  /privacy-legal
  /tests
  /release
  /marketing
  /operations
/src
/tests
/migrations
/scripts
/evidence
```

Die konkrete Struktur darf abweichen. Entscheidend ist, dass Anforderungen, Entscheidungen, Code, Tests und Nachweise auffindbar und versioniert sind.

## 15. Freigabe-Gates

### Produktstruktur freigegeben

- Rollen und Kernabläufe vollständig;
- Funktionen priorisiert;
- MVP und Nicht-Ziele festgelegt;
- Funktionsdossiers für den Kern vorhanden.

### Systemstruktur freigegeben

- Systemdiagramm;
- Architekturentscheidungen;
- Anbieter und Kosten;
- Umgebungen und Exit-Plan.

### Datenstruktur freigegeben

- Datenmodell;
- Datenfluss;
- Berechtigungsmatrix;
- Aufbewahrung, Export und Löschung;
- Migration und Recovery.

### Entwicklungsfreigabe

Erst danach wird der erste vollständige vertikale Kernablauf umgesetzt.

## Ergebnis dieses Kapitels pro Projekt

1. `ROLLEN-UND-BERECHTIGUNGEN.md`
2. `FUNKTIONSBAUM.md`
3. `FUNKTIONS-DOSSIERS/`
4. `SCREEN-INVENTAR.md`
5. `SYSTEMKONTEXT.md`
6. `ARCHITEKTUR-ADRS.md`
7. `DATENMODELL.md`
8. `DATENFLUESSE.md`
9. `API-UND-ANBIETERREGISTER.md`
10. `NICHTFUNKTIONALE-ANFORDERUNGEN.md`
11. `MIGRATIONS-UND-EXIT-PLAN.md`
