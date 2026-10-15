# Vorlagen – Allgemeine App-Entwicklung v1.1

Diese Vorlagen werden für jede App kopiert und projektspezifisch ausgefüllt. Die Entscheidung, welche Vorlagen Pflicht sind, liefert der [Entscheidungsassistent](../00-start/entscheidungsassistent.md).

## Zentrale Startvorlagen

- [App-Risikoprofil](./app-risikoprofil.md)
- [PRD – Product Requirements Document](./prd.md)
- [Produktionspaket v1.1](./produktionspaket-v1.md)
- [Evidenz-Matrix](./evidenz-matrix.md)
- [Plattform- und Gerätetestmatrix](./plattform-testmatrix.md)

## Weitere im Verzeichnis vorhandene Fachvorlagen

- Screen-Inventar;
- Architekturentscheidung (ADR);
- Daten- und Anbieterregister;
- Berechtigungsmatrix;
- Threat Model;
- AI-System-Register;
- Release-Freigabe;
- Incident Report.

## Empfohlene Projektstruktur

```text
docs/product/
docs/design/
docs/architecture/
docs/security/
docs/privacy/
docs/testing/
docs/release/
docs/operations/
evidence/
```

## Verbindliche Regeln

1. Eine leere Vorlage ist kein Nachweis.
2. Jede Freigabe verweist auf konkrete Evidenz.
3. Zeitabhängige Entscheidungen besitzen Prüf- und Ablaufdatum.
4. Widersprüche zwischen PRD, Design, Code, Store und Datenschutz werden vor Release gelöst.
5. Keine Secrets oder produktiven personenbezogenen Daten in Dokumentation und Evidenz committen.
6. Bei hohem Risiko ist eine zweite fachliche Prüfperspektive erforderlich.
