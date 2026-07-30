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
EXPRESSIONS = SKILL_DIR / "references/lilo-expressions.md"
DECLARATIONS = SKILL_DIR / "references/lilo-declarations.md"
MODCOMP = SKILL_DIR / "references/lilo-modules-components.md"
ATTRIBUTES = SKILL_DIR / "references/lilo-attributes.md"
STATIC_ANALYSIS = SKILL_DIR / "references/lilo-static-analysis.md"
CONVENTIONS = SKILL_DIR / "references/lilo-conventions.md"
NEW_REFS = (
    EXPRESSIONS,
    DECLARATIONS,
    MODCOMP,
    ATTRIBUTES,
    STATIC_ANALYSIS,
    CONVENTIONS,
)
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
        ) + NEW_REFS:
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
        text = " ".join(self.read_required(ATTRIBUTES).split())
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
        self.assertIn("any temporal requirement", text)

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

    def flat(self, path: Path) -> str:
        return " ".join(self.read_required(path).split())

    def assert_all_in(self, path: Path, phrases) -> None:
        text = self.flat(path)
        for phrase in phrases:
            with self.subTest(path=path.name, phrase=phrase):
                self.assertIn(phrase, text)

    def test_every_reference_names_its_authority(self) -> None:
        expected = {
            EXPRESSIONS: "`specforge doc lilo-language`",
            DECLARATIONS: "`specforge doc lilo-systems`",
            MODCOMP: "`specforge doc lilo-modules`",
            ATTRIBUTES: "`specforge doc lilo-additional-features`",
            STATIC_ANALYSIS: "`specforge doc lilo-static-analysis`",
            CONVENTIONS: "`specforge doc conventions`",
        }
        for path, topic in expected.items():
            with self.subTest(path=path.name):
                text = self.flat(path)
                self.assertIn(DOCS_URL, text)
                self.assertIn(topic, text)

    def test_expressions_cover_types_units_and_operators(self) -> None:
        self.assert_all_in(EXPRESSIONS, (
            "`Bool`", "`Int`", "`Float`", "`String`",
            "`///`", "`//`", "`/*",
            "`1.0<cm>`", "`100.0<km/h>`", "`60.0<1/s>`",
            "`9.81<m*s^-2>`", "`1.0<1/(kg*m)>`",
            "`m/s*kg`", "`(m/s)*kg`",
            "`unit km`",
            "no relation",
            "`1000.0<m/km>`",
            "`0 < x <= 10`",
            "`-(-x)`",
        ))

    def test_expressions_cover_builtins(self) -> None:
        self.assert_all_in(EXPRESSIONS, (
            "`float`", "`time`", "`sqrt`", "`abs`",
            "`max(x, y)`", "`min(x, y)`",
            "dimensionless",
            "units are preserved",
        ))

    def test_expressions_cover_conditionals_and_cases(self) -> None:
        self.assert_all_in(EXPRESSIONS, (
            "`if`", "`then`", "`else`",
            "mandatory",
            "pointwise",
            "`cases {`",
            "all branches",
            "exhaustive",
            "disjoint",
        ))

    def test_expressions_cover_records_enums_and_bindings(self) -> None:
        self.assert_all_in(EXPRESSIONS, (
            "structurally typed",
            "`{ foo = 42, bar = \"hello\" }`",
            "`{ foo }`",
            "`{ status.throttle = 0, status.fault = false }`",
            "`{ base with status.throttle = 70 }`",
            "must already exist",
            "`p.x`",
            "`c.center.x`",
            "`enum Color = #Red | #Green | #Blue`",
            "`#Color::Red`",
            "`match`",
            "`let name = expression1; expression2`",
        ))

    def test_declarations_cover_every_keyword_with_syntax(self) -> None:
        self.assert_all_in(DECLARATIONS, (
            "`system Engine`",
            "match the file name",
            "`type Point = { x: Float, y: Float }`",
            "`signal x: Float`",
            "`param temp_threshold: Float`",
            "`def foo: Int = 42`",
            "`def foo(x: Float) = x + 42`",
            "`def foo(x: Float): Float = x + 42`",
            "function types",
            "cannot have parameters",
            "`assumption`",
            "circular",
        ))

    def test_modules_and_components_cover_imports_and_access(self) -> None:
        self.assert_all_in(MODCOMP, (
            "`specforge doc lilo-components`",
            "`module Util`",
            "`pub`",
            "`import Util`",
            "`import Util as U`",
            "`import Util use { calc }`",
            "`import Units use { unit m, unit s }`",
            "`Util::calc(x)`",
            "`component cell1: BatteryCell`",
            "lifted",
            "mapped",
            "`cell1::voltage`",
            "`battery::cell1::voltage`",
            "always public",
            "`specforge schema`",
            "`--diff`",
        ))

    def test_modules_reference_separates_scope_from_projection(self) -> None:
        text = self.flat(MODCOMP)
        self.assertIn("record projection", text)
        self.assertIn("`gps.lat`", text)
        self.assertIn("`battery::level`", text)

    def test_attributes_cover_every_documented_attribute(self) -> None:
        self.assert_all_in(ATTRIBUTES, (
            "immediately precede",
            "`#[label(\"safety\", \"critical\")]`",
            "`#[alias(en = ",
            "`#[field(priority = 1, reviewed = true, owner = \"ops\")]`",
            "scalar",
            "`#[default = 25.0]`",
            "`#[disable(unused)]`",
            "`#[disable(satisfiability)]`",
            "`#[disable(redundancy)]`",
            "`#[timeout(10)]`",
            "`#[timeout(satisfiability = 20, redundancy = 30)]`",
            "`#[rigidity = \"soft\"]`",
            "`null`",
        ))

    def test_attributes_document_spec_stubs(self) -> None:
        self.assert_all_in(ATTRIBUTES, (
            "stub",
            "without a body",
            "interpreted as `true`",
            "`spec error_recovery`",
            "`assumption height_non_negative`",
        ))

    def test_attributes_prefer_documented_timeout_spelling(self) -> None:
        text = self.flat(ATTRIBUTES)
        self.assertIn("`#[timeout = 10.0]`", text)
        self.assertIn("not the documented", text)

    def test_static_analysis_covers_three_checks_without_running_them(
        self,
    ) -> None:
        self.assert_all_in(STATIC_ANALYSIS, (
            "Consistency",
            "Redundancy",
            "Guard",
            "satisfiability",
            "exhaustiveness",
            "disjointness",
            "Do not run",
        ))

    def test_conventions_cover_naming_and_file_names(self) -> None:
        self.assert_all_in(CONVENTIONS, (
            "snake_case",
            "CamelCase",
            "must match the file name",
        ))

    def test_skill_routes_to_every_reference(self) -> None:
        text = self.flat(SKILL)
        for name in (
            "references/lilo-declarations.md",
            "references/lilo-expressions.md",
            "references/lilo-modules-components.md",
            "references/lilo-attributes.md",
            "references/lilo-static-analysis.md",
            "references/lilo-conventions.md",
            "references/lilo-temporal-semantics.md",
            "references/lilo-temporal-patterns.md",
            "references/lilo-authoring.md",
        ):
            with self.subTest(name=name):
                self.assertIn(name, text)

    def test_ambiguity_gate_offers_a_stub_before_refusing(self) -> None:
        text = self.flat(SKILL)
        self.assertIn("stub", text)
        self.assertIn("verifies nothing", text)
        self.assertIn("Do not invent", text)

    def test_no_rule_is_duplicated_across_references(self) -> None:
        naming = self.flat(AUTHORING)
        self.assertNotIn("snake_case", naming)
        self.assertNotIn("#[default", naming)

    def test_references_author_no_undocumented_syntax(self) -> None:
        for path in NEW_REFS:
            text = self.read_required(path)
            with self.subTest(path=path.name):
                self.assertNotIn("next_with", text)
                self.assertNotIn("previous_with", text)

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
