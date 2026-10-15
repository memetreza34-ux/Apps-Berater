# 13 – Automatisierung und Qualitätsnachweise

Version 1.1 ergänzt das Handbuch um abhängigkeitsarme Prüfskripte und einen vorbereiteten GitHub-Actions-Workflow. Dadurch kann ein Teil der Qualität wiederholbar statt nur nach Gefühl geprüft werden.

## Lokale Prüfungen

Im Repository-Stamm:

```bash
python scripts/validate_handbook.py
python -m unittest discover -s scripts/tests -v
python -m unittest discover -s beispiel-apps/focusflow-pwa/tests -v
node --check beispiel-apps/focusflow-pwa/app.js
node --check beispiel-apps/focusflow-pwa/sw.js
node --check beispiel-apps/focusflow-supabase/rls-smoke.mjs
python scripts/check_external_links.py
```

## Vorbereiteter GitHub-Workflow

`.github/workflows/qualitaet.yml` enthält dieselben Prüfungen und einen HTTP-Smoke-Test.

Der Workflow ist momentan auf `workflow_dispatch` beschränkt. Bei der Erstellung von v1.1 scheiterte selbst ein minimaler Diagnosejob im verbundenen Repository vor dem ersten ausführbaren Schritt. Das spricht für eine GitHub-Actions-/Runner- oder Kontokonfiguration und nicht für einen konkreten fehlgeschlagenen Test.

Nach Behebung können wieder ergänzt werden:

```yaml
on:
  push:
    branches: [main]
  pull_request:
  schedule:
    - cron: "17 6 * * 1"
  workflow_dispatch:
```

## Geprüfte Bereiche des Workflows

1. Pflichtdateien und relative Links;
2. JSON- und PWA-Manifest;
3. Prüfdatum im Quellenregister;
4. sieben Freigabe-Gates;
5. Entscheidungsassistent und Klassifizierungsfälle;
6. FocusFlow-PWA-Struktur;
7. JavaScript-Syntax;
8. lokaler HTTP-Smoke-Test;
9. externe Links mit toleranter Behandlung von 401/403/429.

## Nachweis statt Behauptung

Jede Freigabeaussage benötigt einen Beleg.

| Aussage | Schwacher Nachweis | Belastbarer Nachweis |
|---|---|---|
| Login funktioniert | Entwickler sagt es | E2E-Test plus Testprotokoll |
| Daten sind getrennt | RLS ist aktiviert | negative Tests mit Nutzer A/B |
| Backup existiert | Anbieter zeigt Backup an | dokumentierter Restore-Test |
| App ist schnell | fühlt sich schnell an | Messung auf definierten Geräten |
| Löschung funktioniert | Auth-Account verschwindet | Audit über DB, Storage und Anbieter |
| KI ist sicher | Systemprompt vorhanden | Goldenset, Angriffstests und Kill Switch |
| Release ist freigegeben | Checkliste angekreuzt | verlinkte Test-, Build- und Betriebsbelege |

## Evidenzordner pro App

```text
evidence/
├── product/
├── design/
├── builds/
├── tests/
├── security/
├── privacy/
├── performance/
├── release/
└── operations/
```

Keine echten Secrets, Produktionsdaten oder unnötigen personenbezogenen Inhalte in Evidenzdateien speichern.

## Quellenpflege

Zeitabhängige Aussagen erhalten:

- Quellen-ID;
- Primärquelle;
- Prüfdatum;
- betroffene Kapitel;
- verantwortliche Person;
- nächstes Prüfdatum;
- Änderungsnotiz.

## Freigaberegel

Ein Haken ohne Beleg zählt nicht als bestanden. Bei jedem Release verweist das Produktionspaket auf konkrete Dateien, Testläufe, Screenshots, Messungen oder Freigaben.
