# 15 – Sonderfälle nach App-Typ

Manche App-Ideen lösen zusätzliche Gesetze, Erlaubnispflichten oder Store-Regeln aus. Prüfe vor dem Start, ob deine App in eine dieser Gruppen fällt. Bei den meisten gilt: **fachliche Prüfung einholen**, bevor du veröffentlichst.

## A. Finanz-Apps (Budget, Investments, Krypto, Kredite)

- [ ] `PFLICHT` **Keine individuelle Anlageberatung ohne Erlaubnis.** Konkrete Kauf- oder Verkaufsempfehlungen für bestimmte Finanzinstrumente, zugeschnitten auf eine Person, können erlaubnispflichtig sein (KWG, WpIG, § 34f GewO). Allgemeine Informationen und Bildung sind in der Regel erlaubt.
- [ ] `PFLICHT` **Klarer Hinweis,** dass es sich nicht um Anlage-, Steuer- oder Rechtsberatung handelt – ein Hinweis allein macht erlaubnispflichtige Beratung aber nicht erlaubt.
- [ ] `PFLICHT` **Kreditwürdigkeit bewerten ist Hochrisiko-KI** nach AI Act (siehe [01](./01-eu-ai-act.md)).
- [ ] `PFLICHT` **Kontozugriff (Open Banking)** nur über einen lizenzierten Anbieter oder mit eigener BaFin-Registrierung als Kontoinformationsdienst.
- [ ] `PFLICHT` **Kundengelder, Guthaben-Wallets und Zahlungsabwicklung** zwischen Nutzern sind in der Regel erlaubnispflichtig (Zahlungsdiensteaufsichtsgesetz). Lieber einen lizenzierten Zahlungsdienstleister nutzen. Dazu kommen Pflichten nach dem Geldwäschegesetz (Identitätsprüfung).
- [ ] `PFLICHT` **Krypto-Dienste** (Verwahrung, Tausch, Handel) sind nach der EU-Verordnung MiCA erlaubnispflichtig. Apple führt Krypto-Börsen als stark regulierte Kategorie (5.1.1(ix)).
- [ ] `PFLICHT` **Kredit-Apps:** Apple lässt keine Kredite mit einem effektiven Jahreszins über 36 % oder einer vollständigen Rückzahlung innerhalb von 60 Tagen zu (3.2.2(ix)). Google Play hat eigene Regeln für Privatkredite.
- [ ] `PFLICHT` **Ratenkauf und „Jetzt kaufen, später zahlen“ nach neuem Kreditrecht.** Ab 20. November 2026 gelten auch Kredite unter 200 € und zinsfreie Zahlungsaufschübe von Dritten als Verbraucherkredite mit Prüf- und Informationspflichten. Wer Kredite gegen Provision vermittelt, braucht eine Erlaubnis nach § 34k GewO.
- [ ] `PFLICHT` **Keine Dark Patterns bei Finanzverträgen.** Wer Finanzdienstleistungen online an Verbraucher verkauft, darf seit 19. Juni 2026 keine Auswahl optisch bevorzugen, nicht nach einer Entscheidung erneut nachfragen und das Beenden nicht schwerer machen als den Abschluss (Art. 246b § 4 EGBGB). Verstöße gelten als irreführend und sind abmahnbar (§ 5 Abs. 6 UWG).
- [ ] `PFLICHT` **Menschlicher Ansprechpartner bei Finanz-Chatbots.** Wer Finanzdienstleistungen online über Chatbot oder automatische Beratung abschließt, muss Verbrauchern auf Wunsch einen echten Menschen zur Verfügung stellen (seit 19. Juni 2026, EU-Richtlinie 2023/2673). Die genaue deutsche Umsetzung prüfen lassen.
- [ ] `SOLLTE` **Zahlen und Berechnungen im Code,** nicht vom Sprachmodell. Kurse und Daten aus lizenzierten Quellen mit Zeitstempel.
- [ ] `SOLLTE` **Werbeaussagen vorsichtig:** keine Renditeversprechen.

## B. Gesundheit, Psyche, Fitness, Ernährung

- [ ] `PFLICHT` **Medizinprodukt prüfen.** Hat die App einen medizinischen Zweck (Diagnose, Behandlung, Überwachung von Krankheiten), ist sie wahrscheinlich ein Medizinprodukt nach MDR – mit Zertifizierung. Die KI darin kann dann Hochrisiko-KI sein (ab 2. August 2028).
- [ ] `PFLICHT` **Gesundheitsdaten sind besondere Kategorien** (Art. 9 DSGVO): ausdrückliche Einwilligung, hohe Sicherheit, meist DSFA.
- [ ] `PFLICHT` **Krisen erkennen:** Bei Hinweisen auf Suizidgedanken oder Notfälle Hilfsangebote anzeigen (z. B. Telefonseelsorge 0800 111 0 111 oder 0800 111 0 222, Notruf 112) statt normal weiterzuchatten.
- [ ] `PFLICHT` **Heilmittelwerberecht beachten:** keine Heilversprechen.
- [ ] `SOLLTE` **Klare Abgrenzung** „Wellness und Information, kein Ersatz für ärztliche Behandlung“ – in Zweckbestimmung, Texten und Werbung einheitlich.
- [ ] `KANN` **DiGA-Weg prüfen.** Sollen Krankenkassen die App erstatten, ist seit 1. Januar 2025 ein Datensicherheits-Zertifikat nach BSI TR-03161 nötig. Die Richtlinie ist auch ohne DiGA ein guter Maßstab für Gesundheits-Apps.

## C. Kinder und Jugendliche

- [ ] `PFLICHT` **Einwilligung der Eltern** unter 16 Jahren (DSGVO Art. 8).
- [ ] `PFLICHT` **Schutz Minderjähriger auf Plattformen** (Art. 28 DSA): sichere Voreinstellungen, keine Werbung auf Basis von Profiling bei Minderjährigen. Gilt für Online-Plattformen ab mittlerer Unternehmensgröße; Kleinst- und Kleinunternehmen sind nach Art. 19 DSA ausgenommen. Jugendschutz (JMStV, JuSchG), DSGVO und Store-Regeln gelten trotzdem.
- [ ] `PFLICHT` **Jugendschutz:** Altersfreigabe, Schutz vor ungeeigneten Inhalten, ggf. Altersprüfung.
- [ ] `PFLICHT` **Nutzungsbedingungen des KI-Anbieters** zu Minderjährigen prüfen (Mindestalter, zusätzliche Schutzmaßnahmen).
- [ ] `PFLICHT` **OpenAI: Kinderdaten nur mit Zero Data Retention.** OpenAI fordert, keine personenbezogenen Daten von Kindern unter 13 bzw. unter dem Alter der digitalen Einwilligung (in Deutschland 16) zu verarbeiten, ohne vorher „Zero Data Retention“ (keine Speicherung beim Anbieter) einzurichten; dazu Altersprüfung und Inhaltsfilter.
- [ ] `PFLICHT` **Anthropic: Regeln für Apps mit minderjährigen Nutzern.** Wer Claude Minderjährigen zugänglich macht, muss zusätzliche Schutzmaßnahmen umsetzen (z. B. Altersprüfung, Moderation, Überwachung) und offenlegen, dass eine KI antwortet. Anthropic prüft das und kann Konten sperren.
- [ ] `SOLLTE` **KI-Funktionen für Minderjährige standardmäßig aus.** Auf Plattformen, die auch Minderjährige nutzen, sind eingebaute KI-Chatbots nicht automatisch aktiv und werden nicht beworben. Sie weisen kindgerecht darauf hin, dass kein Mensch antwortet, und lassen sich abschalten (EU-Leitlinien zum Schutz Minderjähriger).
- [ ] `PFLICHT` **Store-Regeln für Kinder-Apps** (Apple Kids Category, Google Families Policy): keine Drittanbieter-Werbung und -Analytics ohne Freigabe, Elternschranke für Käufe und externe Links.
- [ ] `SOLLTE` **Alterssignale der Stores nutzen** (Apple Declared Age Range, Google Play Age Signals), statt selbst viele Daten zum Alter zu erheben.
- [ ] `SOLLTE` **Jugendschutz-Modus der Betriebssysteme vorbereiten.** Nach dem reformierten Jugendmedienschutz-Staatsvertrag bekommen verbreitete Betriebssysteme eine Jugendschutzfunktion, die bei eingestelltem Alter nur Apps mit passender, auslesbarer Altersstufe zulässt (Pflichten voraussichtlich ab Ende 2027). Altersfreigabe im Store korrekt pflegen; vom System gelieferte Altersdaten nur für den Jugendschutz nutzen und sofort löschen.
- [ ] `KANN` **Altersnachweis über EU-App oder EUDI-Wallet einplanen.** Die EU drängt die Mitgliedstaaten, eine App zur Altersüberprüfung bis Ende 2026 bereitzustellen; die deutsche digitale Brieftasche (EUDI-Wallet) soll Anfang 2027 starten. Damit lässt sich „über 18“ datensparsam nachweisen – Verfügbarkeit vor der Umsetzung prüfen.
- [ ] `SOLLTE` **EU-Leitlinien zum Schutz Minderjähriger** (Juli 2025) als Maßstab: geeignete Altersprüfung, sichere Voreinstellungen, kein süchtig machendes Design, Schutz vor Grooming und Mobbing.
- [ ] `PFLICHT` **Käufe von Minderjährigen:** Verträge ohne Zustimmung der Eltern können unwirksam sein (§§ 106 ff. BGB). Kaufsperren und Elternfreigaben einplanen.
- [ ] `PFLICHT` **Regeln kindgerecht erklären.** Nutzen vor allem Minderjährige deine App mit Nutzerinhalten, müssen Nutzungsbedingungen und Moderationsregeln für sie verständlich sein, z. B. als kurze Erklärung in einfacher Sprache (Art. 14 Abs. 3 DSA), auch für kleine Anbieter.
- [ ] `SOLLTE` **EU KIDS Act im Blick behalten.** Die EU-Kommission hat am 17. September 2026 vorgeschlagen, soziale Netzwerke erst ab 15 zu öffnen, Altersnachweise über zertifizierte Lösungen zu verlangen und KI-Chatbots und KI-Begleiter „safe by design“ zu gestalten (keine emotionale Abhängigkeit, Risikotest vor dem Start, keine Serien- und Lockbenachrichtigungen). Noch nicht beschlossen, Anwendung wohl nicht vor 2028; wer KI-Chats für junge Menschen plant, baut Altersprüfung und „aus für Minderjährige“ schon jetzt ein.
- [ ] `SOLLTE` **Strengere Moderation** und keine offenen Chats mit Fremden.

Beispiel mit vollständigem Weg: [KI-Lernassistent für Minderjährige](../app-master-anleitung/11-beispielwege/C-ki-lernassistent-minderjaehrige.md).

## D. Stimme, Gesicht und Biometrie (z. B. Sprach-Coach, Avatar-Apps)

- [ ] `PFLICHT` **Stimm- und Videoaufnahmen sind personenbezogene Daten.** Werden sie zur Identifizierung genutzt, sind es biometrische Daten (Art. 9 DSGVO).
- [ ] `PFLICHT` **Emotionserkennung:** am Arbeitsplatz und in Bildungseinrichtungen verboten; sonst Informationspflicht (AI Act Art. 50 Abs. 3) plus DSGVO.
- [ ] `PFLICHT` **Keine heimlichen Aufnahmen anderer Personen** (§ 201 StGB). Wenn Gespräche mit anderen aufgenommen werden, müssen alle zustimmen – die App muss darauf hinweisen.
- [ ] `PFLICHT` **Stimmklone und Avatare nur mit Einwilligung** der abgebildeten Person, mit Missbrauchsschutz.
- [ ] `SOLLTE` **Aufnahmen kurz speichern,** nach Auswertung löschen, Nutzer löschen lassen.
- [ ] `SOLLTE` **Verarbeitung auf dem Gerät** prüfen, wo möglich.

## E. Community, Chat und Nutzerinhalte

- [ ] `PFLICHT` **DSA-Pflichten** (Melden, Begründen, Beschwerde, siehe [03](./03-verbraucherrecht-und-weitere-gesetze.md)).
- [ ] `PFLICHT` **Melden, Blockieren, Moderieren** (Store-Regeln).
- [ ] `PFLICHT` **Umgang mit strafbaren Inhalten** festlegen (Entfernen, Beweissicherung, ggf. Meldung).
- [ ] `PFLICHT` **Anzeigen und Profile mit Personendaten vor Veröffentlichung prüfen** (Marktplätze, Kleinanzeigen, öffentliche Profile). Betreiber sind für die Daten in Nutzeranzeigen mitverantwortlich (EuGH, 2. Dezember 2025, C-492/23): sensible Angaben (z. B. Gesundheit, Sexualität) vorab erkennen, nur veröffentlichen, wenn der Nutzer selbst betroffen ist oder eine Einwilligung nachweist, und das Kopieren erschweren. Wie weit das für alle Nutzerinhalte gilt, ist umstritten.
- [ ] `SOLLTE` **Klare Community-Regeln** und abgestufte Maßnahmen (Warnung, Sperre).
- [ ] `PFLICHT` **Schutz vor Spam, Belästigung, Grooming und Identitätsmissbrauch** (Meldewege, Kontaktbeschränkungen, Erkennung verdächtiger Muster).
- [ ] `PFLICHT` **Private Nachrichten zwischen Nutzern schützen.** Solche Dienste können dem Fernmeldegeheimnis unterliegen (TDDDG). Inhalte nicht ohne Rechtsgrundlage mitlesen oder automatisch durch KI auswerten – vorher prüfen.

## F. KI-Begleiter und Beziehungs-Chatbots

- [ ] `PFLICHT` **Erotische oder pornografische KI-Inhalte nur hinter echter Altersprüfung.** Pornografische Texte, Bilder oder Chats dürfen in Deutschland nur in einer geschlossenen Benutzergruppe mit einem anerkannten Altersverifikationssystem angeboten werden (§ 4 Abs. 2 JMStV). Ein Klick auf „Ich bin 18“ reicht nicht; ohne echte Prüfung droht eine Strafanzeige (§ 184 StGB) – Erotik-Modus deshalb standardmäßig aus und ohne geprüftes Alter technisch nicht erreichbar. Unabhängig davon verbieten Anthropic und Apple (Foundation Models) erotische Chats ganz – vorher die Regeln des gewählten Modellanbieters prüfen.
- [ ] `PFLICHT` **Kein Ausnutzen von Einsamkeit oder Abhängigkeit** (AI-Act-Manipulationsverbot).
- [ ] `PFLICHT` **Minderjährige besonders schützen** (Altersprüfung, keine sexualisierten Inhalte).
- [ ] `SOLLTE` **Regelmäßig daran erinnern, dass es eine KI ist,** und Krisen erkennen. Bei Begleiter-, Gesundheits-, Finanz- und Rechts-Chats und bei Kindern halten die Leitlinien zu Art. 50 AI Act regelmäßige Erinnerungen in der Regel für nötig. Einige Länder und US-Bundesstaaten haben dafür eigene Gesetze – bei Angebot außerhalb der EU prüfen.
- [ ] `SOLLTE` **Pausenhinweise bei langen Sitzungen.** Begleiter- und Chat-Apps erinnern bei sehr langen Gesprächen freundlich an eine Pause und messen Erfolg nicht an der Nutzungsdauer.

## G. Bildung und Prüfungen

- [ ] `PFLICHT` **Hochrisiko im Bildungsbereich prüfen:** Zulassung, Bewertung von Lernergebnissen, Einstufung und Prüfungsaufsicht sind Anhang-III-Bereiche.
- [ ] `PFLICHT` **Keine Emotionserkennung** in Bildungseinrichtungen.
- [ ] `SOLLTE` **Bewertungen durch KI nur als Vorschlag,** mit Begründung und menschlicher Prüfung.

## H. Bewerbung, Personal und Arbeit

- [ ] `PFLICHT` **Hochrisiko im Personalbereich prüfen:** Lebenslauf-Filter, Bewerberranking, Leistungsbewertung und Kündigungsentscheidungen sind Anhang-III-Bereiche.
- [ ] `PFLICHT` **Diskriminierung vermeiden** (AGG): Ergebnisse auf Benachteiligung nach Geschlecht, Alter, Herkunft usw. prüfen.
- [ ] `PFLICHT` **Mitbestimmung:** Bei Tools, die Mitarbeitende überwachen können, hat der Betriebsrat mitzubestimmen.

## I. Rechts- und Steuerfragen

- [ ] `PFLICHT` **Rechtsdienstleistungsgesetz beachten.** Rechtliche Prüfung konkreter fremder Angelegenheiten ist erlaubnispflichtig. Allgemeine Informationen und standardisierte Vorlagen sind eher zulässig – im Einzelfall prüfen.
- [ ] `PFLICHT` **Keine Steuerberatung im Einzelfall** (Steuerberatungsgesetz).
- [ ] `SOLLTE` **Quellen und Stand** jeder Rechtsinformation anzeigen.

## J. Video, Clipping und Social-Media-Content

- [ ] `PFLICHT` **Fremde Videos nur mit Rechten** schneiden, bearbeiten und neu veröffentlichen. Das Zitatrecht ist eng. Eigene Inhalte, lizenzierte Inhalte oder ausdrückliche Erlaubnis der Urheber.
- [ ] `PFLICHT` **Musik in Clips lizenzieren** oder Plattform-Bibliotheken nutzen.
- [ ] `PFLICHT` **KI-Inhalte kennzeichnen** nach AI Act (Deepfakes) und nach Plattformregeln (siehe [13](./13-app-stores-plattformen.md)).
- [ ] `PFLICHT` **Plattform-Bedingungen** zu Download, automatischem Hochladen und API-Nutzung einhalten.
- [ ] `SOLLTE` **Qualität statt Masse,** sonst droht Ausschluss von der Monetarisierung.

## K. Agenten, die handeln (E-Mails, Käufe, Buchungen, Posts)

- [ ] `PFLICHT` **Bestätigung vor jeder Aktion mit Außenwirkung** (siehe [06](./06-ki-sicherheit-llm-risiken.md)).
- [ ] `PFLICHT` **Klare Haftungsregeln in den AGB** und Grenzen (Beträge, Empfänger, Häufigkeit).
- [ ] `SOLLTE` **Vollständiges Protokoll** und Rückgängig-Funktion.
- [ ] `SOLLTE` **Zugänge zu Drittkonten** (OAuth) mit minimalen Rechten und jederzeit widerrufbar.
- [ ] `PFLICHT` **Freigabeverfahren der Plattformen einplanen.** Wer z. B. mit Google-Schnittstellen auf Gmail- oder Drive-Inhalte zugreift, braucht für sensible bzw. eingeschränkte Berechtigungen eine Prüfung durch Google. Laufen eingeschränkte Daten (z. B. Gmail-Inhalte) über deinen Server, ist zusätzlich mindestens alle 12 Monate eine Sicherheitsbewertung durch eine anerkannte Prüfstelle nötig (CASA). Das kann Wochen dauern und Geld kosten; Microsoft verlangt für Firmenkunden oft eine verifizierte Herausgeber-Identität.
- [ ] `PFLICHT` **KI-Telefonie: Werbeanrufe nur mit Einwilligung.** Ruft ein KI-Sprachagent Verbraucher zu Werbezwecken an, braucht es vorher deren ausdrückliche Einwilligung (§ 7 Abs. 2 Nr. 1 UWG). Die Einwilligung musst du dokumentieren und fünf Jahre aufbewahren (§ 7a UWG); die Bundesnetzagentur verhängt Bußgelder bis 300.000 €. Die KI-Stimme muss sich als KI zu erkennen geben (AI Act Art. 50), und Gespräche dürfen nur mit Zustimmung aufgezeichnet werden (§ 201 StGB).

## L. Bildgeneratoren und Bildbearbeitung

- [ ] `PFLICHT` **Verbot von Nacktbildern realer Personen ohne Einwilligung und von Missbrauchsdarstellungen** technisch durchsetzen (siehe [01](./01-eu-ai-act.md)).
- [ ] `PFLICHT` **Maschinenlesbare Kennzeichnung** aller generierten Bilder.
- [ ] `SOLLTE` **Reale Personen, Marken und geschützte Figuren** standardmäßig filtern.

## M. Apps für Unternehmen (B2B)

- [ ] `PFLICHT` **Auftragsverarbeitungsvertrag anbieten** – du verarbeitest Daten im Auftrag deiner Kunden.
- [ ] `SOLLTE` **Sicherheitsunterlagen bereithalten:** TOMs, Liste der Unterauftragsverarbeiter, Datenstandorte, Backup- und Notfallkonzept.
- [ ] `SOLLTE` **AI-Act-Informationen für Kunden** (Einordnung, Transparenz, Grenzen), da sie Betreiber sind.
- [ ] `KANN` **Single Sign-on, Rollen, Audit-Logs, Datenexport** – typische Anforderungen von Firmenkunden.

## N. Apps mit tiefen Systemrechten (Bildschirmzeit, Blocker, VPN, Bedienungshilfen)

- [ ] `PFLICHT` **Besondere Store-Freigaben:** Unter iOS brauchen Bildschirmzeit-Funktionen eine eigene Berechtigung von Apple (Family Controls). Google Play erlaubt die Bedienungshilfen-Schnittstelle nur für bestimmte Zwecke mit Erklärung.
- [ ] `PFLICHT` **Klare Einwilligung und Erklärung,** welche Daten dabei gelesen werden.
- [ ] `SOLLTE` **Verarbeitung möglichst auf dem Gerät,** keine Übertragung von Bildschirminhalten an KI ohne ausdrückliche Zustimmung.

## O. Hardware, IoT und vernetzte Geräte

- [ ] `PFLICHT` **Cyber Resilience Act** voll anwendbar (siehe [03](./03-verbraucherrecht-und-weitere-gesetze.md)): sichere Grundeinstellungen, signierte Updates, Supportzeitraum, Schwachstellenprozess.
- [ ] `PFLICHT` **Funkanlagen mit Internetzugang:** Cybersicherheitsanforderungen der Funkanlagenrichtlinie gelten seit 1. August 2025.
- [ ] `PFLICHT` **Data Act für vernetzte Geräte und Begleit-Apps.** Seit 12. September 2025 vor Kauf oder Vertrag über Art, Menge und Speicherort der Gerätedaten und die Zugriffswege informieren; Geräte und zugehörige Dienste, die ab 12. September 2026 neu auf den Markt kommen, geben Nutzern die Daten standardmäßig, kostenlos und maschinenlesbar frei; für ältere Geräte gibt es einen Anspruch auf Herausgabe. Kleinst- und Kleinunternehmen sind von diesen Pflichten ausgenommen, wenn sie nicht zu einer größeren Gruppe gehören und nicht im Auftrag fertigen (Art. 7).
- [ ] `PFLICHT` **Physische Risiken bewerten:** Was passiert, wenn die KI oder die App falsch steuert (Heizung, Schloss, Fahrzeug, Maschine)? Ggf. Produktsicherheitsrecht und Hochrisiko nach Anhang I.
- [ ] `PFLICHT` **KI-gesteuerte Geräte mit Not-Aus** (wenn eine KI z. B. Schlösser, Heizung oder Fahrzeuge steuert): Eine Person kann jederzeit stoppen, bei Verbindungsabbruch geht das Gerät in einen sicheren Zustand, und Grenzwerte setzt das Gerät selbst durch, nicht die KI. Anthropic verlangt das ab 12. November 2026 ausdrücklich.
- [ ] `SOLLTE` **Funktion ohne Internet und ohne Cloud** für sicherheitsrelevante Grundfunktionen.
- [ ] `SOLLTE` **Plan für das Lebensende des Geräts** (Updates enden, Cloud wird abgeschaltet).

## P. Angebot außerhalb der EU

- [ ] `PFLICHT` **Lokales Recht der Zielländer prüfen,** sobald du dort aktiv Nutzer ansprichst.
- [ ] `PFLICHT` **USA:** Kinder unter 13 Jahren (COPPA), Datenschutzgesetze einzelner Bundesstaaten (z. B. Kalifornien), eigene KI-Gesetze einzelner Bundesstaaten, Altersprüfungsgesetze einzelner Bundesstaaten für App Stores, Werbe- und Verbraucherschutz (FTC).
- [ ] `PFLICHT` **Vereinigtes Königreich:** UK-DSGVO und Online Safety Act (vor allem bei Nutzerinhalten und Minderjährigen).
- [ ] `PFLICHT` **Schweiz:** revidiertes Datenschutzgesetz.
- [ ] `PFLICHT` **EU-Vertreter benennen, wenn du keinen Sitz in der EU hast.** Wer z. B. aus der Schweiz oder Großbritannien Nutzern in der EU eine App mit Nutzerkonten oder Nutzerinhalten anbietet, braucht einen schriftlich benannten Vertreter in der EU (Art. 27 DSGVO, Art. 13 DSA) und nennt ihn in Impressum und Datenschutzerklärung.
- [ ] `SOLLTE` **Verfügbarkeit der KI-Anbieter** in den Zielländern prüfen – nicht jedes Modell ist überall erlaubt oder verfügbar.
- [ ] `SOLLTE` **Steuern im Ausland** (Umsatzsteuer, Sales Tax) über einen Merchant of Record oder mit Steuerberatung lösen.

## Q. Glücksspiel, Wetten, Lootboxen, Alkohol, Tabak, Waffen

- [ ] `PFLICHT` **Glücksspiel und Wetten** nur mit Lizenz (Glücksspielstaatsvertrag) und nach Store-Regeln.
- [ ] `PFLICHT` **Lootboxen und zufällige Belohnungen gegen Geld:** Store-Pflicht zur Offenlegung der Wahrscheinlichkeiten, Jugendschutz beachten.
- [ ] `PFLICHT` **Alkohol, Tabak, Waffen, Arzneimittel:** Werbe- und Verkaufsbeschränkungen, Altersprüfung, Store-Regeln.

## R. Politik, Wahlen und öffentliche Meinung

- [ ] `PFLICHT` **KI zur Beeinflussung von Wahlen** oder Wahlverhalten ist ein Hochrisiko-Bereich nach Anhang III des AI Act.
- [ ] `PFLICHT` **Politische Werbung.** Seit 10. Oktober 2025 gilt die EU-Verordnung 2024/900: Politische Anzeigen müssen gekennzeichnet sein und eine Transparenzbekanntmachung haben (Auftraggeber, Kosten, Zielgruppenauswahl). Wer in der App Werbung zeigt, schließt politische Anzeigen am einfachsten ganz aus.
- [ ] `PFLICHT` **Deepfakes von Politikern** und KI-Texte zu Themen öffentlichen Interesses kennzeichnen (AI Act Art. 50).
- [ ] `SOLLTE` **Plattform-Regeln** zu politischen Inhalten und Anzeigen prüfen (viele Plattformen schränken sie stark ein).

## S. Spiele und spielerische Apps

- [ ] `PFLICHT` **Altersfreigabe ehrlich angeben** (Apple-Fragebogen, IARC bei Google). Käufe in der App, Lootboxen und Chats beeinflussen die Einstufung (Nutzungsrisiken nach dem Jugendschutzgesetz).
- [ ] `PFLICHT` **Alterskennzeichen bei Spielen, Filmen und Serien zeigen.** Seit 1. Juni 2026 bekommen eigene Spiele, Filme und Serien online eine Altersstufe (0, 6, 12, 16, 18), die ohne Klick oder Scrollen vor oder mit dem Start sichtbar ist (§ 5c Abs. 3 JMStV). Daneben die wichtigsten Gründe und Risiken nennen (z. B. „Chats“, „In-Game-Käufe“); Selbsteinstufung ist erlaubt, eine Ausnahme gibt es nur bei echter Altersverifikation.
- [ ] `PFLICHT` **Echte Preise zeigen.** Auch wenn mit einer virtuellen Währung bezahlt wird, muss der Preis in Euro erkennbar sein. So legen es die EU-Verbraucherschutzbehörden in ihren Grundsätzen zu virtuellen Währungen (März 2025) aus.
- [ ] `PFLICHT` **Keine direkten Kaufaufforderungen an Kinder** („Kauf dir jetzt …“). Das ist nach dem UWG immer unzulässig.
- [ ] `PFLICHT` **Keine versteckten Kosten und kein Zwang zum Kauf von Spielwährung,** z. B. durch Pakete, die nie genau zum Preis eines Artikels passen.
- [ ] `SOLLTE` **KI-Spielfiguren, mit denen frei gechattet wird,** wie einen offenen Chat behandeln: Moderation, Jugendschutz, Melden-Funktion.
- [ ] `SOLLTE` **Belohnungs- und Serienmechaniken fair gestalten** (siehe süchtig machendes Design in [03](./03-verbraucherrecht-und-weitere-gesetze.md)).

## T. Dating und Partnersuche

- [ ] `PFLICHT` **Sexuelle Orientierung und intime Angaben sind besondere Kategorien** (Art. 9 DSGVO): ausdrückliche Einwilligung, strenger Schutz, sparsam anzeigen.
- [ ] `PFLICHT` **Keine erfundenen oder KI-gesteuerten Profile,** die echte Menschen vortäuschen. Das ist irreführend, und ein Chat mit einer KI muss als KI erkennbar sein (AI Act Art. 50).
- [ ] `PFLICHT` **Dating-Apps bei Google Play für Minderjährige sperren.** Ist Dating der Kern der App, in der Play Console „Restrict Minor Access“ aktivieren; ist es nur eine Nebenfunktion, eine wirksame Altersschranke einbauen (ein Klick auf „Ich bin 18“ reicht nicht).
- [ ] `SOLLTE` **Profile verifizieren** und vor Fake-Profilen und Liebesbetrug warnen (Romance Scam).
- [ ] `SOLLTE` **Standort nur ungefähr anzeigen** und Nutzer entscheiden lassen, was sichtbar ist.
- [ ] `SOLLTE` **Sicherheitsfunktionen:** Melden, Blockieren, Hinweise für erste Treffen.

## U. Religion und Weltanschauung (z. B. Gebets-, Koran-, Bibel- oder Meditations-Apps)

- [ ] `PFLICHT` **Schon die Nutzung kann die Religion verraten.** Daten, aus denen sich die Religionszugehörigkeit ableiten lässt (z. B. Nutzung einer Gebets-App, Gebetszeiten, Fastenplan), sind besondere Kategorien nach Art. 9 DSGVO (EuGH, 1. August 2022, C-184/20, und 4. Oktober 2024, C-21/23). Du brauchst in der Regel eine ausdrückliche Einwilligung und erhebst nur, was die Funktion wirklich braucht.
- [ ] `PFLICHT` **Keine Werbe-, Tracking- oder Standortdaten-SDKs ohne ausdrückliche Einwilligung.** Jede Weitergabe verrät Dritten die Religion des Nutzers. 2020 wurde bekannt, dass Standortdaten aus einer großen Gebets-App über einen Datenhändler an Rüstungsfirmen und das US-Militär gingen – das Vertrauen war danach weg.
- [ ] `SOLLTE` **Standort für Gebetszeiten und Gebetsrichtung nur auf dem Gerät nutzen,** grob statt metergenau, alternativ Stadt manuell wählen lassen.
- [ ] `SOLLTE` **Gebetszeiten und Kalender im Code berechnen, nicht von der KI.** Die Berechnungsmethode (z. B. Winkel für Fajr und Isha, Rechtsschule für Asr) offenlegen und wählbar machen; Ergebnisse mit einer anerkannten Quelle vergleichen.
- [ ] `PFLICHT` **Keine erfundenen religiösen Zitate.** KI erfindet leicht Verse, Hadithe oder Bibelstellen. Zitate nur aus einer geprüften Textdatenbank mit genauer Fundstelle zeigen und KI-Zusammenfassungen davon klar trennen.
- [ ] `SOLLTE` **KI-Antworten sind keine verbindliche religiöse Auskunft.** Klar sagen, dass die KI kein Gelehrter ist und z. B. keine Fatwa erteilt, bei strittigen Fragen verschiedene Auffassungen nennen und auf Ansprechpartner der eigenen Gemeinde verweisen.
- [ ] `PFLICHT` **Rechte an Übersetzungen, Rezitationen und Kommentaren klären.** Alte heilige Texte sind gemeinfrei, moderne Übersetzungen, Kommentare, Audio-Rezitationen und aufbereitete Textdatenbanken sind aber meist geschützt (§§ 3, 85, 87a UrhG). Nur mit Lizenz oder freier Lizenz verwenden und die Quelle nennen.
- [ ] `SOLLTE` **Respektvolle Inhalte und Moderation.** KI-Ausgaben und Nutzerinhalte, die Religionen beschimpfen oder zu Hass aufrufen, filtern und melden lassen; das Beschimpfen von Bekenntnissen kann strafbar sein (§ 166 StGB), ebenso Volksverhetzung (§ 130 StGB).

## Nachweis

Kurzbewertung je zutreffendem Sonderfall mit Datum, Ergebnis einer fachlichen Prüfung (falls nötig), umgesetzte Schutzmaßnahmen.
