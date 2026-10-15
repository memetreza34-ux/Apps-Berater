from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable


QUESTIONS = [
    ("personal_data", "Verarbeitet die App personenbezogene Daten?"),
    ("sensitive_data", "Verarbeitet sie besondere oder sehr sensible Daten?"),
    ("accounts", "Besitzt die App Nutzerkonten oder mehrere Rollen?"),
    ("ai", "Enthält die App KI-Funktionen?"),
    ("automated_decisions", "Trifft KI automatische Entscheidungen über Menschen oder führt Aktionen aus?"),
    ("user_content", "Können Nutzer Inhalte veröffentlichen oder miteinander interagieren?"),
    ("minors", "Richtet sich die App an Minderjährige oder besonders verletzliche Gruppen?"),
    ("health", "Betrifft die Kernfunktion Gesundheit, Diagnose, Therapie oder medizinische Überwachung?"),
    ("finance", "Betrifft sie Anlage, Kredit, Versicherung, Wallet, Zahlung oder personalisierte Finanzentscheidungen?"),
    ("hardware", "Steuert oder verbindet sie Hardware, IoT, Fahrzeuge oder physische Prozesse?"),
    ("payments", "Verkauft sie Käufe, Abos, Credits oder B2B-Lizenzen?"),
    ("tracking", "Nutzt sie nicht notwendiges Tracking, Werbung oder Marketing-SDKs?"),
    ("mobile", "Wird sie als iOS-/Android-App veröffentlicht?"),
    ("offline", "Muss der Kernablauf zuverlässig offline funktionieren und später synchronisieren?"),
]


@dataclass(frozen=True)
class DecisionResult:
    risk_level: str
    blockers_to_resolve: list[str]
    required_modules: list[str]
    required_artifacts: list[str]
    release_minimums: list[str]


def normalize_answers(raw: dict[str, object]) -> dict[str, bool]:
    answers: dict[str, bool] = {}
    valid = {key for key, _ in QUESTIONS}
    unknown = set(raw) - valid
    if unknown:
        raise ValueError(f"Unbekannte Antwortschlüssel: {', '.join(sorted(unknown))}")

    for key, _ in QUESTIONS:
        value = raw.get(key, False)
        if isinstance(value, bool):
            answers[key] = value
        elif isinstance(value, str) and value.strip().lower() in {"ja", "j", "yes", "y", "true", "1"}:
            answers[key] = True
        elif isinstance(value, str) and value.strip().lower() in {"nein", "n", "no", "false", "0", ""}:
            answers[key] = False
        else:
            raise ValueError(f"Ungültiger Wert für {key}: {value!r}")
    return answers


def evaluate(raw_answers: dict[str, object]) -> DecisionResult:
    a = normalize_answers(raw_answers)
    modules = {
        "00-start/entscheidungsweg.md",
        "01-produkt/README.md",
        "02-design/README.md",
        "03-technik/README.md",
        "05-sicherheit-datenschutz-recht/README.md",
        "06-tests-release-betrieb/README.md",
        "11-masterprozess/APP-VON-0-BIS-RELEASE.md",
    }
    artifacts = {
        "APP-RISIKOPROFIL.md",
        "PRD.md",
        "SCREEN-INVENTAR.md",
        "ARCHITEKTUR-ADRS.md",
        "TESTPLAN.md",
        "RELEASE-DOSSIER.md",
    }
    blockers: list[str] = []
    minimums = [
        "Kein kritischer Blocker",
        "Kernfunktion und Produktnutzen mindestens Evidenzstufe 4",
        "Release-Evidenzmatrix vollständig",
    ]

    elevated = False
    high = False

    if a["personal_data"] or a["accounts"]:
        artifacts.update({"DATENINVENTAR-UND-LOESCHUNG.md", "BERECHTIGUNGSMATRIX.md", "THREAT-MODEL.md"})
        modules.add("03-technik/supabase-produktionsleitfaden.md")
        minimums.extend([
            "Daten/Autorisierung mindestens Evidenzstufe 4",
            "Datenschutz/Recht mindestens Evidenzstufe 4",
            "Export und Löschung Ende-zu-Ende getestet",
        ])
        elevated = True

    if a["sensitive_data"]:
        blockers.append("DSFA-/Hochrisiko-Datenschutzprüfung vor Produktionsdaten klären")
        minimums.append("Zweite fachliche Datenschutz-/Security-Prüfperspektive")
        high = True

    if a["ai"]:
        modules.add("04-ki-agenten/ki-produktionsleitfaden.md")
        artifacts.add("AI-SYSTEM-REGISTER.md")
        minimums.extend([
            "KI-Goldenset, Angriffstests, Kostenlimit und Kill Switch",
            "Modell-/Promptversion und Transparenz dokumentiert",
        ])
        elevated = True

    if a["automated_decisions"]:
        blockers.append("AI-Act-/DSGVO-Rolle, menschliche Aufsicht und Schadenspotenzial fachlich klassifizieren")
        high = True

    if a["user_content"]:
        modules.add("10-sonderfaelle/README.md")
        artifacts.update({"MODERATIONS-UND-MELDEKONZEPT.md", "COMMUNITY-RISIKOMODELL.md"})
        minimums.append("Melden, Blockieren, Beschwerde und Moderation getestet")
        elevated = True

    if a["minors"]:
        blockers.append("Zielalter, Einwilligung, Schutzkonzept und manipulative Muster fachlich prüfen")
        modules.add("10-sonderfaelle/README.md")
        high = True

    if a["health"]:
        blockers.append("Medizinische Zweckbestimmung und mögliche Medizinprodukteinstufung vor Kernentwicklung klären")
        modules.add("10-sonderfaelle/README.md")
        high = True

    if a["finance"]:
        blockers.append("Erlaubnis-/Lizenz-, Haftungs-, Betrugs- und automatisierte Entscheidungsfragen fachlich klären")
        modules.add("10-sonderfaelle/README.md")
        high = True

    if a["hardware"]:
        blockers.append("Physische Folgen, CRA-Scope, Updatezeitraum, SBOM und sichere Deaktivierung klären")
        modules.update({"10-sonderfaelle/README.md", "14-plattform-playbooks/README.md"})
        high = True

    if a["payments"]:
        modules.add("08-zahlungen-und-abos/README.md")
        artifacts.add("ZAHLUNGS-UND-ENTITLEMENT-MATRIX.md")
        minimums.append("Zahlungen/Entitlements mindestens Evidenzstufe 4")
        elevated = True

    if a["tracking"]:
        artifacts.add("SDK-UND-CONSENT-REGISTER.md")
        minimums.append("Consent, Widerruf und Store-Datenschutzangaben abgeglichen")
        elevated = True

    if a["mobile"]:
        modules.add("14-plattform-playbooks/README.md")
        artifacts.add("PLATTFORM-UND-GERAETETESTMATRIX.md")
        minimums.append("Release-Build auf echten Zielgeräten getestet")

    if a["offline"]:
        artifacts.add("OFFLINE-UND-SYNCHRONISATIONSKONZEPT.md")
        minimums.append("Konflikt-, Retry-, Doppelaktions- und Wiederverbindungstests")
        elevated = True

    if high:
        risk_level = "hoch – externe/fachkundige Prüfung vor Kernfreigabe"
    elif elevated:
        risk_level = "erhöht – zusätzliche technische und Compliance-Nachweise"
    else:
        risk_level = "normal – allgemeiner App-Prozess anwendbar"

    return DecisionResult(
        risk_level=risk_level,
        blockers_to_resolve=sorted(set(blockers)),
        required_modules=sorted(modules),
        required_artifacts=sorted(artifacts),
        release_minimums=sorted(set(minimums)),
    )


def ask_interactively() -> dict[str, bool]:
    answers: dict[str, bool] = {}
    print("App-Entscheidungsassistent – antworte mit j/n")
    for key, question in QUESTIONS:
        while True:
            value = input(f"{question} [j/n]: ").strip().lower()
            if value in {"j", "ja", "y", "yes"}:
                answers[key] = True
                break
            if value in {"n", "nein", "no"}:
                answers[key] = False
                break
            print("Bitte j oder n eingeben.")
    return answers


def to_markdown(result: DecisionResult) -> str:
    def section(title: str, items: Iterable[str], empty: str = "Keine zusätzlichen Punkte.") -> list[str]:
        values = list(items)
        return [f"## {title}", "", *(f"- {item}" for item in values)] if values else [f"## {title}", "", empty]

    lines = ["# App-Entscheidung", "", f"**Risikostufe:** {result.risk_level}", ""]
    lines += section("Vor Entwicklung zu klärende Blocker", result.blockers_to_resolve)
    lines += [""] + section("Pflichtmodule", result.required_modules)
    lines += [""] + section("Pflichtartefakte", result.required_artifacts)
    lines += [""] + section("Release-Mindestnachweise", result.release_minimums)
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Ermittelt Pflichtmodule und Risiken für eine App.")
    parser.add_argument("--answers", type=Path, help="JSON-Datei mit Antworten; ohne Datei interaktiv")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    parser.add_argument("--output", type=Path, help="optionale Ausgabedatei")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.answers:
        raw = json.loads(args.answers.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise ValueError("Die Antwortdatei muss ein JSON-Objekt enthalten.")
        answers = raw
    else:
        answers = ask_interactively()

    result = evaluate(answers)
    output = json.dumps(asdict(result), ensure_ascii=False, indent=2) + "\n" if args.format == "json" else to_markdown(result)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
        print(f"Erstellt: {args.output}")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
