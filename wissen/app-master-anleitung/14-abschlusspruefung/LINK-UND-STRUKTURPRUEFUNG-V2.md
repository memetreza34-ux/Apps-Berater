# Link- und Strukturprüfung v2

**Prüfdatum:** 4. August 2026  
**Prüfobjekt:** `01-apps/app-master-anleitung`

## Methode

- sämtliche 41 in Pull Request #2 geänderten Pfade mit der endgültigen Dateiliste abgeglichen;
- Ziele der zentralen Navigation in `README.md` und `INHALTSVERZEICHNIS.md` gegen vorhandene Pfade geprüft;
- Links der Vorlagenübersicht und der drei Beispielwege geprüft;
- technische Vertiefung `../allgemeine-app-entwicklung/README.md` auf dem Hauptbranch bestätigt;
- Pflichtdateiliste und Abschlussbedingungen mit `scripts/validate_master_guide.py` abgeglichen;
- DOCX vollständig in 31 Seiten gerendert und über Kontaktbögen visuell geprüft;
- PDF separat in 31 Seiten gerendert und mit PDF-Preflight auf Öffnbarkeit, Verschlüsselung und Seitenzahl geprüft.

## Ergebnis

- zentrale relative Links: ohne bekannten Defekt;
- vollständiges verlinktes Inhaltsverzeichnis: vorhanden;
- drei Beispielwege: vorhanden;
- sieben spezialisierte Projekt-/Vorlagenpakete einschließlich Master-Projektpaket: vorhanden;
- Quellen- und Aktualisierungsregister: vorhanden;
- Abschluss-Prüfrubrik und Rollenreview: vorhanden;
- DOCX-/PDF-Layout: keine erkannten Überlappungen, abgeschnittenen Texte, schwarzen Kästen oder fehlenden Seiten;
- PDF: 31 Seiten, nicht verschlüsselt, mit PyMuPDF öffnbar, kein Scan-PDF.

## Technische Grenze

Der Repository-Validator konnte nicht durch einen erfolgreichen GitHub-Actions-Lauf belegt werden, weil in diesem Repository auch minimale Diagnosejobs bereits vor dem ersten ausführbaren Schritt scheiterten. Diese Datei dokumentiert deshalb eine manuelle Zielpfad- und Renderprüfung. Das Skript bleibt für lokale oder später wieder funktionierende Runner vorhanden.

## Freigabe

**Ergebnis:** bestanden, mit dokumentierter GitHub-Actions-Einschränkung.
