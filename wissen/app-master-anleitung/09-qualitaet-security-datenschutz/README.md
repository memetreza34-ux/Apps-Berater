# Produktionsreife: Tests, Accessibility, Security, Datenschutz, Performance und Recovery

Dieses Kapitel bestimmt, wann eine App nicht nur „funktioniert“, sondern verantwortbar veröffentlicht und betrieben werden kann.

## Ziel

Vor Release liegen belastbare Nachweise vor für:

- funktionale Qualität;
- Accessibility;
- Autorisierung und Security;
- Datenschutz und Datenrechte;
- Performance und Zuverlässigkeit;
- Backup, Restore und Rollback;
- Monitoring und Incident-Reaktion;
- Store-/Produktabgleich.

## 1. Risikobasierte Teststrategie

Nicht jede Funktion benötigt dieselbe Testtiefe.

Höhere Tiefe bei:

- Authentifizierung und Konten;
- Berechtigungen und Mandantentrennung;
- Zahlungen;
- Löschung und Export;
- Gesundheits-/Finanzfunktionen;
- Minderjährigen;
- KI-Aktionen;
- Hardware oder physischen Folgen;
- Admin- und Moderationsfunktionen.

Für jede Funktion dokumentieren:

| Risiko | möglicher Schaden | Testebenen | Zielumgebung | Nachweis | Verantwortlicher |
|---|---|---|---|---|---|
| | | | | | |

## 2. Testebenen

### Unit-Tests

Einzelne Regeln, Parser, Berechnungen und Zustandsübergänge.

### Integrationstests

Zusammenspiel mit Datenbank, API, Auth, Storage, Queue oder Drittanbieter.

### E2E-Tests

Kernablauf aus Nutzersicht über mehrere Schichten.

### Manuelle Tests

Visuelle Qualität, Gerätebesonderheiten, Screenreader, reale Store-Builds und komplexe Explorationsfälle.

### Vertragstests

API-Schemas und Erwartungen zwischen Systemen.

### Recovery-Tests

Backup, Restore, Migration, Rollback und Anbieter-Ausfall.

## 3. Pflichtfälle

Für jeden Kernablauf:

- Erfolg;
- ungültige Eingabe;
- leere Daten;
- fehlende Berechtigung;
- abgelaufene Session;
- Netzwerkfehler;
- Timeout;
- Retry;
- Doppelaktion;
- App-/Browserneustart;
- anderes Gerät;
- große Datenmenge;
- Löschung;
- Wiederherstellung entsprechend Produktregel.

## 4. Zwei-Nutzer- und Rollen-Negativtests

Mindestens zwei echte Testkonten verwenden.

Prüfen:

- Nutzer A kann Daten von B nicht lesen;
- A kann Daten von B nicht ändern oder löschen;
- Rollenwechsel wird sofort wirksam;
- Team-/Mandantenwechsel vermischt keine Daten;
- Support/Admin sieht nur erlaubte Daten;
- direkte API-/DB-Anfrage umgeht UI nicht;
- Export enthält nur berechtigte Daten.

## 5. Accessibility-Prüfung

Automatisierte Baseline plus manuelle Prüfung.

Prüfen:

- semantische Überschriften/Elemente;
- Screenreader-Namen;
- Fokus sichtbar und logisch;
- Tastatur vollständig;
- Textskalierung;
- Kontrast;
- Touch-Ziele;
- Gestenalternativen;
- Reduced Motion;
- Statusmeldungen;
- Formfehler;
- Untertitel/Transkripte;
- Zoom und Reflow;
- Plattformhilfen.

Ergebnisse mit Gerät, Betriebssystem, Browser/App-Version und Schweregrad dokumentieren.

## 6. Security-Grundprüfung

Mindestens:

- Threat Model;
- sichere Authentifizierung;
- serverseitige Autorisierung;
- minimale Rechte;
- Admin-MFA;
- Secret-Management;
- Eingabevalidierung;
- Rate Limits;
- Uploadschutz;
- sichere Redirects/Deep Links;
- Dependency-/Supply-Chain-Prüfung;
- Logging ohne Secrets;
- sichere Fehlerantworten;
- Schutz vor Missbrauch und Automatisierung;
- Incident-Kontakte.

## 7. Threat Modeling

Für jeden sensiblen Datenfluss:

```text
Asset
→ Angreifer/Missbraucher
→ Einstiegspunkt
→ Bedrohung
→ Auswirkung
→ Kontrolle
→ Erkennung
→ Reaktion
→ Test
→ Restrisiko
```

Nicht nur externe Hacker betrachten:

- missbräuchlicher Nutzer;
- kompromittiertes Konto;
- fehlerhafte Adminaktion;
- bösartiger Upload;
- unsicherer Anbieter;
- falsch konfigurierte Datenbank;
- Prompt Injection;
- Insider/Supportrolle;
- verlorenes Gerät.

## 8. Datenschutz und Dateninventar

Für jede Datenart:

| Datenart | Zweck | Grundlage/Entscheidung | Quelle | Empfänger | Speicherorte | Dauer | Export | Löschung | Risiko |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

Zusätzlich:

- Datenminimierung;
- Drittanbieter;
- Transfers/Region;
- Consent und Widerruf;
- Logs;
- Analytics;
- KI-Eingaben/Ausgaben;
- Embeddings;
- Backups;
- Testdaten;
- Supportdaten.

## 9. Export, Berichtigung und Löschung

Ende zu Ende testen:

- Identitätsprüfung;
- Exportformat;
- vollständige Datenquellen;
- verständliche Inhalte;
- Berichtigung;
- Auth-Konto;
- Datenbank;
- Storage;
- Suchindex;
- KI-/Vektorsysteme;
- Analytics/CRM, soweit betroffen;
- Anbieter;
- Backups nach dokumentierter Regel;
- aktive Abos getrennt behandeln;
- Audit ohne unnötige Daten.

## 10. Tracking und Analytics

Nur Ereignisse erfassen, die Entscheidungen unterstützen.

Für jedes Event:

- Produktfrage;
- Auslöser;
- Eigenschaften;
- Identifikatoren;
- Zweck/Grundlage;
- Aufbewahrung;
- Zugriff;
- Widerruf/Opt-out;
- Löschung;
- Dashboard-Verantwortlicher.

Keine Passwörter, Tokens, vollständigen sensiblen Inhalte oder unnötigen KI-Prompts erfassen.

## 11. KI-Sicherheit und Evaluation

Testset enthält:

- typische Fälle;
- schwierige zulässige Fälle;
- unvollständige/widersprüchliche Eingaben;
- Halluzinationen;
- unbelegte Aussagen;
- Prompt Injection;
- Datenexfiltration;
- unerlaubte Tool-Aktionen;
- Rechteverletzung im RAG;
- Kosten-/Latenzspitzen;
- Modell-/Promptwechsel;
- Fallback.

Metriken:

- Aufgaben-Erfolg;
- Schema-Gültigkeit;
- fachliche Fehler;
- Sicherheitsverstöße;
- Quellenqualität;
- Latenz;
- Kosten pro erfolgreichem Ergebnis;
- menschliche Eskalationen.

## 12. Performance

Vorher Budgets definieren:

- Zeit bis nutzbarer Screen;
- Reaktionszeit auf Interaktion;
- Navigation;
- API p50/p95;
- Bild-/Bundle-Größe;
- Speicher;
- Akku/Netz;
- KI-Zeit bis erstes Ergebnis;
- Syncdauer;
- Datenbankabfragen.

Testen auf:

- schwächerem Zielgerät;
- langsamem Netz;
- großen Datenbeständen;
- kaltem Start;
- Hintergrund/Wiederaufnahme;
- Offline/Sync;
- mehreren Konten/Rollen.

## 13. Zuverlässigkeit und SLOs

Beispiele:

- erfolgreicher Kernablauf;
- Auth-Erfolg;
- Zahlungswebhook-Verarbeitung;
- Löschjob innerhalb definierter Frist;
- API-Latenz;
- Crashfreie Sitzungen;
- Alarmreaktionszeit.

SLOs müssen zum Produkt und Risiko passen.

## 14. Backup und Restore

Dokumentieren:

- welche Systeme gesichert werden;
- Frequenz;
- Verschlüsselung;
- Aufbewahrung;
- RPO;
- RTO;
- Verantwortlicher;
- Wiederherstellungsreihenfolge;
- letzter Restore-Test;
- bekannte Lücken.

Restore in isolierter Umgebung testen.

## 15. Migration und Rollback

Vor Release:

- Schemaänderung in Staging;
- Backfill;
- Kompatibilität alt/neu;
- Feature Flag;
- Monitoring;
- Rollback-/Roll-forward-Plan;
- Datenverlustanalyse;
- Zeitfenster und Verantwortliche.

## 16. Monitoring und Alarme

Sichtbar machen:

- Crashes;
- Authfehler;
- API-Fehler;
- Datenbank-/Jobfehler;
- Zahlungszustände;
- KI-Ausfälle/Kosten;
- Lösch-/Exportjobs;
- Missbrauch;
- Kosten;
- Kernproduktmetrik.

Ein Alarm benötigt Schwelle, Zeitraum, Schweregrad, Verantwortlichen, Runbook und Entwarnungskriterium.

## 17. Incident-Management

Ablauf:

```text
Erkennen
→ eindämmen
→ Verantwortung klären
→ Beweise sichern
→ Auswirkung bewerten
→ kommunizieren/melden, falls erforderlich
→ beheben
→ wiederherstellen
→ Ursachenanalyse
→ Maßnahmen verfolgen
```

Runbooks für mindestens:

- Auth-Ausfall;
- Datenbank-/Migrationfehler;
- Datenleck/Security-Vorfall;
- Zahlungsfehler;
- KI-Anbieterausfall;
- hohe Kosten;
- defekter Release.

## 18. Release Candidate

Vor RC:

- Scope eingefroren;
- offene Befunde bewertet;
- automatisierte Tests grün;
- reale Geräte geprüft;
- Migration/Staging erfolgreich;
- Backup/Restore getestet;
- Store-/Datenschutzangaben abgeglichen;
- Support/Statusseite bereit;
- Monitoring/Alarme aktiv;
- Rollback bereit.

## 19. Blocker

Kein Release bei:

- fremdem Datenzugriff;
- möglichem Datenverlust ohne Recovery;
- Secrets im Client/Repo/Log;
- manipulierbarer Abrechnung;
- kritischem Crash im Kernablauf;
- fehlender erforderlicher Löschung;
- falschen Store-/Datenschutzangaben;
- ungeklärter Hochrisiko-/Zulassungsfrage;
- fehlendem Verantwortlichen für Vorfälle;
- nicht getesteter kritischer Migration.

## KI-Einsatz

KI kann Tests, Threat-Model-Entwürfe, Checklisten, Loganalysen, Regressionen und Dokumentation unterstützen.

KI kann keine reale Geräteprüfung, Penetrationsprüfung, Rechtsfreigabe, Restore-Übung oder finale Verantwortung ersetzen.

## Gate

**Gate bestanden:** Release-Dossier enthält konkrete Evidenzlinks für Kernablauf, Rechte, Daten, Accessibility, Security, Performance, Restore, Rollback, Monitoring und Support; kein Blocker ist offen.
