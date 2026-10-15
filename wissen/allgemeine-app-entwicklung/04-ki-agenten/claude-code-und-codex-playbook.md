# Claude-Code- und Codex-Playbook

## Ziel

KI-Agenten sollen kleine, überprüfbare Änderungen ausführen. Sie dürfen weder Produktumfang noch Sicherheitsregeln unbemerkt neu definieren.

## Projektkontext

Im Repository sollten vorhanden sein:

```text
README.md
AGENTS.md oder CLAUDE.md
PRD.md
docs/architecture/
docs/data-model/
docs/design-system/
docs/security/
docs/privacy/
docs/testing/
docs/release/
```

## Verbindliche Agentenregeln

1. Vor Änderungen relevante Dokumente und bestehende Tests lesen.
2. Erst Plan, dann Patch.
3. Kleine, zusammenhängende Änderungseinheiten.
4. Keine Secrets oder personenbezogenen Daten ausgeben.
5. Keine Datenbankänderung ohne Migration.
6. Keine Autorisierung ausschließlich im Client.
7. Keine Abhängigkeit ohne Begründung, Lizenz- und Wartungsprüfung.
8. Keine Tests löschen oder lockern, nur damit CI grün wird.
9. Bestehende Geschäftslogik nicht still ändern.
10. Nach Änderungen Lint, Typen, Tests, Build und relevante E2E-Prüfung.
11. Migration und Rollback dokumentieren.
12. Unsicherheit ausdrücklich markieren.

## Auftragsschablone

```text
Ziel:
Konkretes Nutzerergebnis.

Nicht-Ziele:
Was unverändert bleiben muss.

Kontext:
Relevante Dateien, Entscheidungen und Einschränkungen.

Akzeptanzkriterien:
- ...
- ...

Security/Datenschutz:
- ...

Tests:
- ...

Ausgabe:
1. kurzer Plan
2. betroffene Dateien
3. Implementierung
4. Testresultate
5. Risiken
6. Rollback
```

## Arbeitsablauf

```text
Issue
→ Agent liest Kontext
→ Plan
→ menschliche Freigabe bei hohem Risiko
→ kleiner Patch
→ automatische Tests
→ visueller/fachlicher Review
→ Commit
→ nächstes Issue
```

## Aufgaben sinnvoll teilen

### Gute Einheit

„Füge dem bestehenden Projektformular einen validierten Titel mit 120-Zeichen-Limit hinzu, inklusive Migration/Constraint, UI-Fehlertext und Tests.“

### Schlechte Einheit

„Baue die gesamte App fertig und mach sie sicher.“

## Visuelle Umsetzung

Bei UI-Arbeit immer:

- echten Screen rendern;
- Referenz und Design Tokens vergleichen;
- kleine und große Viewports;
- Light/Dark Mode;
- Loading/Empty/Error/Success;
- Textskalierung;
- Tastatur und Fokus;
- Screenshot oder visuellen Regressionstest.

## Datenbankänderungen

Der Agent muss angeben:

- neue/änderte Tabellen und Spalten;
- Constraints und Indizes;
- Migration;
- Backfill;
- RLS/Grants;
- Testkonten;
- Auswirkung auf Export/Löschung;
- Rollback oder Roll-forward.

## Parallel arbeitende Agenten

Mehrere Agenten dürfen nur parallel arbeiten, wenn:

- Bereiche klar getrennt;
- keine gemeinsamen Migrationsdateien;
- keine identischen Komponenten;
- eine Integrationsreihenfolge besteht;
- eine Person Konflikte und Gesamtarchitektur prüft.

## Review-Fragen

- Erfüllt die Änderung exakt das Issue?
- Wurde Scope erfunden?
- Ist die Lösung einfacher möglich?
- Sind Rechte serverseitig geschützt?
- Gibt es neue Daten oder Anbieter?
- Sind Fehler- und Randfälle abgedeckt?
- Wurden echte Tests ausgeführt?
- Ist ein Rollback möglich?

## Definition of Done

- [ ] Akzeptanzkriterien erfüllt
- [ ] keine unbeabsichtigte Scope-Änderung
- [ ] Lint/Typen/Tests/Build erfolgreich
- [ ] visueller oder E2E-Nachweis
- [ ] Migration und RLS geprüft
- [ ] Security-/Datenschutzauswirkung dokumentiert
- [ ] Dokumentation aktualisiert
- [ ] Rollback oder Roll-forward beschrieben
