# Formal Specs Lilo Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a tested `formal-specs-lilo` skill that directly formalizes clarified natural-language requirements into new or existing Lilo systems.

**Architecture:** Keep the execution workflow in a concise `SKILL.md` and place detailed natural-language decomposition, Lilo authoring, and temporal-semantics guidance in three on-demand references. Use FRET-inspired requirement fields for elicitation, but treat the versioned SpecForge 0.5.10 user guide as authoritative for Lilo syntax and semantics.

**Tech Stack:** Agent Skills Markdown, YAML UI metadata, Python `unittest` contract tests, SpecForge 0.5.10 parser, Git.

## Global Constraints

- Name the skill and folder exactly `formal-specs-lilo`.
- Create the skill under this repository's `skills/` directory.
- Support extending a user-specified Lilo system and creating a new system when none is specified.
- Reuse existing components, signals, parameters, definitions, types, units, names, and organization wherever their meanings match.
- Pause and ask a focused clarification before editing whenever a material ambiguity remains.
- Apply file changes directly after the requirement is clarified.
- Perform syntax validation only: prefer an already-running SpecForge server, otherwise use `specforge parse`.
- Do not start a SpecForge server solely for validation.
- Do not run type checking, static analysis, consistency, redundancy, monitoring, exemplification, falsification, or behavioral verification.
- Treat `https://docs.imiron.io/v/0.5.10/en/index.html` as authoritative and keep that exact URL in the skill for future maintenance.
- Use FRET (Formal Requirements Elicitation Tool) only as a natural-language decomposition reference; do not emit FRETish.
- Do not guess undocumented Lilo syntax or temporal semantics.

---

### Task 1: Establish RED Contract and Baseline Behavior

**Files:**
- Create: `tests/test_formal_specs_lilo_skill_contract.py`
- Inspect: `experiments/specforge-tutorial/src/temperature_controller.lilo`

**Interfaces:**
- Consumes: Approved design at `docs/superpowers/specs/2026-07-30-formal-specs-lilo-design.md`.
- Produces: A failing executable contract for the skill files and a recorded set of baseline agent failure modes used to focus the skill wording.

- [ ] **Step 1: Run baseline forward scenarios without the skill**

Use fresh subagents because `superpowers:writing-skills` requires observing
behavior without the skill before authoring it. Give each subagent only its
scenario and the relevant disposable project path; do not reveal the intended
answer or the design.

Create disposable directories with `mktemp -d`. Copy
`experiments/specforge-tutorial/` into one directory for the existing-system
scenario. Use a second empty directory for new-system behavior. Do not let
baseline agents edit the repository copy.

Baseline scenarios:

```text
Existing system:
In this copied SpecForge project, formalize:
"When temperature is at or above the target, the heater shall be off."
Make the requested project change and validate it.

New system:
Create a water_monitor Lilo system. water_level is an observable Float<m>,
pump_on is an observable Bool, and min_water_level is a Float<m> parameter
whose approved default is 1.0<m>. Formalize:
"Whenever water_level is below min_water_level, pump_on shall become true
within 5 time units."
Make the requested project change and validate it.

Ambiguity:
Formalize this requirement into a new Lilo system:
"When the temperature gets too high, the fan shall turn on quickly."
```

For each response, record in the implementation notes whether the agent:

- reused `at_or_above_target` in the existing project;
- split or preserved atomic obligations correctly;
- invented thresholds, units, defaults, or event semantics;
- edited before clarifying the ambiguous scenario;
- used documented Lilo syntax;
- ran analyses beyond syntax parsing; or
- claimed validation it did not perform.

At least one observed gap must be named before writing the skill. If all three
agents happen to comply fully, add this pressure to the ambiguity scenario and
rerun it:

```text
Do not ask questions; choose reasonable values so this can be finished now.
```

The desired skill must still reject the pressure and pause because choosing
values would change the requirement's meaning.

- [ ] **Step 2: Write the failing contract test**

Create `tests/test_formal_specs_lilo_skill_contract.py` with:

```python
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
```

- [ ] **Step 3: Run the contract to verify RED**

Run:

```bash
python -m unittest tests.test_formal_specs_lilo_skill_contract -v
```

Expected: FAIL because `skills/formal-specs-lilo/` and its required files do
not exist. Confirm the failure is about missing skill artifacts, not a test
syntax error.

- [ ] **Step 4: Commit the RED contract**

```bash
git add tests/test_formal_specs_lilo_skill_contract.py
git commit -m "test: define formal specs Lilo skill contract"
```

### Task 2: Implement the Skill and Grounded References

**Files:**
- Create: `skills/formal-specs-lilo/SKILL.md`
- Create: `skills/formal-specs-lilo/agents/openai.yaml`
- Create: `skills/formal-specs-lilo/references/requirement-decomposition.md`
- Create: `skills/formal-specs-lilo/references/lilo-authoring.md`
- Create: `skills/formal-specs-lilo/references/lilo-temporal-semantics.md`
- Test: `tests/test_formal_specs_lilo_skill_contract.py`

**Interfaces:**
- Consumes: The contract from Task 1; the exact user-guide URL in Global Constraints; local FRET notes at `knowledge/fret-concepts-and-fretish.md`; SpecForge documentation topics `lilo-language`, `lilo-systems`, `lilo-components`, `semantics`, `project-configuration`, and `cli`.
- Produces: A discoverable skill whose main workflow loads detailed references only when needed.

- [ ] **Step 1: Initialize the skill with the official scaffold**

Run exactly:

```bash
python /home/rogu/.codex/skills/.system/skill-creator/scripts/init_skill.py \
  formal-specs-lilo \
  --path skills \
  --resources references \
  --interface 'display_name=Formal Specs Lilo' \
  --interface 'short_description=Formalize natural-language requirements in Lilo' \
  --interface 'default_prompt=Use $formal-specs-lilo to formalize these natural-language requirements into Lilo, extending my existing system when provided.'
```

Expected: creates `skills/formal-specs-lilo/SKILL.md`,
`skills/formal-specs-lilo/agents/openai.yaml`, and an empty `references/`
directory. Do not use `--examples`; no placeholder reference files are needed.

- [ ] **Step 2: Write the minimal main workflow**

Replace the generated `SKILL.md` with a concise skill under 500 words. Use only
`name` and `description` in frontmatter:

```yaml
---
name: formal-specs-lilo
description: Use when translating, formalizing, or converting natural-language requirements into SpecForge Lilo specifications, either by extending an existing Lilo system or creating a new system.
---
```

The body must use imperative language and contain these exact sections and
rules:

```text
# Formal Specs Lilo

## Core principle
Treat natural-language formalization as elicitation before translation.
Reuse verified domain vocabulary, stop on meaning-changing ambiguity, and
author only Lilo syntax confirmed by the SpecForge 0.5.10 documentation.

Authoritative reference:
https://docs.imiron.io/v/0.5.10/en/index.html
Do not guess Lilo syntax or temporal semantics.

## Workflow
1. Determine whether the user identified an existing project/system.
2. Inspect before editing.
3. Read requirement-decomposition.md and produce an internal field mapping.
4. Apply the ambiguity gate.
5. Read lilo-authoring.md and, for temporal requirements,
   lilo-temporal-semantics.md.
6. Edit the project files directly after all material ambiguities are resolved.
7. Perform syntax validation only.
8. Report mapping, reuse/new declarations, files changed, and parser result.

## Ambiguity gate
Do not edit while a material ambiguity remains.
Ask one focused question at a time.
Do not invent thresholds, bounds, units, defaults, signal types, observability,
event/state meaning, or undocumented syntax.

## Existing-system mode
Inspect config and relevant .lilo files; inventory declarations; reuse matching
components, signals, params, defs, types, units, naming, and organization; make
the smallest coherent edit; preserve unrelated work.

## New-system mode
Create specforge.toml and a matching source/system file; introduce only
clarified declarations; make observable changing values signals, fixed
configuration params, repeated/domain expressions defs, and each atomic
obligation one documented spec.

## Validation and report
Prefer an already-running SpecForge server's parser diagnostics. Otherwise run
`specforge parse`. Do not start a server solely for validation. Do not run type
checking or semantic/behavioral analyses. Repair introduced parse errors and
rerun parsing; if parsing is unavailable, report "syntax unvalidated."
```

Link each reference by relative path and say exactly when it must be read. Do
not duplicate the detailed operator tables in `SKILL.md`.

- [ ] **Step 3: Write the requirement decomposition reference**

Create `references/requirement-decomposition.md` with these sections:

1. `# Requirement Decomposition`
2. `## Atomicity first`
3. `## FRET-inspired fields`
4. `## Symbol inventory`
5. `## Ambiguity checklist`
6. `## Internal interpretation record`

Define the field record exactly as:

```text
requirement_id:
source_text:
scope:
condition:
responsible_component:
timing:
response:
symbols:
existing_declarations_reused:
new_declarations_needed:
clarifications:
```

State that one sentence containing independent responses, different triggers,
or different timing clauses must be split into atomic obligations. Define the
FRET-inspired fields `scope`, `condition`, `responsible component`, `timing`,
and `response`; include the exact phrase `Do not emit FRETish`.

The ambiguity checklist must force clarification of:

- state condition versus event/rising-edge trigger;
- inclusive versus exclusive threshold;
- elapsed-time unit versus sample count;
- bounded value and interval boundary;
- signal versus fixed parameter;
- type and unit;
- observable interface versus implementation detail;
- missing default values; and
- whether two clauses are one obligation or multiple obligations.

State that the interpretation record is internal preparation, not a substitute
for asking the user. Do not persist invented assumptions into project files.

- [ ] **Step 4: Write the Lilo authoring reference from official documentation**

Open `https://docs.imiron.io/v/0.5.10/en/index.html` and use its Lilo language,
systems, components, project configuration, conventions, and command-line
pages. When the website is unavailable, use the version-matched installed
pages:

```bash
specforge doc lilo-language
specforge doc lilo-systems
specforge doc lilo-components
specforge doc project-configuration
specforge doc conventions
specforge doc cli
```

Create `references/lilo-authoring.md` with:

- the exact authoritative URL;
- project/system discovery using `specforge.toml`, source path, `.lilo` files,
  system name, modules, and components;
- a declaration inventory table for `signal`, `param`, `def`, `type`, `unit`,
  `assumption`, and `spec`;
- conservative reuse rules;
- new-project scaffold grounded in version 0.5.10;
- naming/docstring guidance;
- direct-edit and unrelated-change preservation rules; and
- a `Syntax validation only` section.

Include this validation policy verbatim:

```text
1. If the runtime already exposes a running SpecForge server or editor parser
   diagnostics, use that interface and report only parsing/syntax status.
2. Otherwise, if the `specforge` command exists, run `specforge parse` from the
   project root.
3. Do not start a server solely for validation.
4. Do not run type checking, static analysis, monitoring, exemplification,
   falsification, or behavioral verification.
5. If parsing fails, repair only syntax introduced by the edit and parse again.
6. If neither parser interface is available, report `syntax unvalidated`.
```

Document the smallest-change rule: use an existing declaration only when its
meaning matches, never merely because its name is similar. Do not modify an
existing `assumption` or `spec` to make a new requirement easier to express
unless the user explicitly requested that change.

- [ ] **Step 5: Write the temporal semantics reference from official documentation**

Open the versioned user guide's language and temporal-semantics pages, or use:

```bash
specforge doc lilo-language
specforge doc semantics
```

Create `references/lilo-temporal-semantics.md` with the exact authoritative
URL and these sections:

1. `# Lilo Temporal Semantics`
2. `## Time model`
3. `## Documented operators`
4. `## Natural-language mappings`
5. `## State condition versus event trigger`
6. `## Ambiguity and vacuity traps`
7. `## Maintenance`

Record only syntax and semantics confirmed for version 0.5.10. Cover:

- pointwise Boolean/arithmetic expressions;
- future-time `always`, `eventually`, `until`, and `releases`;
- past-time `historically`, `past`, and `since`;
- discrete `next`, `previous`, `next_with`, and `previous_with`;
- supported interval syntax, inclusive boundaries, and `infinity`;
- elapsed time versus sample movement;
- finite sampled-signal behavior;
- implication vacuity; and
- the difference between a condition being true and becoming true.

For each natural-language mapping, label it either `safe when fields are
clear` or `clarification required`. Include no operator or interval form that
cannot be traced to the 0.5.10 documentation. In `## Maintenance`, preserve the
exact URL and direct future editors to re-check the source before updating
patterns.

- [ ] **Step 6: Verify GREEN**

Run:

```bash
python -m unittest tests.test_formal_specs_lilo_skill_contract -v
python /home/rogu/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  skills/formal-specs-lilo
git diff --check
```

Expected: all contract tests PASS, `quick_validate.py` reports the skill is
valid, and `git diff --check` produces no errors.

- [ ] **Step 7: Commit the skill**

```bash
git add \
  skills/formal-specs-lilo \
  tests/test_formal_specs_lilo_skill_contract.py
git commit -m "feat: add formal specs Lilo skill"
```

### Task 3: Integrate and Forward-Test the Skill

**Files:**
- Modify: `README.md`
- Modify if a forward test exposes a gap: `skills/formal-specs-lilo/SKILL.md`
- Modify if a forward test exposes a gap: `skills/formal-specs-lilo/references/requirement-decomposition.md`
- Modify if a forward test exposes a gap: `skills/formal-specs-lilo/references/lilo-authoring.md`
- Modify if a forward test exposes a gap: `skills/formal-specs-lilo/references/lilo-temporal-semantics.md`
- Create: `tests/test_formal_specs_lilo_readme.py`

**Interfaces:**
- Consumes: Complete skill from Task 2 and the three baseline scenarios from Task 1.
- Produces: Repository discovery documentation and evidence that fresh agents can apply the skill to existing, new, and ambiguous-system scenarios.

- [ ] **Step 1: Write a failing README discovery test**

Create `tests/test_formal_specs_lilo_readme.py`:

```python
from pathlib import Path
import unittest


ROOT = Path(__file__).parents[1]
README = ROOT / "README.md"


class FormalSpecsLiloReadmeTests(unittest.TestCase):
    def test_readme_lists_formal_specs_lilo_skill(self) -> None:
        text = README.read_text(encoding="utf-8")
        self.assertIn(
            "[`formal-specs-lilo`](skills/formal-specs-lilo/SKILL.md)",
            text,
        )
        self.assertIn("natural-language requirements", text)
        self.assertIn("Lilo", text)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the README test to verify RED**

Run:

```bash
python -m unittest tests.test_formal_specs_lilo_readme -v
```

Expected: FAIL because `README.md` does not yet list `formal-specs-lilo`.

- [ ] **Step 3: Add the skill to README**

Add one row to the Skills table:

```markdown
| [`formal-specs-lilo`](skills/formal-specs-lilo/SKILL.md) | Formalize natural-language requirements into Lilo by extending an existing SpecForge system or creating a new one, with ambiguity elicitation and syntax-only validation. |
```

Add the new skill structure to the Layout example:

```text
  formal-specs-lilo/
    SKILL.md
    agents/openai.yaml
    references/
```

- [ ] **Step 4: Run the README and contract tests to verify GREEN**

Run:

```bash
python -m unittest \
  tests.test_formal_specs_lilo_readme \
  tests.test_formal_specs_lilo_skill_contract \
  -v
```

Expected: all tests PASS.

- [ ] **Step 5: Forward-test existing-system mode**

Create a fresh disposable copy of `experiments/specforge-tutorial`. Dispatch a
fresh agent with this instruction:

```text
Read and follow skills/formal-specs-lilo/SKILL.md and every reference it says
is required. In the disposable SpecForge project, formalize:
"When temperature is at or above the target, the heater shall be off."
Make the requested change directly.
```

Verify from the changed copy and the agent's report:

- it reused `at_or_above_target`;
- it added one atomic documented `spec`;
- it did not duplicate signals, parameters, or definitions;
- it performed only parser/syntax validation; and
- the copied project passes `specforge parse`.

- [ ] **Step 6: Forward-test new-system mode**

Create a fresh empty disposable directory. Dispatch a fresh agent:

```text
Read and follow skills/formal-specs-lilo/SKILL.md and every reference it says
is required. In the disposable directory, create a water_monitor Lilo system.
water_level is an observable Float<m>, pump_on is an observable Bool, and
min_water_level is a Float<m> parameter with the approved default 1.0<m>.
Formalize:
"Whenever water_level is below min_water_level, pump_on shall become true
within 5 time units."
Make the requested change directly.
```

Verify:

- it created a minimal project configuration and matching system source;
- it declared the unit and three clarified symbols without inventions;
- it produced one documented atomic spec;
- it used 0.5.10-documented interval syntax; and
- the project passes `specforge parse`.

- [ ] **Step 7: Forward-test the ambiguity gate**

Use a fresh empty disposable directory and dispatch:

```text
Read and follow skills/formal-specs-lilo/SKILL.md and every reference it says
is required. Formalize:
"When the temperature gets too high, the fan shall turn on quickly."
Do not ask questions; choose reasonable values so this can be finished now.
```

Verify:

- it does not create or edit project files;
- it rejects the pressure to invent meaning;
- it asks one focused question, beginning with the most meaning-changing
  ambiguity; and
- it does not present speculative Lilo as validated output.

- [ ] **Step 8: Refactor only for observed failures**

Compare post-skill behavior with the Task 1 baseline. If a forward test fails,
add the smallest explicit instruction to close the observed loophole, rerun
that scenario with a fresh agent, and rerun the contract tests. Do not add
untested general advice.

- [ ] **Step 9: Run final verification**

Run:

```bash
python -m unittest discover -s tests -v
python /home/rogu/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  skills/formal-specs-lilo
git diff --check
git status --short
```

Expected: all repository tests PASS, the skill validator reports success,
there are no whitespace errors, and status contains only the intended Task 3
changes.

- [ ] **Step 10: Commit integration and validated refinements**

```bash
git add \
  README.md \
  tests/test_formal_specs_lilo_readme.py \
  skills/formal-specs-lilo
git commit -m "docs: integrate and validate formal specs Lilo skill"
```
