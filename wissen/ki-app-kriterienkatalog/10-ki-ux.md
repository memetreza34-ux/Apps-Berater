# 10 – KI-UX

KI verhält sich anders als normale Software: Sie ist langsam, manchmal falsch, nicht immer gleich und schwer vorhersehbar. Gute KI-UX macht das sichtbar und gibt Nutzern Kontrolle. Schlechte KI-UX versteckt es – dann verlieren Nutzer Vertrauen.

## A. Erwartungen setzen

- [ ] `PFLICHT` **KI klar als KI erkennbar.** Keine Täuschung, dass ein Mensch antwortet. Eindeutig formulieren („Du chattest mit einem KI-Assistenten“), nicht nur „KI-gestützt“ oder „AI“, und den Hinweis auch für Screenreader lesbar machen (AI Act Art. 50 Abs. 1 und 5, siehe [01](./01-eu-ai-act.md)).
- [ ] `SOLLTE` **Zeigen, was die KI kann und was nicht,** im Onboarding und im leeren Zustand.
- [ ] `SOLLTE` **Beispiel-Eingaben** als anklickbare Vorschläge statt leeres Eingabefeld.
- [ ] `SOLLTE` **Hinweise zu Uploads:** erlaubte Formate, maximale Größe, was mit der Datei passiert.
- [ ] `SOLLTE` **Keine übertriebenen Versprechen** („perfekte Antworten“, „ersetzt Experten“).

## B. Warten und Fortschritt

- [ ] `SOLLTE` **Antworten streamen,** damit sofort etwas passiert.
- [ ] `SOLLTE` **Fortschritt benennen** bei längeren Schritten („Lese Dokument …“, „Suche Quellen …“, „Erstelle Bild …“).
- [ ] `SOLLTE` **Abbrechen-Button** während der Generierung.
- [ ] `SOLLTE` **Hintergrundverarbeitung mit Benachrichtigung** bei Aufgaben über etwa 30 Sekunden.
- [ ] `SOLLTE` **Eingaben nicht verlieren,** wenn ein Fehler auftritt (Text bleibt im Feld).

## C. Kontrolle für Nutzer

- [ ] `SOLLTE` **Ergebnisse bearbeiten** statt nur annehmen oder ablehnen.
- [ ] `SOLLTE` **Neu generieren** und ggf. Varianten vergleichen.
- [ ] `SOLLTE` **Rückgängig** für Änderungen, die die KI vorgenommen hat.
- [ ] `PFLICHT` **Vorschau und Bestätigung vor Aktionen mit Wirkung** (E-Mail senden, veröffentlichen, kaufen, löschen).
- [ ] `SOLLTE` **Personalisierung und Gedächtnis sichtbar und abschaltbar.**
- [ ] `SOLLTE` **KI nicht aufdrängen.** Ungefragte KI-Vorschläge erscheinen nur passend zur aktuellen Aufgabe, lassen sich mit einem Tipp verwerfen und ganz abschalten (Apple-Richtlinien zu generativer KI, Juni 2026).
- [ ] `SOLLTE` **Nachfragen statt raten.** Bei unklaren Eingaben stellt die KI eine kurze Rückfrage, statt etwas zu erfinden. Merkmale wie Geschlecht, Herkunft oder Alter fragt sie ab, statt sie aus Namen oder Fotos abzuleiten.
- [ ] `KANN` **Modell- oder Qualitätswahl** für erfahrene Nutzer (schnell vs. gründlich).

## D. Vertrauen und Ehrlichkeit

- [ ] `SOLLTE` **Quellen anzeigen** mit Link zur genauen Stelle.
- [ ] `SOLLTE` **Unsicherheit kommunizieren.** Die KI darf sagen, dass sie etwas nicht weiß.
- [ ] `SOLLTE` **Blindes Vertrauen vermeiden** (Automation Bias): bei wichtigen Ergebnissen zur eigenen Prüfung anregen und Unsicherheit sichtbar machen, statt alles gleich sicher klingen zu lassen.
- [ ] `SOLLTE` **Erklären, wie ein Ergebnis zustande kam** (Quellen, Kriterien, verwendete Daten), wo das für Nutzer wichtig ist.
- [ ] `SOLLTE` **Keine Schmeichel-KI.** Die KI widerspricht, wenn etwas falsch oder riskant ist, statt Nutzern nach dem Mund zu reden – besonders bei Gesundheit, Geld und psychischen Themen. Daumen-hoch-Feedback nicht ungeprüft zum Optimieren nutzen, denn es belohnt Zustimmung statt Richtigkeit.
- [ ] `SOLLTE` **Änderungen am KI-Verhalten mitteilen.** Ändern sich Antworten spürbar, weil Modell, Prompt oder Gedächtnis geändert wurden, Nutzer kurz informieren (z. B. unter „Was ist neu“) und vorher mit Evals prüfen (siehe [07](./07-ki-api-modelle-kosten-qualitaet.md)).
- [ ] `SOLLTE` **Hinweis zur Prüfung** bei wichtigen Themen („Bitte prüfe diese Angaben, bevor du sie verwendest.“).
- [ ] `PFLICHT` **Keine emotionale Manipulation,** um Nutzer zu binden oder zum Kauf zu drängen (z. B. KI-Figur, die traurig ist, wenn man gehen will). Das kann gegen das Manipulationsverbot des AI Act und das Lauterkeitsrecht verstoßen.
- [ ] `SOLLTE` **Keine übertriebene Vermenschlichung,** besonders bei jungen oder verletzlichen Nutzern.
- [ ] `SOLLTE` **Weg zu einem Menschen** anbieten (Support), wenn die KI nicht weiterhilft.

## E. Fehler und Grenzen

- [ ] `PFLICHT` **Verständliche Fehlermeldungen mit nächstem Schritt.** Beispiel: „Der KI-Dienst ist gerade überlastet. Versuch es in einer Minute erneut.“ plus Button „Erneut versuchen“.
- [ ] `SOLLTE` **Ablehnungen erklären,** wenn Inhalte blockiert werden (ohne die Filterregeln im Detail offenzulegen).
- [ ] `SOLLTE` **Limit erreicht** freundlich erklären, mit Zeitpunkt der Erneuerung oder Upgrade-Option.
- [ ] `SOLLTE` **Abgeschnittene Antworten** erkennen und „Weiter“ anbieten.
- [ ] `SOLLTE` **Weg ohne KI anbieten.** Wo möglich, lässt sich die Kernaufgabe auch ohne KI erledigen (manuelle Eingabe, Vorlage, Suche), etwa wenn der KI-Dienst ausfällt oder Nutzer der KI nicht vertrauen.

## F. Kosten transparent machen

- [ ] `SOLLTE` **Verbrauch vor der Aktion anzeigen,** wenn eine Aktion mehrere Credits kostet („Diese Videoanalyse kostet 5 Credits“).
- [ ] `SOLLTE` **Restguthaben sichtbar,** nicht erst beim Fehler.
- [ ] `SOLLTE` **Keine Überraschungskosten** durch automatische Aktionen.
- [ ] `SOLLTE` **Credits fair verkaufen.** Den Preis immer auch in Euro zeigen, Paketgrößen passend zu den Kosten der Aktionen wählen (keine erzwungenen Restbeträge) und nicht mehrere Guthabenarten mischen. Die EU-Verbraucherbehörden haben solche Regeln 2025 für Spielwährungen aufgestellt; sie lassen sich auf Credits übertragen.

## G. Feedback

- [ ] `SOLLTE` **Daumen hoch/runter** mit optionalem Grund (falsch, unvollständig, unangemessen, zu lang).
- [ ] `SOLLTE` **Melden** bei schädlichen Inhalten.
- [ ] `SOLLTE` **Feedback sichtbar wirken lassen** („Danke, wir nutzen das, um Antworten zu verbessern.“) – aber nur, wenn das stimmt.

## H. Darstellung von Antworten

- [ ] `SOLLTE` **Länge und Format passend zum Gerät.** Auf dem Handy kurze Absätze, keine riesigen Tabellen.
- [ ] `SOLLTE` **Markdown sauber und sicher rendern** (Überschriften, Listen, Code mit Kopier-Button).
- [ ] `SOLLTE` **Kopieren, Teilen, Exportieren** der Ergebnisse.
- [ ] `SOLLTE` **Barrierefreier KI-Chat.** Während des Streamings nur „Antwort wird erstellt“ ansagen und die fertige Antwort einmal vorlesen lassen (kein `aria-atomic` auf dem Antwortbereich). Der Fokus bleibt nach dem Senden im Eingabefeld, Stoppen geht per Tastatur, und Antworten in anderer Sprache bekommen das passende `lang`-Attribut.

## I. Sprach- und Bild-Interfaces

- [ ] `SOLLTE` **Sprachausgabe unterbrechbar** und Geschwindigkeit einstellbar.
- [ ] `SOLLTE` **Transkript** zu jeder Sprachinteraktion.
- [ ] `SOLLTE` **Aufnahme-Status deutlich** (Mikrofon aktiv sichtbar).
- [ ] `SOLLTE` **Generierte Bilder** mit Alternativtext und KI-Label.
- [ ] `SOLLTE` **Alternative zur Sprache anbieten** (Texteingabe), für Menschen, die nicht sprechen können oder wollen.

## J. Einfache Verständlichkeit

- [ ] `SOLLTE` **Antworten in verständlicher Sprache,** Fachbegriffe erklären.
- [ ] `KANN` **Option für einfache Sprache** oder kürzere Antworten.
- [ ] `SOLLTE` **Einheitliche Persönlichkeit** der KI (Ton, Anrede, Namen) über alle Funktionen hinweg.

## Typische Fehler beim Vibe-Coding

- Leeres Chatfeld ohne Hinweis, was man fragen kann.
- Spinner ohne Abbruch, ohne Zeitlimit, ohne Fehlerzustand.
- KI führt Aktionen aus, ohne vorher zu zeigen, was passiert.
- KI-Persona tut so, als wäre sie ein Mensch.
- Credits verschwinden ohne Anzeige.

## Nachweis

Screenshots von leerem Zustand, Ladezustand, Fehlerzustand, Bestätigungsdialog und KI-Hinweis; kurzer Usability-Test mit drei bis fünf Personen.
