# Interaktiver App-Entscheidungsassistent

Der Assistent erzeugt aus den wichtigsten Risikofragen eine projektspezifische Liste aus Pflichtmodulen, Artefakten, Release-Mindestwerten und Themen, die vor der Kernentwicklung fachlich geklärt werden müssen.

## Interaktiv starten

Im Repository-Stamm:

```bash
python scripts/app_decision_assistant.py
```

## Mit Antwortdatei

Beispiel `app-answers.json`:

```json
{
  "personal_data": true,
  "accounts": true,
  "ai": true,
  "automated_decisions": false,
  "payments": true,
  "mobile": true
}
```

Ausführen:

```bash
python scripts/app_decision_assistant.py \
  --answers app-answers.json \
  --format markdown \
  --output APP-ENTSCHEIDUNG.md
```

JSON-Ausgabe für weitere Automatisierung:

```bash
python scripts/app_decision_assistant.py \
  --answers app-answers.json \
  --format json
```

## Fragen

Der Assistent prüft:

- personenbezogene und sensible Daten;
- Konten und Rollen;
- KI und automatisierte Entscheidungen;
- Nutzerinhalte;
- Minderjährige;
- Gesundheit und Medizin;
- Finanzen und Zahlungen;
- Hardware/IoT;
- Tracking/Werbung;
- Mobile-Release;
- Offline-Synchronisation.

## Grenzen

Das Ergebnis ist eine Vorprüfung, keine Rechts- oder Zulassungsentscheidung. Bei hohem Risiko erzeugt der Assistent ausdrücklich Blocker zur fachkundigen Klärung, statt eine automatische Freigabe vorzutäuschen.

## Test

```bash
python -m unittest discover -s scripts/tests -v
```
