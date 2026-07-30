# Formal Specs Lilo Temporal Patterns Design

## Goal

Make `formal-specs-lilo` reliably translate temporal natural-language
requirements using only syntax and semantics documented by SpecForge 0.5.10.
Cover every documented temporal construct relevant to translation without
copying the complete Lilo language manual into one reference.

## Approaches Considered

1. Expand `lilo-temporal-semantics.md` into a comprehensive Lilo guide. This
   keeps one lookup location but duplicates the authoritative manual, mixes
   temporal and non-temporal concerns, and increases maintenance risk.
2. Keep exact semantics in `lilo-temporal-semantics.md` and add a focused
   `lilo-temporal-patterns.md` translation catalog. This separates language
   truth from natural-language elicitation and is the selected approach.
3. Keep the current references and consult the installed documentation for
   every requirement. This minimizes repository content but repeatedly incurs
   discovery work and leaves common mistranslations uncaught.

## Reference Responsibilities

`lilo-temporal-semantics.md` is the compact semantic authority. It inventories
documented temporal constructs and records:

- finite sampled-signal support and elapsed-time intervals;
- exact universal or existential readings;
- endpoint obligations for `until`, `since`, and `releases`;
- witness and vacuity behavior;
- discrete `next` and `previous` boundaries;
- `will_change` and `did_change` as window variation, not point transitions;
- numeric future/past aggregates and their interval restrictions; and
- the unsupported `next_with` and `previous_with` forms.

`lilo-temporal-patterns.md` is the natural-language translation catalog. Each
entry contains:

1. a representative natural-language phrase;
2. fields that must be clarified;
3. the safe Lilo form after clarification;
4. a precise reading; and
5. a common mistranslation or edge case.

It covers invariants, bounded eventual response, bounded history, occurrence
in the past, strong `until`, `since`, `releases`, one-sample movement, value
variation, explicit point transitions, rolling extrema, and nested temporal
operators. Examples use neutral symbols rather than project-specific names.

`lilo-authoring.md` remains responsible for non-temporal syntax such as
declarations, types, units, records, imports, functions, and project layout.

## Workflow Routing

For every temporal requirement, `SKILL.md` requires reading both temporal
references after requirement decomposition and before authoring. The
ambiguity gate remains unchanged: examples are reusable only when their
clarification fields match the user requirement.

## Correctness Constraints

- Preserve `https://docs.imiron.io/v/0.5.10/en/index.html` as the authority.
- Confirm constructs against `specforge doc lilo-language` and
  `specforge doc semantics`.
- Do not imply continuous-time evaluation where only supported samples are
  checked.
- Treat interval endpoints as inclusive; author no exclusive interval syntax.
- Distinguish elapsed-time bounds from sample movement.
- Distinguish persistent state predicates, window variation, and explicit
  sample transitions.
- Do not introduce undocumented syntax or claim that a pattern resolves an
  unclarified requirement.

## Validation

Extend the repository contract test before editing the references. The
contract requires:

- the new pattern catalog and its workflow routing;
- every documented temporal family used in translation;
- exact witness, endpoint, boundary, and variation distinctions;
- the standard pattern-entry fields; and
- representative safe mappings and mistranslation warnings.

Then run:

1. the focused contract test;
2. the repository skill validator;
3. a scan for undocumented interval and `_with` syntax; and
4. syntax parsing of complete Lilo expressions embedded in examples where a
   project-independent parser invocation is available.

No semantic or behavioral SpecForge analyses are part of validation.

## Scope Exclusions

- Do not copy every general Lilo syntax feature into the temporal references.
- Do not change the skill's syntax-only project-validation boundary.
- Do not modify the example submodule while implementing this skill update.
- Do not add project-specific domain mappings to the reusable pattern catalog.
