# App-Masterprozess – von 0 bis Release und Betrieb

Dieses Dokument ist die operative Reihenfolge. Es verbindet alle Kapitel zu einem ausführbaren Projektplan.

## Phase A – Idee und Risiko

### A1 Problemstatement
- Zielgruppe
- konkreter letzter Problemfall
- heutige Alternative
- Kosten/Frust/Häufigkeit
- gewünschtes messbares Ergebnis

### A2 Risikoprofil
- personenbezogene und besondere Daten
- KI
- Nutzerinhalte
- Minderjährige
- Gesundheit/Finanzen/Hardware
- Tracking und Werbung
- Rechte an Daten, Marke und Assets

### A3 Kill-Kriterien
Beispiele:
- weniger als fünf starke Problembelege;
- notwendige Daten/API nicht legal oder stabil verfügbar;
- variable Kosten übersteigen realistische Erlöse;
- Kernfunktion braucht ungeklärte Erlaubnis/Zulassung;
- kein verantwortlicher Betreiber.

**Output:** App-Risikoprofil und Stop/Go.

---

## Phase B – Produkt

### B1 Interviews und Konkurrenz
Nicht nur direkte Apps prüfen, sondern auch Excel, WhatsApp, Papier, Agenturen oder manuelle Workarounds.

### B2 PRD
- Ziele/Nicht-Ziele
- Rollen
- Kernablauf
- Must-have-Funktionen
- Datenobjekte
- nichtfunktionale Anforderungen
- Akzeptanzkriterien
- Metriken

### B3 MVP
Nur Funktionen, die Kernablauf, Sicherheit, Recht, Zahlung oder Lernbeweis ermöglichen.

**Output:** PRD, MVP-Backlog, Roadmap.

---

## Phase C – UX und Design

### C1 Informationsarchitektur
Inhalte und Funktionen gruppieren, bevor Navigation gestaltet wird.

### C2 User Flow
Für Registrierung, Kernfunktion, Fehler, Offline, Zahlung, Export, Löschung und Support.

### C3 Screen-Inventar
Jeder Screen mit Zweck, Daten, Aktionen, Zuständen, Berechtigungen, Accessibility und Test.

### C4 Prototyp und Nutzertest
Mindestens fünf passende Testpersonen für den Kernablauf; Probleme nach Schwere und Häufigkeit priorisieren.

### C5 Designsystem
Tokens, Komponenten, Zustände, Responsive, Dark Mode, Motion und Accessibility.

**Output:** getesteter Prototyp, Designsystem, Screen-Inventar.

---

## Phase D – Architektur und Daten

### D1 Plattformentscheidung
Web/PWA, React Native/Expo, Flutter oder Native anhand tatsächlicher Anforderungen.

### D2 Systemkontext
Client, Backend, Auth, DB, Storage, KI, Zahlung, E-Mail/Push, Analytics und Monitoring.

### D3 Datenmodell
- Primär-/Fremdschlüssel
- Constraints
- Indizes
- Eigentümer/Mandant
- Aufbewahrung und Löschung

### D4 Berechtigungen
Rolle × Ressource × Aktion. Keine Autorisierung nur im UI.

### D5 Qualitätsziele
Verfügbarkeit, Latenz, RPO, RTO, Kostenbudget, Supportzeitraum.

**Output:** ADRs, Diagramme, Datenmodell, Berechtigungsmatrix, Threat Model v1.

---

## Phase E – Repository und Entwicklungsbasis

### E1 Repository
- README
- Setup
- Architektur
- Contributing
- Security
- `.env.example`
- Branch-/Review-Regeln

### E2 Automatische Qualität
- Formatter/Lint
- Typecheck
- Unit-/Integrationstests
- Build
- Dependency-/Secret-Scan

### E3 Umgebungen
Dev, Staging, Production; getrennte Schlüssel und Daten.

### E4 Agentenregeln
Claude Code/Codex liest Pflichtdokumente, plant zuerst, arbeitet klein, testet und dokumentiert Migration/Rollback.

**Output:** reproduzierbarer leerer Produktionsrahmen.

---

## Phase F – Vertikaler Kernablauf

Baue nicht erst alle Screens und später das Backend. Baue einen vollständigen Pfad:

```text
Nutzeraktion
→ UI
→ Validierung
→ Auth/Autorisierung
→ API/DB
→ Erfolg/Fehler
→ Persistenz nach Neustart
→ Test und Monitoring
```

### Pflichtprüfungen
- Nutzer A kann Daten von B weder lesen noch ändern.
- abgelaufene Session.
- Netzwerkfehler und Retry.
- Doppel-Tap/Doppel-Request.
- App-Neustart.
- Löschung und Wiederherstellung.

**Output:** sicherer, getesteter vertikaler Slice.

---

## Phase G – Zusatzsysteme

Erst nach Kernablauf:
- KI/RAG/Agenten
- Zahlungen/Abos
- Push/E-Mail
- Uploads/Medien
- Realtime
- Analytics
- Adminbereich

Jedes Zusatzsystem benötigt eigenen Ausfall-, Kosten-, Datenschutz- und Missbrauchsplan.

---

## Phase H – Produktionsreife

### H1 Security
Threat Model, Auth, RLS, Secrets, Uploads, Rate Limits, Supply Chain, Admin-MFA.

### H2 Datenschutz
Dateninventar, Anbieter, Transfers, Consent, Export, Löschung, Breach-Prozess.

### H3 Accessibility
Screenreader, Fokus, Textgröße, Kontrast, Touch, Gesten, Reduced Motion.

### H4 Performance
Budgets, echte Geräte, langsames Netz, große Datenbestände.

### H5 Recovery
Backup/Restore, Migration, Rollback, Provider-Ausfall.

**Output:** Produktionsreifebericht ohne kritische offene Befunde.

---

## Phase I – Release

### I1 Store/Web-Abgleich
Beschreibung, Screenshots, Preise, Datenschutz, Data Safety/App Privacy, Altersfreigabe, Löschwege.

### I2 Release Candidate
Code Freeze, Version, Migration, Testkonten, Support, Statusseite, Rollback.

### I3 Gestaffelter Rollout
5 % → 20 % → 50 % → 100 %, nur bei stabilen Kernmetriken.

### I4 Go/No-Go
Blocker dürfen nicht als „später“ akzeptiert werden, wenn Datenverlust, fremder Zugriff, falsche Abrechnung oder fehlende Löschung drohen.

**Output:** signiertes Release-Dossier.

---

## Phase J – Betrieb

### Täglich
Crashes, Auth, Zahlung, Kernablauf, Kosten, Missbrauch.

### Wöchentlich
Supportmuster, Jobs/Webhooks, Reviews, Produktmetriken.

### Monatlich
Abhängigkeiten, Adminrechte, RLS, Löschjobs, Kosten, Backups.

### Quartalsweise
Restore-Test, Threat Model, Incident-Übung, Anbieterreview.

### Jährlich
Gesetze, Store-Regeln, Plattform-/API-Support, Verträge, End-of-Life, Gesamtqualität.

---

## Phase K – Verbesserung

Jede Verbesserung folgt:

```text
Beobachtung
→ Hypothese
→ kleinstes Experiment
→ Messung
→ Entscheidung
→ Dokumentation
```

Keine Funktionsmenge mit Qualität verwechseln. Oft wird eine App besser, wenn Abläufe kürzer, verständlicher und zuverlässiger werden.

## Endzustand

Eine App ist nicht „für immer fertig“. Version 1.0 des Produkts ist fertig, wenn der definierte Nutzen sicher, verständlich und wirtschaftlich betreibbar geliefert wird. Danach beginnt kontrollierte Produktpflege.
