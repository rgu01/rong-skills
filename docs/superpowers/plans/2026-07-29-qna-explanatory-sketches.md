# QnA Explanatory Sketches Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the `qna` skill draw compact explanatory sketches when they materially improve a paced answer.

**Architecture:** Keep the behavior entirely in the existing Markdown skill and protect it with a focused Python contract test. Add one positive recipe that selects, draws, and explains a sketch without revealing later answer chunks.

**Tech Stack:** Markdown, Python standard-library `unittest`

## Global Constraints

- Use lightweight inline ASCII or Unicode sketches by default.
- Use Mermaid only when the response environment is known to render it.
- Prefer prose for simple facts, definitions, and linear explanations.
- Keep sketches within the current paced chunk and explain them immediately.

---

### Task 1: Add the explanatory-sketch contract

**Files:**
- Create: `tests/test_qna_skill_contract.py`
- Modify: `skills/qna/SKILL.md`

**Interfaces:**
- Consumes: the existing paced-answer structure in `skills/qna/SKILL.md`
- Produces: a documented per-chunk sketch decision protected by `QnaSkillContractTests`

- [x] **Step 1: Write the failing contract test**

Add `QnaSkillContractTests` assertions for the situations where sketches help, the lightweight text default, the prose fallback, immediate explanation, and current-chunk pacing.

- [x] **Step 2: Run the focused test and verify RED**

Run: `python -m unittest tests.test_qna_skill_contract -v`

Expected: four failures because the existing skill does not contain the explanatory-sketch contract.

- [x] **Step 3: Add the minimal skill guidance**

Add `## Sketch when it clarifies` with:

- a per-chunk visual decision;
- ASCII or Unicode as the default;
- Mermaid only when rendering support is known;
- prose for simple linear material;
- a compact example and immediate explanation; and
- a common-mistakes row against decorative or unexplained sketches.

- [x] **Step 4: Run the focused test and verify GREEN**

Run: `python -m unittest tests.test_qna_skill_contract -v`

Expected: all four QnA contract tests pass.

- [x] **Step 5: Run repository validation**

Run: `python -m unittest discover -s tests -v`

Expected: all 34 repository tests pass.

Run: `python /home/rogu/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/qna`

Observed: the validator rejects the pre-existing `disable-model-invocation` field. Preserve it because the README documents `qna` as opt-in via `/qna`; the implementation does not alter frontmatter.

- [x] **Step 6: Commit the implementation**

```bash
git add skills/qna/SKILL.md tests/test_qna_skill_contract.py docs/superpowers/plans/2026-07-29-qna-explanatory-sketches.md
git commit -m "Improve qna answers with explanatory sketches"
```
