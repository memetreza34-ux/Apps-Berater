# Gesamtfahrplan – von der Idee bis zum langfristigen App-Betrieb

Dieser Fahrplan zeigt den vollständigen Lebenszyklus. Die einzelnen Kapitel erklären später jeden Schritt ausführlich.

## Phase 0 – Voraussetzungen und Ziel

### Klären

- Warum möchtest du diese App bauen?
- Soll sie lernen, Geld verdienen, Bewerbungen stärken oder ein Unternehmen werden?
- Wie viel Zeit und Budget stehen realistisch zur Verfügung?
- Arbeitest du allein oder mit Partnern?
- Welche Plattformen sind wirklich nötig?

### Du benötigst grundsätzlich

- einen geeigneten Computer;
- stabile Internetverbindung;
- E-Mail-Adresse für Projektkonten;
- Passwortmanager und Zwei-Faktor-Authentifizierung;
- GitHub-Repository;
- Entwicklungsumgebung;
- KI- oder Coding-Agent;
- Designwerkzeug oder klare Designreferenz;
- Testgeräte beziehungsweise Browser;
- Budgetübersicht für Anbieter, Stores, Domains und APIs;
- Zeit für Support, Updates und Marketing.

### Ergebnis

`APP-STECKBRIEF.md` mit Ziel, Zielgruppe, Plattform, Zeit, Budget und Verantwortlichem.

---

## Phase 1 – Problem und Zielgruppe

### Schritte

1. Problem in einem Satz formulieren.
2. Zielgruppe so eng wie möglich bestimmen.
3. Aktuelle Lösung oder Workaround untersuchen.
4. Mit passenden Personen sprechen.
5. Häufigkeit, Dringlichkeit und Zahlungsbereitschaft prüfen.
6. Belege und Gegenargumente dokumentieren.
7. Stop-/Go-Kriterien anwenden.

### KI hilft bei

- Interviewfragen;
- Zusammenfassung anonymisierter Aussagen;
- Hypothesen und Gegenhypothesen;
- Zielgruppenvarianten;
- Research-Struktur.

### Mensch prüft

- ob echte Personen das Problem tatsächlich haben;
- ob Aussagen nur Zustimmung aus Höflichkeit sind;
- ob die App gegenüber bestehenden Alternativen relevant genug ist.

### Gate

Nicht weiterbauen, solange nur die eigene Vermutung existiert.

---

## Phase 2 – Markt und Positionierung

### Schritte

1. Direkte Konkurrenz sammeln.
2. Indirekte Lösungen einbeziehen: Tabellen, Papier, WhatsApp, Agenturen, bestehende Abläufe.
3. Funktionen, Preise, Bewertungen und Beschwerden vergleichen.
4. Marktsegment und erreichbaren Einstieg bestimmen.
5. klare Differenzierung formulieren.
6. Nutzenversprechen testen.

### Ergebnis

- Wettbewerbsübersicht;
- Positionierung;
- Satz: „Für [Zielgruppe] löst die App [Problem] durch [Unterschied].“

---

## Phase 3 – Geschäftsmodell und Kosten

### Entscheidungen

- kostenloses Produkt;
- einmaliger Kauf;
- Abonnement;
- Freemium;
- Credits;
- Werbung;
- B2B-Lizenz;
- Lead- oder Vermittlungsmodell.

### Kosten erfassen

- Entwicklung und Design;
- Domain, Hosting, Datenbank und Storage;
- E-Mail, Push und Analytics;
- KI- und Medien-APIs;
- Apple-/Google-Konten und mögliche Storegebühren;
- Zahlungsabwicklung;
- Recht, Steuer und Buchhaltung;
- Support und Wartung;
- Marketing;
- Rückerstattungen und Missbrauch.

### Gate

Das Modell muss bei realistischen Nutzerzahlen grundsätzlich tragfähig sein. Eine kostenlose App mit hohen laufenden KI-Kosten ist kein nachhaltiges Modell.

---

## Phase 4 – Machbarkeit, Rechte und Risiken

### Prüfen

- Sind Daten oder APIs verfügbar und legal nutzbar?
- Besitzt du Rechte an Namen, Texten, Bildern, Icons, Sounds und Designs?
- Welche personenbezogenen Daten werden verarbeitet?
- Welche Drittanbieter erhalten Daten?
- Gibt es Medizin-, Finanz-, Kinder-, Biometrie-, Community- oder Hardware-Risiken?
- Erlauben Stores und Plattformen die Kernfunktion?
- Was passiert, wenn ein Anbieter verschwindet oder Preise erhöht?

### Ergebnis

- Risikoprofil;
- Datenquellen- und Rechte-Register;
- Anbieterübersicht;
- Stop-/Go-Entscheidung.

---

## Phase 5 – Produktkonzept, PRD und MVP

### Schritte

1. Produktvision und messbares Ziel definieren.
2. Nutzerrollen bestimmen.
3. wichtigsten End-to-End-Kernablauf beschreiben.
4. Funktionen sammeln.
5. Must-have, später und nicht geplant trennen.
6. Akzeptanzkriterien schreiben.
7. Nicht-Ziele dokumentieren.
8. erste Roadmap erstellen.

### KI hilft bei

- PRD-Entwurf;
- User Stories;
- Akzeptanzkriterien;
- Priorisierungsvorschlägen;
- Risiko- und Grenzfalllisten.

### Gate

Das MVP muss einen vollständigen Nutzen liefern. Es darf klein sein, aber nicht aus vielen unfertigen Attrappen bestehen.

---

## Phase 6 – Nutzerabläufe und Inhalte

### Schritte

1. Informationsarchitektur erstellen.
2. Navigation wählen.
3. User Flows für Einstieg, Kernfunktion, Fehler, Zahlung, Export, Löschung und Support zeichnen.
4. alle Screens inventarisieren.
5. Zustände planen: Loading, Empty, Error, Offline, Success.
6. Texte und Fehlermeldungen schreiben.
7. Accessibility- und Mehrsprachigkeitsanforderungen definieren.

### Ergebnis

Ein vollständiger Ablauf, bevor High-Fidelity-Design oder großer Code entsteht.

---

## Phase 7 – Design und Prototyp

### Schritte

1. Designrichtung und Referenzen sammeln.
2. Prinzipien statt fremde Screens kopieren.
3. Wireframes erstellen.
4. Design Tokens definieren.
5. Komponenten mit Zuständen bauen.
6. wichtigsten Screen vollständig gestalten.
7. klickbaren Kernflow erstellen.
8. mit passenden Nutzern testen.
9. schwere Verständnisprobleme beheben.

### Gate

Nutzer müssen den Kernablauf ohne dauernde Erklärung durchführen können.

---

## Phase 8 – Plattform und Architektur

### Entscheidungen

- Web-App/PWA;
- React Native/Expo;
- Flutter;
- native iOS-/Android-App;
- Desktop;
- Kombination mehrerer Plattformen.

### Architektur umfasst

- Client und Navigation;
- Backend/API;
- Authentifizierung;
- Datenbank und Storage;
- Rollen und Berechtigungen;
- Offline und Synchronisation;
- Drittanbieter;
- KI-Gateway;
- Zahlung;
- Analytics und Monitoring;
- Backup, Restore und Exit-Plan.

### Gate

Kernfunktionen müssen technisch getestet sein. Plattformwahl nicht allein wegen eines Trends treffen.

---

## Phase 9 – Entwicklungsumgebung und KI-Agent

### Einrichten

- Repository und README;
- Setup-Anleitung;
- `.env.example` ohne echte Secrets;
- Dev, Staging und Production;
- Formatter, Lint und Typecheck;
- Test- und Buildbefehle;
- Branch- und Commitregeln;
- Datenbankmigrationen;
- Agentenregeln und Kontextdateien;
- Backup- und Rollbackstrategie.

### KI-Arbeitsweise

Der Agent liest zuerst Produkt-, Design-, Architektur- und Risikodokumente. Danach analysiert er den Bestand, plant kleine Schritte, setzt nur den bestätigten Abschnitt um und liefert Test- sowie Abschlussbericht.

---

## Phase 10 – Ersten vertikalen Kernablauf bauen

Nicht zuerst alle Oberflächen bauen. Einen vollständigen Weg umsetzen:

```text
Nutzeraktion
→ UI
→ Validierung
→ Authentifizierung und Autorisierung
→ API und Datenbank
→ Erfolg oder verständlicher Fehler
→ Speicherung nach Neustart
→ Test und Monitoring
```

### Pflichtfälle

- Doppelaktion;
- abgelaufene Sitzung;
- langsames oder fehlendes Internet;
- ungültige Eingabe;
- Daten anderer Nutzer;
- App-Neustart;
- Löschen und Wiederherstellen;
- kleine und große Bildschirmgrößen.

---

## Phase 11 – Weitere Funktionen kontrolliert ergänzen

Erst nach dem stabilen Kern:

- KI/RAG/Agenten;
- Zahlungen und Abos;
- Push und E-Mail;
- Uploads und Medien;
- Realtime;
- Community;
- Adminbereich;
- Importe und Exporte;
- komplexe Integrationen.

Jede Zusatzfunktion braucht Nutzen, Kostenlimit, Datenschutzprüfung, Fehlerplan, Tests und Abschaltmöglichkeit.

---

## Phase 12 – Produktionsreife

### Prüfen

- funktionale Tests;
- echte Geräte und Browser;
- Accessibility;
- Security und Berechtigungen;
- Datenschutz, Export und Kontolöschung;
- Performance und große Datenbestände;
- Backup und Restore;
- Rollback;
- Monitoring und Alarme;
- Support und Incident-Prozess;
- Store- und Rechtstexte gegen echte Technik.

### Ergebnis

Release Candidate ohne kritische Blocker und mit verlinkten Nachweisen.

---

## Phase 13 – Monetarisierung

### Umsetzen und testen

- Produkte und Preise;
- Store- oder Web-Zahlung;
- serverseitige Verifikation;
- internes Entitlement;
- signierte, idempotente Webhooks;
- Restore;
- Kündigung;
- Refund und Chargeback;
- Grace Period;
- Geräte- und Accountwechsel;
- Kontolöschung mit aktivem Abo;
- Kosten- und Supportprozess.

---

## Phase 14 – Veröffentlichungspaket

### Benötigt

- finaler Name und Icon;
- Screenshots und Vorschauvideo;
- Store-Beschreibung und Keywords;
- Landingpage;
- Supportseite;
- Datenschutzerklärung und Anbieterinformationen;
- externer Löschweg, falls erforderlich;
- Altersfreigabe;
- Berechtigungsbegründungen;
- App-Privacy-/Data-Safety-Angaben;
- Review-Konto und Review Notes;
- signierter Build;
- Rollout- und Rollbackplan.

---

## Phase 15 – Beta und Veröffentlichung

### Ablauf

1. interne Tests;
2. geschlossene Beta;
3. Feedback priorisieren;
4. Release Candidate einfrieren;
5. letzte Migration und Backup;
6. Store- oder Web-Einreichung;
7. Reviewfragen beantworten;
8. gestaffelt ausrollen;
9. Crashes, Kernablauf, Zahlung und Kosten beobachten;
10. bei Bedarf stoppen oder zurückrollen.

---

## Phase 16 – Marketing vor und während des Launches

### Vor dem Launch

- Zielgruppe und Botschaft;
- Warteliste oder Beta-Gruppe;
- Landingpage;
- Content-Plan;
- Demo und Erklärmaterial;
- Communities und Partner;
- App Store Optimization;
- Tracking und Conversionziele.

### Launch

- klarer Starttermin;
- Plattformen und Inhalte koordinieren;
- bestehende Kontakte informieren;
- Feedbackkanäle besetzen;
- Bewertungen nicht manipulieren;
- Anzeigen zuerst klein testen;
- Akquisitionskosten gegen tatsächlichen Nutzerwert messen.

### KI hilft bei

- Contentvarianten;
- Skripten und Creatives;
- Keyword- und Konkurrenzanalyse;
- Kampagnenstruktur;
- Auswertung von Rückmeldungen.

### Mensch entscheidet

- Markenbotschaft;
- ehrliche Produktversprechen;
- Budget;
- Zielgruppe;
- Interpretation der Ergebnisse.

---

## Phase 17 – Nach dem Launch verbessern

### Messen

- Aktivierung;
- Erfolg des Kernablaufs;
- D1/D7/D30-Retention;
- Abbruchstellen;
- Crash- und Fehlerrate;
- Conversion und Kündigung;
- Supportfälle;
- Kosten pro aktivem Nutzer;
- Nutzerbewertungen;
- Marketingkanäle.

### Verbesserungsprozess

```text
Beobachtung
→ Hypothese
→ kleinstes Experiment
→ Messung
→ Entscheidung
→ Dokumentation
```

Nicht jede Nutzerforderung wird direkt gebaut. Häufigkeit, Schwere, Produktziel und Kosten entscheiden.

---

## Phase 18 – Betrieb über Jahre

### Täglich oder laufend

- kritische Fehler;
- Authentifizierung;
- Zahlungen;
- Kernablauf;
- Missbrauch;
- Kosten und Limits.

### Regelmäßig

- Supportmuster;
- Abhängigkeiten und Security-Patches;
- Backup-/Restore-Test;
- Zugriffsrechte;
- Anbieter und Verträge;
- Datenschutz- und Storeangaben;
- Betriebssystem- und Geräteunterstützung;
- Roadmap und Profitabilität.

### Jährlich

- Gesamtprüfung des Produkts;
- rechtliche und technische Aktualisierung;
- Architektur- und Anbieterentscheidung;
- Marktposition;
- End-of-Life- oder Skalierungsentscheidung.

---

## Phase 19 – Skalieren, verkaufen oder beenden

### Skalieren nur bei Beleg

- wiederkehrende Nutzung;
- tragfähige Kosten;
- klarer Wachstumskanal;
- stabile Qualität;
- Supportfähigkeit.

### Mögliche Wege

- neue Plattformen;
- Internationalisierung;
- Teamaufbau;
- B2B-Version;
- Partnerschaften;
- API oder Integrationen;
- Finanzierung;
- Lizenzierung oder Verkauf;
- Anbieterwechsel;
- geordnetes Produktende.

### Produktende

Nutzer früh informieren, Exporte ermöglichen, Zahlungen beenden, Daten nach Plan löschen, Abhängigkeiten abschalten und Sicherheitsrisiken vermeiden.

## Die zentrale Wahrheit

Eine App ist nicht fertig, weil sie kompiliert oder im Store sichtbar ist. Sie ist als Version fertig, wenn sie einen belegten Nutzen verständlich, sicher, wirtschaftlich und betreibbar liefert. Danach beginnt die Produktpflege.
