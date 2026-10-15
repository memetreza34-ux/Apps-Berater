# Testen – alle Möglichkeiten auf einen Blick

Tests beweisen, dass die App wirklich funktioniert – nicht nur, dass die KI es behauptet. Diese Seite zeigt **jede Art von Test**: wofür sie gut ist, wann du sie brauchst und womit sie geht. Die Werkzeuge sind Beispiele; gleichwertige Alternativen sind in Ordnung.

Ausführlich: [Teststrategie und Release-Gates](./wissen/allgemeine-app-entwicklung/06-tests-release-betrieb/teststrategie-und-release-gates.md), Katalog [12 – Tests, Release und Betrieb](./wissen/ki-app-kriterienkatalog/12-tests-release-betrieb.md), [Plattform-Testmatrix](./wissen/allgemeine-app-entwicklung/vorlagen/plattform-testmatrix.md), [Supabase-RLS-Testmatrix](./wissen/allgemeine-app-entwicklung/03-technik/supabase-rls-testmatrix.md).

## Mindestumfang vor jedem Release

Ohne diese Punkte nicht veröffentlichen. Jeder braucht einen Nachweis (Testausgabe, Screenshot oder Protokoll).

1. Automatische Prüfungen grün: Lint, Typprüfung, Unit- und Integrationstests, Secret-Scan, Abhängigkeits-Scan.
2. **Zwei-Konten-Test:** Konto A sieht, ändert und löscht nie Daten von Konto B – über die Oberfläche **und** direkt über die Schnittstelle.
3. Kernablauf als End-to-End-Test und von Hand auf einem echten iPhone, einem echten Android-Gerät und im Safari-Browser.
4. Rollen und Tarife lassen sich nicht vom Client aus ändern; Admin-Bereiche sind ohne Rechte nicht erreichbar.
5. KI: Limits, Timeout, Fehlerfall (Anbieter langsam oder weg), Prompt-Injection-Liste, Evals grün.
6. Zahlungen im Testmodus komplett: kaufen, kündigen, widerrufen, fehlgeschlagene Zahlung, Käufe wiederherstellen.
7. Konto löschen: alle Daten weg, auch Dateien, Vektor-Einträge und Daten bei Drittanbietern.
8. Rechtsseiten erreichbar; vor der Einwilligung werden keine Tracker geladen.
9. Barrierefreiheit: automatischer Scan plus Screenreader- und Tastaturtest des Kernablaufs.
10. Backup einmal zurückgespielt, Rückroll-Weg bekannt, Fehlerüberwachung und Kostenalarm aktiv.

## Alle Testarten

### Code und Logik

| Test | Wofür | Wann | Werkzeuge |
|---|---|---|---|
| Statische Prüfung | Tippfehler, falsche Typen, unsicherer Code | bei jedem Push | ESLint, TypeScript `strict`, Ruff, Semgrep |
| Unit-Tests | einzelne Funktionen rechnen richtig (Preise, Limits, Datumslogik) | bei jedem Push | Vitest, Jest, pytest |
| Integrationstests | Zusammenspiel mit Datenbank, Auth, Zahlung, KI-Adapter | bei jedem Push | Vitest/Jest mit Testdatenbank, Supabase CLI lokal |
| Schnittstellen-Tests | API-Routen und Server Actions: Anmeldung, Besitz, Eingaben, Fehlercodes | bei jedem Push | Supertest, Playwright `request`, Bruno, Postman |
| Datenbank- und Zugriffsregel-Tests | Row Level Security, Firebase-Regeln, GRANTs | bei jeder Migration | pgTAP, Supabase-Testskripte, Firebase Emulator; [Beispiel](./beispiel-apps/focusflow-supabase/README.md) |
| Migrationstest | Migration läuft vorwärts und ist rückwärtskompatibel | vor jedem Deployment | Staging-Datenbank, `supabase db reset` |

### Ganze App

| Test | Wofür | Wann | Werkzeuge |
|---|---|---|---|
| End-to-End-Test | ein echter Nutzerweg von Anfang bis Ende | bei jedem Release, besser bei jedem Push | Playwright, Cypress; mobil Maestro, Detox |
| Echte Geräte | Verhalten auf iPhone, Android, Safari, kleinen Bildschirmen, alten Geräten | vor jedem Release | eigene Geräte, BrowserStack, Firebase Test Lab |
| Schlechtes Netz und offline | Laden, Abbrechen, Wiederholen, keine verlorenen Eingaben | vor jedem Release | Netzwerk-Drosselung im Browser, Flugmodus |
| Grenzwerte und Doppelaktionen | leere, sehr lange und falsche Eingaben, Doppelklick auf „Bezahlen“ | vor jedem Release | Testfälle im E2E-Test, von Hand |
| Visuelle Tests | Layout bricht nicht (Dunkelmodus, große Schrift, lange Texte) | bei Design-Änderungen | Playwright-Screenshots, Chromatic |

### Sicherheit

| Test | Wofür | Wann | Werkzeuge |
|---|---|---|---|
| Secret-Scan | keine Schlüssel im Code oder in der Git-Historie | bei jedem Push | GitHub Push Protection, gitleaks |
| Abhängigkeits-Scan | bekannte Lücken, Schadpakete | bei jedem Push und monatlich | `npm audit`, OSV-Scanner, Dependabot, Socket |
| Code-Scan | typische Schwachstellen | bei jedem Push | Semgrep, CodeQL |
| Dynamischer Scan | Lücken in der laufenden Web-App | vor jedem Release | ZAP-Baseline-Scan |
| Datenbank-Berater | offene Tabellen, fehlende Regeln | nach jeder Migration | Supabase Security Advisor |
| Getrennte KI-Sicherheitsprüfung | eine frische KI-Sitzung prüft den Code | nach riskanten Änderungen | [Prüf-Prompts](./wissen/ki-app-kriterienkatalog/PRUEF-PROMPTS.md) |
| Penetrationstest | Profis greifen gezielt an | vor großem Launch, bei sensiblen Daten | externe Prüfer |

### KI-Funktionen

| Test | Wofür | Wann | Werkzeuge |
|---|---|---|---|
| Evals (Testsammlung) | Qualität der Antworten bleibt gleich oder wird besser | vor jeder Änderung an Prompt, Modell oder RAG | Promptfoo, eigene Testliste, LLM-as-Judge |
| Prompt-Injection-Test | KI lässt sich nicht umlenken, verrät keinen verborgenen Kontext | vor jedem Release | eigene Angriffsliste, Promptfoo Red Teaming, garak |
| Datenabfluss-Test | keine Daten anderer Nutzer im Kontext oder in der Vektor-Suche | vor jedem Release | Zwei-Konten-Test mit RAG |
| Limit- und Kostentest | Kontingente, `max_tokens`, Ausgabenlimit greifen | vor jedem Release | Testskript mit vielen Anfragen |
| Ausfalltest | App bleibt nutzbar, wenn der KI-Anbieter langsam ist oder ausfällt | vor jedem Release | Fehler simulieren; [Runbook](./wissen/allgemeine-app-entwicklung/15-runbooks/ki-anbieter-ausfall.md) |
| Moderations- und Krisentest | schädliche Inhalte werden abgelehnt, Hilfsangebote erscheinen | vor jedem Release | Testliste mit kritischen Eingaben |
| Fairness- und Sprachentest | gleiche Qualität für verschiedene Gruppen und Sprachen | vor dem Launch | Testsammlung mit Varianten |

### Barrierefreiheit, Design und Nutzbarkeit

| Test | Wofür | Wann | Werkzeuge |
|---|---|---|---|
| Automatischer Barrierefreiheits-Scan | Kontrast, Beschriftungen, Struktur | bei jedem Release | axe, Lighthouse, Accessibility Inspector (Xcode), Accessibility Scanner (Android) |
| Screenreader-Test | App ist ohne Sehen bedienbar | vor jedem Release | VoiceOver, TalkBack, NVDA |
| Tastaturtest | Web vollständig ohne Maus bedienbar, Fokus sichtbar | vor jedem Release | von Hand |
| Textgröße und Zoom | 200 % Text, große Systemschrift, Querformat | vor jedem Release | Systemeinstellungen |
| Usability-Test | echte Menschen verstehen die App ohne Hilfe | Prototyp und vor dem Launch | fünf Testpersonen, Aufgaben laut denken lassen |

### Leistung und Last

| Test | Wofür | Wann | Werkzeuge |
|---|---|---|---|
| Ladezeit und Core Web Vitals | schnelle, stabile Seiten | vor jedem Release | Lighthouse, PageSpeed Insights, WebPageTest |
| App-Leistung | Startzeit, Abstürze, hängende App | laufend | Android Vitals, Xcode Organizer, Sentry |
| Lasttest | App hält viele gleichzeitige Nutzer aus | vor großem Launch | k6, Artillery |

### Datenschutz und Recht

| Test | Wofür | Wann | Werkzeuge |
|---|---|---|---|
| Einwilligungs-Test | vor dem „Ja“ keine Tracker, Pixel, fremden Schriften oder Einbettungen | vor jedem Release | Netzwerk-Tab im Browser, Charles Proxy, Exodus Privacy (Android) |
| Datenfluss-Abgleich | Datenschutzerklärung und Store-Angaben stimmen mit den echten Anfragen überein | vor jedem Release | Netzwerkmitschnitt, SDK-Liste |
| Rechtsseiten-Test | Impressum, Datenschutz, AGB, Kündigungs- und Widerrufsbutton erreichbar und funktionsfähig | vor jedem Release | von Hand, E2E-Test |
| Betroffenenrechte-Test | Auskunft, Export, Löschung funktionieren vollständig | vor dem Launch | Testkonto |

### Zahlungen und Stores

| Test | Wofür | Wann | Werkzeuge |
|---|---|---|---|
| Zahlungstest | Kauf, Abo, Kündigung, Widerruf, Erstattung, Fehlschlag, Webhook | vor jedem Release | Stripe-Testmodus und Testkarten, StoreKit-Sandbox, Google-Play-Lizenztester |
| Store-Vorabtest | Apple und Google prüfen die App vorab | vor dem Einreichen | TestFlight, geschlossener Test bei Google Play (bei neuen Privatkonten 12 Tester, 14 Tage), Pre-Launch-Bericht |
| Beta-Test | echte Nutzer finden, was du übersiehst | vor dem Launch | TestFlight, Play-Testtracks, Warteliste |

### Betrieb und Notfall

| Test | Wofür | Wann | Werkzeuge |
|---|---|---|---|
| Wiederherstellungstest | Backup lässt sich wirklich zurückspielen | vor dem Launch, dann jährlich | Restore in eine Testdatenbank |
| Rückroll-Test | eine fehlerhafte Version lässt sich schnell zurücknehmen | vor dem Launch | Hosting-Rollback, Feature-Flags |
| Überwachungstest | Fehler und Ausfälle lösen wirklich einen Alarm aus | vor dem Launch | absichtlicher Testfehler, Sentry, Uptime-Monitor |
| Notfallübung | Datenpanne, Schlüssel-Leck, Ausfall: jeder weiß, was zu tun ist | jährlich | [Runbooks](./wissen/allgemeine-app-entwicklung/15-runbooks/README.md) |

## So hilft dir die KI beim Testen

- Bitte die KI, zu jeder neuen Funktion **gleich den passenden Test** zu schreiben und ihn auszuführen.
- Bitte sie, die Testausgabe zu zeigen – nicht nur zu sagen „Tests laufen“.
- Lass sicherheitskritische Tests (Zwei-Konten-Test, Zahlungen, Löschen) zusätzlich **selbst von Hand** durchspielen.
- Vor jedem Release: den Prüfer [`ki-app-check`](./pruefer/README.md) laufen lassen.
