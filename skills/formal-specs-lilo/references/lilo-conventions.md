# Lilo Naming Conventions

Authoritative 0.5.10 reference: <https://docs.imiron.io/v/0.5.10/en/index.html>.
Owning page: `specforge doc conventions`. Consult it rather than guessing
whenever a construct here leaves a case open.

Lilo is deliberately flexible about names so a specification can match the
naming of the system it describes. **An existing project's own convention wins
over the defaults below.** Inspect the project first and follow what is there.

## Documented defaults

| Kind | Convention | Example |
| --- | --- | --- |
| modules, systems | lowercase snake_case | `system climate_control` |
| signals, params, defs, specs | lowercase snake_case | `signal wind_speed` |
| arguments, record fields | lowercase snake_case | `ground_speed: Float` |
| types, including user-defined | capitalized CamelCase | `type Plane = { … }` |

## File names

A module or system name **must match the file name** it is defined in.
`module climate_control` and `system climate_control` both belong in
`climate_control.lilo`. This is a requirement, not a style preference. See
[lilo-declarations.md](lilo-declarations.md) for the header form and for the
case where a system file omits the header entirely.

## Matching an existing project

The example projects show why the defaults are only defaults. `Energy.lilo`
uses CamelCase for both its system and its signals — `system Energy`,
`signal Production`, `signal Consumption` — and quotes identifiers containing
spaces in backticks so they can match data-file column names:

```lilo
signal `Oil and Gas`: Float<MW>
```

When extending such a project, reuse its conventions. Introducing snake_case
names beside CamelCase ones is a defect, not a correction. Use `///` docstrings
to attach requirement context to whatever you add.
