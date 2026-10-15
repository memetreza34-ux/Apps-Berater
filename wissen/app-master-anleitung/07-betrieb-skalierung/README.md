# Betrieb, Support, Skalierung und Produktende

Eine veröffentlichte App ist ein dauerhaftes System aus Software, Daten, Nutzern, Anbietern, Verträgen, Kosten und Verantwortung. Dieses Kapitel beschreibt den Betrieb über Jahre.

## Ergebnis dieses Kapitels

- Betriebshandbuch;
- Verantwortungs- und Bereitschaftsplan;
- Monitoring-, Alarm- und Runbooksystem;
- Support- und Wissensprozess;
- Wartungs- und Updatekalender;
- Kosten- und Kapazitätskontrolle;
- Sicherheits- und Datenschutzrhythmus;
- Skalierungs- und Migrationskriterien;
- Exit- und End-of-Life-Plan.

## 1. Betriebsverantwortung

Für jedes produktive System festlegen:

- Produktverantwortlicher;
- technische Verantwortung;
- Security-/Privacy-Kontakt;
- Supportverantwortung;
- Zahlungs-/Finanzkontakt;
- Marketing-/Kommunikationskontakt;
- Vertretung und Eskalation;
- Zugriff auf Konten und Notfallschlüssel.

Ein Produkt ohne erreichbare verantwortliche Person darf nicht dauerhaft öffentlich betrieben werden.

## 2. Betriebsinventar

| System | Zweck | Eigentümer | Region | Kostenmodell | Daten | Abhängigkeiten | Backup/Export | Statusseite | Exit-Plan |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

Erfasst werden mindestens:

- Frontend und Hosting;
- Backend und Datenbank;
- Auth;
- Storage;
- KI- und API-Anbieter;
- E-Mail, Push und SMS;
- Zahlungen;
- Analytics und Monitoring;
- Supportsystem;
- Domain und DNS;
- Build-, Signierungs- und Storekonten.

## 3. Monitoring

### Produkt

- Registrierung und Aktivierung;
- erfolgreicher Kernablauf;
- Abbrüche;
- Retention;
- Conversion und Churn;
- Supportfälle.

### Technik

- Verfügbarkeit;
- Fehlerrate;
- Latenz;
- Crashes;
- Queue- und Jobstatus;
- Datenbanklast;
- Storage und Bandbreite;
- Webhooks;
- Versionsverteilung.

### Sicherheit und Datenschutz

- verdächtige Anmeldungen;
- Rate-Limit-Ereignisse;
- Adminaktionen;
- ungewöhnliche Exporte oder Löschfehler;
- Schwachstellen und Abhängigkeiten;
- fehlgeschlagene Backups;
- Vorfälle bei Anbietern.

### Kosten

- Gesamtkosten;
- Kosten pro aktivem Nutzer;
- Kosten pro Kernvorgang;
- KI-/Medienkosten;
- ungewöhnliche Spitzen;
- Budgetgrenzen und Prognose.

## 4. Alarme

Ein Alarm benötigt:

- messbare Schwelle;
- Zeitraum;
- Schweregrad;
- verantwortliche Person;
- Benachrichtigungskanal;
- Runbook;
- Eskalationszeit;
- Entwarnungskriterium;
- Nachbesprechung bei schweren Ereignissen.

Nur handlungsrelevante Zustände alarmieren. Dauerhafte Fehlalarme zerstören Aufmerksamkeit.

## 5. Runbooks

Mindestens für:

- Login-/Auth-Ausfall;
- Datenbank- oder Hostingausfall;
- fehlerhafte Migration;
- Datenverlust oder Restore;
- Zahlungsstörung;
- KI-/API-Anbieterausfall;
- Kostenexplosion;
- kompromittierter Schlüssel;
- Datenschutz- oder Securityvorfall;
- fehlerhaftes Release;
- Kontolöschjob bleibt hängen;
- Domain-/DNS-Problem.

Jedes Runbook enthält Erkennung, Sofortmaßnahmen, Kommunikation, Wiederherstellung, Prüfung und Nachbereitung.

## 6. Support

### Kanäle

- In-App-Hilfe;
- Support-E-Mail oder Ticketsystem;
- FAQ/Wissensdatenbank;
- Statusseite;
- Store-Reviews;
- B2B-Ansprechpartner, falls vorhanden.

### Ticketdaten

- Problemkategorie;
- App-Version und Plattform;
- reproduzierbare Schritte;
- erwartetes und tatsächliches Verhalten;
- Schweregrad;
- Datenschutzstufe;
- Lösung;
- Produkt- oder Dokumentationsfolge.

Keine Passwörter, Tokens oder unnötigen sensiblen Daten anfordern.

## 7. Wartungsrhythmus

### Täglich oder automatisiert

- kritische Alarme;
- Kernablauf;
- Zahlung und Auth;
- Kostenlimits;
- Sicherheitsmeldungen.

### Wöchentlich

- Supportmuster;
- Fehler nach Version;
- Jobs und Webhooks;
- Bewertungen;
- aktive Experimente.

### Monatlich

- Abhängigkeiten und Updates;
- Adminrechte;
- Daten- und Löschjobs;
- Kosten und Kapazität;
- Produktmetriken;
- Runbook- und Dokumentationslücken.

### Quartalsweise

- Restore-Test;
- Incident-Übung;
- Anbieter- und Exitprüfung;
- Berechtigungsmatrix;
- Security-/Privacy-Review;
- Geräte- und Plattformmatrix.

### Jährlich

- vollständige Produkt-, Rechts-, Normen- und Storeprüfung;
- Architektur- und Technologierisiken;
- Verträge und Versicherungen;
- Preis und Wirtschaftlichkeit;
- Supportversprechen;
- End-of-Life-Fähigkeit.

## 8. Updates und Abhängigkeiten

Für jede zentrale Abhängigkeit:

| Komponente | Version | Supportende | Sicherheitsstatus | Upgradeweg | Testumfang | Rollback | Ersatz |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Updateprozess:

```text
Änderung beobachten
→ Relevanz bewerten
→ Testumgebung
→ automatisierte und manuelle Regression
→ Migration/Rollback
→ gestaffelter Release
→ Monitoring
→ Dokumentation
```

Nicht jahrelang ungepflegte Abhängigkeiten sammeln und dann alles gleichzeitig aktualisieren.

## 9. Backup und Restore

Ein Backup ist erst belegt, wenn Wiederherstellung getestet wurde.

Dokumentieren:

- welche Daten und Konfigurationen gesichert werden;
- RPO und RTO;
- Verschlüsselung und Zugriff;
- Aufbewahrung;
- Wiederherstellungsreihenfolge;
- Abhängigkeit von Anbieterzugängen;
- letzter Test und Ergebnis;
- Umgang mit gelöschten Nutzerdaten in Backups;
- Kommunikation bei Datenverlust.

## 10. Security- und Datenschutzvorfälle

Vorbereitet werden:

- Erkennung und Triage;
- Beweissicherung mit Datenminimierung;
- Eindämmung;
- Schlüsselrotation;
- Wiederherstellung;
- interne und externe Kommunikation;
- Prüfung gesetzlicher oder vertraglicher Meldepflichten;
- Nutzermaßnahmen;
- Ursachenanalyse;
- Korrektur und Nachweis.

Keine Fristen oder Meldepflichten raten. Die konkrete Anwendbarkeit wird anhand aktueller Primärquellen und Fachprüfung bestimmt.

## 11. Kostenkontrolle

- Budget je Anbieter und Funktion;
- Warnung und harte Grenze;
- Kosten pro Nutzer und Erfolg;
- kostenlose und bezahlte Nutzung getrennt;
- Missbrauch und Bots;
- ineffiziente Abfragen, Medien oder KI-Aufrufe;
- Notfallabschaltung teurer Zusatzfunktionen;
- Forecast bei Wachstum.

Wachstum ohne positive Wirtschaftlichkeit ist kein automatischer Erfolg.

## 12. Skalierung

Erst skalieren, wenn ein messbarer Engpass besteht.

Mögliche Skalierungsbereiche:

- Datenbankindizes und Abfragen;
- Caching und CDN;
- Jobs und Queues;
- Storage und Medienverarbeitung;
- Rate Limits;
- horizontale Anwendungsskalierung;
- Mandanten- oder Regionsarchitektur;
- Supportteam;
- Prozesse und Freigaben;
- Marketingbudget;
- Vertrag und SLA.

Keine Microservices oder komplexe Infrastruktur nur für ein hypothetisches Wachstum bauen.

## 13. Team und Organisation

Mit Wachstum werden Rollen formalisiert:

- Product;
- Design und Research;
- Engineering;
- QA;
- Security/Privacy;
- Data/Analytics;
- Marketing/Growth;
- Sales/Partnerships;
- Support/Operations;
- Finance/Legal.

Zugänge, Entscheidungen und Wissen dürfen nicht von einer einzigen Person abhängig sein.

## 14. Internationalisierung

Vor neuem Markt prüfen:

- Sprache und kulturelle Anpassung;
- Datum, Zeit, Währung, Zahlen und Adressen;
- lokale Preise und Steuern;
- Recht, Datenschutz und Verbraucherpflichten;
- Store- und Zahlungsunterstützung;
- Datenregion und Anbieter;
- Supportzeiten;
- Marketingkanäle;
- Barrierefreiheit;
- lokale Fachprüfung bei erhöhtem Risiko.

## 15. B2B und Enterprise

Zusätzliche Themen:

- Organisationen und Mandanten;
- Rollen und Genehmigungen;
- SSO/SCIM;
- Auditlogs;
- Datenregion;
- Auftragsverarbeitung;
- SLA und Support;
- Security-Fragebögen;
- Penetrationstests;
- Vertrags- und Kündigungsprozesse;
- Datenexport und Übergabe;
- Beschaffung und Rechnungen.

## 16. Anbieterwechsel und Migration

Vor Abhängigkeit dokumentieren:

- Exportformat;
- API- und Datenzugang;
- Datenmenge;
- Downtime;
- paralleler Betrieb;
- Identitäten und Passwörter;
- URLs, Webhooks und Schlüssel;
- alte Clients;
- Test und Rückfall;
- Nutzerkommunikation;
- Vertragsende und Datenlöschung beim Altanbieter.

## 17. Verkauf oder Übertragung

Vorbereiten:

- Eigentum am Code und an Assets;
- Verträge und Lizenzen;
- Marken und Domains;
- Kontenübertragbarkeit;
- Datenschutzrollen und Nutzerinformation;
- technische Dokumentation;
- Finanz- und Nutzungsmetriken;
- offene Risiken;
- Supportübergang;
- Datenmigration.

## 18. Produktende

Ein Produktende wird geplant, bevor es nötig wird.

```text
Entscheidung
→ rechtliche und vertragliche Prüfung
→ Zeitplan
→ Nutzerinformation
→ Export/Migration
→ Kündigung und Erstattung
→ Store- und Webstatus
→ Datenaufbewahrung und Löschung
→ Anbieter kündigen
→ Systeme abschalten
→ Nachweis und Archiv
```

Nutzer dürfen nicht überraschend den Zugang zu wichtigen Daten verlieren.

## Freigabe-Gate

Langfristiger Betrieb ist nur vertretbar, wenn:

- Verantwortliche und Vertretungen existieren;
- Kernsysteme überwacht werden;
- Backups und Restore getestet sind;
- Security-, Datenschutz- und Supportprozesse funktionieren;
- Kosten und Limits kontrolliert werden;
- Updates und Abhängigkeiten regelmäßig gepflegt werden;
- Anbieterwechsel und Produktende grundsätzlich möglich sind.
