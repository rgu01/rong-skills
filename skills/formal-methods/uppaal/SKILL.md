---
name: uppaal
description: Use when asked to build, generate, fix, or review a UPPAAL model — a network of timed automata, clocks/guards/invariants, synchronisation channels, urgent/committed locations, templates, or TCTL verification queries — and especially to emit a single runnable UPPAAL model `.xml` (with queries embedded) that loads and verifies in UPPAAL. Covers the UPPAAL modelling language and the concrete `.xml` file format.
---

# UPPAAL — build correct, runnable timed-automata models

## Core principle
A model is only useful if it (a) loads and verifies in UPPAAL and (b) faithfully captures
the *intended* system. This skill makes (a) reliable; **(b) is a human validation judgment**
that model checking cannot supply — the checker only proves what you actually asked.

Authoritative source of truth: <https://docs.uppaal.org/>. When unsure about current syntax
or the file format, check the docs rather than guessing.

## Clarity guardrail
Never use an acronym without spelling out the full name the first time: TA (timed automaton),
TCTL (Timed Computation Tree Logic), NTA (network of timed automata).

## Model-building workflow
1. **Decompose the system into templates.** Each concurrent component (controller, task,
   channel, environment actor) becomes one template = one timed automaton. Shared events
   between components become **channels**.
2. **Per template, design the automaton:**
   - **Locations** = modes. Mark exactly one as `init`. Use **invariants** (upper bounds on
     clocks, e.g. `x<=5`) to *force progress* — an invariant is the only thing that stops a
     component delaying forever in a location.
   - **Clocks** measure elapsed time; reset on the edges where "the timer starts".
   - **Edges** carry: a **guard** (enabling condition — clock lower bounds and/or data
     conditions), an optional **synchronisation** (`a!` / `a?`), and **assignments** (clock
     resets, variable updates). All are optional.
3. **Choose channel kinds** (see reference): regular (two-way rendezvous), **urgent** (fire
   as soon as enabled — no delay; *no clock guards allowed* on such edges), **broadcast**
   (one sender, many receivers, sender never blocks).
4. **Remove unwanted delay / enforce atomicity** with **urgent** locations (no delay here) or
   **committed** locations (no delay *and* the next transition must involve this component) —
   both also reduce the clock count and thus verification cost.
5. **Write the system declaration:** instantiate templates into processes and list them after
   the `system` keyword.
6. **Formalise requirements as TCTL queries** (`E<>`, `A[]`, `A<>`, `E[]`, `p --> q`) and
   **embed them in the `<queries>` block** of the same `.xml` (modern UPPAAL needs no separate
   `.q` file). Choosing the *right* query is validation — say in a comment what each checks.
7. **Emit one valid `.xml`, then verify.** Read counterexample traces, reconcile them against
   the intent, and refine. Never fabricate a trace — run the tool.

## Non-negotiable correctness rules
| Rule | Why |
|---|---|
| Escape `<`, `>`, `&` inside label text as `&lt;`, `&gt;`, `&amp;` | Labels are XML text; raw `<` breaks the file. |
| Invariants use **upper bounds only** (`<`, `<=`) | UPPAAL requires it; lower bounds go in guards. |
| **No clock guard** on an edge with an **urgent** or **broadcast** synchronisation | Language restriction; data guards are fine. |
| Every `<location>` has a unique `id`; `<init>` and every `<source>/<target>` ref an existing id | Dangling refs fail to load. |
| Exactly one `<init>` per template | A template must have an initial location. |
| Correct `<!DOCTYPE nta ... flat-1_6.dtd>` (or the version your UPPAAL writes) and `<nta>` root | Required for UPPAAL to parse the file. |

## Readability (editor layout)
A model that loads is not automatically one a human can read — supply editor layout so the
diagram is clean:
- Give locations, names, and every label `x`/`y` coordinates; keep each label (guard,
  assignment/update, synchronisation, select, invariant) from overlapping edges or other labels.
- When two edges join the same pair of locations, route one through `<nail>` turning points so
  the two arrows and their labels separate instead of stacking.
- Split a long guard or assignment across multiple lines (literal newlines in the label text).

See `reference/xml-file-format.md` → "Layout & readability".

## References (read on demand)
- **`reference/modeling-language.md`** — the UPPAAL modelling language: declarations (clocks,
  bounded ints, arrays, constants, channel kinds), locations (urgent/committed), edges
  (guard/select/sync/assignment), invariants, templates & parameterised instantiation,
  select/meta/`forall`/`exists`, expression operators, and the TCTL query language & patterns.
- **`reference/xml-file-format.md`** — the concrete `.xml` structure with a complete,
  annotated, loadable example including the embedded `<queries>` block, plus an emit checklist.

## Common mistakes
| Mistake | Fix |
|---|---|
| Unescaped `x<=5` in a label | Write `x&lt;=5`. |
| Modeling "as fast as possible" with only invariants | Use an urgent channel/location — pure invariants can't force a rendezvous. |
| Assuming a passing query means the model is correct | It means the model satisfies *that* formula. Validate the model *and* the formula against intent. |
| Emitting a separate `.q` file | Embed queries in the model `.xml` `<queries>` block. |
| Presenting a hand-written "counterexample" | Generate it in UPPAAL; the tool's trace is the evidence. |
