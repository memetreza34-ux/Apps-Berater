# So benutzt du diese Anleitung

## Das eigentliche Ziel

Diese Anleitung ist kein Buch, das nur gelesen wird. Sie ist ein Arbeitsprozess. Jeder Abschnitt erzeugt ein konkretes Ergebnis, das für die nächste Phase benötigt wird.

Beispiel:

```text
Problembelege
→ PRD
→ User Flow
→ Designsystem
→ Architektur
→ Umsetzung
→ Testnachweise
→ Release-Paket
→ Marketingplan
→ Betriebsplan
```

Wer einzelne Stufen überspringt, spart am Anfang Zeit und verliert sie später häufig durch Umbauten, Sicherheitsprobleme, schlechte Nutzerführung oder eine Veröffentlichung ohne Nachfrage.

## Die vier Dokumentarten

### 1. Anleitung

Erklärt das Thema verständlich und unabhängig von einem bestimmten Werkzeug.

### 2. Entscheidungshilfe

Hilft zwischen mehreren Wegen zu wählen, etwa Web-App oder native App, kostenlos oder Abo, Supabase oder eigenes Backend.

### 3. Vorlage

Wird für die konkrete App ausgefüllt. Eine leere Vorlage ist noch kein Ergebnis.

### 4. Playbook

Beschreibt einen aktuellen technischen Weg mit konkreten Werkzeugen, Befehlen und Anbieteroberflächen. Playbooks dürfen veralten und werden separat aktualisiert.

## Warum diese Trennung wichtig ist

In fünfzehn Jahren können heutige Frameworks, App-Baukasten, KI-Modelle oder Anbieter verschwunden sein. Diese Aufgaben bleiben trotzdem bestehen:

- Nutzerproblem prüfen;
- Anforderungen festlegen;
- ein verständliches Erlebnis gestalten;
- Daten und Rechte modellieren;
- sichere Änderungen durchführen;
- Qualität messen;
- ein Produkt veröffentlichen und betreiben;
- Nutzer gewinnen und halten.

Deshalb darf ein zeitloses Kapitel nicht sagen: „Benutze immer Werkzeug X“. Es erklärt zuerst die Entscheidung. Das aktuelle Playbook zeigt anschließend eine mögliche Umsetzung.

## Wähle deinen Weg

### Schnellweg – einfacher Prototyp

Geeignet für:

- reine Offline-App;
- keine Konten;
- keine sensiblen Daten;
- keine Zahlungen;
- keine automatische Entscheidung über Menschen;
- kleiner Test mit wenigen Personen.

Der Schnellweg darf Produktresearch und Design verkürzen. Security, Rechte an Inhalten und ehrliche Kommunikation dürfen trotzdem nicht übersprungen werden.

### Standardweg – öffentliche App

Geeignet für:

- Web-, iOS- oder Android-App;
- Nutzerkonten;
- Cloud-Daten;
- öffentliches Marketing;
- möglicherweise Abos oder Käufe;
- langfristiger Betrieb.

Der Standardweg verwendet alle Hauptphasen und verlangt echte Test-, Datenschutz-, Release- und Betriebsnachweise.

### Hochrisikoweg

Erforderlich bei:

- Medizin oder Gesundheit mit Diagnose-/Therapiebezug;
- personalisierten Finanz-, Kredit- oder Versicherungsentscheidungen;
- Minderjährigen als Kernzielgruppe;
- Biometrie, Identitäts- oder Emotionserkennung;
- Hardware mit möglicher körperlicher Wirkung;
- kritischer Infrastruktur;
- automatisierten Entscheidungen mit erheblicher Wirkung;
- großen Mengen besonderer personenbezogener Daten.

Hier reicht eine allgemeine Anleitung nicht. Fachkundige Prüfung, zusätzliche Dokumentation, strengere Tests und möglicherweise Zulassungen oder Erlaubnisse werden Teil des Projekts.

## So arbeitest du mit KI

### KI darf vorbereiten

- Fragen für Interviews;
- Markt- und Wettbewerbslisten;
- erste PRD-Entwürfe;
- User-Flow-Varianten;
- Wireframes und Designbeschreibungen;
- Architekturvorschläge;
- Code und Tests;
- Dokumentation;
- Store-Texte und Marketingvarianten;
- Auswertung anonymisierter Messdaten.

### KI darf nicht ungeprüft entscheiden

- ob ein Problem wirklich relevant ist;
- ob Nutzer ein Design verstehen;
- ob eine rechtliche Einordnung stimmt;
- ob eine Security-Lücke geschlossen ist;
- ob medizinische oder finanzielle Inhalte korrekt sind;
- ob ein Store-Formular wahrheitsgemäß ausgefüllt ist;
- ob eine App veröffentlicht werden darf;
- ob ein Preis akzeptiert wird;
- ob ein Marketingversprechen ehrlich ist.

## Arbeitsregel für Coding-Agenten

Jeder Auftrag enthält mindestens:

```text
Ziel
Nicht-Ziele
betroffene Dateien
Akzeptanzkriterien
Design- und Datenregeln
Security-/Privacy-Anforderungen
Tests
Migration und Rollback
gewünschter Abschlussbericht
```

Der Agent arbeitet in kleinen Schritten:

```text
Repository lesen
→ Bestandsanalyse
→ Plan
→ einen Schritt umsetzen
→ Tests und gerenderte Prüfung
→ Risiken dokumentieren
→ Commit
→ nächster Schritt
```

## Was du für jede App anlegst

Empfohlener Projektordner:

```text
project-docs/
├── 00-app-steckbrief.md
├── 01-problem-und-zielgruppe.md
├── 02-markt-und-positionierung.md
├── 03-geschaeftsmodell-und-kosten.md
├── 04-risiken-und-rechte.md
├── 05-prd-und-mvp.md
├── 06-user-flows-und-screens.md
├── 07-designsystem.md
├── 08-architektur-und-daten.md
├── 09-entwicklungsplan.md
├── 10-testplan.md
├── 11-release-dossier.md
├── 12-marketing-und-launch.md
└── 13-betrieb-und-weiterentwicklung.md
```

Dazu kommt ein Evidenzordner mit Testläufen, Screenshots, Messungen und Freigaben. Keine Secrets oder unnötigen personenbezogenen Daten dort speichern.

## Freigaben statt Bauchgefühl

Eine Phase ist erst abgeschlossen, wenn ihr Ergebnis nachweisbar vorliegt.

Beispiele:

- „Nutzer brauchen die App“ → Interview- und Nutzungsbelege;
- „Design ist verständlich“ → Usability-Test;
- „Daten sind getrennt“ → negativer Zwei-Nutzer-Test;
- „Backup funktioniert“ → Restore-Protokoll;
- „App ist schnell“ → Messung auf benannten Geräten;
- „Marketing funktioniert“ → Conversion- und Akquisitionsdaten;
- „App ist fertig“ → Release-Dossier ohne Blocker.

## Aktualisierungsprinzip

Jede zeitabhängige Angabe bekommt:

- Quelle;
- Prüfdatum;
- betroffenes Kapitel;
- nächstes Prüfdatum;
- Änderungsnotiz.

Das Grundhandbuch bleibt stabil. Playbooks und Quellenregister werden regelmäßig aktualisiert.

## Dein nächster Schritt

Öffne den [Gesamtfahrplan](./01-gesamtfahrplan.md), wähle Schnellweg, Standardweg oder Hochrisikoweg und beginne mit dem App-Steckbrief.
