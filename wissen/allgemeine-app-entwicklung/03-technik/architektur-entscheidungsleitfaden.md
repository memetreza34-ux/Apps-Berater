# Architektur-Entscheidungsleitfaden

## Ziel

Nicht die modernste Architektur wählen, sondern die einfachste, die Produkt, Sicherheit, Kosten und erwartete Skalierung zuverlässig trägt.

## Schritt 1 – Plattform wählen

| Option | Gut geeignet für | Vorsicht bei |
|---|---|---|
| Web/PWA | schnelle Veröffentlichung, Desktop, Formulare, Inhalte, SaaS | tiefe Gerätefunktionen, Store-Abhängigkeit |
| React Native/Expo | iOS und Android mit gemeinsamer Codebasis | native Spezialfunktionen, komplexe Upgrades |
| Flutter | konsistente Cross-Platform-UI | Dart-Ökosystem, Plattformbesonderheiten |
| Native iOS/Android | maximale Plattformintegration | doppelte Teams/Kosten |

### Entscheidungsfragen

- Muss die App in Stores erscheinen?
- Welche Gerätefunktionen sind zwingend?
- Muss sie offline funktionieren?
- Wie wichtig sind Widgets, Background Tasks oder Bluetooth?
- Welche Plattform kennt das Team wirklich?
- Welche Update- und Testkosten entstehen über fünf Jahre?

## Schritt 2 – Backend wählen

### BaaS wie Supabase

Sinnvoll, wenn:

- relationale Daten passen;
- Auth, Storage und Realtime benötigt werden;
- kleines Team schnell produktiv werden soll;
- Standard-CRUD und Policies einen großen Teil abdecken.

### Eigenes Backend

Sinnvoll, wenn:

- sehr spezielle Geschäftslogik;
- komplexe Hintergrundprozesse;
- ungewöhnliche Integrationen;
- eigene Betriebs- oder Compliance-Anforderungen;
- starke Portabilitäts- oder Multi-Region-Anforderungen.

### Hybrid

BaaS für Auth/Daten, eigene Services für KI, Zahlungen, Webhooks oder rechenintensive Jobs.

## Schritt 3 – Modularer Monolith vor Microservices

Für ein kleines Team ist ein modularer Monolith meist der bessere Start:

```text
App
└── Backend
    ├── identity
    ├── projects
    ├── billing
    ├── notifications
    └── ai
```

Klare Modulgrenzen sind wichtig. Getrennte Deployments sind erst nötig, wenn reale Skalierungs-, Team- oder Verfügbarkeitsgründe bestehen.

## Schritt 4 – Datenmodell

Vor UI-Massenausbau festlegen:

- zentrale Entitäten;
- Eigentümer und Mandant;
- Beziehungen;
- Statusmodelle;
- Auditbedarf;
- Aufbewahrung und Löschung;
- eindeutige Constraints;
- Indizes;
- Datenmigrationen.

## Schritt 5 – Nichtfunktionale Ziele

| Ziel | Beispiel |
|---|---|
| RPO | höchstens 24 Stunden Datenverlust |
| RTO | Wiederherstellung innerhalb 4 Stunden |
| Verfügbarkeit | 99,5 % im Monatsmittel |
| Kernlatenz | p95 unter 800 ms |
| Kosten | unter 0,50 € variable Plattformkosten pro aktivem Nutzer/Monat |
| Supportzeitraum | mindestens fünf Jahre ab Erstveröffentlichung |

Werte sind projektspezifisch und müssen realistisch finanzierbar sein.

## Schritt 6 – Architekturdiagramme

Mindestens:

1. Systemkontext
2. Container/Services
3. Auth- und Datenfluss
4. Zahlungsfluss
5. KI-Datenfluss
6. Löschfluss
7. Backup/Restore

## Schritt 7 – ADRs

Für jede wichtige Entscheidung eine Architecture Decision Record:

```text
Kontext
Entscheidung
Alternativen
Konsequenzen
Security/Datenschutz
Kosten
Exit-Plan
Prüfdatum
```

## Anbieterabhängigkeit

Dokumentiere für jeden kritischen Anbieter:

- Exportformat;
- Datenregion;
- Kündigung;
- Preisrisiko;
- alternative Anbieter;
- Migrationsaufwand;
- Verhalten bei Ausfall;
- Eigentum an Daten und Assets.

## Typische Fehlentscheidungen

- Microservices ohne Team oder Messbedarf
- Datenmodell entsteht zufällig aus Screens
- Geschäftslogik nur im Client
- keine Trennung von Entwicklungs- und Produktivsystem
- keine Migrationsstrategie
- keine Kostenalarme
- keine Backups oder nie getestete Wiederherstellung
- Anbieterwechsel wird pauschal versprochen, aber nie vorbereitet

## Architektur-Gate

- [ ] Plattform begründet
- [ ] Backend-Option begründet
- [ ] Systemkontextdiagramm
- [ ] Datenmodell und Rollen
- [ ] RPO/RTO und Kostenbudget
- [ ] Threat Model gestartet
- [ ] Exit-Plan für kritische Anbieter
- [ ] ADRs für zentrale Entscheidungen
