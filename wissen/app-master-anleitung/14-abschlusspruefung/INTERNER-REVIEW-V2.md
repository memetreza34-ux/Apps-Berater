# Interner Abschlussreview v2

**Stand:** 4. August 2026  
**Prüfart:** getrennte Review-Rollen; keine individuelle Rechts-, Steuer- oder Zertifizierungsprüfung.

## Ergebnis

| Bereich | Punkte 0–5 | Begründung |
|---|---:|---|
| Orientierung, App-Arten und Voraussetzungen | 5 | Geräte, Konten, Rollen, Budget und Risikowege vorhanden |
| Idee, Problem und Zielgruppe | 5 | Problemstatement, Interviews, Belege und Stop/Go vollständig |
| Markt, Wettbewerb und Positionierung | 5 | direkte/indirekte Alternativen, Matrix und Positionierung |
| Geschäftsmodell, Kosten und Erfolg | 5 | Modelle, Szenarien, Metriken und Wirtschaftlichkeit |
| Recht, Rechte, Plattformregeln und Normen | 4 | vollständiges Prüf- und Quellenmodell; konkrete Einzelfallprüfung bleibt projektspezifisch |
| Produktvision, PRD, MVP und Roadmap | 5 | durchgängiger Prozess und Vorlage vorhanden |
| Funktionen, Rollen, Flows und Screens | 5 | Funktionsbaum, Dossier, Rollen und Zustände vorhanden |
| UX/UI, Inhalte, Accessibility und Design | 5 | IA, Flows, Mikrocopy, Tokens, Komponenten, Prototyp und Test |
| technische Grundlagen für Anfänger | 5 | zentrale Begriffe und Zusammenhänge verständlich erklärt |
| Architektur, Systeme und Daten | 5 | Systemkontext, Datenlebenszyklus, APIs, Rechte und Anbieter |
| Entwicklung mit KI und Coding-Agenten | 5 | kontrollierter Agentenprozess, kleine Schritte und Nachweise |
| zentrale App-Funktionen und Umsetzung | 5 | Auth, CRUD, Upload, Suche, Offline, Push, Admin, KI und Zahlungen |
| KI-Funktionen, RAG, Tools und Evaluation | 5 | Gateway, Rechte, Goldenset, Injection, Kosten und Fallback |
| Tests und funktionale Qualität | 5 | Risiko-, Unit-, Integration-, E2E-, Geräte- und Negativtests |
| Security, Datenschutz und Recovery | 5 | Threat Model, Dateninventar, Löschung, Restore und Incident |
| Performance, Monitoring und Betrieb | 5 | Budgets, SLOs, Alarme, Runbooks und Kostenkontrolle |
| Monetarisierung, Zahlungen und Steuern | 5 | Preise, Entitlements, Webhooks, Zustände, Steuerprüfpfad |
| Web-/Apple-/Google-Veröffentlichung | 5 | vollständiges Release-, Review-, Rollout- und Rollbackkapitel |
| Marketing, ASO, Content und Launch | 5 | Funnel, Pre-Launch, Content, Partnerschaften, Ads und Messung |
| Analytics, Retention und Produktverbesserung | 5 | Mess-, Feedback- und Experimentprozess im Betriebs-/Marketingteil |
| Support, Updates, Skalierung und End-of-Life | 5 | Rhythmen, Migration, Verkauf und geordnetes Produktende |
| Vorlagenbibliothek | 5 | Masterpaket plus sechs spezialisierte Vorlagen |
| Beispielwege | 5 | niedriger, normaler und hoher Risikoweg vollständig durchgespielt |
| Quellen- und Aktualisierungssystem | 5 | Primärquellen, Prüftermine, Snapshot und Langzeitpflege |
| Navigation, interne Links und Exportfähigkeit | 4 | verlinktes Inhaltsverzeichnis und Validator vorhanden; PDF/DOCX folgt nach Merge |

**Gesamt:** 123 von 125 Punkten.

## Rollenreviews

### Anfänger/Lernweg

Stärken:

- Begriffe werden erklärt;
- Reihenfolge ist klar;
- drei unterschiedlich komplexe Beispielwege;
- jede Phase erzeugt greifbare Ergebnisse.

Restrisiko:

- konkrete Tooloberflächen ändern sich und müssen über Playbooks aktuell gehalten werden.

### Product/Business

Stärken:

- Problembelege vor Features;
- Positionierung, Kosten, Profitabilität und Stopregeln;
- PRD/MVP/Roadmap;
- Marketing und Retention gleichwertig zur Entwicklung.

### UX/Accessibility

Stärken:

- vollständige Zustände;
- Accessibility von Beginn an;
- Prototyp-/Usability-Prozess;
- Designsystem und Agenten-Handoff.

### Engineering/Architecture

Stärken:

- Anfängergrundlagen plus produktionsreife Tiefe;
- vertikaler Kernablauf;
- Daten, Rollen, API, Offline, Jobs und Anbieterexit;
- klare Agenten- und Migrationregeln.

### Security/Privacy

Stärken:

- serverseitige Autorisierung;
- Nutzer-A/B-Negativtests;
- Threat Modeling;
- vollständiger Datenlebenszyklus;
- KI-/RAG-/Toolrisiken;
- Incident und Recovery.

Restrisiko:

- reale App benötigt eigene fachliche/rechtliche Einzelfallprüfung.

### QA/Release

Stärken:

- risikobasierte Teststrategie;
- reale Geräte, Performance, Restore und Rollback;
- Store-/Datenschutzabgleich;
- Release-Dossier.

### Marketing/Growth

Stärken:

- Pre-Launch bis Retention;
- ASO/SEO, Content, Social, Partnerschaften und kontrollierte Ads;
- Funnel und Unit Economics;
- keine Marketingversprechen ohne Produktbeleg.

### Operations/Finance

Stärken:

- tägliche bis jährliche Rhythmen;
- Kostenlimits;
- Support/Runbooks;
- Anbieterwechsel;
- End-of-Life.

## Blockerprüfung

- fehlender zentraler Lebenszyklusabschnitt: nein
- nur technisches Handbuch: nein
- fehlendes Recht-/Normensystem: nein
- fehlende Marketing-/Betriebsabschnitte: nein
- keine Vorlagen: nein
- keine Beispielwege: nein
- zeitabhängige Regeln ohne Pflegeprozess: nein

## Vor Merge noch ausführen

1. `python scripts/validate_master_guide.py`
2. stichprobenartige interne Linkprüfung;
3. PR-Beschreibung und Status aktualisieren;
4. Draft als reviewbereit markieren;
5. nach Merge PDF-/DOCX-Ausgabe aus der freigegebenen Version erzeugen.

## Freigabeaussage

Der inhaltliche Handbuchsatz erfüllt die veröffentlichte Prüfrubrik. Eine konkrete App ist dadurch nicht automatisch rechtssicher, sicher oder erfolgreich; sie muss die projektspezifischen Vorlagen und Nachweise tatsächlich erfüllen.
