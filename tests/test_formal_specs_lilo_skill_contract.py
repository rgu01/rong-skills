from pathlib import Path
import unittest


ROOT = Path(__file__).parents[1]
SKILL_DIR = ROOT / "skills/formal-specs-lilo"
SKILL = SKILL_DIR / "SKILL.md"
OPENAI_YAML = SKILL_DIR / "agents/openai.yaml"
DECOMPOSITION = SKILL_DIR / "references/requirement-decomposition.md"
AUTHORING = SKILL_DIR / "references/lilo-authoring.md"
TEMPORAL = SKILL_DIR / "references/lilo-temporal-semantics.md"
DOCS_URL = "https://docs.imiron.io/v/0.5.10/en/index.html"


class FormalSpecsLiloSkillContractTests(unittest.TestCase):
    def read_required(self, path: Path) -> str:
        self.assertTrue(path.is_file(), f"missing required file: {path}")
        return path.read_text(encoding="utf-8")

    def test_required_skill_files_exist(self) -> None:
        for path in (SKILL, OPENAI_YAML, DECOMPOSITION, AUTHORING, TEMPORAL):
            with self.subTest(path=path):
                self.assertTrue(path.is_file(), f"missing required file: {path}")

    def test_skill_metadata_is_discoverable(self) -> None:
        text = self.read_required(SKILL)
        self.assertIn("name: formal-specs-lilo", text)
        self.assertIn("description: Use when", text)
        for phrase in (
            "natural-language requirements",
            "SpecForge",
            "Lilo",
            "existing",
            "new",
        ):
            self.assertIn(phrase, text)

    def test_skill_has_existing_and_new_system_branches(self) -> None:
        text = self.read_required(SKILL)
        for phrase in (
            "Existing-system mode",
            "New-system mode",
            "Inspect before editing",
            "Reuse",
            "specforge.toml",
        ):
            self.assertIn(phrase, text)

    def test_skill_stops_before_editing_on_ambiguity(self) -> None:
        text = self.read_required(SKILL)
        self.assertIn("Ambiguity gate", text)
        self.assertIn("Do not edit", text)
        self.assertIn("Ask one focused question", text)
        self.assertIn("Do not invent", text)

    def test_skill_applies_changes_directly_after_clarification(self) -> None:
        text = self.read_required(SKILL)
        self.assertIn("Edit the project files directly", text)
        self.assertIn("after all material ambiguities are resolved", text)

    def test_validation_is_syntax_only(self) -> None:
        text = self.read_required(SKILL) + self.read_required(AUTHORING)
        self.assertIn("Syntax validation only", text)
        self.assertIn("already-running SpecForge server", text)
        self.assertIn("`specforge parse`", text)
        self.assertIn("Do not start a server", text)
        self.assertIn("Do not run type checking", text)
        for command in (
            "`specforge check",
            "`specforge analyze",
            "`specforge monitor",
        ):
            self.assertNotIn(command, text)

    def test_decomposition_uses_fret_fields_without_emitting_fretish(self) -> None:
        text = self.read_required(DECOMPOSITION)
        for phrase in (
            "scope",
            "condition",
            "responsible component",
            "timing",
            "response",
            "atomic obligation",
            "observability",
        ):
            self.assertIn(phrase, text)
        self.assertIn("Do not emit FRETish", text)

    def test_lilo_references_keep_authoritative_versioned_url(self) -> None:
        skill = self.read_required(SKILL)
        authoring = self.read_required(AUTHORING)
        temporal = self.read_required(TEMPORAL)
        for text in (skill, authoring, temporal):
            self.assertIn(DOCS_URL, text)
        self.assertIn("Do not guess", skill)

    def test_authoring_documents_approved_unit_bearing_param_defaults(
        self,
    ) -> None:
        text = " ".join(self.read_required(AUTHORING).split())
        for phrase in (
            "`specforge doc lilo-additional-features`",
            "`#[default = 1.0<m>]`",
            "`param min_water_level: Float<m>`",
            "only when the user supplied or approved",
        ):
            self.assertIn(phrase, text)

    def test_skill_does_not_fall_back_when_requested_system_is_missing(
        self,
    ) -> None:
        text = " ".join(self.read_required(SKILL).split())
        for phrase in (
            "cannot be located",
            "ask for the path or correct name",
            "Do not fall back to new-system mode",
        ):
            self.assertIn(phrase, text)

    def test_skill_handles_unsupported_constructs_and_existing_work(
        self,
    ) -> None:
        text = " ".join(self.read_required(SKILL).split())
        for phrase in (
            "unsupported or undocumented",
            "ask for a reformulation",
            "existing dirty files",
            "unrelated diagnostics",
            "introduced parse errors",
        ):
            self.assertIn(phrase, text)

    def test_temporal_reference_covers_required_distinctions(self) -> None:
        text = self.read_required(TEMPORAL)
        for phrase in (
            "state condition",
            "event trigger",
            "bounded",
            "unbounded",
            "elapsed time",
            "sample",
            "future-time",
            "past-time",
            "vacuity",
        ):
            self.assertIn(phrase, text)

    def test_openai_metadata_matches_skill(self) -> None:
        text = self.read_required(OPENAI_YAML)
        self.assertIn('display_name: "Formal Specs Lilo"', text)
        self.assertIn(
            'short_description: "Formalize natural-language requirements in Lilo"',
            text,
        )
        self.assertIn("$formal-specs-lilo", text)


if __name__ == "__main__":
    unittest.main()
