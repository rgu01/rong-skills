# Lilo Attributes and Spec Stubs

Authoritative 0.5.10 reference: <https://docs.imiron.io/v/0.5.10/en/index.html>.
Owning page: `specforge doc lilo-additional-features`. Consult it rather than
guessing whenever a construct here leaves a case open.

## Attribute shape

Beyond `///` docstrings, Lilo definitions, specs, params, and signals may carry
attributes. An attribute must **immediately precede** the item it annotates.
The generic form mixes key-value entries, calls, and bare flags:

```lilo
#[key = "value", fn(arg), flag]
spec foo = true
```

Attributes carry metadata for the tooling — chiefly the VS Code extension — and
never change what a spec means. Multiple attribute lines may stack on one item.

## Labels

A label is a string attached to a specification; the spec sidebar groups by it.
Write `#[label("safety", "critical")]`. Several `#[label]` attributes on one
item all apply. Label colors are configured in `specforge.toml` under
`[labels.colors]`, keyed by label name with a hex code or an HTML color name.

## Aliases

An alias is an alternative name in a particular language:
`#[alias(en = "Brake Must Work", ja = "ブレーキは動作しなければならない")]`.
The sidebar shows the alias beside the source name. Aliases of a signal or
param may also be used to refer to them in data files, so they must be
unambiguous — an alias must not collide with another alias or with any
declaration name.

## Custom fields

Custom fields attach project-specific metadata such as review status, owner, or
priority: `#[field(priority = 1, reviewed = true, owner = "ops")]`. Field
values must be **scalar**.

## Parameter defaults

A parameter may carry a default, written immediately before it — `#[default = 25.0]`
above a `Float` parameter:

```lilo
#[default = 25.0]
param temperature: Float
```

Combine it with a unit-bearing literal for a dimensioned parameter — write
`#[default = 1.0<m>]` immediately before `param min_water_level: Float<m>`.

A default states the value the parameter is expected to take in a typical case.
It is **not** a constant declaration; use a `def` for a true constant, e.g.
`def pi: Float = 3.14159`. Do not invent a missing default: author one only
when the user supplied or approved the value.

Documented behavior:

- When monitoring, a parameter with a default may be omitted, and the default
  is used; supplying it explicitly overrides the default.
- When exporting a formula, defaults are substituted before export.
- When exemplifying, the solver is required to fix the parameter to the default.
- Passing JSON `null` for the parameter in a config tells SpecForge to ignore
  the default, freeing the solver to choose a value. `null` cannot be used as a
  default inside the Lilo program itself.

## Suppressing diagnostics

- `#[disable(unused)]` suppresses unused warnings on a def, param, or signal.
  Specs and public defs always count as used.
- `#[disable(satisfiability)]` and `#[disable(redundancy)]` switch off those
  static analyses for the annotated item.

Use these to record a deliberate choice, not to quiet a real problem — see
[lilo-static-analysis.md](lilo-static-analysis.md).

## Analysis timeouts

Override the default static-analysis timeout, in seconds, either together with
`#[timeout(10)]` or individually with
`#[timeout(satisfiability = 20, redundancy = 30)]`.

Trap: `Energy.lilo` in the example projects writes `#[timeout = 10.0]`. The
generic `#[key = value]` shape accepts it, but that is **not the documented**
spelling for a timeout. Author `#[timeout(10)]`.

## Soft assumptions

`#[rigidity = "soft"]` on an `assumption` marks it a soft constraint: the
solver tries to satisfy it but may relax it when it conflicts with hard
constraints.

## Spec stubs

A `spec` or `assumption` **without a body** is legal. It may still carry a
docstring and attributes, and it is **interpreted as `true`** by the tooling:

```lilo
/// The system should always eventually recover from errors.
spec error_recovery

/// height is always non-negative
assumption height_non_negative
```

Both forms are stubs: `spec error_recovery` for an unformalized requirement and
`assumption height_non_negative` for an unformalized assumption.

A stub records a requirement in the project without asserting a formalization.
Because it reads as `true`, it **verifies nothing** — it is a placeholder, and
saying so is part of reporting one.

This is the documented alternative to refusing when a requirement cannot be
formalized from what the user supplied: name the stub, put the requirement text
in its `///` docstring, and state that it is unproven. It never licenses
inventing a formalization. See the ambiguity gate in
[../SKILL.md](../SKILL.md).
