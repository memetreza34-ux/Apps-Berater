# Start hier – Allgemeine App-Entwicklung v1.0

**Stand:** 4. August 2026  
**Zweck:** Eine App von der Idee bis zum stabilen Betrieb führen, ohne zentrale Produkt-, Design-, Technik-, Sicherheits-, Rechts- oder Release-Schritte zu überspringen.

## Wichtige Wahrheit

Kein Dokument garantiert eine perfekte App. Eine sehr gute App entsteht durch einen klaren Prozess, echte Nutzertests, kleine Releases, Messdaten, Fehlerbehebung und laufende Verbesserung. Dieses Handbuch soll die Wahrscheinlichkeit schwerer Fehler stark reduzieren.

## Der vollständige Weg

```text
0. Risikoprofil
1. Problem und Zielgruppe belegen
2. MVP und PRD festlegen
3. User Flow und Screen-Inventar
4. Designsystem und Prototyp
5. Plattform und Architektur entscheiden
6. Datenmodell, Rollen und Berechtigungen
7. sicheren vertikalen Kernablauf bauen
8. KI, Zahlungen und Drittanbieter kontrolliert ergänzen
9. Security, Datenschutz und Sonderrecht prüfen
10. Unit-, Integrations-, E2E-, Accessibility- und Recovery-Tests
11. Store-/Web-Release vorbereiten
12. gestaffelt veröffentlichen
13. Monitoring, Support, Updates und Skalierung
14. jährliche Gesamtprüfung
15. geordnetes Produktende vorbereiten
```

## Sechs Freigabe-Gates

| Gate | Frage | Pflichtnachweis |
|---|---|---|
| 0 – Risiko | Darf und kann die App sinnvoll gebaut werden? | Risikoprofil, Rechte, Regulierungsentscheidung |
| 1 – Produkt | Löst sie ein echtes, häufiges Problem? | Nutzerbelege, PRD, MVP, Kill-Kriterien |
| 2 – Design/Architektur | Ist der Ablauf verständlich und technisch tragfähig? | Prototyp, Designsystem, ADRs, Datenmodell |
| 3 – Sicherer Kern | Funktioniert ein kompletter Ablauf mit echten Daten? | vertikaler Slice, RLS-/Autorisierungstests |
| 4 – Produktionsreife | Ist die App sicher, testbar und betreibbar? | Testbericht, Löschung, Backup/Restore, Monitoring |
| 5 – Release | Stimmen Produkt, Store, Datenschutz und Rollback überein? | Release-Dossier und Go/No-Go |
| 6 – Betrieb | Kann die App über Jahre gepflegt werden? | SLOs, Support, Wartungs- und End-of-Life-Plan |

## Pflichtdateien pro App

1. `APP-RISIKOPROFIL.md`
2. `PRD.md`
3. `SCREEN-INVENTAR.md`
4. `DESIGN-SYSTEM.md`
5. `ARCHITEKTUR-ADRS.md`
6. `DATENMODELL.md`
7. `BERECHTIGUNGSMATRIX.md`
8. `THREAT-MODEL.md`
9. `DATENINVENTAR-UND-LOESCHUNG.md`
10. `TESTPLAN.md`
11. `RELEASE-DOSSIER.md`
12. `BETRIEBSHANDBUCH.md`

## Reihenfolge beim Bauen mit Claude Code oder Codex

1. Agent liest alle Pflichtdateien.
2. Agent erstellt nur einen Plan.
3. Mensch prüft Scope, Datenmodell und Risiken.
4. Agent setzt einen kleinen vertikalen Schritt um.
5. Lint, Typen, Tests, Build und Screenshotprüfung.
6. Negative Berechtigungs- und Fehlerfälle.
7. Commit mit klarer Änderung.
8. Erst danach nächster Schritt.

## Qualitätsziel

Eine App ist für den ersten echten Release geeignet, wenn:

- der Kernnutzen in kurzer Zeit erreichbar ist;
- keine kritische Funktion nur als Attrappe existiert;
- fremde Nutzer- und Mandantendaten technisch getrennt sind;
- Fehler-, Lade-, Leer- und Offlinezustände vorhanden sind;
- Konten, Datenexport und Löschung vollständig funktionieren;
- Store- und Datenschutzerklärungen der realen Technik entsprechen;
- kritische Abläufe automatisch getestet werden;
- Monitoring und Rollback eingerichtet sind;
- Support und Wartung finanziell und organisatorisch möglich sind.

## Nächster Schritt

Beginne mit `00-start/entscheidungsweg.md` und kopiere danach die Vorlagen in das Repository deiner konkreten App.
