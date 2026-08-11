---
name: qna
description: Use when a single reply would run long — explaining a block of code, a document or article, a system's design, or any multi-part question whose full answer is a wall of text the user must scroll and wait through before reaching the part they care about.
disable-model-invocation: true
---

# QnA — pace long answers instead of dumping them

## Core principle
A big answer delivered all at once forces the user to wait through — and scroll past — text they may not even need. Deliver it in checkpoints: one part at a time, continuing only when the user signals they're ready.

## Clarity guardrail
- Never use an acronym without spelling out the full name the first time it appears.
- Always talk in ASD-STE100 Simplified Technical English.

## The shape of a paced answer
1. Open with a one-line map: name the topic and list the parts you'll cover (e.g. "three parts: X, Y, Z").
2. Give **one** part — short enough to read in a few seconds, not a few paragraphs.
3. End with a checkpoint: say what comes next and hand control back — ask whether to continue, go deeper, or skip ahead.
4. Continue only after the user responds. Never pre-write the remaining parts.

## Choosing the order
Decision: does explaining an earlier part require a concept from a later part?

- **No → sequential (default).** Explain start to end: first line → last line, first section → last section.
  _e.g. an article that builds ideas in order — cover its sections top to bottom._
- **Yes → overview first.** Give a brief 2–3 sentence overview so later concepts are named up front, then walk the parts in detail.
  _e.g. a parameterized decorator — no single layer makes sense until the reader knows there are three nested layers, so sketch the shape first._

## Sketch when it clarifies
Decide within each chunk whether the idea is clearer shown than described.

- Draw a compact sketch for structure, flow, hierarchy, spatial arrangement, state changes, or relationships.
- Default to an inline ASCII or Unicode sketch. Use Mermaid only when the response environment is known to render it.
- Keep facts, definitions, and linear explanations in prose.

Introduce the sketch in one sentence. Explain the sketch immediately afterward, then continue the current chunk. Do not put concepts from later chunks into it.

Example:

```text
request → decorator → wrapper → retry loop
             │
             └─ captures configuration
```

The arrows show call flow; the branch shows where configuration is retained. The sketch belongs only to the current chunk and does not replace the explanation.

## Example (overview-first)
> **User:** "Explain this code."
>
> **You:** "It's a retry decorator, built as three nested layers — a config factory, the decorator it returns, and the wrapper that actually runs the retry loop. I'll take one layer at a time.
>
> **Layer 1 — the factory:** `retry(...)` just captures the config (max attempts, delay, which exceptions to catch) and hands back a decorator, so you can tune it per use…
>
> Continue to the decorator and its wrapper?"

Then **stop and wait.** Do not write layers 2 and 3 until the user replies.

## Common mistakes
| Mistake | Fix |
|---|---|
| Dumping the full explanation, then asking "any questions?" | Check in *before* the wall of text, not after. |
| Chunks too large (multiple paragraphs each) | A chunk is a few sentences — one idea. |
| Ending a part with no checkpoint | Always name what's next and hand control back. |
| Racing ahead once you've mapped the parts | The map is a promise, not permission — still stop after part 1. |
| Drawing every idea or leaving a sketch unexplained | Sketch only when relationships are clearer visually, then explain it immediately. |
