# 00 – Start und Entscheidungsweg

## Ziel

Vor dem ersten Code wird entschieden, welche Art App gebaut wird, welche Risiken bestehen und welche Kapitel zwingend gelten.

## Schritt 1: App-Typ bestimmen

- reine Offline-App
- Web-App oder PWA
- native oder Cross-Platform-Mobile-App
- SaaS mit Accounts
- App mit KI
- App mit Community oder Nutzerinhalten
- App mit Zahlungen/Abos
- App mit Standort, Kamera, Mikrofon oder Kontakten
- Gesundheits-, Finanz-, Bildungs- oder Kinder-App
- App mit Hardware oder IoT

## Schritt 2: Risikofragen

| Frage | Bei „Ja“ zusätzlich erforderlich |
|---|---|
| Werden personenbezogene Daten verarbeitet? | Dateninventar, Rechtsgrundlage, Löschung, Betroffenenrechte |
| Werden besondere Daten verarbeitet? | hohes Datenschutzrisiko, DSFA prüfen, strengere Schutzmaßnahmen |
| Gibt es KI-Funktionen? | AI-System-Register, Risikoklasse, Transparenz, Evaluation |
| Können Nutzer Inhalte veröffentlichen? | Moderation, Meldeweg, Rechte- und Plattformprüfung |
| Sind Minderjährige Zielgruppe? | Alterskonzept, Schutz, Einwilligung und Stores besonders prüfen |
| Gibt es Gesundheits- oder Finanzversprechen? | Zweckbestimmung und fachliche Regulierung vorab klären |
| Gibt es Abos oder Käufe? | Verbraucherrecht, Store-Billing, Kündigung, Rückerstattung |
| Werden Tracking-SDKs verwendet? | Einwilligung, SDK-Register, Store-Angaben, Datenflüsse |

## Schritt 3: Stop, Überarbeiten oder Starten

### Starten

- Problem ist real und wiederkehrend.
- Kernfunktion ist technisch umsetzbar.
- notwendige Daten und Rechte sind verfügbar.
- variable Kosten sind beherrschbar.
- Risiken können mit vertretbarem Aufwand kontrolliert werden.

### Überarbeiten

- Scope ist zu groß.
- Kernnutzen ist unklar.
- Datenmodell, Rechte oder Anbieter sind noch offen.
- eine regulierte Funktion kann durch eine weniger riskante Variante ersetzt werden.

### Stoppen

- die Kernfunktion wäre ohne Zulassung oder nicht verfügbare Rechte unzulässig;
- fremde Inhalte oder Daten dürfen nicht verwendet werden;
- die App kann wirtschaftlich nicht betrieben werden;
- das Problem ist nicht ausreichend belegt.

## Pflichtartefakte vor Entwicklung

1. App-Risikoprofil
2. Problemstatement
3. Zielgruppe
4. MVP und Nicht-Ziele
5. PRD
6. Kern-User-Flow
7. Dateninventar
8. erste Architekturentscheidung
9. Kostenannahme
10. Stop-/Go-Entscheidung
