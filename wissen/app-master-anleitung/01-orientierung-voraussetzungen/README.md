# Orientierung und Voraussetzungen

Dieses Kapitel klärt vor der ersten Codezeile, welche Art App gebaut wird, welche Konten, Geräte, Fähigkeiten, Unterlagen und laufenden Ressourcen benötigt werden und welcher Entwicklungsweg zum Risiko des Projekts passt.

## Ergebnis dieses Kapitels

Am Ende liegen vor:

- App-Typ und Zielplattformen;
- Projektrolle und Verantwortlichkeiten;
- Geräte- und Testgeräteplan;
- Konten- und Zugangsliste;
- Werkzeug- und Anbieterplan;
- Kostenrahmen und Zeitbudget;
- Kompetenz- und Unterstützungsplan;
- gewählter Schnell-, Standard- oder Hochrisikoweg;
- erster Projektordner mit Verantwortlichem und Prüfdatum.

## 1. App-Arten verstehen

| App-Art | Typische Nutzung | Besonderheiten |
|---|---|---|
| Web-App | Browser, SaaS, Dashboards, Portale | Domain, Hosting, Browserkompatibilität, Cookies und Web-Sicherheit |
| PWA | installierbare Web-App | Offline-App-Shell, Manifest, Service Worker, Plattformgrenzen |
| Native iOS | Apple-Geräte | Apple-Entwicklung, Signierung, Berechtigungen, App-Review |
| Native Android | Android-Geräte | Gerätevielfalt, Berechtigungen, Signierung, Google-Play-Regeln |
| Cross-Platform Mobile | iOS und Android aus gemeinsamer Basis | Framework- und Pluginpflege, native Sonderfälle |
| Desktop-App | Windows, macOS, Linux | Installer, Updates, Dateisystem, Plattformrechte |
| SaaS/Plattform | mehrere Nutzer, Rollen oder Organisationen | Mandantentrennung, Abrechnung, Support und Betrieb |
| Offline-App | lokale Daten ohne Cloudzwang | Backup, Export, Gerätewechsel und lokale Sicherheit |
| IoT/Hardware-App | Verbindung zu Geräten | physische Sicherheit, Firmware, Updatepflichten und Produkthaftung |
| KI-App | Modelle, RAG oder Agenten | Datenfluss, Evaluation, Kosten, Transparenz und Missbrauchsschutz |

Eine App kann mehrere Arten kombinieren. Die Kombination erhöht Aufwand und Prüfbedarf.

## 2. Projektrollen

Auch eine Einzelperson muss die Rollen gedanklich trennen:

- **Produktverantwortung:** Problem, Zielgruppe, Nutzen, Prioritäten und Wirtschaftlichkeit;
- **UX/UI:** Struktur, Flows, Inhalte, Designsystem und Usability;
- **Entwicklung:** Architektur, Code, Daten, Integrationen und Builds;
- **QA:** Testfälle, Geräte, Fehler- und Grenzfälle;
- **Security/Privacy:** Bedrohungen, Daten, Berechtigungen, Anbieter und Vorfälle;
- **Release:** Store-Unterlagen, Signierung, Versionierung, Rollout und Rollback;
- **Marketing:** Positionierung, Inhalte, Kampagnen, ASO und Messung;
- **Betrieb/Support:** Monitoring, Kosten, Nutzeranfragen, Updates und Notfälle.

Für jede Rolle wird dokumentiert:

```text
Rolle
→ verantwortliche Person
→ Entscheidungen
→ notwendige Freigaben
→ Vertretung
→ Eskalationsweg
```

## 3. Geräte und Infrastruktur

### Entwicklungsgeräte

- ausreichend unterstützter Rechner;
- aktuelles, unterstütztes Betriebssystem;
- verschlüsselter Datenträger;
- Passwortmanager;
- Mehrfaktor-Authentifizierung;
- zuverlässige Sicherung wichtiger Projektunterlagen;
- getrennte lokale und produktive Zugangsdaten.

### Testgeräte

Mindestens nach Produktbedarf:

- kleines und großes Smartphone;
- mindestens ein älteres unterstütztes Gerät;
- Tablet, falls vorgesehen;
- relevante Browser und Desktopgrößen;
- langsames Netz, Offlinezustand und wenig Speicher;
- reale Bedienung mit Tastatur, Screenreader oder vergrößertem Text.

Emulatoren und Simulatoren ergänzen echte Geräte, ersetzen sie aber nicht vollständig.

## 4. Konten und Zugänge

Je nach Projekt werden benötigt:

- GitHub- oder anderes Versionsverwaltungskonto;
- Domain- und DNS-Konto;
- Hosting-/Cloudkonto;
- Datenbank-/Backendkonto;
- E-Mail-Versand und Supportpostfach;
- Apple-Entwicklerkonto;
- Google-Play-Entwicklerkonto;
- Zahlungsanbieter;
- Analytics- und Monitoringanbieter;
- KI- und API-Anbieter;
- Design- und Medienwerkzeuge;
- Passwortmanager und Secret-Management;
- Steuer-, Rechnungs- oder Buchhaltungssystem.

Für jeden Zugang dokumentieren:

| Anbieter | Zweck | Eigentümer | Admins | MFA | Kosten | Daten/Region | Kündigung/Export | Vertretung |
|---|---|---|---|---|---:|---|---|---|
| | | | | | | | | |

Konten werden auf den tatsächlichen Betreiber angelegt, nicht dauerhaft auf private Konten externer Helfer.

## 5. Werkzeugkategorien

Werkzeuge ändern sich. Das Handbuch entscheidet deshalb zuerst nach Aufgabe:

- Recherche und Dokumentation;
- Produktplanung und Backlog;
- Wireframes und Design;
- Coding-Agent und Entwicklungsumgebung;
- Datenbank und Backend;
- Authentifizierung;
- Hosting und Deployment;
- Tests und Gerätecloud;
- Monitoring und Fehleranalyse;
- E-Mail, Push und Kommunikation;
- Zahlungen und Abos;
- Marketing, ASO und Content;
- Support und Wissensdatenbank.

Für jedes Werkzeug werden bewertet:

- Funktionsbedarf;
- Export- und Migrationsmöglichkeit;
- Kosten heute und bei Wachstum;
- Datenverarbeitung und Verträge;
- Sicherheit und Rollen;
- Wartung und Anbieterabhängigkeit;
- Ersatzweg bei Einstellung.

## 6. Kostenarten

### Einmalig

- Geräte und Testgeräte;
- Marken-, Rechts- oder Fachprüfung;
- Design- und Medienproduktion;
- Store- und Entwicklerregistrierung;
- Domain und erste Einrichtung;
- externe Entwicklung oder Security-Test.

### Laufend

- Hosting, Datenbank und Storage;
- E-Mail, Push und SMS;
- KI- und API-Nutzung;
- Monitoring und Analytics;
- Design-, Entwicklungs- und Marketingwerkzeuge;
- Support, Buchhaltung und Versicherungen;
- Wartung und Sicherheitsupdates;
- Werbung und Partnerschaften.

### Kostenmodell

Mindestens für diese Stufen rechnen:

```text
0–100 aktive Nutzer
1.000 aktive Nutzer
10.000 aktive Nutzer
100.000 aktive Nutzer, falls realistisch
```

Variable Kosten werden pro erfolgreichem Kernvorgang und pro aktivem Nutzer betrachtet.

## 7. Fähigkeiten und Lernplan

Ein Anfänger muss nicht alles vorab beherrschen, aber folgende Zusammenhänge verstehen:

- Produktproblem und Zielgruppe;
- User Flow und Screenstruktur;
- Frontend, Backend, Datenbank, Auth und API;
- Datenmodell und Berechtigungen;
- Git, Branch, Commit und Pull Request;
- Umgebungen und Secrets;
- Testarten und Releaseprozess;
- Datenschutz, Plattformregeln und Rechte;
- Marketing, Analytics, Support und Kosten.

Fehlendes Spezialwissen wird erkannt und beschafft, statt von KI erfunden.

## 8. Drei Entwicklungswege

### Schnellweg

Geeignet für risikoarme Prototypen, interne Tests und kleine Offline-Werkzeuge.

- minimale Daten;
- keine kritischen Entscheidungen;
- kein komplexes Zahlungs- oder Communitysystem;
- enger MVP;
- frühe Nutzerprüfung.

### Standardweg

Geeignet für normale öffentliche Apps mit Konten, Cloud-Daten oder Abos.

- vollständiges Projektpaket;
- Dev, Staging und Production;
- Rollen und Berechtigungen;
- automatisierte Kernprüfungen;
- Store-, Datenschutz-, Support- und Betriebsunterlagen.

### Hochrisikoweg

Ausgelöst etwa durch Gesundheit, Finanzen, Kinder, Biometrie, Hardware, kritische Infrastruktur oder erhebliche automatisierte Entscheidungen.

- externe Fachprüfung vor Kernumsetzung;
- strengere Dokumentation und Nachweise;
- formale Risiko- und Freigabeprozesse;
- zusätzliche Normen, Tests und Verantwortlichkeiten;
- keine Freigabe nur durch Coding-Agenten.

## 9. KI-Einsatz in dieser Phase

KI kann:

- Fragenkataloge erstellen;
- App-Arten vergleichen;
- Konten- und Kostenlisten vorbereiten;
- Risiken und fehlende Informationen markieren;
- Projektordner und Vorlagen anlegen;
- einen Lernplan entwerfen.

Der Mensch entscheidet:

- Betreiber und Verantwortlichkeit;
- Budget und Zeit;
- Zielplattform;
- tatsächliche Verträge und Konten;
- Risikoklasse;
- welche Aussagen fachlich oder rechtlich geprüft werden müssen.

## Freigabe-Gate

Der nächste Abschnitt beginnt erst, wenn:

- App-Art und Plattformen benannt sind;
- Betreiber und Verantwortliche feststehen;
- Konten, Geräte, Budget und Zeit realistisch geplant sind;
- Risiken den passenden Entwicklungsweg bestimmen;
- alle kritischen offenen Fragen dokumentiert sind.
