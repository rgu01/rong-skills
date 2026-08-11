# rong-skills

A small collection of personal [Agent Skills](https://agentskills.io) — reusable technique guides that an AI coding agent (Claude Code, Codex, and other skill-aware runtimes) loads on demand.

Skills and knowledge are grouped by topic: **formal methods**, **AI**, and **engineering**.

## Golden rule

This repository is personal and public. It carries **no information about the author's
employer** and **no reference to the author's work account** — no employer or product
names, no work email addresses, internal hosts, remotes, ticket IDs, or customer/project
data. Where the employer must be referred to at all, it is written `P`; proprietary tool
and language names are genericized. The only identity that appears here is
`ronggufly@gmail.com`. See [`AGENTS.md`](AGENTS.md) for the full rule that agents follow.

## Skills

### Formal methods

| Skill | Purpose |
|-------|---------|
| [`formal-specs-lilo`](skills/formal-methods/formal-specs-lilo/SKILL.md) | Formalize natural-language requirements into Lilo by extending an existing SpecForge system or creating a new one, with ambiguity elicitation and syntax-only validation. |
| [`uppaal`](skills/formal-methods/uppaal/SKILL.md) | Build correct, runnable UPPAAL timed-automata models — networks of TA, clocks/guards/invariants, synchronisation channels, urgent/committed locations, templates, and TCTL queries — emitting a single `.xml` (queries embedded) that loads and verifies in UPPAAL. |

### AI

| Skill | Purpose |
|-------|---------|
| [`creating-ai-newsletters`](skills/ai/creating-ai-newsletters/SKILL.md) | Save and email a source-verified English/Simplified-Chinese weekly AI newsletter, track checkbox-marked interests, and research qualifying follow-ups. |
| [`qna`](skills/ai/qna/SKILL.md) | Pace long answers instead of dumping them — deliver a big explanation one part at a time, checking in with the user before continuing. Invoked with `/qna` (opt-in per question). |

### Engineering

Empty for now; reserved for future engineering skills.

## Layout

```
skills/
  formal-methods/
    formal-specs-lilo/
      SKILL.md
      agents/openai.yaml
      references/
    uppaal/
      SKILL.md        # thin launcher
      reference/      # workflow docs loaded on demand
  ai/
    creating-ai-newsletters/
      SKILL.md
      agents/openai.yaml
      references/newsletter-template.md
      scripts/newsletter_state.py
    qna/
      SKILL.md        # one skill per directory; SKILL.md is the entry point
  engineering/        # reserved

knowledge/
  formal-methods/
  ai/
    AI-newsletter/    # dated newsletter editions (see below)
  engineering/        # reserved
```

Each skill is a directory under `skills/<topic>/` containing a `SKILL.md` with YAML frontmatter (`name`, `description`) and the skill body. The topic directory is organizational only — runtimes discover a skill by the directory you symlink, not by its position in this tree.

## Scripts

Standalone helper scripts live under `scripts/`.

| Script | Purpose |
|--------|---------|
| [`compare_tokenizers.py`](scripts/compare_tokenizers.py) | Compare how two Claude models tokenize the same strings via the `count_tokens` API — identical counts across varied inputs indicate a shared vocabulary. Requires the `anthropic` SDK and API credentials. |

```bash
pip install anthropic
export ANTHROPIC_API_KEY=...   # or: ant auth login
python scripts/compare_tokenizers.py claude-opus-4-8 claude-haiku-4-5
```

## Knowledge

Study notes and reference write-ups live under `knowledge/`, grouped by the same topics as the skills.

### Formal methods

| Note | Topic |
|------|-------|
| [`fret-concepts-and-fretish.md`](knowledge/formal-methods/fret-concepts-and-fretish.md) | NASA FRET part 1 — the requirements-formalization mental model, the six-field FRETish language, variables as interface (not implementation), and the AI-assisted "draft → validate" formalization workflow. |
| [`fret-cli-and-setup.md`](knowledge/formal-methods/fret-cli-and-setup.md) | NASA FRET part 2 — the headless `fretcli` (`formalize`/`realizability`/`list`), the two-tier plan, and the verified no-sudo setup on WSL/Ubuntu 22.04 (Node 20, kind2 v2.2.0, z3 4.14.1). |
| [`specforge-learning-notes.md`](knowledge/formal-methods/specforge-learning-notes.md) | Imiron SpecForge — the AI-assisted formal-specification platform, its Signal Temporal Logic core, and how LLM-drafted specs pair with deterministic analysis. |

### AI

| Note | Topic |
|------|-------|
| [`llm-tokens-and-attention.md`](knowledge/ai/llm-tokens-and-attention.md) | How LLMs work end to end — tokenization (BPE/WordPiece/Unigram), embeddings, training & gradient descent, positional encoding (RoPE), and attention (Q/K/V, transformer layers, MLP), plus the philosophical limits of what an LLM's output can mean. |
| [`workplace-ai-policy-survey.md`](knowledge/ai/workplace-ai-policy-survey.md) | Baseline record of named employers that encourage, discourage, or disallow their own employees' AI use, from the 2023 bans through the 2026 reversals, with an evidence label per row. Read it before writing the newsletter's `AI at Work` section so a candidate can be judged as a change rather than a restatement. |

### Engineering

Empty for now; reserved for future engineering notes.

### AI newsletter archive

`knowledge/ai/AI-newsletter/` holds the dated editions produced by the
[`creating-ai-newsletters`](skills/ai/creating-ai-newsletters/SKILL.md) skill, one file per edition
(`YYYY-MM-DD-ai-newsletter.md`). The archive is the skill's live state, not just an output log:

- Each story carries a stable HTML anchor and an `- [ ] Interesting` checkbox. Change one to `[x]`
  to mark that story, and the next edition researches in-window follow-ups for it and lists it
  under `Tracked Interests` until you uncheck it.
- The skill's preflight moves unmarked editions older than six months into
  `knowledge/ai/.AI-newsletter-trash/` (recoverable, purged after 30 days) and never touches an
  edition that still contains a mark.
- The `AI at Work` section keeps its prior state outside the archive, in
  [`knowledge/ai/workplace-ai-policy-survey.md`](knowledge/ai/workplace-ai-policy-survey.md). Read
  that file before writing the section and update it after publishing one, so each edition reports
  a stance *change* rather than a policy that was already in force.

```bash
# preflight: prune the archive and list active interest marks
python3 skills/ai/creating-ai-newsletters/scripts/newsletter_state.py prepare \
  --archive knowledge/ai/AI-newsletter \
  --trash knowledge/ai/.AI-newsletter-trash \
  --today "$(date +%F)"

# validate a saved edition against the template contract
python3 skills/ai/creating-ai-newsletters/scripts/newsletter_state.py validate \
  knowledge/ai/AI-newsletter/2026-08-04-ai-newsletter.md
```

## Installation

Skills are picked up from a runtime's skills directory, which expects `<name>/SKILL.md` one level
down. The topic grouping in this repo is therefore flattened when you install: symlink each skill
directory in by its own name, not by `<topic>/<name>`.

```bash
# from a clone of this repo
REPO="$(pwd)"

for dir in ~/.claude/skills ~/.agents/skills ~/.codex/skills; do
  mkdir -p "$dir"
  for skill in "$REPO"/skills/*/*/; do          # <topic>/<skill>/
    [ -f "$skill/SKILL.md" ] || continue        # skip .gitkeep-only topic dirs
    ln -sfn "$skill" "$dir/$(basename "$skill")"
  done
done
```

`ln -sfn` makes this re-runnable: run it again after moving a skill between topics and the existing
links are repointed rather than duplicated.

- `~/.claude/skills` — Claude Code
- `~/.codex/skills` — Codex
- `~/.agents/skills` — cross-runtime alias recognized by Codex/Copilot/Gemini

Editing a skill in this repo then propagates to every runtime automatically.

## License

[MIT](LICENSE) — use, adapt, and redistribute these skills freely, keeping the copyright notice.
Provided as is, without warranty.
