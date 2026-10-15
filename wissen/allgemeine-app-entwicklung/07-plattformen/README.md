# 07 – Plattformwahl und technische Basis

Die beste Plattform ist nicht die modernste, sondern diejenige, die Produkt, Team, Budget, Hardwarezugriff und Wartung am zuverlässigsten trägt.

## Entscheidungsübersicht

| Option | Geeignet für | Stärken | Hauptrisiken |
|---|---|---|---|
| Responsive Web/PWA | Inhalte, Dashboards, SaaS, schneller Markttest | ein Codebestand, schneller Release, kein Store-Zwang | eingeschränkter Hardware-/Hintergrundzugriff, iOS-PWA-Grenzen |
| React Native/Expo | iOS und Android mit JS/TS-Team | hoher Wiederverwendungsgrad, großes Ökosystem, OTA-Möglichkeiten | Native-Abhängigkeiten, Upgrade-/Plugin-Risiken |
| Flutter | mobile Multiplattform mit konsistenter UI | kontrolliertes Rendering, gute Cross-Platform-Story | eigenes Ökosystem/Dart, Plattformdetails trotzdem nötig |
| Native Swift/Kotlin | tiefe Plattformintegration, anspruchsvolle Hardware | beste Plattformnähe und Kontrolle | zwei Codebasen/Teams, höhere Kosten |
| Desktop/Electron/Tauri | Desktop-Workflows | Web-Know-how, schneller Cross-Platform-Start | Ressourcenverbrauch bzw. Integrationsaufwand |

## Entscheidungsfragen

1. Muss die App in den Stores sein?
2. Welche Gerätefunktionen werden benötigt?
3. Muss sie zuverlässig offline arbeiten?
4. Braucht sie Hintergrundprozesse, Widgets oder Push?
5. Wie wichtig sind Startzeit, Akku und Speicher?
6. Welches Wissen besitzt das Team dauerhaft?
7. Welche Abhängigkeit kann fünf Jahre gepflegt werden?
8. Gibt es ein realistisches Migrations- oder Exit-Szenario?

## Empfohlene Baseline für kleine Teams

### Web-App
- TypeScript
- aktuelles, langfristig gepflegtes Framework
- serverseitige Secrets
- relationale Datenbank
- automatisierte Tests
- CDN/Hosting mit Rollback

### Mobile App
- React Native/Expo oder Flutter, wenn keine tiefe Native-Spezialisierung nötig ist
- native Module nur bei belegtem Bedarf
- getrennte Dev-/Staging-/Production-Konfiguration
- sichere Speicherung für Tokens
- Release-Builds früh auf echten Geräten testen

## Modularer Monolith vor Microservices

Für die meisten neuen Apps:

```text
Client
→ ein klar strukturiertes Backend/API
→ relationale Datenbank
→ Storage
→ wenige externe Anbieter
```

Microservices erst bei messbarem Grund:
- unabhängige Skalierung;
- getrennte Teams/Releasezyklen;
- harte Isolation;
- besondere Verfügbarkeit;
- regulatorische Trennung.

## Architecture Decision Records

Für jede große Entscheidung dokumentieren:
- Kontext;
- Entscheidung;
- Alternativen;
- Folgen;
- Security/Privacy;
- Kosten bei 100, 1.000 und 10.000 aktiven Nutzern;
- Exit-/Migrationsweg;
- nächstes Prüfdatum.

## Offline und Synchronisation

Offline ist kein einzelner Schalter. Kläre:
- lokale Quelle der Wahrheit;
- Konfliktstrategie;
- Retry und Idempotenz;
- Löschung auf mehreren Geräten;
- Uhrzeit/Zeitzone;
- Verschlüsselung lokaler Daten;
- Verhalten bei alter App-Version.

## Konfigurations- und Umgebungsregeln

- Dev, Staging und Production trennen.
- keine produktiven Daten in Dev.
- keine Secrets im Client oder Repository.
- Feature Flags für riskante Funktionen.
- reproduzierbare Builds und Lockfiles.
- Migrationen vor App-Code kompatibel ausrollen.
- alte Clients während eines definierten Übergangs unterstützen.

## Plattform-Gate

Die Plattformentscheidung ist erst freigegeben, wenn:
- Kernfunktionen technisch als Spike geprüft wurden;
- Store-/Hardwareanforderungen bekannt sind;
- Upgrade- und Wartungspfad dokumentiert ist;
- variable Kosten modelliert sind;
- Backup, Export und Anbieterwechsel grundsätzlich möglich sind.
