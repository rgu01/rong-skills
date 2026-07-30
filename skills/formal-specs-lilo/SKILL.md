---
name: formal-specs-lilo
description: Use when translating, formalizing, or converting natural-language requirements into SpecForge Lilo specifications, either by extending an existing Lilo system or creating a new system.
---

# Formal Specs Lilo

## Core principle

Treat natural-language formalization as elicitation before translation. Reuse
verified domain vocabulary, stop on meaning-changing ambiguity, and author only
Lilo syntax confirmed by the SpecForge 0.5.10 documentation.

Authoritative reference: <https://docs.imiron.io/v/0.5.10/en/index.html>
Do not guess Lilo syntax or temporal semantics.

## Workflow

1. Determine whether the user identified an existing project/system.
2. Inspect before editing.
3. Read [requirement-decomposition.md](references/requirement-decomposition.md) and produce an internal field mapping before formalizing any requirement.
4. Apply the ambiguity gate.
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
6. Edit the project files directly after all material ambiguities are resolved.
7. Perform syntax validation only.
8. Report mapping, reuse/new declarations, files changed, and parser result.

## Ambiguity gate

Do not edit while a material ambiguity remains. Ask one focused question at a
time. Do not invent thresholds, bounds, units, defaults, signal types,
observability, event/state meaning, or undocumented syntax.

When a requirement cannot be formalized from what the user has supplied, prefer
a documented spec stub over refusing: a named `spec` carrying the requirement
text as its `///` docstring and no body. Say explicitly that a stub is
interpreted as `true` and therefore verifies nothing, so the requirement is
recorded but unproven. See
[lilo-attributes.md](references/lilo-attributes.md). This never licenses
inventing a formalization.

## Existing-system mode

Inspect config and relevant `.lilo` files; inventory declarations; reuse
matching components, signals, params, defs, types, units, naming, and
organization; make the smallest coherent edit; preserve unrelated work.

## New-system mode

Create `specforge.toml` and a matching source/system file; introduce only
clarified declarations; make observable changing values signals, fixed
configuration params, repeated/domain expressions defs, and each atomic
obligation one documented spec.

## Error handling

If a requested existing project or system cannot be located, report the
missing target and ask for the path or correct name.
Do not fall back to new-system mode.
For an unsupported or undocumented construct, do not edit or guess; offer a
spec stub, ask for a reformulation, or report the documented limitation. Preserve existing dirty
files and unrelated diagnostics. Distinguish them from introduced parse
errors, and do not claim to have caused or repaired them.

## Validation and report

Prefer an already-running SpecForge server's parser diagnostics. Otherwise run
`specforge parse`. Do not start a server solely for validation. Do not run type
checking or semantic/behavioral analyses. Repair introduced parse errors and
rerun parsing; if parsing is unavailable, report "syntax unvalidated."
