# Supabase-RLS-Testmatrix

## Ziel

RLS wird nicht durch Lesen der SQL-Datei freigegeben. Jede Policy muss mit echten Rollen und Gegenbeispielen getestet werden.

## Testkonten

- Nutzer A
- Nutzer B
- Admin/Support-Rolle, falls vorhanden
- unauthentifizierter Client
- abgelaufene oder manipulierte Session

## Kernmatrix

| Test | A auf A | A auf B | Ohne Login | Admin | Erwartung |
|---|---:|---:|---:|---:|---|
| SELECT | erlaubt | verboten | verboten | projektspezifisch | nur berechtigte Zeilen |
| INSERT mit eigener user_id | erlaubt | – | verboten | projektspezifisch | Eigentümer korrekt |
| INSERT mit fremder user_id | verboten | verboten | verboten | projektspezifisch | WITH CHECK blockiert |
| UPDATE eigene Zeile | erlaubt | – | verboten | projektspezifisch | USING + WITH CHECK |
| UPDATE user_id auf fremd | verboten | verboten | verboten | projektspezifisch | Eigentümerwechsel blockiert |
| DELETE eigene Zeile | erlaubt | – | verboten | projektspezifisch | fachlich erlaubt? |
| DELETE fremde Zeile | verboten | verboten | verboten | projektspezifisch | keine IDOR/BOLA |

## Direkter API-Test

Die UI darf nicht Teil der Sicherheitsannahme sein.

Teste:

- bekannte UUID von Nutzer B direkt anfragen;
- Filter und Queryparameter manipulieren;
- Body mit fremder `user_id` senden;
- REST/RPC direkt aufrufen;
- Storage-URL und Pfad verändern;
- Realtime-Channel fremder Ressourcen abonnieren;
- Batch-/Upsert-Verhalten;
- Pagination und Joins.

## UPDATE-Sonderfall

Ein UPDATE kann eine passende SELECT-Policy benötigen. Teste getrennt:

1. Zeile ist lesbar und änderbar.
2. Zeile ist nicht lesbar.
3. Eigentümerfeld soll geändert werden.
4. Statusübergang ist fachlich unzulässig.

RLS ersetzt keine fachlichen Constraints. Statusübergänge können zusätzlich über Check Constraints, Trigger oder serverseitige Funktionen abgesichert werden.

## Mandantenmodell

Bei Organisationen/Teams prüfen:

- Mitgliedschaft aktiv?
- Rolle innerhalb des Mandanten?
- Einladung noch gültig?
- entfernte Mitglieder verlieren Zugriff sofort?
- Wechsel zwischen Mandanten?
- Owner darf sich selbst entfernen?
- Supportzugriff dokumentiert und zeitlich begrenzt?

## Storage-Matrix

| Aktion | Eigene Datei | Fremde Datei | Ohne Login | Nach Kontolöschung |
|---|---:|---:|---:|---:|
| Upload | erlaubt | verboten | verboten | verboten |
| Lesen | erlaubt | verboten | verboten | nicht vorhanden |
| Listen | nur eigene | keine fremden | verboten | leer |
| Ersetzen | projektspezifisch | verboten | verboten | verboten |
| Löschen | erlaubt | verboten | verboten | bereits gelöscht |

## Regression

Jede gefundene Autorisierungslücke erhält:

- reproduzierbaren Test;
- betroffene Rolle und Ressource;
- Ursache;
- SQL-/Code-Korrektur;
- Negativtest in CI;
- Prüfung ähnlicher Tabellen/Policies.

## Freigabeprotokoll

```text
Ressource:
Migration/Commit:
Tester:
Datum:
Rollen:
SELECT:
INSERT:
UPDATE:
DELETE:
Storage/Realtime/RPC:
Offene Risiken:
Freigabe:
```
