# Inhaltsverzeichnis – Allgemeine App-Entwicklung v1.1

## Start

1. [Start hier v1.1](./START-HIER-V1.1.md)
2. [Entscheidungsweg](./00-start/entscheidungsweg.md)
3. [Interaktiver Entscheidungsassistent](./00-start/entscheidungsassistent.md)
4. [Quellen- und Rechtsstand](./QUELLEN-UND-RECHTSSTAND.md)
5. [Status v1.1](./STATUS-V1.1.md)

## Kernhandbuch

### 01 – Produkt
- [Produkt, MVP und PRD](./01-produkt/README.md)

### 02 – UX/UI und Design
- [UX, UI und Designsystem](./02-design/README.md)
- [Figma- und Mobbin-Workflow](./02-design/figma-und-mobbin-workflow.md)
- [Maschinenlesbare FocusFlow Design Tokens](./02-design/beispiele/focusflow-design-tokens.json)
- [FocusFlow Komponentenvertrag](./02-design/beispiele/focusflow-komponentenvertrag.md)

### 03 – Architektur, Backend und Supabase
- [Technische Basis](./03-technik/README.md)
- [Supabase-Produktionsleitfaden](./03-technik/supabase-produktionsleitfaden.md)

### 04 – Claude Code, Codex und KI
- [KI und Agenten](./04-ki-agenten/README.md)
- [KI-Produktionsleitfaden](./04-ki-agenten/ki-produktionsleitfaden.md)

### 05 – Security, Datenschutz und Recht
- [Security, Datenschutz und Recht](./05-sicherheit-datenschutz-recht/README.md)

### 06 – Tests, Release und Betrieb
- [Tests, Release und langfristiger Betrieb](./06-tests-release-betrieb/README.md)
- [Release-Checkliste](./CHECKLISTE-VOR-JEDEM-RELEASE.md)

### 07 – Plattformwahl
- [Plattformwahl und technische Basis](./07-plattformen/README.md)

### 08 – Zahlungen
- [Zahlungen, Abos und Entitlements](./08-zahlungen-und-abos/README.md)

### 09 – Performance und Observability
- [Performance, Analytics und Observability](./09-performance-analytics-betrieb/README.md)

### 10 – Sonderfälle
- [Medizin, Finanzen, Minderjährige, Community, Biometrie, Hardware und Enterprise](./10-sonderfaelle/README.md)

### 11 – Masterprozess und Qualität
- [App von 0 bis Release und Betrieb](./11-masterprozess/APP-VON-0-BIS-RELEASE.md)
- [Evidenzbasiertes Qualitätssystem](./11-masterprozess/QUALITAETSSYSTEM.md)

### 12 – Agenten-Masterprompt
- [Claude-Code-/Codex-Masterprompt](./12-agenten-masterprompt/CLAUDE-CODE-APP-MASTERPROMPT.md)

### 13 – Automatisierung
- [Automatisierung und Qualitätsnachweise](./13-automatisierung/README.md)
- [Web-TypeScript-CI-Vorlage](./13-automatisierung/ci-templates/web-typescript.yml.example)
- [Mobile-TypeScript-CI-Vorlage](./13-automatisierung/ci-templates/mobile-typescript.yml.example)

### 14 – Plattform-Playbooks
- [Übersicht](./14-plattform-playbooks/README.md)
- [Web und PWA](./14-plattform-playbooks/web-pwa.md)
- [React Native und Expo](./14-plattform-playbooks/react-native-expo.md)
- [Flutter und Native](./14-plattform-playbooks/flutter-und-native.md)

### 15 – Runbooks
- [Runbook-Übersicht](./15-runbooks/README.md)
- [Auth-Ausfall](./15-runbooks/auth-ausfall.md)
- [Datenbankmigration und Rollback](./15-runbooks/datenbankmigration-und-rollback.md)
- [KI-Anbieter-Ausfall](./15-runbooks/ki-anbieter-ausfall.md)
- [Security- und Datenschutzvorfall](./15-runbooks/security-und-datenschutzvorfall.md)

## Vorlagen

- [Vorlagenübersicht](./vorlagen/README.md)
- [App-Risikoprofil](./vorlagen/app-risikoprofil.md)
- [PRD](./vorlagen/prd.md)
- [Produktionspaket](./vorlagen/produktionspaket-v1.md)
- [Evidenz-Matrix](./vorlagen/evidenz-matrix.md)
- [Plattform- und Gerätetestmatrix](./vorlagen/plattform-testmatrix.md)

## Ausführbare Referenz

- [FocusFlow PWA – Start und Grenzen](../../beispiel-apps/focusflow-pwa/README.md)
- [App-Oberfläche](../../beispiel-apps/focusflow-pwa/index.html)
- [Design Tokens/CSS](../../beispiel-apps/focusflow-pwa/styles.css)
- [Kernlogik](../../beispiel-apps/focusflow-pwa/app.js)
- [Offline Service Worker](../../beispiel-apps/focusflow-pwa/sw.js)
- [Automatische Strukturtests](../../beispiel-apps/focusflow-pwa/tests/test_static.py)

## Repository-Automatisierung

- [Handbook-GitHub-Action](../../.github/workflows/qualitaet.yml)
- [Handbook-Validator](../../scripts/validate_handbook.py)
- [Entscheidungsassistent](../../scripts/app_decision_assistant.py)
- [Assistententests](../../scripts/tests/test_app_decision_assistant.py)
