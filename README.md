# rong-skills

A small collection of personal [Agent Skills](https://agentskills.io) — reusable technique guides that an AI coding agent (Claude Code, Codex, and other skill-aware runtimes) loads on demand.

## Skills

| Skill | Purpose |
|-------|---------|
| [`creating-ai-newsletters`](skills/creating-ai-newsletters/SKILL.md) | Save and email a source-verified English/Simplified-Chinese weekly AI newsletter, track checkbox-marked interests, and research qualifying follow-ups. |
| [`formal-specs-lilo`](skills/formal-specs-lilo/SKILL.md) | Formalize natural-language requirements into Lilo by extending an existing SpecForge system or creating a new one, with ambiguity elicitation and syntax-only validation. |
| [`qna`](skills/qna/SKILL.md) | Pace long answers instead of dumping them — deliver a big explanation one part at a time, checking in with the user before continuing. Invoked with `/qna` (opt-in per question). |
| [`uppaal`](skills/uppaal/SKILL.md) | Build correct, runnable UPPAAL timed-automata models — networks of TA, clocks/guards/invariants, synchronisation channels, urgent/committed locations, templates, and TCTL queries — emitting a single `.xml` (queries embedded) that loads and verifies in UPPAAL. |

## Layout

```
skills/
  creating-ai-newsletters/
    SKILL.md
    agents/openai.yaml
    references/newsletter-template.md
    scripts/newsletter_state.py
  formal-specs-lilo/
    SKILL.md
    agents/openai.yaml
    references/
  qna/
    SKILL.md        # one skill per directory; SKILL.md is the entry point
  uppaal/
    SKILL.md        # thin launcher
    reference/      # workflow docs loaded on demand
```

Each skill is a directory under `skills/` containing a `SKILL.md` with YAML frontmatter (`name`, `description`) and the skill body.

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

Study notes and reference write-ups live under `knowledge/`.

| Note | Topic |
|------|-------|
| [`llm-tokens-and-attention.md`](knowledge/llm-tokens-and-attention.md) | How LLMs work end to end — tokenization (BPE/WordPiece/Unigram), embeddings, training & gradient descent, positional encoding (RoPE), and attention (Q/K/V, transformer layers, MLP), plus the philosophical limits of what an LLM's output can mean. |
| [`fret-concepts-and-fretish.md`](knowledge/fret-concepts-and-fretish.md) | NASA FRET part 1 — the requirements-formalization mental model, the six-field FRETish language, variables as interface (not implementation), and the AI-assisted "draft → validate" formalization workflow. |
| [`fret-cli-and-setup.md`](knowledge/fret-cli-and-setup.md) | NASA FRET part 2 — the headless `fretcli` (`formalize`/`realizability`/`list`), the two-tier plan, and the verified no-sudo setup on WSL/Ubuntu 22.04 (Node 20, kind2 v2.2.0, z3 4.14.1). |
| [`specforge-learning-notes.md`](knowledge/specforge-learning-notes.md) | Imiron SpecForge — the AI-assisted formal-specification platform, its Signal Temporal Logic core, and how LLM-drafted specs pair with deterministic analysis. |

### AI newsletter archive

`knowledge/AI-newsletter/` holds the dated editions produced by the
[`creating-ai-newsletters`](skills/creating-ai-newsletters/SKILL.md) skill, one file per edition
(`YYYY-MM-DD-ai-newsletter.md`). The archive is the skill's live state, not just an output log:

- Each story carries a stable HTML anchor and an `- [ ] Interesting` checkbox. Change one to `[x]`
  to mark that story, and the next edition researches in-window follow-ups for it and lists it
  under `Tracked Interests` until you uncheck it.
- The skill's preflight moves unmarked editions older than six months into
  `knowledge/.AI-newsletter-trash/` (recoverable, purged after 30 days) and never touches an
  edition that still contains a mark.

```bash
# preflight: prune the archive and list active interest marks
python3 skills/creating-ai-newsletters/scripts/newsletter_state.py prepare \
  --archive knowledge/AI-newsletter \
  --trash knowledge/.AI-newsletter-trash \
  --today "$(date +%F)"

# validate a saved edition against the template contract
python3 skills/creating-ai-newsletters/scripts/newsletter_state.py validate \
  knowledge/AI-newsletter/2026-08-04-ai-newsletter.md
```

## Installation

Skills are picked up from a runtime's skills directory. Symlink each skill you want into the directories for the runtimes you use, so a single source stays the source of truth:

```bash
# from a clone of this repo
REPO="$(pwd)"

for dir in ~/.claude/skills ~/.agents/skills ~/.codex/skills; do
  mkdir -p "$dir"
  for skill in "$REPO"/skills/*/; do
    ln -s "$skill" "$dir/$(basename "$skill")"
  done
done
```

- `~/.claude/skills` — Claude Code
- `~/.codex/skills` — Codex
- `~/.agents/skills` — cross-runtime alias recognized by Codex/Copilot/Gemini

Editing a skill in this repo then propagates to every runtime automatically.

## License

Personal use.
