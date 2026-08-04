# UPPAAL modelling language reference

Distilled for model *construction*. Full grammar: <https://docs.uppaal.org/language-reference/>.
UPPAAL models are **networks of timed automata** extended with data variables. Expression
syntax is C-like.

## Declarations (global, or local to a template)

Syntax mirrors C. Terminate each with `;`.

```c
clock x, y;                 // real-valued clocks
int n;                      // int, machine default domain
int[0,9] d;                 // bounded int, domain 0..9
bool b;
int a[4];                   // array, elements a[0]..a[3]
int m[4] = {1,2,3,4};       // array initialiser
const int N = 6;            // constant
const int[0,1] YES = 1;
typedef int[0,N-1] id_t;    // type declaration
typedef struct { int a; int b; } pair;   // record type
meta int tmp;               // meta var: stored but NOT part of the state (states equal if only meta differs)
```

### Channels (for synchronisation)
```c
chan a, b;                  // ordinary: two-way rendezvous, a! blocks until an a? is ready
urgent chan hurry;          // urgent: no time may pass while a synchronisation is enabled
broadcast chan bc;          // 1-to-many: sender never blocks; all enabled receivers sync
chan c[3];                  // array of channels
```

## Locations
- **Normal** — time may pass, bounded only by the location's invariant.
- **Invariant** — a clock **upper-bound** constraint (`x<=5`, `y<10`), possibly conjoined
  (`x<=5 && y<=10`). It is the *only* mechanism that forces a component to leave a location.
  Lower bounds are **not** allowed in invariants (put them in edge guards).
- **Urgent** (`<urgent/>`) — no delay is allowed in this location (but other components may
  still act). Removes the need for a `x:=0 … x<=0` clock trick.
- **Committed** (`<committed/>`) — no delay, **and** the next transition of the whole network
  must involve an edge out of a committed location. Use for atomic sequences (e.g. passing a
  value through a temp variable, or emitting two synchronisations "simultaneously"). Urgent and
  committed locations reduce clock usage and thus verification cost.

## Edges (transitions)
An edge from a source to a target location carries up to four optional labels:

| Label kind | Meaning | Example |
|---|---|---|
| `select` | Bind a local var to a non-deterministic value from a range | `i : int[0,42]` |
| `guard` | Enabling condition: clock lower/upper bounds and/or data conditions, conjoined with `&&` | `x>=2 && i==3` |
| `synchronisation` | One channel action: `a!` (send) or `a?` (receive); at most one per edge | `appr!` |
| `assignment` | Comma-separated updates: clock resets and variable updates | `x := 0, i := i+1` |

Guard clock constraints compare a clock (or difference of clocks) to an integer:
`x < c`, `x <= c`, `x >= c`, `x > c`, `x - y <= c`, combined with `&&` (and, via negation, `||`).

**Restriction:** an edge whose synchronisation is on an **urgent** or **broadcast** channel may
**not** carry a clock guard (data guards and invariants are fine).

## Timed-automata semantics (why the above works)
- A **state** is `(location vector, clock valuation, data valuation)`; clocks are real-valued.
- **Action transition** — follow an edge if its guard holds; apply resets/updates; the target's
  invariant must hold afterwards. Instantaneous (no time passes).
- **Delay transition** — stay in the current location(s) and let all clocks advance by the same
  real amount `d`, provided every invariant stays true throughout.
- **Invariants ensure progress**; guards enable/disable; non-determinism comes from choosing
  *when* to act (delay vs. transition) and *which* enabled edge to take.

## Templates, parameters, instantiation
A template is a parameterised automaton. Parameters are call-by-value (bounded int / scalar) or
call-by-reference (`&`). Instantiate in the `<system>` section:

```c
Train(const id_t id, id_t &e)   // template header (in <parameter>)
...
Train1 = Train(1, el);          // process assignment
Train2 = Train(2, el);
system Train1, Train2, Gate;    // list all processes to compose
```
A parameterised template can also be composed directly (`system Train, Gate;`) — UPPAAL binds
free bounded-int/scalar parameters to one process per value.

## Expression operators (on data, not clocks)
- Logical: `&&`, `||`, `!`
- Bitwise: `&`, `|`, `^`; shifts `<<`, `>>`
- Arithmetic: `+ - * / %`
- Compound assignment: `+=`, `-=`, `*=`, `/=`, `%=`, `<<=`, `>>=`, and `:=`
- Increment/decrement: `++`, `--`
- Conditional (C ternary): `cond ? a : b`
- Quantifiers over ranges: `forall (i:int[0,N]) expr`, `exists (i:int[0,N]) expr`

## Query language (TCTL) — what to verify
A query is a **path quantifier** over a **state formula** `p`. State formulae: `Proc.Location`,
clock/data guards, `deadlock`, combined with `and`/`or`/`not`/`imply`.

| Query | Name | Meaning |
|---|---|---|
| `E<> p` | Reachable | some reachable state satisfies `p` (sanity checks) |
| `A[] p` | Invariant / safety | `p` holds in **all** reachable states ("something bad never happens") |
| `E[] p` | Potentially always | there is a path on which `p` holds forever |
| `A<> p` | Inevitable / liveness | every path eventually reaches a `p`-state |
| `p --> q` | Leads-to (response) | `A[] (p imply A<> q)` — whenever `p`, then eventually `q` |

Guidance:
- **Safety**: state it positively — `A[] not (Light.On && Light.Off)` style, or `A[] not bad`.
- **Deadlock freedom**: `A[] not deadlock`.
- **Bounded response**: combine with a clock, e.g. reset a clock on `p` and check
  `A[] (obs.waiting imply obs.t <= D)`.
- Choosing the query that matches the real requirement is a **validation** act — a green result
  only proves the model satisfies *that* formula.

## Statistical model checking (UPPAAL SMC) — brief
For stochastic timed automata (probabilistic edge choices, distributions over delays, ODEs for
continuous variables). Query forms: simulation `simulate [<=T] {exprs}`, probability estimation
`Pr[<=T](<> p)`, hypothesis testing `Pr[...](...) >= p0`, and probability comparison. Use only
when the requirement is probabilistic; classic TCTL above covers deterministic timing.
