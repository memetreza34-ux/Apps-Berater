# App umsetzen: vom Repository zum vollständigen Kernablauf

Dieses Kapitel beschreibt die praktische Reihenfolge der Entwicklung mit KI. Es verhindert, dass ein Agent große Mengen unverbundenen Code erzeugt, während zentrale Daten-, Sicherheits- und Betriebsfragen offen bleiben.

## Ziel

Am Ende existiert ein vollständiger, getesteter vertikaler Kernablauf in Development und Staging. Die App besitzt ein reproduzierbares Setup, klare Agentenregeln, Datenmigrationen, Fehlerzustände und Nachweise.

## 1. Repository vorbereiten

Mindestens:

```text
README.md
CONTRIBUTING.md
SECURITY.md
.env.example
docs/
src/
tests/
migrations/
scripts/
evidence/
```

Die konkrete Struktur hängt vom Stack ab. Wichtig sind klare Verantwortlichkeiten und reproduzierbares Setup.

README enthält:

- Produktzweck;
- aktuellen Scope;
- Architekturüberblick;
- Setup;
- Umgebungen;
- Tests und Builds;
- Deployment;
- bekannte Grenzen;
- Links zu PRD, Design und Betrieb.

## 2. Umgebungen trennen

```text
Development
Staging
Production
```

Je Umgebung getrennt:

- Datenbank;
- Nutzer;
- Storage;
- API-Schlüssel;
- Webhooks;
- Redirect-URLs;
- E-Mail-/Push-Ziele;
- Analytics;
- Monitoring;
- Kostenlimits.

Keine echten Produktionsdaten ungeprüft in Development kopieren.

## 3. Secrets verwalten

- keine Secrets im Repository;
- keine privilegierten Schlüssel im Client;
- `.env.example` nur mit Platzhaltern;
- Secrets je Umgebung;
- Rotation dokumentieren;
- Zugriff minimal halten;
- Logs und Screenshots prüfen;
- kompromittierte Schlüssel sofort widerrufen.

## 4. Agentenregeln

Der Coding-Agent liest zuerst:

- README;
- Risikoprofil;
- PRD;
- Funktionsdossier;
- User Flow und Screen-Inventar;
- Designsystem;
- Architektur;
- Datenmodell;
- Berechtigungsmatrix;
- Testplan.

Er beginnt mit:

1. Bestandsanalyse;
2. Risiken und Blocker;
3. kleinem Implementierungsplan;
4. offenen Fragen.

Noch keine große Änderung, bevor Scope und Plan geprüft wurden.

## 5. Grundgerüst

Zuerst:

- Routing/Navigation;
- Design Tokens;
- Basiskomponenten;
- Fehlergrenze;
- Konfiguration;
- Datenzugriffsschicht;
- Auth-Grundlage;
- Logging/Monitoring-Grundlage;
- Test-Setup;
- CI-Basis.

Keine vollständige App mit Mock-Erfolgen vortäuschen.

## 6. Erster vertikaler Kernablauf

Beispiel:

```text
Nutzer erstellt Aufgabe
→ Formular
→ Validierung
→ Sessionprüfung
→ serverseitige Autorisierung
→ Datenbank-Insert
→ Erfolg/Fehler
→ Liste aktualisieren
→ App-Neustart
→ Daten weiterhin vorhanden
→ automatischer Test
```

Pflichtprüfungen:

- gültige Eingabe;
- ungültige Eingabe;
- abgelaufene Session;
- keine Berechtigung;
- Netzwerkfehler;
- Doppel-Tap/Doppel-Request;
- App-Neustart;
- Nutzer A gegen Nutzer B;
- Löschen und Wiederherstellung entsprechend Produktregel.

## 7. Formulare und Validierung

Validierung auf mehreren Ebenen:

- UI für schnelle Rückmeldung;
- Server/API als Vertrauensgrenze;
- Datenbank mit Constraints.

Prüfen:

- Pflichtfelder;
- Längen;
- Wertebereiche;
- Dateitypen;
- unerwartete Felder;
- Unicode und Sonderzeichen;
- doppelte Aktionen;
- Fehlermeldungen;
- Accessibility.

## 8. Authentifizierung

Implementieren und testen:

- Registrierung;
- Bestätigung;
- Login;
- Logout;
- Recovery;
- Sessionablauf;
- Gerätewechsel;
- Sperren/Löschen;
- optional MFA/Passkeys;
- Adminschutz.

Keine Information preisgeben, ob ein Konto existiert, wenn dies Missbrauch erleichtert.

## 9. Autorisierung

Für jede Ressource getrennt:

```text
Rolle × Ressource × Aktion
```

Aktionen:

- lesen;
- erstellen;
- ändern;
- löschen;
- teilen;
- exportieren;
- moderieren;
- administrieren.

Serverseitig durchsetzen und negative Tests schreiben.

## 10. Datenbank und Migrationen

- Primär-/Fremdschlüssel;
- Constraints;
- Indizes;
- Eigentümer/Mandant;
- Zeitstempel;
- Statusfelder;
- Aufbewahrung;
- Löschregeln;
- Auditbedarf.

Migrationen versionieren und zuerst in Staging testen.

## 11. Datei-Uploads

- maximale Größe;
- erlaubte Typen;
- tatsächlichen Inhalt prüfen;
- private/public Buckets;
- Pfad und Eigentümer;
- signierte URLs;
- Malware-/Inhaltsprüfung nach Risiko;
- Bild-/Medienvarianten;
- Löschung und Export;
- Kostenlimits.

## 12. Listen, Suche und Pagination

Keine unbegrenzten Datenmengen laden.

Planen:

- Seitengröße;
- Cursor oder Offset;
- Sortierung;
- Filter;
- Suchindex;
- Berechtigungsfilter;
- leere Ergebnisse;
- langsame Abfrage;
- Cache;
- Datenschutz bei Suchlogs.

## 13. Offline und Retry

Für jede Aktion klassifizieren:

- online erforderlich;
- offline lesbar;
- offline schreibbar;
- später synchronisieren;
- nicht wiederholbar.

Benötigt:

- lokaler Status;
- Retryregeln;
- Idempotenz;
- Konfliktstrategie;
- Nutzerfeedback;
- Abbruch;
- Datenverlustschutz.

## 14. Push, E-Mail und Deep Links

Jede Nachricht benötigt:

- Zweck;
- Zielgruppe;
- Auslöser;
- Frequenz;
- Inhalt;
- sensible Daten;
- Opt-out;
- Deep-Link-Ziel;
- Fehler-/Unsubscribe-Verhalten;
- Messung.

## 15. Admin und Support

Nicht erst nach Release planen.

Mögliche Funktionen:

- Nutzer suchen;
- Konto sperren;
- Moderationsfall bearbeiten;
- Zahlungsreferenz prüfen;
- Job erneut starten;
- Auditlog sehen;
- Datenexport/Löschung verfolgen;
- Feature Flag ändern;
- Supportnotiz.

Adminfunktionen benötigen besonders strenge Rechte, MFA, Audit und minimale Datenanzeige.

## 16. KI-Funktionen

Schichten:

```text
UI
→ serverseitiges Gateway
→ Auth und Rechte
→ Validierung
→ Kosten-/Rate-Limit
→ optionale Moderation
→ Modell/RAG/Tools
→ strukturierte Output-Prüfung
→ Ergebnis/Fallback
```

Pflicht:

- Modell- und Promptversion;
- Eingabe-/Ausgabeschema;
- Goldenset;
- Prompt-Injection-Tests;
- Datenexfiltrationstest;
- RAG-Berechtigungen;
- Tool-Berechtigungen;
- Kostenlimit;
- Timeout/Abbruch;
- Fallback;
- Kill Switch;
- Transparenz;
- Löschung/Export.

## 17. Zahlungen vorbereiten

Vor echter Integration:

- Produkt-/Plan-IDs;
- Preisquelle;
- Plattformen;
- Entitlement-Modell;
- Serververifikation;
- Webhooks;
- Restore;
- Kündigung;
- Refund/Chargeback;
- Grace Period;
- Kontolöschung;
- Supportprozess.

## 18. Fehlerbehandlung

Fehler klassifizieren:

- Nutzerfehler;
- Berechtigungsfehler;
- Netzwerk;
- Anbieter;
- Datenkonflikt;
- Server;
- unbekannt.

Nutzer sehen eine verständliche Aktion. Entwickler erhalten strukturierte Diagnose ohne Secrets oder unnötige personenbezogene Daten.

## 19. Performance während der Umsetzung

Früh vermeiden:

- große Bilder;
- zu viele Startrequests;
- nicht paginierte Listen;
- N+1-Abfragen;
- fehlende Indizes;
- unnötige Re-Renders;
- blockierende Arbeit im UI-Thread;
- KI ohne Streaming/Timeout;
- unkontrolliertes Logging.

Erst messen, dann gezielt optimieren.

## 20. Tests je Änderung

Passend zum Risiko:

- Unit;
- Integration;
- E2E;
- Autorisierungs-Negativtest;
- Accessibility;
- Screenshot/visuell;
- Performance;
- manuelle Geräteprüfung.

Keine Tests löschen oder abschwächen, nur um CI grün zu machen.

## 21. Pull Request

Jeder PR enthält:

- Ziel;
- Nicht-Ziele;
- geänderte Dateien;
- Screenshots/Video bei UI;
- Daten-/Migrationseffekt;
- Security/Privacy-Effekt;
- Tests und Ergebnisse;
- Rollback;
- offene Risiken;
- Dokumentationsänderungen.

## 22. Fertigstellung einer Funktion

Eine Funktion ist fertig, wenn:

- Akzeptanzkriterien erfüllt;
- alle Zustände umgesetzt;
- Rechte serverseitig;
- Datenmodell/Migration korrekt;
- Tests passend zum Risiko;
- reale UI geprüft;
- Fehler/Offline/Doppelaktion geklärt;
- Monitoring vorhanden;
- Datenschutz/Security dokumentiert;
- Rollback möglich;
- Dokumentation und Evidenz aktuell.

## KI-Einsatz

KI kann Code, Tests, Migrationen, Dokumentation und Reviews vorbereiten. Sie arbeitet nur in kleinen bestätigten Schritten.

Menschliche Pflicht:

- Scope freigeben;
- gerenderte App prüfen;
- echte Tests ausführen;
- Daten- und Rechtefolgen kontrollieren;
- Kosten und Anbieter prüfen;
- Migration/Release verantworten.

## Gate

**Gate bestanden:** Ein vollständiger Kernablauf funktioniert in Staging mit echten Daten, negativen Berechtigungstests, Fehlerfällen, reproduzierbarem Build und dokumentiertem Rollback.
