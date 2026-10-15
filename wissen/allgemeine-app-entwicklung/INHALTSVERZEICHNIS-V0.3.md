# Inhaltsverzeichnis – Allgemeine App-Entwicklung v0.3

## 0. Start

- [Entscheidungsweg und Risikoprüfung](./00-start/entscheidungsweg.md)
- [App-Risikoprofil](./vorlagen/app-risikoprofil.md)

## 1. Produkt

- [Produkt und MVP](./01-produkt/README.md)
- [PRD-Vorlage](./vorlagen/prd.md)

## 2. UX, UI und Design

- [Grundlagen UX/UI/Designsystem](./02-design/README.md)
- [Figma- und Mobbin-Workflow](./02-design/figma-und-mobbin-workflow.md)
- [Design Tokens und Komponenten](./02-design/design-tokens-und-komponenten.md)
- [Screen-Inventar](./vorlagen/screen-inventar.md)

## 3. Architektur, Backend und Supabase

- [Technik-Grundlagen](./03-technik/README.md)
- [Architektur-Entscheidungsleitfaden](./03-technik/architektur-entscheidungsleitfaden.md)
- [Supabase-Produktionsleitfaden](./03-technik/supabase-produktionsleitfaden.md)
- [Supabase-RLS-Testmatrix](./03-technik/supabase-rls-testmatrix.md)
- [ADR-Vorlage](./vorlagen/architecture-decision-record.md)
- [Berechtigungsmatrix](./vorlagen/berechtigungsmatrix.md)

## 4. Claude Code, Codex und KI

- [KI-Agenten-Grundlagen](./04-ki-agenten/README.md)
- [Claude-Code- und Codex-Playbook](./04-ki-agenten/claude-code-und-codex-playbook.md)
- [KI-Produktionsleitfaden](./04-ki-agenten/ki-produktionsleitfaden.md)
- [KI-Systemregister](./vorlagen/ki-systemregister.md)

## 5. Security, Datenschutz und Recht

- [Grundlagen Security/Datenschutz/Recht](./05-sicherheit-datenschutz-recht/README.md)
- [Threat Model und Security-Baseline](./05-sicherheit-datenschutz-recht/threat-model-und-security-baseline.md)
- [Datenlebenszyklus, Export und Löschung](./05-sicherheit-datenschutz-recht/datenlebenszyklus-export-und-loeschung.md)
- [Threat-Model-Vorlage](./vorlagen/threat-model.md)
- [Daten- und Anbieterregister](./vorlagen/daten-und-anbieterregister.md)
- [Quellen- und Rechtsstand](./QUELLEN-UND-RECHTSSTAND.md)

## 6. Tests, Release und Betrieb

- [Grundlagen Tests/Release/Betrieb](./06-tests-release-betrieb/README.md)
- [Teststrategie und Release-Gates](./06-tests-release-betrieb/teststrategie-und-release-gates.md)
- [Release-Freigabe](./vorlagen/release-freigabe.md)
- [Incident Report](./vorlagen/incident-report.md)

## 7. Durchgehendes Beispielprojekt

- [FocusFlow Übersicht](./07-beispielprojekt-focusflow/README.md)
- [FocusFlow PRD](./07-beispielprojekt-focusflow/PRD.md)
- [FocusFlow Architektur](./07-beispielprojekt-focusflow/ARCHITEKTUR.md)
- [FocusFlow Supabase-Schema und RLS](./07-beispielprojekt-focusflow/supabase-schema-und-rls.sql)
- [FocusFlow Testplan](./07-beispielprojekt-focusflow/TESTPLAN.md)
- [FocusFlow Release und Betrieb](./07-beispielprojekt-focusflow/RELEASE-UND-BETRIEB.md)

## 8. Vorlagen

- [Vorlagenübersicht](./vorlagen/README.md)

## Empfohlene Reihenfolge

```text
Risikoprofil
→ PRD
→ Screen-Inventar
→ Architektur/ADR
→ Daten und Berechtigungen
→ sicherer vertikaler Slice
→ KI/Security/Datenschutz
→ Tests und Release-Gates
→ gestaffelter Launch
→ Betrieb
```
