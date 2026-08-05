# FRET, part 1: Concepts, FRETish, and AI-assisted formalization

A study summary of NASA's **FRET** (Formal Requirements Elicitation Tool,
<https://github.com/NASA-SW-VnV/fret>) — what it is, the FRETish language, and
how an AI agent can help turn an English requirement into FRETish. Companion
note: [`fret-cli-and-setup.md`](fret-cli-and-setup.md) covers the CLI and install.

FRET solves the same problem industrial formal-methods engineers solve by hand: taking a
near-natural-language requirement and turning it into precise temporal logic you
can verify against. It is Apache-2.0, latest release **v3.1.0** (March 2026).

---

## The map everything hangs on

```
Your intent (fuzzy, in your head / in a Word doc)
      │  you write it in FRETish  (structured, 6 slots)
      ▼
FRETish requirement  ──►  FRET parses & type-checks it
      │
      ├──►  English "semantics" gloss   "this requirement means: …"
      ├──►  Simulation diagram          a timeline of exactly when the response must hold
      └──►  Formalization
               ├─ Metric/mixed LTL   (past-time + future-time)   → generic
               └─ CoCoSpec contract  (Lustre)                    → Simulink models, checked by Kind2
```

The reason FRET exists is the **middle branches**: the gloss + diagram let you
confirm *"did I write what I meant?"* **before** trusting the generated logic.
That is the classic requirements-ambiguity gap — the same one you close by hand
turning a natural-language safety requirement into a formal specification language. The "E" in FRET is **Elicitation**:
vagueness is the *starting* state it is built to resolve, not a disqualifier.

---

## FRETish — the language (the core of everything)

A FRETish requirement is **one sentence** built from six ordered fields:

```
[scope]  [condition]  component  shall  [timing]  response
```

| # | Field | Mandatory? | Fixes | Example words |
|---|-------|-----------|-------|---------------|
| 1 | **scope** | optional | *which mode(s)* the requirement is active | `In takeoff mode`, `Before X`, `After X`, `Only in Y`, `Not in Z` |
| 2 | **condition** | optional | a *trigger / precondition* that arms the response | `when alt > 100`, `upon boot`, `if fault`, `whenever …` |
| 3 | **component** | **required** | *who* is responsible (subject of "shall") | `the autopilot`, `sensor` |
| 4 | **shall** | **required** | the obligation keyword | `shall` |
| 5 | **timing** | optional | *when / how long* the response must hold | `immediately`, `always`, `eventually`, `within 5 ticks`, `for 3 ticks`, `until X` |
| 6 | **response** | **required** | *what* must become true (Boolean over variables) | `satisfy output = TRUE` |

- Only **component + shall + response** are mandatory.
- Omit `scope` → active for the whole run. Omit `timing` → "always, while armed".
- FRET counts in **ticks** (discrete steps). "within 3 seconds" becomes
  "within 3 ticks" once you fix one tick = one second for your product.

**Worked example** — English:
> *"The controller must turn on the warning light within 3 seconds of detecting an overheat."*

FRETish:
```
when overheatDetected the controller shall within 3 ticks satisfy warningLight
```
fields: condition=`when overheatDetected`, component=`the controller`,
timing=`within 3 ticks`, response=`satisfy warningLight`.

---

## Variables are the interface, not the implementation

`condition` and `response` are **not free English** — they are Boolean/typed
expressions over the product's **variables** (`warningLight`, `overheatDetected`).
Two things people get wrong:

1. **You do NOT need to read source code.** FRETish references the product's
   *observable interface* (signals/outputs) — a spec-level artifact (interface
   control document, signal list, data dictionary). Reading code is only a
   fallback when the spec is missing.
2. **You declare variables as you write.** FRET *extracts* the names you used
   and drops them into a Variables view where you assign each a **type**
   (Boolean, int, enum…) and a **role** (Input / Output / Mode / Internal). No
   model or code required; connecting them to a real model is a later, optional
   step.

The small act of naming a variable is often what forces you to decide what you
actually want ("is `ready` a Boolean flag or a mode?"). That is elicitation
working.

---

## The AI-assisted formalization workflow

Goal: give an English requirement → AI drafts FRETish → a tool validates it →
result shown back user-friendly.

> **Golden rule: AI is the drafting accelerator; FRET's parser + semantics gloss
> + simulation are the judge.** Everything AI produces is a *proposal with flags
> attached*, not ground truth. AI proposes, you and FRET dispose.

The four parts:

1. **Extract from Word.** Read the `.docx`. Raw prose is usually *compound* —
   one Word "shall" often becomes *several* atomic FRETish requirements (FRET
   wants each requirement single, testable, about one observable output). First
   real work is splitting into atomic obligations, not syntax.
2. **Pin down variables.** AI extracts a *candidate* variable list (name, guessed
   type, guessed role) from specs/interface docs. Trust levels:
   - **From specs / interface docs → high trust** (already describe observable signals).
   - **From source code → low trust, needs filtering** — code is full of
     *internal* variables that are not the observable interface. Grabbing an
     implementation detail makes the requirement constrain internals, not
     behavior (the design-vs-requirement mixing to avoid). Flag "looks internal —
     observable?" as a finding.
3. **AI drafts the FRETish** — maps prose to the six fields; returns the sentence
   plus a variable table with per-variable questions/findings for you to resolve.
4. **Validate + iterate** — run it through FRET (`fretcli formalize`), read the
   generated logic / gloss, correct, repeat.

Gaps and unclear names become **findings to resolve, not blockers** — consistent
with the object-model (OM) methodology.

---

## How this maps to the skill / MCP world

- FRETish ≈ a controlled front-end over a formal specification language.
- The formalization engine ≈ deterministic **grounding**: FRETish in → LTL out.
  It is a natural **L1 MCP tool** an agent wraps.
- The AI does the reasoning/synthesis (drafting, decomposition, rendering); the
  tool stays authoritative only for what it explicitly returns.
- A future **FRET skill** orchestrates the loop (extract → draft → validate →
  render) while the tool/CLI does the executable work — the same two-layer
  MCP-server + skill design used for other verification toolchains.

See [`fret-cli-and-setup.md`](fret-cli-and-setup.md) for the concrete CLI and the
verified two-tier setup.
