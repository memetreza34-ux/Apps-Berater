from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "app_decision_assistant.py"
SPEC = importlib.util.spec_from_file_location("app_decision_assistant", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def answers(**overrides: bool) -> dict[str, bool]:
    base = {key: False for key, _ in MODULE.QUESTIONS}
    base.update(overrides)
    return base


class DecisionAssistantTests(unittest.TestCase):
    def test_simple_offline_app_is_normal_risk(self) -> None:
        result = MODULE.evaluate(answers())
        self.assertTrue(result.risk_level.startswith("normal"))
        self.assertFalse(result.blockers_to_resolve)
        self.assertIn("PRD.md", result.required_artifacts)

    def test_account_app_requires_data_controls(self) -> None:
        result = MODULE.evaluate(answers(accounts=True, personal_data=True))
        self.assertTrue(result.risk_level.startswith("erhöht"))
        self.assertIn("BERECHTIGUNGSMATRIX.md", result.required_artifacts)
        self.assertIn("DATENINVENTAR-UND-LOESCHUNG.md", result.required_artifacts)
        self.assertTrue(any("Autorisierung" in item for item in result.release_minimums))

    def test_medical_ai_app_is_high_risk(self) -> None:
        result = MODULE.evaluate(
            answers(
                personal_data=True,
                sensitive_data=True,
                ai=True,
                automated_decisions=True,
                health=True,
                mobile=True,
            )
        )
        self.assertTrue(result.risk_level.startswith("hoch"))
        self.assertGreaterEqual(len(result.blockers_to_resolve), 3)
        self.assertIn("AI-SYSTEM-REGISTER.md", result.required_artifacts)
        self.assertIn("PLATTFORM-UND-GERAETETESTMATRIX.md", result.required_artifacts)

    def test_unknown_key_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            MODULE.evaluate({"unknown": True})

    def test_markdown_output_contains_sections(self) -> None:
        result = MODULE.evaluate(answers(ai=True, payments=True))
        output = MODULE.to_markdown(result)
        self.assertIn("# App-Entscheidung", output)
        self.assertIn("## Pflichtmodule", output)
        self.assertIn("AI-SYSTEM-REGISTER.md", output)


if __name__ == "__main__":
    unittest.main()
