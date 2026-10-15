# Produkt planen: Vision, PRD, Funktionen, MVP und Roadmap

Dieses Kapitel übersetzt ein belegtes Problem in ein klar begrenztes Produkt. Es verhindert Funktionssammlungen ohne Priorität und Apps, die nie einen vollständigen Kernablauf erreichen.

## Ziel

Am Ende liegen vor:

- Produktvision;
- Ziele und Nicht-Ziele;
- Nutzerrollen;
- Kernablauf;
- Funktionsbaum;
- MVP-Scope;
- PRD;
- Akzeptanzkriterien;
- priorisiertes Backlog;
- Release-Roadmap.

## 1. Produktvision

Die Vision beschreibt den langfristigen Nutzen, nicht eine Funktionsliste.

Vorlage:

```text
Wir helfen [Zielgruppe], [Ergebnis] zu erreichen, indem wir
[grundlegender Lösungsansatz]. Erfolg bedeutet [messbares Ergebnis].
```

Zusätzlich dokumentieren:

- Warum existiert das Produkt?
- Welches Verhalten oder Ergebnis soll sich ändern?
- Welche Prinzipien sind nicht verhandelbar?
- Welche Zielgruppe steht zuerst im Mittelpunkt?
- Was soll die App ausdrücklich nicht werden?

## 2. Ziele und Nicht-Ziele

### Ziele

Messbar und zeitlich einordnen:

- Nutzer kann den Kernablauf in weniger als X Minuten abschließen;
- mindestens X Prozent der Testnutzer erreichen Aktivierung;
- Kernfunktion funktioniert auf definierten Zielgeräten;
- Betrieb bleibt unter festgelegtem Kostenbudget.

### Nicht-Ziele

Beispiele:

- kein soziales Netzwerk im MVP;
- keine vollständige Desktop-App;
- keine automatische medizinische Entscheidung;
- keine zehn Integrationen vor dem ersten Nutzertest;
- keine internationale Einführung im ersten Release.

Nicht-Ziele schützen das Projekt vor unkontrolliertem Wachstum.

## 3. Nutzerrollen

Für jede Rolle:

| Rolle | Hauptziel | Kernaktionen | sensible Rechte | benötigte Daten | Ausschlüsse |
|---|---|---|---|---|---|
| Gast | | | | | |
| Nutzer | | | | | |
| Teammitglied | | | | | |
| Moderator | | | | | |
| Support | | | | | |
| Administrator | | | | | |

Rollen müssen später mit Berechtigungen, Daten und Tests verbunden werden.

## 4. Kernablauf

Der Kernablauf ist der kürzeste Weg vom Nutzerproblem zum Ergebnis.

```text
Auslöser
→ Einstieg
→ notwendige Eingabe
→ Verarbeitung
→ Ergebnis
→ Speichern/Teilen/Fortsetzen
```

Beispiel:

```text
Nutzer hat eine Aufgabe
→ öffnet App
→ erstellt Aufgabe
→ startet Fokuszeit
→ beendet Sitzung
→ sieht Fortschritt
```

Jeder zusätzliche Schritt benötigt eine Begründung.

## 5. Funktionen sammeln

Quellen für Funktionen:

- Problembelege;
- Kernablauf;
- Nutzerrollen;
- Sicherheits- und Rechtsanforderungen;
- Betrieb und Support;
- Monetarisierung;
- Accessibility;
- Store- und Plattformregeln.

Nicht aus „andere Apps haben das“ automatisch eine Pflichtfunktion ableiten.

## 6. Funktionsbaum

Strukturiere nach Modulen:

```text
App
├── Einstieg und Konto
├── Kernfunktion
├── Suche und Organisation
├── Kommunikation
├── Einstellungen und Datenschutz
├── Monetarisierung
├── Support und Moderation
└── Betrieb und Administration
```

Für jede Funktion wird das Funktionsdossier aus dem Kapitel `03-funktionen-system-daten` verwendet.

## 7. Priorisierung

### Muss

Ohne diese Funktion kann der Kernnutzen nicht sicher, legal oder wirtschaftlich getestet werden.

### Soll

Deutlich wertvoll, aber der erste Test funktioniert ohne sie.

### Kann

Verbesserung oder Komfort, nicht notwendig für die Kernfrage.

### Nicht jetzt

Bewusst verschoben, um Scope zu schützen.

Zusätzlich prüfen:

- Nutzerwert;
- Risiko;
- Aufwand;
- Betriebskosten;
- Abhängigkeiten;
- Lernwert;
- Rückbaubarkeit.

## 8. MVP definieren

Ein MVP ist nicht die billigste Attrappe. Es ist die kleinste belastbare Produktversion, mit der die wichtigste Hypothese getestet wird.

Der MVP enthält:

- einen vollständigen Kernablauf;
- notwendige Sicherheits- und Datenschutzfunktionen;
- Fehler-, Lade- und Leerzustände;
- minimale Supportmöglichkeit;
- Messung der Kernhypothese;
- Export/Löschung, wenn Daten und Konten betroffen sind;
- Kosten- und Missbrauchskontrollen.

Der MVP enthält normalerweise nicht:

- mehrere Zielgruppen gleichzeitig;
- umfangreiche Gamification;
- komplexe Community;
- viele Integrationen;
- vollständige Automatisierung aller Randfälle;
- internationale Skalierung.

## 9. PRD-Struktur

Ein gutes Product Requirements Document enthält:

1. Kontext und Problem;
2. Zielgruppe und Rollen;
3. Ziele und Nicht-Ziele;
4. Kernablauf;
5. MVP-Funktionen;
6. spätere Funktionen;
7. Datenobjekte;
8. Geschäftsregeln;
9. nichtfunktionale Anforderungen;
10. Accessibility;
11. Security und Datenschutz;
12. Analytics und Erfolgsmessung;
13. Abhängigkeiten;
14. Risiken und offene Fragen;
15. Akzeptanzkriterien;
16. Release- und Betriebsvoraussetzungen.

## 10. Akzeptanzkriterien

Akzeptanzkriterien beschreiben überprüfbares Verhalten.

Schlecht:

```text
Login soll gut funktionieren.
```

Besser:

```text
Gegeben ist ein bestätigtes Konto.
Wenn der Nutzer gültige Zugangsdaten eingibt,
dann wird eine Session erstellt und der Nutzer zum Dashboard geleitet.
Bei ungültigen Daten wird keine Information preisgegeben, ob die E-Mail existiert.
```

Für jede Funktion berücksichtigen:

- Happy Path;
- Berechtigungen;
- Validierung;
- Ladezustand;
- leerer Zustand;
- Fehler;
- Offline;
- Doppelaktion;
- Accessibility;
- Analytics nur bei Bedarf;
- Löschung und Datenfolgen.

## 11. Backlog

Jeder Backlog-Eintrag enthält:

- ID;
- Nutzerergebnis;
- verlinkte Anforderung;
- Priorität;
- Akzeptanzkriterien;
- betroffene Daten und Rollen;
- Designstatus;
- technische Abhängigkeiten;
- Tests;
- Risiken;
- Aufwandsschätzung;
- Releaseziel.

## 12. Vertikale Umsetzung planen

Nicht erst sämtliche Screens und danach Backend bauen.

Ein vertikaler Schritt umfasst:

```text
UI
→ Eingabevalidierung
→ Authentifizierung
→ Autorisierung
→ API/Datenbank
→ Erfolg und Fehler
→ Persistenz
→ Test
→ Monitoring
```

Der erste vertikale Schritt soll den Kernnutzen Ende zu Ende beweisen.

## 13. Roadmap

Roadmap nach Ergebnissen, nicht nur Features:

### Phase 0 – Machbarkeit

- Daten/API testen;
- Risiko klären;
- Prototyp;
- Kosten prüfen.

### Phase 1 – Kernablauf

- sicherer vertikaler Slice;
- erste Nutzerprüfung.

### Phase 2 – Beta

- vollständiger MVP;
- Fehlerfälle;
- Support;
- Analytics;
- Datenschutz.

### Phase 3 – Release Candidate

- Security;
- Performance;
- Store-Paket;
- Backup/Restore;
- Rollback.

### Phase 4 – Nach Release

- Aktivierung verbessern;
- Retention;
- Kosten;
- echte Nutzerprobleme priorisieren.

## 14. Änderungsmanagement

Neue Funktion nur aufnehmen, wenn beantwortet ist:

- Welches belegte Problem löst sie?
- Für welche Rolle?
- Welche Metrik verändert sie?
- Welche Daten und Rechte benötigt sie?
- Welche Kosten erzeugt sie?
- Was wird dafür verschoben oder entfernt?
- Wie kann sie zurückgerollt oder abgeschaltet werden?

## KI-Einsatz

KI kann:

- PRD-Entwurf strukturieren;
- Funktionsideen clustern;
- Akzeptanzkriterien formulieren;
- Abhängigkeiten und Randfälle finden;
- Backlog-Einträge erstellen;
- Roadmap-Varianten vergleichen;
- Inkonsistenzen zwischen Dateien erkennen.

KI darf nicht:

- Problembelege erfinden;
- Scope ohne Freigabe erweitern;
- Sicherheits- oder Rechtsanforderungen als optional entfernen;
- Produktentscheidungen nur anhand generischer Best Practices treffen;
- Akzeptanzkriterien als bestanden erklären, ohne Tests.

## Ergebnisse und Gate

Vor Design und Entwicklung müssen vorliegen:

- Produktvision;
- Ziele/Nicht-Ziele;
- Rollenmodell;
- Kernablauf;
- Funktionsbaum;
- MVP-Liste;
- PRD;
- Akzeptanzkriterien;
- priorisiertes Backlog;
- Roadmap.

**Gate bestanden:** Jede MVP-Funktion ist einem belegten Nutzer-, Sicherheits-, Rechts- oder Geschäftsbedarf zugeordnet und der vollständige Kernablauf ist klar beschrieben.
