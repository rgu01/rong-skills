# How LLMs Work: From Tokens to Attention

A study summary — the path from raw text to a generated answer, built up step by step.
Covers tokenization, embeddings, training, and attention, plus the philosophical
limits of what an LLM's output can mean.

---

## The pipeline (the map everything hangs on)

```
RAW TEXT
  ① Normalization        unicode cleanup, (sometimes) lowercasing
  ② Pre-tokenization     split on whitespace/punctuation into word-units
  ③ Subword segmentation BPE / WordPiece / Unigram → tokens
  ④ Add special tokens   BOS/EOS, chat & tool markers
  ⑤ Vocabulary lookup    each token → integer ID   (count_tokens measures here)
  ─────────── everything above is the TOKENIZER ───────────
  ⑥ Embeddings           each ID → a vector (+ positional encoding)
  ⑦ Transformer          attention + MLP, stacked many times
  ⑧ Output               next-token distribution → sampling → detokenize
```

---

## 1. Tokens

- A **token** is the smallest meaningful unit a system breaks a stream into.
  - In *parsing* (e.g. a Graphviz DOT lexer): rule-based, deterministic units.
  - In *LLMs*: subword pieces drawn from a fixed vocabulary.
- **Vocabulary** = a fixed, numbered list of all tokens the model knows (~50k–200k
  entries). Text → token IDs is a lookup into this table. Models compute on numbers,
  not text, so this conversion is mandatory. The vocabulary is frozen at build time.

## 2. Why subwords

- **Whole words** → vocabulary explodes; any unseen word becomes unknown.
- **Single characters** → tiny vocabulary but very long sequences.
- **Subwords** (the modern choice) → common words stay whole (`the`), rare ones split
  into pieces (`brainstorm` + `ing`). Manageable vocabulary size, and no truly
  "unknown" word — worst case it falls back to smaller pieces.

## 3. Tokenizer algorithms

### BPE (Byte Pair Encoding) — GPT family, Claude's lineage
- **Training:** start from characters; repeatedly merge the **most frequent adjacent
  pair** into a new token; produces an *ordered merge list*. Every vocabulary entry is
  built by merging exactly **two** existing entries — a tree down to single chars.
- **Encoding:** start from characters, then repeatedly **apply the highest-priority
  applicable merge anywhere in the sequence** (priority = rank in the merge list),
  until no adjacent pair has a rule. *Not* left-to-right; priority-driven.
- **Key behaviors** (traced with "there is the man mann"):
  - Merges only combine characters actually present — you can't merge in a letter that
    isn't there. `the` never becomes `them` when tokenizing `the`.
  - Word boundaries: text is split on whitespace first, so merges never cross gaps.
  - A typo like `mann` **doesn't break** — it gracefully falls back to `man` + `n`.
    No unknown token. Rare = more tokens (rarity shows up as fragmentation).
  - A substring can be *absorbed*: `the` inside `there` disappears if `there` fully
    merges into one token.

### WordPiece — BERT
- **Training:** merges the most **informative** pair, not the most frequent.
  `score(a,b) = freq(a·b) / (freq(a) × freq(b))` — favors pairs that co-occur more than
  chance predicts (e.g. `qu`), dampening pairs that are common only because their pieces
  are common (e.g. `th`).
- **Encoding:** greedy **longest-match** from the vocabulary, left to right.
- **`##` marker** distinguishes word-start pieces from continuations: `play` + `##ing`.
- **Fallback:** can emit a true **`[UNK]`** token if no prefix matches (rare).

### Unigram — T5 / SentencePiece
- Built **top-down**: start with a huge candidate vocabulary, assign each token a
  probability, then **prune** the least-useful tokens until the target size. A word can
  be segmented many ways; the model keeps the set that best explains the corpus
  probabilistically. (We only sketched this one.)

### Measuring tokens
- Use the model-specific `count_tokens` API — counts are **model-specific**, so pass the
  exact target model. **Never** use `tiktoken` for Claude (it's OpenAI's tokenizer).
- Script written this session: `scripts/compare_tokenizers.py` — feeds the same strings
  to two models and reports SAME/DIFF to probe whether they share a vocabulary.

## 4. Embeddings (step ⑥)

- **Why IDs won't work:** an ID (e.g. 582) is just a label. Its *numeric magnitude* is
  meaningless — `man`(582) is not "twice" some token 291. Words have no 1-D ordering,
  though they *do* have rich multi-dimensional relationships.
- **The fix — embedding lookup table `E`:** a matrix of shape `V × d` (one row per token,
  each row a vector of `d` numbers, e.g. `d = 4096`). "Look up the embedding" = grab the
  token's row. No math, just indexing.
- Embedding does two jobs: **removes** the fake numeric relationships integers impose,
  and **installs** learned semantic structure — similar words end up at similar vectors,
  and `man→woman ≈ king→queen` as a *direction* (a combination of columns, not one column).
- **Individual columns generally have no clean meaning** — meaning is distributed/entangled.
- **Why a width like 4096:** a design hyperparameter balancing capacity vs cost; usually a
  power-of-2-ish number for GPU efficiency; `d` is the model's hidden size carried through
  every layer. Bigger model → wider `d`.
- **Does Claude reveal `E`?** No — closed weights (like GPT/Gemini). To inspect a real `E`,
  use an open-weights model (Llama, Mistral, Qwen, GPT-2).

## 5. Training

- **Objective:** next-token prediction. The training text is its own answer key
  (**self-supervised**). "the man is here" yields pairs: (`the`→`man`), (`the man`→`is`),
  (`the man is`→`here`). The true answer `y` is simply the actual next token.
- **Loss (cross-entropy):** the model outputs a probability for every vocabulary token;
  loss ≈ "how little probability you put on the correct next token."
- **Gradient:** for each parameter, the slope of the loss w.r.t. that parameter (which way,
  and how steeply, error changes if you nudge it). Computed via the **chain rule**
  (backprop = reusing each layer's gradient as the start for the previous layer).
- **Update:** `new_param = old_param − learning_rate × gradient` (subtract → move downhill).
- **Worked example:** `ŷ = w·x`, `L = (ŷ−y)²`, `x=2, y=10, w=3` → `ŷ=6, L=16`,
  `gradient = 2(ŷ−y)·x = −16`, `w ← 3 − 0.01·(−16) = 3.16` → `L` drops to 13.5.
- **Stopping generation:** the model emits a special **end token** (`<EOS>` / end-of-turn),
  learned from training; the runtime halts on it. Plus external caps: `max_tokens`, stop
  sequences. `stop_reason: "max_tokens"` = the cap hit before the model chose to stop.
- **At scale (Opus-4.8-class):** same loop, just enormous — trillions of tokens, hundreds
  of billions of parameters, batched (one averaged gradient step over thousands of
  sequences), parallelized across many GPUs (model + data split).

## 6. Diverse data → distribution, not determinism

- Contradictory continuations don't cancel — each claims **probability mass**. If "the man
  is" is followed by `here` 600× and `there` 400×, the loss is minimized by outputting the
  **true frequencies** (`P(here)≈0.6, P(there)≈0.4`), not by picking one.
- **Context collapses ambiguity:** real prompts condition on everything before, reshaping
  the distribution so one continuation usually dominates.
- **Determinism is a decoding choice, not baked in:**
  - Greedy / temperature 0 → always take the argmax → reproducible.
  - Temperature > 0 → sample from the distribution → varied. (Why the same prompt can give
    different answers across runs.)

## 7. Philosophy — what an LLM's answer can mean

- Output quality depends on **three** factors, not two:
  1. **Model fidelity** — how well it reproduces the training distribution (measurable/math).
  2. **Data quality** — whether that distribution reflects reality (empirical, hard).
  3. **The objective itself** — next-token prediction targets *plausibility*, not *truth*.
- **Frequency ≠ truth.** A perfectly faithful model of human text faithfully reproduces
  human errors, biases, and myths. The gap between "typical" and "true" is where
  **hallucination** comes from.
- This is why models have a **second stage (post-training / RLHF)** that bends the
  distribution away from pure imitation toward helpful/honest/harmless behavior. Correctness
  is *engineered on top of* imitation, not derived from it.
- **You can't certify outputs by verifying the training data**, because the model
  **synthesizes** (interpolates) rather than retrieves — and *truth is not preserved under
  synthesis* (two true facts can combine into a false statement). Also: most training text
  has no truth-value, the corpus is unreadably large, and the deployed model ≠ the raw
  pretraining predictor. Trust must be earned at the **output**, per-claim, against external
  reality.

## 8. Positional encoding (finishing step ⑥)

- **Problem:** self-attention is **order-blind** — it sees a *set* of vectors.
  `the man is` and `is man the` would look identical.
- **Fix:** add a position signal to each token: `input[i] = token_embedding(i) + position(i)`.
- **Three schemes:**
  - **Sinusoidal** (2017 Transformer): fixed sine/cosine waves at many frequencies; no
    parameters; extrapolates somewhat.
  - **Learned absolute** (BERT/GPT-2): a second lookup table of position vectors; flexible
    but has a **fixed max length**.
  - **RoPE** (most current LLMs): **rotate** each token's vector by an angle proportional to
    its position, instead of adding. Because attention compares tokens via dot product, the
    result depends only on the **relative distance** (`pos_a − pos_b`). Encodes relative
    position for free and stretches to longer contexts (position interpolation).
- **The 361° question:** a *single* rotation wraps (361° = 1°), so one frequency would alias
  distant positions. RoPE avoids this by rotating at **many frequencies at once** — like a
  clock with many hands. Fast hands wrap often; slow hands have periods longer than the
  context, so the full multi-frequency fingerprint is unique within range. Pushing past the
  trained range degrades the fingerprints — the reason extending context isn't free.

## 9. Attention (step ⑦) — the heart

- **Purpose:** let isolated token vectors **pull in information from other tokens**
  (e.g. resolve what `it` refers to). Attention is a **soft, learned lookup**.
- **Query / Key / Value** — every token produces all three, via three learned matrices
  applied to its one embedding:
  ```
  q = embedding · W_Q   (searcher — what am I looking for?)
  k = embedding · W_K   (advertisement — what am I?)
  v = embedding · W_V   (content — what I hand over if selected)
  ```
  Each token plays all three roles at once: it **searches**, it's **searchable**, and it
  **holds content**. Example "the tired cat slept": `cat` queries `tired` (pulls in
  tiredness) while simultaneously being queried by `slept` (offers itself as the subject).
- **One vector, three projections:** q/k/v are three *lenses* on the **single** embedding —
  not three independent stores. Even the value is a projection (`·W_V`), not the raw
  embedding. Roles are **designed** (architecture); the numbers inside are **learned** and
  mostly **not human-interpretable** — English glosses like "which noun am I attached to?"
  are teaching scaffolding, not literal content.
- **Why project live instead of storing q/k/v:** they're **context-dependent** — they change
  by position and by layer (each layer's input is the previous layer's attention output). So
  there's nothing static to store; what's stored is the reusable **matrices** (the learned
  *recipe*). Context-sensitivity is the *source of the capability*, not an efficiency
  trade-off.
- **The mechanism (to be detailed):** `scores = q · k` → **softmax** → weights → the token's
  new vector = **weighted sum of everyone's values**.

### The transformer layer & MLP
- Attention **is part of** the neural network — q/k/v are intermediate values inside one
  attention sub-layer, not fed into a separate net.
- **One layer:** input → attention sub-layer → (add back input: residual) → feed-forward
  MLP → (residual) → output → next layer.
  - **Attention** mixes information *across* tokens ("look around, gather").
  - **MLP** processes *each* token individually ("think about what you gathered").
- **MLP (Multi-Layer Perceptron):** linear layers with a nonlinearity between them. In a
  transformer it's 2 layers: expand (e.g. 4096 → ~16384) → nonlinearity (ReLU-like) →
  contract (→ 4096), applied per token. The nonlinearity is essential (else stacked linear
  layers collapse to one). MLP blocks hold the **majority of parameters** (~2/3) — a lot of
  the model's stored knowledge.
- **Stacking** dozens–hundreds of layers builds representations up from raw word meaning to
  abstract, context-rich meaning. Final vectors → project to vocabulary → next-token
  distribution.

---

## Open threads (not yet covered)
- Attention Part 2 in detail: the `q·k → softmax → weighted-sum` arithmetic.
- Multi-head attention, causal masking, residual connections (why "add back the input").
- Decoding/sampling in depth: temperature, top-k, top-p.
- Byte-level tokenization; special tokens; "why tokenization bites" (letter-counting,
  arithmetic, glitch tokens, non-English token inflation).
- RLHF mechanics; whether an LLM answer is ever "knowledge."
- Hands-on: load an open model's embedding matrix `E` and inspect it.

## The big picture in one line
A simple objective (predict the next token) + enormous computation (deep transformer
stacks) + scale (trillions of tokens) produces emergent structure that behaves like
comprehension — with correctness limited by data quality and the fact that the objective
targets *plausibility*, not *truth*.
