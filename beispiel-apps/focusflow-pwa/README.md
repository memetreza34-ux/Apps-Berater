# FocusFlow PWA – ausführbare Referenz-App

Diese kleine Referenz-App ist bewusst abhängigkeitsfrei. Sie beweist die Verbindung zwischen Produktanforderungen, Designsystem, Zuständen, lokaler Persistenz, Offline-Grundlage, Export, Löschung und Tests.

## Starten

```bash
cd beispiel-apps/focusflow-pwa
python -m http.server 4173
```

Danach im Browser öffnen:

```text
http://localhost:4173
```

Die App darf nicht direkt über `file://` gestartet werden, weil Service Worker einen lokalen HTTP-Server benötigen.

## Enthalten

- Aufgaben anlegen und auswählen
- 25-Minuten-Fokustimer
- Pause und Reset
- lokale Speicherung
- Leer-, Erfolgs- und Fehlerfeedback
- Export als JSON
- vollständige lokale Datenlöschung
- Light/Dark Mode über Systemeinstellung
- Tastatur- und Screenreader-Baseline
- Web-App-Manifest
- Service-Worker-App-Shell
- dependency-freier Strukturtest

## Tests

```bash
python -m unittest discover -s tests -v
```

## Bewusste Grenzen

Diese Referenz-App ist kein Ersatz für das produktive FocusFlow-Beispiel mit Supabase. Sie besitzt:

- keine echten Nutzerkonten;
- keine Cloud-Synchronisation;
- keine RLS-/Serverautorisierung;
- keine Push-Mitteilungen;
- keine Zahlung;
- keine KI.

Dafür existieren im Handbuch Architektur-, SQL-, RLS-, KI-, Zahlungs- und Releasebeispiele. Der Zweck dieser PWA ist ein sofort sichtbarer und testbarer vertikaler UI-Kernablauf.

## Produktionsausbau

1. PRD und Screen-Inventar auf das konkrete Produkt anpassen.
2. Supabase-Schema und RLS aus dem Beispielprojekt verwenden und erneut prüfen.
3. lokale Speicherung durch Repository-/API-Schicht abstrahieren.
4. Auth, Export und Kontolöschung Ende-zu-Ende testen.
5. CI, E2E, Monitoring, Datenschutz und Release-Dossier ergänzen.
