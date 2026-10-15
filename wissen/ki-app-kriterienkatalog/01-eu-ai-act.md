# 01 – EU AI Act (KI-Verordnung)

Die KI-Verordnung (EU) 2024/1689 regelt KI-Systeme nach Risiko. Sie wurde durch den **Digital Omnibus zu KI** (Verordnung (EU) 2026/1744, in Kraft seit 27. Juli 2026) geändert. Sie gilt auch für Anbieter außerhalb der EU, wenn die App in der EU angeboten wird oder ihre Ergebnisse in der EU genutzt werden.

**Kurz gesagt:** Die meisten KI-Apps (Chatbots, Schreibhilfen, Bildgeneratoren, Coaches) sind kein Hochrisiko. Für sie gelten vor allem **Verbote**, **KI-Kompetenz** und **Transparenzpflichten**. Hochrisiko betrifft Apps, die über Menschen entscheiden (Bewerbung, Kredit, Bildung, Behörden).

## Zeitplan

| Ab | Was gilt |
|---|---|
| 2. Februar 2025 | Verbotene Praktiken (Art. 5), KI-Kompetenz (Art. 4) |
| 2. August 2025 | Pflichten für Anbieter von KI-Modellen mit allgemeinem Verwendungszweck (GPAI), Aufsicht, Bußgelder |
| 2. August 2026 | Allgemeine Anwendbarkeit, Transparenzpflichten (Art. 50) |
| 2. Dezember 2026 | Neues Verbot von KI, die intime Darstellungen realer Personen ohne Einwilligung oder Missbrauchsdarstellungen von Kindern erzeugt; Kennzeichnungspflicht nach Art. 50 Abs. 2 für Systeme, die schon vor dem 2. August 2026 auf dem Markt waren |
| 2. Dezember 2027 | Hochrisiko-KI nach Anhang III (z. B. Bewerbung, Kredit, Bildung) |
| 2. August 2028 | Hochrisiko-KI in regulierten Produkten nach Anhang I (z. B. Medizinprodukte, Spielzeug, Maschinen) |

## A. Grundlagen und Rolle

- [ ] `PFLICHT` **Prüfen, ob überhaupt ein KI-System vorliegt.** Ein KI-System leitet aus Eingaben selbstständig Ausgaben wie Texte, Vorhersagen oder Entscheidungen ab. Feste Wenn-dann-Regeln sind kein KI-System. Jede App, die ein Sprachmodell nutzt, ist es praktisch immer.
- [ ] `PFLICHT` **Deine Rolle bestimmen.** *Anbieter* ist, wer ein KI-System unter eigenem Namen anbietet – auch wenn es auf GPT, Claude oder Gemini aufbaut. *Betreiber* ist, wer ein KI-System beruflich nutzt. Wer eine KI-App veröffentlicht, ist in der Regel Anbieter.
- [ ] `PFLICHT` **Jede KI-Funktion einzeln einordnen.** Ein Chat, ein Bildgenerator und eine automatische Bewertung können unterschiedliche Pflichten auslösen. Nutze dafür das [KI-Systemregister](../allgemeine-app-entwicklung/vorlagen/ki-systemregister.md).
- [ ] `PFLICHT` **Risikostufe je Funktion festlegen:** verboten, hochriskant, Transparenzpflicht oder minimales Risiko.
- [ ] `SOLLTE` **KI-Risikoregister führen:** je KI-Funktion möglicher Schaden, Wahrscheinlichkeit, Schutzmaßnahme und verantwortliche Person.
- [ ] `KANN` **KI-Managementsystem nach ISO/IEC 42001,** wenn Geschäftskunden einen Nachweis verlangen.
- [ ] `SOLLTE` **Einordnung schriftlich festhalten.** Datum, Funktion, Rolle, Risikostufe, Begründung. Bei einer Kontrolle ist das dein wichtigster Nachweis.
- [ ] `SOLLTE` **Fine-Tuning prüfen.** Prompting, RAG (Wissensdatenbank) und API-Nutzung machen dich nicht zum Modellanbieter. Erst wenn das Nachtrainieren mehr als ein Drittel der Rechenleistung des ursprünglichen Trainings braucht, wirst du nach den GPAI-Leitlinien (Juli 2025) in der Regel selbst Anbieter eines KI-Modells.
- [ ] `SOLLTE` **Neu einordnen bei jeder neuen KI-Funktion,** neuen Zielgruppe (z. B. Kinder) oder neuem Einsatzzweck.
- [ ] `SOLLTE` **Ausnahmen kennen:** rein private, nicht berufliche Nutzung; Forschung und Entwicklung vor dem Markteintritt; eingeschränkt kostenlose Open-Source-KI-Systeme. Die Open-Source-Ausnahme gilt nicht für verbotene Praktiken, Hochrisiko-Systeme und Transparenzpflichten.
- [ ] `SOLLTE` **KI-Compliance-Kompass und KI-Service-Desk der Bundesnetzagentur nutzen.** Der kostenlose Online-Kompass gibt eine erste Einschätzung, ob eine KI-Funktion verboten, hochriskant oder kennzeichnungspflichtig ist; der Service-Desk beantwortet Fragen kleiner Unternehmen. Das Ergebnis ist unverbindlich, aber ein guter Start für die Dokumentation.
- [ ] `SOLLTE` **Leitlinien zur KI-System-Definition und zu verbotenen Praktiken lesen.** Die beiden Leitlinien der EU-Kommission vom Februar 2025 erklären mit Beispielen, wann Software als KI-System gilt und wo verbotene Manipulation oder Emotionserkennung beginnt. Sie sind nicht verbindlich, Behörden richten sich aber danach.
- [ ] `SOLLTE` **Modell-Dokumentation des KI-Anbieters nutzen.** Anbieter von KI-Modellen müssen dir als App-Anbieter Informationen zu Fähigkeiten, Grenzen und Einsatz geben (AI Act Art. 53, Anhang XII). Diese Unterlagen herunterladen oder anfordern und zu deiner Einordnung legen.

## B. Verbotene KI-Praktiken (Art. 5)

Diese Funktionen darfst du nicht bauen oder anbieten. Die Verbote gelten seit 2. Februar 2025.

- [ ] `PFLICHT` **Keine unterschwellige oder täuschende Manipulation,** die Menschen zu schädlichen Entscheidungen bringt (z. B. KI, die gezielt psychologische Schwächen ausnutzt, um Käufe zu erzwingen).
- [ ] `PFLICHT` **Keine Ausnutzung von Schwächen** wegen Alter, Behinderung oder sozialer oder wirtschaftlicher Lage.
- [ ] `PFLICHT` **Kein Social Scoring.** Keine Bewertung von Menschen nach Sozialverhalten oder Persönlichkeit, die zu Benachteiligung in anderen Lebensbereichen führt.
- [ ] `PFLICHT` **Keine Vorhersage von Straftaten** allein auf Basis von Profiling oder Persönlichkeitsmerkmalen.
- [ ] `PFLICHT` **Kein ungezieltes Sammeln von Gesichtsbildern** aus dem Internet oder von Kameras für Gesichtserkennungs-Datenbanken.
- [ ] `PFLICHT` **Keine Emotionserkennung am Arbeitsplatz und in Bildungseinrichtungen** (Ausnahme: medizinische oder Sicherheitsgründe). Wichtig für Coaching-, Lern- und HR-Apps.
- [ ] `PFLICHT` **Keine biometrische Kategorisierung** nach Herkunft, politischer Meinung, Religion, Gewerkschaft oder sexueller Orientierung.
- [ ] `PFLICHT` **Keine biometrische Echtzeit-Fernidentifizierung** im öffentlichen Raum für Strafverfolgung (nur enge Ausnahmen für Behörden).
- [ ] `PFLICHT` **Keine intimen Darstellungen realer Personen ohne Einwilligung und keine Missbrauchsdarstellungen von Kindern** (Verbot gilt ab 2. Dezember 2026). Es trifft dich als Anbieter schon dann, wenn solche Inhalte mit deiner App vorhersehbar und ohne großen technischen Aufwand erzeugt werden können. Bild-, Video- und Audio-Generatoren brauchen Ablehnungsregeln, Filter für Ein- und Ausgaben und Missbrauchserkennung; Verstöße fallen in die höchste Bußgeldstufe. Gemeldete Missbrauchsfälle musst du schnell abstellen; eine Übergangsfrist für Apps, die schon vorher auf dem Markt waren, gibt es nicht.
- [ ] `SOLLTE` **Grenzfälle dokumentieren.** Beispiel: Ein Sprach-Coach, der „Unsicherheit in der Stimme“ erkennt, ist Emotionserkennung. Im Schul- oder Firmeneinsatz wäre das verboten, privat gilt die Informationspflicht (siehe D).

## C. KI-Kompetenz (Art. 4)

- [ ] `PFLICHT` **Maßnahmen zur KI-Kompetenz ergreifen.** Seit dem Omnibus musst du die KI-Kompetenz von dir, deinem Team und Helfern *fördern* (Bemühungspflicht); ein bestimmtes Niveau musst du nicht garantieren. Das KI-MIG sieht dafür kein eigenes Bußgeld vor, fehlende Schulung kann bei einem Schaden aber als Fahrlässigkeit gelten.
- [ ] `SOLLTE` **Kurz dokumentieren,** wie das passiert: z. B. Schulung, interne KI-Richtlinie, Wissen über Grenzen und Risiken der genutzten Modelle.
- [ ] `SOLLTE` **Interne KI-Richtlinie** schreiben: Welche KI-Tools dürfen genutzt werden, welche Daten dürfen hinein, wer prüft Ergebnisse.

## D. Transparenzpflichten (Art. 50)

Gelten seit **2. August 2026**. Die Information muss spätestens bei der ersten Interaktion klar, erkennbar und barrierefrei erfolgen.

- [ ] `PFLICHT` **Chatbots und Sprachassistenten als KI kennzeichnen** (Anbieter, Abs. 1). Menschen müssen wissen, dass sie mit einer KI sprechen. Die Ausnahme „offensichtlich“ gilt laut Leitlinien fast nie, sobald die App für die Allgemeinheit offen ist (auch Kinder und Ältere); für Kinder den Hinweis kindgerecht und barrierefrei formulieren. Beispiel: Hinweis im Chatfenster „Du schreibst mit einer KI“. Bei Voicebots zu Beginn des Gesprächs ansagen.
- [ ] `PFLICHT` **KI-Hinweis im Gespräch selbst, nicht nur in AGB.** Der Hinweis steht sichtbar im Chat (z. B. am Eingabefeld) und kommt spätestens zu Beginn jeder Sitzung; Wörter wie „Assistent“ oder „nutzt LLMs“ reichen nicht, ein Hinweis nur in AGB oder Datenschutzerklärung auch nicht. Fragt jemand, ob er mit einer KI spricht, antwortet die App immer ehrlich (Leitlinien zu Art. 50, Juli 2026).
- [ ] `PFLICHT` **KI-Agenten geben sich als KI zu erkennen.** Schreibt, bucht oder verhandelt ein Agent mit Menschen, sagt er bei jeder neuen Interaktion und an wichtigen Schritten, dass er eine KI ist und in wessen Auftrag er handelt (Art. 50 Abs. 1, Leitlinien Juli 2026). Beispiel: KI-Hinweis oben in jeder E-Mail, die der Agent verschickt.
- [ ] `PFLICHT` **Generierte Inhalte maschinenlesbar kennzeichnen** (Anbieter generativer Systeme, Abs. 2). Gilt für synthetische Bilder, Videos, Audios und Texte. Technisch z. B. über Metadaten (C2PA/Content Credentials) und Wasserzeichen. Ausnahme: reine Bearbeitungshilfe, die den Inhalt nicht wesentlich verändert (z. B. Rechtschreibkorrektur). Für Systeme, die schon vor dem 2. August 2026 auf dem Markt waren, gilt die Frist 2. Dezember 2026.
- [ ] `PFLICHT` **Deepfakes offenlegen** (Betreiber, Abs. 4). Wer realistisch wirkende Bilder, Videos oder Audios von echten Personen, Orten oder Ereignissen erzeugt und veröffentlicht, muss sichtbar darauf hinweisen. Bei klar künstlerischen oder satirischen Werken reicht ein zurückhaltender Hinweis.
- [ ] `PFLICHT` **KI-Texte zu Themen von öffentlichem Interesse offenlegen** (Betreiber, Abs. 4). Ausnahme: Ein Mensch hat den Text redaktionell geprüft und trägt die Verantwortung.
- [ ] `PFLICHT` **Über Emotionserkennung und biometrische Kategorisierung informieren** (Betreiber, Abs. 3). Zusätzlich gilt die DSGVO.
- [ ] `SOLLTE` **Leitlinien (20. Juli 2026) und Verhaltenskodex (10. Juni 2026) zu Art. 50 umsetzen.** Die Kommission hat den Kodex als geeignetes Mittel bestätigt. Er beschreibt Markierungstechniken (Bilder, Audio und Video: digital signierte Metadaten wie C2PA **und** ein unsichtbares Wasserzeichen; freier Text ab 200 Tokens: Wasserzeichen; Fingerprinting oder Protokolle allein reichen nicht; das Entfernen von Markierungen in den Nutzungsbedingungen verbieten) und drei EU-Symbole für die sichtbare Kennzeichnung. Auch wenn du nur ein fremdes Modell per API nutzt, bist du als App-Anbieter für Hinweis und Markierung verantwortlich und darfst Wasserzeichen des Modells nicht entfernen.
- [ ] `SOLLTE` **Abmahnrisiko bei fehlender KI-Kennzeichnung ernst nehmen.** Fehlende KI-Hinweise oder Deepfake-Kennzeichnungen können nach verbreiteter Meinung auch von Wettbewerbern und Verbänden abgemahnt werden (Verstoß gegen eine Marktverhaltensregel, § 3a UWG). Gerichtlich geklärt ist das noch nicht; die Kennzeichnung deshalb gut sichtbar umsetzen und mit Screenshot belegen.
- [ ] `SOLLTE` **Kennzeichnung auch beim Export erhalten.** Metadaten dürfen beim Download, Teilen oder Komprimieren nicht verloren gehen – testen.
- [ ] `KANN` **EU-Symbol für KI-Inhalte nutzen.** Die drei kostenlosen EU-Symbole (allgemein, vollständig KI-erzeugt, teilweise KI-verändert) gut sichtbar einsetzen, mit Alt-Text oder ARIA-Label für Screenreader. Sie sind freiwillig; die Kennzeichnungspflicht selbst bleibt.
- [ ] `KANN` **Sichtbares Label „KI-generiert“** auch dort, wo es nicht Pflicht ist. Das schafft Vertrauen und passt zu Plattformregeln (siehe [13](./13-app-stores-plattformen.md)).

## E. Hochrisiko-KI prüfen (Art. 6, Anhang III)

Die Pflichten für Anhang III gelten nach dem Omnibus ab **2. Dezember 2027**. Die Einordnung solltest du trotzdem jetzt machen, weil sie Produkt und Architektur bestimmt.

- [ ] `PFLICHT` **Prüfen, ob deine App in einen Hochrisiko-Bereich fällt:**
  - Biometrie (Fernidentifizierung, Kategorisierung, Emotionserkennung);
  - kritische Infrastruktur;
  - Bildung (Zulassung, Bewertung von Lernergebnissen, Niveau-Einstufung, Prüfungsaufsicht);
  - Beschäftigung (Bewerberauswahl, Lebenslauf-Filter, Beförderung, Kündigung, Leistungsüberwachung);
  - wichtige Dienstleistungen (Kreditwürdigkeit, Preise für Lebens- und Krankenversicherungen, Sozialleistungen, Notruf-Priorisierung);
  - Strafverfolgung, Migration, Justiz, Wahlen.
- [ ] `PFLICHT` **Regulierte Produkte prüfen (Anhang I).** Ist die App z. B. ein Medizinprodukt, kann die KI darin Hochrisiko sein (ab 2. August 2028).
- [ ] `PFLICHT` **Ausnahme nach Art. 6 Abs. 3 dokumentieren und registrieren.** Fällt eine Funktion in einen Anhang-III-Bereich und stufst du sie trotzdem als nicht hochriskant ein (z. B. weil sie nur eine enge Verfahrensaufgabe erledigt, ein fertiges menschliches Ergebnis verbessert, nur Muster erkennt oder nur vorbereitet), musst du die Begründung vor dem Markteintritt festhalten und das System in der EU-Datenbank registrieren (Art. 6 Abs. 4, Art. 49 Abs. 2; laut Digital Omnibus mit vereinfachten Angaben; ab 2. Dezember 2027 – Datum vor dem Markteintritt nochmals prüfen). **Profiling von Personen ist immer hochriskant.**
- [ ] `SOLLTE` **Leitlinien zur Hochrisiko-Einstufung nutzen.** Die Kommission hat am 19. Mai 2026 einen Entwurf mit Praxisbeispielen veröffentlicht; die Endfassung wird bis Ende 2026 erwartet. Die eigene Einordnung danach erneut prüfen.
- [ ] `SOLLTE` **Funktionen so schneiden, dass die KI nicht über Menschen entscheidet,** wenn du kein Hochrisiko-Anbieter werden willst. Ob das reicht, im Einzelfall prüfen lassen.
- [ ] `PFLICHT` **Wenn Hochrisiko: Pflichtenpaket einplanen.** Risikomanagement, Datenqualität, technische Dokumentation, automatische Protokolle, Gebrauchsanweisung, menschliche Aufsicht, Genauigkeit und Cybersicherheit, Qualitätsmanagement, Konformitätsbewertung, CE-Kennzeichnung, Registrierung in der EU-Datenbank, Überwachung nach dem Markteintritt, Meldung schwerer Vorfälle. Ohne Fachberatung nicht umsetzen.
- [ ] `PFLICHT` **Wenn du Hochrisiko-KI anderer nutzt (Betreiber):** Gebrauchsanweisung befolgen, kompetente menschliche Aufsicht, Protokolle mindestens sechs Monate aufbewahren, Beschäftigte informieren, Betroffene über KI-gestützte Entscheidungen informieren. Öffentliche Stellen und Betreiber im Kredit- und Versicherungsbereich müssen zusätzlich eine Grundrechte-Folgenabschätzung durchführen (Art. 27).
- [ ] `PFLICHT` **Recht auf Erklärung beachten** (Art. 86): Wer von einer Entscheidung auf Basis von Hochrisiko-KI betroffen ist, kann eine Erklärung verlangen.
- [ ] `PFLICHT` **Aufpassen, nicht ungewollt Hochrisiko-Anbieter zu werden** (Art. 25). Das passiert, wenn du ein fremdes Hochrisiko-System unter deinem Namen anbietest, es wesentlich veränderst oder den Zweck eines normalen KI-Systems so änderst, dass es hochriskant wird – z. B. wenn ein allgemeiner Chatbot als Bewerber-Filter vermarktet wird.
- [ ] `KANN` **Normen für Hochrisiko-KI beobachten.** Nur wenn du Hochrisiko-KI anbietest: Die europäische Norm EN 18286 (Qualitätsmanagement) ist erschienen; erst wenn sie im EU-Amtsblatt steht, gilt bei Einhaltung die Vermutung, dass die Pflicht erfüllt ist.
- [ ] `KANN` **KI-Reallabore nutzen.** Jeder EU-Staat muss bis 2. August 2027 mindestens ein KI-Reallabor betreiben, in Deutschland die Bundesnetzagentur (ein Pilot läuft); dazu kommt eines auf EU-Ebene. Dort kannst du eine KI-Funktion mit Begleitung der Behörde testen; KMU und Start-ups sollen bevorzugt teilnehmen.
- [ ] `KANN` **Erleichterungen für KMU nutzen.** Der Omnibus vereinfacht Dokumentationspflichten für kleine und mittlere Unternehmen und kleine Mid-Caps.

## F. Eigene KI-Modelle (GPAI)

Nur relevant, wenn du selbst ein Modell trainierst oder stark veränderst und weitergibst.

- [ ] `PFLICHT` **Technische Dokumentation** des Modells für nachgelagerte Anbieter.
- [ ] `PFLICHT` **Urheberrechts-Strategie,** inklusive Beachtung maschinenlesbarer Nutzungsvorbehalte (Opt-out) beim Training.
- [ ] `PFLICHT` **Zusammenfassung der Trainingsdaten** nach der Vorlage der EU-Kommission veröffentlichen.
- [ ] `SOLLTE` **Verhaltenskodex für GPAI (Code of Practice)** prüfen und ggf. unterzeichnen.

## G. Aufsicht und Strafen

- [ ] `SOLLTE` **Bußgeldrahmen kennen:** bis 35 Mio. € oder 7 % des weltweiten Jahresumsatzes bei verbotenen Praktiken; bis 15 Mio. € oder 3 % bei anderen Pflichten (z. B. Art. 50); bis 7,5 Mio. € oder 1 % bei falschen Angaben. Für KMU und Start-ups – seit dem Omnibus auch für kleine Mid-Caps – gilt jeweils der niedrigere Betrag.
- [ ] `SOLLTE` **Zuständige Stelle kennen.** In Deutschland ist die Bundesnetzagentur seit 29. Juli 2026 Marktüberwachungsbehörde, zentrale Anlaufstelle und Beschwerdestelle für den AI Act (KI-MIG); für KI in Finanzunternehmen ist die BaFin zuständig, für journalistische Medien sind es Landesbehörden. Jeder kann sich dort über deine App beschweren, und das KI-MIG ergänzt die EU-Bußgelder um eigene Bußgelder bis 50.000 € (§ 15 KI-MIG), vor allem bei Mitwirkungspflichten gegenüber Behörden und bei Hochrisiko-Pflichten.
- [ ] `SOLLTE` **Anfragen von Geschäftskunden vorbereiten.** Firmen, die deine App nutzen, sind Betreiber und fragen nach Einordnung, Transparenz und Dokumentation.

## Typische Fehler beim Vibe-Coding

- Chat-Oberfläche ohne KI-Hinweis, weil das UI-Template keinen vorsieht.
- Bild-Export entfernt Metadaten und damit die Kennzeichnung.
- „Stimmungsanalyse“ oder „Motivations-Score“ für Mitarbeitende oder Schüler eingebaut – das ist verbotene Emotionserkennung.
- Automatische Vorauswahl von Bewerbern „nur als Hilfe“ – das ist in der Regel Hochrisiko.
- Einordnung nur im Kopf, nicht dokumentiert.

## Nachweis

KI-Systemregister mit Rolle und Risikostufe je Funktion, Screenshot des KI-Hinweises, Test der Metadaten-Kennzeichnung, Notiz zur KI-Kompetenz.
