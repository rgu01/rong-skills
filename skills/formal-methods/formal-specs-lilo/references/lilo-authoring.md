# Lilo Authoring

Authoritative 0.5.10 reference: <https://docs.imiron.io/v/0.5.10/en/index.html>.
Re-check its Lilo language, systems, components, project configuration,
conventions, and command-line pages before relying on syntax.

## Discover the project and system

From the project root, inspect `specforge.toml`, its `[project].source` path,
the `.lilo` files in that source tree, each `system` name, modules, components,
and the system selected by the user. A configured project must state
`[project].source`; the documented default scaffold uses `source = "src/"`.
Match a system or module name to its file name. Inspect component boundaries and
their public declarations before adding a parent-level property.

## Declaration inventory

This table is the reuse policy. For declaration syntax see
[lilo-declarations.md](lilo-declarations.md); for expressions see
[lilo-expressions.md](lilo-expressions.md); for attributes and parameter
defaults see [lilo-attributes.md](lilo-attributes.md).

| Declaration | Inventory meaning | Reuse rule |
| --- | --- | --- |
| `signal` | time-varying system input | Reuse only for the same observable changing value and type/unit. |
| `param` | value constant over time | Reuse only for the same fixed configuration meaning. |
| `def` | reusable expression or helper | Reuse only for the same documented domain expression. |
| `type` | named record/type shape | Reuse only for the same data structure. |
| `unit` | declared unit usable in annotations | Reuse only for the same physical/unit convention. |
| `assumption` | property taken as given by analysis | Do not modify it for a new requirement without explicit user request. |
| `spec` | parameterless Boolean requirement | Add one atomic obligation; do not modify an existing one without explicit user request. |

Use an existing declaration only when its meaning matches, never merely because
its name is similar. Do not modify an existing `assumption` or `spec` to make a
new requirement easier to express unless the user explicitly requested that
change.

## New project scaffold

After clarification, create `specforge.toml` and the matching source/system
file, for example `src/<system>.lilo`:

```toml
[project]
name = "<project-name>"
source = "src/"
```

```lilo
system <system>
```

Choose only confirmed declarations. `signal` is time-varying, `param` is
non-temporal, `def` captures a reusable expression, and `spec` is a
parameterless Boolean property. Use documented `component` declarations only
when the system structure is already clarified.

## Documentation and edits

Follow the project's own conventions; see
[lilo-conventions.md](lilo-conventions.md) for the documented defaults. Use
`///` docstrings to attach requirement context to declarations. Edit files
directly only after ambiguity resolution; make the smallest coherent change
and preserve unrelated changes.

## Syntax validation only

1. If the runtime already exposes a running SpecForge server or editor parser
   diagnostics, use that interface and report only parsing/syntax status.
2. Otherwise, if the `specforge` command exists, run `specforge parse` from the
   project root.
3. Do not start a server solely for validation.
4. Do not run type checking, static analysis, monitoring, exemplification,
   falsification, or behavioral verification.
5. If parsing fails, repair only syntax introduced by the edit and parse again.
6. If neither parser interface is available, report `syntax unvalidated`.
