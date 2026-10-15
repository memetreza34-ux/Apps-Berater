# FocusFlow – Beispiel-Release-Dossier v1.0

Dieses fiktive Beispiel zeigt, wie die Vorlagen ausgefüllt werden. Es ist kein reales Store-Release.

## 1. Produkt

**Kernnutzen:** Nutzer starten innerhalb von 60 Sekunden eine fokussierte Arbeitssession für eine konkrete Aufgabe.

**MVP:**
- E-Mail-Login
- Projekte und Aufgaben
- Fokus-Session
- Tagesziel und einfache Statistik
- Export und Kontolöschung
- optionale KI-Aufgabenzerlegung

**Nicht-Ziele:**
- medizinische Behandlung
- Arbeitgeberüberwachung
- Community
- Werbung
- komplexes Projektmanagement

## 2. Zielmetriken

- mindestens 60 % der neuen Nutzer starten am ersten Tag eine Session;
- Median bis zur ersten Session unter 60 Sekunden;
- technischer Abbruch im Kernablauf unter 2 %;
- keine bestätigten Fälle fremden Datenzugriffs;
- KI-Kosten pro erfolgreicher Zerlegung unter projektspezifischem Budget.

## 3. Architektur

```text
React-Native-App
→ Supabase Auth/Data API
→ PostgreSQL mit RLS
→ Edge Function als KI-Gateway
→ Modellprovider
→ Monitoring/Analytics mit minimalem Event-Schema
```

## 4. Daten

- Profile
- Projekte
- Aufgaben
- Fokus-Sessions
- minimale KI-Nutzungsmetadaten

Vollständige KI-Rohprompts werden standardmäßig nicht dauerhaft gespeichert. Jede fachliche Tabelle trägt `user_id`, Constraints und passende Indizes.

## 5. Autorisierung

### Pflichtnegative Tests
- Nutzer A liest Projekt B: verweigert
- Nutzer A ändert Aufgabe B: verweigert
- anonymer Zugriff auf private Tabellen: verweigert
- manipulierte `user_id` beim Insert: verweigert
- direkte REST-Anfrage ohne UI: identische Regeln
- abgelaufene Session: erneute Authentifizierung

## 6. KI-Funktion

**Zweck:** Eine große Aufgabe in kurze, konkrete Schritte zerlegen.

Kontrollen:
- serverseitiger API-Key;
- Eingabelimit;
- kein medizinisches/finanzielles Versprechen;
- strukturierte Ausgabe mit Schema-Validierung;
- Rate- und Kostenlimit pro Nutzer;
- Timeout und manueller Fallback;
- Testset für Halluzination, Prompt Injection und ungeeignete Inhalte.

## 7. Datenschutz und Löschung

Kontolöschung erfasst:
- Auth-Nutzer;
- Profile, Projekte, Aufgaben und Sessions;
- KI-Nutzungsmetadaten;
- Storage-Objekte, falls später vorhanden;
- Analytics-Zuordnung soweit technisch/rechtlich erforderlich;
- externe Anbieter nach dokumentiertem Prozess.

Google-Play-Version benötigt zusätzlich einen externen Web-Löschweg. Store- und Datenschutzerklärungen werden gegen die realen Datenflüsse geprüft.

## 8. Tests

### Unit
- Sessiondauer
- Statusübergänge
- Validierung
- Zeitzone/Tagesziel

### Integration
- Auth + Profilerstellung
- CRUD + RLS
- KI-Gateway + Limits
- Export und Löschjob

### E2E
1. registrieren;
2. Aufgabe anlegen;
3. Session starten;
4. App schließen/öffnen;
5. Session abschließen;
6. Statistik prüfen;
7. Export;
8. Kontolöschung.

### Recovery
- Netzwerkverlust während Session;
- doppelter Abschlussrequest;
- fehlerhafte Migration in Staging;
- Restore-Test;
- KI-Provider nicht erreichbar.

## 9. Monitoring

- Auth-Fehler
- Start/Abschluss einer Fokus-Session
- API-/RLS-Fehler
- KI-Latenz, Fehler und Kosten
- Kontolöschjob
- Crashrate

Keine Aufgabeninhalte in Standardlogs.

## 10. Releaseplan

1. interne Testkonten;
2. kleine geschlossene Beta;
3. Blocker schließen;
4. 5-%-Rollout;
5. 24 Stunden Kernmetriken prüfen;
6. 20 %, 50 %, 100 % nur bei stabiler Lage;
7. Kill Switch für KI-Funktion.

## 11. Beispielbewertung

| Bereich | Punkte |
|---|---:|
| Produktnutzen | 4 |
| UX | 4 |
| visuelle Qualität | 4 |
| Accessibility | 4 |
| Architektur | 4 |
| Daten/Autorisierung | 5 |
| Security | 4 |
| Datenschutz/Recht | 4 |
| Funktionalität | 4 |
| Performance/Zuverlässigkeit | 4 |
| Monetarisierung/Kosten | 3 |
| Betrieb/Verbesserung | 4 |

**Gesamt:** 48/60 – Beta, noch kein öffentlicher Release nach dem v1.0-Qualitätsmaßstab.

## 12. Offene Punkte vor Release Candidate

- Zahlungsmodell final entscheiden;
- Accessibility-Test mit realem Screenreader;
- Restore-Test dokumentieren;
- KI-Goldset erweitern;
- Support- und Statusseite veröffentlichen;
- Store-Datenschutzformulare final mit Produktionsbuild abgleichen.

Dieses Beispiel zeigt: Auch eine technisch weit entwickelte App wird nicht künstlich als „perfekt“ bezeichnet. Offene Nachweise bleiben sichtbar.
