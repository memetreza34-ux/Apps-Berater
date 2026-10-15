# 03 – Architektur, Backend und Supabase

## Ziel

Die einfachste Architektur wählen, die den erwartbaren Betrieb sicher erfüllt und später verändert werden kann.

## 1. Plattformentscheidung

| Option | Gut geeignet für | Hauptnachteil |
|---|---|---|
| Web-App/PWA | schneller Start, Desktop und Mobile, einfache Updates | eingeschränkte native Funktionen |
| React Native/Expo | eine Codebasis für iOS und Android | native Sonderfälle bleiben möglich |
| Flutter | konsistente plattformübergreifende UI | eigenes Ökosystem und Dart |
| Native | maximale Plattformintegration | zwei Codebasen und höherer Aufwand |

Die Entscheidung wird als ADR dokumentiert. Nicht nach Trend entscheiden, sondern nach Funktionen, Teamwissen, Betrieb und Exit-Möglichkeit.

## 2. Architektur-Baseline

Für kleine Teams ist ein modularer Monolith häufig besser als frühe Microservices.

```text
App
→ Authentifizierung
→ serverseitige/API-Schicht
→ Datenbank
→ Storage
→ externe Anbieter
→ Monitoring
```

## 3. Pflichtentscheidungen

- Plattform und Framework
- Hosting/Region
- Backend oder BaaS
- Datenbank
- Authentifizierung
- Storage
- E-Mail und Push
- KI-Gateway
- Zahlungen
- Analytics und Monitoring
- Backups
- Export- und Anbieterwechsel

## 4. Datenmodell

Vor UI-Massenausbau festlegen:

- zentrale Datenobjekte
- Eigentümer und Rollen
- Beziehungen
- Constraints
- Statuswerte
- Aufbewahrung
- Löschreihenfolge
- Indizes
- Auditbedarf

## 5. Supabase-Produktionsregeln

1. Dev, Staging und Production trennen.
2. Jede Schemaänderung als Migration versionieren.
3. RLS auf allen exponierten Tabellen und Views aktivieren.
4. Datenbank-Grants und RLS getrennt prüfen.
5. Secret-/Service-Role-Schlüssel niemals in Client oder Repository.
6. Autorisierung nicht aus nutzeränderbaren Metadaten ableiten.
7. Negative Tests mit mindestens zwei Konten durchführen.
8. Storage-Policies für Upload, Lesen, Listen, Update und Löschen getrennt testen.
9. Backup und Restore wirklich ausführen.
10. Policy- und Filterspalten indexieren.

## 6. Vollständiger vertikaler Slice

Der erste echte Meilenstein ist kein voller Screen-Satz, sondern ein kompletter Ablauf:

1. Nutzer authentifiziert sich.
2. Nutzer erstellt echte Daten.
3. Daten werden sicher gespeichert.
4. Nach Neustart werden sie korrekt geladen.
5. Nutzer B kann nicht darauf zugreifen.
6. Fehler und Wiederholung funktionieren.
7. Export/Löschung sind technisch vorbereitet.
8. E2E- und Autorisierungs-Negativtest bestehen.

## 7. Kosten und Skalierung

Schätze mindestens für 100, 1.000 und 10.000 aktive Nutzer:

- Datenbank
- Storage und Egress
- KI-Aufrufe
- E-Mail/Push
- Monitoring
- Support
- Zahlungen und Refunds

## Gate 2/3

- [ ] Systemkontext und Datenfluss vorhanden
- [ ] Datenmodell und Rollen freigegeben
- [ ] RPO/RTO festgelegt
- [ ] Threat Model begonnen
- [ ] vertikaler Kernablauf produktionsnah getestet
- [ ] fremder Zugriff nachweislich verhindert
- [ ] grobes Kostenmodell vorhanden
