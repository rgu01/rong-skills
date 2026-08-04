# UPPAAL `.xml` model file format

The modern UPPAAL native format is a single `.xml` file (GUI native since v3.2) that holds
**everything**: global declarations, all templates, the system declaration, and — in current
versions — the verification **queries**. A separate `.q` file is legacy and optional; prefer
embedding queries in the model.

Source: <https://docs.uppaal.org/toolsandapi/file-formats/> and
<https://docs.uppaal.org/language-reference/>. The format is deliberately abstract: label
contents (guards, invariants, assignments, …) are stored as **plain strings** — UPPAAL parses
them when it loads the model, so the XML layer does not validate expression syntax.

## Skeleton

```
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE nta PUBLIC '-//Uppaal Team//DTD Flat System 1.6//EN' 'http://www.it.uu.se/research/group/darts/uppaal/flat-1_6.dtd'>
<nta>
    <declaration> ... global declarations ... </declaration>
    <template> ... automaton 1 ... </template>
    <template> ... automaton 2 ... </template>
    <system> ... process instantiation + `system ...;` ... </system>
    <queries>
        <query><formula>...</formula><comment>...</comment></query>
    </queries>
</nta>
```

## Element reference

- **`<nta>`** — root. Network of Timed Automata.
- **`<declaration>`** (global, direct child of `<nta>`) — clocks, channels, ints, consts,
  typedefs, functions. Plain text.
- **`<template>`** — one automaton. Children, in order:
  - `<name>Foo</name>` — template name.
  - `<parameter>const id_t id, id_t &e</parameter>` — optional; `&` marks reference params.
  - `<declaration>clock x;</declaration>` — optional local declarations.
  - `<location id="idN" x=".." y="..">` (repeatable) — attributes `id` (unique, referenced
    elsewhere), plus `x`/`y` layout coords (integers; y grows downward). Children:
    - `<name x=".." y="..">Loc</name>` — optional but recommended (used in queries as `Proc.Loc`).
    - `<label kind="invariant" x=".." y="..">x&lt;=5</label>` — optional clock/upper-bound invariant.
    - `<committed/>` **or** `<urgent/>` — optional; marks the location committed or urgent.
  - `<init ref="idN"/>` — exactly one; the initial location.
  - `<transition id="idN">` (repeatable) — an edge. Children:
    - `<source ref="idA"/>`, `<target ref="idB"/>` — required.
    - `<label kind="select" x=".." y="..">i : int[0,4]</label>` — optional non-deterministic binding.
    - `<label kind="guard" x=".." y="..">x&gt;=2 &amp;&amp; i==3</label>` — optional.
    - `<label kind="synchronisation" x=".." y="..">a!</label>` — optional; `a!` send, `a?` receive.
    - `<label kind="assignment" x=".." y="..">x := 0, i := i+1</label>` — optional; comma-separated.
    - `<nail x=".." y=".."/>` — optional, repeatable, in order; a turning point the edge is routed
      through. Use nails to bend an edge away from another edge between the same two locations so the
      arrows and labels don't overlap (see "Layout & readability" below).
  - Every `<label>` (and `<location>`/`<name>`) accepts `x`/`y`. Positions are optional for loading
    but essential for a readable diagram.
- **`<system>`** — process assignments and the `system P1, P2;` line. Plain text.
- **`<queries>`** — modern query storage. Each `<query>` has a `<formula>` (the TCTL query,
  XML-escaped) and a `<comment>` (what it checks / why). Newer GUIs may add extra children
  (`<result>`, options) — a minimal `<formula>`+`<comment>` always loads.

Note the British spelling **`synchronisation`** for the label kind — it is exact.

## XML escaping (critical)

Guards/invariants/assignments frequently contain `<`, `>`, `&`. Inside label text these MUST
be escaped, or the file will not parse:

| Source | In XML |
|---|---|
| `x<=5` | `x&lt;=5` |
| `x>3` | `x&gt;3` |
| `i==3 && j<2` | `i==3 &amp;&amp; j&lt;2` |
| `E<> P.done` | `E&lt;&gt; P.done` |

## Complete, loadable example — timed light control + user (mirrors the lecture example)

Two templates synchronise on `press`. The `Light` uses clock `x` to tell a *quick* second
press (`x<=3` → Bright) from a *slow* one (`x>3` → Off).

```xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE nta PUBLIC '-//Uppaal Team//DTD Flat System 1.6//EN' 'http://www.it.uu.se/research/group/darts/uppaal/flat-1_6.dtd'>
<nta>
	<declaration>// Global declarations
chan press;</declaration>
	<template>
		<name>Light</name>
		<declaration>clock x;</declaration>
		<location id="id0"><name>Off</name></location>
		<location id="id1"><name>On</name></location>
		<location id="id2"><name>Bright</name></location>
		<init ref="id0"/>
		<transition>
			<source ref="id0"/>
			<target ref="id1"/>
			<label kind="synchronisation">press?</label>
			<label kind="assignment">x := 0</label>
		</transition>
		<transition>
			<source ref="id1"/>
			<target ref="id2"/>
			<label kind="guard">x &lt;= 3</label>
			<label kind="synchronisation">press?</label>
		</transition>
		<transition>
			<source ref="id1"/>
			<target ref="id0"/>
			<label kind="guard">x &gt; 3</label>
			<label kind="synchronisation">press?</label>
		</transition>
		<transition>
			<source ref="id2"/>
			<target ref="id0"/>
			<label kind="synchronisation">press?</label>
		</transition>
	</template>
	<template>
		<name>User</name>
		<location id="id3"><name>Idle</name></location>
		<init ref="id3"/>
		<transition>
			<source ref="id3"/>
			<target ref="id3"/>
			<label kind="synchronisation">press!</label>
		</transition>
	</template>
	<system>// Process instantiation and system definition
system Light, User;</system>
	<queries>
		<query>
			<formula>E&lt;&gt; Light.Bright</formula>
			<comment>Reachability: the light can eventually become bright.</comment>
		</query>
		<query>
			<formula>A[] not deadlock</formula>
			<comment>Safety: the system never deadlocks.</comment>
		</query>
	</queries>
</nta>
```

## Layout & readability (coordinates, nails, multi-line labels)

A model that *loads* is not automatically one a human can *read*. The XML stores editor layout,
and UPPAAL preserves and re-saves it — so emit it deliberately. Three levers:

- **Coordinates** — `<location x y>`, its `<name x y>`, and every `<label kind=… x y>` carry
  positions (integers; y increases downward). Place each label clear of its edge and of every
  other label. **All labels — guards, assignments (updates), synchronisations, selects,
  invariants — must not overlap each other or the edges.**
- **Nails** — `<nail x y/>` inside a `<transition>` (repeatable, in order) are turning points the
  edge routes through. Primary use: when two transitions join the same pair of locations (a
  forward edge and its return), route one through nails that bow it away from the other, so the
  two arrows and their label groups separate cleanly instead of stacking.
- **Multi-line labels** — a long guard or assignment may contain literal newlines; UPPAAL renders
  each line on its own row. Split a long comma-separated assignment across lines so it stays
  narrow and doesn't run across the diagram.

Example — a forward edge bowed up over two nails, assignment split across three lines (from the
bridge model). The return edge (id1 → id0) is drawn straight, so these nails at y=-34 lift the
forward edge above it and they never overlap:

```xml
<transition id="id2">
    <source ref="id0"/>
    <target ref="id1"/>
    <label kind="select" x="42" y="-59">i : int[0,3], j : int[0,3]</label>
    <label kind="guard" x="42" y="-85">i &lt;= j &amp;&amp; side[i] == torch &amp;&amp; side[j] == torch</label>
    <label kind="assignment" x="42" y="-153">ci := i, cj := j,
dur := (t[i] &gt; t[j] ? t[i] : t[j]),
y := 0</label>
    <nail x="42" y="-34"/>
    <nail x="442" y="-34"/>
</transition>
```

Omit all coordinates and UPPAAL still loads the model and auto-lays it out — but the result is
usually cramped with overlapping labels. Supplying coordinates + nails is how you keep it clean.

## Emit checklist
- [ ] XML declaration + correct `<!DOCTYPE nta ... flat-1_N.dtd>` present (current UPPAAL writes
      `flat-1_6.dtd`; `flat-1_1.dtd` also loads — match what your UPPAAL saves).
- [ ] Every template has a `<name>`, exactly one `<init>`, and unique `<location id=...>`.
- [ ] Every `<source>/<target>/<init>` `ref` points to an existing location `id`.
- [ ] All `<`, `>`, `&` inside `<label>`/`<formula>` are escaped.
- [ ] `synchronisation` labels come in matching `!`/`?` pairs across templates (or use broadcast).
- [ ] No clock guard on an edge with an urgent/broadcast synchronisation.
- [ ] `<system>` instantiates and lists every process; `<queries>` holds the TCTL checks.
- [ ] Where two edges join the same pair of locations, one is routed through `<nail>`s so the
      arrows and labels don't overlap.
- [ ] Labels are positioned (x/y) clear of edges and each other; long guards/assignments are
      split across multiple lines.
