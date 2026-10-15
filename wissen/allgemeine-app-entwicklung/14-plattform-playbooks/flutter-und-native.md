# Flutter- und Native-Playbook

## Flutter

Geeignet, wenn ein gemeinsames mobiles UI mit kontrolliertem Rendering wichtig ist und das Team Dart dauerhaft pflegen kann.

### Prüfpunkte
- Plugins nach Wartung, Lizenz, Plattformabdeckung und nativer Implementierung bewerten;
- Plattformkanäle klein halten und testen;
- Navigation, State und Fehlerzustände als feste Architekturentscheidung dokumentieren;
- Isolates nur bei gemessenem Bedarf;
- App-Größe, Shader/Jank, Speicher und Startzeit auf echten Geräten messen;
- sichere lokale Speicherung und Cache-Löschung;
- Build-Flavors für Dev, Staging und Production;
- native Signierung und Berechtigungen separat pflegen.

## Native Swift/Kotlin

Geeignet, wenn tiefe Plattformintegration, maximale Kontrolle, anspruchsvolle Hardware oder sehr hohe native UX-Qualität benötigt wird.

### Prüfpunkte
- gemeinsame API- und Datenverträge zwischen iOS und Android;
- Feature-Parität bewusst definieren statt automatisch voraussetzen;
- Plattformdesign respektieren;
- Keychain/Keystore und geschützte lokale Daten;
- Hintergrundausführung nach Plattformregeln;
- Berechtigungen im Nutzungskontext erklären;
- App-/Universal Links;
- Signierung, Zertifikate und Recovery;
- Testmatrix je OS- und Geräteklasse;
- getrennte Store-Release- und Rollbackabläufe.

## Wann native statt Cross-Platform?

Native wird bevorzugt, wenn mehrere dieser Punkte gelten:
- Kernnutzen hängt von neuer oder spezieller Geräte-API ab;
- sehr hohe Anforderungen an Hintergrundbetrieb, Audio/Video oder Bluetooth;
- komplexe Widgets, Wearables oder Car-Integration;
- besonders strenge Performance- oder Sicherheitsanforderungen;
- getrennte Plattformteams sind dauerhaft finanzierbar.

## Gemeinsames Release-Gate

- [ ] schwierigste Plattformfunktion als Spike bewiesen
- [ ] Plugin-/SDK-Register vollständig
- [ ] sichere lokale Daten und Logoutbereinigung
- [ ] Build-Flavors/Targets getrennt
- [ ] Signierung und Recovery dokumentiert
- [ ] alte und neue Clients mit API/Migration kompatibel
- [ ] Accessibility je Plattform
- [ ] Geräte-, OS- und Netzwerktestmatrix
- [ ] Crash-, Startzeit-, Speicher- und Akkumessung
- [ ] Store-Rollout und Rollback
