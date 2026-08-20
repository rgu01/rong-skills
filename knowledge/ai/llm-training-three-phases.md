# The Three Phases of LLM Training

A study summary recorded on 2026-08-20, prompted by the GLM-5.3 story in the
[2026-08-20 AI newsletter](AI-newsletter/2026-08-20-ai-newsletter.md#story-glm-5-3-post-training)
— a model whose entire capability jump came from post-training on an unchanged base.

The diagrams live in the companion web page, not in this file:

- **Local page:** [`llm-training-three-phases.html`](llm-training-three-phases.html) — a
  self-contained HTML page (six inline-SVG diagrams, no build step, no network needed;
  offline it falls back from Google Fonts to local serif/grotesque/mono stacks).
- **Published artifact:** <https://claude.ai/code/artifact/f778a927-395e-4d8a-9535-d035ebdda38b>
  — private to the author's account unless explicitly shared.

---

## The map

A model is trained three times, on the same weight tensors. Each phase edits the model
the phase before it produced.

| Phase | Data | Volume | Objective | Installs | Metaphor |
|---|---|---|---|---|---|
| 01 Pre-training | anything written down, unlabelled | 10–30T tokens | predict the next token | **knowledge** | reads the library |
| 02 Mid-training | curated mix: code, maths, long documents | 0.1–1T tokens | predict the next token | **balance** | specialist school |
| 03 Post-training | demonstrations, preferences, graded attempts | 10⁶–10⁹ examples | imitate, prefer, maximise reward | **behaviour** | apprenticeship |

Three words carry the whole map: **knowledge → balance → behaviour**.

The asymmetry worth remembering: pre-training consumes roughly ten thousand times more
data than post-training, yet post-training is what turns a text predictor into something
that takes an instruction and finishes a job.

## 01 Pre-training — predict the next token, ten trillion times

No labels, no questions, no answers. The model guesses the next token, the guess is
compared with what actually followed, and the gap nudges every weight slightly. Because
the "label" is just the following token, any text is usable training data — which is why
this phase absorbs trillions of tokens with no human annotating anything.

The artifact that comes out is the **base model**: knows a great deal, obeys nothing. Ask
it "What is a clamp?" and it may reply with more questions, because a list of questions is
a plausible continuation of a question.

## 02 Mid-training — same lesson, different diet

Nothing changes about *how* the model learns. What changes is *which* documents are in the
bucket: web text drops (roughly 62% → 16% in published mixes), while code (×2.4),
maths and proofs (×5.5) and long documents (×3) grow. Percentages are illustrative of
published mixes, not any single lab's recipe.

Feeding a whole repository as one unbroken sequence — rather than a random 4,000-token
slice of one file — is what teaches the model that a test file and an implementation file
are related, and to hold both in mind at once. A model is only usable at 200k tokens of
context if it saw documents that long in training.

## 03 Post-training — where behaviour is installed

Three sub-stages, run in order. The supervision gets cheaper and vaguer moving right —
and more powerful.

1. **SFT** (supervised fine-tuning) — consumes one prompt plus one ideal answer, written
   by a human or a stronger model. Teaches the *shape* of an answer by imitation. What it
   really installs is habits: read before editing, run the tests afterwards, report what
   happened.
2. **Preference optimisation** — **RLHF** (reinforcement learning from human feedback) or
   **DPO** (direct preference optimisation). Consumes two answers to one prompt, one
   marked better. Nobody has to write the perfect answer, only rank two real outputs.
   This is where "gets to the point", "doesn't flatter you" and "admits uncertainty" come
   from.
3. **RLVR** (reinforcement learning from verifiable rewards) — consumes a task plus an
   automatic checker returning pass/fail. The model is shown no target at all: it is
   turned loose on the task K times (K ≈ 8–64), each attempt runs in a real environment
   (shell, repo, test runner, browser), and a program — test suite, compiler, exit code —
   scores the final state. Winning trajectories get reinforced token by token.

RLVR is the mechanism behind "the model learned to plan". Nobody wrote a rule saying read
the test before editing; the attempts that read first passed more often, so reading first
got reinforced. It scales where RLHF cannot because no human ever reads an attempt — but
the reward is only as honest as the checker, which is why coding, maths and terminal work
improved first.

## What post-training can and cannot do

**Can:** make capability the base already has reliably reachable; install habits; extend
the horizon from one good answer to a hundred coherent steps; shape tone, refusals,
formatting and tool-calling syntax.

**Cannot:** add knowledge the base never saw; change architecture-level limits (tokenizer,
context length, parameter count); guarantee the gain generalises — training against
graders can also teach fitting the grader, and benchmark-shaped tasks are the easiest
thing to overfit; prove anything about safety.

## Case: GLM-5.3 (2026-08-14)

Z.ai shipped GLM-5.3 on the same 743B base as GLM-5.2. Base and mid-training were reused
bit for bit; only post-training was scaled up. Terminal-Bench 3.0 went 4.6 → 28.3 and
DeepSWE v1.1 went 46.2 → 66.9 — both *agentic* benchmarks, which is exactly what stage 3
trains. Numbers as reported at launch; weights were promised roughly two weeks later,
after safety evaluation, so the first independent check landed after the release itself.

Post-training is cheap relative to pre-training, so a lab holding a good base model can
ship capability jumps repeatedly without paying for another base run. Expect the release
cadence to keep looking like this.

## If you keep three sentences

Pre-training decides what the model *knows*. Mid-training decides what it is *good at*.
Post-training decides what it *does* — and it is the only one of the three you can redo
cheaply, which is why it is where the competition now happens.
