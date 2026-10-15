# Beispielprojekt – FocusFlow

FocusFlow ist eine fiktive Fokus- und Aufgaben-App. Das Beispiel zeigt den vollständigen Weg von der Idee bis zum Betrieb, ohne medizinische Versprechen oder unnötig komplexe Funktionen.

## Produktversprechen

Nutzer sollen innerhalb von höchstens 60 Sekunden eine Aufgabe erfassen und eine Fokus-Session starten können.

## Zielgruppe

- Lernende
- Auszubildende
- Berufstätige
- Einzelpersonen, denen große Projektmanagementsysteme zu komplex sind

## Version 1

- E-Mail-Login
- Projekte und Aufgaben
- Fokus-Sessions
- Tagesziel und einfache Statistik
- Wiederaufnahme nach App-Neustart
- Datenexport
- Kontolöschung
- optionale KI-Zerlegung einer Aufgabe in kleine Schritte

## Nicht-Ziele

- Community oder öffentliche Profile
- Arbeitgeberüberwachung
- medizinische Diagnose oder Behandlung
- Werbung
- Marketplace
- komplexes Team-Projektmanagement

## Erfolgsmetriken

| Metrik | Ziel für Beta |
|---|---|
| Start einer ersten Session am ersten Tag | mindestens 60 % |
| Median bis zur ersten Session | unter 60 Sekunden |
| technische Abbrüche im Kernablauf | unter 2 % |
| D7-Retention | zunächst messen, danach Ziel festlegen |
| KI-Kosten | projektspezifisches hartes Limit pro Nutzer |

## Projektartefakte

- [PRD](./PRD.md)
- [Architektur](./ARCHITEKTUR.md)
- [Datenmodell und RLS](./supabase-schema-und-rls.sql)
- [Testplan](./TESTPLAN.md)
- [Release und Betrieb](./RELEASE-UND-BETRIEB.md)

## Kernablauf

```text
Registrieren/Anmelden
→ Aufgabe erstellen
→ Fokusdauer wählen
→ Session starten
→ unterbrechen oder abschließen
→ Fortschritt anzeigen
```

## Hauptrisiken

1. Nutzer A sieht oder ändert Daten von Nutzer B.
2. Eine aktive Session geht bei Neustart verloren.
3. Manipulierte Clientzeiten verfälschen Statistiken.
4. KI-Aufrufe werden missbraucht oder zu teuer.
5. Kontolöschung lässt Daten in Storage, Vektoren oder Drittanbietern zurück.
6. Marketing macht unzulässige Gesundheitsversprechen.

## Definition „fertige Beta“

- vollständiger Kernablauf auf realem Gerät;
- getrennte Entwicklungs-, Staging- und Produktionsumgebung;
- negative RLS-Tests mit zwei Nutzern;
- Export und Löschung getestet;
- KI-Funktion besitzt Rate-/Kostenlimit und Fallback;
- Backup/Restore geprüft;
- Monitoring, Support und Rollback vorhanden.
