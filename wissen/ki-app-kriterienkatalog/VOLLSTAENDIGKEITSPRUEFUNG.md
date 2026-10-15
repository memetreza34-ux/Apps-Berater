# Vollständigkeitsprüfung des KI-App-Kriterienkatalogs

**Prüfdatum:** 29. September 2026; zweite Prüfung am 30. September 2026; dritte Prüfung mit fünf parallelen Recherchen am 2. Oktober 2026; vierte Prüfung mit eigenem Lückenabgleich und fünf Recherchen am 13. Oktober 2026
**Ergebnis:** Nach den Ergänzungen dieser Prüfung sind alle Bereiche der unten genannten Referenzrahmen im Katalog abgedeckt. Offen bleiben nur Punkte, die eine Einzelfallbewertung brauchen (siehe „Bewusste Grenzen“), und Rechtsentwicklungen, die beobachtet werden müssen.

## Prüfmethode

1. **Abgleich mit Referenzrahmen:** Vollständigkeitsstandard dieses Repositories, AI Act, DSGVO, DSK-Orientierungshilfe „KI und Datenschutz“, OWASP Top 10 für LLM-Anwendungen (2026), OWASP Top 10 für agentische Anwendungen (2026), OWASP Top 10 (Web), NIST AI RMF, WCAG 2.2, aktuelle Store-Regeln von Apple und Google, aktuelle Vibe-Coding-Sicherheitschecklisten.
2. **Faktenprüfung** aller zeitabhängigen Aussagen (Fristen, Schwellenwerte, Store-Regeln) anhand von Primärquellen und aktuellen Fachquellen. Ergebnis in [Quellen und Stand](./QUELLEN-UND-STAND.md).
3. **Technische Prüfung:** relative Links, doppelte Überschriften, Zeilenenden und Struktur mit `scripts/validate_handbook.py`.
4. **Lückenliste:** Jede gefundene Lücke wurde direkt im passenden Kapitel ergänzt.

## 1. Abgleich mit dem Vollständigkeitsstandard des Repositories

Grundlage: [Vollständigkeitsstandard der Master-Anleitung](../app-master-anleitung/VOLLSTAENDIGKEITSSTANDARD.md).

| Bereich des Standards | Im Katalog abgedeckt in | Status |
|---|---|---|
| 1. Orientierung und Voraussetzungen | 13 E (Konten, Signierung), 14 A und I (Gründung, Anbieterkonten), 16 A (Plan, Stack, Regeldatei) | abgedeckt; Werkzeug-Einstieg ausführlich in der Master-Anleitung |
| 2. Idee, Nutzer, Markt und Geschäft | 17 A, B und G, 14 E | abgedeckt |
| 3. Recht, Rechte, Regeln und Normen | 01, 02, 03, 04, 15 | abgedeckt |
| 4. Produktaufbau und Funktionsstruktur | 09, 17 B | abgedeckt |
| 5. UX, UI, Inhalte und Marke | 10, 11, 04 G | abgedeckt |
| 6. Systemaufbau und Architektur | 08, 05, 07 | abgedeckt |
| 7. Daten von Entstehung bis Löschung | 02, 05 D, 06 E, 08 D und H, 12 D | abgedeckt |
| 8. Entwicklung mit KI | 16, [Prüf-Prompts](./PRUEF-PROMPTS.md) | abgedeckt |
| 9. Qualität, Tests und Normen | 12 A, 05 L, 06, 07 E, 11 C | abgedeckt |
| 10. Veröffentlichung | 13, 12 B | abgedeckt |
| 11. Marketing und Nutzergewinnung | 17 C bis G | abgedeckt (neu in dieser Prüfung) |
| 12. Betrieb über Jahre | 12, 14 H und I | abgedeckt |
| 13. Langfristige Nutzbarkeit | 07 A (Abstraktionsschicht), 14 I (Anbieterwechsel), 12 G (Produktende) | abgedeckt |

## 2. Abgleich mit dem AI Act

| Regelung | Kapitel |
|---|---|
| Anwendungsbereich und Ausnahmen (Art. 2), Definition KI-System (Art. 3) | 01 A |
| KI-Kompetenz (Art. 4) | 01 C |
| Verbotene Praktiken (Art. 5, inkl. neues Verbot durch den Digital Omnibus) | 01 B, 06 G, 15 L |
| Hochrisiko-Einstufung (Art. 6, Anhang I und III) | 01 E, 15 |
| Anforderungen an Hochrisiko-Systeme (Art. 8–15) und Anbieterpflichten (Art. 16–17, 43, 47–49) | 01 E |
| Verantwortung entlang der Wertschöpfungskette (Art. 25) | 01 E |
| Betreiberpflichten und Grundrechte-Folgenabschätzung (Art. 26–27) | 01 E |
| Transparenzpflichten (Art. 50) | 01 D, 09 C, 10 A, 13 D, 17 E |
| GPAI-Modelle (Art. 53–55) | 01 F |
| Reallabore (Art. 57) | 01 E |
| Beobachtung nach dem Inverkehrbringen, schwere Vorfälle (Art. 72–73) | 01 E |
| Recht auf Erklärung (Art. 86) | 01 E |
| Sanktionen (Art. 99) | 01 G |

## 3. Abgleich mit der DSGVO

| Regelung | Kapitel |
|---|---|
| Grundsätze, Rechtsgrundlagen, Einwilligung und Nachweis (Art. 5–7) | 02 A |
| Kinder (Art. 8) | 02 F, 15 C |
| Besondere Kategorien (Art. 9) | 02 A, 15 B und D |
| Informationspflichten (Art. 12–14) | 02 A und B |
| Betroffenenrechte (Art. 15–21) | 02 C |
| Automatisierte Einzelentscheidungen (Art. 22) | 02 A |
| Datenschutz durch Technikgestaltung (Art. 25) | 02 A |
| Gemeinsame Verantwortlichkeit, Auftragsverarbeitung (Art. 26, 28) | 02 A, 15 M |
| Verzeichnis, Sicherheit, Datenpannen (Art. 30, 32–34) | 02 A und E, 12 E |
| Datenschutz-Folgenabschätzung, Datenschutzbeauftragter (Art. 35, 37) | 02 A |
| Drittlandübermittlung (Art. 44 ff.) | 02 A |
| Endgerätezugriff und Cookies (TDDDG) | 02 D |
| DSK-Orientierungshilfe „KI und Datenschutz“ (Zweck, Transparenz, Training, Betroffenenrechte, Richtigkeit, Diskriminierung) | 02 A bis C, 07 E |

## 4. Abgleich mit den OWASP Top 10 für LLM-Anwendungen (2026)

Die Ausgabe 2026 (veröffentlicht am 3. August 2026) enthält dieselben zehn Risiken wie 2025 in neuer Reihenfolge. „System Prompt Leakage“ heißt jetzt „Hidden Context Exposure“ und umfasst allen verborgenen Kontext.

| Risiko | Kapitel |
|---|---|
| LLM01 Prompt Injection (auch in Bildern und Audio) | 06 A, 16 D |
| LLM02 Offenlegung sensibler Informationen | 06 B, 02 B |
| LLM03 Zu viel Handlungsspielraum | 06 D und L, 15 K |
| LLM04 Lieferkette (inkl. erfundener Paketnamen) | 06 F, 06 D (MCP, Plugins), 05 H, 16 D |
| LLM05 Daten- und Modellvergiftung (inkl. Fine-Tuning) | 06 E und F, 02 B |
| LLM06 Unbegrenzter Verbrauch (inkl. Denk-Tokens, Denial of Wallet) | 06 I, 07 D, 05 G |
| LLM07 Fehlinformation | 06 H, 10 D |
| LLM08 Offenlegung verborgenen Kontexts | 06 B |
| LLM09 Schwächen bei Vektoren und Embeddings | 06 E, 02 B |
| LLM10 Unsichere Verarbeitung der Ausgabe | 06 C, 06 B, 05 E |

## 4a. Abgleich mit den OWASP Top 10 für agentische Anwendungen (2026)

| Risiko | Kapitel |
|---|---|
| ASI01 Zielentführung | 06 A und L |
| ASI02 Missbrauch von Werkzeugen | 06 D |
| ASI03 Missbrauch von Identität und Rechten | 06 D und L |
| ASI04 Lieferkette von Agenten | 06 D und F, 05 H, 16 D |
| ASI05 Unerwartete Code-Ausführung | 06 C, 16 D |
| ASI06 Vergiftung von Gedächtnis und Kontext | 06 E und L |
| ASI07 Unsichere Kommunikation zwischen Agenten | 06 L |
| ASI08 Kettenreaktionen | 06 L |
| ASI09 Ausnutzen von Vertrauen | 06 L, 10 D |
| ASI10 Abweichende Agenten | 06 J und L |

## 4b. Abgleich mit dem NIST AI Risk Management Framework

| Merkmal vertrauenswürdiger KI | Kapitel |
|---|---|
| gültig und zuverlässig | 07 C und E |
| sicher (keine Schäden) | 06 G und H, 15 |
| geschützt und widerstandsfähig | 05, 06 |
| verantwortlich und transparent | 01 A und D, 09 B |
| erklärbar und nachvollziehbar | 10 D, 07 F (Quellen) |
| datenschutzfreundlich | 02 |
| fair, schädliche Verzerrungen kontrolliert | 07 E, 15 H |
| Steuerung (Govern): Rollen, Richtlinie, Risikoregister | 01 A und C, 14 H |
| Abbilden, Messen, Steuern (Map, Measure, Manage) | 01 A (Einordnung), 07 E (Evals), 06 J und 12 C (Betrieb) |

NIST überarbeitet das AI RMF 1.0; das GenAI-Profil (NIST AI 600-1) und SP 800-218A sind über 06 und 16 abgedeckt. Neue Fassungen werden bei der nächsten Prüfung abgeglichen.

## 5. Abgleich mit den OWASP Top 10 (Web, Ausgabe 2025)

| Risiko | Kapitel |
|---|---|
| A01 Fehlerhafte Zugriffskontrolle | 05 C (inkl. Server Actions, `user_metadata`), 05 D (RLS, GRANT, Firebase-Besitz, Views), 06 E |
| A02 Sicherheitsrelevante Fehlkonfiguration | 05 A (Google-Schlüssel, sensible Variablen), 05 D, 05 F, 05 K, 08 C (Vorschau-Schutz) |
| A03 Fehler in der Software-Lieferkette | 05 H (Installationsskripte, Wartezeit, `npm ci`, SHA-Pinning), 06 D und F, 16 D, 03 F (SBOM), 12 E |
| A04 Kryptografische Fehler | 05 A, 05 D (Verschlüsselung, gehashte Tokens), 05 F, 05 K |
| A05 Injection | 05 D und E, 06 A und C |
| A06 Unsicheres Design | 08 A, 05 C (Berechtigungsmatrix), 06 D (tödliches Dreigespann), [Threat Model](../allgemeine-app-entwicklung/05-sicherheit-datenschutz-recht/threat-model-und-security-baseline.md) |
| A07 Fehler bei der Anmeldung | 05 B, 09 A, 14 I (phishing-resistente Anmeldung der eigenen Konten) |
| A08 Fehler bei Software- und Datenintegrität | 05 I (Webhook-Signatur), 05 H, 05 K (signierte Updates), 06 F |
| A09 Fehler bei Protokollierung und Alarmierung | 05 J, 12 C, 06 D |
| A10 Falscher Umgang mit Ausnahmezuständen | 05 E (im Fehlerfall sicher schließen), 07 C, 08 E |

Server-Side Request Forgery gehört in der Ausgabe 2025 zu A01 und ist in 05 E abgedeckt.

## 5a. Abgleich mit den OWASP API Security Top 10 (2023)

| Risiko | Kapitel |
|---|---|
| API1 Zugriff auf fremde Objekte | 05 C und D |
| API2 Fehlerhafte Anmeldung | 05 B |
| API3 Zugriff auf einzelne Felder | 05 C, 08 F |
| API4 Unbegrenzter Ressourcenverbrauch | 05 G, 06 I, 07 D |
| API5 Fehlerhafte Funktionsrechte | 05 C, 09 H |
| API6 Missbrauch sensibler Abläufe | 05 G (Gratis-Kontingente, Bot-Schutz), 10 F |
| API7 Server-Side Request Forgery | 05 E |
| API8 Fehlkonfiguration | 05 A und F |
| API9 Fehlende Übersicht über Endpunkte | 05 C (Endpunkt-Liste, neu) |
| API10 Unsichere Nutzung fremder APIs | 08 F (Antworten fremder Dienste prüfen, neu) |

## 5b. Abgleich mit den OWASP MCP Top 10 (Beta)

| Risiko | Kapitel |
|---|---|
| MCP01 Token und Geheimnisse | 16 D, 05 A |
| MCP02 Zu weite Rechte | 06 D |
| MCP03 und MCP04 Vergiftete Werkzeuge und Lieferkette | 06 D, 16 D |
| MCP05 Befehlsausführung | 06 C und D |
| MCP06 Prompt Injection über Kontext | 06 A, 16 D |
| MCP07 Anmeldung und Autorisierung | 06 D (eigener MCP-Server) |
| MCP08 Fehlende Protokollierung | 06 D |
| MCP09 Schatten-MCP-Server | 16 D (MCP-Liste, neu) |
| MCP10 Kontext-Überfüllung und Datenabfluss | 06 B |

## 5c. Behördenleitfäden zu KI und Agenten

| Leitfaden | Kapitel |
|---|---|
| BSI und ANSSI: KI-Codeassistenten (2024) | 16 |
| BSI und ANSSI: Zero-Trust-Prinzipien für LLM-Systeme | 06 A bis D |
| CISA, NSA und Partner: Careful Adoption of Agentic AI Services (Mai 2026) | 06 L |
| MCP-Spezifikation 2026-07-28, Security Best Practices | 06 D |

## 6. Abgleich mit WCAG 2.2 und Store-Regeln

| Bereich | Kapitel |
|---|---|
| WCAG 2.2, alle Erfolgskriterien der Stufen A und AA | 11 B, C und D, 10 H (Details in Abschnitt 6a) |
| BFSG, EN 301 549 V4.1.1, Barrierefreiheitsinformationen nach § 14 und Anlage 3 | 03 E, 11 C und E |
| Apple: Kontolöschung, Datenschutzangaben, Privacy Manifest, Drittanbieter-KI, ATT (inkl. EU-Abfrage ab iOS 27.2), In-App-Kauf und EU-Bedingungen (inkl. Elternschranke), Credits, Web-Abos, Login, Nutzerinhalte (1.2), keine Belohnung gegen Systemfreigaben, Chatbot-Kataloge, anonyme Chats, Altersfreigabe (inkl. Social Media), Medizinprodukt-Status, Duplikate (4.3), Vorlagen (4.2.6), nachgeladener Code (2.5.2), regulierte Bereiche, Bewertungen, Händlerstatus, Exportkontrolle, Foundation Models | 13 A, 13 F, 07 A |
| Google Play: Kontolöschung, Data Safety, KI-Inhalte, KI-Integrationen, Ziel-API 36, Entwicklerverifizierung, Testphase, Billing und Abo-Regeln, Pflichterklärungen, Age Signals, anonyme Chats, Dating-Apps, Händlerstatus, sensible Berechtigungen (inkl. Änderungen 2027), Werbe-ID, Bewertungen | 13 B, 15 T |
| Desktop und Browser: macOS-Notarisierung und Developer ID, Windows-Signatur, Electron, Chrome Web Store, Microsoft Store | 13 G |
| Messenger und Social Bots: WhatsApp Business, Telegram, Discord, § 18 Abs. 3 MStV | 13 D |
| Signierung, Versionen, Organisationskonten, Kontosperren, Xcode-Pflicht, Vertriebsländer | 13 E |

## 6a. WCAG 2.2 im Detail (Stufen A und AA)

| Prinzip | Erfolgskriterien | Kapitel |
|---|---|---|
| Wahrnehmbar | 1.1.1, 1.2.1–1.2.5, 1.3.1–1.3.5, 1.4.1–1.4.5, 1.4.10–1.4.13 | 11 B (kleine Bildschirme), 11 C (Alternativtexte, Untertitel, Farbe, Kontrast, Textgröße), 11 D (Struktur, Ausrichtung, Eingabezweck, Ton stoppbar, Text nicht als Bild, Textabstände, Einblendungen) |
| Bedienbar | 2.1.1, 2.1.2, 2.1.4, 2.2.1, 2.2.2, 2.3.1, 2.4.1–2.4.7, 2.4.11, 2.5.1–2.5.4, 2.5.7, 2.5.8 | 11 C (Tastatur, Fokus, Zeitlimits, Blinken), 11 D (Tastenkürzel, Bewegtes, Überspringen, Titel, Linktexte, mehrere Wege, Fokus nicht verdeckt, Gesten, Name im Label, Ziehen, Klickflächen) |
| Verständlich | 3.1.1, 3.1.2, 3.2.1–3.2.4, 3.2.6, 3.3.1–3.3.4, 3.3.7, 3.3.8 | 11 C (Sprache, Beschriftungen, Fehlermeldungen), 11 D (keine Überraschungen, einheitliche Navigation, Hilfe, Fehlerhilfen, Fehlervermeidung, keine doppelte Eingabe, barrierefreie Anmeldung), 10 H (Sprache von KI-Antworten) |
| Robust | 4.1.2, 4.1.3 (4.1.1 entfällt in WCAG 2.2) | 11 D (Name, Rolle, Zustand; Statusmeldungen), 10 H |

## 7. In dieser Prüfung gefundene Lücken und Korrekturen

**Neues Kapitel:** [17 – Produkt, Launch und Wachstum](./17-produkt-launch-wachstum.md) (Idee prüfen, MVP, Launch, Auffindbarkeit, Werberecht, Nutzerbindung, Kennzahlen).

**Korrigiert oder präzisiert:**

- Apple 5.1.2(i): Anbieter der KI namentlich nennen, aktive Zustimmung nötig, Weiternutzen zählt nicht (13 A).
- Impressum: Wirtschafts-Identifikationsnummer ergänzt (03 A).

**Ergänzt (Auswahl nach Kapitel):**

| Kapitel | Ergänzungen |
|---|---|
| 01 | Ausnahmen vom Anwendungsbereich, ungewollter Wechsel in die Anbieterrolle (Art. 25), Grundrechte-Folgenabschätzung, Recht auf Erklärung, Reallabore |
| 02 | Datenschutz durch Technikgestaltung, Nachweis von Einwilligungen, Daten Dritter in Uploads, gemeinsame Verantwortlichkeit, Session-Replay, Fine-Tuning und Löschbarkeit, Embeddings |
| 03 | AGB-Zustimmung protokollieren, Mindestalter, Geoblocking-Verordnung, P2B-Verordnung, Gewinnspiele |
| 04 | Datenbankherstellerrecht, Herkunft von Datensätzen, Designschutz, eigene Geschäftsgeheimnisse |
| 05 | eigene Keys der Nutzer, Key-Liste, Kontoübernahme, Teams und Organisationen, Verschlüsselung ruhender Daten, neuer Abschnitt Mobile Apps |
| 06 | mehrstufige Agenten, Browser- und Computer-Steuerung, neuer Abschnitt Lieferkette für Modelle und Trainingsdaten |
| 07 | Anbieter-Limits, Statusseiten, lange Chatverläufe, Fairness, Sprachen, Latenz-Budget, Herkunft von RAG-Quellen |
| 08 | Zeitzonen, weiches Löschen, neuer Abschnitt Echtzeit, Synchronisation und Offline |
| 09 | Mindestalter, Sicherheits-Benachrichtigungen, Update-Hinweise, Suche, Teilen, Bewertungsdialog |
| 10 | Sprachalternative, neuer Abschnitt Verständlichkeit |
| 11 | lange Texte, Gesten-Alternativen, bequeme Formulare |
| 12 | langsames Netz und alte Geräte, Doppelaktionen, gestaffeltes Rollout, Release-Tag, Domain und DNS |
| 13 | App Tracking Transparency, Nachahmer-Verbot, Gesundheitsangaben, Bewertungsregeln, Google-Pflichterklärungen, neuer Abschnitt Konten, Signierung und Versionen |
| 14 | Steuerrücklagen, Sanktionen, Rechtekette, neuer Abschnitt Team und Zugänge |
| 15 | Zahlungsdienste und Geldwäsche, Krypto (MiCA), Käufe von Minderjährigen, Grooming und Spam, Fernmeldegeheimnis, Plattform-Freigaben, neue Abschnitte Hardware und IoT, Märkte außerhalb der EU, Glücksspiel und Co., Politik und Wahlen |
| 16 | Datenschutz des Coding-Tools, erfundene Funktionen erkennen, zusätzliches Warnsignal |
| Prüf-Prompts | neuer Prompt zur Launch-Bereitschaft |

## 7a. Zweite Prüfung mit neuer Recherche (30. September 2026)

Neu recherchiert: OWASP-Ausgaben 2026, Verhaltenskodex zu Art. 50, deutsches KI-Durchführungsgesetz, Änderungen der Apple-Richtlinien (November 2025 und Juni 2026), Google-Play-Richtlinien (Juli 2026), EU-Leitlinien zum Schutz Minderjähriger, geplanter Digital Fairness Act, aktuelle Vibe-Coding-Sicherheitschecklisten, NIST AI RMF.

| Kapitel | Ergänzt oder aktualisiert |
|---|---|
| 01 | Verhaltenskodex zu Art. 50 final (10.06.2026) mit EU-Symbolen; Bundesnetzagentur seit 29.07.2026 zuständig (KI-MIG); KI-Risikoregister; ISO/IEC 42001 |
| 03 | süchtig machendes Design, angekündigter Digital Fairness Act |
| 05 | Pakete mit Installationsskripten oder Besitzerwechsel |
| 06 | OWASP 2026: verborgener Kontext statt nur Systemprompt, Injection über Audio; gefährliche Anleitungen; neuer Abschnitt L zu Agenten-Risiken |
| 07 | Energie sparen |
| 08 | Geldbeträge als Ganzzahl |
| 10 | blindes Vertrauen vermeiden, Ergebnisse erklären |
| 12 | Grenzwerte testen |
| 13 | Apple 4.1, 4.3 (verschärft Juni 2026) und 1.2.1(a); Declared Age Range; Google: KI-Integrationen in der Nutzerdaten-Richtlinie, Age Signals, anonyme Chats, Modell-Wrapper |
| 15 | Apple-Regeln zu Krediten und Krypto-Börsen; Alterssignale; EU-Leitlinien Minderjährige; US-Altersprüfungsgesetze |
| 16 | Security-Review nach riskanten Änderungen; Skills und Erweiterungen prüfen |

## 7b. Dritte Prüfung mit `/katalog-pruefen` (2. Oktober 2026)

Fünf Recherche-Agenten haben parallel geprüft: KI-Recht EU/DE, Datenschutz/Verbraucherrecht/Urheberrecht/Steuern, App Stores und KI-Anbieter, Sicherheit, Produkt/UX/Barrierefreiheit/Launch. Jeder Fund wurde gegen den Katalog abgeglichen; Funde mit niedriger Sicherheit stehen nur unter „Beobachten“. Drei folgenreiche Funde (Supabase-GRANT-Änderung, npm 12, Firebase App Check) wurden zusätzlich an der Primärquelle nachgeprüft.

**Wichtigste Korrekturen:**

- Art. 28 DSA gilt nicht für Kleinst- und Kleinunternehmen (Art. 19 DSA) – 03 H und 15 C korrigiert.
- Das neue AI-Act-Verbot (intime Darstellungen, Missbrauchsdarstellungen) gilt ab 02.12.2026 direkt, keine „Umsetzungsfrist“.
- Die Ausnahme nach Art. 6 Abs. 3 AI Act ist registrierungspflichtig (`PFLICHT` statt `SOLLTE`).
- BFSG: Barrierefreiheitsinformationen nach § 14 und Anlage 3 statt BITV-Begriffen; WCAG 2.2 statt 2.1 (EN 301 549 V4.1.1).
- Mehrere WCAG-Kriterien der Stufe A standen nur als `SOLLTE` im Katalog.
- Apple 4.3 (Juni 2026) hat keinen KI-Bezug; Vorlagen-Apps regelt 4.2.6.
- Google: anonyme Chats ab 26.08.2026 (nicht 14.08.); Store-Gebühren seit 30.06.2026 neu.
- Firebase-Regeln: `request.auth != null` reicht nicht, Besitz muss geprüft werden.
- Abo-Laufzeiten, Kleinunternehmer im Gründungsjahr, E-Rechnung und Aufbewahrungsfristen präzisiert.

**Ergänzt (Auswahl nach Kapitel):**

| Kapitel | Ergänzungen |
|---|---|
| 01 | KI-Compliance-Kompass der Bundesnetzagentur, Leitlinien zu KI-System-Definition, verbotenen Praktiken und Hochrisiko, Ein-Drittel-Regel beim Fine-Tuning, Leitlinien zu Art. 50 (20.07.2026), Abmahnrisiko, Bußgelder für kleine Mid-Caps, KI-MIG-Zuständigkeiten |
| 02 | Abmahnbarkeit von Datenschutzfehlern, Schadensersatz, Datenschutzhinweise schichten, Data-Privacy-Framework-Rückfallebene, Erklärung automatischer Entscheidungen, Scoring nach § 37a BDSG, Herkunft des Modells, neue DSK-Hilfen, Digital Omnibus noch nicht geltend, Newsletter-Tracking, Werbe-Einwilligungslösung (IAB TCF), Einwilligungsdienste |
| 03 | Kündigungs-Bestätigungsseite (BGH), Widerrufsbutton im Detail, Widerrufsbelehrung, Kündigungsbutton bei Einmalzahlung, Preiserhöhungen, § 327r BGB, ehrliche Update-Infos, Ranking-Transparenz, personalisierte Preise, Schlichtung im Streitfall, BFSG bei Gratis-Apps und MLBF, CRA-Leitlinien und Meldeweg, SBOM, Schwachstellen-Richtlinie, Produkthaftung (deutscher Entwurf), BKA-Meldung nach Art. 18 DSA, Data Act für SaaS |
| 04 | Haftung für auswendig gelernte Werke (GEMA-Urteile), Nutzungsvorbehalte nach OLG Hamburg |
| 05 | neue Supabase-Schlüssel und GRANT-Regel, Google-Schlüssel und Gemini, sensible Umgebungsvariablen, Better Auth, `user_metadata`, Server Actions, Views, Altspeicher, gehashte Tokens, fail closed, Installationsskripte (npm 12), Wartezeit für Pakete, `npm ci`, SHA-Pinning, signierte OTA-Updates, ZAP, ASVS 5.0 |
| 06 | tödliches Dreigespann, MCP-Rug-Pull, eigener MCP-Server mit OAuth |
| 07 | Firebase AI Logic mit App Check, Regeln der KI-Anbieter für Beratungs-Apps, Gemini-Bedingungen (EU, Minderjährige), Gratis-Tarife und Training, EU-Datenresidenz, Abkündigungsfristen, Art. 4a AI Act |
| 08 | Vorschau-Deployments schützen, Core-Web-Vitals-Grenzwerte |
| 09 | „Mit Apple anmelden“ beim Löschen widerrufen, Barrierefreiheitsinformationen |
| 10 | Nachfragen statt raten, Schmeichel-KI, Änderungen am KI-Verhalten mitteilen, Weg ohne KI, Credits fair verkaufen, barrierefreier KI-Chat |
| 11 | neue Abschnitte D (weitere WCAG-2.2-Regeln) und E (Barrierefreiheitsinformationen und Support), Systemeinstellungen, Liquid Glass, Android 16 |
| 12 | keine bekannten Lücken ausliefern, Android Vitals, kompromittierte Pakete, kritische Framework-Updates |
| 13 | Apple-EU-Bedingungen, Credits, Web-Abos, Kaufbildschirm, 4.2.6, 2.5.2, 4.7, anonyme Chats, regulierte Bereiche, Bewertungsregeln, Accessibility Nutrition Labels, Tracking-Domains, Ziel-API 36, Entwicklerverifizierung, Testphase, Google-Abo-Regeln, iOS-PWA, noindex, automatisches Posten, X, Kontosperren, Xcode 26, Vertriebsländer |
| 14 | Anmeldefrist, Kleinunternehmer im Gründungsjahr, EU-Kleinunternehmerregelung, Reverse Charge, Store-Einnahmen, monatliche Voranmeldung, E-Rechnung, Aufbewahrungsfristen, DAC7, Store-Gebühren, phishing-resistente Anmeldung |
| 15 | BNPL und § 34k GewO, Finanz-Chatbots, DiGA und TR-03161, OpenAI- und Anthropic-Regeln für Minderjährige, KI für Minderjährige standardmäßig aus, Jugendschutz-Modus der Betriebssysteme, EU-Alters-App, Erotik nur mit Altersverifikation, Pausenhinweise, Data Act ab Werk, politische Werbung, Alterskennzeichen in Spielen, neue Abschnitte S (Spiele) und T (Dating) |
| 16 | Security-Review als Pflicht, Coding-Agent nicht ohne Rückfragen, Agenten-Konfiguration prüfen, Secrets vor dem Agenten verbergen, Datenbank-MCP nur lesend, neue Warnsignale |
| 17 | ASO konkret, Vorbestellung, KI-Suche und Crawler, Werbekennzeichnung, Chatbot-Haftung (OLG Hamm), Pflichten nicht als Vorteil bewerben, Umweltversprechen, KI-Kundenstimmen, KI-Labels der Werbeplattformen, Kündigungsgründe, Empfehlungs-E-Mails, Bestandskunden-Werbung |

## 7c. Vierte Prüfung mit `/katalog-pruefen` (13. Oktober 2026)

Zuerst ein eigener Lückenabgleich: eine KI-App gedanklich von der Idee bis zur Einstellung durchgehen und dabei jeden Schritt sowie alle verbreiteten App-Typen gegen den Katalog prüfen (mit `grep`, ob ein Thema schon vorkommt). Danach fünf parallele Recherchen wie in der dritten Prüfung. Folgenreiche Funde wurden zusätzlich an der Primärquelle nachgeprüft (u. a. § 356 BGB, § 13 und § 13a UWG, Produkthaftungsgesetz, Gemini-Schlüssel, Next.js-Support, Claude-Code-Startmodus, Apple-Medizinprodukt-Status, Anthropic Usage Policy).

**Wichtigste Korrekturen:**

- Newsletter: Pflicht ist die nachweisbare Einwilligung; Double-Opt-in ist der übliche Nachweis, keine eigene Pflicht (03 D, 09 I).
- Widerrufsrecht bei KI-Abos: Die Checkbox-Regel für vorzeitiges Erlöschen gilt nur für digitale Inhalte (§ 356 Abs. 6 BGB); bei digitalen Dienstleistungen bleibt das Widerrufsrecht bis zur vollständigen Erbringung, vorher gibt es nur Wertersatz (03 C).
- Produkthaftungsgesetz am 8. Oktober 2026 vom Bundestag beschlossen, Inkrafttreten 9. Dezember 2026 (03 G).
- Art. 50 AI Act: Ausnahme „offensichtlich“ eng, Markierung von Medien braucht Metadaten und Wasserzeichen (01 D).
- Gemini-API lehnt uneingeschränkte Google-Schlüssel ab (05 A); alte Supabase-Schlüssel sind abgekündigt, nicht fest abgeschaltet (05 A).
- npm 12 wird nicht mit Node.js ausgeliefert (05 H); MCP-Spezifikation 2026-07-28 ohne Protokoll-Sitzungen (06 D).
- Anthropic-Hochrisiko-Liste ab 12. November 2026 neu gefasst; `temperature` bei neueren Modellen nicht mehr erlaubt (07 A und B).
- Apple: Altersfreigabe mit Social-Media-Frage, iOS-27-SDK ab April 2027, US-Altersgesetze in Texas, Utah und Louisiana; Google: Verifizierung außerhalb von Play nach Regionen (13).

**Ergänzt (Auswahl nach Kapitel):**

| Kapitel | Ergänzungen |
|---|---|
| 01 | KI-Hinweis im Gespräch statt nur in AGB, KI-Agenten nennen Auftraggeber, EU-Symbole, Modell-Dokumentation nach Art. 53, EN 18286, KI-MIG-Bußgelder bis 50.000 € |
| 02 | eingebettete Inhalte erst nach Klick, Chat-Inhalte nicht für Werbung (LG Köln), Widerspruchsrecht gesondert, Missbrauch bei Auskunft (EuGH C-526/24), jede Datenpanne dokumentieren, § 19 TDDDG, DSK-Hilfe „Digitale Dienste“, Stand Digital Omnibus und Data Privacy Framework |
| 03 | Social-Media-Impressum, Credits-Verfall, Bestellprozess (§ 312i), keine Zusatzkosten und Zahlungsgebühren, Gewährleistungshinweis, „Bezahlen mit Daten“, Nutzerinhalte nach Vertragsende (§ 327p), Kündigen ohne Login und per E-Mail, Gratis-Test mit Bezahl-Button, Preisanpassungsklauseln (BGH Amazon Prime), Telefonnummer in Pflichtinfos, Kontaktstelle nicht nur per Chatbot (Art. 12 DSA), DSA-Anordnungen, terroristische Inhalte, UrhDaG, Schlichtung ab 2028, neuer Abschnitt J (Abmahnung, Aufsicht, Polizei) |
| 04 | EDPB-Leitlinien zu Scraping und Anonymisierung, GEMA-Urteile mit Datum, KI-Musik prüfen, Nachahmer und Fake-Apps melden, Patentrisiko |
| 05 | geleakte Passwörter, Edge Functions, Endpunkt-Liste, geteilte Links, Git-Abhängigkeiten, Python-Wartezeit, `binding.gyp`, Trusted Publishing, Secrets nicht in KI-Chats |
| 06 | falsche KI-Aussagen über Personen, Denk-Budget, risikoarm starten (CISA), Kontrollpunkt vor Agenten-Aktionen |
| 07 | kein privates KI-Abo als Backend, Apple Foundation Models, Speicherpflichten einzelner Modelle, abgekündigte OpenAI-Funktionen, Einmal-Tokens, Gemini-Ausgabenlimits, ImageCreator |
| 08 | Antworten fremder Dienste prüfen |
| 10 | KI-Hinweis eindeutig und barrierefrei, KI nicht aufdrängen |
| 11 | Rechtsstatus EN 301 549 V4.1.1, Kontrast- und Farbeinstellungen im Web (9.7), WCAG 3 nur beobachten, faltbare iPhones |
| 09 | neue Apple-Relay-Adressen, Hotline ohne Aufpreis, Ein-Klick-Abmeldung, Sprachversionen |
| 12 | nur Versionen mit Sicherheitsupdates (Node.js 20, Next.js 15), Next.js-Sicherheitsreleases, Supabase-Backups, Backup außerhalb des Hauptkontos, Apple- und Google-Abos beim Einstellen geordnet beenden |
| 13 | Werbe-ID, Social Bots (MStV), Messenger-Bots, Exportkontrolle, Medizinprodukt-Status, Nutzerinhalte (1.2), keine Belohnung gegen Systemfreigaben, EU-Elternschranke, neuer Abschnitt G (Desktop-Apps und Browser-Erweiterungen) |
| 14 | Transparenzregister, unter 18 gründen, Nebentätigkeit und Sozialleistungen, US-Steuerformular, Künstlersozialabgabe, Verkauf der App, Kleinbetragsrechnungen, Scheinselbstständigkeit, Arbeitgeberpflichten |
| 15 | Google CASA, KI-Telefonie, Dark Patterns bei Finanzverträgen, DSA-Regeln kindgerecht, EU KIDS Act, Russmedia (Anzeigen), Data Act mit KMU-Ausnahme, EU-Vertreter, Not-Aus für KI-Geräte, Erotik-Verbote der Modellanbieter, Dating bei Google Play, JMStV-Kennzeichen, neuer Abschnitt U (Religion und Weltanschauung) |
| 16 | Startmodus mit KI-Klassifikator, Vibe-Coding-Plattform privat stellen, KI-Agenten in GitHub Actions, MCP-Liste, Plugins mit Wartezeit, eng begrenzte Zugriffstokens |
| 17 | KI-Werbung als Deepfake (auch Produktbilder), kein „AI Washing“, keine gekauften Likes oder Upvotes, Sterne-Durchschnitt, keine anonymen Zitate bei Google Play, Regeln der Launch-Plattformen, KI-Crawler und CDN, KI-Massenseiten, App-Store-Keywords in Bytes, neue App-Store-Werbeflächen |

**Bewusst nicht übernommen (unsichere Funde):** kalifornisches Altersgesetz AB 1043, Abschaltung aller Gemini-Standardschlüssel, Zahlen zum Wurm ChainDrop außer der Microsoft-Angabe, Inhalt des BSI-Zusatzes zu TR-03185, genauer Starttermin der deutschen EUDI-Wallet.

## 8. Bewusste Grenzen

Der Katalog ist eine Prüfliste. Diese Dinge leistet er absichtlich nicht:

- **Keine Rechtsberatung im Einzelfall.** Einordnungen (Hochrisiko, Erlaubnispflicht, Medizinprodukt, BFSG-Ausnahme) brauchen bei Unsicherheit eine fachliche Prüfung.
- **Außerhalb der EU nur Überblick.** Kapitel 15 P nennt die wichtigsten Regelwerke, ersetzt aber keine Länderprüfung.
- **Keine Branchenverfahren im Detail** (z. B. MDR-Zertifizierung, BaFin-Erlaubnisverfahren, Glücksspiellizenz).
- **Keine Framework-Anleitungen.** Konkrete Umsetzung steht in den [Plattform-Playbooks](../allgemeine-app-entwicklung/14-plattform-playbooks/README.md) und Leitfäden des Repositories.
- **Zeitabhängige Aussagen veralten.** Deshalb stehen sie mit Datum in [Quellen und Stand](./QUELLEN-UND-STAND.md).

## 9. Beobachten bis zur nächsten Prüfung

- **14.10.2026:** angekündigtes Next.js-Sicherheitsupdate; **um den 21.10.2026:** Ende der Wartung für Next.js 15; **23.10.2026:** Abschaltung vieler älterer OpenAI-Modelle.
- **30.10.2026:** Supabase-GRANT-Regel für bestehende Projekte, Ende der EDPB-Konsultation zur Anonymisierung; **01.11.2026:** Ende der Verlängerung für Ziel-API 36; **02.11.2026:** App-Check-Pflicht bei Firebase AI Logic; **10.11.2026:** Supabase entfernt ältere TLS-Verfahren (alte Geräte testen); **12.11.2026:** neue Anthropic Usage Policy; **30.11.2026:** Abschaltung Claude Sonnet 4.5 sowie OpenAI Agent Builder und gespeicherte Prompts; Bundesrat zum Produkthaftungsgesetz im November.
- **20.11.2026:** neues Verbraucherkreditrecht (BNPL), § 37a BDSG, § 34k GewO.
- **01.12.2026:** KJM bestimmt Betriebssysteme mit Jugendschutzvorrichtung (Pflichten etwa ein Jahr später).
- **02.12.2026:** neues AI-Act-Verbot und Ende der Übergangsfrist für Art. 50 Abs. 2.
- **03.12.2026:** Ende der Rückmeldefrist zum EU KIDS Act.
- **09.12.2026:** Inkrafttreten des neuen Produkthaftungsgesetzes (Bundestag hat am 08.10.2026 beschlossen); **11.12.2026:** weitere OpenAI-Abschaltungen (u. a. gpt-5-2025-08-07, o3).
- **Ende 2026:** Endfassung der Hochrisiko-Leitlinien, gemeinsame Leitlinien von EDPB und Kommission zu AI Act und DSGVO, EU-Alters-App, EN 301 549 V4.1.1 im Amtsblatt (erwartet 30.11. oder 16.12.2026), Abkündigung der alten Supabase-Schlüssel (Abschaltdatum offen), Jahressteuergesetz 2026 (monatliche Voranmeldung).
- **Anfang 2027:** Medizinprodukt-Status bei Apple für bestehende Apps; **01.02.2027:** alte Apple-Developer-ID-Zertifizierungsstelle läuft ab; **27.01.2027:** neue Google-Play-Berechtigungsregeln; **etwa Januar 2027:** npm beendet direktes Veröffentlichen mit Tokens, die 2FA umgehen; **April 2027:** iOS-27-SDK und iPhone-Duo-Screenshots.
- **2027:** E-Rechnung (Ausstellen), monatliche Voranmeldung für Gründer, Android-Entwicklerverifizierung außerhalb von Play, Xcode-27-Pflicht, Data-Act-Wechselentgelte entfallen (12.01.2027).
- Vorschlag der EU-Kommission für einen Digital Fairness Act (angekündigt für das vierte Quartal 2026) und EU KIDS Act (Vorschlag vom 17.09.2026).
- Digital Omnibus zu Daten (DSGVO, Cookies) und Omnibus IV (Art. 30 DSGVO): Inkrafttreten abwarten, erst dann Katalog anpassen.
- Gerichtsverfahren: BGH zu OLG Hamm (Chatbot-Haftung), OLG München zu GEMA gegen OpenAI, BGH zu LAION (Nutzungsvorbehalt), EuGH C-250/25 (KI und Urheberrecht), EuGH C-703/25 P (Data Privacy Framework).
- Deutsches Gesetz gegen digitale Gewalt (Deepfakes; Kabinettsbeschluss vom 07.10.2026, erste Lesung im Bundestag offen).
- BGH I ZR 5/26 zur Haftung von Tracking-Anbietern für Cookies ohne Einwilligung (Verhandlung am 08.10.2026, Urteil offen).
- WhatsApp-Verfahren der EU-Kommission gegen Meta (einstweilige Maßnahmen vom 09.06.2026).
- Startdatum der Registrierungspflicht nach Art. 6 Abs. 3 AI Act nach dem Digital Omnibus (an EUR-Lex prüfen).
- CRA-Durchführungsgesetz mit dem BSI als Marktüberwachungsbehörde; EN 18286 und weitere KI-Normen im Amtsblatt.
- Endfassung der OWASP MCP Top 10, Überarbeitung des NIST AI RMF, NIST IR 8596 (Cyber AI Profile), BSI-Projekt zu Prüfanforderungen für KI-Agenten.
- Berufungen und Revisionen: GEMA gegen Suno, LG München I und LG Aachen zu falschen KI-Aussagen, LG Köln zu Snap „My AI“, LAION (Stand der Revision prüfen).
- Durchführungsgesetz zur politischen Werbung (PWTG).
- Weitere Leitlinien der Bundesnetzagentur und des EU-AI-Office.
- CRA-Vollanwendung am 11. Dezember 2027, E-Rechnungs-Pflicht zum Ausstellen ab 2027/2028.
- Änderungen der App Review Guidelines und der Google-Play-Richtlinien.
- Neue Ausgaben der OWASP-Listen.

## 10. Wiederholung

Diese Prüfung wird bei der nächsten planmäßigen Aktualisierung (siehe [Quellen und Stand](./QUELLEN-UND-STAND.md)) mit denselben Referenzrahmen wiederholt. Neue Referenzrahmen werden als eigene Tabelle ergänzt.
