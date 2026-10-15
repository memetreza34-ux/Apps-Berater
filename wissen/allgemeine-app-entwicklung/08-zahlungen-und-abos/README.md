# 08 – Zahlungen, Abos und Berechtigungen

Zahlungen sind nicht nur ein Button. Sie verbinden Store-Regeln, Verbraucherinformation, Steuerbelege, Webhooks, Erstattungen, Kontolöschung und Support.

## Geschäftsmodell zuerst

| Modell | Geeignet, wenn | Risiko |
|---|---|---|
| einmaliger Kauf | dauerhafte lokale Funktion oder klar abgegrenztes Produkt | laufende Cloudkosten ohne Folgeumsatz |
| Abo | dauerhaft wiederkehrender Nutzen und Kosten | Churn, Transparenz, Store-/Verbraucherpflichten |
| Freemium | kostenloser Kern und klarer Premiumwert | zu großzügige Gratisversion oder künstliche Sperren |
| Credits | messbare variable KI-/Medienkosten | komplizierte Erstattung, Ablauf und Verbrauchsanzeige |
| B2B-Lizenz | Teams/Unternehmen mit Vertrag | Rollen, Rechnungen, Beschaffung und Support-SLA |

## Abo-Grundregel

Ein Abo braucht **dauerhaften, wiederkehrenden Wert**. Preis, Abrechnungszeitraum, automatische Verlängerung, Testphase, Einschränkungen und Kündigung dürfen nicht versteckt oder irreführend sein.

Aktuelle Store-Details immer in den offiziellen Apple- und Google-Richtlinien prüfen; das Quellenregister enthält die Primärquellen.

## Technische Architektur

```text
Store/Payment Provider
→ signierter Kauf / Checkout
→ Server-Verifikation
→ internes Entitlement
→ App liest Entitlement
→ Webhooks/Server Notifications aktualisieren Status
```

Die App darf Premiumzugriff nicht allein anhand eines lokalen Schalters oder einer Client-Antwort freigeben.

## Internes Entitlement-Modell

Speichere mindestens:
- Nutzer/Organisation;
- Produkt/Plan;
- Quelle: Apple, Google, Web, manuell;
- aktueller Status;
- Start und Ende;
- Testphase;
- Kündigung zum Laufzeitende;
- Grace Period;
- letzte verifizierte Transaktion;
- Provider-Referenz;
- Auditzeitpunkte.

## Webhooks und Idempotenz

Webhooks können doppelt, verspätet oder in falscher Reihenfolge eintreffen.

Pflichten:
- Signatur prüfen;
- Event-ID deduplizieren;
- Status serverseitig erneut abrufen, wenn nötig;
- Verarbeitung idempotent;
- Retry/Dead-Letter-Prozess;
- keine dauerhafte Freischaltung durch ungeprüfte Clientdaten;
- Auditlog ohne unnötige Zahlungsdaten.

## Zustände, die getestet werden müssen

- Kauf erfolgreich
- Kauf abgebrochen
- Zahlung ausstehend
- Testphase aktiv/abgelaufen
- Verlängerung erfolgreich/fehlgeschlagen
- Grace Period
- Kündigung zum Periodenende
- Erstattung/Chargeback
- Wiederherstellen von Käufen
- Gerätewechsel
- Accountwechsel
- Store- und App-Konto stimmen nicht überein
- Provider-Ausfall

## Kontolöschung bei aktivem Abo

Account und Store-Abo sind getrennte Dinge. Der Löschprozess muss:
1. auf ein aktives Abo hinweisen;
2. Verwaltung/Kündigung erreichbar machen;
3. trotzdem eine sofortige Kontolöschung ermöglichen, soweit Store- und Rechtslage dies verlangen;
4. transparent erklären, was mit verbleibender Laufzeit und Daten geschieht;
5. Provider- und interne Daten korrekt behandeln.

Apple weist ausdrücklich darauf hin, dass Store-Abrechnung nach Accountlöschung weiterlaufen kann, wenn das Abo nicht gekündigt wurde. Google verlangt bei Apps mit Accounterstellung einen auffindbaren In-App- und externen Löschweg.

## Preisgestaltung

Rechne nicht nur Storegebühr und Hosting:
- Umsatzsteuer/Steuerprozess;
- KI-/API-Kosten;
- Storage und Bandbreite;
- Support;
- Refunds/Chargebacks;
- Monitoring/E-Mail/Push;
- Entwicklungs- und Wartungszeit;
- Währungs- und Preisänderungen.

## Release-Gate Zahlungen

- Produkte und Preise stimmen in App, Store und Backend überein.
- Entitlement wird serverseitig verifiziert.
- Webhooks sind signiert, idempotent und überwacht.
- Restore und Gerätewechsel getestet.
- Kündigung, Erstattung und Kontolöschung verständlich.
- Keine Dark Patterns.
- Support kann Transaktionen anhand zulässiger Referenzen nachvollziehen.
- Finanz-/Steuerprozess ist organisatorisch geklärt.

## Primärquellen

- Apple App Review Guidelines: https://developer.apple.com/app-store/review/guidelines/
- Apple Account Deletion: https://developer.apple.com/support/offering-account-deletion-in-your-app
- Google Play Subscriptions: https://support.google.com/googleplay/android-developer/answer/9900533
- Google Play User Data: https://support.google.com/googleplay/android-developer/answer/10144311
