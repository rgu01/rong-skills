# rong-skills

A small collection of personal [Agent Skills](https://agentskills.io) — reusable technique guides that an AI coding agent (Claude Code, Codex, and other skill-aware runtimes) loads on demand.

## Skills

| Skill | Purpose |
|-------|---------|
| [`qna`](skills/qna/SKILL.md) | Pace long answers instead of dumping them — deliver a big explanation one part at a time, checking in with the user before continuing. Invoked with `/qna` (opt-in per question). |

## Layout

```
skills/
  qna/
    SKILL.md        # one skill per directory; SKILL.md is the entry point
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

## Installation

Skills are picked up from a runtime's skills directory. Symlink each skill you want into the directories for the runtimes you use, so a single source stays the source of truth:

```bash
# from a clone of this repo
REPO="$(pwd)"

for dir in ~/.claude/skills ~/.agents/skills ~/.codex/skills; do
  mkdir -p "$dir"
  ln -s "$REPO/skills/qna" "$dir/qna"
done
```

- `~/.claude/skills` — Claude Code
- `~/.codex/skills` — Codex
- `~/.agents/skills` — cross-runtime alias recognized by Codex/Copilot/Gemini

Editing a skill in this repo then propagates to every runtime automatically.

## License

Personal use.
