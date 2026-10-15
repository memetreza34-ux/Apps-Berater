# Web- und PWA-Playbook

## Geeignet für

- SaaS und Dashboards;
- Inhalts-, Lern- und Verwaltungsapps;
- schnellen Markttest;
- Desktop- und Tablet-Arbeitsabläufe;
- Produkte ohne zwingende tiefe Geräteintegration.

## Produktionsbaseline

### Browser und Rendering
- unterstützte Browser und Mindestversionen festlegen;
- server- und clientseitige Zuständigkeiten dokumentieren;
- Formulare auch ohne perfekte Netzwerkverbindung robust machen;
- Hydration-, Routing- und Cachefehler testen;
- responsive Layouts mit realen Inhalten prüfen.

### Web-Security
- HTTPS erzwingen;
- Content Security Policy projektspezifisch definieren;
- sichere Cookieattribute verwenden;
- CSRF-Schutz entsprechend Architektur;
- XSS durch Output-Encoding und sichere Rendering-APIs verhindern;
- CORS eng konfigurieren;
- keine Secrets in Browser-Bundles;
- Security Header automatisch testen.

### Auth
- Sessionablauf und parallele Tabs;
- Login-Link/Reset-Link nur für erlaubte Domains;
- OAuth-State/PKCE entsprechend Anbieter;
- Abmeldung und Widerruf;
- sichere Weiterleitungen;
- Adminzugänge mit MFA.

### PWA
- Manifest, Icons und Start-URL;
- Service Worker mit klarer Cache-Strategie;
- alte Assets nach Deployment entfernen;
- keine sensiblen API-Antworten unkontrolliert cachen;
- Offline-Screen und Updatehinweis;
- Verhalten bei inkompatibler alter App-Version;
- Installation ist Zusatznutzen, keine Pflicht für den Kernablauf.

## Performance

Messe mindestens:
- Zeit bis nutzbarer Kernscreen;
- Core-Web-/Interaktionsmetriken passend zum Produkt;
- JavaScript-, CSS-, Font- und Bildbudget;
- API-p95;
- langsames Mobilnetz;
- große Listen und Datei-Uploads.

## Deployment

```text
Pull Request
→ automatische Prüfung
→ Preview
→ Staging
→ Migration
→ Smoke-/E2E-Test
→ Production
→ synthetische Prüfung
→ gestaffelte Feature-Freigabe
```

## Release-Gate

- [ ] HTTPS und Header geprüft
- [ ] Auth und Redirects negativ getestet
- [ ] CSP ohne unnötig breite Ausnahmen
- [ ] Cookie-/Consent-Verhalten entspricht echter Technik
- [ ] Responsive und Tastaturbedienung
- [ ] PWA-Update und Offlinezustand
- [ ] Preview, Staging und Rollback
- [ ] Monitoring für Client, API und Kernablauf
