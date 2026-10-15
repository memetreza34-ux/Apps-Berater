# Qualitätssystem für produktionsreife Apps v1.1

Dieses System verhindert, dass eine optisch gute, aber unsichere oder unfertige App als fertig bezeichnet wird. Punkte werden nicht nach Gefühl vergeben, sondern anhand von überprüfbaren Belegen. Jeder vergebene Punkt braucht einen konkreten Nachweis.

## 1. Einheitliche Evidenzstufen

Jeder anwendbare Bereich erhält 0 bis 5 Punkte.

| Punkte | Objektiver Mindestnachweis |
|---:|---|
| 0 | fehlt oder unbekannt |
| 1 | Absicht/Idee dokumentiert, aber nicht belastbar umgesetzt |
| 2 | teilweise umgesetzt; wichtige Zustände, Risiken oder Belege fehlen |
| 3 | vollständig für den definierten Beta-Scope umgesetzt und manuell reproduzierbar geprüft |
| 4 | automatisiert oder wiederholbar getestet; Staging-/Gerätenachweis und dokumentierte Restrisiken vorhanden |
| 5 | Produktionsmessung über einen definierten Zeitraum, Regressionserkennung und unabhängige zweite Prüfperspektive bei kritischen Bereichen |

Ein Dokument allein rechtfertigt höchstens 1 Punkt. Ein grüner Test ohne passende Anforderung, negative Fälle und reale Umgebung rechtfertigt nicht automatisch 4 oder 5 Punkte.

## 2. Zulässige Belege

- Nutzerinterviews und Research-Protokolle;
- Figma-Prototyp und Usability-Testbericht;
- ADR, Datenmodell und Berechtigungsmatrix;
- Testcode und CI-Lauf;
- Build-/Store-Artefakt;
- Screenshot oder Video eines reproduzierbaren Ablaufs;
- RLS-/Autorisierungs-Negativtest;
- Performancebericht auf benanntem Gerät/Browser;
- Restore-/Rollback-Protokoll;
- Anbieter-, Datenschutz- oder Rechtsentscheidung mit Prüfdatum;
- Produktionsdashboard über definierten Zeitraum;
- Review durch zweite Person oder klar getrennte Review-Rolle.

Keine Secrets, produktiven personenbezogenen Daten oder unnötigen sensiblen Inhalte als Beleg committen.

## 3. Die zwölf Qualitätsbereiche

### 1. Problem und Produktnutzen

**Prüfung:**
- reale Problembelege statt hypothetischer Zustimmung;
- enger Kernnutzen und klare Nicht-Ziele;
- messbare Aktivierung und Retention;
- Kill-Kriterien.

**Für 4 Punkte mindestens:** validiertes PRD, dokumentierte Interviews, Beta-Metrik und Entscheidung anhand echter Nutzung.

### 2. UX und Verständlichkeit

**Prüfung:**
- kurzer Kernablauf;
- klare Informationsarchitektur;
- Loading, Empty, Error, Offline und Success;
- Nutzertest mit priorisierten Problemen.

**Für 4 Punkte mindestens:** getesteter Prototyp plus gerenderte App mit behobenen schweren UX-Problemen.

### 3. Visuelle Qualität

**Prüfung:**
- eigenes Designsystem und semantische Tokens;
- klare Hierarchie;
- responsive/adaptive Darstellung;
- reale Inhalte und konsistente Komponenten.

**Für 4 Punkte mindestens:** Komponentenbibliothek, Screenvergleich auf Zielgrößen und keine bekannten schweren Inkonsistenzen.

### 4. Accessibility

**Prüfung:**
- Screenreader-Namen und Fokusreihenfolge;
- Kontrast und Textskalierung;
- Touch-Ziele, Tastatur und Gestenalternativen;
- Reduced Motion.

**Für 4 Punkte mindestens:** automatisierte Baseline plus manuelle Prüfung auf den Zielplattformen mit dokumentierten Ergebnissen.

### 5. Architektur und Wartbarkeit

**Prüfung:**
- klare Module und Verantwortlichkeiten;
- ADRs;
- reproduzierbarer Build;
- Upgrade-, Anbieter- und Exit-Plan.

**Für 4 Punkte mindestens:** frischer Setup-Test, CI-Build und dokumentierter Migrations-/Rollbackweg.

### 6. Datenmodell und Autorisierung

**Prüfung:**
- Constraints und Indizes;
- Rollen-, Eigentümer- und Mandantentrennung;
- sichere Migrationen;
- negative Tests.

**Für 4 Punkte mindestens:** Nutzer-A/B-Tests für jede kritische Ressource, Stagingmigration und Prüfung von Tabellen, Views, Functions, Storage und Realtime, soweit verwendet.

### 7. Security

**Prüfung:**
- Threat Model;
- Auth, Secrets, Rate Limits und Uploadschutz;
- Abhängigkeiten und Supply Chain;
- Incident-Prozess.

**Für 4 Punkte mindestens:** automatisierte Scans, manuelle Angriffstests der Kernrisiken, Admin-MFA, getestetes Incident-Runbook und keine offenen kritischen Befunde.

### 8. Datenschutz und Recht

**Prüfung:**
- Dateninventar, Zwecke und Aufbewahrung;
- Anbieter, Transfers und Verträge;
- Export, Berichtigung und Löschung;
- Store-/Rechtstexte entsprechen der echten Technik.

**Für 4 Punkte mindestens:** vollständiger Datenflussabgleich, getestete Löschung über alle Systeme und aktuelle Quellen-/Entscheidungsnachweise.

### 9. Funktionale Qualität

**Prüfung:**
- Kernablauf vollständig;
- Grenz-, Fehler-, Offline- und Retryfälle;
- Geräte-, Versions- und Kontowechsel;
- keine Attrappen im Produktionspfad.

**Für 4 Punkte mindestens:** E2E-Kernablauf, Integrationsfehlerfälle und manuelle Prüfung eines Release-Builds.

### 10. Performance und Zuverlässigkeit

**Prüfung:**
- Budgets und echte Messungen;
- große Datenbestände und langsames Netz;
- Backup/Restore;
- SLOs, Monitoring und Rollback.

**Für 4 Punkte mindestens:** reproduzierbare Performanceprüfung, getesteter Restore und mindestens ein getesteter Alarm mit Runbook.

### 11. Monetarisierung und Kosten

**Prüfung:**
- ehrliche Preise und verständliche Bedingungen;
- serverseitige Entitlements;
- Webhook-/Zahlungszustände;
- Kostenlimits, Refunds und Support.

**Für 4 Punkte mindestens:** Sandbox-/Testkauf aller kritischen Zustände, serverseitige Verifikation und Kostenmodell bei realistischen Nutzerzahlen.

### 12. Betrieb und Verbesserung

**Prüfung:**
- Monitoring und Support;
- Wartungsrhythmus;
- Produkt- und Kostenmetriken;
- Incident-, Anbieter- und End-of-Life-Prozess.

**Für 4 Punkte mindestens:** Betriebsdashboard, verantwortliche Person, getestete Runbooks und dokumentierter monatlicher/vierteljährlicher Rhythmus.

## 4. Nicht anwendbare Bereiche

Ein Bereich darf nur als `N/A` markiert werden, wenn eine schriftliche Begründung zeigt, dass er tatsächlich nicht zutrifft. Beispiele:

- keine Monetarisierung und keine variablen kostenpflichtigen Funktionen;
- reine Offline-App ohne Konto und ohne personenbezogene Cloud-Daten;
- keine KI-Funktion.

Die Bewertung wird dann normalisiert:

```text
Qualitätsquote = erreichte Punkte / maximal anwendbare Punkte × 100
```

`N/A` darf keine versteckte Lücke ersetzen. Eine kostenlose App mit laufenden Cloudkosten benötigt weiterhin Kostenkontrolle.

## 5. Risikobasierte Mindestwerte

Unabhängig von der Gesamtquote gelten:

- Produktnutzen und funktionale Qualität: mindestens 4 für öffentlichen Release;
- Daten/Autorisierung und Security: mindestens 4 bei Konten, Cloud-Daten oder mehreren Rollen;
- Datenschutz/Recht: mindestens 4 bei personenbezogenen Daten;
- Monetarisierung: mindestens 4 bei Käufen, Abos oder Credits;
- KI: die betroffenen Bereiche benötigen mindestens 4 bei automatischen Aktionen oder erhöhtem Schadenspotenzial;
- Medizin, Finanzen, Minderjährige, Biometrie, Hardware oder kritische Infrastruktur: externe fachliche Freigabe entsprechend Risiko.

## 6. Blocker – kein Release unabhängig von Punkten

- fremder Datenzugriff oder unklare Mandantentrennung;
- möglicher Datenverlust ohne getestete Wiederherstellung;
- Secrets im Client, Repository oder Log;
- manipulierbare oder falsche Abrechnung;
- fehlende erforderliche Kontolöschung oder falsche Store-Angaben;
- kritischer Crash oder Datenfehler im Kernablauf;
- ungeklärte Hochrisiko-, Erlaubnis- oder Zulassungsfrage;
- irreführende Gesundheits-, Finanz-, KI- oder Abo-Aussagen;
- keine verantwortliche Person für Betrieb und Vorfälle.

## 7. Reifegrade

| Qualitätsquote | Reifegrad |
|---:|---|
| unter 50 % | Konzept/Prototyp |
| 50–69 % | Alpha |
| 70–82 % | Beta |
| 83–92 % | Release Candidate |
| über 92 % | sehr starker Produktionsstand |

Für einen öffentlichen Release werden mindestens **83 %**, alle risikobasierten Mindestwerte und kein Blocker verlangt. Für die interne Einstufung „9,5/10-Handbuchprozess vollständig angewendet“ werden über **92 %** sowie vollständige Evidenzlinks erwartet.

## 8. Definition of Done – Feature

Ein Feature ist fertig, wenn:

- Anforderung und Akzeptanzkriterien verlinkt;
- Design und alle anwendbaren Zustände umgesetzt;
- Accessibility geprüft;
- serverseitige Autorisierung vorhanden;
- Unit-/Integration-/E2E-Test passend zum Risiko;
- Fehler, Retry, Doppelaktion und Offline geklärt;
- Analytics nur bei begründetem Bedarf;
- Datenschutz-/Security-Auswirkung dokumentiert;
- Migration kompatibel oder mit Rollback;
- gerenderte App manuell geprüft;
- Dokumentation und Evidenz aktualisiert.

## 9. Definition of Done – Release

- alle Must-haves vollständig;
- kein kritischer oder ungeklärter hoher Befund;
- Datenexport und Kontolöschung Ende-zu-Ende getestet;
- Backup und Restore getestet;
- Storeangaben entsprechen den realen Datenflüssen;
- Zahlungszustände getestet, falls anwendbar;
- Performancebudget eingehalten;
- Kernmetriken, Kostenalarme und Runbooks aktiv;
- Review-/Supportkonten verfügbar;
- gestaffelter Rollout und Rollback bereit;
- Evidenzpaket vollständig;
- verantwortliche Person gibt Go.

## 10. Review-Rollen

Auch bei einem Einzelentwickler werden Rollen getrennt geprüft:

- Product Owner: Löst es das richtige Problem?
- Designer: Ist es verständlich und konsistent?
- Engineer: Ist es wartbar und korrekt?
- Security/Privacy Reviewer: Sind Daten und Rechte geschützt?
- QA: Funktionieren Grenz- und Fehlerfälle?
- Operator: Kann es überwacht und wiederhergestellt werden?

Claude Code oder Codex kann Reviews unterstützen, aber weder reale Tests noch die finale Verantwortung ersetzen.

## 11. Qualitätsprotokoll

```text
Version:
Datum:
Anwendbare Bereiche:
Punkte je Bereich:
Qualitätsquote:
Risikobasierte Mindestwerte erfüllt:
Blocker:
Akzeptierte Restrisiken:
Evidenzlinks:
Go/No-Go:
Verantwortlicher:
Zweite Prüfperspektive:
Nächste Neubewertung:
```
