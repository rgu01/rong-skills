# Lilo Declarations

Authoritative 0.5.10 reference: <https://docs.imiron.io/v/0.5.10/en/index.html>.
Owning page: `specforge doc lilo-systems`. Consult it rather than guessing
whenever a construct here leaves a case open.

This file gives the syntax of every declaration keyword. For the expressions
that fill their bodies see [lilo-expressions.md](lilo-expressions.md) and
[lilo-temporal-semantics.md](lilo-temporal-semantics.md); for `module`,
`component`, and `pub` see
[lilo-modules-components.md](lilo-modules-components.md); for attributes and
stubs see [lilo-attributes.md](lilo-attributes.md); for naming see
[lilo-conventions.md](lilo-conventions.md).

## System header

A system groups the temporal input signals, the non-temporal parameters, the
auxiliary definitions, and the specifications. A system file starts with a
system declaration:

```lilo
system Engine
```

The system name should **match the file name** — `system Engine` in
`Engine.lilo`.

Practical note: a project may omit the header, in which case the system name
comes from the file name. `temperature_sensor.lilo` in the example projects
opens with an import and declares signals directly. An absent header is not a
defect to repair; do not add one unless the user asks.

## `type`

A named type is declared with `type`. Record shapes are the common case, e.g.
`type Point = { x: Float, y: Float }`.

`Point` is then usable as a type anywhere in the file. Naming a record type is
recommended over repeating a structural type.

## `signal`

Signals are the time-varying values of the system, declared as
`signal x: Float`:

```lilo
signal speed: Float
signal rain_sensor: Bool
```

A signal may have any type that contains no **function types** — that is, any
combination of primitive types and records. Definitions and specifications may
refer to the system's signals freely.

## `param`

Parameters are the values of a system that are constant over time, declared as
`param temp_threshold: Float`:

```lilo
param temp_threshold: Float
param max_errors: Int
```

Parameters must be supplied before monitoring can begin. For exemplification
they are optional: supply them and the example must conform, or omit them and
the exemplifier searches for values that work. For default values see
[lilo-attributes.md](lilo-attributes.md).

## `def`

A definition names a reusable expression. The three documented shapes are
`def foo: Int = 42` for an annotated constant expression,
`def foo(x: Float) = x + 42` for a function with an inferred return type, and
`def foo(x: Float): Float = x + 42` with the return type written out.

Argument and return type annotations are optional and otherwise inferred, but
writing them is recommended as documentation. Arguments may be record-typed:

```lilo
type S = { x: Float, y: Float }

def more_x_than_y(s: S) = s.x > s.y
def foo(s: S) = eventually [0,1] more_x_than_y(s)
```

Definitions may call other definitions, may appear in any order, and must not
be **circular**. They may use the system's signals without declaring them as
arguments.

## `spec`

A `spec` states something that should be true of the system, and may use all
of the system's signals and definitions. It is like a `def` except:

- the return type is always `Bool`, and need not be written; and
- specs **cannot have parameters**.

```lilo
signal speed: Float

def above_min = 0 <= speed
def below_max = speed <= 100

spec valid_speed = always (above_min && below_max)
```

**A family of related obligations.** Because a spec takes no parameters, use a
parameterized `def` returning `Bool` and conjoin its instances in one spec:

```lilo
def gear_steady_for(g: Int): Bool =
  always [0.0, 30.0] ((!(gear == g) && next (gear == g))
                      => next (always [0.0, 2.5] (gear == g)))

spec gear_steady =
  gear_steady_for(1) && gear_steady_for(2) && gear_steady_for(3)
```

One spec may also reference another by name, since a spec is an expression of
type `Bool`.

For a requirement that cannot yet be formalized, use a documented spec stub —
see [lilo-attributes.md](lilo-attributes.md).

## `assumption`

An `assumption` declares a property taken as given when analysing the system.
Syntactically it matches a `spec` — no parameters, always `Bool` — but the
tooling treats it as a constraint on exemplification and satisfiability rather
than something to verify:

```lilo
signal temperature: Float
signal heater_on: Bool

assumption physics = always (heater_on => next temperature >= temperature)

spec eventually_warm = eventually (temperature > 30.0)
```

Here `physics` must hold for any trace SpecForge generates. Do not modify an
existing `assumption` to make a new requirement easier to express unless the
user explicitly asked for that change.
