# Entwicklung mit KI – vom Projektkontext zum geprüften Release

Dieses Kapitel beschreibt, wie Coding-Agenten und andere KI-Systeme kontrolliert eingesetzt werden. Das Ziel ist nicht möglichst viel generierter Code, sondern ein nachvollziehbarer, sicherer und wartbarer Entwicklungsprozess.

## Grundsatz

```text
Klare Anforderung
→ vollständiger Projektkontext
→ kleiner Implementierungsplan
→ begrenzte Änderung
→ automatische und manuelle Prüfung
→ dokumentierter Commit
→ nächster Schritt
```

Der Agent erhält niemals nur den Auftrag „Baue die komplette App“. Große unkontrollierte Änderungen erschweren Fehlersuche, Reviews, Migrationen und Rollbacks.

## 1. Projektkontext für den Agenten

Vor jeder größeren Umsetzung müssen mindestens vorhanden sein:

- `README.md` mit Setup und Projektziel;
- App-Steckbrief;
- PRD und MVP;
- Nutzerrollen und Berechtigungsmatrix;
- Funktionsbaum und Funktionsdossiers;
- User Flows und Screen-Inventar;
- Designsystem und Komponentenregeln;
- Architekturentscheidungen;
- Datenmodell und Datenlebenszyklus;
- Security-, Datenschutz- und Rechtsentscheidungen;
- Testplan;
- Definition of Done;
- aktuelle offene Risiken.

Der Agent soll fehlende Informationen markieren, nicht stillschweigend erfinden.

## 2. Agentenrollen trennen

Ein einzelnes Modell kann mehrere Rollen simulieren, die Prüfungen werden aber getrennt ausgeführt:

1. **Analyst:** liest Repository, Anforderungen und Risiken.
2. **Planer:** erstellt kleine Umsetzungsschritte.
3. **Implementierer:** ändert nur bestätigten Scope.
4. **Tester:** sucht Fehler-, Grenz- und Negativfälle.
5. **Security-/Privacy-Reviewer:** prüft Daten, Rechte und Missbrauch.
6. **UX-Reviewer:** prüft Flows, Zustände und Accessibility.
7. **Release-Reviewer:** prüft Build, Migration, Rollback und Dokumentation.

Die gleiche KI-Antwort ist keine unabhängige Prüfung. Kritische Bereiche benötigen einen getrennten Reviewlauf und je nach Risiko eine zweite Person.

## 3. Standardauftrag an einen Coding-Agenten

Jeder Auftrag enthält:

```text
Ziel:
Nutzerergebnis:
Nicht-Ziele:
Betroffene Rollen:
Betroffene Funktionen und Daten:
Akzeptanzkriterien:
Fehler- und Grenzfälle:
Security-/Privacy-Anforderungen:
Design- und Accessibility-Regeln:
Erlaubte Dateien/Bereiche:
Verbotene Änderungen:
Testkommandos:
Migration und Rollback:
Erwarteter Abschlussbericht:
```

## 4. Verbindlicher Arbeitsablauf

### Schritt A – Bestandsanalyse

Der Agent nennt:

- relevante Dateien;
- bestehende Architektur;
- Datenflüsse;
- vorhandene Tests;
- Konflikte mit Anforderungen;
- fehlende Informationen;
- Risiken und mögliche Breaking Changes.

Noch keine Änderung.

### Schritt B – Implementierungsplan

Für jeden Teilschritt:

- Dateien;
- konkrete Änderung;
- Akzeptanzkriterium;
- Test;
- Daten- und Rechteauswirkung;
- Migration;
- Rollback;
- Dokumentationsänderung.

### Schritt C – Umsetzung

- nur bestätigten Teilschritt umsetzen;
- vorhandene Architektur und Komponenten nutzen;
- Patch klein halten;
- keine unnötigen Abhängigkeiten;
- keine Attrappen im Produktionspfad;
- keine Geheimnisse im Code;
- keine Geschäftsregel ohne Dokumentation verändern.

### Schritt D – Verifikation

Je nach Stack:

- Formatierung;
- Lint;
- Typprüfung;
- Unit-Tests;
- Integrationstests;
- Build;
- E2E-Kernablauf;
- negative Autorisierungstests;
- Screenshot-/UI-Prüfung;
- Accessibility-Baseline;
- Migration auf Testumgebung;
- Rollback- oder Restore-Probe.

### Schritt E – Abschlussbericht

- was geändert wurde;
- warum;
- welche Tests tatsächlich liefen;
- konkrete Ergebnisse;
- offene Risiken;
- Migration und Rollback;
- aktualisierte Dokumentation;
- genau der nächste sinnvolle Schritt.

## 5. Verbotene Agentenmuster

- vollständige Neuschreibung ohne belegten Grund;
- Tests löschen oder abschwächen, damit CI grün wird;
- Autorisierung nur in der Oberfläche;
- produktive Schlüssel im Client oder Repository;
- Datenbankänderung ohne Migration;
- ungeprüfte neue Abhängigkeiten;
- erfundene APIs, Gesetze, Preise oder Anbieterregeln;
- „alles fertig“ ohne Build und Tests;
- automatische Freigabe von Medizin-, Finanz- oder Hochrisikofunktionen;
- stille Änderung von Aufbewahrung, Rollen, Preisen oder Abos;
- Nutzung echter Produktionsdaten in Prompts oder Testumgebungen.

## 6. Repository-Struktur für KI-Arbeit

```text
/docs
  /product
  /design
  /architecture
  /security
  /privacy
  /release
/decisions
/evidence
/src
/tests
/migrations
/scripts
README.md
AGENTS.md oder vergleichbare Agentenregeln
```

Das konkrete Framework darf abweichen. Entscheidend ist, dass Anforderungen, Entscheidungen, Nachweise und Code auffindbar sind.

## 7. Aufgaben richtig schneiden

Schlecht:

> Baue Login, Dashboard, Abos, KI-Chat und Adminbereich komplett.

Besser:

```text
1. Login-Screen mit vorhandenen Komponenten
2. serverseitige Sessionprüfung
3. Fehler- und Recoveryfälle
4. Integrationstest
5. E2E auf Staging
6. Dokumentation und Evidenz
```

Ein Teilschritt sollte ein überprüfbares Nutzer- oder Systemergebnis liefern.

## 8. KI für Design

KI kann:

- Referenzen analysieren;
- Informationsarchitektur vorschlagen;
- Wireframes und Varianten erzeugen;
- Design Tokens vorbereiten;
- Komponentenverträge schreiben;
- Screens anhand klarer Spezifikation umsetzen;
- visuelle Abweichungen aus Screenshots markieren.

Menschlich geprüft werden:

- visuelle Qualität;
- Originalität und Rechte;
- Zielgruppenpassung;
- tatsächliche Bedienbarkeit;
- Accessibility;
- Konsistenz auf echten Geräten.

## 9. KI-Funktionen innerhalb der App

Für jede KI-Funktion dokumentieren:

- konkrete Nutzeraufgabe;
- Modell und Anbieter;
- Eingabedaten;
- Ausgabeformat;
- Speicherung und Löschung;
- Kosten- und Ratenlimit;
- fachliche Risiken;
- Transparenz;
- Evaluationstestset;
- Fallback;
- menschliche Eskalation;
- Kill Switch;
- Verhalten bei Modellwechsel.

Geheime Modellschlüssel gehören in eine geschützte serverseitige Umgebung.

## 10. RAG und Agentenwerkzeuge

RAG benötigt:

- dokumentierte Quellen;
- Berechtigungsfilter vor Retrieval;
- Chunking- und Metadatenstrategie;
- Quellenanzeige;
- Versions- und Löschkonzept;
- Tests für fehlende, alte und widersprüchliche Quellen.

Werkzeuge eines Agenten benötigen:

- minimale Rechte;
- validiertes Eingabeschema;
- klare Lesend-/Schreibend-Kennzeichnung;
- Bestätigung vor irreversiblen Aktionen;
- Idempotenz;
- Schritt-, Zeit- und Kostenlimits;
- Auditnachweis;
- Abbruch- und Wiederaufnahmeweg.

## 11. Modell- und Werkzeugwechsel

Damit der Prozess langfristig nutzbar bleibt, werden Aufgaben nicht an einen Markennamen gebunden.

```text
Aufgabe
→ erforderliche Fähigkeiten
→ Ein-/Ausgabeformat
→ Qualitätskriterien
→ Datenschutz-/Kostenanforderungen
→ aktuelles Werkzeug
→ Ersatzwerkzeug
```

Vor einem Wechsel:

- Goldenset gegen alt und neu ausführen;
- Qualität, Sicherheit, Kosten und Latenz vergleichen;
- Prompt- und Schema-Kompatibilität prüfen;
- gestaffelt ausrollen;
- Rollback bereithalten;
- Register aktualisieren.

## 12. Nachweise

Pro Änderung werden gespeichert:

- Anforderung und Akzeptanzkriterien;
- Agentenplan;
- relevanter Diff oder Pull Request;
- ausgeführte Testkommandos;
- Ergebnisse und Screenshots;
- Migration und Rollback;
- offene Risiken;
- Reviewentscheidung.

Prompts allein sind kein Qualitätsnachweis.

## Freigabe-Gate

Ein KI-entwickelter Abschnitt ist erst freigegeben, wenn:

- Scope und Nicht-Ziele eingehalten wurden;
- Build und anwendbare Tests bestanden sind;
- UI tatsächlich gerendert geprüft wurde;
- Daten und Berechtigungen negative Tests besitzen;
- keine Secrets oder Produktionsdaten offengelegt wurden;
- Migration und Rollback dokumentiert sind;
- Dokumentation und Evidenz aktualisiert wurden;
- offene Risiken sichtbar bleiben.
