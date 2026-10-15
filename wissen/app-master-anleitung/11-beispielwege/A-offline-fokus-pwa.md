# Beispiel A – Offline-Fokus-App als PWA

## 1. Ausgangslage

Eine einfache App hilft Nutzern, Aufgaben anzulegen und 25-minütige Fokusphasen zu starten. Alle Daten bleiben lokal im Browser. Kein Konto, keine Cloud, keine Zahlung und keine KI.

## 2. Warum dieser Weg sinnvoll ist

Dieses Beispiel zeigt den kleinsten vollständigen App-Lebenszyklus:

```text
Problem
→ MVP
→ UX/UI
→ lokale Technik
→ Tests
→ Web-Release
→ erste Nutzer
→ Betrieb
```

Es ist geeignet als Lernprojekt und als früher Test, bevor Konten oder Cloudfunktionen ergänzt werden.

## 3. Problem und Zielgruppe

### Problemstatement

Menschen, die kurze konzentrierte Arbeitseinheiten nutzen möchten, verlieren Zeit durch komplexe Produktivitätssysteme und möchten sofort eine Aufgabe plus Timer starten.

### Zielgruppe

- Einzelpersonen;
- Browser-/Smartphone-Nutzer;
- keine Teamfunktion erforderlich;
- geringe Einrichtungsbereitschaft;
- Datenschutzpräferenz für lokale Daten.

### Belege

- fünf Interviews;
- Beobachtung des heutigen Ablaufs mit Timer plus Notiz-App;
- Test eines klickbaren Prototyps;
- Warteliste oder kleine Testgruppe.

## 4. Positionierung

```text
Eine extrem einfache Fokus-App, die ohne Konto und ohne Cloud sofort funktioniert.
```

Nicht-Ziele:

- Teamarbeit;
- soziale Funktionen;
- KI;
- umfangreiche Statistiken;
- native Store-App im ersten Release.

## 5. Geschäftsmodell

Erster Release kostenlos. Kosten:

- Domain;
- statisches Hosting;
- optional Analytics ohne unnötige personenbezogene Daten;
- Supportzeit.

Spätere Optionen:

- freiwillige Unterstützung;
- Einmalkauf einer erweiterten Version;
- keine Monetarisierung, wenn Lernprojekt.

## 6. Recht und Regeln

Prüfen:

- Betreiber-/Anbieterinformationen, soweit anwendbar;
- Datenschutzerklärung auch bei minimalen Datenflüssen;
- Hosting-Logs;
- Analytics/Tracking;
- Rechte an Name, Icon, Font und Sounds;
- Accessibility;
- PWA-/Browsergrenzen.

Da keine Konten und keine Cloud-Appdaten existieren, sind Datenexport und Kontolöschung für Produktdaten nicht erforderlich. Lokale Datenlöschung muss dennoch klar möglich sein.

## 7. Produkt und MVP

### Kernablauf

```text
App öffnen
→ Aufgabe eingeben
→ Fokus starten
→ Timer läuft
→ Sitzung beenden
→ Aufgabe/Fortschritt lokal speichern
```

### MVP-Funktionen

- Aufgabe anlegen;
- Aufgabe auswählen;
- Timer starten/pausieren/zurücksetzen;
- lokale Speicherung;
- Daten exportieren;
- lokale Daten vollständig löschen;
- Offline-App-Shell;
- Light/Dark Mode;
- Accessibility-Baseline;
- Fehler-/Leer-/Erfolgzustände.

## 8. UX/UI

### Hauptscreens

- Dashboard;
- neue Aufgabe;
- Fokusansicht;
- Einstellungen/Daten;
- Hilfe/Datenschutz.

### Testfälle

- erste Nutzung ohne Daten;
- lange Aufgabentitel;
- Browserneustart;
- Offlinebetrieb;
- Tastatur;
- Screenreader;
- Textvergrößerung;
- Timer im Hintergrund;
- gelöschte lokale Daten.

## 9. Technik

### Plattform

Web/PWA.

### Architektur

```text
Browser-UI
→ lokale Anwendungslogik
→ lokale Speicherung
→ Service Worker für App-Shell
```

Keine Backend- oder Datenbankpflicht.

### Dateien

```text
index.html
styles.css
app.js
manifest.webmanifest
sw.js
tests/
```

### Wichtige Entscheidungen

- lokale Datenstruktur versionieren;
- Migrationsweg bei neuen Feldern;
- Timer nicht nur visuell zählen, sondern aus Zeitstempeln berechnen;
- Service-Worker-Updateverhalten;
- Exportformat dokumentieren.

## 10. Entwicklung mit KI

Aufträge in kleinen Schritten:

1. statische UI und Tokens;
2. Aufgabenmodell;
3. lokale Persistenz;
4. Timerlogik;
5. Export/Löschung;
6. Service Worker;
7. Tests;
8. Accessibility-/Screenshotprüfung.

Agentenregel:

```text
Keine Cloud, keine Konten und keine neuen Abhängigkeiten ohne bestätigte Scope-Änderung.
```

## 11. Tests

- Unit-Test für Timerberechnung;
- Strukturtest für Manifest und Service Worker;
- manuelle Offlineprüfung;
- Persistenz nach Neustart;
- Exportdatei öffnen;
- Löschung prüfen;
- Tastatur/Screenreader;
- kleine und große Displays;
- HTTP-Smoke-Test.

## 12. Veröffentlichung

### Vorbereiten

- Domain;
- HTTPS;
- Icon;
- Manifest;
- Privacy-/Supportseite;
- Fehlerseite;
- Cache-/Updateprüfung;
- Backup des Quellcodes;
- Release-Tag.

### Rollout

1. private URL;
2. fünf Testpersonen;
3. Fehler beheben;
4. öffentliche Landingpage;
5. kontrollierte Bekanntgabe.

## 13. Marketing

Geeignete Botschaft:

```text
Keine Anmeldung. Keine Cloud. Aufgabe eingeben und Fokus starten.
```

Kanäle:

- kurze Demo;
- Produktivitäts-Communities;
- Social-Media-Clip;
- SEO-Landingpage;
- persönliche Testgruppe;
- Open-Source-/Showcase-Plattform, falls passend.

Messen:

- Landingpage → App-Start;
- erster erstellter Task;
- erste abgeschlossene Sitzung;
- Wiederkehr nach 7 Tagen;
- Export-/Löschprobleme;
- Supportfragen.

## 14. Betrieb

Monatlich:

- Browserkompatibilität;
- defekte Links;
- Hostingkosten;
- Service-Worker-Updates;
- Supportfeedback;
- Abhängigkeiten, falls später ergänzt.

Jährlich:

- Datenschutz-/Hostingprüfung;
- Accessibility-Prüfung;
- Domainverlängerung;
- End-of-Life-Entscheidung.

## 15. Fertignachweise

- Problembelege;
- PRD/MVP;
- Screen-Inventar;
- funktionierende PWA;
- Testprotokoll;
- Datenschutz-/Rechteprüfung;
- Release-Tag;
- Launchplan;
- Wartungskalender.

## 16. Nächster Ausbau

Erst nach echtem Nutzungsbeleg:

- optionale Synchronisation;
- native Verpackung;
- Benachrichtigungen;
- Statistiken;
- bezahlte Version.

Jeder Ausbau verändert Daten-, Rechts-, Kosten- und Testumfang und durchläuft den Masterprozess erneut.
