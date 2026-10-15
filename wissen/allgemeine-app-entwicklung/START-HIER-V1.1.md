# Start hier – Allgemeine App-Entwicklung v1.1

**Stand:** 4. August 2026  
**Zweck:** Eine App von der Idee bis zum stabilen Betrieb führen und jede wichtige Freigabe mit überprüfbaren Belegen absichern.

## Wichtige Wahrheit

Kein Dokument garantiert eine perfekte App. Version 1.1 verbindet deshalb Anleitung, ausführbare Beispiele, automatisierte Prüfungen, objektivere Evidenzstufen und Betriebs-Runbooks. Qualität wird nicht nur behauptet, sondern nachgewiesen.

## Schnellstart

```text
1. Entscheidungsassistent ausführen
2. App-Risikoprofil und PRD ausfüllen
3. Produktionspaket kopieren
4. Plattform- und Designentscheidungen belegen
5. sicheren vertikalen Kernablauf bauen
6. Evidenzmatrix während der Entwicklung pflegen
7. Qualitätssystem und Release-Checkliste anwenden
8. gestaffelt veröffentlichen und Runbooks testen
```

### Entscheidungsassistent

```bash
python scripts/app_decision_assistant.py
```

Er erzeugt projektspezifische Pflichtmodule, Artefakte und Themen, die vor der Kernentwicklung geklärt werden müssen.

## Vollständiger Weg

```text
0. Risikoprofil und Rechte
1. Problem und Zielgruppe belegen
2. MVP, Nicht-Ziele und PRD
3. User Flow und Screen-Inventar
4. Designsystem, Prototyp und Nutzertest
5. Plattform und Architektur
6. Datenmodell, Rollen und Berechtigungen
7. sicherer vertikaler Kernablauf
8. KI, Zahlungen und Drittanbieter kontrolliert ergänzen
9. Security, Datenschutz und Sonderrecht
10. funktionale, negative, Accessibility-, Performance- und Recovery-Tests
11. Store-/Web-Abgleich und Release-Dossier
12. gestaffelter Rollout
13. Monitoring, Support, Kosten und Runbooks
14. regelmäßige Gesamtprüfung
15. geordnetes Produktende
```

## Sieben Freigabe-Gates

| Gate | Frage | Pflichtnachweis |
|---|---|---|
| 0 – Risiko | Darf und kann die App sinnvoll gebaut werden? | Risikoprofil, Rechte, Regulierungsentscheidung |
| 1 – Produkt | Löst sie ein echtes und ausreichend wichtiges Problem? | Nutzerbelege, PRD, MVP, Kill-Kriterien |
| 2 – Design/Architektur | Ist der Ablauf verständlich und technisch tragfähig? | getesteter Prototyp, Designsystem, ADRs, Datenmodell |
| 3 – Sicherer Kern | Funktioniert ein kompletter Ablauf mit echten Daten? | vertikaler Slice, negative Autorisierungs- und Fehlerfälle |
| 4 – Produktionsreife | Ist die App sicher, zugänglich, performant und wiederherstellbar? | Testbericht, Löschung, Restore, Monitoring, Evidenzmatrix |
| 5 – Release | Stimmen Produkt, Store, Datenschutz und Rollback überein? | Release-Dossier, Qualitätsquote und Go/No-Go |
| 6 – Betrieb | Kann die App über Jahre gepflegt und bei Vorfällen kontrolliert werden? | SLOs, Kostenlimits, Support, Runbooks und End-of-Life-Plan |

## Pflichtdateien pro normaler Account-App

1. `APP-RISIKOPROFIL.md`
2. `APP-ENTSCHEIDUNG.md`
3. `PRD.md`
4. `SCREEN-INVENTAR.md`
5. `DESIGN-SYSTEM.md`
6. `ARCHITEKTUR-ADRS.md`
7. `DATENMODELL.md`
8. `BERECHTIGUNGSMATRIX.md`
9. `THREAT-MODEL.md`
10. `DATENINVENTAR-UND-LOESCHUNG.md`
11. `TESTPLAN.md`
12. `EVIDENZ-MATRIX.md`
13. `RELEASE-DOSSIER.md`
14. `BETRIEBSHANDBUCH.md`

Der Entscheidungsassistent ergänzt weitere Dateien für KI, Zahlungen, Minderjährige, Communities, Hardware oder andere Sonderfälle.

## Reihenfolge mit Claude Code oder Codex

1. Agent liest alle Pflichtdateien.
2. Agent nennt Blocker und erstellt nur einen Plan.
3. Mensch prüft Scope, Datenmodell, Rechte und Risiken.
4. Agent setzt einen kleinen vertikalen Schritt um.
5. Lint, Typen, Tests, Build und gerenderte Prüfung.
6. Negative Berechtigungs-, Fehler-, Offline- und Doppelaktionsfälle.
7. Evidenzmatrix und Dokumentation aktualisieren.
8. Kleiner Commit; erst danach nächster Schritt.

Nutze `12-agenten-masterprompt/CLAUDE-CODE-APP-MASTERPROMPT.md` als verbindliche Arbeitsgrundlage.

## Qualitätsziel

Für einen öffentlichen Release:

- mindestens 83 % der anwendbaren Qualitätspunkte;
- risikobasierte Mindestwerte erfüllt;
- kein Blocker;
- Kernnutzen und Funktion mindestens Evidenzstufe 4;
- Datenrechte, Security und Datenschutz mindestens Stufe 4, sofern anwendbar;
- Export, Löschung, Restore und Rollback praktisch getestet;
- Store-/Datenschutzangaben entsprechen der realen Technik;
- Alarme, Kostenlimits und Runbooks funktionieren.

Über 92 % mit vollständigen Evidenzlinks entspricht einem sehr starken Produktionsprozess. Die Punktzahl ersetzt keine fachliche Zulassungs- oder Rechtsprüfung bei Hochrisiko-Apps.

## Direkt ausprobieren

Die ausführbare FocusFlow-PWA liegt unter:

```text
beispiel-apps/focusflow-pwa/
```

Start:

```bash
cd beispiel-apps/focusflow-pwa
python -m http.server 4173
```

## Automatische Prüfung

```bash
python scripts/validate_handbook.py
python -m unittest discover -s scripts/tests -v
python -m unittest discover -s beispiel-apps/focusflow-pwa/tests -v
```

Die GitHub-Action führt diese Prüfungen bei Push und Pull Request aus und kontrolliert zusätzlich Markdown-Links.

## Nächster Schritt

Führe den Entscheidungsassistenten aus und kopiere anschließend `vorlagen/produktionspaket-v1.md` sowie `vorlagen/evidenz-matrix.md` in das Repository deiner konkreten App.
