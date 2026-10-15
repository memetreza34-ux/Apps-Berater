# Prüf-Prompts für Coding-Agenten

Mit diesen Prompts prüft ein Coding-Agent (z. B. Claude Code, Codex, Cursor) deine App gegen diesen Katalog. Voraussetzung: Der Katalog liegt im Repository deiner App, z. B. unter `docs/kriterien/`. Passe den Pfad in den Prompts an.

**Wichtig:**

- Jeden Prompt in einer **frischen Sitzung** starten. Die KI, die den Code geschrieben hat, übersieht eigene Fehler leichter.
- Die KI soll **nur berichten**, nicht sofort ändern. Du entscheidest, was umgesetzt wird.
- Eine KI-Prüfung ersetzt keine Rechtsberatung und keinen professionellen Sicherheitstest. Sie findet aber viele typische Fehler.

## 1. Gesamtprüfung

```text
Du bist ein strenger Reviewer für KI-Apps. Lies alle Dateien in docs/kriterien/.
Prüfe dann dieses Repository gegen jeden Punkt mit der Stufe PFLICHT.

Für jeden PFLICHT-Punkt gib an:
- Status: erfüllt / nicht erfüllt / teilweise / nicht anwendbar / nicht prüfbar im Code
- Beleg: Datei und Zeile oder Begründung
- Risiko, falls nicht erfüllt
- konkreter nächster Schritt

Ändere keinen Code. Sortiere das Ergebnis nach Risiko. Erfinde keine Belege –
wenn du etwas nicht im Code findest, schreibe „nicht gefunden“.
```

## 2. Sicherheitsprüfung (Kapitel 05)

```text
Führe ein Security-Review dieses Repositories durch. Grundlage ist
docs/kriterien/05-sicherheit-grundlagen.md. Prüfe besonders:

1. Secrets im Client-Code, in öffentlichen Umgebungsvariablen oder in der Git-Historie
2. Datenbank: Hat jede Tabelle und jeder Storage-Bucket RLS bzw. Security Rules?
   Sind die Policies korrekt (Nutzer sieht nur eigene Daten)?
3. Jede API-Route: Wird Anmeldung UND Besitz bzw. Rolle geprüft? Gibt es IDOR-Lücken?
4. Kann ein Nutzer seine eigene Rolle, seinen Tarif oder Credits ändern?
5. Eingabevalidierung auf dem Server, XSS durch HTML- oder Markdown-Ausgabe
6. Uploads, SSRF, CORS, Security-Header
7. Rate-Limits auf teuren Endpunkten
8. Stripe- oder Store-Webhooks: Signaturprüfung, Preis vom Server
9. Unbekannte oder verdächtige Abhängigkeiten

Gib für jeden Fund an: Schweregrad (kritisch/hoch/mittel/niedrig), Datei und Zeile,
Angriffsszenario in einem Satz, Lösung. Ändere keinen Code.
```

## 3. KI-Sicherheitsprüfung (Kapitel 06 und 07)

```text
Prüfe alle KI-Funktionen dieses Repositories gegen
docs/kriterien/06-ki-sicherheit-llm-risiken.md und
docs/kriterien/07-ki-api-modelle-kosten-qualitaet.md.

Liste zuerst jeden KI-Aufruf auf (Datei, Modell, Zweck, welche Daten in den Prompt gehen).
Prüfe dann:
- Läuft der Aufruf nur serverseitig?
- Stehen Geheimnisse oder fremde Nutzerdaten im Prompt?
- Wird die Ausgabe ungeprüft als HTML, SQL, Code oder Befehl verwendet?
- Können Tools oder Agenten ohne Bestätigung folgenreiche Aktionen ausführen?
- Filtert die Vektor-Suche serverseitig nach Nutzer oder Organisation?
- Gibt es max_tokens, Eingabegrenzen, Timeout, Fehlerbehandlung, Nutzerlimits?
- Können externe Bilder oder Links in Antworten Daten abfließen lassen?
- Ist die Modellversion festgelegt?

Schlage außerdem zehn konkrete Angriffsprompts vor, mit denen ich die App testen kann.
Ändere keinen Code.
```

## 4. AI-Act-Einordnung (Kapitel 01)

```text
Lies docs/kriterien/01-eu-ai-act.md und docs/kriterien/15-sonderfaelle-nach-app-typ.md.
Analysiere dieses Repository und die Produktbeschreibung in docs/ bzw. README.md.

Erstelle eine Tabelle mit jeder KI-Funktion:
- Funktion und Zweck
- meine Rolle (Anbieter/Betreiber)
- mögliches Verbot nach Art. 5? (ja/nein/prüfen, mit Begründung)
- Transparenzpflicht nach Art. 50? (welcher Absatz, ist sie umgesetzt?)
- Hochrisiko nach Anhang III oder Anhang I? (ja/nein/prüfen, mit Begründung)
- offene Fragen für eine rechtliche Prüfung

Kennzeichne Unsicherheiten deutlich. Das ist eine Vorprüfung, keine Rechtsberatung.
```

## 5. Datenfluss und Datenschutz (Kapitel 02)

```text
Erstelle aus diesem Repository ein Daten- und Anbieterregister nach
docs/kriterien/02-datenschutz-dsgvo.md:

- Welche personenbezogenen Daten werden erhoben (Feld, Tabelle, Datei)?
- Wohin gehen sie (Datenbank, Storage, KI-Anbieter, Analytics, E-Mail, Fehler-Tracking)?
- Welche Drittanbieter und SDKs sind eingebunden, in welcher Region vermutlich?
- Wo werden Daten gelöscht, wenn ein Konto gelöscht wird – und wo nicht?
- Wird vor der Einwilligung Tracking geladen?
- Welche Angaben müssen in die Datenschutzerklärung und die Store-Formulare?

Gib das Ergebnis als Tabelle aus und liste Lücken separat auf. Ändere keinen Code.
```

## 6. Pflichtfunktionen und Store-Bereitschaft (Kapitel 09 und 13)

```text
Prüfe anhand von docs/kriterien/09-pflichtfunktionen.md und
docs/kriterien/13-app-stores-plattformen.md, welche Pflichtfunktionen und
Store-Anforderungen in dieser App vorhanden sind und welche fehlen.
Suche konkret nach: Konto löschen, Datenexport, Rechtsseiten in der App,
KI-Hinweis, Melden-Funktion, Kündigungs- und Widerrufsbutton, Käufe wiederherstellen,
Fehler- und Leerzustände, Berechtigungstexte.
Gib eine Liste „vorhanden (mit Datei)“ und „fehlt“ aus. Ändere keinen Code.
```

## 7. Kostenprüfung (Kapitel 07)

```text
Analysiere alle Stellen, an denen dieses Repository kostenpflichtige Dienste aufruft
(KI, Bild/Audio/Video, E-Mail, SMS, Speicher).
Schätze pro Aktion die Kosten, finde Stellen ohne Limit, ohne Caching oder mit
unnötig großem Modell oder Kontext. Schlage Kontingente pro Nutzer vor.
Berechne grob die monatlichen Kosten bei 100, 1.000 und 10.000 aktiven Nutzern
und nenne deine Annahmen. Ändere keinen Code.
```

## 8. Barrierefreiheit und UX (Kapitel 10 und 11)

```text
Prüfe die Oberfläche dieses Repositories gegen docs/kriterien/10-ki-ux.md und
docs/kriterien/11-design-barrierefreiheit.md.
Suche nach: fehlenden Labels und Alternativtexten, Buttons ohne zugänglichen Namen,
zu geringem Kontrast in den Design-Tokens, fehlenden Fokus-Stilen, fehlenden
Lade-/Fehler-/Leerzuständen, fehlendem Abbrechen bei KI-Generierung, fehlendem
KI-Hinweis, uneinheitlichen Abständen und Komponenten.
Gib die Funde mit Datei und Vorschlag aus. Ändere keinen Code.
```

## 9. Launch-Bereitschaft (Kapitel 12, 13 und 17)

```text
Prüfe anhand von docs/kriterien/12-tests-release-betrieb.md,
docs/kriterien/13-app-stores-plattformen.md und
docs/kriterien/17-produkt-launch-wachstum.md, ob diese App bereit für den Launch ist.
Suche im Repository nach: Fehler-Tracking, Kostenalarmen (soweit im Code sichtbar),
Rollback-Weg, Backup-Hinweisen, Analyse-Ereignissen (Tracking-Plan),
Landingpage mit Rechtsseiten, Store-Metadaten, Bewertungsdialog über die offizielle API,
Versions- und Build-Nummern.
Liste, was vorhanden ist, was fehlt und was nur außerhalb des Codes geprüft werden kann.
Ändere keinen Code.
```

## 10. Umsetzen nach der Prüfung

```text
Setze aus dem letzten Prüfbericht nur Punkt [NUMMER] um.
Vorgehen:
1. Zeige mir zuerst den Plan und die Dateien, die du ändern willst.
2. Warte auf meine Bestätigung.
3. Ändere nur, was für diesen Punkt nötig ist.
4. Schreibe oder ergänze einen Test, der das Problem nachweist und jetzt besteht.
5. Führe Build, Typprüfung, Linter und Tests aus und zeige die Ausgabe.
6. Schlage eine Commit-Nachricht vor.
```

## Nachweis

Die Prüfberichte mit Datum im Repository ablegen (z. B. `docs/pruefungen/2026-09-29-security.md`). So siehst du später, was geprüft und behoben wurde.
