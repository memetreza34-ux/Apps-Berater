# 10 – Sonderfälle mit erhöhtem Risiko

Diese Bereiche dürfen nicht wie eine normale To-do- oder Content-App behandelt werden. Vor dem Bau der Kernfunktion ist eine fachkundige Einzelfallprüfung nötig.

## 1. Gesundheit und Medizin

### Warnsignale
- Diagnose, Prognose oder Therapieempfehlung;
- Dosierung oder Medikamentenentscheidung;
- Überwachung medizinischer Zustände;
- Auswertung von Vital-, Labor- oder Bilddaten;
- Werbung mit Heilungs- oder Behandlungsaussagen.

### Pflichtfragen
- Welche medizinische Zweckbestimmung vermittelt Funktion, UX und Marketing?
- Könnte Software als Medizinprodukt eingestuft werden?
- Wer prüft fachliche Richtigkeit und klinische Risiken?
- Welche Folgen hat eine falsche Ausgabe?
- Ist menschliche Kontrolle vorhanden?

Ein Disclaimer allein verhindert keine Regulierung, wenn die tatsächliche Funktion medizinisch ist.

## 2. Finanzen und Zahlungen

### Warnsignale
- personalisierte Anlage-, Kredit- oder Versicherungsentscheidung;
- Kundengelder, Wallet oder Zahlungsabwicklung;
- automatisiertes Trading;
- Bonitätsbewertung;
- Steuer- oder Rechtsberatung als verbindliche Einzelfallentscheidung.

### Pflichtfragen
- Erlaubnispflicht oder lizenzierter Partner?
- Haftung bei falschen Berechnungen?
- Betrugs-, Geldwäsche- und Identitätsrisiken?
- Revisions- und Aufbewahrungspflichten?
- DSGVO Art. 22 und AI-Act-Risiko bei automatisierten Entscheidungen?

## 3. Minderjährige

### Zusätzliche Anforderungen
- Zielalter exakt definieren;
- verständliche Sprache und altersgerechte UX;
- keine manipulativen Kauf- oder Engagementmuster;
- minimale Datenerhebung;
- Eltern-/Einwilligungsprozess entsprechend Land und Funktion;
- sichere Standardprofile;
- Kontakt-, Standort- und Community-Risiken begrenzen;
- Melde-, Blockier- und Moderationswege.

## 4. Community und Nutzerinhalte

Benötigt mindestens:
- Community-Regeln;
- Melde- und Beschwerdeweg;
- Blockieren/Stummschalten;
- Moderationsrollen und Audit;
- Umgang mit illegalen, verletzenden oder urheberrechtswidrigen Inhalten;
- Schutz vor Spam, Grooming, Belästigung und Identitätsmissbrauch;
- Löschung und Beweissicherung nach klarer Regel;
- DSA-Klassifizierung und Pflichtenprüfung.

## 5. Biometrie, Emotionen und Identität

Sehr hohes Risiko bei:
- Gesichtserkennung;
- Stimmidentifikation;
- biometrischer Kategorisierung;
- Emotionserkennung;
- Fernidentifikation;
- sensiblen Merkmalen.

Vor Prototyp:
- Notwendigkeit und Alternativen;
- verbotene AI-Act-Praktiken;
- besondere DSGVO-Daten;
- DSFA;
- Genauigkeit, Bias und Missbrauch;
- Speicherort und Löschung;
- On-Device-Verarbeitung als Alternative.

## 6. Hardware, IoT und Produkte mit digitalen Elementen

Prüfe:
- sichere Erstinstallation;
- eindeutige Geräteidentität;
- signierte Updates;
- sichere Standardkonfiguration;
- Offline-/Netzausfall;
- physische Folgen eines Fehlers;
- Support- und Updatezeitraum;
- SBOM und Schwachstellenprozess;
- CRA-Scope und Meldepflichten;
- Rückruf/Deaktivierung und End-of-Life.

## 7. Kritische Infrastruktur und B2B-Enterprise

Zusätzlich:
- Mandantentrennung;
- SSO/SCIM;
- Rollen und Vier-Augen-Prinzip;
- Auditlogs;
- Datenregion;
- SLA/SLO;
- Business Continuity;
- Penetrationstest;
- Lieferantenmanagement;
- NIS2-/Sektorprüfung.

## Eskalationsregel

Stoppe die Umsetzung und hole Fachprüfung ein, wenn:
- eine Fehlentscheidung Menschen, Vermögen oder Rechte erheblich schädigen kann;
- die rechtliche Einordnung offen ist;
- besondere Daten in großem Umfang verarbeitet werden;
- ein System automatisch über Menschen entscheidet;
- physische Sicherheit betroffen ist;
- Kinder oder besonders verletzliche Gruppen Kernzielgruppe sind.

## Nachweis

Für jeden Sonderfall wird ein Dokument erstellt:

```text
SONDERFALL-ENTSCHEIDUNG.md
- Auslöser
- Scope
- fachliche/rechtliche Bewertung
- Risikokontrollen
- externe Prüfer
- Tests
- Restrisiko
- Freigabe und Datum
```
