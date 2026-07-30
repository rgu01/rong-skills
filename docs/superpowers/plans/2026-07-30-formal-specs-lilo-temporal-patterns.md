# Formal Specs Lilo Temporal Patterns Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Give `formal-specs-lilo` a complete, documented temporal translation
capability by extending `lilo-temporal-semantics.md` to every documented
temporal construct and adding a `lilo-temporal-patterns.md` natural-language
translation catalog, both routed from `SKILL.md`.

**Architecture:** Three-file split. `lilo-temporal-semantics.md` stays the
compact semantic authority (operator inventory, exact readings, boundary and
vacuity behavior). A new `lilo-temporal-patterns.md` is the elicitation-to-Lilo
catalog with a fixed five-field entry shape. `lilo-authoring.md` keeps all
non-temporal syntax. `SKILL.md` step 5 routes temporal requirements to both
temporal references. Contract tests are extended before the references change.

**Tech Stack:** Markdown skill references, Python `unittest` contract tests,
`specforge` 0.5.10 CLI (`specforge doc`, `specforge parse`),
`quick_validate.py` skill validator.

## Global Constraints

- Authoritative reference URL, verbatim, in every temporal reference file:
  `https://docs.imiron.io/v/0.5.10/en/index.html`
- All constructs must be confirmed against `specforge doc lilo-language` and
  `specforge doc semantics`. Confirmed 0.5.10 temporal surface:
  `always`, `eventually`, `historically`, `past`, `until`, `since`,
  `releases`, `will_change`, `did_change`, `next`, `previous`,
  `max_future`, `min_future`, `max_past`, `min_past`.
- `next_with` and `previous_with` are NOT documented in 0.5.10. Never author
  or infer them.
- Intervals are `[a, b]` with `0 <= a <= b`, `b` real or `infinity`; both
  endpoints inclusive. Author no exclusive-interval syntax (no `(`, `)` bounds).
- Sliding-window operators require intervals of the form `[0, b]`.
- `next` and `previous` cannot carry an interval; they move one sample index
  and retain the boundary value at the terminal/initial sample.
- Never imply continuous-time evaluation: every temporal operator intersects
  its interval with the finite sampled-signal support.
- Distinguish elapsed-time bounds from sample movement; distinguish persistent
  state predicates, window variation (`will_change`/`did_change`), and explicit
  sample transitions (`p && !previous p`).
- Do not copy general Lilo syntax into the temporal references, do not change
  the syntax-only validation boundary, do not modify
  `experiments/specforge-examples`, and add no project-specific domain mappings
  to the catalog. Catalog examples use neutral symbols (`p`, `q`, `x`, `a`, `b`).
- Validation runs no semantic or behavioral SpecForge analyses.

---

## File Structure

- `tests/test_formal_specs_lilo_skill_contract.py` — modify. Add the pattern
  catalog path constant and new contract tests for the catalog, the workflow
  routing, and the extended semantic distinctions.
- `skills/formal-specs-lilo/references/lilo-temporal-semantics.md` — modify.
  Extend the operator table and add sections for endpoint obligations,
  window variation vs. point transition, and sliding windows.
- `skills/formal-specs-lilo/references/lilo-temporal-patterns.md` — create.
  Twelve-entry translation catalog with the fixed five-field entry shape.
- `skills/formal-specs-lilo/SKILL.md` — modify. Step 5 routes temporal
  requirements to both temporal references.

---

### Task 1: Extend the contract test for the pattern catalog and routing

**Files:**
- Modify: `tests/test_formal_specs_lilo_skill_contract.py:1-14` (path
  constants), `:20-23` (required-files test), and append new test methods
  before `test_openai_metadata_matches_skill`.

**Interfaces:**
- Consumes: nothing from earlier tasks.
- Produces: module-level constant `PATTERNS = SKILL_DIR /
  "references/lilo-temporal-patterns.md"` and the helper
  `self.read_required(path) -> str` (already present), used by Tasks 2–4.

- [ ] **Step 1: Write the failing tests**

Add the constant next to the existing ones:

```python
PATTERNS = SKILL_DIR / "references/lilo-temporal-patterns.md"
```

Add `PATTERNS` to the tuple in `test_required_skill_files_exist`:

```python
    def test_required_skill_files_exist(self) -> None:
        for path in (SKILL, OPENAI_YAML, DECOMPOSITION, AUTHORING, TEMPORAL, PATTERNS):
            with self.subTest(path=path):
                self.assertTrue(path.is_file(), f"missing required file: {path}")
```

Append these test methods to `FormalSpecsLiloSkillContractTests`:

```python
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
            "`p && !previous p`",
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
            "`p && !previous p`",
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
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python -m unittest tests.test_formal_specs_lilo_skill_contract -v`
Expected: FAIL — `missing required file: .../lilo-temporal-patterns.md` plus
failures in the routing and semantics-distinction tests.

- [ ] **Step 3: Commit the failing contract**

```bash
git add tests/test_formal_specs_lilo_skill_contract.py
git commit -m "test: contract for Lilo temporal pattern catalog"
```

---

### Task 2: Extend the temporal semantics reference

**Files:**
- Modify: `skills/formal-specs-lilo/references/lilo-temporal-semantics.md`
- Test: `tests/test_formal_specs_lilo_skill_contract.py`

**Interfaces:**
- Consumes: the contract constants and tests from Task 1.
- Produces: the semantic authority the catalog in Task 3 cites; the catalog
  must not restate operator semantics, only reference them.

- [ ] **Step 1: Replace the `## Documented operators` table**

Replace the existing table and the two sentences following it with:

```markdown
| Family | Confirmed form and meaning |
| --- | --- |
| future-time | `always [I] p`, `eventually [I] p`, `p until [I] q`, `p releases [I] q`; an omitted interval means `[0, infinity]`. |
| past-time | `historically [I] p`, `past [I] p`, `p since [I] q`. |
| window variation | `will_change [I] p` and `did_change [I] p` are true when two distinct supported samples inside the interval hold different values of `p`; `p` may be any type with equality, not only `Bool`. |
| discrete | `next x` and `previous x` move by one sample index, not elapsed time, and take no interval; at the terminal/initial boundary respectively they retain the boundary value. |
| sliding window | `max_future [0, b] x`, `min_future [0, b] x`, `max_past [0, b] x`, `min_past [0, b] x` return the numeric extremum over the window. The interval must start at `0`; `b` may be `infinity`. |
| not documented in 0.5.10 | `next_with` and `previous_with` have no syntax or semantics in the authoritative 0.5.10 language or semantics pages. Do not author or infer forms for them. |

`releases` is the dual of `until`; `historically`, `past`, and `since` are the
past-time counterparts of `always`, `eventually`, and `until`.

## Endpoint obligations

`p until [I] q` requires a supported witness `t'` for `q` inside `t + I`, and
`p` at every supported sample `t''` with `t <= t'' < t'`: the witness sample
itself is excluded, so `p` need not hold there. `p since [I] q` requires a
supported witness `t'` for `q` inside `t - I` and `p` at every supported sample
`t''` with `t' < t'' <= t`, again excluding the witness sample. When no
supported sample lies between the evaluation point and the witness, neither
form constrains `p` at all. `p releases [I] q` is exactly `!(!p until [I] !q)`
and inherits these obligations through that expansion.

## Window variation versus point transition

`will_change` and `did_change` observe variation across a window: two distinct
supported samples with different values anywhere in the interval. They do not
locate the change, do not give its direction, and are false whenever the
interval intersects the support in one sample or none. An explicit rising
transition at the current sample is `p && !previous p`; a falling transition is
`!p && previous p`. Because `previous p` retains the boundary value at sample
index `0`, no transition is ever detected at the first sample of a signal.

## Sliding-window restriction

Author sliding windows only as `[0, b]`. Because the window always contains the
evaluation point, the intersection with the support is never empty, and a
singleton window returns the value of the operand at the evaluation point
itself. These operators return a numeric value, not a Boolean; compare them to
obtain a property, as in `max_past [0, b] x <= limit`.
```

- [ ] **Step 2: Run the semantics contract tests**

Run: `python -m unittest tests.test_formal_specs_lilo_skill_contract -v -k temporal_semantics`
Expected: PASS for
`test_temporal_semantics_inventories_every_documented_family`,
`test_temporal_semantics_records_exact_distinctions`, and
`test_temporal_semantics_rejects_undocumented_forms`.

- [ ] **Step 3: Commit**

```bash
git add skills/formal-specs-lilo/references/lilo-temporal-semantics.md
git commit -m "docs: cover every documented Lilo temporal construct"
```

---

### Task 3: Create the temporal pattern catalog

**Files:**
- Create: `skills/formal-specs-lilo/references/lilo-temporal-patterns.md`
- Test: `tests/test_formal_specs_lilo_skill_contract.py`

**Interfaces:**
- Consumes: the semantics reference from Task 2 (linked, not restated) and the
  contract tests from Task 1.
- Produces: twelve catalog entries, each with the literal field labels
  `Natural language`, `Clarify`, `Safe Lilo`, `Reading`, `Mistranslation`.

- [ ] **Step 1: Write the catalog**

Write the file with a header stating the authoritative URL
`https://docs.imiron.io/v/0.5.10/en/index.html`, a rule that an entry is
reusable only when every `Clarify` field matches the user requirement, and
twelve `###` entries in this order, each using the five field labels above:

1. `Invariant` — "shall always hold" → `always p`.
2. `Bounded eventual response` — "within b time units" →
   `eventually [0, b] p`, and the guarded form under entry 12.
3. `Bounded history` — "has held throughout the last b time units" →
   `historically [0, b] p`.
4. `Occurrence in the past` — "has happened at some point in the last b" →
   `past [0, b] p`.
5. `Strong until` — "stays p until q" → `p until [0, b] q`.
6. `Since` — "has been p ever since q" → `p since [0, b] q`.
7. `Releases` — "p may stop only once q has been released" →
   `p releases [0, b] q`, expanding to `!(!p until [0, b] !q)`.
8. `One-sample movement` — "on the next cycle" → `next x`, with `previous x`
   for the backward direction.
9. `Value variation` — "the value changes during the window" →
   `will_change [0, b] x` and `did_change [0, b] x`.
10. `Explicit point transition` — "when it becomes true" →
    `p && !previous p`.
11. `Rolling extrema` — "the peak/lowest value over the window" →
    `max_past [0, b] x` and `min_future [0, b] x`, always compared to a bound.
12. `Nested temporal operators` — "whenever p, then q within b" →
    `always (p => eventually [0, b] q)`.

Each `Clarify` field lists the fields that must be confirmed before use — at
minimum the unit and numeric value of `b`, whether the bound is elapsed time or
sample movement, whether a witness is required in a finite trace, and whether
the trigger is a persistent state condition or a point transition. Each
`Mistranslation` field names one concrete failure, covering at least: window
variation is `not a point transition`; a `sample movement` bound written as
`elapsed time` (and the reverse); an implication whose antecedent is never true
is `vacuous`; `previous` at the `first sample` detects no transition; a sliding
window written with a non-zero lower bound instead of `[0, b]`; and an
`always`/`historically` obligation that is vacuously satisfied when the
interval misses the support. Use only neutral symbols `p`, `q`, `x`, `a`, `b`.

- [ ] **Step 2: Run the catalog contract tests**

Run: `python -m unittest tests.test_formal_specs_lilo_skill_contract -v -k pattern_catalog`
Expected: PASS for all four `pattern_catalog` tests.

- [ ] **Step 3: Commit**

```bash
git add skills/formal-specs-lilo/references/lilo-temporal-patterns.md
git commit -m "docs: add Lilo temporal translation pattern catalog"
```

---

### Task 4: Route the workflow and validate the whole skill

**Files:**
- Modify: `skills/formal-specs-lilo/SKILL.md:23`
- Test: `tests/test_formal_specs_lilo_skill_contract.py`,
  `tests/test_formal_specs_lilo_readme.py`

**Interfaces:**
- Consumes: both temporal references from Tasks 2–3.
- Produces: the final routing sentence read by every temporal requirement run.

- [ ] **Step 1: Rewrite workflow step 5**

Replace line 23 of `SKILL.md` with:

```markdown
5. Read [lilo-authoring.md](references/lilo-authoring.md) before authoring; for temporal requirements, also read both [lilo-temporal-semantics.md](references/lilo-temporal-semantics.md) and [lilo-temporal-patterns.md](references/lilo-temporal-patterns.md).
```

- [ ] **Step 2: Run the full contract suite**

Run: `python -m unittest discover -s tests -v`
Expected: PASS, all tests.

- [ ] **Step 3: Run the skill validator**

Run:
```bash
python /home/rogu/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/formal-specs-lilo
```
Expected: validation success for `formal-specs-lilo`.

- [ ] **Step 4: Scan for undocumented interval and `_with` syntax**

Run:
```bash
grep -nE '_with|(always|eventually|historically|past|until|since|releases|will_change|did_change)[[:space:]]*\(' skills/formal-specs-lilo/references/lilo-temporal-*.md
grep -nE '(max|min)_(future|past)[[:space:]]*\[[^0]' skills/formal-specs-lilo/references/lilo-temporal-*.md
```
Expected: `_with` appears only in the "not documented in 0.5.10" prohibition
lines; no exclusive-interval bound and no non-zero sliding-window lower bound.

- [ ] **Step 5: Parse the catalog's Lilo expressions**

Build a throwaway SpecForge project in the scratchpad that declares neutral
signals and params and wraps each catalog expression in a `spec`, then parse it.
This is syntax validation only — no type checking, no analyses.

```bash
SCRATCH=/tmp/claude-1000/-home-rogu-projects-rong-skills/8f2932e2-3794-46f1-8f5f-478a84459b26/scratchpad/lilo-patterns
mkdir -p "$SCRATCH/src"
printf '[project]\nname = "patterns"\nsource = "src/"\n' > "$SCRATCH/specforge.toml"
cat > "$SCRATCH/src/patterns.lilo" <<'LILO'
system patterns

signal p: Bool
signal q: Bool
signal x: Float
param b: Float
param limit: Float

spec invariant = always p
spec bounded_response = eventually [0, 5.0] p
spec bounded_history = historically [0, 5.0] p
spec occurred = past [0, 5.0] p
spec strong_until = p until [0, 5.0] q
spec since_q = p since [0, 5.0] q
spec releases_q = p releases [0, 5.0] q
spec next_sample = next p
spec prev_sample = previous p
spec varies = will_change [0, 5.0] x
spec varied = did_change [0, 5.0] x
spec rising = p && !(previous p)
spec falling = !p && previous p
spec rolling_max = max_past [0, 5.0] x <= limit
spec rolling_min = min_future [0, 5.0] x >= limit
spec guarded = always (p => eventually [0, 5.0] q)
LILO
cd "$SCRATCH" && specforge parse
```

Expected: parsing reports no errors. If a form fails to parse, correct the
catalog entry to the documented form and rerun this step before committing.

- [ ] **Step 6: Commit**

```bash
git add skills/formal-specs-lilo/SKILL.md
git commit -m "feat: route temporal requirements through the pattern catalog"
```

---

## Self-Review

**Spec coverage:** Goal → Tasks 2–3. Reference responsibilities → Task 2
(semantics inventory, endpoint obligations, witness/vacuity, discrete
boundaries, window variation, numeric aggregates and their interval
restriction, undocumented `_with`) and Task 3 (five-field entries, all twelve
families, neutral symbols). `lilo-authoring.md` untouched. Workflow routing →
Task 4 Step 1; the ambiguity gate is unchanged by construction. Correctness
constraints → Global Constraints, enforced by Task 1's tests and Task 4's
scans. Validation items 1–4 → Task 4 Steps 2–5. Scope exclusions → Global
Constraints.

**Placeholders:** none — every step gives the literal text, command, or
expected output.

**Type consistency:** `PATTERNS` is defined once in Task 1 and used unchanged
in Tasks 2–4; the five field labels and the twelve heading strings are
identical in Task 1's assertions and Task 3's entry list; the safe-form strings
asserted in Task 1 match those written in Task 3 and parsed in Task 4 Step 5.
