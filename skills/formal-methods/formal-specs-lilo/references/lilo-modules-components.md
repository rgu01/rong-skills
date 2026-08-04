# Lilo Modules and Components

Authoritative 0.5.10 reference: <https://docs.imiron.io/v/0.5.10/en/index.html>.
Owning pages: `specforge doc lilo-modules` and `specforge doc lilo-components`.
Consult them rather than guessing whenever a construct here leaves a case open.

Modules share pure definitions across files. Components compose systems into a
hierarchy. Both use `::` to cross a scope boundary.

## Modules

A module file starts with a module declaration such as `module Util`, and its
name must match the file name — `module Util` lives in `Util.lilo`.

A module may contain **only** `def`s and `type`s. It has no signals, params, or
specs. Definitions to be used from other files are marked `pub`:

```lilo
module Util

def add(x: Float, y: Float) = x + y

pub def calc(x: Float) = add(x, x)
```

Here `add` is private to the module and `calc` is visible to importers.

## Imports

Four documented forms:

| Form | Use at the call site |
| --- | --- |
| `import Util` | qualified: `Util::calc(x)` |
| `import Util as U` | qualified by alias: `U::calc(x)` |
| `import Util use { calc }` | unqualified: `calc(x)` |
| `import Units use { unit m, unit s }` | units become usable in annotations |

Units are the special case: to import a unit, prefix it with the `unit` keyword
inside the `use` list, as in `import Units use { unit m, unit s }`. A single
import may bring in several names, and the selective and alias forms may both
appear in a file.

## Components

A system becomes reusable as a component by marking the declarations that
parents may see. Signals, params, and defs need `pub`; **specs are always
public** and need no marker:

```lilo
system BatteryCell

pub signal voltage: Float
pub signal temperature: Float
pub param nominal_voltage: Float

pub def over_voltage: Bool = voltage > nominal_voltage * 1.15

spec voltage_range = voltage >= 2.5 && voltage <= 4.5
```

A parent instantiates it with the `component` keyword —
`component cell1: BatteryCell` inside `system Battery`.

## Lifted versus mapped

When a system is instantiated as a component, its signals and params are
**lifted** into the parent's schema under the component's name. An unmapped
`cell1: BatteryCell` therefore contributes `cell1::voltage`,
`cell1::temperature`, and `cell1::nominal_voltage` as parent inputs.

A component may instead **map** some of them, fixing their values from the
parent so they are no longer inputs:

```lilo
// Unmapped - all signals and params are lifted
component cell1: BatteryCell

// Partially mapped - voltage is mapped, temperature is still lifted
component cell2: BatteryCell {
  param nominal_voltage = 3.7
  signal voltage = voltage / 2.0  // derived from the parent's voltage
}
```

Consequence: mapped elements do not appear in the schema and must **not** be
supplied in a data or param file. In the example above the schema still exposes
`cell2::temperature`, but not `cell2::voltage` or `cell2::nominal_voltage`.

## Accessing component members

`::` reaches a component's signals, params, defs, and specs, at any depth:

```lilo
def low_battery: Bool = battery::level < 20.0
def bat_cell1_voltage: Float = battery::cell1::voltage
def any_cell_over_voltage: Bool = cell1::over_voltage || cell2::over_voltage

spec cells_safe = cell1::voltage_range && cell2::voltage_range
```

A parent may reach through two levels to its components' components, as in
`battery::cell1::voltage` and `battery::cell1::temperature`.

## `::` versus `.`

These look alike and are unrelated:

- `::` crosses a **scope** — a module namespace or a component instance.
  `battery::level` is the `level` signal of the `battery` component.
- `.` is **record projection** inside a single value. `gps.lat` is the `lat`
  field of a record-typed signal `gps`.

Both may appear in one expression. Choosing the wrong one is a type error at
best and a different requirement at worst. See
[lilo-expressions.md](lilo-expressions.md) for projection rules.

## System schema

The **schema** of a system is the set of signals and params constituting its
input; when monitoring, the user supplies values for exactly these. Mapped
component elements are excluded, since their values are derived.

Inspect it with `specforge schema`, which can print a flat listing including
defaults. Compare it against a data or param file by adding `--diff`, which
reports missing fields, extra fields, type mismatches, and places where a
scalar was expected but a record was supplied — including near-miss suggestions
for misspelled component paths.

This is inspection, not analysis, so it stays inside the skill's syntax-only
boundary; see [lilo-authoring.md](lilo-authoring.md). Data-file formats are
outside this reference — see `specforge doc data-files`.
