# Vorlage – Berechtigungsmatrix

## Rollen

| Rolle | Beschreibung | Herkunft der Rolle | MFA | Besonderheit |
|---|---|---|---|---|
| | | | | |

## Ressourcen und Aktionen

| Rolle | Ressource | Listen | Lesen | Erstellen | Ändern | Löschen | Sonderaktion | Server/RLS-Kontrolle | Negativtest |
|---|---|---:|---:|---:|---:|---:|---|---|---|
| | | | | | | | | | |

## Mandanten- und Eigentumsregeln

- Eigentümerfeld:
- Mandantenfeld:
- Mitgliedschaftstabelle:
- Rollenwechsel:
- entfernte Mitglieder:
- Support-/Adminzugriff:

## Pflicht-Negativtests

- [ ] Nutzer A liest Ressource von B
- [ ] Nutzer A ändert Ressource von B
- [ ] Nutzer A setzt beim Erstellen eine fremde Eigentümer-ID
- [ ] Eigentümerwechsel über Update
- [ ] direkter API-/RPC-Aufruf ohne UI
- [ ] unauthentifizierter Zugriff
- [ ] abgelaufene Session
- [ ] normale Rolle auf Adminaktion
- [ ] entfernte Teammitgliedschaft
