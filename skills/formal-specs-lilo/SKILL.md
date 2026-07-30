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
5. Read [lilo-authoring.md](references/lilo-authoring.md) before authoring; for temporal requirements, also read [lilo-temporal-semantics.md](references/lilo-temporal-semantics.md).
6. Edit the project files directly after all material ambiguities are resolved.
7. Perform syntax validation only.
8. Report mapping, reuse/new declarations, files changed, and parser result.

## Ambiguity gate

Do not edit while a material ambiguity remains. Ask one focused question at a
time. Do not invent thresholds, bounds, units, defaults, signal types,
observability, event/state meaning, or undocumented syntax.

## Existing-system mode

Inspect config and relevant `.lilo` files; inventory declarations; reuse
matching components, signals, params, defs, types, units, naming, and
organization; make the smallest coherent edit; preserve unrelated work.

## New-system mode

Create `specforge.toml` and a matching source/system file; introduce only
clarified declarations; make observable changing values signals, fixed
configuration params, repeated/domain expressions defs, and each atomic
obligation one documented spec.

## Validation and report

Prefer an already-running SpecForge server's parser diagnostics. Otherwise run
`specforge parse`. Do not start a server solely for validation. Do not run type
checking or semantic/behavioral analyses. Repair introduced parse errors and
rerun parsing; if parsing is unavailable, report "syntax unvalidated."
