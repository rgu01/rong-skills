# Rebuild Design — "Formal Modeling & Analysis of Real-Time Systems" (AI-era edition)

## Context

The existing lecture deck (`Slides.pptx`, 96 slides) teaches formal methods, model
checking, timed automata, and UPPAAL to embedded-systems students. Two things have
changed the teaching goal:

1. **AI can now do the mechanical modeling.** Drawing automata and wiring up UPPAAL
   syntax — the entire Annex (slides 63–96) — is exactly what a capable LLM does well.
   We are dropping that mechanical-syntax teaching.
2. **But students must still understand formal models** so they don't blindly trust AI,
   and the assignment must be **AI-resistant**: pasting it into any AI tool must not
   produce a complete, submittable solution.

This document specifies two deliverables:

1. A **new, template-free presentation** rebuilt from slides 1–2 (reused) and 4–62
   (re-authored with an AI-era lens), excluding slide 3 and the Annex — and now including a
   focused block that teaches students *how to use AI* for formal modelling.
2. A **UPPAAL Agent Skill** (`skills/uppaal/`) so a student's AI can build correct, runnable
   UPPAAL models — the AI-side mechanics that replace the dropped Annex.

## The spine (thesis)

We anchor the whole AI narrative on the deck's **own** verification-vs-validation
distinction (slide 7), rather than bolting on a new frame:

- **Verification** — *"did we build the thing right?"* — exhaustive, symbolic,
  automatable. **This is where AI helps most:** generating models, drafting TCTL
  properties, running tools.
- **Validation** — *"did we build the right thing?"* — connecting the formal model to
  messy real-world intent. **This lives outside the formal system, so AI cannot own it**
  — it only has access to what you typed, not to the true intent.

Two reinforcing messages fall out:

- **Exhaustive ≠ probabilistic ("powerful ≠ certain").** Model checking gives certainty
  over *all* behaviours; an LLM gives a plausible artifact fast, with no guarantee.
  State-space explosion (slides 8–9) is an open problem *orthogonal* to how good LLMs
  get — the concrete rebuttal to "why model-check at all now?"
- **AI lowers the cost of formal methods** (historically the barrier) while **raising the
  importance** of the durable human skills: *specify, validate, judge the counterexample.*

Recurring one-liner for the deck: **"AI manipulates the symbols; it cannot supply the
intent or the guarantee."**

## Deck structure: keep / reframe / add / drop

- **KEEP unchanged (the math doesn't move):** timed-automata definition & semantics,
  invariants, clock constraints, task models, TCTL, quantifiers, property patterns,
  networks of TA.
- **REFRAME (motivation/emphasis only):** the V&V slide (thesis anchor), the
  exhaustiveness/state-explosion slides, the UPPAAL workflow slide (de-emphasise GUI
  mechanics, emphasise the verify→interpret→refine loop), and the worked examples
  (AI builds → you verify/validate).
- **ADD:** an "FM in the age of AI" framing slide; a **focused "how to use AI for formal
  modelling" block (~3–4 slides)**; an "AI builds a model → verification catches its flaw"
  demo slide; and a closing "what's yours vs. the AI's" reflection slide before the assignment.
- **DROP:** slide 3 (stray screenshot), and the entire Annex (63–96, UPPAAL syntax) — the
  syntax mechanics move into the **UPPAAL skill** (see "Second deliverable" below), which the
  students' AI uses instead of learning by hand.

### New "How to use AI for formal modelling" block (~3–4 slides)

We ask students to build models *with* AI, so we must teach that particular skill rather than
assume it. Placed around the worked examples (uses the **bridge problem, slide 52** as the
concrete case), just before the closing reflection and assignment.

1. **What AI is good / bad at here** — good: drafting models, boilerplate, syntax, candidate
   TCTL properties. Bad: *guarantees*, hallucinated counterexample traces, missed timing edge
   cases, and inferring the *intent* you didn't state. Maps back to verification (AI helps) vs
   validation (yours).
2. **How to prompt for a UPPAAL model** — state the requirement precisely; name the formalism
   (network of timed automata); enumerate components/channels; ask for a **single runnable
   `.xml` with embedded queries**; iterate on counterexamples. Point your AI at the **UPPAAL
   skill** so it emits correct, loadable models.
3. **Build your own skill** — the UPPAAL skill is **not distributed to students**; if they want
   one they build it. Teach Agent Skills: a `SKILL.md` (when-to-use + procedure) plus reference
   docs, grounded in `docs.uppaal.org`, validated by generating a model and verifying it. This
   deepens AI-resistance — you must understand UPPAAL to author a skill that produces correct
   models — and teaches a transferable skill.
4. **Worked example — the bridge problem** — show the actual natural-language prompt (plain
   English problem + the question, *not* the automaton) → AI (with a UPPAAL skill) → correct
   `.xml` → verify the reachability query. A good prompt + the skill yields an accurate model.

### Slide-by-slide pass (source slide → new deck)

| Src # | What it teaches | AI-era treatment |
|------|-----------------|------------------|
| 1 | Title / author / date | **Reuse** content verbatim (retitle subtitle optional: "…in the age of AI"). |
| 2 | Speaker bio | **Reuse** content verbatim. |
| 3 | (stray website screenshot) | **Drop.** |
| 4 | Model = abstraction that aids understanding; system models are analysable *with semantics* | Keep. Hook: **an LLM is itself a model — non-semantic, non-analysable.** Motivates models you can reason about. |
| 5 | Perspectives (external/behavioural/structural); examples (data-flow, state machines); "is it a model?" | Keep. Extend "is it a model?" → "is an AI a model?" — yes, but not one you can verify. |
| 6 | Formal models = mathematical semantics | Keep, reframed as **the trust anchor**: semantics is what lets you check an AI's output. |
| 7 | Model analysis; needs model + requirement; **Verification vs Validation** | **Anchor slide.** Introduce the AI mapping here. |
| 8 | Formal verification = check ALL behaviours; property in logic; scalability challenge | **Exhaustive vs probabilistic** — the guarantee AI can't give. |
| 9 | State-space explosion | AI does **not** dissolve this; orthogonal open challenge. "Powerful ≠ certain." |
| — | *(NEW)* **Formal Methods in the Age of AI** | Thesis slide: verification (AI-assisted) vs validation (human), powerful≠certain, cost↓/importance↑. Placed after 9. |
| 10 | Adds deductive verification (theorem proving); not fully automated | **Genuinely shifted by AI** — LLMs + proof assistants pushing autoformalization; honest note. |
| 11 | Theorem proving via Socrates syllogism | Contrast **plausible reasoning (LLM) vs sound proof** — looks the same, isn't. |
| 12 | Model checking inputs: A (network of TA) + F (temporal logic); UPPAAL | Keep. Frame the checker as the **oracle** where AI-built models get checked. |
| 13 | Real-time systems: correctness = order **and** timing; controller/plant; examples | Keep. Safety-critical → "probably correct" is not acceptable → proof needed. |
| 14 | Real-time model checking pipeline | Keep. This is the pipeline AI plugs into as model generator. |
| 15 | UPPAAL workflow: model / simulate / verify loop | **Reframe:** modeling step is AI-assistable; the durable loop is simulate→verify→**interpret**→refine. De-emphasise GUI mechanics. |
| 16 | Industrial ABB model; real property questions (reachability, bounded response, invariants) | Keep — strong. Scale where AI-generated models **must** be checked; humans can't eyeball correctness. |
| 17 | Light Control informal requirement (running example) | Keep. Later reused for the AI validation demo. |
| 18 | Finite state automata (states/transitions/labels) | Keep (foundational). |
| 19 | FSA with variables; guards/assignments; semantics = transition systems | Keep. |
| 20–21 | Light Control as FSA — can't capture "quickly" without time | Keep. **Formalism-choice judgment** — motivates clocks; a modeling decision AI won't raise unprompted. |
| 22 | **Timed Automata (Alur & Dill 1990)** | Keep. Explicitly state: **AI doesn't change this; it changes who draws it.** |
| 23–24 | Light Control with clock x; analysis question | Keep; the analysis question is the human's job. |
| 25 | TA semantics: clocks, guards, state=(loc, R-valued clocks), discrete/delay transitions | Keep — the definition that makes checking possible (trust anchor). |
| 26 | TA with invariants; progress; deadlock risk | Keep. |
| 27 | Clock constraints syntax | Keep. |
| 28–33 | Single-location examples: guards, bounds, invariants, non-determinism | Keep — builds the semantic intuition needed to **hand-trace** (supports assignment). |
| 34–36 | Task models: periodic / sporadic / aperiodic | Keep — canonical RTS patterns. |
| 37 | Light Switch TA | Keep. |
| 38 | Demo: Light Control | Keep as section marker. |
| 39 | Semantics definition (valuations, action/delay rules) | Keep — the rules used to hand-verify (supports assignment). |
| 40 | Light-switch **trace** with clock values | Keep — this *is* hand-tracing; models the assignment skill. |
| 41 | Networks of TA; two-way sync (a!/a?); example transition | Keep (composition foundation). |
| 42 | Demo: Light Control in UPPAAL | **Convert to the AI demo:** AI generates the model → verify → interpret; or keep + add the new AI-demo slide near here. |
| 43 | How to specify what to check? | **Specification = durable skill.** AI can draft properties; you must validate them. |
| 44 | TCTL; paths/timed paths; path vs state formulae | Keep. |
| 45 | Quantifiers E/A, []/<>, combinations | Keep — needed to read/judge AI's properties. |
| 46–50 | Property patterns E<>p, A[]p, E[]p, A<>p, leads-to | Keep. Emphasise: **choosing the right property is validation** — AI can't know which property you actually need. |
| 51 | Demo: Light Control in UPPAAL | Keep as marker. |
| 52 | Bridge / Viking problem (reachability ≤60 min) | Keep — AI-solvable puzzle → "AI solves it, but do you trust it? verify it." |
| 53 | Demo: Bridge in UPPAAL | Keep as marker. |
| 54 | Train Crossing (mutual exclusion, timed) | Keep — good AI demo; **not** the assignment (too textbook). |
| 55 | Demo: Train Crossing in UPPAAL | Keep as marker. |
| 56 | UPPAAL SMC: stochastic TA | Keep (brief). |
| 57 | SMC queries (probability eval / hypothesis testing / comparison) | Keep (brief). |
| 58 | Demo: Train Crossing in SMC | Keep as marker. |
| — | *(NEW)* **What's yours vs. what's the AI's** | Reflection before the assignment: durable skills = specify, validate, judge; AI = draft/build. |
| 59–62 | Assignment (Sender/Channel/Receiver protocol) | **Replace entirely** — see next section. |
| 63–96 | Annex (UPPAAL syntax) | **Drop.** |

## Redesigned assignment (AI-resistant)

**Design principle / acceptance test:** *If a student pastes the entire prompt into any AI
tool, what is left for them to do?* The answer must be "the part that proves they learned."
AI-resistance comes from four levers AI cannot reach: **validation judgment on an ambiguous
scenario, emergent (not planted) failure, hand-traced counterexamples, and per-student
variation.**

### Scenario: Pedestrian crossing controller (per-student parameterised)

A signalised pedestrian crossing: vehicle lights, pedestrian WALK/DON'T-WALK, and a push
button. The requirement is given **deliberately under-specified** in natural language, e.g.:
"pedestrians shouldn't wait too long," "the WALK phase must last long enough to cross,"
"the lights must never let cars and pedestrians go at once," "the controller must respond
promptly to a press but not switch too rapidly." Concrete thresholds (crossing width →
minimum walk time, max pedestrian wait, clearance interval, min green for traffic) are
**left for the student to fix and justify**. Per-student variation via an assigned
parameter set and/or a twist (e.g., a bus-priority input, a second crossing, a night mode).

### Deliverables (graded)

1. **Requirement interpretation & modeling decisions** — resolve each ambiguity explicitly,
   state the chosen thresholds, and **justify them against the real-world intent** (validation
   judgment AI can't defend, because it never received the intent).
2. **Formalisation** — express the requirements as TCTL properties (safety = no conflicting
   greens; bounded response = press ⇝ WALK within N; liveness = pedestrians eventually cross),
   with a justification for each interpretation choice.
3. **Model + emergent-failure hunt** — build the model (AI-assisted is *allowed and expected*),
   then use verification to **discover where the model breaks** on the tricky cases (missing
   clearance interval, simultaneous presses, deadlock). Document each failure with the
   **counterexample trace** produced by the tool.
4. **Hand-traced counterexample** — for one discovered failure, reproduce the trace **by hand**:
   step-by-step locations and clock valuations reconciled with the model. (AI hallucinates
   these; a correct hand trace demonstrates real understanding.)
5. **Fix & re-prove** — correct the model and re-verify, showing the property now holds.
6. **Short reflection** — where AI helped, where it produced something wrong/incomplete, and
   how verification/validation caught it.

### Submission

A single runnable UPPAAL model `.xml` with the verification queries **embedded** (modern
UPPAAL stores queries inside the model file; separate `.q` files are legacy/optional), the
counterexample traces, the hand trace, and a short report covering deliverables 1–6.
(Optional oral spot-check of the hand trace and threshold justifications for high-integrity
grading.)

## Second deliverable: UPPAAL skill (`skills/uppaal/`)

A standalone Agent Skill so an AI can build **correct, runnable** UPPAAL models — the
embodiment of the deck's "mechanics → hand to AI" message. **It is not distributed to
students** (see the "Build your own skill" slide): it serves as the instructor's reference and
the model of what a good skill looks like; students who want one build their own.

- **Location & convention:** `skills/uppaal/SKILL.md` in this repo, matching the existing
  `skills/qna/` layout. Add a row to the repo `README.md` skills table and to the symlink
  install snippet.
- **Authoritative source:** <https://docs.uppaal.org/> (latest), **not** the deck Annex.
  Verify exact XML element structure against the `language-reference/` and
  `toolsandapi/file-formats/` pages during the build.
- **Shape (layered, progressive disclosure — matches the user's skill conventions):**
  - Thin `SKILL.md`: when to use, the model-building workflow (requirement → components →
    locations/edges/guards/invariants → sync channels → TCTL queries → emit `.xml` → verify),
    and clarity/validation guardrails. Routes to reference docs.
  - `reference/` doc(s): the concrete **UPPAAL XML model format** — root `<nta>`, global
    `<declaration>`, `<template>` (name, parameters, `<location>` with invariant labels,
    `<init>`, `<transition>`/`<edge>` with guard/sync/assignment labels), `<system>`
    declaration, and the **`<queries><query><formula>/<comment>`** block for embedded queries.
    Plus the modelling-language reference distilled from the Annex topics (guards, invariants,
    clocks, data variables, arrays, constants, regular/urgent/broadcast channels, urgent &
    committed locations, templates/instantiation, select/meta/forall-exists, TCTL query
    language and quantifiers).
- **Correctness check:** generate a small model (e.g. the bridge problem) with the skill and
  confirm it loads and verifies in UPPAAL (or validates structurally against the documented
  schema if a UPPAAL binary isn't available).

## Build approach

- **Tool:** `python-pptx`. A default `Presentation()` uses the blank Office default — i.e.
  **no template/theme**, satisfying the requirement. Full control over plain text boxes,
  simple shapes, and image placement.
- **Image reuse:** unpack `Slides.pptx` (`scripts/office/unpack.py`) to recover the media
  files, map each to its source slide, and re-embed the relevant diagram/screenshot images
  on the corresponding new slides (per the "reuse all images" decision).
- **Design language (plain but not boring):** one restrained palette + one header/body font
  pairing chosen for a technical lecture; consistent title/body layout; native callout boxes
  for the AI-era notes. No accent lines under titles.
- **Slide count:** final deck is **42 slides** (includes a "Build your own skill" slide in the
  AI block). Beyond the design's explicit merges, the
  incremental click-through sequences were consolidated (old 28–33 → one guards/invariants
  slide; task models 34–36 → one; property patterns 46–50 → one table), keeping one clear
  purpose per slide (user-approved). All 41 slides carry new-flow speaker notes.
- **Built by** `build_deck.py` (reproducible); reused images in `assets/`; the verified
  bridge model in `models/bridge.xml`.

## Verification / QA

1. **Content QA:** `python -m markitdown output.pptx` — check every source-slide's teaching
   point is present, no leftover placeholder text, correct order, typos fixed.
2. **Image-embed check:** confirm reused images are actually embedded and land on the right
   slides.
3. **Visual QA (subagent, fresh eyes):** render slides to images
   (`soffice.py --convert-to pdf` → `pdftoppm`) and inspect for overlap, overflow,
   low-contrast text, footer/page-number collisions, misaligned columns.
4. **Fix-and-reverify loop** until a full pass finds no new issues.
5. **AI-resistance check on the assignment:** paste the assignment prompt into an AI tool and
   confirm the graded deliverables (hand trace, threshold justification, emergent-failure
   documentation) are *not* completable by the AI alone.
