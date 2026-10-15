# 04 – Claude Code, Codex und KI-Funktionen

## 1. KI-Agenten richtig einsetzen

Claude Code, Codex und andere Coding-Agenten beschleunigen die Umsetzung. Sie ersetzen jedoch nicht Produktentscheidung, Architekturverantwortung, Sicherheitsprüfung, Teststrategie oder rechtliche Einordnung.

## 2. Verbindlicher Projektkontext

Vor Änderungen muss der Agent lesen:

- PRD
- Architekturentscheidungen
- Datenmodell
- Designsystem
- Security-Regeln
- Datenschutz-/Compliance-Matrix
- Test- und Releaseprozess

## 3. Jeder Arbeitsauftrag braucht

1. Ziel
2. Nicht-Ziele
3. betroffene Dateien/Bereiche
4. Akzeptanzkriterien
5. Tests
6. Migrationen
7. Sicherheits- und Datenschutzauswirkung
8. Rollback

## 4. Agentenregeln

- keine Secrets im Client oder Repository;
- keine DB-Änderung ohne Migration;
- keine neue Abhängigkeit ohne Begründung, Wartungs- und Lizenzprüfung;
- keine Tests löschen, damit CI grün wird;
- keine Autorisierung nur im UI;
- bestehende Geschäftslogik nicht stillschweigend ändern;
- nach jedem kleinen Schritt Lint, Typen, Tests und Build;
- UI immer gerendert prüfen;
- unklare Hochrisiko-/Compliance-Fragen markieren statt erfinden.

## 5. Arbeitszyklus

```text
Plan
→ kleiner Patch
→ automatische Tests
→ manueller Review
→ gerenderter Screenshot oder E2E
→ akzeptieren oder korrigieren
→ Commit
```

## 6. Context Engineering

Guter Kontext ist nicht maximal lang, sondern relevant und verbindlich:

- aktuelle betroffene Dateien;
- feste Regeln;
- Beispiele und Gegenbeispiele;
- gewünschtes Ausgabeformat;
- reproduzierbare Fehlermeldung;
- konkrete Prüfkriterien.

## 7. KI-Funktionen in der App

Geheime Schlüssel, Kostenkontrolle und sensible Regeln gehören hinter eine serverseitige Schicht.

```text
Nutzer → App → AI-Gateway → Eingabeprüfung → Modell → Ausgabeprüfung → App
                     ↘ Kosten, Rate Limits, Logs und Fallback
```

## 8. AI-System-Register

Für jede Funktion dokumentieren:

- Zweck
- Modell, Provider und Version
- Rolle des App-Anbieters
- Eingabe- und Ausgabedaten
- Risiko-/Rechtsprüfung
- Transparenzhinweis
- menschliche Aufsicht
- Testset und bekannte Grenzen
- Kostenlimit
- Fallback
- Änderungsdatum

## 9. Evaluation

Ein wiederholbares Testset enthält:

- normale Kernfälle
- Grenzfälle
- Halluzinationen
- verbotene Ausgaben
- Prompt Injection
- Datenexfiltration
- Quellenqualität
- Mehrsprachigkeit
- Verzerrung
- Latenz und Kosten

## 10. RAG und Agenten

RAG ersetzt keine Berechtigungsprüfung. Retrieval muss Nutzer- und Mandantenrechte beachten.

Aktionen ausführende Agenten benötigen:

- minimale Werkzeuge und Rechte
- Bestätigung für irreversible Schritte
- Idempotenz
- Zeit- und Kostenlimits
- Auditlogs
- sicheren Abbruch und Wiederaufnahme
