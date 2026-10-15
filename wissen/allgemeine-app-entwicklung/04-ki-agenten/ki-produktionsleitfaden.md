# KI-Produktionsleitfaden

## Ziel

Eine KI-Funktion ist erst produktionsreif, wenn Nutzen, Grenzen, Datenfluss, Kosten, Missbrauchsschutz und Fallback messbar definiert sind.

## Systemregister

Für jede KI-Funktion dokumentieren:

| Feld | Inhalt |
|---|---|
| Funktion | konkrete Nutzeraufgabe |
| Modell | Anbieter, Modellname, Version |
| Rolle | Provider/Deployer-Einordnung prüfen |
| Eingaben | Datenkategorien und Quellen |
| Ausgaben | Format und Weiterverwendung |
| Speicherung | Rohdaten, Logs, Dauer |
| Risiko | fachlich, rechtlich, Missbrauch |
| Transparenz | Hinweis an Nutzer |
| Aufsicht | menschliche Prüfung/Eskalation |
| Evaluation | Testset und Schwellenwerte |
| Kosten | Limit pro Nutzer/Funktion |
| Fallback | Verhalten bei Ausfall/Unsicherheit |

## Gateway-Architektur

```text
App
→ Authentifizierung
→ serverseitiges KI-Gateway
→ Autorisierung
→ Eingabevalidierung
→ Rate-/Kostenlimit
→ optionale Moderation
→ Modellprovider
→ strukturierte Output-Prüfung
→ Ergebnis oder sicherer Fehler
```

Geheime Modellschlüssel gehören nicht in Mobile- oder Web-Clients.

## Strukturierte Ausgaben

Freitext nur verwenden, wenn Freitext wirklich benötigt wird. Für Aktionen und Datenbankänderungen strukturierte Schemas erzwingen.

Beispiel:

```json
{
  "title": "Aufgabe vorbereiten",
  "steps": [
    {"text": "Material sammeln", "minutes": 5}
  ],
  "confidence": "medium",
  "warnings": []
}
```

Serverseitig prüfen:

- Schema;
- Längen und Wertebereiche;
- erlaubte Aktionen;
- Nutzerrechte;
- unerwartete Links/Markup;
- fachliche Plausibilität entsprechend Risiko.

## Evaluation

### Goldene Testfälle

- typische Kernfälle;
- schwierige, aber zulässige Fälle;
- unvollständige Eingaben;
- widersprüchliche Eingaben;
- Mehrsprachigkeit;
- Prompt Injection;
- Datenexfiltration;
- verbotene Inhalte;
- Halluzinationen;
- hohe Kosten/Latenz.

### Metriken

- Aufgaben-Erfolgsquote;
- gültiges Schema;
- fachliche Fehler;
- unbelegte Aussagen;
- Sicherheitsverstöße;
- Nutzerabbruch;
- p50/p95-Latenz;
- Kosten pro erfolgreicher Aufgabe.

## RAG

RAG benötigt:

1. dokumentierte Quellen;
2. Chunking-Strategie;
3. Metadaten;
4. Berechtigungsfilter vor Retrieval;
5. Versions- und Löschkonzept;
6. Quellenanzeige;
7. Tests für fehlende oder widersprüchliche Quellen.

RAG ist keine Garantie für Wahrheit. Das Modell kann Inhalte trotz Retrieval falsch zusammenfassen.

## Embeddings

Dokumentiere:

- Modell und Dimension;
- welche Inhalte eingebettet werden;
- ob personenbezogene Daten enthalten sind;
- Mandantenfilter;
- Neuindexierung bei Modellwechsel;
- Löschung der Vektoren;
- Kosten und Speicherbedarf.

## Caching

Cache nur, wenn Identität und Berechtigung berücksichtigt sind.

Cache-Key kann enthalten:

```text
feature + model-version + prompt-version + normalized-input + permission-scope
```

Keine nutzerübergreifende Wiederverwendung sensibler Antworten.

## Agenten mit Werkzeugen

Jedes Werkzeug braucht:

- kleinste mögliche Berechtigung;
- validiertes Eingabeschema;
- Lesend/Schreibend-Kennzeichnung;
- Bestätigung vor irreversiblen Aktionen;
- Idempotenzschlüssel;
- Zeit-/Schrittkostenlimit;
- Auditlog;
- Abbruch und Wiederaufnahme.

## Guardrails

Guardrails sind mehrere Schichten:

- Produkt-Scope;
- Systemanweisung;
- Eingabevalidierung;
- Retrieval-Berechtigung;
- Tool-Berechtigung;
- Output-Schema;
- Moderation;
- menschliche Aufsicht;
- Monitoring und Abschaltmöglichkeit.

## Modellwechsel

Vor Upgrade:

- Testset gegen alte und neue Version;
- Qualität, Sicherheit, Kosten und Latenz vergleichen;
- Prompt-/Schema-Kompatibilität;
- gestaffelter Rollout;
- Rollback;
- Modellversion im Register aktualisieren.

## Produktionsfreigabe

- [ ] KI-Systemregister vollständig
- [ ] serverseitiges Gateway
- [ ] Datenminimierung und Anbieterprüfung
- [ ] strukturierte Ausgabe, wo möglich
- [ ] Goldenset und Sicherheitsfälle
- [ ] Kosten-/Rate Limits
- [ ] Transparenz und menschliche Eskalation
- [ ] Fallback und Kill Switch
- [ ] Monitoring nach Modell-/Prompt-Version
- [ ] Löschung und Export berücksichtigt
