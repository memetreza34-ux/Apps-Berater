# KI-App-Kriterienkatalog

**Alles, was du bei KI-Apps und Vibe-Coding-Apps beachten musst – über 1.100 abhakbare Prüfpunkte in 17 Kapiteln, jeder mit kurzer Erklärung.**

**Stand:** 13. Oktober 2026 (inklusive Digital Omnibus zum AI Act, KI-MIG, Leitlinien und Kodex zu Art. 50, neuem Produkthaftungsgesetz, OWASP-Listen 2026, WCAG 2.2 nach EN 301 549 V4.1.1, Widerrufsbutton und Widerruf bei KI-Abos, neuer Anthropic-Richtlinie, neuen Apple- und Google-Regeln, Desktop-Apps und Browser-Erweiterungen und CRA-Meldepflichten)
**Für wen:** alle, die Apps mit KI bauen oder mit KI-Coding-Agenten wie Claude Code, Cursor, Codex, Lovable, Bolt oder Replit entwickeln.

> Dieser Katalog ersetzt keine Rechtsberatung. Er zeigt dir, **was** du prüfen musst. Bei Punkten mit hohem Risiko (Hochrisiko-KI, Gesundheit, Finanzen, Kinder) holst du dir fachliche Hilfe.

## Legende

Jeder Punkt hat eine Stufe:

| Stufe | Bedeutung |
|---|---|
| `PFLICHT` | Gesetz, Store-Regel oder kritisches Sicherheitsrisiko. Ohne diesen Punkt nicht veröffentlichen. Manche Pflichten gelten nur unter einer Bedingung – die steht dann in der Erklärung. |
| `SOLLTE` | Bewährte Praxis. Fehlt der Punkt, wird die App unsicherer, teurer, schlechter oder schwerer zu warten. |
| `KANN` | Profi-Niveau oder Nice-to-have. Sinnvoll, sobald die App wächst. |

Ein Haken `[x]` zählt nur, wenn du es **nachweisen** kannst (Screenshot, Test, Dokument, Commit).

## So benutzt du den Katalog

1. **Vor Projektstart:** Kapitel 17 (Abschnitt A–B), dann Kapitel 1–4 und 15 lesen. Klären, ob die Idee trägt und welche Gesetze und Sonderfälle gelten.
2. **Beim Bauen:** Kapitel 5–11 und 16 neben dem Coding offen haben. Die [Prüf-Prompts](./PRUEF-PROMPTS.md) regelmäßig von deinem Coding-Agenten laufen lassen.
3. **Vor dem Release:** Alle `PFLICHT`-Punkte abhaken. Dann Kapitel 12, 13 und 17 (Abschnitt C–E) durchgehen.
4. **Im Betrieb:** Kapitel 12 monatlich, [Quellen und Stand](./QUELLEN-UND-STAND.md) quartalsweise prüfen.

Tipp: Kopiere die Dateien in dein App-Repository (z. B. nach `docs/kriterien/`) und hake dort pro App ab.

## Kapitel

| Nr. | Kapitel | Worum es geht |
|---|---|---|
| 01 | [EU AI Act (KI-Verordnung)](./01-eu-ai-act.md) | Rolle, Verbote, Transparenz, Hochrisiko, Fristen, Strafen |
| 02 | [Datenschutz (DSGVO und TDDDG)](./02-datenschutz-dsgvo.md) | Rechtsgrundlagen, KI-Anbieter, Betroffenenrechte, Cookies, Datenpannen |
| 03 | [Verbraucherrecht, Impressum und weitere Gesetze](./03-verbraucherrecht-und-weitere-gesetze.md) | Impressum, AGB, Widerrufs- und Kündigungsbutton, BFSG, CRA, Produkthaftung, DSA, Abmahnung und Behördenanfragen |
| 04 | [Rechte, Urheberrecht und Lizenzen](./04-rechte-urheberrecht-lizenzen.md) | KI-Output, Trainingsdaten, Personen, Stimmen, Open Source, Marken |
| 05 | [Sicherheit – Grundlagen](./05-sicherheit-grundlagen.md) | Secrets, Auth, Datenbank und RLS, Eingaben, Uploads, Webhooks |
| 06 | [KI-Sicherheit und LLM-Risiken](./06-ki-sicherheit-llm-risiken.md) | Prompt Injection, Agenten, RAG, Moderation, OWASP LLM Top 10 |
| 07 | [KI-API, Modelle, Kosten und Qualität](./07-ki-api-modelle-kosten-qualitaet.md) | Modellwahl, Fehlerbehandlung, Kostenlimits, Evals, RAG, Agenten |
| 08 | [Architektur, Aufbau und Code](./08-architektur-aufbau-code.md) | Struktur, Umgebungen, Datenbank, Code-Qualität, CI, Dokumentation |
| 09 | [Pflichtfunktionen jeder App](./09-pflichtfunktionen.md) | Konto, Rechtsseiten, Einstellungen, Zahlung, Support, Admin |
| 10 | [KI-UX](./10-ki-ux.md) | Erwartungen, Streaming, Quellen, Kontrolle, Fehlerfälle |
| 11 | [Design und Barrierefreiheit](./11-design-barrierefreiheit.md) | Designsystem, Responsive, WCAG, Texte, Vertrauen |
| 12 | [Tests, Release und Betrieb](./12-tests-release-betrieb.md) | Tests, Deployment, Monitoring, Backups, Notfälle, Wartung |
| 13 | [App Stores und Plattformen](./13-app-stores-plattformen.md) | Apple, Google Play, Web, Social-Media-Plattformen und Messenger-Bots, Desktop-Apps, Browser-Erweiterungen |
| 14 | [Business, Zahlungen und Steuern](./14-business-zahlungen-steuern.md) | Gewerbe, Umsatzsteuer, Rechnungen, Künstlersozialabgabe, Versicherung, Verträge |
| 15 | [Sonderfälle nach App-Typ](./15-sonderfaelle-nach-app-typ.md) | Finanzen, Gesundheit, Kinder, Stimme, Community, Video, Agenten, Spiele, Dating, Religion |
| 16 | [Vibe-Coding-Arbeitsweise](./16-vibe-coding-arbeitsweise.md) | Sicher und sauber mit KI-Agenten entwickeln, Warnsignale |
| 17 | [Produkt, Launch und Wachstum](./17-produkt-launch-wachstum.md) | Idee prüfen, MVP, Launch, gefunden werden, Werberecht, Nutzer halten, Kennzahlen |
| – | [Prüf-Prompts für Coding-Agenten](./PRUEF-PROMPTS.md) | Fertige Prompts, mit denen die KI deine App gegen diesen Katalog prüft |
| – | [Quellen und Stand](./QUELLEN-UND-STAND.md) | Primärquellen, Prüfdatum, Prüfintervalle |
| – | [Vollständigkeitsprüfung](./VOLLSTAENDIGKEITSPRUEFUNG.md) | Abgleich mit AI Act, DSGVO, DSK, OWASP (LLM, Agenten, Web), NIST AI RMF, WCAG, Store-Regeln und dem Vollständigkeitsstandard des Repositories |

## Die 30 häufigsten Blocker bei Vibe-Coding-Apps

Wenn du nur wenig Zeit hast: Diese Punkte zuerst. Sie verursachen die meisten Datenlecks, Kostenexplosionen und Rechtsprobleme.

1. API-Key im Frontend oder im App-Bundle → [05](./05-sicherheit-grundlagen.md)
2. Supabase-Tabellen ohne Row Level Security (oder mit `GRANT ALL` an alle) oder Firebase-Regeln, die nur „angemeldet“ statt „Besitzer“ prüfen → [05](./05-sicherheit-grundlagen.md)
3. Nutzer A kann Daten von Nutzer B sehen (fehlende Berechtigungsprüfung auf dem Server) → [05](./05-sicherheit-grundlagen.md)
4. Nutzer kann sich selbst Admin- oder Premium-Rechte geben → [05](./05-sicherheit-grundlagen.md)
5. `.env` mit echten Keys in Git gelandet und nicht rotiert → [05](./05-sicherheit-grundlagen.md)
6. Kein Rate-Limit und kein Kostenlimit auf KI-Endpunkten → [07](./07-ki-api-modelle-kosten-qualitaet.md)
7. Kein Ausgabenlimit beim KI-Anbieter eingestellt → [07](./07-ki-api-modelle-kosten-qualitaet.md)
8. KI-Ausgabe wird ungeprüft als HTML, SQL oder Code ausgeführt → [06](./06-ki-sicherheit-llm-risiken.md)
9. KI-Agent darf ohne Bestätigung löschen, senden oder bezahlen → [06](./06-ki-sicherheit-llm-risiken.md)
10. RAG-Suche liefert Dokumente anderer Nutzer → [06](./06-ki-sicherheit-llm-risiken.md)
11. Chatbot nicht als KI gekennzeichnet → [01](./01-eu-ai-act.md)
12. Generierte Bilder, Videos oder Audios ohne maschinenlesbare Kennzeichnung → [01](./01-eu-ai-act.md)
13. Idee fällt unter verbotene KI-Praktiken oder Hochrisiko, ohne dass es geprüft wurde → [01](./01-eu-ai-act.md)
14. Datenschutzerklärung nennt den KI-Anbieter und die Datenübermittlung nicht → [02](./02-datenschutz-dsgvo.md)
15. Kein Auftragsverarbeitungsvertrag mit KI-, Hosting- und Datenbank-Anbieter → [02](./02-datenschutz-dsgvo.md)
16. Tracking oder Google Fonts laden vor der Einwilligung → [02](./02-datenschutz-dsgvo.md)
17. Konto löschen geht nicht in der App oder löscht nicht alle Daten → [09](./09-pflichtfunktionen.md)
18. Impressum fehlt oder ist nicht leicht erreichbar → [03](./03-verbraucherrecht-und-weitere-gesetze.md)
19. Abo ohne Kündigungsbutton oder ohne Widerrufsbutton, oder Widerrufsrecht bei KI-Abos falsch geregelt → [03](./03-verbraucherrecht-und-weitere-gesetze.md)
20. Stripe-Webhook ohne Signaturprüfung, Preis kommt vom Client → [05](./05-sicherheit-grundlagen.md)
21. Keine Backups oder Wiederherstellung nie getestet → [12](./12-tests-release-betrieb.md)
22. Coding-Agent arbeitet mit Zugriff auf die Produktionsdatenbank oder ganz ohne Rückfragen, oder das Projekt auf der Vibe-Coding-Plattform ist öffentlich → [16](./16-vibe-coding-arbeitsweise.md)
23. Kein Git oder keine regelmäßigen Commits → [16](./16-vibe-coding-arbeitsweise.md)
24. Erfundene oder unseriöse npm-/pip-Pakete installiert, Installationsskripte ungeprüft ausgeführt → [05](./05-sicherheit-grundlagen.md)
25. Keine Fehlerbehandlung, wenn die KI-API langsam ist oder ausfällt → [07](./07-ki-api-modelle-kosten-qualitaet.md)
26. Keine Moderation bei offenen Chats oder Bildgeneratoren → [06](./06-ki-sicherheit-llm-risiken.md)
27. Fremde Inhalte, Stimmen oder Gesichter ohne Rechte oder Einwilligung verarbeitet → [04](./04-rechte-urheberrecht-lizenzen.md)
28. Finanz-, Gesundheits- oder Rechtsberatung durch KI ohne Prüfung der Erlaubnispflicht → [15](./15-sonderfaelle-nach-app-typ.md)
29. Apple: Daten gehen an Drittanbieter-KI ohne Nennung des Anbieters und ohne aktive Zustimmung → [13](./13-app-stores-plattformen.md)
30. Keine Fehlerüberwachung, Probleme erfährt man erst von Nutzern → [12](./12-tests-release-betrieb.md)

## Zusammenhang mit dem restlichen Repository

- [App-Master-Anleitung](../app-master-anleitung/README.md) – der vollständige Weg von der Idee bis zum Betrieb.
- [Allgemeine App-Entwicklung](../allgemeine-app-entwicklung/README.md) – technische Vertiefungen, Vorlagen, Runbooks.
- [KI-Produktionsleitfaden](../allgemeine-app-entwicklung/04-ki-agenten/ki-produktionsleitfaden.md) – Vertiefung zu KI-Funktionen im Produktivbetrieb.
- [Checkliste vor jedem Release](../allgemeine-app-entwicklung/CHECKLISTE-VOR-JEDEM-RELEASE.md) – kurze Release-Freigabe.

Dieser Katalog ist die **breite Prüfliste**. Die anderen Bereiche erklären den **Weg** und liefern **Vorlagen**.

## Pflege

Gesetze, Store-Regeln und KI-Anbieter ändern sich schnell. Zeitabhängige Aussagen stehen mit Datum in [Quellen und Stand](./QUELLEN-UND-STAND.md). Vor jedem öffentlichen Release die Primärquellen erneut prüfen.
