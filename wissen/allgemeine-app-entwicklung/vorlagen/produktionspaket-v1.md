# Produktionspaket v1.1 – Vorlage für jede App

Diese Vorlage wird pro App kopiert, projektspezifisch ausgefüllt und mit der [Evidenz-Matrix](./evidenz-matrix.md) verbunden. Ein Feld ohne Beleg gilt nicht als bestanden.

## 1. App-Steckbrief

- Name:
- Version/Build:
- Plattformen:
- Zielgruppe:
- Kernproblem:
- Kernnutzen:
- Verantwortlicher:
- Supportzeitraum:
- geplanter Release:
- letzter Gesamtcheck:

## 2. Entscheidung und Risiko

- Ergebnis des Entscheidungsassistenten:
- Risikostufe:
- vor Entwicklung zu klärende Blocker:

| Thema | Ja/Nein/Offen | Entscheidung | Beleg/Prüfer | Prüfdatum | nächste Prüfung |
|---|---|---|---|---|---|
| personenbezogene Daten | | | | | |
| besondere/sensible Daten | | | | | |
| Konten/Rollen | | | | | |
| KI | | | | | |
| automatisierte Entscheidungen | | | | | |
| Minderjährige | | | | | |
| Nutzerinhalte/Community | | | | | |
| Gesundheit/Medizin | | | | | |
| Finanzen/Zahlungen | | | | | |
| Hardware/IoT | | | | | |
| Tracking/Werbung | | | | | |
| Offline-Synchronisation | | | | | |

## 3. Produkt

- Problembelege:
- letzte reale Problemsituationen:
- wichtigste heutige Alternative:
- Produktversprechen:
- MVP:
- Nicht-Ziele:
- Aktivierungsmetrik:
- Retention-Metrik:
- wirtschaftliche Kernannahme:
- Kill-Kriterien:
- Evidenzlinks:

## 4. User Flows und Screens

| Flow/Screen | Ziel | primäre Aktion | Daten | Loading | Empty | Error | Offline | Success | Accessibility | Test/Beleg |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |

- getesteter Prototyp:
- Testpersonen/Zielgruppe:
- schwere gefundene Probleme:
- behobene Probleme:
- offene UX-Risiken:

## 5. Designsystem

- Figma-Datei:
- Token-Datei:
- Komponentenvertrag:
- Light/Dark Mode:
- responsive/adaptive Regeln:
- Motion/Reduced Motion:
- Asset- und Lizenzregister:
- Visual-Regression- oder Screenshotnachweis:

## 6. Plattform und Architektur

- Plattformentscheidung/ADR:
- Client:
- Backend/API:
- Auth:
- Datenbank:
- Storage:
- KI:
- Zahlung:
- Push/E-Mail:
- Analytics:
- Monitoring:
- Datenregion:
- RPO/RTO:
- Kosten bei 100/1.000/10.000 aktiven Nutzern:
- Upgrade-/Exit-Plan:
- schwierigster technischer Spike und Ergebnis:

## 7. Datenmodell und Berechtigungen

| Ressource | Eigentümer/Mandant | Rolle | Lesen | Erstellen | Ändern | Löschen | Negativtest | Beleg |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

- Constraints und Indizes:
- Migrationen:
- Views/Functions/Storage/Realtime geprüft:
- alte Clientversionen berücksichtigt:
- Datenkonsistenznachweis:

## 8. Anbieter und SDKs

| Anbieter | Zweck | Daten | Region | Vertrag/DPA | Consent | Löschung | Ausfallplan | Prüfdatum |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

## 9. KI-Systeme

| Funktion | Modell/Prompt-Version | Input | Output | Risiko | Transparenz | Evaluation | Kostenlimit | Fallback/Kill Switch | Beleg |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

- RAG-Quellen und Berechtigungen:
- Prompt-Injection-/Exfiltrationstest:
- menschliche Aufsicht/Eskalation:
- Modellwechsel-/Rollbackplan:

## 10. Zahlungen und Entitlements

- Modell/Plan:
- Store/Web:
- Server-Verifikation:
- internes Entitlement-Modell:
- Webhook-Signatur und Idempotenz:
- Restore:
- Testphase/Grace Period:
- Refund/Chargeback:
- Kontolöschung mit aktivem Abo:
- Sandbox-/Testbelege:
- Supportweg:

## 11. Security

| Bedrohung | Auswirkung | Prävention | Erkennung | Reaktion | Test/Beleg | Restrisiko |
|---|---|---|---|---|---|---|
| | | | | | | |

- Admin-MFA:
- Secret-Management/Rotation:
- Rate Limits/Bot-Schutz:
- Uploadschutz:
- Dependency-/Secret-/Lizenzscan:
- Pentest oder fokussierter manueller Test:
- Incident-Kontakte:
- Vulnerability-Disclosure-Weg:

## 12. Datenschutz, Export und Löschung

| Datenart | Zweck/Grundlage | Dauer | Primärsystem | Kopien/Drittanbieter | Löschprozess | Ausnahme | Beleg |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

- Exportformat und Test:
- In-App-Löschweg:
- externer Löschweg:
- Identitätsprüfung:
- Storage/Suche/Cache/Provider berücksichtigt:
- Backup-Löschung:
- Store-Angaben abgeglichen:
- Breach-Prozess:

## 13. Teststrategie

| Ebene | Kernfälle | Grenz-/Fehlerfälle | Umgebung/Gerät | automatisiert | Beleg | Status |
|---|---|---|---|---|---|---|
| Unit | | | | | | |
| Integration | | | | | | |
| E2E | | | | | | |
| Autorisierung/Security | | | | | | |
| Accessibility | | | | | | |
| Performance | | | | | | |
| Recovery/Restore | | | | | | |
| Store/Release-Build | | | | | | |

- Plattform-/Gerätetestmatrix:
- Testdatenstrategie:
- offene bekannte Fehler:
- Regressionen blockieren Release ab Schweregrad:

## 14. Performance, Zuverlässigkeit und Kosten

- Zeit bis nutzbarer Kernscreen:
- Interaktionsbudget:
- API-p50/p95:
- Crash-/Fehlerziel:
- Kernablauf-SLO:
- KI-Latenz-/Kostenbudget:
- Storage/Bandbreite:
- große Datenbestände getestet:
- langsames Netz/Offline getestet:
- Kostenwarnungen und harte Limits:
- letzte Messung und Beleg:

## 15. Betrieb und Runbooks

- Monitoring-Dashboard:
- Alarme:
- verantwortliche Person/Eskalation:
- Auth-Ausfall-Runbook getestet:
- DB-Migration/Rollback getestet:
- KI-Anbieter-Ausfall getestet:
- Security-/Datenschutzvorfall geübt:
- Backup/Restore-Test:
- Feature Flags/Kill Switch:
- Supportprozess:
- Wartungsrhythmus:
- End-of-Life-Kriterien:

## 16. Store-/Web-Abgleich

- Beschreibung und Screenshots entsprechen echter App:
- App Privacy/Data Safety abgeglichen:
- Privacy Policy erreichbar und korrekt:
- Impressum/Anbieterinformationen, soweit anwendbar:
- Altersfreigabe/Zielgruppe:
- Berechtigungsbeschreibungen:
- Kontolöschung:
- Käufe/Abos:
- Review-Konto und Review Notes:
- Support-/Status-/Lösch-URLs:
- gestaffelter Rollout:

## 17. Evidenzbasierte Qualitätsbewertung

| Bereich | anwendbar | 0–5 | Mindestwert | Evidenzlink | offene Lücke |
|---|---|---:|---:|---|---|
| Produktnutzen | | | 4 | | |
| UX | | | 3 | | |
| visuelle Qualität | | | 3 | | |
| Accessibility | | | 3 | | |
| Architektur | | | 3 | | |
| Daten/Autorisierung | | | risikobasiert | | |
| Security | | | risikobasiert | | |
| Datenschutz/Recht | | | risikobasiert | | |
| Funktionalität | | | 4 | | |
| Performance/Zuverlässigkeit | | | 3 | | |
| Monetarisierung/Kosten | | | risikobasiert | | |
| Betrieb/Verbesserung | | | 3 | | |

- erreichte Punkte:
- maximal anwendbare Punkte:
- Qualitätsquote:
- risikobasierte Mindestwerte erfüllt:
- Blocker:
- abgelaufene/fehlende Evidenz:
- akzeptierte Restrisiken:
- zweite Prüfperspektive:
- Go/No-Go:
- Freigabe durch:
- Datum:

## 18. Nach Release

- tägliche Kontrolle:
- wöchentliche Kontrolle:
- monatliche Kontrolle:
- quartalsweiser Restore-/Incident-Test:
- halbjährlicher Daten-/Accessibility-/Anbieterreview:
- jährliche Rechts-, Store-, Plattform- und Gesamtprüfung:
- nächste Neubewertung:
