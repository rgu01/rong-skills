from pathlib import Path
import unittest


ROOT = Path(__file__).parents[1]
SKILL_DIR = ROOT / "skills/formal-specs-lilo"
SKILL = SKILL_DIR / "SKILL.md"
OPENAI_YAML = SKILL_DIR / "agents/openai.yaml"
DECOMPOSITION = SKILL_DIR / "references/requirement-decomposition.md"
AUTHORING = SKILL_DIR / "references/lilo-authoring.md"
TEMPORAL = SKILL_DIR / "references/lilo-temporal-semantics.md"
PATTERNS = SKILL_DIR / "references/lilo-temporal-patterns.md"
DOCS_URL = "https://docs.imiron.io/v/0.5.10/en/index.html"


class FormalSpecsLiloSkillContractTests(unittest.TestCase):
    def read_required(self, path: Path) -> str:
        self.assertTrue(path.is_file(), f"missing required file: {path}")
        return path.read_text(encoding="utf-8")

    def test_required_skill_files_exist(self) -> None:
        for path in (
            SKILL,
            OPENAI_YAML,
            DECOMPOSITION,
            AUTHORING,
            TEMPORAL,
            PATTERNS,
        ):
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

    def test_skill_routes_temporal_requirements_to_both_references(self) -> None:
        text = " ".join(self.read_required(SKILL).split())
        self.assertIn("references/lilo-temporal-semantics.md", text)
        self.assertIn("references/lilo-temporal-patterns.md", text)
        self.assertIn("for temporal requirements, also read", text)

    def test_temporal_references_keep_authoritative_versioned_url(self) -> None:
        self.assertIn(DOCS_URL, self.read_required(PATTERNS))

    def test_temporal_semantics_inventories_every_documented_family(self) -> None:
        text = self.read_required(TEMPORAL)
        for operator in (
            "always",
            "eventually",
            "historically",
            "past",
            "until",
            "since",
            "releases",
            "will_change",
            "did_change",
            "next",
            "previous",
            "max_future",
            "min_future",
            "max_past",
            "min_past",
        ):
            with self.subTest(operator=operator):
                self.assertIn(f"`{operator}", text)

    def test_temporal_semantics_records_exact_distinctions(self) -> None:
        text = " ".join(self.read_required(TEMPORAL).split())
        for phrase in (
            "inclusive",
            "witness",
            "vacuously true",
            "one sample index",
            "`[0, b]`",
            "two distinct supported samples",
            "`p && !(previous p)`",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_temporal_semantics_rejects_undocumented_forms(self) -> None:
        text = self.read_required(TEMPORAL)
        self.assertIn("next_with", text)
        self.assertIn("previous_with", text)
        self.assertIn("not documented", text)

    def test_pattern_catalog_uses_standard_entry_fields(self) -> None:
        text = self.read_required(PATTERNS)
        for field in (
            "Natural language",
            "Clarify",
            "Safe Lilo",
            "Reading",
            "Mistranslation",
        ):
            with self.subTest(field=field):
                self.assertIn(field, text)

    def test_pattern_catalog_covers_required_families(self) -> None:
        text = self.read_required(PATTERNS)
        for heading in (
            "Invariant",
            "Bounded eventual response",
            "Bounded history",
            "Occurrence in the past",
            "Strong until",
            "Since",
            "Releases",
            "One-sample movement",
            "Value variation",
            "Explicit point transition",
            "Rolling extrema",
            "Nested temporal operators",
        ):
            with self.subTest(heading=heading):
                self.assertIn(heading, text)

    def test_pattern_catalog_maps_representative_safe_forms(self) -> None:
        text = " ".join(self.read_required(PATTERNS).split())
        for form in (
            "`always p`",
            "`eventually [0, b] p`",
            "`historically [0, b] p`",
            "`past [0, b] p`",
            "`p until [0, b] q`",
            "`p since [0, b] q`",
            "`p releases [0, b] q`",
            "`next x`",
            "`will_change [0, b] x`",
            "`did_change [0, b] x`",
            "`p && !(previous p)`",
            "`max_past [0, b] x`",
            "`min_future [0, b] x`",
            "`always (p => eventually [0, b] q)`",
        ):
            with self.subTest(form=form):
                self.assertIn(form, text)

    def test_pattern_catalog_warns_about_mistranslations(self) -> None:
        text = " ".join(self.read_required(PATTERNS).split())
        for phrase in (
            "not a point transition",
            "elapsed time",
            "sample movement",
            "vacuous",
            "first sample",
            "`[0, b]`",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_temporal_references_author_no_undocumented_syntax(self) -> None:
        for path in (TEMPORAL, PATTERNS):
            text = self.read_required(path)
            with self.subTest(path=path):
                self.assertNotIn("next_with [", text)
                self.assertNotIn("previous_with [", text)
                self.assertNotIn("always (0,", text)
                self.assertNotIn("eventually (0,", text)
                self.assertNotIn("max_future [1,", text)
                self.assertNotIn("min_past [1,", text)

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
