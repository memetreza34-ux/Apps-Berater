# 07 – KI-API, Modelle, Kosten und Qualität

Dieses Kapitel behandelt, wie du KI-Modelle technisch sauber einbindest: Anbieterwahl, API-Nutzung, Fehlerbehandlung, Kostenkontrolle und Qualitätsmessung. Vertiefung: [KI-Produktionsleitfaden](../allgemeine-app-entwicklung/04-ki-agenten/ki-produktionsleitfaden.md).

## A. Anbieter und Modellwahl

- [ ] `PFLICHT` **KI-Aufrufe nur über einen Server.** Der Client spricht nie mit deinem eigenen KI-API-Schlüssel. Ausnahme sind nur Proxy-Dienste wie Firebase AI Logic – und dann nur mit App Check (dort Pflicht ab 2. November 2026), Anmeldung und Limits pro Nutzer.
- [ ] `KANN` **Einmal-Tokens für teure KI-Aufrufe.** Bei Firebase App Check Einmal-Tokens mit Schutz vor Wiederverwendung nutzen (`useLimitedUseAppCheckTokens`), damit abgefangene Tokens nicht erneut funktionieren. Debug-Tokens nie in Produktions-Builds.
- [ ] `PFLICHT` **Nutzungsrichtlinien des Anbieters prüfen:** verbotene Einsatzzwecke, Altersgrenzen, Pflichten bei Apps für Endkunden, Kennzeichnung.
- [ ] `PFLICHT` **Beratungs-Apps: Regeln der KI-Anbieter einhalten.** Anthropic verlangt ab 12. November 2026 bei persönlichen Empfehlungen zu Recht, Medizin (auch psychische Gesundheit), Geldanlage und Steuern, Kredit, Versicherung, Wohnen, Arbeit, Bildungsabschlüssen, Gesundheitsversorgung, Sozialleistungen und Aufenthaltsstatus, dass eine qualifizierte Fachperson vor der Ausgabe prüft und Betroffene vom KI-Einsatz erfahren; allgemeine Informationen und Wellness sind ausgenommen. OpenAI verbietet persönliche Beratung, die eine Zulassung erfordert, ohne Beteiligung einer zugelassenen Fachperson.
- [ ] `PFLICHT` **Kein privates KI-Abo als Backend.** Die App darf Claude nicht über ein Verbraucher-Abo (z. B. die Anmeldung eines Claude-Pro- oder Max-Kontos) ansprechen und keinen Claude-Zugang weiterverkaufen; nötig ist ein eigener API-Zugang (Anthropic Usage Policy ab 12. November 2026). Andere Anbieter haben ähnliche Regeln.
- [ ] `PFLICHT` **Apples Regeln für das KI-Modell auf dem Gerät** (wenn die App das Foundation Models Framework nutzt): keine Erotik-Chats, nichts, was schädliche Abhängigkeit fördert, keine Entscheidungen ohne menschliche Aufsicht in Arbeit, Medizin, Recht oder Finanzen, keine Umgehung der Schutzfilter, kein Entfernen von KI-Kennzeichnungen.
- [ ] `PFLICHT` **Gemini API für EU-Nutzer nur im bezahlten Tarif.** Laut den Gemini-API-Bedingungen dürfen Apps für Nutzer in der EU, der Schweiz und Großbritannien nur kostenpflichtige Dienste nutzen, nicht das Gratis-Kontingent. Außerdem darf die Gemini-API nicht in Apps eingesetzt werden, die sich an unter 18-Jährige richten oder wahrscheinlich von ihnen genutzt werden.
- [ ] `PFLICHT` **Keine Nutzerdaten in Gratis-Tarife von KI-Anbietern.** In kostenlosen Tarifen nutzen manche Anbieter Eingaben zum Training oder lassen sie von Menschen lesen (z. B. Gemini-Gratiskontingent außerhalb der EU, Mistral-Gratis-Tarif bis zum Widerspruch). Für echte Nutzerdaten nur Tarife ohne Training nutzen und die Einstellung dokumentieren.
- [ ] `SOLLTE` **Modell nach Aufgabe wählen.** Kleine, schnelle Modelle für Klassifizieren, Zusammenfassen, Extrahieren; große Modelle für komplexes Denken und Code. Nicht alles über das teuerste Modell schicken.
- [ ] `SOLLTE` **Modellversion festlegen** (Version mit Datum statt wechselndem Alias), damit sich das Verhalten nicht unbemerkt ändert.
- [ ] `SOLLTE` **Abkündigungsfristen kennen, keine Vorschau-Modelle in Produktion.** OpenAI kündigt allgemein verfügbare Modelle mindestens sechs Monate vorher ab, Spezialvarianten (z. B. Chat- oder Codex-Varianten) mindestens drei Monate, Vorschau-Modelle teils nur zwei Wochen vorher; Anthropic mindestens 60 Tage vorher. Aktuelle Termine stehen in [Quellen und Stand](./QUELLEN-UND-STAND.md). Termine eintragen und das Ersatzmodell vorher mit der Testsammlung prüfen.
- [ ] `SOLLTE` **Abgekündigte Plattform-Funktionen ersetzen.** OpenAI hat die Assistants API am 26. August 2026 abgeschaltet; Agent Builder, gespeicherte Prompts und die Evals-Plattform enden am 30. November 2026. Prompts und Agenten-Logik im eigenen Code halten.
- [ ] `SOLLTE` **Speicherpflichten einzelner Modelle beachten.** Manche Modelle verlangen eine Speicherung beim Anbieter, z. B. bei Anthropic die „Covered Models“ (Fable 5 und Mythos 5) 30 Tage; Zero Data Retention ist dann nicht möglich. Für Kinderdaten oder sehr sensible Daten ein passendes Modell wählen und die Speicherdauer in der Datenschutzerklärung nennen.
- [ ] `SOLLTE` **Abstraktionsschicht** zwischen App und Anbieter (eigener Adapter oder Bibliothek wie Vercel AI SDK oder LiteLLM), damit ein Wechsel ohne Umbau möglich ist.
- [ ] `SOLLTE` **Ersatzmodell oder Ersatzanbieter** für Ausfälle einplanen: [Runbook KI-Anbieter-Ausfall](../allgemeine-app-entwicklung/15-runbooks/ki-anbieter-ausfall.md).
- [ ] `SOLLTE` **Datenschutzoptionen des Anbieters nutzen:** EU-Datenresidenz, kein Training, kurze Aufbewahrung (siehe [02](./02-datenschutz-dsgvo.md)).
- [ ] `SOLLTE` **EU-Datenresidenz realistisch prüfen.** Nicht jeder Anbieter bietet sie direkt an: Die Claude-API verarbeitet „global“ oder „USA“ (EU-Regionen nur über AWS Bedrock oder Google Cloud), OpenAI gewährt EU-Datenresidenz (`eu.api.openai.com`) nur nach Freigabe und mit angepasster Aufbewahrung, für neuere Modelle mit 10 % Aufpreis. Die tatsächliche Wahl in Datenschutzerklärung und Verarbeitungsverzeichnis festhalten.
- [ ] `SOLLTE` **Limits deines Anbieter-Kontos kennen** (Anfragen und Tokens pro Minute, Nutzungsstufe) und vor dem Launch rechtzeitig erhöhen lassen.
- [ ] `SOLLTE` **Status-Seiten der Anbieter abonnieren,** damit du Störungen vor deinen Nutzern bemerkst.
- [ ] `KANN` **Offene Modelle selbst betreiben** für sehr sensible Daten oder zur Kostensenkung bei hohem Volumen – Aufwand für Betrieb und Sicherheit einrechnen.

## B. Prompts und Ausgaben

- [ ] `SOLLTE` **Prompts im Code versionieren** (eigene Dateien, z. B. `ai/prompts/`), nicht verstreut in Dashboards.
- [ ] `SOLLTE` **Klare Struktur im Prompt:** Rolle, Aufgabe, Regeln, Format, Beispiele. Nutzerinhalte getrennt markieren.
- [ ] `SOLLTE` **Strukturierte Ausgaben** (JSON-Schema oder Tool-Calling) statt Text zu parsen. Immer validieren.
- [ ] `SOLLTE` **Nur relevante Daten in den Kontext.** Weniger Kontext ist günstiger, schneller, genauer und sicherer.
- [ ] `SOLLTE` **Parameter nur setzen, wo das Modell sie erlaubt.** Neuere Modelle unterstützen `temperature`, `top_p` und `top_k` nicht mehr (Claude ab 4.7: Fehler 400; Gemini: abgekündigt seit Juli 2026). Das Verhalten dann über den Prompt steuern und KI-generierten Code darauf prüfen.
- [ ] `SOLLTE` **Sprache und Tonalität festlegen** (z. B. Deutsch, Du-Form), damit Antworten zur App passen.
- [ ] `SOLLTE` **Lange Chatverläufe kürzen oder zusammenfassen.** Sonst steigen Kosten mit jeder Nachricht, und die Qualität sinkt, wenn das Kontextfenster voll wird.

## C. Zuverlässigkeit

- [ ] `PFLICHT` **Timeouts setzen** für jeden KI-Aufruf.
- [ ] `PFLICHT` **Fehler abfangen:** Überlastung, Rate-Limit (429), Serverfehler (5xx), Inhaltsfilter, abgeschnittene Antworten. Nutzer bekommen eine verständliche Meldung statt eines weißen Bildschirms.
- [ ] `SOLLTE` **Wiederholungen mit wachsender Wartezeit** (exponentielles Backoff mit Zufallsanteil), aber begrenzt.
- [ ] `SOLLTE` **Streaming** bei längeren Antworten, damit Nutzer nicht warten.
- [ ] `SOLLTE` **Lange Aufgaben in eine Hintergrund-Warteschlange** (z. B. Video-, PDF- oder Massenverarbeitung). Serverless-Funktionen haben Zeitlimits.
- [ ] `SOLLTE` **Doppelte Ausführung verhindern** (Doppelklick, erneutes Senden): Idempotenz-Schlüssel, Button während der Anfrage sperren.
- [ ] `SOLLTE` **Batch-Schnittstellen nutzen** für Verarbeitung, die nicht sofort fertig sein muss – meist deutlich günstiger.

## D. Kostenkontrolle

- [ ] `PFLICHT` **Ausgabenlimit und Budget-Alarm beim KI-Anbieter einstellen.** Ohne Limit kann ein Fehler oder Angriff über Nacht sehr teuer werden. Bei der Gemini-API dafür die Ausgabenlimits pro Projekt nutzen (seit März 2026).
- [ ] `PFLICHT` **Kontingent pro Nutzer** (Anfragen oder Credits pro Tag/Monat), auch für zahlende Nutzer.
- [ ] `PFLICHT` **`max_tokens` und Eingabegrenzen** bei jedem Aufruf.
- [ ] `SOLLTE` **Verbrauch messen:** Tokens und Kosten pro Nutzer, Funktion und Tag speichern.
- [ ] `SOLLTE` **Preise durchrechnen:** Kosten bei 100, 1.000 und 10.000 aktiven Nutzern – inklusive Vielnutzer. Ein Abo muss auch für die teuersten 5 % der Nutzer tragfähig sein.
- [ ] `SOLLTE` **Prompt-Caching nutzen,** wenn lange, gleichbleibende Systemprompts oder Dokumente wiederholt gesendet werden.
- [ ] `SOLLTE` **Ergebnisse zwischenspeichern,** wo gleiche Anfragen häufig vorkommen und es datenschutzrechtlich passt.
- [ ] `SOLLTE` **Modell-Routing:** einfache Anfragen an günstige Modelle, schwierige an große.
- [ ] `KANN` **Energie sparen:** kleinere Modelle, Caching und kürzere Kontexte senken Kosten und Energieverbrauch.
- [ ] `SOLLTE` **Kosten für Bilder, Audio und Video** gesondert kalkulieren – sie sind oft viel teurer als Text.

## E. Qualität messen (Evals)

- [ ] `SOLLTE` **Testsammlung aufbauen:** 30–100 typische, schwierige und bösartige Eingaben mit erwarteten Ergebnissen oder Bewertungskriterien.
- [ ] `SOLLTE` **Vor jeder Änderung an Prompt, Modell oder RAG** die Testsammlung laufen lassen und mit vorher vergleichen.
- [ ] `SOLLTE` **Automatische Bewertung** (Regeln, Schema-Prüfung, KI als Bewerter) plus **menschliche Stichproben.**
- [ ] `SOLLTE` **Nutzerfeedback sammeln** (Daumen hoch/runter, optionaler Grund) und regelmäßig auswerten.
- [ ] `SOLLTE` **Tracing** jedes KI-Aufrufs (Prompt-Version, Modell, Tokens, Dauer, Ergebnis) mit maskierten personenbezogenen Daten.
- [ ] `SOLLTE` **Fairness prüfen:** Antworten für unterschiedliche Namen, Geschlechter, Herkünfte, Altersgruppen und Sprachniveaus vergleichen. Besonders wichtig, wenn die KI Menschen bewertet oder berät.
- [ ] `KANN` **Sensible Daten für Fairness-Tests nur unter strengen Bedingungen.** Der Digital Omnibus erlaubt ausnahmsweise, besondere Datenkategorien (z. B. Herkunft) zu verarbeiten, um Verzerrungen der KI zu erkennen und zu beheben (Art. 4a AI Act) – nur wenn wirklich nötig, mit Schutzmaßnahmen und Löschung danach.
- [ ] `SOLLTE` **Sprachen testen,** in denen die App angeboten wird (Deutsch, andere Sprachen, einfache Sprache, Umgangssprache, Tippfehler).
- [ ] `KANN` **A/B-Tests** für Prompt-Varianten mit echten Nutzern.
- [ ] `KANN` **Latenz-Budget festlegen** (z. B. erste Antwortzeichen nach höchstens 2 Sekunden) und messen.

## F. RAG (Wissensdatenbank)

- [ ] `SOLLTE` **Dokumente sinnvoll aufteilen** (Chunks nach Absätzen oder Überschriften, mit Überlappung und Metadaten wie Quelle und Seite).
- [ ] `SOLLTE` **Embedding-Modell festhalten.** Bei einem Wechsel müssen alle Dokumente neu eingebettet werden.
- [ ] `SOLLTE` **Hybride Suche** (Stichwort plus Vektor) und ggf. Re-Ranking für bessere Treffer.
- [ ] `SOLLTE` **Quellen in der Antwort anzeigen** mit Link zur Stelle.
- [ ] `PFLICHT` **Mandantentrennung und Löschung** umsetzen (siehe [06](./06-ki-sicherheit-llm-risiken.md)).
- [ ] `SOLLTE` **Veraltete Dokumente aktualisieren oder entfernen,** sonst antwortet die KI mit altem Wissen.
- [ ] `SOLLTE` **Herkunft, Datum und Lizenz jeder Quelle** speichern und Qualität der Quellen stichprobenartig prüfen.

## G. Agenten und Tool-Aufrufe

- [ ] `SOLLTE` **Tools klar beschreiben** (Name, Zweck, Parameter mit Typen und Beispielen).
- [ ] `SOLLTE` **Begrenzte Schritte pro Lauf** und klare Abbruchbedingungen.
- [ ] `PFLICHT` **Bestätigung vor irreversiblen Aktionen** (siehe [06](./06-ki-sicherheit-llm-risiken.md)).
- [ ] `SOLLTE` **Zwischenstände sichtbar machen** („Suche Termine …“, „Erstelle Entwurf …“).
- [ ] `SOLLTE` **Wiederaufnahme nach Fehlern** ermöglichen, statt alles neu zu starten.

## H. Sprache, Bild, Audio und Video

- [ ] `SOLLTE` **Spracherkennung und Sprachausgabe:** Latenz, Kosten pro Minute, Sprachen und Dialekte testen.
- [ ] `PFLICHT` **Generierte Medien kennzeichnen** (Metadaten, Wasserzeichen, siehe [01](./01-eu-ai-act.md)).
- [ ] `SOLLTE` **Große Dateien direkt in den Speicher hochladen** (signierte Upload-URL), nicht durch deine API-Funktion schleusen.
- [ ] `SOLLTE` **Ergebnisse asynchron liefern** (Job-Status, Benachrichtigung, wenn fertig).
- [ ] `SOLLTE` **Apple-Bildgenerierung prüfen** (wenn genutzt). Die Klasse `ImageCreator` aus Image Playground funktioniert ab iOS 27 nicht mehr – rechtzeitig umstellen.

## Typische Fehler beim Vibe-Coding

- Modell-Alias „latest“ – nach einem Update antwortet die App plötzlich anders.
- Keine Fehlerbehandlung: Bei Überlastung bleibt der Lade-Spinner ewig.
- Kein Budget-Limit, Gratis-Tarif ohne Kontingent.
- Prompt nur im Dashboard eines Tools, nicht im Repository.
- Keine Testsammlung, Qualität wird „nach Gefühl“ beurteilt.

## Nachweis

Modell- und Anbieterliste mit Version und Abkündigungsdatum, Budget-Limit-Screenshot, Kostenrechnung, Eval-Ergebnisse vor Release, Test von Timeout und Ausfall.
