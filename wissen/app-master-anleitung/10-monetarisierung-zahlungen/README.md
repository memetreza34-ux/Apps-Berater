# Monetarisierung, Zahlungen, Abos, Steuern und Profitabilität

Dieses Kapitel verbindet Produktnutzen, Preise, technische Entitlements, Plattformregeln, Support und Kosten. Eine Zahlungsseite allein ist noch kein funktionierendes Geschäftsmodell.

## Ziel

Am Ende liegen vor:

- gewähltes Geschäftsmodell;
- Preis- und Paketstruktur;
- Kosten- und Profitabilitätsmodell;
- Zahlungsarchitektur;
- Entitlement-Modell;
- Testplan für alle Zahlungszustände;
- Refund-/Chargeback-/Supportprozess;
- steuerlicher und organisatorischer Prüfplan.

## 1. Bezahlt der Nutzer für laufenden Wert?

Vor Preisgestaltung klären:

- Welches Ergebnis wird bezahlt?
- Wie häufig entsteht dieser Wert?
- Welche laufenden Kosten verursacht die Nutzung?
- Welche kostenlose Alternative existiert?
- Wer trifft die Kaufentscheidung?
- Wie lässt sich der Wert vor dem Kauf zeigen?
- Welche Nutzung muss nach Kündigung bestehen bleiben?

## 2. Modelle

### Kostenlos

Keine Zahlung, aber Betrieb und Support bleiben kostenpflichtig. Finanzierung durch Budget, Spenden, Cross-Selling oder strategischen Nutzen klären.

### Einmalkauf

Geeignet bei abgeschlossenem Wert und begrenzten laufenden Kosten. Update- und Supportzeitraum definieren.

### Abonnement

Geeignet bei laufendem Nutzen, Cloudbetrieb, regelmäßigen Inhalten oder wiederkehrenden Kosten.

### Freemium

Kostenloser Kern plus bezahlte Erweiterung. Die kostenlose Version muss Nutzen zeigen, darf aber nicht alle Kosten unkontrolliert erzeugen.

### Credits/Verbrauch

Geeignet bei klar messbaren kostenintensiven Vorgängen. Saldo, Ablauf, Rückerstattung und Doppelabbuchung müssen korrekt behandelt werden.

### Werbung

Benötigt Reichweite, Daten-/Trackingprüfung, Werbekennzeichnung und Qualitätskontrolle.

### B2B/Lizenz

Verträge, Rechnungen, Rollen, Mandanten, Support, SLA, SSO, Datenschutz und Beschaffung berücksichtigen.

### Provision/Marktplatz

Zusätzliche Betrugs-, Streit-, Auszahlungs-, Identitäts- und regulatorische Risiken.

## 3. Preisstrategie

Preis nicht nur aus Konkurrenz übernehmen.

Berücksichtigen:

- Nutzerwert;
- Kosten;
- Zielgruppe;
- Kaufhäufigkeit;
- Alternativen;
- Supportaufwand;
- Plattformgebühren;
- Steuern;
- Markt und Währung;
- Zahlungsbereitschaft;
- gewünschte Positionierung.

## 4. Pakete

Gute Pakete unterscheiden sich nach Wert, nicht künstlicher Verwirrung.

Beispiel:

| Plan | Zielgruppe | Kernwert | Limits | Support | Preis |
|---|---|---|---|---|---:|
| Free | Testnutzer | Kernablauf | fair begrenzt | Standard | 0 |
| Pro | Einzelperson | volle Nutzung | höhere Limits | Standard | |
| Team | Gruppen | Zusammenarbeit/Admin | je Sitz/Team | priorisiert | |

Vermeiden:

- versteckte Pflichtkosten;
- absichtlich unklare Laufzeiten;
- künstlich erschwerte Kündigung;
- irreführende „kostenlos“-Aussagen;
- Funktionen, die nach Kauf technisch nicht sicher freigeschaltet werden.

## 5. Kostenrechnung

### Fixkosten

- Entwicklerkonten;
- Domain/E-Mail;
- Grundtarife;
- Buchhaltung;
- rechtliche/fachliche Prüfung;
- Geräte;
- Grundmarketing;
- Team/Agentur.

### Variable Kosten

- Hosting/DB/Storage;
- Datentransfer;
- KI/API;
- E-Mail/Push/SMS;
- Zahlungsgebühren;
- Support;
- Refunds/Chargebacks;
- Moderation;
- Medienverarbeitung.

## 6. Unit Economics

Mindestens berechnen:

```text
Umsatz pro aktivem zahlendem Nutzer
- variable Kosten
- Zahlungs-/Storegebühren
- durchschnittlicher Support
- Rückerstattungen/Betrug
= Deckungsbeitrag
```

Zusätzlich:

- Conversion;
- Churn;
- durchschnittliche Laufzeit;
- LTV;
- Akquisitionskosten;
- Break-even;
- Reserve.

Annahmen klar als Annahmen kennzeichnen.

## 7. Entitlements

Ein Entitlement beschreibt, welche Leistung ein Konto wirklich nutzen darf.

Beispiele:

- Plan;
- aktive Periode;
- Grace Period;
- gekündigt zum Periodenende;
- pausiert;
- abgelaufen;
- Refund;
- Chargeback;
- Lifetime;
- Team-Sitz;
- Credit-Saldo.

Entitlements serverseitig oder in gleichwertig vertrauenswürdiger Schicht verwalten. Nicht nur einen Client-Schalter verwenden.

## 8. Zahlungsquellen

Mögliche Quellen:

- Apple;
- Google;
- Web-Zahlungsanbieter;
- Rechnung/B2B;
- Gutscheine/Promocodes;
- manuelle Lizenz.

Eine zentrale Entitlement-Schicht normalisiert Zustände, ohne Originalbelege zu verlieren.

## 9. Serverseitige Verifikation

Prüfen:

- signierte Belege/Events;
- richtige App/Produkt-ID;
- Konto-/Nutzerzuordnung;
- Zeitraum;
- Erstattung/Kündigung;
- Wiederholung;
- Reihenfolge;
- Sandbox/Produktion;
- Idempotenz.

## 10. Webhooks

- Signatur;
- Event-ID;
- idempotente Verarbeitung;
- Wiederholung;
- verspätete Events;
- Reihenfolge;
- Fehlerqueue;
- Monitoring;
- Audit;
- minimale Logs.

## 11. Kaufzustände testen

Mindestens:

- erster Kauf;
- abgebrochener Kauf;
- fehlgeschlagene Zahlung;
- ausstehende Zahlung;
- Gerätewechsel;
- Kontowechsel;
- Restore;
- Verlängerung;
- Kündigung;
- Grace Period;
- Ablauf;
- Upgrade/Downgrade;
- Refund;
- Chargeback;
- doppelte Events;
- Anbieter-/Netzausfall;
- Kontolöschung bei aktivem Abo.

## 12. Credits

Benötigt:

- Ledger statt nur veränderbarer Zahl;
- Buchungstyp;
- Betrag;
- Ursache;
- Referenz;
- Zeit;
- Idempotenz;
- Rückbuchung;
- Audit;
- negative Salden verhindern;
- Ablaufregel klar kommunizieren.

## 13. Werbung

Prüfen:

- Zielgruppe/Minderjährige;
- Tracking/Consent;
- sensible Kategorien;
- Kennzeichnung;
- Frequenz;
- Platzierung;
- Qualitätskontrolle;
- Betrug;
- Datenschutzangaben;
- Entfernen durch bezahlten Plan;
- Einfluss auf Performance und UX.

## 14. Rechnungen und Steuern

Abhängig von Betreiber, Kunden, Ländern und Modell. Früh klären:

- Gewerbe/Unternehmensform;
- Umsatzsteuer und OSS/Marktplatzrolle;
- Rechnungsanforderungen;
- Belegaufbewahrung;
- Plattformabrechnungen;
- B2B-Nachweise;
- Währungen;
- Erstattungen;
- Buchhaltung;
- verantwortliche Fachberatung.

Das Handbuch liefert einen Prüfpfad, keine individuelle Steuerberatung.

## 15. Support

Support benötigt Zugriff auf zulässige Referenzen, nicht unnötig auf Zahlungsdaten.

Prozesse:

- Kauf nicht erkannt;
- Restore;
- falsches Konto;
- Refund;
- Kündigung;
- Rechnung;
- Chargeback;
- verlorenes Gerät;
- Teamlizenz;
- Kontolöschung.

## 16. Kostenlimits

- Budget pro Anbieter;
- Warnschwellen;
- harte Limits;
- Kosten pro Feature;
- Kosten pro aktivem Nutzer;
- KI-/Medienquoten;
- Notfall-Schalter;
- Downgrade-Verhalten;
- Missbrauchserkennung.

## 17. Preisexperimente

Nur mit klarer Hypothese und fairer Kommunikation.

Messen:

- Conversion;
- Aktivierung;
- Retention;
- Churn;
- Refunds;
- Support;
- Deckungsbeitrag;
- Segmentunterschiede.

Keine manipulativen Dark Patterns.

## 18. Dokumente

- Monetarisierungsentscheidung;
- Preis- und Paketmatrix;
- Produkt-/Plan-IDs;
- Entitlement-Modell;
- Zahlungsdatenfluss;
- Webhook-Runbook;
- Testprotokoll;
- Refund-/Supportprozess;
- Kostenmodell;
- Steuer-/Buchhaltungsentscheidung;
- Store-/Web-Abgleich.

## KI-Einsatz

KI kann Szenarien rechnen, Pakete vergleichen, Testfälle und Supportantworten entwerfen, Webhooklogik reviewen und Kostenrisiken finden.

KI darf keine Steuer- oder Rechtsfreigabe erfinden, Zahlungszustände ohne Beleg freischalten oder unrealistische Umsatzannahmen als Tatsache behandeln.

## Gate

**Gate bestanden:** Alle Preise und Leistungsrechte stimmen zwischen Produkt, Stores/Web, Server und Kommunikation überein; kritische Kaufzustände sind in Sandbox/Testumgebung geprüft; Kosten und Support sind tragfähig.
