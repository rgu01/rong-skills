# System One Decision Models: Jev, SemIf and AnyJev

A study note recorded on 2026-09-23. It covers a class of model that returns a
typed decision with a probability instead of text, the technique behind it, and
the three implementations that appeared in September 2026.

All three projects are new. SemIf was created on 2026-09-16, AnyJev on
2026-09-21, and the TypeSafe site carries the date 2026-09-22 at version 0.01.
Nothing below is settled practice.

---

## The idea

A System One model turns a language model into a typed `if` statement. You send
state, a question and a fixed set of options. You get back a probability for
each option. The model writes no sentence, and your code parses no text.

The name comes from Daniel Kahneman's *Thinking, Fast and Slow*. System 1 is
fast, automatic judgment. System 2 is slow, deliberate reasoning. A chat model
that writes out its steps is System 2. This is the fast tick in a box.

TypeSafe names its model **Jev**, after the economist William Stanley Jevons.
The Jevons paradox says that better efficiency increases total demand instead of
reducing it. Their argument: cheap decisions will not mean fewer decisions.

Both names are TypeSafe coinages. Kahneman supplied the idea of System 1
thinking, but no one called a model a "System One Model" before this.

---

## The technique, in six steps

### 1. A language model already computes the numbers

For one input, one forward pass produces one score — a **logit** — for every
token in the vocabulary, about 150,000 of them.

```text
   "The ticket should go to the"
              │
     ┌─────────────────────┐
     │   one forward pass  │
     └─────────────────────┘
              │
     billing      18.2
     technical    16.4
     sales        14.1
     banana        2.3
     ...          ...        ← about 150,000 rows
```

To write text, the model samples one row, appends that token, and runs again.
Fifty tokens cost fifty passes. The decision was finished in the first pass.
The other passes only spell it out.

### 2. Label the options so the answer is one token

The answer must fit in exactly one token, or there is nothing to read. Option
words do not work: they split into several tokens, they have unequal lengths,
and common words win regardless of meaning.

The fix is to label each option with a letter. SemIf uses 16 letters, so it
allows 2 to 16 options. AnyJev allows up to 26.

SemIf's system prompt:

> Apply the supplied criterion to the supplied evidence. Choose exactly one
> listed option. Respond with only its uppercase letter, with no explanation or
> reasoning.

The message it builds carries the letter and the English description only. Your
own option names never reach the model.

```json
{
  "evidence":  "Customer asks to reset a forgotten password.",
  "criterion": "Which queue should handle this request?",
  "options": [
    {"letter": "A", "description": "Account access and authentication support."},
    {"letter": "B", "description": "Billing and payment support."},
    {"letter": "C", "description": "Sales and product evaluation."}
  ]
}
```

The JSON is an envelope. Its string values are English, and the model reads them
as English. Change a description and the answer changes. There is no lookup
table behind the option names.

### 3. Read the logits and normalise them

Nothing forces the model to answer with a letter. The code simply keeps the
logits for the letters in use and ignores the rest.

The scale of a logit means nothing. Only the gaps matter. A gap of *d* means one
option is *e^d* times more likely. Subtracting a constant from every logit
leaves the probabilities unchanged.

```text
logits  22.000, 26.375, 24.375  →  0.0110, 0.8711, 0.1179
logits   0.000,  4.375,  2.375  →  0.0110, 0.8711, 0.1179
```

The probabilities are **conditional on the options supplied**. A value of 0.871
means "87% of the belief that fell on these three options went to B". If the
correct answer was never listed, the number says nothing about that.

### 4. Stop before generating

The model produces the scorecard and the code reads it. No token is sampled and
no string is returned. SemIf calls the model's forward function directly, with
`use_cache=False` and `logits_to_keep=1`, and indexes the resulting tensor.

This is why the technique needs access to the weights, or a service that holds
them. An ordinary chat interface returns only generated text. The Claude
Messages API has no `logprobs` parameter and no token-probability response
field (checked 2026-09-23).

Two costs split apart, and both matter:

| | Prefill | Decode |
|---|---|---|
| Work | Read the prompt | Write the answer |
| Shape | All tokens at once | One token at a time |
| Hardware | The GPU is busy | The GPU mostly waits |
| Cost | One pass | One pass per token |

Measured by SemIf on one frozen 4B model, one state and 21 criteria:

```text
0.489 s  thinking: prefill
4.843 s  typing: 111 tokens at 44 ms each
─────────
5.332 s  total — 91% of it spent writing an answer it already had
```

Removing the typing gives 1.023 s for the same 21 decisions. That is about
49 ms per decision, roughly the cost of writing one word.

A second saving comes from the key-value cache. One long state is prefilled
once, then branched across many questions. SemIf's measurement on 777 decisions,
37 states by 21 criteria:

| Execution path | Decisions per second | 777 decisions |
|---|---:|---:|
| Fresh every time | 2.33 | 333.5 s |
| Reuse the prefix, one at a time | 10.75 | 72.3 s |
| Reuse the prefix, questions in parallel | 20.03 | 38.8 s |

TypeSafe sells the same idea as a pattern. Put every question in one request.
Their published result is 12.2 times cheaper and 10 times faster than separate
calls.

### 5. The raw number lies

The letters solve the token-length problem and create a bias problem.

**Position bias.** The model prefers a slot, whatever sits in it. Reverse the
option order and the content answer changes. AnyJev measured a flip rate of
**0.230** on Qwen3-8B with a 20-way task. Their front page shows one real case
that flips at a stated confidence of 1.00.

**Prior bias.** The model leans toward certain labels before reading anything.
The letter `A` is a more common answer than `P`. The word `yes` is more common
than `no`.

The damage, on the same task:

| | raw readout |
|---|---:|
| Answer flips when options are reversed | 0.230 |
| Expected calibration error | 0.240 |
| Accuracy | 0.747 |
| Traffic automatable at 5% error | 7.7% |

Accuracy is not the problem. Trust is. A calibration error of 0.240 means that
a stated 0.9 behaves nearer 0.66. No threshold works, so almost everything goes
to a person.

### 6. The corrections

**Rotate the options.** Position bias belongs to the slot, not to the option.
Present the options in K cyclic rotations, so each option sits in each slot
exactly once, then average by content. The slot preference cancels. Cost: K
prefills for a K-option question, batched over the shared prefix.

**Divide out the prior.** Average each label's probability across a batch of
different states asking the same question. A label that is consistently high is
showing its prior. Divide it out and renormalise. No labels are needed. This
fails when one answer genuinely dominates, because the high average is then
correct rather than a bias.

Those two steps are AnyJev's **L0**, and they need no labelled data.

**Fit a temperature.** Divide every logit by one number *T* before the softmax.
Above 1 flattens the distribution; below 1 sharpens it. Fit *T* on 100 to 500
labelled cases per question. This is AnyJev's **L1**, and it is also what SemIf
ships.

Temperature never changes the ranking, because dividing all logits by the same
positive number cannot reorder them. It changes only the stated confidence:

| T | A | B | C | Winner | Confidence |
|---:|---:|---:|---:|:--|---:|
| 1.00 | 0.011 | 0.871 | 0.118 | B | 0.807 |
| 1.23 | 0.023 | 0.816 | 0.161 | B | 0.724 |
| 1.71 | 0.056 | 0.721 | 0.224 | B | 0.581 |
| 2.50 | 0.107 | 0.616 | 0.277 | B | 0.424 |

SemIf's fitted temperatures are all above 1, so the raw readout was
overconfident in every workload measured:

| Workload | T | Calibration error before | after |
|---|---:|---:|---:|
| Authored decisions | 1.23 | 0.068 | 0.038 |
| WANLI | 2.50 | 0.208 | 0.069 |
| Every judgments | 1.71 | 0.050 | 0.047 |

What each step buys, on Qwen3-8B with a 20-way task and 300 test items:

| | raw | L0 | L1 |
|---|---:|---:|---:|
| Labels needed | none | none | 100–500 |
| Answer flips on reversal | 0.230 | 0.073 | 0.077 |
| Accuracy | 0.747 | 0.803 | 0.807 |
| Calibration error | 0.240 | 0.184 | 0.095 |
| Traffic automatable at 5% error | 7.7% | 46.3% | 52.0% |

The two fixes do different jobs. Rotation and the prior fix the flipping and the
accuracy. Temperature fixes the calibration error. The bottom row is the one
that decides whether the system is usable.

---

## Probability against confidence

A bare probability is not comparable across questions. A winning probability of
0.6 in a yes-or-no question is nearly a coin flip. The same 0.6 among 20 options
is strong, because a random guess would give 0.05.

TypeSafe reports a second field, `confidence`, which measures how concentrated
the distribution is. Their documented formula for three options:

```text
confidence = (3 × largest probability − 1) / 2
```

The general shape for K options is `(K × p − 1) / (K − 1)`. It reproduces
TypeSafe's published examples to rounding: a largest probability of 0.95 gives
0.925 against a documented 0.92, and 0.88 gives 0.82 against a documented 0.81.

The effect:

```text
p_max = 0.6  among 2 options   →  confidence 0.20
p_max = 0.6  among 20 options  →  confidence 0.58
```

TypeSafe's guidance is three bands, with one rule: act automatically above 0.9
for serious actions, ask for confirmation in the middle, and send anything below
0.5 to a person. Their wording — "A confidence threshold is not one number.
Different actions should be gated at different levels depending on the
consequences of getting it wrong."

A **Score** answer is the probability-weighted mean of the levels, not a rounded
category. Levels 0, 1 and 2 at probabilities 0.00, 0.95 and 0.05 give 1.05,
which is the value TypeSafe's example shows.

---

## The three implementations

| | Jev (TypeSafe) | SemIf | AnyJev |
|---|---|---|---|
| Origin | TypeSafe, San Francisco | Theo Lee, independent | Nokia Applied Research with Tencent Hunyuan |
| Where it runs | Hosted only | Local GPU, CPU, Mac or browser | Local GPU |
| Model | `jev-1.13.0`, trained for the job | Qwen3.5-4B and others, unchanged | Any LLM, unchanged |
| Question types | Choice, Score, Noul | Choice | Choice, Noul, Score |
| Interface | HTTP API, Python and JavaScript SDK | Batch command over a file | Python library |
| Live service | Yes | No | Not yet; on the roadmap |
| Cost | $0.042 per million input tokens | Local compute | Local compute |
| Licence | Commercial service | MIT | Apache-2.0 |

Position on the correction ladder:

| | Rotation | Prior | Temperature |
|---|:--:|:--:|:--:|
| SemIf | no | no | yes, per workload |
| AnyJev | yes | yes | yes |
| Jev | trained in; method not published | | |

SemIf's default output is a plain softmax over the option logits with no
temperature. This is confirmed by its committed prediction rows: the stored
probabilities reproduce exactly from the stored logits. Its own output field
states `"uncalibrated as decision confidence"`. SemIf does measure option
reversal, as one of three perturbation variants, but does not correct it.

AnyJev reports a calibration error of 0.036 with Qwen3-32B at L1, against 0.144
for published Jev, while stating that a fine-tuned model still leads on
accuracy. AnyJev did not rerun the Jev numbers; they read them as published.

**SemIf output fields worth using.** Each row carries two diagnostics:

- `allowed_token_mass` — how much of the whole vocabulary probability landed on
  the letters in use. A value near 1.0 means the model understood the task. A low
  value means the model wanted to answer something the option list does not
  cover.
- `full_vocab_argmax_id` — the token the model liked best across the whole
  vocabulary. When it is not one of the letters, the readout forced an answer the
  model did not want to give.

---

## Three ways to use it

**Hosted.** TypeSafe runs the model and does the readout. No weights and no GPU
are needed. An API key and an HTTP client are enough.

**Candidate probabilities on a general API.** Where a provider returns the
probabilities of the top few candidate tokens, a one-letter answer can be scored
this way. Usually only the top few candidates are returned, so with many options
the ones that matter may be missing, and the rotation correction cannot be
applied. The Claude Messages API does not offer this.

**Open weights locally.** This is running an existing model, not developing one.
SemIf's baseline is a 4B model on one RTX 3090, with CPU and Apple Silicon paths
as well.

**For coding agents.** Jev cannot drive a coding agent. TypeSafe states it
directly: "Jev is not a chat or code-completion LLM." The relation is the other
way round — a coding agent writes the application at development time, and the
application calls the decision model at run time. TypeSafe ships a plugin so
that agents generate correct integration code:

```bash
claude plugin marketplace add typesafe-ai/skills
claude plugin install typesafe@typesafe-ai
```

**Build the decision set first.** The portable asset is not the code. It is a
file of real cases: state, question, options, and a correct answer labelled by
someone who knows. One hundred to three hundred rows per decision. That file
works with all three implementations after a small format change, and it is what
temperature fitting needs. It also keeps the infrastructure choice reversible.

---

## What the technique cannot do

- **Create anything.** No text, no code, no summary, no translation. It selects
  from a list; it never writes.
- **Answer outside the list.** An option set that misses the true answer returns
  a confident wrong pick and a misleading probability. Watch
  `allowed_token_mass`.
- **Rescue a model that cannot do the task.** AnyJev tested mazes and
  Minesweeper, where no readout beat a trivial baseline. Their wording:
  "Calibration cannot fix a model that cannot answer."
- **Survive a change of traffic.** A temperature fitted on one distribution goes
  stale when the input distribution moves.
- **Take more than 26 options in one call**, with the letter readout.

The limit is not "classification". The limit is that the answer must be one you
can list. That is wider than it sounds, because the list can be generated at run
time by cheap means — a regular expression, a search index, a small model — and
the decision model only chooses. TypeSafe's published cookbooks apply it to
search re-ranking, value extraction, citation checking, entity matching,
function calling, guardrails and hierarchical taxonomies.

---

## Naming and evaluation notes

Three unrelated things share the word "typesafe": the company `typesafe.ai`
described here; **Typesafe Inc.**, the older Scala and Akka company, renamed
Lightbend in 2016; and "type safety", a general programming term. Searches need
"Jev" or "System One" to reach the right one.

**BANKING77** is the public benchmark behind AnyJev's headline numbers. It holds
13,083 real online-banking customer messages, each labelled with one of 77
fine-grained intents, published by PolyAI in 2020. AnyJev used a 20-way slice
with 300 test items, not the full 77.

Vendor claims that were not independently checked: TypeSafe's "193.6× faster"
and "244.6× cheaper" against LLM workflows, and "238× cheaper" against a named
competitor model.

---

## Open points

| Question | What would settle it |
|---|---|
| What model and training does Jev use? | TypeSafe publishing an architecture or a method paper |
| Do AnyJev's gains hold outside Qwen models and BANKING77? | Llama and Gemma rows, which are on their roadmap |
| Can AnyJev replace a hosted service operationally? | The Jev-compatible HTTP server on their roadmap |
| How stable are Jev's probabilities across model versions? | A labelled hold-out set, re-measured on each pinned version |

Pin the model version. `jev-1.13.0` is the current model and `jev-latest` is an
alias. A new model changes the probabilities, and a threshold tuned against one
version does not carry to the next.

---

## Sources

- [TypeSafe: System One](https://docs.typesafe.ai/concepts/system-one)
- [TypeSafe: Quick start](https://docs.typesafe.ai/introduction/quickstart)
- [TypeSafe: State](https://docs.typesafe.ai/concepts/state)
- [TypeSafe: Primitives](https://docs.typesafe.ai/primitives)
- [TypeSafe: Confidence](https://docs.typesafe.ai/confidence)
- [TypeSafe: Models](https://docs.typesafe.ai/models)
- [TypeSafe: API reference](https://docs.typesafe.ai/api)
- [TypeSafe: Jev with coding agents](https://docs.typesafe.ai/introduction/coding-agents)
- [TypeSafe: Agent skill](https://docs.typesafe.ai/agent-skill)
- [TypeSafe: Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)
- [SemIf](https://github.com/TheoLeeCJ/SemIf)
- [AnyJev](https://github.com/nokia-applied-research/AnyJev)
- [BANKING77 dataset](https://huggingface.co/datasets/PolyAI/banking77)
- [Efficient Intent Detection with Dual Sentence Encoders](https://arxiv.org/pdf/2003.04807)
- [Claude Messages API reference](https://platform.claude.com/docs/en/api/messages)
