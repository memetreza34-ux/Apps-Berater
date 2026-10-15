# 14 – Plattform-Playbooks

Das allgemeine Architekturkapitel entscheidet **welche Plattform** passt. Diese Playbooks beschreiben, was bei der praktischen Umsetzung zusätzlich geprüft werden muss.

## Verfügbare Playbooks

- [Web und PWA](./web-pwa.md)
- [React Native und Expo](./react-native-expo.md)
- [Flutter und native Apps](./flutter-und-native.md)

## Gemeinsame Pflichtpunkte

Unabhängig von der Plattform:

- getrennte Dev-, Staging- und Produktionsumgebungen;
- reproduzierbare Builds und Lockfiles;
- sichere Secret- und Tokenbehandlung;
- Versionierung von API und Datenbank;
- Accessibility auf echten Geräten;
- Offline-, Fehler- und Updateverhalten;
- Deep Links und App-/Web-Links;
- Push und Berechtigungen nur bei echtem Bedarf;
- Crash-, Performance- und Kostenmonitoring;
- Rollback oder Abschaltmöglichkeit;
- Supportmatrix für Betriebssystem- und App-Versionen.

## Auswahlregel

Ein Stack gilt erst als bestätigt, wenn ein technischer Spike die schwierigsten Anforderungen beweist: beispielsweise Hintergrundbetrieb, Kamera, Push, Offline-Synchronisation, Dateiimport, Widget oder App-Store-Zahlung.
