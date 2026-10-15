# React-Native- und Expo-Playbook

## Geeignet für

- iOS und Android mit gemeinsamem TypeScript-Code;
- kleine Teams ohne tiefe native Spezialisierung;
- Apps mit Push, Kamera, Dateien, Standort oder Store-Veröffentlichung;
- schnelle Iteration bei kontrolliertem nativen Umfang.

## Vor dem Start

Erstelle technische Spikes für jede kritische native Funktion:
- Push Notifications;
- Hintergrundaufgaben;
- Widgets/Live Activities;
- Bluetooth/NFC;
- Kamera und Medien;
- Health-/Fitness-Daten;
- sichere lokale Speicherung;
- Deep Links;
- In-App Purchases.

Ein Plugin gilt erst als akzeptiert, wenn Wartungsstatus, Plattformunterstützung, Lizenz, Berechtigungen, Buildverhalten und Exit-Alternative dokumentiert sind.

## Projektstruktur

```text
src/
├── app/             Navigation und Screen-Komposition
├── features/        fachliche Module
├── components/      wiederverwendbare UI
├── design-system/   Tokens und Komponentenregeln
├── data/            API, Cache, Persistenz
├── security/        sichere Storage-/Auth-Helfer
├── observability/   Fehler, Metriken, Logs
└── test/            Fixtures und Testhelfer
```

## Konfiguration

- App-ID/Bundle-ID früh festlegen;
- Dev, Staging und Production getrennt konfigurieren;
- Berechtigungsbeschreibungen nur für tatsächlich genutzte Funktionen;
- keine geheimen Serverwerte in öffentliche App-Konfiguration;
- Buildprofile versionieren;
- Signierung und Recovery organisatorisch dokumentieren;
- Store- und OTA-Versionen kompatibel halten.

## Auth und lokale Daten

- Tokens nur in geeigneter sicherer Plattformablage;
- keine Passwörter oder Service-Keys speichern;
- Sessionablauf und biometrische Entsperrung getrennt behandeln;
- sensible Offline-Daten minimieren und verschlüsseln;
- Logout löscht lokale sensible Caches;
- Kontowechsel darf keine Daten des vorherigen Nutzers zeigen.

## Navigation und Deep Links

Teste:
- Kaltstart über Link;
- Link bei geöffneter App;
- nicht angemeldeter Nutzer;
- abgelaufene Session;
- gelöschte Ressource;
- manipulierte Parameter;
- Universal-/App-Link-Fallback.

## Updates

- native Änderungen benötigen einen neuen Store-Build;
- JavaScript-/Asset-Updates nur kompatibel zur installierten nativen Laufzeit ausrollen;
- riskante Updates gestaffelt freigeben;
- Kill Switch und Rollback vorsehen;
- Datenbank-/API-Kompatibilität mit alten Clients definieren.

## Gerätetests

Mindestens:
- kleines und großes iPhone;
- aktuelles und unterstütztes älteres Androidgerät;
- langsames Netz und Flugmodus;
- wenig Speicher;
- unterbrochener Upload;
- App im Hintergrund/gekilled;
- Dark Mode, Textvergrößerung und Screenreader;
- Push erlaubt/verweigert;
- Geräte- und Kontowechsel.

## Release-Gate

- [ ] kritische native Spikes bestanden
- [ ] Signierung und Recovery dokumentiert
- [ ] Dev/Staging/Prod getrennt
- [ ] sichere Token- und Cachebehandlung
- [ ] Deep Links negativ getestet
- [ ] Berechtigungen minimal und verständlich
- [ ] OTA-/Store-Kompatibilitätsregel
- [ ] echte Gerätetests
- [ ] Crash-/Performance-Monitoring
- [ ] Rollback und Kill Switch
