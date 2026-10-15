# Prüfer

Hier liegen die zwei Prüfer, die wir für den KI-App-Kriterienkatalog gebaut haben. Sie sind als **Skills für Claude Code** geschrieben, funktionieren aber mit jeder KI, die Dateien lesen kann.

| Prüfer | Wofür | Wann |
|---|---|---|
| [`ki-app-check`](./ki-app-check/SKILL.md) | Prüft **deine App** Punkt für Punkt gegen den Katalog und schreibt einen Ampel-Bericht (🟢 erfüllt, 🟡 teilweise, 🔴 fehlt, ⚪ nicht anwendbar, 🔵 musst du selbst erledigen) – mit Belegen und fertigen Prompts zum Beheben. | vor jedem Release, nach großen Änderungen |
| [`katalog-pruefen`](./katalog-pruefen/SKILL.md) | Prüft und aktualisiert **den Katalog selbst**: recherchiert neue Gesetze, Store-Regeln, Sicherheitsstandards und Best Practices, ergänzt Fehlendes mit Quelle und öffnet einen Pull Request. | alle drei Monate und vor wichtigen Fristen |
| [`katalog_check.py`](./katalog-pruefen/katalog_check.py) | Automatische Prüfung: Format jedes Punkts, Struktur, Links und 254 Pflichtthemen. | nach jeder Änderung am Katalog |

## Benutzen mit Claude Code

Die Skills einmal in deinen Skill-Ordner kopieren:

```bash
mkdir -p ~/.claude/skills && cp -R ~/Apps-Berater/pruefer/ki-app-check ~/Apps-Berater/pruefer/katalog-pruefen ~/.claude/skills/
```

Danach in Claude Code `/ki-app-check` im Ordner deiner App eingeben oder `/katalog-pruefen`, um den Katalog zu aktualisieren.

## Benutzen mit ChatGPT, Gemini oder anderen KIs

1. Die Datei `SKILL.md` des gewünschten Prüfers öffnen und ihren Inhalt als Anweisung in den Chat kopieren.
2. Dazu den Katalog geben (Link zu `wissen/ki-app-kriterienkatalog/` oder die Kapiteldateien hochladen) und den Code bzw. die Beschreibung deiner App.
3. Die KI arbeitet die Schritte der Anweisung ab und schreibt den Bericht.

Ohne Zugriff auf den Code kann die KI viele Punkte nur als 🔵 („selbst prüfen“) markieren. Am genauesten ist die Prüfung mit einem Coding-Agenten, der den App-Ordner lesen kann.

## Automatische Prüfung

```bash
python3 pruefer/katalog-pruefen/katalog_check.py
```

Das Skript findet den Katalog automatisch in diesem Repository. Neue Themen, die immer im Katalog stehen müssen, trägst du in der Liste `THEMEN` im Skript ein.
