# rong-skills

A small collection of personal [Agent Skills](https://agentskills.io) — reusable technique guides that an AI coding agent (Claude Code, Codex, and other skill-aware runtimes) loads on demand.

## Skills

| Skill | Purpose |
|-------|---------|
| [`creating-ai-newsletters`](skills/creating-ai-newsletters/SKILL.md) | Save and email a source-verified English/Simplified-Chinese weekly AI newsletter, track checkbox-marked interests, and research qualifying follow-ups. |
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
