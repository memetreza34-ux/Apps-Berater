# Supabase-Produktionsleitfaden

## Ziel

Supabase beschleunigt die Entwicklung, nimmt dem App-Anbieter aber nicht die Verantwortung für Datenmodell, Rechte, Migrationen, Backups und Betrieb ab.

## Umgebungen

Mindestens getrennt:

```text
Development
Staging
Production
```

Jede Umgebung besitzt eigene:

- Projekt-URL und Schlüssel;
- Datenbank;
- Auth-Nutzer;
- Storage-Buckets;
- Provider-Credentials;
- Webhook-Ziele;
- Redirect-URLs;
- Monitoring- und Kostenalarme.

Produktionsdaten werden nicht ungeprüft in Development kopiert.

## Migrationen

### Regeln

- jede Schemaänderung als versionierte Migration;
- keine dauerhaften manuellen Dashboard-Änderungen ohne nachgezogene Migration;
- Migration zuerst lokal/Development, dann Staging, dann Production;
- Roll-forward bevorzugen;
- riskante Datenmigration in kleinen, wiederholbaren Schritten;
- Backfill und Schemaänderung bei großen Tabellen trennen.

### Sichere Reihenfolge bei Breaking Changes

```text
1. neue Spalte/Tabelle ergänzen
2. Code unterstützt alt und neu
3. Daten backfillen
4. Reads umstellen
5. Writes umstellen
6. alte Struktur nach Beobachtungszeit entfernen
```

## Row Level Security

RLS ist die Datenbank-Autorisierung, nicht nur ein zusätzlicher Filter.

### Eigentumsmodell

Jede nutzerbezogene Ressource benötigt eine eindeutige Beziehung zum Eigentümer oder Mandanten.

```sql
create table public.projects (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  title text not null check (char_length(title) between 1 and 120),
  created_at timestamptz not null default now()
);

create index projects_user_id_idx on public.projects(user_id);
alter table public.projects enable row level security;
```

### CRUD-Policies

```sql
create policy "projects_select_own"
on public.projects
for select
to authenticated
using ((select auth.uid()) = user_id);

create policy "projects_insert_own"
on public.projects
for insert
to authenticated
with check ((select auth.uid()) = user_id);

create policy "projects_update_own"
on public.projects
for update
to authenticated
using ((select auth.uid()) = user_id)
with check ((select auth.uid()) = user_id);

create policy "projects_delete_own"
on public.projects
for delete
to authenticated
using ((select auth.uid()) = user_id);
```

## Rollen und Claims

- `auth.uid()` für Nutzeridentität;
- Rollen nur aus vertrauenswürdigen, serverseitig kontrollierten Claims oder Tabellen;
- nutzeränderbare Metadaten nicht als alleinige Autorisierungsquelle;
- Adminaktionen möglichst über serverseitige Funktionen mit minimalen Rechten;
- Service Role nur in geschützter Serverumgebung.

## Views

Views müssen bewusst geprüft werden, weil sie abhängig von Definition und PostgreSQL-Konfiguration Rechte anders ausführen können.

Prüfe:

- wird RLS des aufrufenden Nutzers angewendet?
- ist `security_invoker` passend gesetzt?
- ist die View im exponierten Schema nötig?
- sind Spalten und Zeilen minimal?

## Functions

Bei Datenbankfunktionen:

- `SECURITY INVOKER` bevorzugen;
- `SECURITY DEFINER` nur bewusst;
- `search_path` festlegen;
- Execute-Rechte einschränken;
- Eingaben validieren;
- keine dynamischen SQL-Fragmente aus ungeprüften Eingaben;
- Seiteneffekte und Idempotenz dokumentieren.

## Storage

Für jeden Bucket getrennt prüfen:

- public oder private;
- Upload;
- Lesen;
- Listen;
- Update/Upsert;
- Löschen;
- Dateityp und Größe;
- Pfadkonvention;
- Eigentümerzuordnung;
- Malware-/Inhaltsprüfung entsprechend Risiko;
- Kontolöschung.

Beispielpfad:

```text
user-id/resource-id/original.ext
```

Der Client darf den Pfad nicht als alleinigen Sicherheitsmechanismus verwenden; Storage-Policies müssen die Eigentümerbeziehung prüfen.

## Auth

Prüfe:

- E-Mail-Bestätigung;
- sichere Redirect-URLs;
- Passwort-Reset;
- MFA für Admins;
- Sessionablauf;
- Abmeldung aller Geräte;
- Rate Limits und Bot-Schutz;
- Account-Zusammenführung;
- Löschen und Sperren;
- Verhalten bei Provider-Wechsel.

## Realtime

Realtime nur aktivieren, wenn die Funktion es benötigt.

Risiken:

- zu breite Channels;
- fremde Mandantendaten;
- hohe Verbindungen/Kosten;
- unkontrollierte Eventflut;
- UI verlässt sich auf Realtime statt verlässlichen Reload.

## Edge Functions

Geeignet für:

- geheime API-Schlüssel;
- Webhooks;
- KI-Gateway;
- Zahlungslogik;
- privilegierte Aktionen;
- serverseitige Validierung.

Benötigt:

- Auth- und Autorisierungsprüfung;
- Eingabevalidierung;
- Rate Limit;
- Timeout;
- Idempotenz;
- strukturierte Fehler;
- minimales Logging;
- Kostenlimit;
- Wiederholungsstrategie.

## Backup und Restore

Ein Backup gilt erst als brauchbar, wenn eine Wiederherstellung getestet wurde.

Dokumentiere:

- RPO;
- RTO;
- verantwortliche Person;
- Wiederherstellungsziel;
- Reihenfolge für DB, Storage, Auth und externe Systeme;
- letzte Übung;
- Ergebnis und offene Lücken.

## Produktionsfreigabe

- [ ] getrennte Umgebungen
- [ ] alle Migrationen reproduzierbar
- [ ] RLS und Grants geprüft
- [ ] zwei Nutzerkonten negativ getestet
- [ ] Views/Functions geprüft
- [ ] Storage-CRUD geprüft
- [ ] keine geheimen Schlüssel im Client
- [ ] Auth- und Recovery-Flows getestet
- [ ] Rate Limits und Kostenalarme
- [ ] Backup und Restore getestet
- [ ] Kontolöschung über alle Systeme getestet
