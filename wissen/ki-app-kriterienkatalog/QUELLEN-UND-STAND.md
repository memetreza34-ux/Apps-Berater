# Quellen und Stand

**Letzte Prüfung:** 13. Oktober 2026
**Nächste planmäßige Prüfung:** 13. Januar 2027 (Quartal) – früher bei Gesetzesänderungen, neuen Store-Regeln oder vor einem öffentlichen Release. Besonders vormerken: 14.10. (Next.js-Sicherheitsupdate), 21.10. (Ende Next.js 15), 23.10. (OpenAI-Abschaltungen), 30.10. (Supabase-GRANT), 01.11. (Ziel-API-Verlängerung), 02.11. (Firebase App Check), 10.11. (Supabase TLS), 12.11. (neue Anthropic-Richtlinie), 20.11. (Kreditrecht), 30.11. (Claude Sonnet 4.5, OpenAI Agent Builder), 01.12. (KJM), 02.12. (AI-Act-Verbot, Art. 50 Abs. 2), 09.12.2026 (Produkthaftungsgesetz), 01.02.2027 (Apple Developer ID) und April 2027 (iOS-27-SDK).

Dieser Katalog trennt dauerhafte Grundsätze (z. B. „Keys nie im Client“) von zeitabhängigen Aussagen (z. B. Fristen, Schwellenwerte, Store-Regeln). Zeitabhängige Aussagen sind hier mit Quelle aufgeführt. Vor einem Release immer die Primärquelle öffnen.

## Zeitabhängige Kernaussagen

| Thema | Aussage im Katalog | Stand | Kapitel |
|---|---|---|---|
| AI Act – Zeitplan | Verbote und KI-Kompetenz seit 02.02.2025, GPAI seit 02.08.2025, Art. 50 seit 02.08.2026, Anhang III ab 02.12.2027, Anhang I ab 02.08.2028 | Digital Omnibus (VO (EU) 2026/1744), in Kraft seit 27.07.2026 | 01 |
| AI Act – neues Verbot | Verbot von KI zur Erzeugung nicht einvernehmlicher intimer Darstellungen und von Missbrauchsdarstellungen von Kindern, gilt ab 02.12.2026 | Digital Omnibus | 01, 06, 15 |
| AI Act – Art. 50 Abs. 2 | Kennzeichnungsfrist 02.12.2026 für Systeme, die vor dem 02.08.2026 auf dem Markt waren | Digital Omnibus | 01 |
| AI Act – Art. 4 | KI-Kompetenz als Bemühungspflicht (fördern statt sicherstellen) | Digital Omnibus | 01 |
| AI Act – Art. 50 | Verhaltenskodex Endfassung 10.06.2026 (EU-Symbole), Leitlinien Endfassung 20.07.2026 | EU-Kommission | 01 |
| AI Act – deutsche Aufsicht | Bundesnetzagentur Marktüberwachung, Anlaufstelle und Beschwerdestelle; KI-MIG in Kraft seit 29.07.2026; nationale Bußgelder bis 50.000 € (§ 15) | KI-MIG vom 22.07.2026, BGBl. 2026 I Nr. 223 | 01 |
| AI Act – Art. 6 Abs. 3 | Registrierungspflicht für als nicht hochriskant eingestufte Anhang-III-Systeme (ab 02.12.2027) | Art. 6 Abs. 4, Art. 49 Abs. 2 AI Act | 01 |
| AI Act – Hochrisiko-Leitlinien | Entwurf vom 19.05.2026, Endfassung bis Ende 2026 erwartet | EU-Kommission | 01 |
| OWASP Top 10 (Web) | Ausgabe 2025 (u. a. neue Kategorien Lieferkette und Fehlerbehandlung) | OWASP | 05 |
| OWASP LLM Top 10 | Ausgabe 2026 vom 03.08.2026, neue Reihenfolge, „Hidden Context Exposure“ | OWASP GenAI Security Project | 06 |
| OWASP Agentic Top 10 | Ausgabe 2026 (ASI01–ASI10), veröffentlicht 09.12.2025 | OWASP GenAI Security Project | 06 |
| Digital Fairness Act | Vorschlag angekündigt für Q4 2026 (Dark Patterns, süchtig machendes Design) | Arbeitsprogramm EU-Kommission | 03 |
| Widerrufsbutton | Pflicht seit 19.06.2026 (§ 356a BGB): „Vertrag widerrufen“, zwei Schritte, Eingangsbestätigung; Belehrung muss auf die Funktion hinweisen; seit 27.09.2026 Hinweis auf gesetzliche Gewährleistung (Art. 246a § 1 Abs. 1 Nr. 11b EGBGB) | BGBl. 2026 I Nr. 28 | 03, 09 |
| Widerruf bei digitalen Dienstleistungen | erlischt erst mit vollständiger Erbringung (§ 356 Abs. 5 BGB); Checkbox-Regel nur für digitale Inhalte (§ 356 Abs. 6) | Gesetzesstand Oktober 2026 | 03 |
| Kündigungsbutton | Pflicht seit 01.07.2022 (§ 312k BGB) | Gesetzesstand September 2026 | 03, 09 |
| Kündigungs-Bestätigungsseite | keine Halteangebote auf der Seite nach dem Kündigungsbutton | BGH, Urteil vom 16.07.2026, I ZR 200/25 | 03, 17 |
| Chatbot-Aussagen | Falsche Aussagen eines KI-Chatbots werden dem Betreiber als Werbung zugerechnet | OLG Hamm, Urteil vom 12.05.2026, 4 UKl 3/25 (Revision zugelassen) | 17 |
| UWG-Änderung | Verbot pauschaler Umweltaussagen und irreführender Update-Informationen | gilt seit 27.09.2026, BGBl. 2026 I Nr. 43 | 03, 17 |
| Abmahnungen | kein Kostenersatz für Mitbewerber bei Informationspflichten online und DSGVO-Verstößen (unter 250 Beschäftigte); keine Vertragsstrafe bei erster Abmahnung (unter 100) | § 13 Abs. 4, § 13a UWG | 03 |
| Dark Patterns bei Finanzverträgen | Verbot nach Art. 246b § 4 EGBGB | seit 19.06.2026 | 15 |
| Datenschutz und UWG | DSGVO-Verstöße (Art. 7, 9, 12, 13) durch Wettbewerber und Verbände abmahnbar | BGH, 27.03.2025 | 02 |
| Verbraucherkredit und Scoring | neues Kreditrecht (u. a. BNPL), § 37a BDSG, § 34k GewO | gilt ab 20.11.2026, BGBl. 2026 I Nr. 139 | 02, 15 |
| EU-Streitschlichtungsplattform | abgeschaltet am 20.07.2025 | – | 03 |
| BFSG | gilt seit 28.06.2025; Informationen nach § 14 und Anlage 3; Aufsicht MLBF; Bußgeld bis 100.000 €; EN 301 549 V4.1.1 (WCAG 2.2) seit 02.09.2026, Amtsblatt-Listung erwartet | Gesetzesstand Oktober 2026 | 03, 11 |
| CRA | Meldepflichten seit 11.09.2026 über die ENISA-Meldeplattform (24 h / 72 h / Abschlussbericht), Leitlinien vom 27.07.2026, volle Pflichten ab 11.12.2027 | EU-Kommission, ENISA, BSI | 03, 12 |
| Produkthaftung | neues Produkthaftungsgesetz (RL (EU) 2024/2853), vom Bundestag am 08.10.2026 beschlossen, Inkrafttreten 09.12.2026; Bundesrat im November | BT-Drs. 21/4297 und 21/8429 | 03 |
| Data Act | gilt seit 12.09.2025; Datenzugang ab Werk für neue Geräte seit 12.09.2026; keine Wechselentgelte ab 12.01.2027; Aufsicht Bundesnetzagentur | DADG, Bundesnetzagentur | 03, 15 |
| Kleinunternehmer | 25.000 € Vorjahr / 100.000 € laufendes Jahr; im Gründungsjahr nur 25.000 €; EU-Kleinunternehmerregelung (§ 19a UStG) | UStG seit 01.01.2025 | 14 |
| E-Rechnung | Empfang seit 01.01.2025; Ausstellung B2B ab 01.01.2027 (Vorjahresumsatz über 800.000 €), ab 01.01.2028 für alle außer Kleinunternehmer | § 34a UStDV | 14 |
| Umsatzsteuer-Voranmeldung | monatlich für Gründer wieder ab 01.01.2027 | § 18 UStG | 14 |
| Apple 5.1.2(i) | Offenlegung mit Nennung des KI-Anbieters und aktive Zustimmung vor Weitergabe personenbezogener Daten an Drittanbieter-KI | App Review Guidelines, Änderung vom 13.11.2025 | 13 |
| Apple ATT | Tracking-Dialog vor anbieterübergreifendem Tracking | App Review Guidelines, aktuelle Fassung prüfen | 13 |
| Google Play Erklärungen | Erklärungen zu Finanz- und Gesundheitsfunktionen für alle Apps verpflichtend | Play Console Hilfe, aktuelle Fassung prüfen | 13 |
| Apple 1.2.1(a), 4.1(c), 3.2.2(ix), 5.1.1(ix) | Altersbeschränkung in Creator-Apps, fremde Marken, Kredit-Obergrenzen, Krypto-Börsen | App Review Guidelines, Änderung vom 13.11.2025 | 13, 15 |
| Apple 4.2.6, 4.3 und 2.5.2 | Vorlagen-Apps (4.2.6); Duplikat-Apps, nachträgliche Entfernung, Ausschluss bei Wiederholung (4.3, geändert 08.06.2026); kein nachgeladener Code (2.5.2) | App Review Guidelines | 13 |
| Apple EU-Bedingungen | einheitliche Bedingungen ab 01.10.2026 (Provisionen für In-App-Kauf, alternative Zahlung, Web-Links, Elternschranke für Minderjährige, 5 % Core Technology Commission bei alternativem Vertrieb) | Apple Developer News vom 18.08.2026, Apps in the EU | 13, 14 |
| Apple SDK | Uploads nur mit Xcode 26 und iOS-26-SDK seit 28.04.2026, ab April 2027 iOS-27-SDK und iPhone-Duo-Screenshots | Apple Upcoming Requirements, Developer News Oktober 2026 | 11, 13 |
| Apple Altersfreigabe und Medizinprodukt | Social-Media-Funktionen Pflichtangabe seit September 2026; Medizinprodukt-Status für neue Apps seit 26.03.2026, für bestehende bis Anfang 2027 | Apple Developer News | 13 |
| Apple macOS | alte Developer-ID-Zertifizierungsstelle läuft am 01.02.2027 ab; macOS 27 letzte Version mit Rosetta | Apple Developer News | 13 |
| US-Altersgesetze | Apple: Texas (04.06.2026), Utah (06.05.2026), Louisiana (01.07.2026); Google Play: Texas über Age Signals API | Apple Developer News, Play Console Hilfe | 13 |
| Google Play 2026 | KI-Integrationen in der Nutzerdaten-Richtlinie; anonyme Chats ab 26.08.2026 (Restrict Minor Access); Ziel-API 36 seit 31.08.2026 (Verlängerung bis 01.11.2026); App-Registrierung bis 30.09.2026; Entwicklerverifizierung außerhalb von Play in BR, ID, SG, TH seit 30.09.2026, weltweit 2027; neue Gebühren seit 30.06.2026; Berechtigungsänderungen ab 27.01.2027 | Play Console Hilfe | 13, 14 |
| Google Play Age Signals | Nutzung der Altersdaten nur für altersgerechte Inhalte, seit 01.01.2026 | Play Console Hilfe | 13 |
| Impressum | Wirtschafts-Identifikationsnummer angeben, sobald zugeteilt (§ 5 Abs. 1 Nr. 6 DDG) | Gesetzesstand September 2026 | 03 |
| Funkanlagen | Cybersicherheitsanforderungen der Funkanlagenrichtlinie seit 01.08.2025 | Delegierte VO (EU) 2022/30 | 15 |
| Krypto | Kryptowerte-Dienstleistungen erlaubnispflichtig nach MiCA | VO (EU) 2023/1114 | 15 |
| Politische Werbung | Transparenz- und Kennzeichnungspflichten | VO (EU) 2024/900 | 15 |
| Google Play KI-Inhalte | Schutzmaßnahmen und Meldefunktion für KI-generierte Inhalte | Developer Program Policies, aktuelle Fassung prüfen | 13 |
| Gemini API | EU, Schweiz, UK nur bezahlte Dienste; nicht für Apps, die sich an Minderjährige richten; Ausgabenlimits pro Projekt seit März 2026 | Gemini API Additional Terms, Changelog | 07 |
| Anthropic Usage Policy | neue Fassung gültig ab 12.11.2026 (neu gefasste Hochrisiko-Liste, kein Zugang über Verbraucher-Abos, Hardware-Steuerung) | anthropic.com/legal/aup | 07, 15 |
| Modell-Abkündigungen | OpenAI: viele ältere Modelle am 23.10.2026 (u. a. gpt-3.5-turbo, gpt-4-turbo, o1, o3-mini, o4-mini, gpt-image-1), weitere am 01.12. und 11.12.2026 (u. a. gpt-5-2025-08-07, o3) sowie 2027; Assistants API seit 26.08.2026 abgeschaltet, Agent Builder und gespeicherte Prompts enden 30.11.2026. Anthropic: Claude Sonnet 4.5 am 30.11.2026. Gemini: 2.5-Modelle seit 18.09.2026 nur für Bestandsnutzer | Abkündigungsseiten der Anbieter | 07 |
| WhatsApp Business | allgemeine KI-Assistenten seit 15.01.2026 ausgeschlossen; EU-Kommission: einstweilige Maßnahmen vom 09.06.2026, Verfahren läuft | EU-Kommission | 13 |
| Supabase | Tabellen ab 30.10.2026 auch in bestehenden Projekten nur mit GRANT über die API erreichbar; alte API-Schlüssel bis Ende 2026 abgekündigt (Abschaltdatum offen); tägliche Backups erst ab Pro | Supabase Changelog und Docs | 05, 12 |
| Gemini-API-Schlüssel | uneingeschränkte Schlüssel werden abgelehnt; neue AI-Studio-Schlüssel seit 28.05.2026 als Auth-Keys | Gemini-API-Dokumentation | 05 |
| Laufzeiten und Frameworks | Node.js 20 ohne Updates; Next.js 15 fällt um den 21.10.2026 aus der Wartung (zwei Jahre nach Erscheinen) | Node.js, Next.js Support Policy | 12 |
| MCP-Spezifikation | Version 2026-07-28 (keine Protokoll-Sitzungen mehr, State Handles) | modelcontextprotocol.io | 06 |
| npm 12 | Installationsskripte von Abhängigkeiten standardmäßig gesperrt; Node.js liefert noch npm 11 mit | GitHub Changelog, Node.js Downloads | 05 |
| Firebase AI Logic | App Check Pflicht ab 02.11.2026 | Firebase-Dokumentation | 07 |
| JMStV | geschlossene Benutzergruppe für Pornografie; Jugendschutzvorrichtung im Betriebssystem (KJM-Festlegung bis 01.12.2026); Alterskennzeichen für eigene Spiele, Filme und Serien seit 01.06.2026 (§ 5c Abs. 3) | JMStV i. d. F. vom 01.12.2025, KJM | 15 |
| AI Act – Art. 50 Leitlinien | Hinweis im Gespräch, Ausnahme „offensichtlich“ eng; KI-Agenten nennen Auftraggeber; Werbung mit KI-Produktbildern kann Deepfake sein | Leitlinien vom 20.07.2026 | 01, 17 |
| Künstlersozialabgabe | 4,9 % (2026), 5,0 % (2027); Bagatellgrenze 1.000 € (2026) | KSA-Verordnungen | 14 |
| E-Rechnung Kleinbeträge | Rechnungen bis 250 € brutto weiter als PDF oder Papier | § 33 UStDV | 14 |
| Terroristische Inhalte | Entfernung binnen einer Stunde nach Anordnung, Kontaktstelle | VO (EU) 2021/784, TerrOIBG | 03 |
| EU KIDS Act | Vorschlag vom 17.09.2026, Feedback bis 03.12.2026 | EU-Kommission | 15 |

## Primärquellen

### EU-Recht

- KI-Verordnung (EU) 2024/1689: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- Digital Omnibus zu KI, Verordnung (EU) 2026/1744: https://eur-lex.europa.eu/eli/reg/2026/1744/oj
- EU-Kommission, Rechtsrahmen KI: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- EU-Kommission, AI Omnibus in Kraft: https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force
- EU-Kommission, Leitlinien zu Transparenzpflichten (Art. 50): https://digital-strategy.ec.europa.eu/en/library/guidelines-transparency-obligations-providers-and-deployers-ai-systems
- EU-Kommission, Verhaltenskodex zu KI-generierten Inhalten: https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content
- EU-Kommission, Leitlinien zum Schutz Minderjähriger (DSA): https://digital-strategy.ec.europa.eu/en/library/commission-publishes-guidelines-protection-minors
- DSGVO (EU) 2016/679: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- Digital Services Act (EU) 2022/2065: https://eur-lex.europa.eu/eli/reg/2022/2065/oj
- Cyber Resilience Act (EU) 2024/2847: https://eur-lex.europa.eu/eli/reg/2024/2847/oj
- CRA-Meldepflichten: https://digital-strategy.ec.europa.eu/en/policies/cra-reporting
- Produkthaftungsrichtlinie (EU) 2024/2853: https://eur-lex.europa.eu/eli/dir/2024/2853/oj
- Data Act (EU) 2023/2854: https://eur-lex.europa.eu/eli/reg/2023/2854/oj
- Richtlinie (EU) 2023/2673 (Widerrufsfunktion): https://eur-lex.europa.eu/eli/dir/2023/2673/oj
- Geoblocking-Verordnung (EU) 2018/302: https://eur-lex.europa.eu/eli/reg/2018/302/oj
- P2B-Verordnung (EU) 2019/1150: https://eur-lex.europa.eu/eli/reg/2019/1150/oj
- MiCA-Verordnung (EU) 2023/1114: https://eur-lex.europa.eu/eli/reg/2023/1114/oj
- Verordnung (EU) 2024/900 über politische Werbung: https://eur-lex.europa.eu/eli/reg/2024/900/oj
- Verordnung (EU) 2021/784 über terroristische Online-Inhalte: https://eur-lex.europa.eu/eli/reg/2021/784/oj
- Schlichtungsrichtlinie (EU) 2025/2647: https://eur-lex.europa.eu/eli/dir/2025/2647/oj
- EU-Symbole für KI-generierte Inhalte: https://digital-strategy.ec.europa.eu/en/policies/eu-icons-labelling-ai-generated-content
- EU KIDS Act erklärt: https://digital-strategy.ec.europa.eu/en/faqs/kids-act-explained
- EDPB zu Anonymisierung und Web-Scraping (Juli 2026): https://www.edpb.europa.eu/news/edpb-sheds-light-on-anonymisation-and-web-scraping-for-generative-ai-and-adopts-final-version_en
- EuGH Russmedia (C-492/23), Pressemitteilung: https://curia.europa.eu/jcms/upload/docs/application/pdf/2025-12/cp250150en.pdf

### Deutsches Recht

- Gesetze im Internet (BGB, BDSG, DDG, TDDDG, BFSG, UrhG, UWG, UStG, RDG): https://www.gesetze-im-internet.de/
- BGB: https://www.gesetze-im-internet.de/bgb/
- DDG: https://www.gesetze-im-internet.de/ddg/
- TDDDG: https://www.gesetze-im-internet.de/tdddg/
- BFSG: https://www.gesetze-im-internet.de/bfsg/
- UrhG: https://www.gesetze-im-internet.de/urhg/
- KI-MIG: https://www.gesetze-im-internet.de/ki-mig/BJNR0DF0B0026.html
- DSK-Orientierungshilfe „KI und Datenschutz“: https://www.datenschutzkonferenz-online.de/media/oh/20240506_DSK_Orientierungshilfe_KI_und_Datenschutz.pdf
- § 5 DDG (Impressum): https://www.gesetze-im-internet.de/ddg/__5.html
- § 356a BGB (Widerrufsfunktion): https://www.gesetze-im-internet.de/bgb/__356a.html
- § 327r BGB (Änderungen digitaler Produkte): https://www.gesetze-im-internet.de/bgb/__327r.html
- UWG mit Anhang: https://www.gesetze-im-internet.de/uwg_2004/
- § 14 BFSG und Anlage 3: https://www.gesetze-im-internet.de/bfsg/__14.html
- § 13b UStG (Reverse Charge): https://www.gesetze-im-internet.de/ustg_1980/__13b.html
- Plattformen-Steuertransparenzgesetz (DAC7): https://www.gesetze-im-internet.de/psttg/
- DSK-Orientierungshilfe TOM bei KI-Systemen: https://www.datenschutzkonferenz-online.de/media/oh/DSK-OH_KI-Systeme.pdf
- DSK-Orientierungshilfe RAG: https://www.datenschutzkonferenz-online.de/media/oh/DSK_OH_RAG.pdf
- Bundesnetzagentur KI: https://www.bundesnetzagentur.de/DE/Fachthemen/Digitales/KI/start_ki.html
- KJM zu Pornografie und Altersverifikation: https://www.kjm-online.de/themen/aufsicht-internet/pornografie/
- § 356 BGB (Erlöschen des Widerrufsrechts): https://www.gesetze-im-internet.de/bgb/__356.html
- § 13 UWG (Abmahnung): https://www.gesetze-im-internet.de/uwg_2004/__13.html
- § 13a UWG (Vertragsstrafe): https://www.gesetze-im-internet.de/uwg_2004/__13a.html
- Art. 246a EGBGB (Informationspflichten): https://www.gesetze-im-internet.de/bgbeg/art_246a__1.html
- Art. 246b § 4 EGBGB (Dark Patterns bei Finanzverträgen): https://www.gesetze-im-internet.de/bgbeg/art_246b__4.html
- § 327p BGB (Nutzerinhalte nach Vertragsende): https://www.gesetze-im-internet.de/bgb/__327p.html
- § 19 TDDDG (technischer Schutz): https://www.gesetze-im-internet.de/ttdsg/__19.html
- § 2 UrhDaG (Diensteanbieter, Start-ups): https://www.gesetze-im-internet.de/urhdag/__2.html
- Bundesnetzagentur zu terroristischen Online-Inhalten: https://www.bundesnetzagentur.de/DE/Fachthemen/Digitales/Schutz/TerrorOnlIn/start.html
- § 18 Medienstaatsvertrag (Social Bots): https://www.gesetze-bayern.de/Content/Document/MStV-18
- Bundestag zum Produkthaftungsgesetz (08.10.2026): https://www.bundestag.de/dokumente/textarchiv/2026/kw41-de-produkthaftungsrecht-1222456
- § 33 UStDV (Kleinbetragsrechnungen): https://www.gesetze-im-internet.de/ustdv_1980/__33.html
- Deutsche Rentenversicherung zur Künstlersozialabgabe 2026: https://www.deutsche-rentenversicherung.de/DRV/DE/Ueber-uns-und-Presse/Presse/Meldungen/2025/250724-kuenstlersozialabgabe-sinkt-ab-2026
- KJM-Infoblatt Kennzeichnungspflicht 2026: https://www.kjm-online.de/fileadmin/user_upload/KJM/Themen/Technischer_Jugendmedienschutz/KJM_Infosheet_Kennzeichnungspflicht_2026.pdf

### Plattformen

- Apple App Review Guidelines: https://developer.apple.com/app-store/review/guidelines/
- Apple Kontolöschung: https://developer.apple.com/support/offering-account-deletion-in-your-app
- Apple App Privacy: https://developer.apple.com/app-store/app-privacy-details/
- Google Play Developer Program Policies: https://play.google.com/about/developer-content-policy/
- Google Play Kontolöschung: https://support.google.com/googleplay/android-developer/answer/13327111
- Google Play Data Safety: https://support.google.com/googleplay/android-developer/answer/10787469
- Google Play Erklärung Finanzfunktionen: https://support.google.com/googleplay/android-developer/answer/13849271
- Google Play Erklärung Gesundheits-Apps: https://support.google.com/googleplay/android-developer/answer/14738291
- Google Play Richtlinien-Ankündigung Juli 2026: https://support.google.com/googleplay/android-developer/answer/17134731
- Google Play KI-generierte Inhalte: https://support.google.com/googleplay/android-developer/answer/14094294
- Apple-Meldung zur Änderung der Review Guidelines (November 2025): https://developer.apple.com/news/?id=ey6d8onl
- Apple Upcoming Requirements: https://developer.apple.com/news/upcoming-requirements/
- Apple DMA und Apps in der EU: https://developer.apple.com/support/dma-and-apps-in-the-eu/
- Google Play Fristen-Übersicht: https://support.google.com/googleplay/android-developer/table/12921780
- Google Play Ziel-API-Level: https://support.google.com/googleplay/android-developer/answer/11926878
- Gemini API Bedingungen: https://ai.google.dev/gemini-api/terms
- Anthropic Usage Policy: https://www.anthropic.com/legal/aup
- OpenAI Hinweise für Nutzer unter 18: https://developers.openai.com/api/docs/guides/safety-checks/under-18-api-guidance
- Anthropic Usage Policy, Ankündigung der Fassung ab 12.11.2026: https://www.anthropic.com/news/2026-usage-policy-update
- OpenAI Abkündigungen: https://developers.openai.com/api/docs/deprecations
- Anthropic Modell-Abkündigungen: https://platform.claude.com/docs/en/about-claude/model-deprecations
- Gemini-API-Schlüssel: https://ai.google.dev/gemini-api/docs/api-key
- Apple Medizinprodukt-Status: https://developer.apple.com/news/?id=nyqbfz1y
- Apple iPhone-Duo-Screenshots ab April 2027: https://developer.apple.com/news/?id=kkphp5qo
- Apple Apps in der EU: https://developer.apple.com/support/apps-in-the-eu/
- Apple Exportkontrolle für Verschlüsselung: https://developer.apple.com/documentation/security/complying-with-encryption-export-regulations
- Apple Foundation Models, Nutzungsregeln: https://developer.apple.com/apple-intelligence/acceptable-use-requirements-for-the-foundation-models-framework/
- Android-Entwicklerverifizierung: https://developer.android.com/developer-verification
- Google OAuth, eingeschränkte Berechtigungen und Sicherheitsbewertung: https://developers.google.com/identity/protocols/oauth2/production-readiness/restricted-scope-verification
- Chrome Web Store Programmrichtlinien: https://developer.chrome.com/docs/webstore/program-policies/policies
- EU-Kommission zu WhatsApp und KI-Assistenten (09.06.2026): https://europa.eu/newsroom/ecpc-failover/pdf/ip-26-1276_en.pdf

### Sicherheit und Barrierefreiheit

- OWASP Top 10 für LLM-Anwendungen 2026: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/
- OWASP Top 10 für agentische Anwendungen 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- OWASP Top 10 (Web) 2025: https://top10.owasp.org/2025/
- OWASP ASVS 5.0: https://github.com/OWASP/ASVS
- BSI/ANSSI: Zero-Trust-Prinzipien für LLM-Systeme: https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/ANSSI-BSI-joint-releases/LLM-based_Systems_Zero_Trust.html
- MCP-Sicherheitsempfehlungen: https://modelcontextprotocol.io/specification/latest/basic/security_best_practices
- Supabase API-Schlüssel: https://supabase.com/docs/guides/api/api-keys
- Supabase GRANT-Änderung: https://supabase.com/changelog/45329-breaking-change-tables-not-exposed-to-data-and-graphql-api-automatically
- npm v12 Änderungen: https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/
- Firebase AI Logic App Check: https://firebase.google.com/docs/ai-logic/app-check
- EN 301 549 V4.1.1: https://www.etsi.org/deliver/etsi_en/301500_301599/301549/04.01.01_60/en_301549v040101p.pdf
- OWASP MASVS: https://mas.owasp.org/MASVS/
- Supabase Row Level Security: https://supabase.com/docs/guides/database/postgres/row-level-security
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- Electron-Sicherheitscheckliste: https://www.electronjs.org/docs/latest/tutorial/security
- Next.js Support Policy: https://nextjs.org/support-policy
- Supabase Edge Functions, Anmeldung: https://supabase.com/docs/guides/functions/auth
- Supabase Backups: https://supabase.com/docs/guides/platform/backups
- OWASP API Security Top 10: https://api-security.owasp.org/
- OWASP MCP Top 10 (Beta): https://owasp.org/www-project-mcp-top-10/
- CISA und Partner, Leitfaden zu agentischer KI: https://www.cisa.gov/news-events/news/cisa-us-and-international-partners-release-guide-secure-adoption-agentic-ai
- Claude Code Berechtigungsmodi: https://code.claude.com/docs/en/permission-modes

Weitere Quellen des Repositories: [Quellen- und Aktualisierungsregister der Master-Anleitung](../app-master-anleitung/QUELLEN-UND-AKTUALISIERUNGSREGISTER.md) und [Quellen und Rechtsstand des Handbuchs](../allgemeine-app-entwicklung/QUELLEN-UND-RECHTSSTAND.md).

## Prüfintervalle

- **Vor jedem Release:** Store-Regeln, Datenschutzangaben, Rechtstexte, KI-Anbieter-Bedingungen.
- **Monatlich:** Sicherheitswarnungen, Abhängigkeiten, Abkündigungen von KI-Modellen.
- **Quartalsweise:** diese Datei, Fristen im AI Act, Leitlinien der EU-Kommission, Verbraucherrecht.
- **Anlassbezogen:** neue KI-Funktion, neue Zielgruppe (z. B. Kinder), neues Land, neue Datenart, Zahlungen.

## Änderungsprotokoll

| Datum | Änderung |
|---|---|
| 29.09.2026 | Erste Fassung des KI-App-Kriterienkatalogs mit 16 Kapiteln, Prüf-Prompts und Quellen. |
| 29.09.2026 | Vollständigkeitsprüfung: Kapitel 17 (Produkt, Launch, Wachstum) ergänzt, rund 160 weitere Prüfpunkte in allen Kapiteln, Apple-5.1.2-Punkt präzisiert, Impressum um Wirtschafts-ID ergänzt. Details: [Vollständigkeitsprüfung](./VOLLSTAENDIGKEITSPRUEFUNG.md). |
| 30.09.2026 | Zweite Prüfung mit neuer Recherche: OWASP-Ausgaben 2026, Kennzeichnungskodex zu Art. 50, KI-MIG, neue Apple- und Google-Regeln, EU-Leitlinien Minderjährige, Digital Fairness Act, Vibe-Coding-Checklisten. Details: [Vollständigkeitsprüfung](./VOLLSTAENDIGKEITSPRUEFUNG.md). |
| 02.10.2026 | Dritte Prüfung mit `/katalog-pruefen`: fünf parallele Recherchen (KI-Recht, Datenschutz und Steuern, Stores und KI-Anbieter, Sicherheit, UX und Barrierefreiheit), rund 140 neue und 40 korrigierte Punkte, neue WCAG-2.2-Abschnitte, neue Abschnitte für Spiele und Dating. Details: [Vollständigkeitsprüfung](./VOLLSTAENDIGKEITSPRUEFUNG.md). |
| 13.10.2026 | Vierte Prüfung mit `/katalog-pruefen`: eigener Lückenabgleich über Lebenszyklus und App-Typen plus fünf parallele Recherchen; rund 120 neue und 45 korrigierte Punkte, neue Abschnitte 03 J (Abmahnung, Aufsicht, Polizei), 13 G (Desktop-Apps und Browser-Erweiterungen) und 15 U (Religion und Weltanschauung); wichtige Korrektur zum Widerrufsrecht bei KI-Abos. Details: [Vollständigkeitsprüfung](./VOLLSTAENDIGKEITSPRUEFUNG.md). |
