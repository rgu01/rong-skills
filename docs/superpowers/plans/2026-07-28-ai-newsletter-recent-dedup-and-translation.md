# AI Newsletter Recent Deduplication and Translation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make every newsletter read the preceding seven days of archived Markdown editions, exclude previously published events, preserve established technical vocabulary in translation, and correct the 2026-07-28 edition.

**Architecture:** Keep Markdown editions as the only prior-story store. Add explicit preflight, selection, translation, and verification contracts to `SKILL.md`; do not change `newsletter_state.py`. Revise the current edition directly after comparing it with the qualifying archive files.

**Tech Stack:** Markdown skill instructions, Python `unittest` contract tests, the existing `newsletter_state.py` validator, and the standard Codex skill validator.

## Global Constraints

- Read every dated `.md` newsletter in `knowledge/AI-newsletter/` from the seven calendar dates preceding the new edition date.
- Deduplicate by the material underlying event, not headline, URL, source, section, or language.
- Retain established English technical vocabulary when literal Chinese would be nonstandard, awkward, or ambiguous.
- Do not change `skills/creating-ai-newsletters/scripts/newsletter_state.py`.
- Preserve current interest marks and do not alter unrelated archived editions.

---

### Task 1: Encode recent-edition exclusion and technical translation

**Files:**
- Modify: `tests/test_newsletter_content_contract.py`
- Modify: `skills/creating-ai-newsletters/SKILL.md`
- Modify: `.agents/napkin.md`

**Interfaces:**
- Consumes: dated Markdown editions named `YYYY-MM-DD-ai-newsletter.md` under `knowledge/AI-newsletter/`
- Produces: mandatory skill instructions for a private prior-event ledger and terminology-aware Simplified-Chinese translation

- [ ] **Step 1: Add failing static contract tests**

Add tests that read `SKILL.md` and require:

```python
def test_contract_reads_preceding_seven_days_of_markdown_editions(self) -> None:
    self.assertIn("seven calendar dates preceding", self.skill)
    self.assertIn("Read every selected edition completely", self.skill)
    self.assertIn("prior-event exclusion ledger", self.skill)

def test_contract_deduplicates_underlying_events_across_recent_editions(self) -> None:
    self.assertIn("material underlying event", self.skill)
    self.assertIn("headline, source, section, language", self.skill)
    self.assertIn("Reject", self.skill)

def test_contract_preserves_established_english_technical_terms(self) -> None:
    self.assertIn("established English technical", self.skill)
    self.assertIn("headless Linux", self.skill)
    self.assertIn("无头 Linux", self.skill)
```

- [ ] **Step 2: Run the focused tests and verify RED**

Run:

```bash
python3 -m unittest \
  tests.test_newsletter_content_contract.NewsletterContentContractTests.test_contract_reads_preceding_seven_days_of_markdown_editions \
  tests.test_newsletter_content_contract.NewsletterContentContractTests.test_contract_deduplicates_underlying_events_across_recent_editions \
  tests.test_newsletter_content_contract.NewsletterContentContractTests.test_contract_preserves_established_english_technical_terms -v
```

Expected: all three tests fail because the current skill does not contain the new contracts.

- [ ] **Step 3: Add the minimal recent-edition preflight**

In `SKILL.md`, after the existing archive preparation step, require the agent to:

```markdown
Before research, inspect `knowledge/AI-newsletter/` for active edition files
whose filename dates fall within the seven calendar dates preceding the new
edition date. Read every selected edition completely and build a private
prior-event exclusion ledger containing each story's headline, event date,
entities, product or project, material change, and source URLs.
```

Add the observable selection rule:

```markdown
Compare every candidate with the prior-event exclusion ledger before scoring.
Reject a candidate when its material underlying event already appeared,
regardless of headline, source, section, language, or later retrospective
coverage. The same entity or product remains eligible only for a distinct,
exactly dated material event; record the distinction in the candidate ledger.
```

- [ ] **Step 4: Add the minimal translation contract**

Replace the general technical-term sentence with:

```markdown
Translate for technical accuracy and natural usage, not word-for-word
symmetry. Preserve established English technical vocabulary when translating
it would be nonstandard, awkward, or ambiguous, including product and model
names, protocols, API and SDK names, commands, code identifiers, filenames,
platform names, and phrases such as `headless Linux`. Never render `headless
Linux` as `无头 Linux`. Use Chinese only when a conventional, unambiguous
technical term exists; when uncertain, keep the English term and translate the
surrounding sentence naturally.
```

Add both rules to the final verification checklist and common-mistakes table.

- [ ] **Step 5: Record the recurring user directive**

Add one priority-sorted `User Directives` item to `.agents/napkin.md`:

```markdown
1. **[2026-07-28] Deduplicate newsletters across the preceding seven days and preserve technical English**
   Do instead: read all recent newsletter Markdown files, exclude repeated underlying events, and retain established English technical terms when Chinese would be nonstandard.
```

Renumber the existing item to `2`.

- [ ] **Step 6: Run focused and full contract tests**

Run:

```bash
python3 -m unittest tests.test_newsletter_content_contract -v
```

Expected: all content-contract tests pass.

- [ ] **Step 7: Commit the workflow contract**

```bash
git add .agents/napkin.md skills/creating-ai-newsletters/SKILL.md tests/test_newsletter_content_contract.py
git commit -m "fix: prevent repeated newsletter stories"
```

### Task 2: Revise the 2026-07-28 edition

**Files:**
- Modify: `knowledge/AI-newsletter/2026-07-28-ai-newsletter.md`
- Read: `knowledge/AI-newsletter/2026-07-21-ai-newsletter.md` through `knowledge/AI-newsletter/2026-07-27-ai-newsletter.md` when present

**Interfaces:**
- Consumes: full text of qualifying prior editions and the validated 2026-07-28 edition
- Produces: a deduplicated, terminology-aware 2026-07-28 newsletter that retains the existing Markdown contract

- [ ] **Step 1: Build the prior-event comparison**

List qualifying files and extract their complete story blocks:

```bash
for edition in knowledge/AI-newsletter/2026-07-{21,22,23,24,25,26,27}-ai-newsletter.md; do
  if test -f "$edition"; then
    printf '%s\n' "$edition"
    sed -n '1,520p' "$edition"
  fi
done
```

Compare the current edition by underlying event and identify at minimum the
already-published AWS AgentCore unified-observability, Claude Opus 5, and AMD
Helios launch events.

- [ ] **Step 2: Remove repeated events and reconcile the edition**

Delete the repeated story blocks from the current edition and remove their
compact-source entries. Keep five AI Tools stories after removing the repeated
AgentCore event. Keep only distinct qualifying Other AI Stories unless research
finds a replacement with an exact in-window date and eligible opened source;
publishing fewer than three is required when no replacement passes.

Update the Executive Brief and `Watch Next Week` so they describe and cite only
events that remain in the edition.

- [ ] **Step 3: Improve technical translations**

Review every English/Chinese pair. Preserve technical expressions such as:

```text
headless Linux
MCP
Agents SDK
runtime
CloudWatch log group
IAM
ROCm
Android XR
```

Rewrite the NemoClaw sentence so `headless Linux` remains unchanged in the
Chinese line, and replace literal or awkward renderings elsewhere with natural
Chinese that retains established technical vocabulary.

- [ ] **Step 4: Preserve archive state and validate**

Confirm the two pre-existing active-interest marks remain only in their
original editions, then run:

```bash
python3 skills/creating-ai-newsletters/scripts/newsletter_state.py validate \
  knowledge/AI-newsletter/2026-07-28-ai-newsletter.md
```

Expected: `"valid": true` and `"errors": []`.

- [ ] **Step 5: Commit the corrected edition**

```bash
git add knowledge/AI-newsletter/2026-07-28-ai-newsletter.md
git commit -m "fix: deduplicate July 28 AI newsletter"
```

### Task 3: Validate the complete skill

**Files:**
- Verify: `skills/creating-ai-newsletters/`
- Verify: `tests/test_newsletter_content_contract.py`
- Verify: `tests/test_newsletter_state.py`
- Verify: `knowledge/AI-newsletter/2026-07-28-ai-newsletter.md`

**Interfaces:**
- Consumes: the completed skill and corrected edition
- Produces: fresh structural, behavioral, and archive-validation evidence

- [ ] **Step 1: Run all newsletter tests**

```bash
python3 -m unittest \
  tests.test_newsletter_content_contract \
  tests.test_newsletter_state -v
```

Expected: zero failures and zero errors.

- [ ] **Step 2: Run the standard skill validator**

```bash
python3 /home/rogu/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  skills/creating-ai-newsletters
```

Expected: validation succeeds.

- [ ] **Step 3: Revalidate the corrected edition**

```bash
python3 skills/creating-ai-newsletters/scripts/newsletter_state.py validate \
  knowledge/AI-newsletter/2026-07-28-ai-newsletter.md
```

Expected: `"valid": true` and `"errors": []`.

- [ ] **Step 4: Inspect the final diff**

```bash
git status --short
git diff --check HEAD~2..HEAD
git show --stat --oneline HEAD~2..HEAD
```

Confirm no unrelated user-owned archive changes were staged or committed.
