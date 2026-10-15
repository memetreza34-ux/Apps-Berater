# Checkliste vor jedem Release v1.1

Ein Release darf erst freigegeben werden, wenn alle anwendbaren Punkte geprüft und in der Evidenz-Matrix belegt wurden. Ein angekreuzter Punkt ohne Beleg gilt als offen.

## Release-Identität

- [ ] Version, Build, Commit und Zielumgebung eindeutig
- [ ] Release-Dossier und Evidenz-Matrix beziehen sich auf genau diesen Stand
- [ ] verantwortliche Person und zweite Prüfperspektive benannt
- [ ] Entscheidungsassistent/Risikoprofil seit letzter wesentlicher Scopeänderung aktualisiert

## Produkt

- [ ] PRD und Akzeptanzkriterien aktuell
- [ ] keine unfertige Pflichtfunktion
- [ ] keine Platzhalter/Fake-Erfolge im Produktionspfad
- [ ] Kernablauf auf echtem Gerät/Browser vollständig getestet
- [ ] Texte, Preise und Versprechen entsprechen der echten Funktion
- [ ] Produktnutzen erreicht mindestens Evidenzstufe 4

## UX/UI und Accessibility

- [ ] Loading, Empty, Error, Offline und Success
- [ ] Tastatur, Formulare und Fokusreihenfolge
- [ ] lange Texte, kleine/große Geräte und Dark Mode
- [ ] Screenreader, Textskalierung, Kontrast und Touch-Ziele
- [ ] Reduced Motion und Alternative zu reinen Gesten
- [ ] keine blockierenden oder manipulativen Dark Patterns
- [ ] gerenderter Screenshot-/Gerätenachweis für den Release-Build

## Daten und Backend

- [ ] Migration zuerst auf Staging getestet
- [ ] Constraints, Fremdschlüssel und Indizes geprüft
- [ ] RLS/Autorisierung für jede Ressource
- [ ] Nutzer A kann Daten von Nutzer B weder lesen noch ändern
- [ ] Views, Functions, Storage und Realtime separat geprüft, soweit verwendet
- [ ] Pagination, Dateigrößen und Quoten
- [ ] Retry, Idempotenz und Doppelaktionen
- [ ] Datenexport und Kontolöschung Ende-zu-Ende
- [ ] alte unterstützte Clientversion gegen neue API/Migration getestet

## Auth und Security

- [ ] Registrierung, Login, Logout, Recovery und Kontowechsel
- [ ] abgelaufene und widerrufene Session
- [ ] Admin-MFA
- [ ] kein Secret im Client, Bundle, Git oder Log
- [ ] Rate Limits und Missbrauchsschutz
- [ ] Upload-, Dateityp- und Größenprüfung
- [ ] Dependency-, Secret- und Lizenzscan
- [ ] Threat Model aktuell
- [ ] kritische Findings geschlossen
- [ ] Security-/Datenschutz-Runbook getestet

## KI, falls anwendbar

- [ ] Modell- und Prompt-Version dokumentiert
- [ ] Goldenset und strukturierte Ausgaben
- [ ] Halluzinationen und Quellenprüfung
- [ ] Prompt Injection und Datenexfiltration
- [ ] Rechte vor Retrieval/RAG
- [ ] Kosten-, Rate-, Token- und Zeitlimit
- [ ] Fallback, Kill Switch und menschliche Eskalation
- [ ] Transparenzhinweis und AI-Act-Klassifizierung
- [ ] Modellwechsel-/Rollbackplan

## Zahlungen, falls anwendbar

- [ ] Produkte und Preise überall identisch
- [ ] serverseitige Verifikation und internes Entitlement
- [ ] signierte, idempotente Webhooks
- [ ] Kauf, Abbruch, Pending, Restore, Kündigung, Refund, Chargeback und Grace Period
- [ ] Geräte-, Store- und Accountwechsel
- [ ] Kontolöschung bei aktivem Abo
- [ ] Support kann zulässige Referenzen nachvollziehen
- [ ] Kostenmodell und harte Limits

## Datenschutz und Recht

- [ ] Dateninventar aktuell
- [ ] Anbieter, SDKs, Transfers und Verträge geprüft
- [ ] Privacy Policy entspricht tatsächlicher Technik
- [ ] App Privacy/Data Safety abgeglichen
- [ ] Consent und Widerruf korrekt
- [ ] Aufbewahrung, Export und Löschung praktisch getestet
- [ ] Impressum/Anbieterinformationen, soweit anwendbar
- [ ] Sonderfälle fachlich freigegeben
- [ ] Quellen und Regeln mit aktuellem Prüfdatum
- [ ] keine ungeklärte Hochrisiko-, Erlaubnis- oder Zulassungsfrage

## Qualität und Performance

- [ ] Unit-, Integrations-, E2E- und negative Tests grün
- [ ] Build reproduzierbar
- [ ] Start, Interaktion und API im Budget
- [ ] langsames Netz, Offline und Wiederverbindung
- [ ] großer Datenbestand
- [ ] Crash, Speicher und Akku entsprechend Plattform
- [ ] Plattform-/Gerätetestmatrix vollständig
- [ ] Qualitätsquote mindestens 83 %
- [ ] risikobasierte Mindestwerte erfüllt

## Store/Web

- [ ] Signierung, Entitlements und Permissions
- [ ] Screenshots und Beschreibung aktuell
- [ ] Altersfreigabe und Zielgruppe
- [ ] Review-Konto und Review Notes
- [ ] Support-, Privacy-, Status- und Lösch-URLs aktiv
- [ ] Kauf-/Abo-Metadaten
- [ ] keine defekten Links
- [ ] Release-Build entspricht geprüftem Commit

## Betrieb und Recovery

- [ ] Monitoring und Kernmetriken
- [ ] Alarm mit Runbook getestet
- [ ] Kostenwarnungen und harte Limits
- [ ] Backup und Restore praktisch getestet
- [ ] Datenbank-/App-Rollback getestet oder nachgewiesen
- [ ] Feature Flag/Kill Switch
- [ ] Supportverantwortung und Eskalation
- [ ] gestaffelter Rollout
- [ ] Incident-Kontakte
- [ ] Beobachtungsfenster und Stopkriterien

## Evidenzabschluss

- [ ] keine fehlenden Pflichtbelege
- [ ] keine abgelaufenen zeitabhängigen Belege
- [ ] Widersprüche zwischen PRD, Design, Code, Store und Datenschutz gelöst
- [ ] bekannte Restrisiken mit Owner, Termin und Entscheidung dokumentiert

## Go/No-Go

- Version/Build/Commit:
- Datum:
- erreichte Punkte:
- maximal anwendbare Punkte:
- Qualitätsquote:
- risikobasierte Mindestwerte erfüllt:
- offene Blocker:
- akzeptierte Restrisiken:
- Evidenzpaket:
- Rollback:
- Freigabe durch:
- zweite Prüfperspektive:
- Entscheidung: GO / NO-GO

> Kein GO bei fremdem Datenzugriff, möglichem Datenverlust ohne getestete Recovery, Secrets im Client/Repository, falscher Abrechnung, fehlender erforderlicher Löschung, offenem kritischem Security-Befund oder ungeklärter Hochrisiko-/Zulassungsfrage.
