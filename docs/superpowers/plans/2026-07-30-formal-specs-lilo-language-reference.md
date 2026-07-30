# Formal Specs Lilo Language Reference Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extend `formal-specs-lilo` to cover all eight sub-pages of chapter 5
(Lilo Language) of the SpecForge 0.5.10 user guide, via six new condensed
references plus a narrowed `lilo-authoring.md` and a routing map in `SKILL.md`.

**Architecture:** Hybrid retrieval. Each reference is condensed and
authoring-oriented, sufficient for authoring on its own, and names the single
`specforge doc <topic>` page that is authoritative for its content. One rule
lives in exactly one file. `SKILL.md` routes by what the requirement needs so
an agent reads only relevant references. Contract tests are written first and
define the required content precisely.

**Tech Stack:** Markdown skill references, Python `unittest` contract tests,
`specforge` 0.5.10 CLI (`specforge doc`, `specforge parse`),
`quick_validate.py` skill validator.

## Global Constraints

- Authoritative URL, verbatim, in every reference:
  `https://docs.imiron.io/v/0.5.10/en/index.html`
- Every reference names its owning topic as `` `specforge doc <topic>` ``.
- Author only constructs confirmed on the owning page. Where the example
  submodule diverges, the manual wins and the divergence is recorded as a trap.
  Known case: `Energy.lilo` writes `#[timeout = 10.0]`; the documented forms
  are `#[timeout(10)]` and `#[timeout(satisfiability = 20, redundancy = 30)]`.
- `::` is module/component access; `.` is record projection. Never conflate.
- Prefix operators cannot be chained: write `!(previous p)` and `-(-x)`.
- Interval endpoints inclusive; sliding windows only `[0, b]`.
- Conditionals: `else` is mandatory, branches must have compatible types,
  `if/then/else` is pointwise. `cases` requires all branches `Bool`.
- Static analyses are diagnostics to recognize, never steps the skill runs. The
  syntax-only validation boundary does not change.
- One rule, one file: no syntax statement duplicated across references.
- Do not modify `experiments/specforge-examples`.
- Do not add project-specific domain vocabulary to any reference.
- No semantic or behavioral SpecForge analyses during validation.

---

## File Structure

- `tests/test_formal_specs_lilo_skill_contract.py` — modify. Add six path
  constants and the contract tests that define required content.
- `skills/formal-specs-lilo/references/lilo-expressions.md` — create (5.1).
- `skills/formal-specs-lilo/references/lilo-declarations.md` — create (5.2).
- `skills/formal-specs-lilo/references/lilo-modules-components.md` — create
  (5.3, 5.4).
- `skills/formal-specs-lilo/references/lilo-attributes.md` — create (5.6).
- `skills/formal-specs-lilo/references/lilo-static-analysis.md` — create (5.5).
- `skills/formal-specs-lilo/references/lilo-conventions.md` — create (5.7).
- `skills/formal-specs-lilo/references/lilo-authoring.md` — modify. Narrow to
  process; remove the naming section (→ conventions) and the parameter-defaults
  section (→ attributes).
- `skills/formal-specs-lilo/SKILL.md` — modify. Reference map + ambiguity-gate
  stub amendment.
- Unchanged: `lilo-temporal-semantics.md`, `lilo-temporal-patterns.md`,
  `requirement-decomposition.md`, `agents/openai.yaml`.

---

### Task 1: Contract tests defining required content

**Files:**
- Modify: `tests/test_formal_specs_lilo_skill_contract.py` — add constants
  after line 12, extend `test_required_skill_files_exist`, and append new test
  methods before `test_openai_metadata_matches_skill`.

**Interfaces:**
- Consumes: existing `read_required(path)` helper and `DOCS_URL`.
- Produces: constants `EXPRESSIONS`, `DECLARATIONS`, `MODCOMP`, `ATTRIBUTES`,
  `STATIC_ANALYSIS`, `CONVENTIONS`, and the module-level tuple `NEW_REFS`,
  used by Tasks 2–9.

- [ ] **Step 1: Add path constants**

```python
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
```

- [ ] **Step 2: Extend the required-files test**

Replace the tuple in `test_required_skill_files_exist` with:

```python
        for path in (
            SKILL,
            OPENAI_YAML,
            DECOMPOSITION,
            AUTHORING,
            TEMPORAL,
            PATTERNS,
        ) + NEW_REFS:
```

- [ ] **Step 3: Write the failing tests**

Append these methods to `FormalSpecsLiloSkillContractTests`:

```python
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
```

- [ ] **Step 4: Run the tests to verify they fail**

Run: `python -m unittest tests.test_formal_specs_lilo_skill_contract -v`
Expected: FAIL — `missing required file` for all six new references, plus
failures in the routing, gate, and dedup tests.

- [ ] **Step 5: Commit**

```bash
git add tests/test_formal_specs_lilo_skill_contract.py
git commit -m "test: contract for full Lilo language reference coverage"
```

---

### Task 2: `lilo-expressions.md` (chapter 5.1)

**Files:**
- Create: `skills/formal-specs-lilo/references/lilo-expressions.md`
- Test: `tests/test_formal_specs_lilo_skill_contract.py`

**Interfaces:**
- Consumes: Task 1's `EXPRESSIONS` constant and its four assertion sets, which
  define the required content.
- Produces: the expression authority cited by Tasks 3–8; those files must not
  restate any expression rule.

- [ ] **Step 1: Write the file**

Head it with the authoritative URL and `` `specforge doc lilo-language` `` as
the owning page. Consult that page for anything the sections below leave open.
Write these sections, in order:

1. **Comments** — `/* … */` blocks, `//` lines, `///` docstrings.
2. **Primitive types** — `Bool` (`true`/`false`), `Int`, `Float`, `String`
   (double-quoted). Note `Int` and `Float` do not mix: `x + n` with
   `x: Float`, `n: Int` is a type error; convert with `float(n)`.
3. **Units of measure** — angle brackets immediately after a literal
   (`1.0<cm>`, `100.0<km/h>`); compound units with `/`, `*`, `^` and the
   dimensionless `1` (`60.0<1/s>`, `9.81<m*s^-2>`); precedence — `^` binds
   tightest, then `*` and `/` equal and left-associative, so `m/s*kg` is
   `(m/s)*kg` and `m*s^-2` is `m*(s^-2)`; parenthesized grouping
   (`1.0<1/(kg*m)>`); `+`, `-` and comparison require identical units while
   `*` and `/` combine them; units are inferred; units are identified as
   strings so `m` and `km` have **no relation** and need an explicit
   conversion (`kilometre * 1000.0<m/km>`); units used in annotations must be
   declared with `unit km`.
4. **Operator precedence** — the documented ladder from highest: prefix `-`
   and `!`; `*` `/`; `+` `-`; comparisons; temporal operators; `&&`; `||`;
   `=>` and `<=>`. Comparisons chain in a consistent direction
   (`0 < x <= 10` means `0 < x && x <= 10`). Prefix operators cannot chain:
   write `-(-x)` and `!(next p)`.
5. **Built-in functions** — `float` (`Int` → `Float`), `time` (current time of
   the signal), `sqrt` (`Int` or **dimensionless** `Float`), `abs` (**units
   are preserved**), `max(x, y)` and `min(x, y)` (two or more arguments, all
   the same type and units). Add a trap: `max`/`min` are pointwise over two
   values; the rolling-window extrema are `max_past`/`min_future` and live in
   the temporal references.
6. **Conditional expressions** — `if c then a else b` is an expression, so
   `else` is **mandatory** and the branches must have compatible types; the
   condition must be `Bool`; conditionals nest; evaluation is **pointwise**.
7. **Case expressions** — `cases {` guard `-> consequence;` … `}` requires
   **all branches** `Bool` and desugars to a conjunction of implications; a
   `-> true` branch may be omitted; prefer **exhaustive** and **disjoint**
   guards. Cross-reference `lilo-static-analysis.md` for guard analysis.
8. **Records** — anonymous, **structurally typed**, extensible. Construction
   `{ foo = 42, bar = "hello" }` with field order irrelevant; named types via
   `type`; punning `{ foo }` for `{ foo = foo }`; dotted-path construction
   `{ status.throttle = 0, status.fault = false }`, which **cannot** be
   combined with punning; updates `{ base with status.throttle = 70 }`, where
   all updated fields **must already exist**; projection `p.x`, chained as
   `c.center.x`.
9. **Enum types** — nominal, no payload:
   `enum Color = #Red | #Green | #Blue`. Constructors start with `#`, enums
   form their own namespaces and are open, constructor names may be shared
   across enums, and references may be bare or qualified (`#Red`,
   `#Color::Red`, `#Utils::Color::Red`). Equality is supported.
10. **Pattern matching** — `match` over enums only, exhaustive cases,
    `#Red -> false;` form; qualified constructors disambiguate shared names.
11. **Local bindings** — `let name = expression1; expression2`; the binding is
    visible only in `expression2`; bindings chain; types are inferred.

- [ ] **Step 2: Run the expression tests**

Run: `python -m unittest tests.test_formal_specs_lilo_skill_contract -v -k expressions`
Expected: PASS for all four `expressions` tests.

- [ ] **Step 3: Commit**

```bash
git add skills/formal-specs-lilo/references/lilo-expressions.md
git commit -m "docs: add Lilo expression and type reference"
```

---

### Task 3: `lilo-declarations.md` (chapter 5.2)

**Files:**
- Create: `skills/formal-specs-lilo/references/lilo-declarations.md`
- Test: `tests/test_formal_specs_lilo_skill_contract.py`

**Interfaces:**
- Consumes: `DECLARATIONS` and `test_declarations_cover_every_keyword_with_syntax`.
- Produces: the declaration-syntax authority; `lilo-authoring.md` keeps only
  the reuse policy and must link here for syntax.

- [ ] **Step 1: Write the file**

Head it with the authoritative URL and `` `specforge doc lilo-systems` ``.
Give every declaration a syntax line and a minimal example — the current skill
has none, which is the gap this file closes. Sections:

1. **System header** — a system file starts with `system Engine`; the name
   must **match the file name**. Note that the example submodule's
   `temperature_sensor.lilo` omits the header and takes its system name from
   the file name, so an absent header is not a defect to repair.
2. **`type`** — `type Point = { x: Float, y: Float }`, usable as a type
   anywhere in the file.
3. **`signal`** — `signal x: Float`. Time-varying input. Any type that
   contains no **function types**, i.e. primitives and records.
4. **`param`** — `param temp_threshold: Float`. Constant over time. Must be
   supplied before monitoring; optional for exemplification, where the solver
   may choose a conforming value.
5. **`def`** — all documented shapes: `def foo: Int = 42`;
   `def foo(x: Float) = x + 42`; `def foo(x: Float): Float = x + 42`.
   Annotations on arguments and return are optional and inferred, but
   recommended as documentation. Arguments may be record-typed
   (`def foo(s: S) = eventually [0,1] s.x > s.y`). Defs may call other defs,
   may be declared in any order, must not be **circular**, and may use the
   system's signals without declaring them as arguments.
6. **`spec`** — like a `def` except the return type is always `Bool` and need
   not be written, and specs **cannot have parameters**. Show the documented
   example building a spec from two defs. Point to `lilo-attributes.md` for
   the stub form and to the temporal references for temporal bodies. Note the
   documented workaround for a family of related obligations: a parameterized
   `def` returning `Bool`, conjoined in one `spec`.
7. **`assumption`** — syntactically like a `spec`, but taken as given: it
   constrains exemplification and satisfiability instead of being verified.
   Include the documented `physics` example.

- [ ] **Step 2: Run the declaration test**

Run: `python -m unittest tests.test_formal_specs_lilo_skill_contract -v -k declarations`
Expected: PASS.

- [ ] **Step 3: Commit**

```bash
git add skills/formal-specs-lilo/references/lilo-declarations.md
git commit -m "docs: add Lilo declaration syntax reference"
```

---

### Task 4: `lilo-modules-components.md` (chapters 5.3, 5.4)

**Files:**
- Create: `skills/formal-specs-lilo/references/lilo-modules-components.md`
- Test: `tests/test_formal_specs_lilo_skill_contract.py`

**Interfaces:**
- Consumes: `MODCOMP` and its two assertion sets.
- Produces: the only place `::` semantics are defined.

- [ ] **Step 1: Write the file**

Head it with the authoritative URL and both owning pages —
`` `specforge doc lilo-modules` `` and `` `specforge doc lilo-components` ``.
Sections:

1. **Modules** — `module Util`; the name must match the file name
   (`Util.lilo`); a module may contain **only** `def`s and `type`s; `pub`
   marks what other files may use.
2. **Imports** — all four documented forms: `import Util` with qualified use
   `Util::calc(x)`; `import Util as U` with `U::calc(x)`;
   `import Util use { calc }` for unqualified use; and
   `import Units use { unit m, unit s }`, where each unit is prefixed with the
   `unit` keyword inside the `use` list.
3. **Components** — child systems mark shared declarations `pub signal`,
   `pub param`, `pub def`; specs are **always public**. A parent instantiates
   with `component cell1: BatteryCell`.
4. **Lifted versus mapped** — an unmapped component has all its signals and
   params **lifted** into the parent schema as `cell1::voltage`,
   `cell1::temperature`, `cell1::nominal_voltage`. A mapping block fixes them
   instead, so they leave the schema:

   ```lilo
   component cell2: BatteryCell {
     param nominal_voltage = 3.7
     signal voltage = voltage / 2.0
   }
   ```

   State the consequence: mapped elements are not inputs and must not be
   supplied in data.
5. **Accessing component members** — `::` reaches signals, params, defs, and
   specs of a component, at any depth: `battery::level`,
   `battery::cell1::voltage`, `cell1::voltage_range`.
6. **`::` versus `.`** — `::` crosses a module or component scope; `.` is
   **record projection** within a value. Contrast the documented pair from the
   same example: `battery::level` (component) against `gps.lat` (record).
   These are unrelated operators that look alike.
7. **System schema** — the schema is the set of signals and params forming the
   system's input; mapped elements are excluded. Inspect it with
   `specforge schema`, and compare against a data or param file with
   `--diff`, which reports missing, extra, mismatched, and
   record-versus-scalar fields. Note this is inspection, not analysis, so it
   stays inside the skill's boundary.

- [ ] **Step 2: Run the module and component tests**

Run: `python -m unittest tests.test_formal_specs_lilo_skill_contract -v -k modules`
Expected: PASS for both `modules` tests.

- [ ] **Step 3: Commit**

```bash
git add skills/formal-specs-lilo/references/lilo-modules-components.md
git commit -m "docs: add Lilo module and component reference"
```

---

### Task 5: `lilo-attributes.md` (chapter 5.6)

**Files:**
- Create: `skills/formal-specs-lilo/references/lilo-attributes.md`
- Test: `tests/test_formal_specs_lilo_skill_contract.py`

**Interfaces:**
- Consumes: `ATTRIBUTES` and its three assertion sets.
- Produces: the stub definition that Task 8's ambiguity-gate amendment cites,
  and the `#[default]` content removed from `lilo-authoring.md` in Task 7.

- [ ] **Step 1: Write the file**

Head it with the authoritative URL and
`` `specforge doc lilo-additional-features` ``. Sections:

1. **Attribute shape** — attributes annotate defs, specs, params, and
   signals, and must **immediately precede** the item. The generic form is
   `#[key = "value", fn(arg), flag]`.
2. **Labels** — `#[label("safety", "critical")]`; multiple `#[label]`
   attributes accumulate; colors are configured under `[labels.colors]` in
   `specforge.toml`.
3. **Aliases** — `#[alias(en = "Brake Must Work", ja = "…")]`; aliases name a
   declaration in data files and must be unambiguous against other aliases and
   declaration names.
4. **Custom fields** — `#[field(priority = 1, reviewed = true, owner = "ops")]`;
   values must be **scalar**.
5. **Parameter defaults** — `#[default = 25.0]` immediately before the
   `param`; combine with a unit-bearing literal as `#[default = 1.0<m>]`. A
   default is the expected typical value, **not** a constant declaration — use
   a `def` for constants. Defaults may be omitted when monitoring, are
   substituted on export, and are fixed during exemplification; JSON `null` in
   a config asks SpecForge to ignore the default, and `null` cannot be a
   default inside a Lilo program. Author a default only when the user supplied
   or approved it.
6. **Suppressing diagnostics** — `#[disable(unused)]` for unused defs, params,
   and signals (specs and public defs always count as used);
   `#[disable(satisfiability)]` and `#[disable(redundancy)]` for the static
   analyses.
7. **Analysis timeouts** — `#[timeout(10)]` sets both, and
   `#[timeout(satisfiability = 20, redundancy = 30)]` sets them individually.
   Record the trap: `Energy.lilo` in the example submodule writes
   `#[timeout = 10.0]`, which the generic `#[key = value]` shape accepts but
   which is **not the documented** spelling — author `#[timeout(10)]`.
8. **Soft assumptions** — `#[rigidity = "soft"]` on an `assumption` marks it a
   soft constraint the solver may relax against hard constraints.
9. **Spec stubs** — a `spec` or `assumption` **without a body** is legal, may
   carry a docstring and attributes, and is **interpreted as `true`** by the
   tooling. Show `spec error_recovery` and
   `assumption height_non_negative` with docstrings. State plainly that a stub
   records a requirement and verifies nothing, and cross-reference the
   ambiguity gate in `SKILL.md`.

- [ ] **Step 2: Run the attribute tests**

Run: `python -m unittest tests.test_formal_specs_lilo_skill_contract -v -k attributes`
Expected: PASS for all three `attributes` tests.

- [ ] **Step 3: Commit**

```bash
git add skills/formal-specs-lilo/references/lilo-attributes.md
git commit -m "docs: add Lilo attribute and spec-stub reference"
```

---

### Task 6: `lilo-static-analysis.md` (chapter 5.5)

**Files:**
- Create: `skills/formal-specs-lilo/references/lilo-static-analysis.md`
- Test: `tests/test_formal_specs_lilo_skill_contract.py`

**Interfaces:**
- Consumes: `STATIC_ANALYSIS` and its assertion set.
- Produces: the diagnostic vocabulary that `lilo-attributes.md`'s
  `#[disable(...)]` section and `lilo-expressions.md`'s `cases` section link to.

- [ ] **Step 1: Write the file**

Head it with the authoritative URL and
`` `specforge doc lilo-static-analysis` ``. Open with the boundary statement:
these are diagnostics SpecForge reports, to be recognized and designed
against. **Do not run** them — the skill validates syntax only, per
`lilo-authoring.md`. Sections:

1. **Consistency checking** — a single spec that cannot be satisfied warns
   (`always (x > 0 && x < 0)`); so does a set of individually satisfiable but
   jointly unsatisfiable specs (`always (x > 0)` with `always (x < 0)`).
   Authoring guidance: a fresh requirement that makes an existing spec
   inconsistent is a requirements conflict to raise with the user, not
   something to resolve by weakening an existing spec.
2. **Redundancy checking** — a spec implied by others is reported; use the
   documented three-spec example. Guidance: report the redundancy rather than
   deleting the user's spec, and use `#[disable(redundancy)]` only when the
   user wants the check kept as a standalone statement.
3. **Guard analysis for case expressions** — guards of a `cases` spec are
   checked for **satisfiability**, **exhaustiveness**, and **disjointness**.
   Guidance: prefer guards that are exhaustive and mutually exclusive, which
   is also why `cases` is preferable to hand-written implication chains.
4. **Recognizing versus causing** — distinguish diagnostics that already
   existed from ones introduced by the edit, consistent with the skill's
   existing rule about pre-existing dirty files and unrelated diagnostics.

- [ ] **Step 2: Run the static-analysis test**

Run: `python -m unittest tests.test_formal_specs_lilo_skill_contract -v -k static_analysis`
Expected: PASS.

- [ ] **Step 3: Commit**

```bash
git add skills/formal-specs-lilo/references/lilo-static-analysis.md
git commit -m "docs: add Lilo static-analysis diagnostics reference"
```

---

### Task 7: `lilo-conventions.md` and narrowing `lilo-authoring.md`

**Files:**
- Create: `skills/formal-specs-lilo/references/lilo-conventions.md`
- Modify: `skills/formal-specs-lilo/references/lilo-authoring.md` — remove the
  "Naming, documentation, and edits" naming rules and the whole "Parameter
  defaults" section; keep discovery, the reuse table, edit discipline, and
  syntax validation.
- Test: `tests/test_formal_specs_lilo_skill_contract.py`

**Interfaces:**
- Consumes: `CONVENTIONS`; `lilo-attributes.md` from Task 5, which now owns
  parameter defaults.
- Produces: the deduplicated authoring file asserted by
  `test_no_rule_is_duplicated_across_references`.

- [ ] **Step 1: Write `lilo-conventions.md`**

Head it with the authoritative URL and `` `specforge doc conventions` ``.
State that Lilo itself is flexible and a project's own convention wins, then
record the documented defaults: modules and systems in lowercase snake_case;
signals, params, defs, specs, arguments, and record fields in lowercase
snake_case; types in CamelCase; and the requirement that a module or system
name **must match the file name** it lives in. Add the practical note that the
example submodule uses CamelCase system and signal names (`system Energy`,
`signal Production`) and backtick-quoted identifiers for names with spaces
(`` `Oil and Gas` ``), so matching an existing project overrides the default.

- [ ] **Step 2: Strip the moved rules from `lilo-authoring.md`**

Replace the "Naming, documentation, and edits" section body so it no longer
states snake_case or CamelCase rules, keeping only the edit discipline and a
pointer:

```markdown
## Documentation and edits

Follow the project's own conventions; see
[lilo-conventions.md](lilo-conventions.md) for the documented defaults. Use
`///` docstrings to attach requirement context to declarations. Edit files
directly only after ambiguity resolution; make the smallest coherent change
and preserve unrelated changes.
```

Delete the "Parameter defaults" section entirely and, in the declaration
inventory preamble, point at the new references:

```markdown
For declaration syntax see [lilo-declarations.md](lilo-declarations.md); for
expressions see [lilo-expressions.md](lilo-expressions.md); for attributes and
parameter defaults see [lilo-attributes.md](lilo-attributes.md).
```

- [ ] **Step 3: Run the conventions and dedup tests**

Run: `python -m unittest tests.test_formal_specs_lilo_skill_contract -v -k "conventions or duplicated"`
Expected: PASS for `test_conventions_cover_naming_and_file_names` and
`test_no_rule_is_duplicated_across_references`.

- [ ] **Step 4: Check the moved assertions still hold elsewhere**

The pre-existing `test_authoring_documents_approved_unit_bearing_param_defaults`
asserts the defaults content against `AUTHORING`. Repoint it at `ATTRIBUTES`:

```python
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
```

Ensure `lilo-attributes.md` contains the `` `param min_water_level: Float<m>` ``
example so this passes.

- [ ] **Step 5: Run the full suite**

Run: `python -m unittest discover -s tests`
Expected: PASS except the `SKILL.md` routing and ambiguity-gate tests, which
Task 8 fixes.

- [ ] **Step 6: Commit**

```bash
git add skills/formal-specs-lilo/references/lilo-conventions.md \
        skills/formal-specs-lilo/references/lilo-authoring.md \
        tests/test_formal_specs_lilo_skill_contract.py
git commit -m "docs: split Lilo conventions out of the authoring reference"
```

---

### Task 8: `SKILL.md` reference map and ambiguity-gate amendment

**Files:**
- Modify: `skills/formal-specs-lilo/SKILL.md` — replace workflow step 5, and
  extend the "Ambiguity gate" and "Error handling" sections.
- Test: `tests/test_formal_specs_lilo_skill_contract.py`

**Interfaces:**
- Consumes: all six references from Tasks 2–7.
- Produces: the routing asserted by `test_skill_routes_to_every_reference` and
  the gate wording asserted by
  `test_ambiguity_gate_offers_a_stub_before_refusing`.

- [ ] **Step 1: Replace workflow step 5 with a reference map**

```markdown
5. Read the references this requirement needs, before authoring:

   | Read | When |
   | --- | --- |
   | [lilo-authoring.md](references/lilo-authoring.md) | always — discovery, reuse, edit discipline, validation |
   | [lilo-declarations.md](references/lilo-declarations.md) | always — syntax for every declaration keyword |
   | [lilo-conventions.md](references/lilo-conventions.md) | always — naming and file-name rules |
   | [lilo-expressions.md](references/lilo-expressions.md) | any non-trivial expression: types, units, records, enums, `cases`, `let` |
   | [lilo-temporal-semantics.md](references/lilo-temporal-semantics.md) and [lilo-temporal-patterns.md](references/lilo-temporal-patterns.md) | any temporal requirement |
   | [lilo-modules-components.md](references/lilo-modules-components.md) | the project has modules or components, or the edit crosses a `::` boundary |
   | [lilo-attributes.md](references/lilo-attributes.md) | metadata, parameter defaults, suppressed diagnostics, or a spec stub |
   | [lilo-static-analysis.md](references/lilo-static-analysis.md) | a consistency, redundancy, or guard diagnostic appears, or a `cases` spec is authored |

   Each reference names the `specforge doc` page that overrides it. Consult
   that page rather than guessing when a construct is not covered.
```

- [ ] **Step 2: Amend the ambiguity gate**

Append to the "Ambiguity gate" section:

```markdown
When a requirement cannot be formalized from what the user has supplied,
prefer a documented spec stub over refusing: a named `spec` carrying the
requirement text as its `///` docstring and no body. Say explicitly that a
stub is interpreted as `true` and therefore verifies nothing, so the
requirement is recorded but unproven. See
[lilo-attributes.md](references/lilo-attributes.md). This never licenses
inventing a formalization.
```

- [ ] **Step 3: Amend error handling**

Replace the unsupported-construct sentence with:

```markdown
For an unsupported or undocumented construct, do not edit or guess; offer a
spec stub, ask for a reformulation, or report the documented limitation.
```

- [ ] **Step 4: Run the routing and gate tests**

Run: `python -m unittest tests.test_formal_specs_lilo_skill_contract -v -k "routes or ambiguity"`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add skills/formal-specs-lilo/SKILL.md
git commit -m "feat: route the Lilo language reference and allow spec stubs"
```

---

### Task 9: Whole-skill validation

**Files:**
- Test: all of `tests/`
- Create (scratchpad only, not committed): a multi-file SpecForge project
  embedding every complete Lilo form used across the references.

**Interfaces:**
- Consumes: every file from Tasks 2–8.
- Produces: evidence for the completion claim.

- [ ] **Step 1: Run the full suite**

Run: `python -m unittest discover -s tests -v`
Expected: PASS, all tests.

- [ ] **Step 2: Run the skill validator**

Run:
```bash
python /home/rogu/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/formal-specs-lilo
```
Expected: `Skill is valid!`

- [ ] **Step 3: Scan for undocumented syntax**

```bash
cd /home/rogu/projects/rong-skills
grep -rnE '_with|#\[timeout *=' skills/formal-specs-lilo/references/
grep -rnE '(max|min)_(future|past) *\[[^0]' skills/formal-specs-lilo/references/
```
Expected: `_with` only in the "not documented in 0.5.10" prohibition lines;
`#[timeout =` only in the trap paragraph that labels it undocumented; no
non-zero sliding-window lower bound.

- [ ] **Step 4: Parse every embedded Lilo form**

Build a project covering modules, components, and expressions, then parse it.
`specforge parse` exits 0 even on failure, so grep the output.

```bash
SCRATCH=/tmp/claude-1000/-home-rogu-projects-rong-skills/8f2932e2-3794-46f1-8f5f-478a84459b26/scratchpad/lilo-ref
mkdir -p "$SCRATCH/src"
printf '[project]\nname = "ref"\nsource = "src/"\n' > "$SCRATCH/specforge.toml"

cat > "$SCRATCH/src/Units.lilo" <<'LILO'
module Units

unit m
unit km
unit s

pub def km_to_m(kilometre: Float<km>): Float<m> = kilometre * 1000.0<m/km>
LILO

cat > "$SCRATCH/src/Util.lilo" <<'LILO'
module Util

type Point = { x: Float, y: Float }
type Engine = { status: { throttle: Int, fault: Bool } }

def add(x: Float, y: Float) = x + y

pub def calc(x: Float) = add(x, x)

pub def is_on_x_axis(p: Point): Bool = p.y == 0.0

pub def default_engine: Engine = { status.throttle = 0, status.fault = false }

pub def warmed_up: Engine = { default_engine with status.throttle = 70 }

pub def circumcircle(a: Float, b: Float, c: Float): Float =
  let s = (a + b + c) / 2.0;
  let area = sqrt(s * (s - a) * (s - b) * (s - c));
  (a * b * c) / (4.0 * area)
LILO

cat > "$SCRATCH/src/BatteryCell.lilo" <<'LILO'
system BatteryCell

pub signal voltage: Float
pub signal temperature: Float
pub param nominal_voltage: Float

pub def over_voltage: Bool = voltage > nominal_voltage * 1.15

spec voltage_range = voltage >= 2.5 && voltage <= 4.5
LILO

cat > "$SCRATCH/src/Battery.lilo" <<'LILO'
system Battery

import Util as U
import Units use { unit m, unit km }

pub signal level: Float
pub signal voltage: Float
pub param capacity: Float

component cell1: BatteryCell

component cell2: BatteryCell {
  param nominal_voltage = 3.7
  signal voltage = voltage / 2.0
}

enum Color = #Red | #Green | #Blue
enum Mode = #On | #Off

signal color: Color
signal mode: Mode
signal temp: Float
signal n: Int
signal gps: { lat: Float, lon: Float }

#[default = 25.0]
param threshold: Float

#[default = 1.0<m>]
param min_water_level: Float<m>

def is_red(c: Color): Bool = c == #Red

def is_green(c: Color): Bool =
  match c {
    #Red -> false;
    #Color::Green -> true;
    #Blue -> false;
  }

def mode_num(x: Mode): Int = match x { #On -> 1; #Off -> 0; }

def as_float: Float = float(n)
def now: Float = time
def magnitude: Float = abs(temp)
def biggest: Float = max(temp, threshold)
def smallest: Float = min(temp, threshold)

def chained: Bool = 0.0 < temp <= 100.0
def double_neg: Float = -(-temp)
def not_next: Bool = !(next (temp > 0.0))

def describe: String =
  if temp > 30.0 then "hot"
  else if temp < 10.0 then "cold"
  else "moderate"

def punned = { threshold, capacity }
def at_meihan: Bool = 34.63 < gps.lat < 34.65 && 135.99 < gps.lon < 136.01
def converted: Float<m> = Units::km_to_m(2.0<km>)
def helper: Float = U::calc(temp)
def cell_ok: Bool = cell1::over_voltage || cell2::over_voltage

#[label("safety", "critical")]
#[alias(en = "Level Valid", ja = "レベル有効")]
#[field(priority = 1, reviewed = true, owner = "ops")]
spec level_valid = level >= 0.0 && level <= 100.0

#[disable(redundancy)]
#[timeout(10)]
spec cells_safe = cell1::voltage_range && cell2::voltage_range

#[timeout(satisfiability = 20, redundancy = 30)]
spec regimes = cases {
  temp > 30.0 -> eventually temp < 20.0;
  temp < 10.0 -> eventually temp > 20.0;
  10.0 <= temp <= 30.0 -> true;
}

/// Not yet formalised.
spec frequency_within_band

#[rigidity = "soft"]
assumption warm_enough = always (temp > -50.0)

/// Not yet formalised.
assumption height_non_negative

#[disable(unused)]
def unused_helper: Bool = is_red(color) && is_green(color) && mode_num(mode) == 1
LILO

cd "$SCRATCH" && specforge parse > out.txt 2>&1
echo "parse errors: $(grep -c 'parse error' out.txt)"
grep -n 'parse error' -A3 out.txt | head -40
```
Expected: `parse errors: 0`. If a form fails, correct the reference to the
documented form and rerun before committing.

- [ ] **Step 5: Confirm the example submodule is untouched**

```bash
git -C /home/rogu/projects/rong-skills status --short
git -C /home/rogu/projects/rong-skills/experiments/specforge-examples status --short
```
Expected: no changes under `experiments/`.

- [ ] **Step 6: Commit the plan and any parse-driven corrections**

```bash
git add docs/superpowers/plans/2026-07-30-formal-specs-lilo-language-reference.md
git commit -m "docs: add Lilo language reference implementation plan"
```

---

## Self-Review

**Spec coverage.** 5.1 → Task 2. 5.2 → Task 3. 5.3 and 5.4 → Task 4. 5.5 →
Task 6. 5.6 → Task 5. 5.7 → Task 7. 5.8 → already complete, untouched.
Retrieval contract → Task 1 `test_every_reference_names_its_authority`.
Reference responsibilities → Tasks 2–7 section lists. Narrowed
`lilo-authoring.md` → Task 7. Workflow routing → Task 8 Step 1. Ambiguity-gate
amendment → Task 8 Steps 2–3, asserted by Task 1. Correctness constraints →
Global Constraints plus Task 9 Steps 3–4. Validation → Task 9. Scope
exclusions → Global Constraints and Task 9 Step 5. Decision reversal is
recorded in the spec; no task contradicts it.

**Placeholders.** None. Every step gives the literal text, section list,
command, or expected output. The contract assertions in Task 1 are the precise
content specification for Tasks 2–8; each later task additionally names its
sections, required forms, and traps.

**Type consistency.** The six path constants are defined once in Task 1 and
used unchanged thereafter. `NEW_REFS` is defined in Task 1 Step 1 and consumed
in Task 1 Step 2 and `test_references_author_no_undocumented_syntax`. The
helpers `flat` and `assert_all_in` are defined once in Task 1 Step 3 and used
by every content test. Every backticked form asserted in Task 1 appears in the
matching task's section list and, where it is a complete Lilo construct, in
Task 9's parse project. `test_authoring_documents_approved_unit_bearing_param_defaults`
is repointed from `AUTHORING` to `ATTRIBUTES` in Task 7 Step 4, matching the
`param min_water_level: Float<m>` example required there in Task 5 Step 1.
