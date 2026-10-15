# 05 – Sicherheit – Grundlagen

KI-Coding-Agenten bauen schnell funktionierende Apps – aber oft ohne Sicherheitsgrenzen. Die meisten Datenlecks bei Vibe-Coding-Apps entstehen durch offene Datenbanken, Keys im Frontend und fehlende Berechtigungsprüfungen. Dieses Kapitel deckt die klassische App-Sicherheit ab. KI-spezifische Risiken stehen in [06](./06-ki-sicherheit-llm-risiken.md).

Vertiefung: [Threat Model und Security-Baseline](../allgemeine-app-entwicklung/05-sicherheit-datenschutz-recht/threat-model-und-security-baseline.md).

## A. Secrets und API-Keys

- [ ] `PFLICHT` **Keine geheimen Keys im Frontend oder App-Bundle.** Alles mit `NEXT_PUBLIC_`, `VITE_`, `EXPO_PUBLIC_` oder im Browser-Code ist öffentlich. Mobile Apps lassen sich entpacken. KI-, Stripe-Secret- und Datenbank-Admin-Keys gehören nur auf den Server.
- [ ] `PFLICHT` **`.env` in `.gitignore`.** Eine `.env.example` ohne echte Werte dokumentiert die nötigen Variablen.
- [ ] `PFLICHT` **Secret-Scanning aktivieren** (GitHub Push Protection, gitleaks oder ähnlich). Bei privaten Repos ohne bezahlte GitHub Secret Protection gitleaks als Pre-Commit-Hook oder in der CI laufen lassen.
- [ ] `PFLICHT` **Geleakte Keys sofort rotieren.** Löschen aus dem Code reicht nicht – die Git-Historie und Forks behalten sie.
- [ ] `PFLICHT` **Geheime Datenbankschlüssel nur auf dem Server.** Supabase `sb_secret_…` (früher `service_role`) und das Firebase Admin SDK umgehen alle Zugriffsregeln. Im Browser oder in der App nur den öffentlichen Schlüssel `sb_publishable_…` (früher `anon`) nutzen. Die alten Supabase-Schlüssel sind bis Ende 2026 abgekündigt (genaues Abschaltdatum noch offen) – jetzt umstellen und die alten danach im Dashboard deaktivieren.
- [ ] `PFLICHT` **Google- und Firebase-Schlüssel einschränken.** Öffentliche Google-API-Schlüssel (z. B. aus der Firebase-Konfiguration oder für Maps) nur für die nötigen Dienste und deine App oder Domain freigeben, nie für die Gemini-API. Für Gemini einen eigenen Schlüssel nutzen, der nur auf dem Server liegt; die Gemini-API lehnt uneingeschränkte Schlüssel ab, und neue Schlüssel aus AI Studio sind seit 28. Mai 2026 an ein Dienstkonto gebundene „Auth-Keys“. Alte uneingeschränkte Schlüssel austauschen.
- [ ] `SOLLTE` **Getrennte Keys für Entwicklung, Staging und Produktion.**
- [ ] `SOLLTE` **Minimale Rechte je Key** und Ablaufdatum, wo möglich.
- [ ] `SOLLTE` **Secrets im Secret-Manager des Hostings** speichern, nicht in Chat-Nachrichten, KI-Chats oder Agenten-Prompts, Tickets oder Notizen. KI-Chatverläufe auf Vibe-Coding-Plattformen wurden schon öffentlich sichtbar.
- [ ] `SOLLTE` **Secrets beim Hosting als „sensibel“ markieren.** Bei Vercel und ähnlichen Plattformen geheime Umgebungsvariablen als „Sensitive“ anlegen, dann sind sie nach dem Speichern nicht mehr im Klartext lesbar. Drittanbieter-Apps (besonders KI-Tools), die per OAuth auf Google-, GitHub- oder Hosting-Konten zugreifen, regelmäßig prüfen und entfernen.
- [ ] `SOLLTE` **Eigene API-Keys der Nutzer** („bring your own key“) verschlüsselt speichern, nie loggen und nie zurück an den Client senden.
- [ ] `SOLLTE` **Liste aller Keys** führen: wo verwendet, wer Zugriff hat, wie man ihn austauscht.

## B. Anmeldung (Authentifizierung)

- [ ] `PFLICHT` **Bewährten Auth-Anbieter nutzen** (z. B. Supabase Auth, Firebase Auth, Clerk oder Better Auth, der Nachfolger des für neue Projekte nicht mehr empfohlenen Auth.js). Keine eigene Passwort- oder Token-Logik bauen.
- [ ] `PFLICHT` **Passwort-Reset sicher:** einmalige Tokens mit Ablaufzeit, keine Auskunft, ob eine E-Mail existiert.
- [ ] `SOLLTE` **E-Mail-Adresse bestätigen lassen,** bevor wichtige Funktionen freigeschaltet werden.
- [ ] `SOLLTE` **Mehr-Faktor-Anmeldung oder Passkeys anbieten.** Für Admin-Konten immer aktivieren.
- [ ] `SOLLTE` **Sitzungen sicher:** Cookies mit `HttpOnly`, `Secure`, `SameSite`; Ablaufzeit; „Überall abmelden“.
- [ ] `SOLLTE` **Login-Versuche begrenzen** (Schutz vor Passwort-Raten).
- [ ] `SOLLTE` **Geleakte Passwörter ablehnen.** Neue Passwörter gegen Listen bekannter, schon geleakter Passwörter prüfen (NIST SP 800-63B), statt komplizierte Zeichenregeln zu erzwingen. Viele Auth-Anbieter haben dafür einen Schalter, z. B. Supabase „Leaked password protection“.
- [ ] `SOLLTE` **OAuth-Weiterleitungs-URLs fest eintragen** (keine Wildcards).
- [ ] `SOLLTE` **Kontoübernahme erschweren:** E-Mail-Änderung mit Bestätigung an die alte Adresse, Benachrichtigung bei neuem Gerät oder Passwortänderung.

## C. Berechtigungen (Autorisierung)

- [ ] `PFLICHT` **Bei jeder Anfrage auf dem Server prüfen: Wer ist das – und darf er genau das?** Angemeldet sein heißt nicht berechtigt sein.
- [ ] `PFLICHT` **Kein Zugriff über fremde IDs** (IDOR). Wenn `/api/rechnung/123` funktioniert, darf `/api/rechnung/124` für einen anderen Nutzer nicht funktionieren.
- [ ] `PFLICHT` **Test mit zwei Konten:** Mit Nutzer A anmelden und versuchen, Daten von Nutzer B zu lesen, zu ändern und zu löschen – über UI und direkt über API.
- [ ] `PFLICHT` **Rollen und Tarife nicht vom Client änderbar.** Häufiger Fehler: Nutzer darf die eigene Profilzeile bearbeiten und setzt damit `role = 'admin'` oder `plan = 'pro'`.
- [ ] `PFLICHT` **Keine Berechtigungen aus `user_metadata`.** Supabase-Nutzer können ihre eigenen `user_metadata` selbst ändern. Rollen, Tarife und Rechte gehören in `app_metadata` oder in eine eigene Tabelle, die nur der Server ändern darf.
- [ ] `PFLICHT` **Jede Server Action und API-Route prüft selbst.** In Next.js ist jede Server Action ein öffentlicher Endpunkt, den jeder direkt aufrufen kann. Anmeldung und Besitz des Datensatzes in jeder Action oder in einer zentralen Datenzugriffsschicht prüfen; Middleware bzw. `proxy.ts` ist nie die einzige Schutzschicht – sie wurde 2025 und 2026 mehrfach umgangen.
- [ ] `PFLICHT` **Supabase Edge Functions nicht durch Abschalten der Prüfung „reparieren“.** `verify_jwt = false` oder `auth: 'none'` macht eine Funktion für jeden aufrufbar; dann muss der Code den Aufrufer selbst prüfen (z. B. Webhook-Signatur). Wer in der Funktion den geheimen Schlüssel nutzt, umgeht RLS und muss jede Abfrage auf die Nutzer-ID des Aufrufers beschränken. Supabase warnt ausdrücklich davor, die Prüfung abzuschalten, um einen 401-Fehler loszuwerden.
- [ ] `PFLICHT` **Admin-Bereiche serverseitig schützen.** Eine versteckte URL ist kein Schutz.
- [ ] `SOLLTE` **Teams und Organisationen sauber trennen:** Rollen innerhalb einer Organisation, Einladungen per einmaligem Token, entfernte Mitglieder verlieren sofort den Zugriff.
- [ ] `SOLLTE` **Berechtigungsmatrix** schreiben: Rolle × Aktion × Daten. Vorlage: [Berechtigungsmatrix](../allgemeine-app-entwicklung/vorlagen/berechtigungsmatrix.md).
- [ ] `SOLLTE` **Liste aller öffentlich erreichbaren Endpunkte** führen: API-Routen, Server Actions, Edge Functions, Webhooks, Vorschau- und alte Versionen. Was nicht gebraucht wird, abschalten (OWASP API Security Top 10, API9).
- [ ] `SOLLTE` **Geteilte Links schützen.** Teilen-Links für Chats, Dokumente oder Ergebnisse standardmäßig privat, mit zufälliger ID, widerrufbar und mit Ablaufdatum. `noindex` ersetzt keinen Zugriffsschutz – 2025 landeten geteilte KI-Chats in Suchmaschinen. Vor dem Teilen zeigen, was sichtbar wird.

## D. Datenbank

- [ ] `PFLICHT` **Supabase: Row Level Security auf jeder Tabelle aktivieren** und passende Policies schreiben. Ohne RLS kann jeder mit dem öffentlichen Schlüssel alle Daten lesen, ändern und löschen. Auch Storage-Buckets absichern.
- [ ] `PFLICHT` **Tabellenfreigabe, RLS und Policy immer zusammen.** Bei Supabase sind neue Tabellen ab 30. Oktober 2026 auch in bestehenden Projekten erst nach einer ausdrücklichen Freigabe (`GRANT`) über die API erreichbar. Freigabe, RLS und Policy gehören in dieselbe Migration; die Rolle `anon` (nicht angemeldete Besucher) bekommt nie Schreibrechte, und der Agent darf bei „permission denied“ nicht einfach alles freigeben.
- [ ] `PFLICHT` **Firebase: Security Rules prüfen Besitz, nicht nur Anmeldung.** Regeln wie `if true` oder nur `if request.auth != null` geben jedem bzw. jedem angemeldeten Nutzer alle Daten – 2026 wurden so 300 Millionen Chatnachrichten einer KI-Chat-App öffentlich. Jede Regel prüft, dass die Nutzer-ID zum Datensatz passt (z. B. `request.auth.uid == resource.data.owner`), auch in Cloud Storage.
- [ ] `PFLICHT` **Policies mit zwei Nutzern testen.** Vorlage: [Supabase-RLS-Testmatrix](../allgemeine-app-entwicklung/03-technik/supabase-rls-testmatrix.md).
- [ ] `PFLICHT` **Parametrisierte Abfragen oder ORM** verwenden. Nie Nutzereingaben in SQL-Strings zusammenbauen.
- [ ] `PFLICHT` **Datenbank nicht direkt aus dem Internet erreichbar** (außer über die vorgesehene API), starke Passwörter.
- [ ] `SOLLTE` **Supabase Security Advisor** regelmäßig prüfen und Warnungen beheben.
- [ ] `PFLICHT` **Views und Funktionen mit erhöhten Rechten prüfen.** Datenbank-Sichten (Views) und `security definer`-Funktionen umgehen RLS, wenn sie mit den Rechten ihres Erstellers laufen. Views mit `security_invoker = true` anlegen und jede über die API erreichbare Funktion mit zwei Nutzern testen; der Supabase Security Advisor meldet solche Fälle.
- [ ] `SOLLTE` **Sensible Felder zusätzlich verschlüsseln** (z. B. Tokens von Drittanbietern).
- [ ] `SOLLTE` **Verschlüsselung ruhender Daten** beim Hosting-Anbieter prüfen (Datenbank, Backups, Dateispeicher).
- [ ] `PFLICHT` **Alte Speicherorte und Verifizierungsdaten löschen.** Nach einem Umzug alte Buckets, Datenbanken und Backups löschen oder absichern; Ausweis- und Selfie-Bilder aus Identitätsprüfungen nach der Prüfung löschen. Eine Dating-Sicherheits-App verlor 2025 so rund 13.000 Ausweisfotos aus einem vergessenen Altspeicher.
- [ ] `SOLLTE` **Eigene API-Schlüssel der App nur als Hash speichern.** Schlüssel, die deine App an Nutzer oder deren Agenten ausgibt, nur einmal anzeigen und in der Datenbank nur einen Prüfwert (Hash) speichern – dann sind sie nach einem Datenleck wertlos.
- [ ] `KANN` **Ungenutzte Schnittstellen abschalten.** Greift die App nur über eigene Server-Routen auf die Datenbank zu, die automatische Supabase-Data-API bzw. GraphQL abschalten. Was nicht erreichbar ist, kann nicht falsch eingestellt sein.

## E. Eingaben und Ausgaben

- [ ] `PFLICHT` **Alle Eingaben serverseitig validieren** (Typ, Länge, Format, erlaubte Werte), z. B. mit zod. Prüfungen im Browser sind nur Komfort.
- [ ] `PFLICHT` **Im Fehlerfall sicher schließen.** Schlägt eine Prüfung von Anmeldung, Berechtigung, Abo-Status, Moderation oder Limit fehl oder stürzt ab, wird der Zugriff verweigert („fail closed“). Ein `catch`-Block darf nie „erlaubt“ oder „erfolgreich“ zurückgeben, nur damit die App weiterläuft.
- [ ] `PFLICHT` **Kein ungeprüftes HTML ausgeben.** `dangerouslySetInnerHTML`, `v-html` und `innerHTML` nur mit Bereinigung (z. B. DOMPurify). Gilt besonders für Markdown aus der KI.
- [ ] `PFLICHT` **Datei-Uploads absichern:** Dateityp serverseitig prüfen, Größe und Anzahl begrenzen, Dateinamen neu vergeben, private Buckets, signierte URLs mit Ablauf. SVG und HTML als Upload nur mit Bereinigung.
- [ ] `PFLICHT` **Server-seitige URL-Abrufe absichern (SSRF).** Wenn die App Links abruft („Fasse diese Website zusammen“), interne Adressen, `localhost` und Cloud-Metadaten-Endpunkte blockieren.
- [ ] `SOLLTE` **CSRF-Schutz** bei Cookie-basierten Sitzungen.
- [ ] `SOLLTE` **Fehlermeldungen ohne Interna.** Keine Stacktraces, SQL-Fehler oder Pfade an Nutzer.
- [ ] `KANN` **Virenscan für Uploads,** wenn Dateien mit anderen geteilt werden.

## F. Transport und Browser-Schutz

- [ ] `PFLICHT` **HTTPS überall,** mit HSTS.
- [ ] `PFLICHT` **CORS eng einstellen.** Nur eigene Domains, nie `*` zusammen mit Zugangsdaten.
- [ ] `SOLLTE` **Security-Header setzen:** Content-Security-Policy, `X-Content-Type-Options`, `frame-ancestors`, `Referrer-Policy`.

## G. Missbrauch und Limits

- [ ] `PFLICHT` **Rate-Limits pro Nutzer und IP** auf teuren oder sensiblen Endpunkten: KI-Anfragen, Login, Registrierung, Passwort-Reset, Uploads, E-Mail-Versand.
- [ ] `SOLLTE` **Bot-Schutz bei Registrierung** (z. B. Cloudflare Turnstile), datenschutzfreundlich eingebunden.
- [ ] `SOLLTE` **Missbrauch von Gratis-Kontingenten erkennen** (Wegwerf-E-Mails, viele Konten pro Gerät).

## H. Abhängigkeiten und Lieferkette

- [ ] `PFLICHT` **Prüfen, ob ein Paket wirklich existiert und seriös ist.** KI-Agenten erfinden manchmal Paketnamen; Angreifer registrieren genau diese Namen („Slopsquatting“). Downloads, Alter, Maintainer und Repository ansehen.
- [ ] `PFLICHT` **Lockfile committen** (`package-lock.json`, `pnpm-lock.yaml`, `poetry.lock`).
- [ ] `SOLLTE` **Automatische Updates und Warnungen** (Dependabot oder Renovate, `npm audit`).
- [ ] `PFLICHT` **Installationsskripte von Paketen nur nach Freigabe.** Schadpakete laufen oft über `preinstall`- oder `postinstall`-Skripte oder eine versteckte `binding.gyp` schon beim Installieren. npm 12 sperrt das standardmäßig, Node.js bringt aber noch npm 11 mit: mit `npm install -g npm@12` aktualisieren, erlaubte Pakete mit `npm approve-scripts` festlegen und die Liste committen. Wer bei npm 11 bleibt, setzt `ignore-scripts=true` in `.npmrc`.
- [ ] `SOLLTE` **Neue Paketversionen erst nach einigen Tagen.** Eine Wartezeit einstellen, z. B. `min-release-age=7` in `.npmrc` (npm ab 11.10) oder `minimumReleaseAge` bei pnpm. Für Python: `exclude-newer` in uv oder `pip install --uploaded-prior-to P7D`. Die meisten Schadversionen werden innerhalb von Stunden entdeckt und entfernt. Die Wartezeit schützt auch vor Schadcode, der erst beim Laden oder Importieren läuft – den fängt die Sperre für Installationsskripte nicht ab (Wurm „ChainDrop“, August 2026). Sicherheitsupdates dürfen trotzdem sofort kommen.
- [ ] `SOLLTE` **Keine Pakete direkt aus Git-Repos oder Download-Links.** Nur Pakete aus der Registry nutzen. Eine `.npmrc` in einem Git-Paket kann sogar mit `--ignore-scripts` Code ausführen. Ab npm 12 werden solche Abhängigkeiten nur nach Freigabe aufgelöst; bei npm 11 `allow-git=none` und `allow-remote=none` in `.npmrc` setzen.
- [ ] `SOLLTE` **Im Build `npm ci` statt `npm install`.** `npm ci` installiert genau die Versionen aus dem Lockfile und bricht ab, wenn Lockfile und `package.json` nicht zusammenpassen.
- [ ] `SOLLTE` **So wenige Abhängigkeiten wie möglich.** Für drei Zeilen Code kein neues Paket.
- [ ] `PFLICHT` **GitHub Actions auf Commit-SHA festlegen.** Fremde Actions mit dem vollständigen Commit-Hash statt mit `@v4` einbinden, weil Versions-Tags nachträglich auf Schadcode umgebogen werden können (2025 bei tj-actions, 2026 beim Scanner Trivy). Rechte des Workflow-Tokens minimieren und Secrets nur den Jobs geben, die sie brauchen.
- [ ] `KANN` **Eigene npm-Pakete nur per Trusted Publishing oder Staged Publishing veröffentlichen.** Keine langlebigen Publish-Tokens; jede Version gibt ein Mensch mit Zwei-Faktor-Anmeldung frei.

## I. Zahlungen und Webhooks

- [ ] `PFLICHT` **Webhook-Signaturen prüfen** (z. B. Stripe-Signatur). Sonst kann jeder „Zahlung erfolgreich“ melden.
- [ ] `PFLICHT` **Preise, Rabatte und Berechtigungen nie vom Client übernehmen.** Der Server bestimmt den Preis und prüft den Abo-Status.
- [ ] `PFLICHT` **Keine Kartendaten selbst speichern.** Stripe Checkout, Elements oder die Store-Kaufsysteme verwenden.
- [ ] `SOLLTE` **Webhooks idempotent verarbeiten.** Dieselbe Nachricht kann mehrfach ankommen.

## J. Protokolle

- [ ] `PFLICHT` **Keine Passwörter, Tokens, Keys oder vollständigen sensiblen Inhalte in Logs.**
- [ ] `SOLLTE` **Audit-Log** für Admin-Aktionen, Rollenänderungen, Logins und Löschungen.

## K. Mobile Apps

- [ ] `PFLICHT` **Tokens und Geheimnisse im sicheren Speicher des Geräts** (iOS Keychain, Android Keystore, z. B. über `expo-secure-store`), nicht unverschlüsselt in AsyncStorage, SharedPreferences oder Dateien.
- [ ] `PFLICHT` **Keine Debug-Funktionen, Test-Endpunkte oder ausführlichen Logs** im Produktions-Build.
- [ ] `SOLLTE` **App-Echtheit prüfen** (Firebase App Check, Apple App Attest, Google Play Integrity), damit nicht jeder deine KI-Endpunkte außerhalb der App missbrauchen kann.
- [ ] `SOLLTE` **Universal Links bzw. App Links** statt nur eigener URL-Schemata, besonders für Login-Rückleitungen – eigene Schemata können von anderen Apps abgefangen werden.
- [ ] `SOLLTE` **Android: keine unnötig exportierten Komponenten** (Activities, Services, Receiver) und keine Klartext-Verbindungen.
- [ ] `SOLLTE` **Sensible Inhalte im App-Umschalter ausblenden** (Vorschaubild beim Wechseln zwischen Apps).
- [ ] `KANN` **Code-Verschleierung, Certificate Pinning und Root-/Jailbreak-Erkennung** bei besonders sensiblen Apps (Finanzen, Gesundheit).
- [ ] `KANN` **Over-the-Air-Updates signieren.** Bei Expo EAS Update die Code-Signierung aktivieren, damit die App nur von dir signierte Updates lädt.

## L. Prüfen lassen

- [ ] `SOLLTE` **Automatische Scans:** Semgrep oder CodeQL, ZAP-Baseline-Scan (Zed Attack Proxy, früher „OWASP ZAP“), Supabase Security Advisor, Secret-Scan, `npm audit` oder OSV-Scanner.
- [ ] `SOLLTE` **Separaten Security-Review durch die KI** in einer frischen Sitzung (siehe [Prüf-Prompts](./PRUEF-PROMPTS.md)). Die KI, die den Code geschrieben hat, prüft sich selbst schlecht.
- [ ] `KANN` **Professioneller Penetrationstest** vor großem Launch oder bei sensiblen Daten.
- [ ] `KANN` **Strukturierte Prüflisten:** OWASP ASVS 5.0 Stufe 1 als Mindestprüfung für Web-Backends, für Mobile Apps OWASP MASVS 2.1 mit dem Testleitfaden MASTG.

## Typische Fehler beim Vibe-Coding

- Agent deaktiviert RLS, „damit der Fehler weggeht“.
- OpenAI- oder Anthropic-Key als `NEXT_PUBLIC_…` im Browser.
- API-Route prüft nur „ist eingeloggt“, nicht „gehört der Datensatz diesem Nutzer“.
- Profil-Update-Endpunkt übernimmt das ganze Objekt vom Client, inklusive `role`.
- Stripe-Erfolgsseite schaltet Premium frei statt der Webhook.

## Nachweis

Secret-Scan ohne Funde, RLS-/Rules-Testprotokoll mit zwei Nutzern, IDOR-Test, Rate-Limit-Test, Scan-Reports, Liste der Abhängigkeiten mit Prüfung.
