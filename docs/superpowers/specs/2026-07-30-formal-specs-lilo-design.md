# Formal Specs Lilo Skill Design

## Purpose

Create a reusable `formal-specs-lilo` skill that turns natural-language
requirements into Lilo specifications. The skill supports two modes:

- Extend a user-specified existing Lilo system, reusing its declarations and
  domain vocabulary wherever possible.
- Create a new SpecForge project and Lilo system when no existing system is
  specified.

The skill edits project files directly after the requirement is unambiguous.
Its automated validation boundary is syntax checking only.

## Authoritative Sources

The authoritative language reference is the versioned
[SpecForge 0.5.10 User Guide](https://docs.imiron.io/v/0.5.10/en/index.html).
The exact URL remains in the skill so future maintainers can re-check and
update Lilo syntax and semantics without guessing.

The repository's FRET notes provide the natural-language decomposition model.
FRET (Formal Requirements Elicitation Tool) contributes the concepts of scope,
condition, responsible component, timing, and response. FRETish syntax is not
an output format and is not treated as authoritative for Lilo.

## Skill Structure

```text
skills/formal-specs-lilo/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── requirement-decomposition.md
    ├── lilo-authoring.md
    └── lilo-temporal-semantics.md
```

`SKILL.md` contains the mandatory workflow, ambiguity gate, mode selection,
direct-edit policy, and syntax-only validation boundary.

`requirement-decomposition.md` describes atomic-obligation splitting, the
FRET-inspired fields, symbol extraction, observability checks, and the
structured interpretation prepared before authoring.

`lilo-authoring.md` describes project discovery, declaration reuse, new-system
scaffolding, declaration patterns, naming, editing, and syntax validation.

`lilo-temporal-semantics.md` records documented Lilo temporal operators,
interval semantics, natural-language timing mappings, and common semantic
traps. It points maintainers back to the versioned user guide.

`agents/openai.yaml` supplies discoverable user-facing metadata. The skill
requires no scripts or assets because semantic interpretation needs agent
judgment, while file editing and SpecForge parsing are already available in
the runtime.

## Workflow

1. Accept one or more natural-language requirements and an optional existing
   project or system.
2. If an existing system is specified, locate its project configuration and
   inspect all relevant `.lilo` files before proposing declarations.
3. Split compound prose into atomic obligations.
4. For each obligation, extract:
   - scope;
   - trigger or condition;
   - responsible component;
   - timing;
   - response;
   - referenced signals, parameters, definitions, types, units, and bounds.
5. Compare extracted concepts with existing declarations. Prefer existing
   signals, parameters, definitions, types, components, naming, and units when
   they express the intended meaning.
6. Stop and ask one focused clarification whenever a choice could change the
   requirement's meaning. Make no file edits while a material ambiguity
   remains.
7. If extending a system, add the smallest coherent set of declarations and
   atomic specs. If creating a system, create the project configuration and a
   self-contained Lilo system with only the declarations required by the
   clarified requirements.
8. Edit the files directly.
9. Validate syntax only:
   - Prefer a SpecForge server that is already running and exposes syntax
     diagnostics.
   - Otherwise run `specforge parse` when the command is available.
   - Do not start a server solely for validation.
   - Do not run type checking, static analysis, monitoring, exemplification,
     or behavioural verification.
10. If parsing fails, correct the syntax and repeat the same syntax check. If
    no parser is available, report the result as unvalidated rather than
    implying success.
11. Report the natural-language-to-Lilo mapping, changed files, reused and new
    declarations, clarification decisions, and syntax-check result.

## Ambiguity Gate

The skill pauses before editing when:

- the requirement has multiple plausible interpretations;
- a signal's type, unit, role, or observability is unclear;
- a time phrase lacks a usable bound or unit;
- an existing declaration conflicts with the requested meaning;
- a compound statement cannot be split without changing its intent; or
- the required Lilo construct cannot be confirmed in the versioned
  documentation.

The question must isolate the smallest unresolved choice. The skill does not
silently invent assumptions or emit a marked speculative draft.

## Existing-System Mode

Existing-system work is conservative. The skill:

- reads the project configuration and relevant source files;
- finds the named system and any referenced modules or components;
- builds an inventory of declarations before editing;
- reuses existing domain definitions instead of duplicating expressions;
- preserves local naming, formatting, documentation, and organization;
- adds only declarations needed by the clarified requirement; and
- avoids unrelated changes.

If the requested concept is already expressible with existing declarations,
the new `spec` references those declarations directly.

## New-System Mode

When no project or system is specified, the skill:

- derives a concise project and system name from the clarified domain;
- creates `specforge.toml` and a matching source file;
- declares observable time-varying values as `signal`s;
- declares fixed configuration values as `param`s, with defaults only when the
  user supplied or approved them;
- introduces `def`s for repeated or domain-significant expressions;
- writes one documented `spec` per atomic obligation; and
- avoids speculative signals, parameters, components, or implementation
  details.

## Temporal Formalization Policy

The skill uses FRET-inspired decomposition to identify intent, then authors
only syntax confirmed by the SpecForge 0.5.10 documentation. It distinguishes:

- global activation from scoped activation;
- state conditions from change or event triggers;
- invariants from eventual responses;
- bounded from unbounded timing;
- discrete sample movement from elapsed-time intervals; and
- future-time from past-time statements.

Generic Signal Temporal Logic notation may explain semantics but must not be
copied into Lilo unless the versioned Lilo documentation confirms the exact
surface syntax.

## Error Handling

- Material ambiguity: stop before editing and ask a focused question.
- Missing existing project/system: report what could not be located and ask
  for the path or correct name.
- Unsupported or undocumented construct: do not guess; ask for a reformulation
  or state the documented limitation.
- Syntax failure: repair only the introduced syntax and re-run parsing.
- No validation interface: complete the requested edit but label syntax as
  unvalidated.
- Unrelated diagnostics or existing dirty files: preserve them and avoid
  claiming they were caused or repaired by the skill.

## Testing

Skill validation uses test-first scenarios:

1. Extend an existing system while reusing its signals and definitions.
2. Create a new system from a clear requirement.
3. Refuse to edit an ambiguous requirement and ask a focused question.
4. Split a compound requirement into atomic specifications.
5. Map bounded timing with syntax grounded in the versioned documentation.
6. Restrict automated validation to syntax parsing.
7. Fall back cleanly when no SpecForge server or parser is available.

Repository contract tests verify the required metadata, files, authoritative
documentation URL, ambiguity gate, reuse policy, direct-edit policy, and
syntax-only boundary. Forward tests exercise the workflow against realistic
requirements before and after the skill is introduced.

## Success Criteria

The design is complete when:

- both existing-system and new-system modes are explicit;
- ambiguous requirements cause a pause before any edit;
- existing declarations are preferred over duplicate concepts;
- generated syntax is grounded in the SpecForge 0.5.10 documentation;
- edits are applied directly only after clarification;
- validation performs syntax checks and no semantic analyses;
- validation failures or unavailable tools are reported honestly; and
- the skill passes repository contract tests and forward-use scenarios.
