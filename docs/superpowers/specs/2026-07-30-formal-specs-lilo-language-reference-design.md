# Formal Specs Lilo Language Reference Design

## Goal

Make `formal-specs-lilo` cover the whole Lilo language reference — chapter 5
of the SpecForge 0.5.10 user guide — so an agent can author any documented
construct without consulting the manual first, and can recognize every
construct it meets in an existing project.

Chapter 5 comprises eight sub-pages, retrievable locally as
`specforge doc <topic>`:

| Sub-page | Topic | Current skill coverage |
| --- | --- | --- |
| 5.1 Language Basics | `lilo-language` | none |
| 5.2 Systems | `lilo-systems` | reuse policy only, no syntax |
| 5.3 Modules | `lilo-modules` | named, not documented |
| 5.4 Components | `lilo-components` | none |
| 5.5 Static Analysis | `lilo-static-analysis` | none |
| 5.6 Additional Features | `lilo-additional-features` | `#[default]` only |
| 5.7 Conventions | `conventions` | naming sentence only |
| 5.8 Semantics | `semantics` | complete |

## Decision Reversal

The 2026-07-30 temporal-patterns design rejected its Approach 1, "expand into
a comprehensive Lilo guide," on the grounds that it duplicates the
authoritative manual. That judgment is hereby overridden by explicit user
direction: the skill must carry the full language reference. This spec adopts
the duplication consciously and manages its cost through the retrieval
contract below, rather than by limiting scope.

## Approaches Considered

1. Reproduce the reference verbatim in the skill. Fully self-contained, but
   ~7,800 words of transcription, highest drift risk on every 0.5.x bump.
2. Thin construct-to-topic index that routes to `specforge doc`. Zero drift and
   tiny, but useless without the CLI and carries no translation guidance.
3. **Selected.** Condensed authoring-oriented references covering every
   construct, each naming its `specforge doc` page as the authority for
   exhaustive detail. Works with no CLI present; escalates for corner cases.

## Retrieval Contract

Every reference file states, at its head, the one `specforge doc <topic>`
command that is authoritative for its content, plus the versioned URL. Each
entry is written to be sufficient for authoring; when a case is not covered by
the entry, the agent runs the named command rather than guessing. A reference
must never contradict its source page: where an example project and the manual
disagree, the manual wins and the divergence is recorded as a trap.

## Reference Responsibilities

`lilo-expressions.md` — chapter 5.1. Comments (`/*`, `//`, `///`); primitive
types `Bool`/`Int`/`Float`/`String`; units of measure (angle-bracket literals,
compound `*` `/` `^`, dimensionless `1`, precedence and associativity,
parenthesized grouping, permitted operations, inference, string identity of
units, `unit` declaration); the operator precedence ladder including chained
comparisons and the no-prefix-chaining rule; built-ins `float`, `time`,
`sqrt`, `abs`, `max`, `min`; `if`/`then`/`else` as a pointwise expression with
mandatory `else`; `cases` and its desugaring; records (construction,
structural typing, named `type`, punning, dotted-path construction, `with`
updates, projection and chaining); enums (`#` constructors, namespaces, shared
constructor names, qualified forms, equality); `match`; and `let` bindings.

`lilo-declarations.md` — chapter 5.2. The `system` header and its file-name
obligation; `type`; `signal` and the no-function-types restriction; `param`
and its monitoring-versus-exemplification obligations; `def` in all documented
shapes (bare, annotated, parameterized, record-parameterized, mutually
referring, order-independent, no cycles); `spec` and its two restrictions;
`assumption` and its analysis role. Every declaration gets a syntax line and a
minimal example. Retains the existing reuse policy from `lilo-authoring.md`.

`lilo-modules-components.md` — chapters 5.3 and 5.4. `module` and its
`def`/`type`-only restriction; `pub`; all four import forms including
`use { unit m }`; `component` instantiation; lifted versus mapped signals and
params and the schema consequence; `::` access at one, two, and three levels,
including component specs; the system schema and the `specforge schema`
command with `--diff`. Carries the `::`-versus-`.` distinction explicitly,
since component access and record projection are visually similar and
semantically unrelated.

`lilo-attributes.md` — chapter 5.6. The generic attribute shape and its
immediately-precedes rule; `#[label]`; `#[alias]` and its data-file role;
`#[field]` with scalar-only values; `#[default]` including the `null`
override and the default-is-not-a-constant rule; `#[disable(unused)]`,
`#[disable(satisfiability)]`, `#[disable(redundancy)]`; `#[timeout(10)]` and
`#[timeout(satisfiability = …, redundancy = …)]`; `#[rigidity = "soft"]`. Spec
stubs — a bodyless `spec` or `assumption`, reading as `true` — are documented
here and cross-referenced from the ambiguity gate.

`lilo-static-analysis.md` — chapter 5.5. Consistency checking for single specs
and for spec sets; redundancy checking; guard analysis of `cases` for
satisfiability, exhaustiveness, and disjointness. Framed as diagnostics to
recognize and design against, never to run: the skill's syntax-only validation
boundary is unchanged, and this file must say so.

`lilo-conventions.md` — chapter 5.7. snake_case for modules, systems, signals,
params, defs, specs, arguments, and record fields; CamelCase for types; the
name-matches-file-name requirement.

`lilo-authoring.md` — retained, narrowed to process: project discovery,
declaration reuse policy, smallest-coherent-edit discipline, and syntax-only
validation. Syntax detail moves to the files above; naming moves to
`lilo-conventions.md`; `#[default]` moves to `lilo-attributes.md`. No syntax
rule is stated in two files.

`lilo-temporal-semantics.md` and `lilo-temporal-patterns.md` — unchanged,
already covering 5.8.

## Workflow Routing

`SKILL.md` gains a reference map keyed by what the requirement needs, so the
agent reads only the relevant files. `lilo-declarations.md` and
`lilo-conventions.md` are read for any authoring task; `lilo-expressions.md`
whenever a non-trivial expression is written; the temporal pair for temporal
requirements; `lilo-modules-components.md` when the project has modules or
components; `lilo-attributes.md` when metadata, defaults, or a stub is
involved; `lilo-static-analysis.md` when a diagnostic is reported or a `cases`
spec is authored. The ambiguity gate is unchanged except that it now offers the
spec-stub option before refusing.

## Ambiguity Gate Amendment

Spec stubs change the response to an unformalizable requirement. Current
behavior refuses to edit and asks for a reformulation. New behavior: propose a
documented stub — a named `spec` with the requirement text as its docstring
and no body — recording the requirement in the project without asserting an
unverified formalization. The agent must state that a stub reads as `true` and
therefore verifies nothing. Inventing a formalization remains prohibited.

## Correctness Constraints

- Preserve `https://docs.imiron.io/v/0.5.10/en/index.html` as the authority
  and name the owning `specforge doc` topic in every reference.
- Author only constructs confirmed on those pages. Where the example
  submodule diverges, follow the manual and record the divergence: notably
  `#[timeout = 10.0]` in `Energy.lilo` versus the documented `#[timeout(10)]`.
- Keep `::` (module and component access) distinct from `.` (record
  projection) wherever both could apply.
- Keep prefix operators unchained: `!(previous p)`, `-(-x)`.
- Sliding windows remain `[0, b]`; interval endpoints remain inclusive.
- State the `else`-is-mandatory and branches-agree rules for conditionals, and
  the all-branches-`Bool` rule for `cases`.
- Do not present static analyses as steps the skill runs.
- One rule, one file: no syntax statement duplicated across references.

## Validation

Extend the contract test before editing any reference. The contract requires
each new file to exist, to name its authoritative `specforge doc` topic and
the versioned URL, to cover the constructs listed for it above, to route from
`SKILL.md`, and to keep the stub option in the ambiguity gate. Add a negative
check that `#[timeout = ` never appears as a recommended form.

Then run: the focused contract test; the full repository suite; the skill
validator; a scan for undocumented syntax; and `specforge parse` over a
scratchpad project embedding every complete Lilo form used as an example
across the references. No semantic or behavioral SpecForge analyses run as
part of validation.

## Scope Exclusions

- Chapters outside 5: project configuration, data files, spec search, CLI,
  Python SDK, exemplification, falsification, monitoring, export. Referenced
  only where 5.4 and 5.6 point at them.
- Do not modify `experiments/specforge-examples`.
- Do not change the syntax-only project-validation boundary.
- Do not add project-specific domain vocabulary to any reference.
