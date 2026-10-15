# Inhaltsverzeichnis – Allgemeine App-Entwicklung v1.0

## Einstieg

1. [Start hier](./START-HIER-V1.0.md)
2. [Entscheidungsweg](./00-start/entscheidungsweg.md)
3. [Quellen- und Rechtsstand](./QUELLEN-UND-RECHTSSTAND.md)
4. [Checkliste vor jedem Release](./CHECKLISTE-VOR-JEDEM-RELEASE.md)

## 01 – Produkt

- [Produkt, Problemvalidierung, MVP und PRD](./01-produkt/README.md)

## 02 – UX, UI und Design

- [UX/UI und Designsystem](./02-design/README.md)
- Figma- und Mobbin-Workflow
- Design Tokens und Komponenten
- Screen-Inventar und Zustände
- Accessibility-Baseline

## 03 – Technik, Daten und Supabase

- [Architektur, Backend und Supabase](./03-technik/README.md)
- Datenmodell und Berechtigungsmatrix
- Supabase-Produktionsregeln
- RLS-Testmatrix
- Auth, Storage und Realtime

## 04 – Claude Code, Codex und KI

- [Claude Code, Codex und KI-Funktionen](./04-ki-agenten/README.md)
- Context Engineering
- RAG, Embeddings und Caching
- Agenten, Tools und Guardrails
- KI-Evaluation und Kostenkontrolle

## 05 – Security, Datenschutz und Recht

- [Security, Datenschutz und Recht](./05-sicherheit-datenschutz-recht/README.md)
- Threat Modeling
- Datenlebenszyklus, Export und Kontolöschung
- DSGVO, AI Act, CRA, DSA, DDG, TDDDG und BFSG

## 06 – Tests, Release und Betrieb

- [Tests, Release und langfristiger Betrieb](./06-tests-release-betrieb/README.md)
- Release-Gates
- Store- und Web-Release
- Rollback, Monitoring und Fünf-Jahres-Betrieb

## 07 – Plattformwahl

- [Web, PWA, React Native/Expo, Flutter und Native](./07-plattformen/README.md)

## 08 – Zahlungen und Abos

- [Zahlungs-, Abo- und Entitlement-Playbook](./08-zahlungen-und-abos/README.md)

## 09 – Performance, Analytics und Observability

- [Performancebudgets, Metriken, Alarme und Kosten](./09-performance-analytics-betrieb/README.md)

## 10 – Sonderfälle

- [Medizin, Finanzen, Minderjährige, Community, Biometrie, Hardware und Enterprise](./10-sonderfaelle/README.md)

## 11 – Masterprozess und Qualität

- [App von 0 bis Release und Betrieb](./11-masterprozess/APP-VON-0-BIS-RELEASE.md)
- [Qualitätssystem und Definition of Done](./11-masterprozess/QUALITAETSSYSTEM.md)

## 12 – Agenten-Masterprompt

- [Claude-Code-/Codex-Masterprompt](./12-agenten-masterprompt/CLAUDE-CODE-APP-MASTERPROMPT.md)

## Vorlagen

- [Vorlagenübersicht](./vorlagen/README.md)
- [App-Risikoprofil](./vorlagen/app-risikoprofil.md)
- [PRD](./vorlagen/prd.md)
- [Produktionspaket v1](./vorlagen/produktionspaket-v1.md)
- weitere Vorlagen für Screen-Inventar, ADR, Dateninventar, Berechtigungen, Threat Model, KI-Systeme, Anbieter, Löschung, Tests, Release und Incident

## Beispielprojekt

- FocusFlow: PRD, Architektur, Datenmodell, Supabase/RLS, Testplan und Betrieb
- [Beispiel-Release-Dossier](./beispielprojekt-focusflow/V1-RELEASE-DOSSIER.md)

## Empfohlene Arbeitsweise

```text
START-HIER-V1.0
→ Risikoprofil
→ PRD
→ Design/Architektur
→ vertikaler Kernablauf
→ Produktionspaket
→ Qualitätsscore
→ Release-Checkliste
→ gestaffelter Rollout
```

## Versionsprinzip

Markdown im Repository ist die aktuelle Hauptquelle. PDF- und DOCX-Ausgaben sind Momentaufnahmen und müssen mit Version und Prüfdatum gekennzeichnet werden.
