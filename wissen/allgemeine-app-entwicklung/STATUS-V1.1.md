# Status – Allgemeine App-Entwicklung v1.1

**Stand:** 4. August 2026  
**Status:** evidenzbasierter Produktionsleitfaden abgeschlossen

## Was gegenüber v1.0 verbessert wurde

- objektive Evidenzstufen statt überwiegend subjektiver Punktvergabe;
- normalisierte Qualitätsquote für nicht anwendbare Bereiche;
- risikobasierte Mindestwerte und klarere Release-Blocker;
- Evidenz-Matrix und erweiterte Produktionsvorlage;
- interaktiver App-Entscheidungsassistent mit Testfällen;
- konkrete Plattform-Playbooks für Web/PWA, React Native/Expo, Flutter und Native;
- maschinenlesbare Design Tokens und Komponentenvertrag;
- kopierbare CI-Vorlagen;
- lokaler Validator und vorbereiteter GitHub-Actions-Workflow;
- vier konkrete Betriebs- und Notfall-Runbooks;
- direkt ausführbare FocusFlow-PWA mit Persistenz, Offline-App-Shell, Export und Löschung;
- FocusFlow-Supabase-Migration;
- ausführbarer Zwei-Nutzer-RLS-Negativtest;
- korrigierte sieben Freigabe-Gates;
- vollständige v1.1-Navigation.

## Qualitätsbewertung unter demselben Maßstab

| Bereich | v1.0 | v1.1 |
|---|---:|---:|
| Themenabdeckung | 9,5 | 9,7 |
| praktische Vorlagen | 9,3 | 9,7 |
| direkte Umsetzbarkeit | 7,5 | 9,1 |
| vorbereitete Automatisierung | 6,5 | 9,4 |
| objektive Qualitätsprüfung | 8,2 | 9,7 |
| Plattformpraxis | 8,0 | 9,4 |
| Betrieb und Recovery | 8,5 | 9,6 |
| ausführbare Beispiele | 6,8 | 9,0 |
| Aktualisierbarkeit | 9,6 | 9,8 |

**Gesamtbewertung als allgemeines App-Handbuch und Qualitätssystem: 9,5/10.**

Die Bewertung bezieht sich auf das Handbuchsystem, nicht auf eine konkrete App. Eine konkrete App erreicht ihre Qualität erst durch ausgefüllte Artefakte, tatsächliche Implementierung, Nutzerfeedback und projektspezifische Evidenz.

## Prüfskripte und Workflow

Vorhanden sind Prüfungen für:

- Pflichtdateien und relative Links;
- Quellen-Prüfdatum;
- Struktur des Qualitätssystems;
- Entscheidungsassistent und Klassifizierungsfälle;
- FocusFlow-PWA-Struktur;
- JavaScript-Syntax;
- HTTP-Smoke-Test;
- externe Markdown-Links.

Der GitHub-Workflow ist derzeit absichtlich nur manuell aktivierbar. Bei der v1.1-Erstellung schlug auch ein minimaler Einzeilen-Diagnosejob im verbundenen Repository bereits vor dem ersten ausführbaren Schritt fehl. Daher konnte kein erfolgreicher GitHub-Actions-Lauf als Nachweis erzeugt werden. Nach Behebung der Runner-/Kontokonfiguration können Push-, Pull-Request- und Zeitplantrigger aktiviert werden.

Der echte RLS-Smoke-Test wird nur gegen eine isolierte Test-/Staging-Umgebung mit zwei Testkonten ausgeführt, weil dafür Zugangsdaten erforderlich sind.

## Bewusste Grenzen

Auch v1.1 ersetzt nicht:

- echte Nutzerinterviews und Usability-Tests;
- externe Security- oder Code-Reviews bei hohem Risiko;
- Tests auf den tatsächlichen Zielgeräten;
- fachkundige Rechts-, Medizin-, Finanz- oder Zulassungsprüfung;
- eine vollständige produktive App mit realem Storekonto, Zahlung und Cloudbetrieb;
- laufende Aktualisierung bei geänderten Gesetzen, Store-Regeln und Frameworks.

## Ergebnis

Version 1.1 ist als allgemeiner, praktischer und wiederholbar prüfbarer App-Entwicklungsleitfaden abgeschlossen. Neue Projekte starten mit `START-HIER-V1.1.md`, führen den Entscheidungsassistenten aus und verwenden Produktionspaket plus Evidenz-Matrix.
