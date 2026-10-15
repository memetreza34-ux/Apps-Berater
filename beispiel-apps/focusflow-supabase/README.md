# FocusFlow Supabase – Migration und RLS-Smoke-Test

Dieses Referenzpaket ergänzt die lokale PWA um eine konkrete Datenbankmigration und einen ausführbaren Negativtest mit zwei echten Testkonten.

## Inhalt

- `migrations/202608040001_focusflow.sql`: Tabellen, Constraints, Indizes, Grants und RLS-Policies;
- `rls-smoke.mjs`: Nutzer A erstellt einen Datensatz; Nutzer B darf ihn weder lesen, verändern noch löschen.

## Voraussetzungen

- isoliertes lokales oder Staging-Supabase-Projekt;
- Migration wurde dort angewendet;
- zwei bestätigte Testkonten ohne Produktionsdaten;
- Node.js mit eingebautem `fetch`;
- keine Service-Role für den Test verwenden.

## Umgebungsvariablen

```bash
export SUPABASE_URL="https://PROJECT.supabase.co"
export SUPABASE_ANON_KEY="..."
export USER_A_EMAIL="rls-a@example.test"
export USER_A_PASSWORD="..."
export USER_B_EMAIL="rls-b@example.test"
export USER_B_PASSWORD="..."
```

## Ausführen

```bash
node beispiel-apps/focusflow-supabase/rls-smoke.mjs
```

Erwartung:

```text
PASS: Nutzer A kann eigenes Projekt erstellen und lesen.
PASS: Nutzer B kann Projekt von A nicht lesen.
PASS: Nutzer B kann Projekt von A nicht ändern.
PASS: Nutzer B kann Projekt von A nicht löschen.
PASS: Nutzer A kann Testprojekt löschen.
```

## Sicherheitsregeln

- ausschließlich Testkonten und Testumgebung;
- Anon-Key darf clientseitig nutzbar sein, Service-Role niemals;
- Test schlägt fehl, wenn fremde Daten sichtbar oder veränderbar sind;
- Test für jede neue Ressource und Rolle erweitern;
- Views, Functions, Storage und Realtime benötigen eigene Tests;
- Ergebnis als CI-/Release-Evidenz speichern, aber keine Tokens loggen.

## Grenze

Der Test beweist nur die geprüften Operationen des geprüften Stands. Er ersetzt keine vollständige Berechtigungsmatrix, Migrationstests oder Security-Prüfung.
