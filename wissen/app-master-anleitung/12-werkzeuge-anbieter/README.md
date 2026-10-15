# Werkzeuge und Anbieter auswählen und aktuell halten

Dieses Kapitel nennt bewusst keine dauerhaft „beste“ Plattform. Werkzeuge ändern sich. Das Handbuch liefert deshalb ein Auswahl-, Prüf- und Austauschsystem.

## Kategorien

Für jede App prüfen:

- KI-Chat und Recherche;
- Coding-Agent;
- Design/Prototyping;
- Repository und CI;
- Frontend-/Mobile-Framework;
- Backend/API;
- Datenbank;
- Auth;
- Storage/CDN;
- Hosting;
- E-Mail/Push/SMS;
- Analytics;
- Monitoring/Errors;
- Zahlungen;
- KI-Modelle/Embeddings;
- Karten/Suche/Übersetzung;
- Support/CRM;
- Marketing/ASO;
- Dokumentation;
- Security-/Dependency-Scans.

## Auswahlmatrix

| Anbieter/Werkzeug | Zweck | Kernanforderung | Kostenmodell | Daten/Region | Sicherheit | Export/Exit | Support | Reife | Entscheidung |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

## Pflichtfragen

### Produkt

- Löst das Werkzeug eine echte Anforderung?
- Wird es im Kernablauf oder nur aus Bequemlichkeit benötigt?
- Ist die UX abhängig von einer proprietären Besonderheit?

### Technik

- offizielle SDKs und Plattformen;
- Versions-/Supportpolitik;
- Rate Limits;
- Verfügbarkeit/SLA;
- lokale Entwicklung und Staging;
- Migrationen;
- Webhooks;
- Observability;
- Backups;
- Skalierung.

### Daten und Recht

- welche Daten erhält der Anbieter?
- Region und Transfers;
- Unterauftragnehmer;
- Löschung/Export;
- Aufbewahrung;
- Training/Weiterverwendung;
- DPA/Verträge;
- Alters-/Inhaltsgrenzen;
- verbotene Nutzungen.

### Wirtschaft

- Fixkosten;
- variable Kosten;
- Kosten bei 100/1.000/10.000 Nutzern;
- Mindestvertrag;
- Zahlungswährung;
- Supportkosten;
- Preisänderungsrisiko;
- Wechselkosten.

### Exit

- Datenexportformat;
- Alternativen;
- Abstraktionsschicht;
- Migrationsdauer;
- Downtime;
- doppelte Betriebsphase;
- Vertrags-/Löschabschluss.

## KI-Modelle und Coding-Agenten

Getrennt bewerten:

- Codeverständnis;
- Kontextgröße;
- Toolzugriff;
- Patchqualität;
- Testverhalten;
- Datenschutz;
- Kosten;
- Latenz;
- Modell-/Versionskontrolle;
- IDE/CLI;
- Rechte und Bestätigung vor Aktionen.

Kein Agent erhält ungeprüft:

- Produktions-Secrets;
- vollständige Kundendaten;
- unbegrenzte Adminrechte;
- automatische Merge-/Deployrechte;
- irreversible Aktionen ohne Bestätigung.

## Stack-Entscheidung

Ein Stack wird erst gewählt, wenn diese Fragen beantwortet sind:

1. Welche Plattformen sind wirklich erforderlich?
2. Welche Gerätefunktionen werden benötigt?
3. Wie wichtig sind Offline und Hintergrundbetrieb?
4. Welche Daten und Rollen gibt es?
5. Welche laufenden Kosten entstehen?
6. Welche Kenntnisse sind vorhanden?
7. Wie wird getestet und veröffentlicht?
8. Wie kann später migriert werden?

## Standardwege

### Einfacher Web-/PWA-Weg

Geeignet für schnellen Test, geringe Geräteintegration und einfache Veröffentlichung.

### Cross-Platform-Mobile-Weg

Geeignet für iOS/Android mit gemeinsamer Produktlogik und moderaten nativen Anforderungen.

### Native-Weg

Geeignet bei tiefen Plattformfunktionen, hoher Performance oder spezialisierten Geräteanforderungen.

### Backend-as-a-Service

Geeignet für schnelle Entwicklung, wenn Datenmodell, RLS/Autorisierung, Migrationen, Kosten und Exit bewusst kontrolliert werden.

### Eigenes Backend

Geeignet bei besonderen Integrationen, Kontrolle oder Skalierungsanforderungen; höherer Betriebsaufwand.

## Anbieterregister pro App

| ID | Anbieter | Zweck | Daten | Vertrag/DPA | Region | Kostenlimit | Alarm | Löschung | Export | Ausfallplan | Verantwortlicher | geprüft am |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |

## Upgrade- und Austauschprozess

```text
neue Version/Preis/Regel
→ Auswirkung prüfen
→ Testumgebung
→ Kompatibilitäts- und Regressionstest
→ Kosten-/Datenschutzreview
→ gestaffelter Rollout
→ Monitoring
→ Rollback
→ Register aktualisieren
```

## Aktualisierungsrhythmus

- kritische Security-Hinweise: laufend;
- Abhängigkeiten: monatlich;
- Preise/Limits: quartalsweise;
- Verträge/Datenflüsse: jährlich oder anlassbezogen;
- vollständige Stackentscheidung: vor großem Versionssprung oder neuer Plattform.

## Ergebnis

Die konkrete Werkzeugliste steht nie nur in diesem allgemeinen Kapitel, sondern im Anbieterregister jeder App mit Version, Kosten, Daten, Exit und Prüfdatum.
