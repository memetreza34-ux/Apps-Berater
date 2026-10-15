# FocusFlow – Product Requirements Document

## 1. Problem

Viele einfache Fokus-Apps starten mit komplizierter Einrichtung, zu vielen Statistiken oder einem überladenen Aufgabenmanagement. Nutzer benötigen einen schnellen Weg von „Ich muss etwas erledigen“ zu einer laufenden Fokus-Session.

## 2. Zielgruppe

Primär:

- Lernende und Auszubildende
- Berufstätige mit individuellen Aufgaben
- Nutzer, die einfache visuelle Führung bevorzugen

Nicht primär:

- große Teams
- Unternehmen mit Überwachungs- oder Zeiterfassungsbedarf
- medizinische Behandlung von ADHS oder anderen Erkrankungen

## 3. Produktziel

Ein neuer Nutzer kann ohne Erklärung:

1. ein Konto erstellen;
2. eine Aufgabe erfassen;
3. eine Dauer auswählen;
4. eine Session starten;
5. nach Ablauf den Erfolg sehen.

## 4. Nicht-Ziele

- kein soziales Netzwerk
- keine öffentliche Rangliste
- keine medizinischen Empfehlungen
- keine automatische Mitarbeiterbewertung
- kein komplexes Kalender-/Projektmanagement
- keine generative KI außerhalb der Aufgabenzerlegung

## 5. Rollen

### Gast

- Landing/Onboarding sehen
- Datenschutz/Impressum/Support öffnen
- registrieren oder anmelden

### Nutzer

- eigene Projekte, Aufgaben und Sessions verwalten
- eigene Daten exportieren
- eigenes Konto löschen
- optionale KI-Funktion innerhalb Limits nutzen

### Support/Admin

- minimale technische Kontoinformation sehen
- keine Aufgabeninhalte standardmäßig lesen
- Zugriff nur begründet und protokolliert
- keine Nutzerstatistik manipulieren

## 6. Kernfunktionen

### Auth

- Registrierung
- E-Mail-Bestätigung
- Login/Logout
- Passwort zurücksetzen
- alle Sessions widerrufen
- Konto löschen

### Projekte und Aufgaben

- Projekt erstellen/umbenennen/archivieren
- Aufgabe erstellen/bearbeiten/abschließen
- Titel erforderlich, begrenzte Länge
- optional geschätzte Minuten

### Fokus-Session

- Dauer auswählen
- Startzeit serverseitig oder nachvollziehbar speichern
- Pause/Abbruch nach klarer Produktentscheidung
- App-Neustart überstehen
- Abschluss genau einmal verbuchen
- Offline-/Synchronisationsverhalten dokumentieren

### Statistik

- heutige abgeschlossene Fokuszeit
- Anzahl abgeschlossener Sessions
- keine medizinische oder leistungsdiagnostische Interpretation

### KI-Aufgabenzerlegung

- Nutzer übermittelt eine Aufgabe
- Server-Gateway prüft Login, Limit und Eingabe
- Modell liefert strukturierte Schritte
- Nutzer muss Schritte vor Speicherung bestätigen
- kein automatisches Ausführen externer Aktionen

### Export und Löschung

- Export als JSON/CSV plus Metadaten
- Löschung von Auth, Datenbank, Storage, KI-/Anbieterdaten entsprechend Konzept
- aktive Abos vor Löschung behandeln, falls später eingeführt

## 7. Zustände

Jeder Kernscreen benötigt:

- Loading
- Empty
- Error
- Offline
- Success
- abgelaufene Session
- fehlende Berechtigung

## 8. Nichtfunktionale Anforderungen

### Security

- RLS auf allen nutzerbezogenen Tabellen
- negative Tests mit Nutzer A und B
- Secret-/Service-Schlüssel nur serverseitig
- Admin-MFA
- Rate Limits für Auth und KI

### Datenschutz

- Datenminimierung
- keine Rohprompts dauerhaft, sofern nicht erforderlich
- Export und Löschung
- Anbieterregister
- begrenzte technische Logs

### Accessibility

- WCAG-2.2-AA-Baseline für Web/Design
- Screenreader-Namen
- Textskalierung
- logische Fokusreihenfolge
- Reduced Motion
- ausreichend große Touch-Ziele

### Performance

- Kerninteraktion ohne unnötige Netzwerkrunden
- Timer läuft nicht ausschließlich über Client-Intervalle
- Bilder/Assets budgetieren
- p95-API- und KI-Latenz überwachen

### Betrieb

- getrennte Umgebungen
- versionierte Migrationen
- Backup und Restore
- Monitoring
- Incident- und Rollbackprozess

## 9. Akzeptanzkriterien Beta

- [ ] neuer Nutzer startet erste Session in unter 60 Sekunden im Usability-Test
- [ ] App-Neustart zerstört aktive Session nicht
- [ ] Nutzer A kann keine Ressource von Nutzer B lesen/ändern/löschen
- [ ] doppelter Abschluss erzeugt keine doppelte Statistik
- [ ] KI-Ausgabe wird validiert und erst nach Bestätigung gespeichert
- [ ] Export enthält alle eigenen fachlichen Daten
- [ ] Kontolöschung entfernt alle vorgesehenen Daten
- [ ] kritischer Fehler kann über Rollback oder Kill Switch eingedämmt werden

## 10. Kill-Kriterien

Produkt oder Funktion überarbeiten/stoppen, wenn:

- Kernablauf nach mehreren Iterationen nicht verständlich wird;
- variable KI-Kosten nicht beherrschbar sind;
- Daten-/Store-/Rechtsanforderungen nicht erfüllt werden können;
- die Hauptzielgruppe das Problem mit bestehenden einfachen Mitteln ausreichend löst;
- Retention zeigt, dass der Kernnutzen nicht wiederholt gebraucht wird.
