# Veröffentlichung – Web, Apple App Store und Google Play

Dieses Kapitel führt von der fertigen Testversion bis zu einer überwachten öffentlichen Veröffentlichung. Die konkrete Oberfläche der Anbieter kann sich ändern; die erforderlichen Entscheidungen, Unterlagen und Nachweise bleiben weitgehend gleich.

## Ergebnis dieses Kapitels

- veröffentlichungsfähiger Release Candidate;
- korrekte Version und signierter Build;
- vollständiges Store- oder Web-Paket;
- erreichbare Privacy-, Support- und Löschseiten;
- Beta- und Reviewkonten;
- Rollout-, Monitoring- und Rollbackplan;
- dokumentierte Go-/No-Go-Entscheidung.

## 1. Veröffentlichungskanäle

| Kanal | Geeignet für | Zusätzliche Anforderungen |
|---|---|---|
| Web-App | schnelle globale Bereitstellung | Domain, TLS, Hosting, Browser, Cookies, SEO und Web-Sicherheit |
| PWA | installierbare Web-Erfahrung | Manifest, Icons, Service Worker, Offline- und Updateverhalten |
| Apple App Store | iPhone, iPad und weitere Apple-Plattformen | Entwicklerkonto, Signierung, Datenschutzangaben und Review |
| Google Play | Android-Geräte | Entwicklerkonto, App-Signierung, Data Safety und Policy-Prüfung |
| Enterprise/Internal | Organisationen und interne Nutzer | Geräteverwaltung, Verträge, Rollen, Support und Verteilung |
| Alternative Stores/Direct | besondere Märkte oder Desktop | jeweilige Regeln, Signierung, Updates und Nutzervertrauen |

## 2. Release Candidate

Ein Release Candidate wird aus einem festgelegten Commit erzeugt. Er enthält keine unbekannten Änderungen mehr.

Pflichten:

- Versionsnummer und Buildnummer;
- reproduzierbarer Build;
- zugehörige Migrationen;
- Changelog;
- bekannte Restrisiken;
- Testbericht;
- Signierungs- und Berechtigungsprüfung;
- Support- und Incidentkontakte;
- Rollback- oder Hotfixweg.

## 3. Pflichtunterlagen

Je nach App:

- Produktname und Betreiber;
- App-Beschreibung;
- Kategorie und Zielgruppe;
- Altersfreigabe;
- Screenshots je Geräteklasse;
- App-Icon und weitere Grafiken;
- Vorschauvideo;
- Support-URL;
- Datenschutzerklärung;
- Anbieter-/Impressumsinformationen;
- externe Kontolöschseite;
- Nutzungsbedingungen;
- Community-Regeln;
- Reviewkonto und Review Notes;
- Daten- und Berechtigungsangaben;
- Kauf- und Aboinformationen;
- Lizenz- und Open-Source-Hinweise;
- Kontakt für Behörden, Datenschutz und Support, soweit nötig.

Alle Angaben müssen der tatsächlich veröffentlichten App entsprechen.

## 4. Website vor dem Store

Auch eine mobile App benötigt häufig eine kleine, zuverlässige Webbasis:

```text
Start-/Landingpage
Datenschutzerklärung
Support/Kontakt
Kontolöschung
Nutzungsbedingungen
Statusseite oder Störungshinweise
Presse-/Medienpaket
```

Die Seiten müssen öffentlich erreichbar, mobil nutzbar, aktuell und dem Betreiber eindeutig zugeordnet sein.

## 5. Apple-Vorbereitung

Aktuelle Primärquellen stehen im Quellenregister. Vor Einreichung prüfen:

- Bundle-ID und App-Datensatz;
- Zertifikate, Signierung und Teamzugänge;
- Entitlements und Geräteberechtigungen;
- App Privacy;
- Altersfreigabe;
- In-App-Käufe und Abos;
- Kontolöschung;
- Login- und Reviewkonto;
- Export-/Verschlüsselungsfragen;
- Screenshots und Metadaten;
- Review Notes für schwer auffindbare Funktionen;
- Verhalten bei abgelehnten Berechtigungen;
- keine unvollständigen oder versteckten Pflichtfunktionen.

Bei Konten und Abos sind Kontolöschung und Store-Abonnement getrennt zu erklären und technisch korrekt zu behandeln.

## 6. Google-Play-Vorbereitung

Aktuelle Primärquellen stehen im Quellenregister. Vor Einreichung prüfen:

- eindeutiger Paketname;
- App-Signierung und Schlüsselverwaltung;
- Ziel- und Mindestplattform entsprechend aktueller Vorgaben;
- Berechtigungen;
- Data Safety;
- Datenschutzrichtlinie;
- Kontolöschung in der App und externe Webressource, falls Konten vorhanden sind;
- Inhalts- und Altersangaben;
- Käufe und Abos;
- Testzugänge;
- SDKs, Werbung und sensible Daten;
- Store-Metadaten und Screenshots;
- Richtlinienstatus ohne offene Blocker.

## 7. Web-Veröffentlichung

Vor Veröffentlichung:

- Produktionsdomain und TLS;
- sichere Header und Content Security Policy entsprechend Architektur;
- Cookie-/Trackingentscheidung;
- robots.txt und Sitemap, falls öffentlich auffindbar;
- Caching und CDN;
- Fehlerseiten;
- Monitoring und Logs;
- Backup und Restore;
- Datenbankmigration;
- Rollback auf vorherige Version;
- Datenschutz-, Support- und Löschseiten;
- Status- und Incidentweg.

## 8. Beta-Test

### Interne Alpha

- Team und technische Tester;
- Kernablauf;
- Migration und Recovery;
- keine produktiven Nutzerdaten.

### Geschlossene Beta

- passende Zielgruppe;
- klare Testaufgaben;
- Feedbackformular;
- Gerät-, Browser- und Versionsmatrix;
- Supportweg;
- Messung von Aktivierung, Fehlern und Abbrüchen.

### Offene Beta, falls sinnvoll

- bekannte Grenzen offen kommunizieren;
- Daten und Support skalierbar;
- Rollback- und Missbrauchsschutz;
- keine Beta als Ersatz für erforderliche Produktionsreife.

## 9. Store-Review

Review Notes enthalten:

- Zweck der App;
- Testkonto und Rollen;
- Weg zur Kernfunktion;
- Erklärung ungewöhnlicher Berechtigungen;
- Hardware- oder Standortanforderungen;
- Testdaten;
- Käufe, Abos oder externe Dienste;
- Kontolöschung;
- Kontakt bei Rückfragen.

Bei Ablehnung:

1. genaue Regel und betroffene Funktion erfassen;
2. nicht defensiv oder spekulativ antworten;
3. Produkt, Metadaten oder Technik korrigieren;
4. Nachweise aktualisieren;
5. erneut einreichen oder begründet widersprechen.

## 10. Rollout

```text
interner Test
→ kleine Nutzergruppe
→ größere Gruppe
→ vollständige Veröffentlichung
```

Je Stufe beobachten:

- Installationen und Aktivierung;
- Crashes und Fehler;
- Login und Kernablauf;
- Datenbank und Migrationen;
- Zahlungen;
- KI- und API-Kosten;
- Supportfälle;
- Bewertungen und Missbrauch.

## 11. Rollback und Hotfix

Vor Veröffentlichung festlegen:

- welche Änderungen serverseitig abschaltbar sind;
- Feature Flags und Kill Switches;
- kompatible Datenbankmigrationen;
- vorherige Webversion;
- Store-Hotfixprozess;
- Umgang mit bereits installierten alten Clients;
- Kommunikation an Nutzer;
- Datenkorrektur und Restore.

Ein Rollback darf Daten nicht weiter beschädigen.

## 12. Go-/No-Go-Gate

Kein GO bei:

- fremdem Datenzugriff;
- ungeklärtem Datenverlust;
- fehlender Kontolöschung;
- falschen Datenschutz- oder Store-Angaben;
- manipulierbarer Abrechnung;
- kritischem Crash im Kernablauf;
- ungeklärter Hochrisikofrage;
- fehlendem Monitoring oder verantwortlichem Support;
- nicht getesteter Migration ohne sicheren Rückweg.

## 13. Nach dem Release

Die ersten Stunden und Tage benötigen erhöhte Beobachtung:

- Kernmetriken und Alarme;
- Store- und Supportnachrichten;
- Fehlertrend nach Version;
- Kosten und Limits;
- Zahlungs- und Löschprozesse;
- Nutzerfeedback;
- Entscheidung über Fortsetzung, Stopp oder Rollback.

Die Veröffentlichung ist ein Übergang in den Betrieb, nicht das Ende des Projekts.
