# Lilo Expressions and Types

Authoritative 0.5.10 reference: <https://docs.imiron.io/v/0.5.10/en/index.html>.
Owning page: `specforge doc lilo-language`. Consult it rather than guessing
whenever a construct here leaves a case open.

Lilo is expression-based: arithmetic and temporal properties alike are
expressions evaluating to a time-series value. Temporal operators live in
[lilo-temporal-semantics.md](lilo-temporal-semantics.md); declarations live in
[lilo-declarations.md](lilo-declarations.md).

## Comments

`/* … */` delimits a block comment. `//` comments to end of line. `///` is a
docstring and attaches documentation to the declaration that follows.

## Primitive types

- `Bool` — `true` and `false`.
- `Int` — integers, e.g. `42`.
- `Float` — floating point, e.g. `42.3`.
- `String` — double-quoted text, e.g. `"hello world"`.

`Int` and `Float` do not mix. With `x: Float` and `n: Int`, `x + n` is a type
error; convert explicitly with `float(n)`.

## Units of measure

A unit is written in angle brackets immediately after a numeric literal, which
changes its type from `Float` to a dimensioned type — `1.0<cm>` has type
`Float<cm>` and `100.0<km/h>` has type `Float<km/h>`.

Compound units combine with `/` (ratio), `*` (product), and `^`
(exponentiation); the literal `1` is the dimensionless unit, as in `60.0<1/s>`:

```lilo
50.0<m*m>
100.0<m^2>
9.81<m*s^-2>
```

Note `9.81<m*s^-2>` for an acceleration: a negative exponent is written
directly.

**Precedence.** `^` binds tightest, to the immediately preceding unit. `*` and
`/` have equal precedence and associate left-to-right. So `m/s*kg` means
`(m/s)*kg`, and `m*s^-2` means `m*(s^-2)`, not `(m*s)^-2`. Parenthesize to
override: `1.0<1/(kg*m)>`.

**Operations.** `+`, `-`, and comparison require both operands to carry the
same unit, or it is a type error. `*` and `/` accept differing units and
combine them: `100.0<km> * 2.0<s>` is `200.0<km*s>`, and `100.0<km> / 2.0<s>`
is `50.0<km/s>`.

**Inference.** Units are inferred where not written. In
`def f(speed) = speed * 5.0<s> <= 10.0<m>`, `speed` is inferred `Float<m/s>`.

**Identification.** Units are identified as strings, so `m` and `km` have
**no relation** as units. Relate them with an explicit conversion, multiplying
by a ratio literal such as `1000.0<m/km>`:

```lilo
def km_to_m(kilometre: Float<km>) = kilometre * 1000.0<m/km>
```

**Declaration.** A unit used in a type annotation must be declared, e.g.
`unit km`. Units are importable from a module — see
[lilo-modules-components.md](lilo-modules-components.md).

## Operator precedence

Highest to lowest:

1. prefix `-` (additive inverse) and `!` (negation)
2. `*` `/`
3. `+` `-`
4. comparisons `==` `!=` `>=` `<=` `>` `<`
5. temporal operators
6. `&&`
7. `||`
8. `=>` (implication) and `<=>` (equivalence)

Comparisons chain in a consistent direction: `0 < x <= 10` means
`0 < x && x <= 10`.

Prefix operators **cannot** be chained. Write `-(-x)` and `!(next p)`; the
unparenthesized forms are parse errors. Unary temporal operators may chain
without parentheses, as in `always eventually (x < 0)`.

## Built-in functions

| Function | Meaning and restriction |
| --- | --- |
| `float` | `Int` → `Float`, e.g. `float(n)`. |
| `time` | the current time of the signal. |
| `sqrt` | square root; the argument must be an `Int` or a **dimensionless** `Float`. |
| `abs` | absolute value of an `Int` or `Float`; **units are preserved**. |
| `max(x, y)` | maximum of two or more values, all of the same type and units. |
| `min(x, y)` | minimum of two or more values, all of the same type and units. |

Trap: `max(x, y)` and `min(x, y)` are pointwise over their arguments at one
sample. The rolling-window extrema over an interval are `max_past`,
`min_past`, `max_future`, and `min_future`, documented in
[lilo-temporal-semantics.md](lilo-temporal-semantics.md). Choosing the wrong
family silently changes the requirement.

## Conditional expressions

`if` / `then` / `else` is an **expression**, not a statement, so the `else`
branch is **mandatory** and both branches must produce compatible types. The
condition must be `Bool`. Conditionals nest:

```lilo
def describe_temp(temp: Float): String =
  if temp > 30.0
    then "hot"
  else if temp < 10.0
    then "cold"
  else
    "moderate"
```

Evaluation is **pointwise**: the condition is applied at each time point
independently.

## Case expressions

When all branches are `Bool`, use a `cases {` … `}` expression whose entries
are `guard -> consequence;`:

```lilo
cases {
  temp > 30.0 -> eventually temp < 20.0;
  temp < 10.0 -> eventually temp > 20.0;
  10.0 <= temp <= 30.0 -> true;
}
```

This is interpreted as the conjunction
`(temp > 30.0 => eventually temp < 20.0) && (temp < 10.0 => eventually temp > 20.0) && (10.0 <= temp <= 30.0 => true)`.
A `-> true` branch may therefore be omitted, but prefer **exhaustive** and
**disjoint** guards for clarity — SpecForge checks exactly those properties,
see [lilo-static-analysis.md](lilo-static-analysis.md).

Prefer `cases` over a hand-written chain of implications for a multi-regime
requirement: the guards become explicit and checkable.

## Record types

Records are anonymous, **structurally typed**, and extensible.

**Construction.** A comma-separated list of `field = value` pairs in braces;
field order does not matter, so `{ foo = 42, bar = "hello" }` is a two-field
record.

That value has type `{ foo: Int, bar: String }`. Naming the type with a `type`
declaration is recommended — see
[lilo-declarations.md](lilo-declarations.md).

**Field punning.** When a name in scope should be copied in, `{ foo }` is
shorthand for `{ foo = foo }`. Punning works anywhere fields are listed.

**Path construction.** Assign a dotted path to build or extend nested records
in one step; paths merge and their order does not matter, as in
`{ status.throttle = 0, status.fault = false }` for a record whose `status`
field is itself a record.

A dotted path **cannot** be combined with punning: write
`{ status.throttle = throttle }`, not `{ status.throttle }`.

**Updates.** `{ base with fields }` copies a record and overrides fields,
accepting assignments, puns, and paths — `{ base with status.throttle = 70 }`
rewrites one nested field and keeps the rest.

All updated fields **must already exist** in the base record.

**Projection.** `.` accesses a field, and chains through nesting: `p.x`, and
`c.center.x` for a record inside a record. Note that `.` is projection within
a value, while `::` crosses a module or component scope — see
[lilo-modules-components.md](lilo-modules-components.md).

## Enum types

Enums are nominal and carry no payload. Constructors begin with `#` and are
listed after the type name, as in `enum Color = #Red | #Green | #Blue`.

Each enum forms its own namespace and is open by default, and different enums
may share constructor names. A constructor may be written bare or qualified:
`#Red`, `#Color::Red`, `#Utils::Color::Red`. Constructors support equality:

```lilo
def is_red(c: Color): Bool = c == #Red
```

In data files, constructors are written with the leading `#`, unquoted and
unqualified.

## Pattern matching

`match` currently supports enums only, over an exhaustive set of cases:

```lilo
def is_green(c: Color): Bool =
  match c {
    #Red -> false;
    #Color::Green -> true;
    #Utils::Color::Blue -> false;
  }
```

Qualified constructors in cases disambiguate names shared by two enums.

## Local bindings

A local binding has the form `let name = expression1; expression2`. It binds
the result of `expression1` to `name`, visible only within `expression2`.
Bindings chain, and the bound type is inferred:

```lilo
def circumcircle(a: Float, b: Float, c: Float): Float =
  let s = (a + b + c) / 2.0;
  let area = sqrt(s * (s - a) * (s - b) * (s - c));
  (a * b * c) / (4.0 * area)
```

Use `let` to name sub-expressions for readability and to avoid repeating a
sub-expression.
