# UX/UI, Inhalte, Designsystem und Prototyp

Dieses Kapitel führt vom Produktkonzept zu einer verständlichen, konsistenten und testbaren Benutzeroberfläche. Es verhindert, dass ein einzelner schöner Screenshot mit einem vollständigen App-Design verwechselt wird.

## Ziel

Am Ende liegen vor:

- Informationsarchitektur;
- Navigation;
- User Flows;
- Screen-Inventar;
- Content- und Mikrocopy-System;
- Accessibility-Anforderungen;
- Wireframes;
- Design Tokens;
- Komponentenbibliothek;
- klickbarer Prototyp;
- Usability-Testbericht;
- Entwickler-Handoff.

## 1. Informationsarchitektur

Ordne Inhalte und Funktionen nach Nutzeraufgaben, nicht nach interner Technik.

```text
Nutzerziel
→ benötigte Information
→ Entscheidung
→ Aktion
→ Rückmeldung
→ nächster sinnvoller Schritt
```

Prüffragen:

- Welche Hauptaufgaben haben Nutzer?
- Was muss sofort erreichbar sein?
- Welche Inhalte gehören zusammen?
- Welche Begriffe verstehen neue Nutzer?
- Welche Ebenen können entfernt werden?
- Was bleibt sichtbar, wenn keine Daten vorhanden sind?

## 2. Navigation auswählen

Mögliche Muster:

- Tab-/Bottom-Navigation;
- Sidebar;
- Stack-Navigation;
- Dashboard;
- Suche als Haupteinstieg;
- Master-Detail;
- schrittweiser Wizard.

Auswahl nach:

- Anzahl der Hauptbereiche;
- Nutzungshäufigkeit;
- Plattform;
- Gerätegröße;
- Tiefe der Struktur;
- Accessibility;
- Offline- und Ladeverhalten.

Navigation darf nicht nur aus einer Designreferenz kopiert werden.

## 3. User Flows

Für jeden wichtigen Ablauf dokumentieren:

- Auslöser;
- Einstiegspunkt;
- Schritte;
- Entscheidungen;
- Abbruch;
- Fehler;
- Wiederaufnahme;
- Erfolg;
- nächster Schritt.

Pflichtflows je nach App:

- Onboarding;
- Registrierung/Login;
- Kernfunktion;
- Erstellen/Bearbeiten/Löschen;
- Suche und Filter;
- Offline/Netzfehler;
- Kauf/Abo/Restore;
- Export und Kontolöschung;
- Support;
- Admin/Moderation.

## 4. Screen-Inventar

| Screen | Ziel | Rolle | Daten | primäre Aktion | sekundäre Aktionen | Zustände | Accessibility | Test |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

Für jeden Screen planen:

- Standard;
- Loading;
- Empty;
- Error;
- Offline;
- Success;
- Disabled;
- fehlende Berechtigung;
- sehr lange Inhalte;
- kleine und große Displays;
- Dark Mode;
- Textvergrößerung.

## 5. Onboarding und Aktivierung

Onboarding erklärt nur, was für den ersten Erfolg notwendig ist.

Gute Reihenfolge:

```text
Nutzen zeigen
→ nur notwendige Daten/Berechtigungen abfragen
→ Kernaktion durchführen
→ Ergebnis sichtbar machen
→ optionale Vertiefung anbieten
```

Vermeiden:

- lange Tour vor erster Nutzung;
- Berechtigungen ohne Kontext;
- Pflichtkonto ohne Produktgrund;
- mehrere Profilfragen vor Kernnutzen;
- manipulative Ablehnungsbuttons.

## 6. Inhalte und Mikrocopy

Für Texte gelten:

- klare Verben;
- kurze Sätze;
- eine Aktion pro Button;
- konkrete Fehlermeldungen;
- keine Schuldzuweisung;
- keine irreführenden Versprechen;
- konsistente Begriffe;
- verständliche Datenschutz- und Zahlungsinformationen.

Fehlermeldung enthält möglichst:

```text
Was ist passiert?
Was wurde nicht verändert?
Was kann der Nutzer tun?
Wo gibt es Hilfe?
```

## 7. Accessibility

Von Anfang an berücksichtigen:

- semantische Struktur;
- Screenreader-Namen;
- Fokusreihenfolge;
- Tastaturbedienung;
- Kontrast;
- Textskalierung;
- Touch-Ziele;
- Gestenalternativen;
- Reduced Motion;
- Statusmeldungen;
- Untertitel/Transkripte;
- Fehlererkennung und Korrektur;
- verständliche Sprache.

Accessibility ist kein abschließendes Plugin. Sie beeinflusst Struktur, Komponenten, Texte und Tests.

## 8. Mehrsprachigkeit und Lokalisierung

Planen:

- Textlängen;
- Rechts-nach-links-Sprachen;
- Datums-/Zeitformate;
- Zahlen und Währungen;
- Zeitzonen;
- Mehrzahlformen;
- kulturelle Symbole;
- Übersetzungsworkflow;
- Review durch Sprachkundige;
- Storetexte je Markt.

Texte nicht fest im Code verstreuen.

## 9. Referenzen analysieren

Referenzen dienen zum Lernen, nicht zum Kopieren.

Für jede Referenz:

| Quelle | gelöstes Problem | Muster | Stärke | Risiko | übernommenes Prinzip |
|---|---|---|---|---|---|
| | | | | | |

Nicht übernehmen:

- Logos und Markenauftritt;
- geschützte Illustrationen;
- Texte und Assets ohne Rechte;
- nahezu identische Gesamtgestaltung;
- ungewöhnliche, stark wiedererkennbare Kombinationen.

## 10. Wireframes

Wireframes klären:

- Hierarchie;
- Reihenfolge;
- Navigation;
- Aktionen;
- Zustände;
- Informationsdichte.

Noch keine Zeit in perfekte Farben oder Effekte investieren, bevor der Ablauf funktioniert.

## 11. Design Tokens

Semantische Tokens statt Einzelwerte:

```text
color.background.default
color.surface.primary
color.text.primary
color.text.secondary
color.action.primary
color.status.error
space.1 ... space.n
radius.small / medium / large
type.body / label / title / display
motion.fast / normal / slow
```

Tokens unterstützen:

- Light/Dark Mode;
- Plattformvarianten;
- konsistente Entwicklung;
- spätere Markenänderungen;
- automatisierte Prüfung.

## 12. Komponentenbibliothek

Mindestens:

- Button;
- Textfeld;
- Auswahl;
- Checkbox/Radio/Switch;
- Navigation;
- Karte/Listenzeile;
- Dialog/Bottom Sheet;
- Toast/Statusmeldung;
- Skeleton/Loader;
- Tabellen oder Listen;
- leere und Fehlerzustände.

Jede Komponente dokumentiert:

- Zweck;
- Varianten;
- Größen;
- Zustände;
- erlaubte Inhalte;
- Fokus/Screenreader;
- responsive Verhalten;
- verbotene Nutzung;
- Code-/Designreferenz.

## 13. Kernscreen als Qualitätsprobe

Bevor alle Screens gebaut werden, einen Kernscreen vollständig umsetzen:

- echte Texte und Daten;
- alle Zustände;
- kleine und große Displays;
- Dark Mode;
- Textvergrößerung;
- Fokus und Screenreader;
- lange Inhalte;
- langsame Daten;
- Fehler und Wiederholung.

Erst nach Freigabe weitere Screens ableiten.

## 14. Prototyp

Der Prototyp muss die wichtigsten Entscheidungen und Übergänge zeigen.

Mindestens testen:

- Einstieg;
- Kernaufgabe;
- Fehler;
- Rücknavigation;
- Abschluss;
- Auffindbarkeit wichtiger Einstellungen;
- Löschung/Kündigung, falls relevant.

## 15. Usability-Test

Mit passenden Personen, nicht nur Projektbeteiligten.

Aufgaben stellen, nicht erklären:

```text
Du möchtest [Nutzerziel] erreichen. Zeige, wie du vorgehen würdest.
```

Beobachten:

- Wo zögert die Person?
- Was wird falsch verstanden?
- Welche Begriffe sind unklar?
- Wo wird zurücknavigiert?
- Welche Erwartung wird verletzt?
- Wird der Kernnutzen erkannt?

Probleme bewerten nach:

- Schwere;
- Häufigkeit;
- Auswirkung auf Kernablauf;
- Sicherheits-/Rechtsfolge;
- Behebungsaufwand.

## 16. Entwickler-Handoff

Der Coding-Agent oder Entwickler erhält:

- Figma/Designquelle;
- Design Tokens;
- Komponentenvertrag;
- Screen-Inventar;
- User Flows;
- responsive Regeln;
- Accessibility-Anforderungen;
- echte Texte;
- Asset-Rechte;
- Akzeptanzkriterien;
- Screenshots der Sollzustände;
- Nicht-Ziele.

Guter KI-Auftrag:

```text
Setze ausschließlich den Dashboard-Screen anhand des bestehenden
Designsystems um. Bewahre Datenlogik und Navigation. Implementiere
Loading, Empty, Error, Offline und Success. Verwende nur vorhandene
Tokens und Komponenten. Prüfe Typecheck, Tests, Build, Tastatur,
Textskalierung und gerenderten Screenshot.
```

## KI-Einsatz

KI kann:

- Informationsarchitekturvarianten erzeugen;
- User Flows strukturieren;
- Screen-Inventare vorbereiten;
- Mikrocopyvarianten liefern;
- Design Tokens in Code übertragen;
- Accessibility-Risiken sammeln;
- Komponenten dokumentieren;
- Screens anhand klarer Vorgaben implementieren;
- visuelle Abweichungen beschreiben.

KI darf nicht:

- ungeprüft Designreferenzen kopieren;
- Nutzerforschung ersetzen;
- visuelle Qualität allein freigeben;
- Accessibility nur aus Code ableiten;
- Marken- und Asset-Rechte erfinden;
- neue UI-Muster ohne Produktbegründung einführen.

## Ergebnisse und Gate

Vor großer Umsetzung müssen vorliegen:

- Informationsarchitektur;
- User Flows;
- Screen-Inventar;
- Content-/Mikrocopy-Grundlage;
- Accessibility-Anforderungen;
- Wireframes;
- Tokens und Komponenten;
- getesteter Prototyp;
- priorisierte Usability-Probleme;
- Entwickler-Handoff.

**Gate bestanden:** Passende Testpersonen können den Kernablauf ohne Erklärung verstehen und schwere UX-/Accessibility-Probleme sind behoben oder klar als Blocker dokumentiert.
