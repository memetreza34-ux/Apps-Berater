# Allgemeine App-Entwicklung – von der Idee bis zum langfristigen Betrieb

**Status:** Version 1.1 – evidenzbasierter Produktionsleitfaden  
**Stand:** 4. August 2026

Dieses Handbuch führt eine App von der Idee über Produkt, UX/UI, Architektur, Claude Code/Codex, Supabase, KI, Security, Datenschutz, Tests und Stores bis zu Monitoring, Skalierung und Produktende. Version 1.1 ergänzt ausführbare Beispiele, Automatisierung, objektivere Qualitätsnachweise, Plattform-Playbooks und Betriebs-Runbooks.

## Direkt starten

1. [Start hier – v1.1](./START-HIER-V1.1.md)
2. [Interaktiver Entscheidungsassistent](./00-start/entscheidungsassistent.md)
3. [Inhaltsverzeichnis v1.1](./INHALTSVERZEICHNIS-V1.1.md)
4. [App-Masterprozess](./11-masterprozess/APP-VON-0-BIS-RELEASE.md)
5. [Produktionspaket](./vorlagen/produktionspaket-v1.md)
6. [Evidenz-Matrix](./vorlagen/evidenz-matrix.md)
7. [Claude-Code-/Codex-Masterprompt](./12-agenten-masterprompt/CLAUDE-CODE-APP-MASTERPROMPT.md)
8. [Release-Checkliste](./CHECKLISTE-VOR-JEDEM-RELEASE.md)
9. [Qualitätssystem v1.1](./11-masterprozess/QUALITAETSSYSTEM.md)
10. [Ausführbare FocusFlow-PWA](../../beispiel-apps/focusflow-pwa/README.md)

## Enthaltene Bereiche

- Risiko- und Stop/Go-Prüfung
- interaktiver Assistent für Pflichtmodule, Artefakte und Eskalationen
- Produktvalidierung, MVP und PRD
- User Flows, Screen-Inventar, Figma/Mobbin und Designsystem
- maschinenlesbare Design Tokens und Komponentenverträge
- Plattformwahl sowie konkrete Web/PWA-, Expo-, Flutter- und Native-Playbooks
- Architektur, Datenmodell, Supabase, RLS, Auth, Storage und Realtime
- Claude Code, Codex, Context Engineering und sichere Agentenarbeit
- KI, RAG, Embeddings, Caching, Guardrails und Evaluation
- Zahlungen, Abos, Entitlements, Webhooks und Erstattungsfälle
- Security, Threat Modeling, Datenschutz, Export und Kontolöschung
- EU-/Deutschland- und Store-Prüfpfade
- Unit-, Integrations-, E2E-, Accessibility-, Performance- und Recovery-Tests
- Performancebudgets, Analytics, Observability, SLOs und Kostenkontrolle
- App Store, Google Play, Web-Release, Rollout und Rollback
- fünfjähriger Betrieb, Skalierung und End-of-Life
- Sonderfälle: Medizin, Finanzen, Minderjährige, Community, Biometrie und Hardware
- ausfüllbare Vorlagen, Evidenzsystem und FocusFlow-Beispielprojekt
- direkt startbare Referenz-PWA mit lokalen Daten, Export, Löschung und Offline-App-Shell
- vorbereitete Struktur-, Test-, JavaScript-, HTTP- und Linkprüfung
- Runbooks für Auth, Datenbankmigration, KI-Ausfall sowie Security-/Datenschutzvorfälle

## Zentrale Regel

> Erst einen vollständigen, sicheren und messbaren Kernablauf bauen. Danach zusätzliche Funktionen ergänzen. Jede Freigabe benötigt einen konkreten Beleg.

## Was „fertig“ bedeutet

Das allgemeine Handbuch v1.1 ist eine vollständige Arbeitsgrundlage. Eine konkrete App ist erst fertig, wenn ihre projektspezifischen Artefakte ausgefüllt, Risiken geprüft, Funktionen implementiert und die Evidenz aus Tests, Geräten, Store-Abgleich, Restore, Rollback und Betrieb erbracht wurde.

## Qualitätsmaßstab

- mindestens 83 % der anwendbaren Qualitätspunkte für öffentlichen Release;
- risikobasierte Mindestwerte;
- kein Blocker;
- über 92 % plus vollständige Evidenzlinks für einen sehr starken Produktionsprozess;
- Hochrisikobereiche benötigen zusätzliche fachliche Freigabe.

## Grenzen

Kein Handbuch garantiert eine perfekte App oder ersetzt Nutzerfeedback, technische Reviews, echte Gerätetests oder fachkundige Rechts-/Zulassungsprüfung. Die neue Referenz-App beweist einen ausführbaren UI-Kernablauf, ist aber bewusst keine vollständige produktive Cloud-App.

## Qualitätsprüfung

```bash
python scripts/validate_handbook.py
python -m unittest discover -s scripts/tests -v
python -m unittest discover -s beispiel-apps/focusflow-pwa/tests -v
node --check beispiel-apps/focusflow-pwa/app.js
node --check beispiel-apps/focusflow-pwa/sw.js
node --check beispiel-apps/focusflow-supabase/rls-smoke.mjs
```

Der GitHub-Workflow ist vollständig vorbereitet, bleibt wegen eines Runner-/Kontoproblems des Repositorys momentan manuell. Selbst ein Einzeilen-Diagnosejob scheiterte vor dem ersten ausführbaren Schritt. Details stehen im [Automatisierungskapitel](./13-automatisierung/README.md).

## Aktualität

Technische, rechtliche und Store-bezogene Aussagen werden im [Quellen- und Rechtsstandsregister](./QUELLEN-UND-RECHTSSTAND.md) mit Prüfdatum geführt. Die Markdown-Dateien im Repository sind die aktuelle Hauptversion; spätere PDF-/DOCX-Ausgaben sind versionierte Momentaufnahmen.
