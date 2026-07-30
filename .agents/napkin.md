# Napkin Runbook

## Curation Rules
- Re-prioritize on every read.
- Keep recurring, high-value notes only.
- Max 10 items per category.
- Each item includes date + "Do instead".

## Execution & Validation (Highest Priority)

1. **[2026-07-30] Detect git execution context before worktree or branch-finishing operations**
   Do instead: compare the absolute `git rev-parse --git-dir` and `--git-common-dir` results and inspect `git branch --show-current`; skip worktree creation in a linked worktree and treat an empty branch as detached HEAD.

2. **[2026-07-30] Finish detached Codex App work through native controls**
   Do instead: test and commit locally, then tell the user to use “Create branch” or “Hand off to local,” including suggested branch, commit, and PR text.

## Shell & Command Reliability

1. **[2026-07-30] Enable multi-agent support before using dispatch skills**
   Do instead: ensure `[features] multi_agent = true` is present in `~/.codex/config.toml`; keep implementers available through review fix loops and release reviewer slots after their findings return.

## Domain Behavior Guardrails

## User Directives

1. **[2026-07-29] Pace SpecForge teaching with the `qna` skill**
   Do instead: teach one short concept at a time, spell out acronyms on first use, and wait for the user's signal before continuing or going deeper.

2. **[2026-07-29] Use explanatory sketches when they materially improve understanding**
   Do instead: add compact text sketches for structure, flow, hierarchy, or relationships, while keeping simple linear explanations in prose.

3. **[2026-07-27] Make AI agent tools the newsletter's primary coverage**
   Do instead: select 5–7 agent-tool stories and 3–5 broader AI stories independently in every edition.

4. **[2026-07-29] Cover AI + Formal Methods news in every newsletter edition**
   Do instead: run dedicated queries for AI-assisted formal specification/verification tools (e.g. Imiron SpecForge, LLM-to-formal-spec, STL/temporal-logic tooling, AI safety verification) alongside the standard buckets, and follow the tracked SpecForge spotlight (2026-07-29 edition) for Imiron updates.
