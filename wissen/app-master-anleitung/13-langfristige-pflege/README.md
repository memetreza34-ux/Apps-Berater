# So bleibt das Handbuch über viele Jahre nutzbar

Das Handbuch trennt bewusst zeitlose Grundprinzipien von veränderlichen Werkzeugen, Gesetzen und Plattformregeln.

## 1. Drei Ebenen

### Zeitlose Grundlagen

Nur selten ändern:

- Problemvalidierung;
- Zielgruppe und Nutzen;
- MVP und Priorisierung;
- Rollen, Funktionen und Datenflüsse;
- UX und Accessibility;
- sichere Entwicklung;
- Test- und Recoverydenken;
- Marketingfunnel;
- Wirtschaftlichkeit;
- Betrieb und End-of-Life.

### Veränderliche Playbooks

Regelmäßig prüfen:

- KI-Modelle und Agenten;
- Frameworks;
- Hosting/Backend;
- Stores;
- Zahlungen;
- Gesetze und Normen;
- konkrete Befehle/Oberflächen;
- Anbieterpreise und Limits.

### Projektbelege

Je App aktuell halten:

- PRD;
- Funktionen;
- Daten;
- Regeln;
- Tests;
- Release;
- Marketing;
- Betrieb.

## 2. Versionierung

Versionsschema:

```text
MAJOR.MINOR.PATCH
```

- MAJOR: Struktur oder Prozess grundlegend geändert;
- MINOR: neues Kapitel, neue Regelgruppe oder neues Beispiel;
- PATCH: Fehler, Link, Formulierung oder kleine Aktualisierung.

Jede Ausgabe erhält:

- Version;
- Datum;
- Änderungsprotokoll;
- Quellenstand;
- bekannte Grenzen;
- nächste Prüfung.

## 3. Änderungsarten

### Recht/Store

Sofortige Anwendbarkeitsprüfung und Markierung betroffener Kapitel.

### Security

Kritische Hinweise priorisiert behandeln; keine jährliche Prüfung abwarten.

### Framework/Anbieter

Version, Supportende, Kosten, Migration und Exit prüfen.

### Produktmethodik

Nur nach belastbarer Erfahrung oder Quelle ändern; Trendbegriffe nicht ungeprüft übernehmen.

## 4. Prüfkalender

- monatlich: kritische Abhängigkeiten/Security;
- quartalsweise: Anbieter, Preise, Limits, Links;
- vor jedem Release: Stores, Daten, Zahlungen, Berechtigungen;
- jährlich: vollständige Rechts-/Normen-/Architekturprüfung;
- anlassbezogen: neue Länder, Zielgruppen, Daten, KI, Zahlungen, Community, Hardware.

## 5. Änderungsprotokoll

| Version | Datum | Änderung | Grund/Quelle | betroffene Kapitel | Migration für bestehende Projekte |
|---|---|---|---|---|---|
| | | | | | |

## 6. Veraltete Inhalte

Nicht still löschen.

- als veraltet markieren;
- Ersatz verlinken;
- Datum nennen;
- Migrationshinweis;
- historische Version archivieren;
- prüfen, welche Projekte betroffen sind.

## 7. Qualitätskontrolle

Bei jeder größeren Änderung:

- interne Links;
- Quellen;
- Widersprüche;
- Vorlagen;
- Beispielwege;
- Verständlichkeit für Anfänger;
- Anwendbarkeit für bestehende Apps;
- PDF/DOCX-Synchronität.

## 8. Feedback

Fehlende oder unklare Inhalte werden als Issue erfasst mit:

- Problem;
- Kapitel;
- Nutzergruppe;
- Beispiel;
- erwartete Verbesserung;
- Quelle/Nachweis;
- Priorität.

## 9. Toolneutralität

Ein Werkzeug darf nicht zum Grundprinzip erklärt werden.

Schlecht:

```text
Jede App muss Anbieter X verwenden.
```

Besser:

```text
Die App benötigt Authentifizierung mit diesen Anforderungen. Anbieter X ist eine aktuell geprüfte Option; Entscheidung und Exit werden dokumentiert.
```

## 10. PDF/DOCX

Repository-Markdown ist Hauptquelle. Exporte sind versionierte Momentaufnahmen.

Vor Export:

- Strukturprüfung;
- Links/Quellen;
- Versionsnummer;
- Inhaltsverzeichnis;
- Warnhinweise für zeitabhängige Inhalte;
- Druck-/Lesbarkeit;
- Archivierung.

## Ergebnis

Die Anleitung bleibt nutzbar, weil sie nicht von einem bestimmten Agenten, Framework oder Store-Screenshot abhängig ist und veränderliche Teile einen klaren Prüf- und Austauschprozess besitzen.
