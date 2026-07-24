# AI Newsletter Persistence and Interests Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extend `creating-ai-newsletters` with government-source exclusion, persistent Markdown editions, checkbox-based interest tracking and follow-ups, and safe six-month retention.

**Architecture:** Markdown editions remain the sole state store. A standard-library Python helper parses the canonical newsletter structure, reports active interests as JSON, validates editions, moves expired unmarked editions to recoverable trash, and purges old trash; `SKILL.md` orchestrates that helper around web research and saving, while the reference template defines the stable anchors, checkboxes, and separate new/follow-up/tracking sections.

**Tech Stack:** Agent Skills Markdown/YAML, Python 3 standard library, `unittest`, Git.

## Global Constraints

- Government agencies, ministries, regulators, legislatures, courts, intergovernmental bodies, and state-controlled media are ineligible as cited or supporting sources in every language.
- Public universities and publicly funded research institutions remain eligible.
- Independent reporting about government actions requires an exact in-window event date and confirmation from at least two reputable, independent, non-government sources.
- Save editions as `knowledge/AI-newsletter/YYYY-MM-DD-ai-newsletter.md` and return both a clickable file link and the complete newsletter inline.
- Never overwrite a same-day edition without an explicit user request.
- Keep five to seven independent `New Stories` unless fewer qualify; place any number of meaningful qualifying follow-ups in their own section.
- Every new story has a stable HTML anchor and `- [ ] Interesting`; the original checkbox is the sole interest record.
- Every active mark appears under `Tracked Interests`, including a no-update status and a six-month review reminder when applicable.
- Move unmarked editions older than six calendar months to `knowledge/.AI-newsletter-trash/`; preserve marked editions and purge trash older than 30 days.
- Cleanup never follows symlinks or changes unrelated or malformed files.
- Python code uses only the standard library.

---

## File Map

- Create `skills/creating-ai-newsletters/scripts/newsletter_state.py`: deterministic parser, interest scan, retention cleanup, validation, and JSON CLI.
- Create `tests/test_newsletter_state.py`: unit tests for parsing, calendar boundaries, cleanup safety, CLI JSON, and validation.
- Modify `skills/creating-ai-newsletters/SKILL.md`: source exclusions, preflight, research split, persistence, marking, reminders, and failure rules.
- Modify `skills/creating-ai-newsletters/references/newsletter-template.md`: canonical saved-edition structure with anchors, checkboxes, follow-ups, and tracked interests.
- Modify `skills/creating-ai-newsletters/agents/openai.yaml`: mention saved editions and tracked follow-ups in the interface prompt.
- Modify `README.md`: update the catalog description and layout for the helper.

### Task 1: Capture RED Behavior for the Existing Skill

**Files:**
- Create: none
- Modify: none
- Test: fresh-agent pressure scenarios without the revised skill content

**Interfaces:**
- Consumes: `docs/superpowers/specs/2026-07-24-ai-newsletter-persistence-and-interests-design.md`
- Produces: recorded baseline failures that the skill revision must correct

- [ ] **Step 1: Run a no-guidance control**

Give a fresh agent the current skill plus this request, without showing it the new design:

```text
Create this week's AI newsletter. Save it, follow up every story I marked in old editions, exclude government-operated sources, and clean up old editions safely. Return the saved path and the full newsletter.
```

- [ ] **Step 2: Record concrete failures**

Score whether the agent states or performs all of these behaviors:

```text
[ ] Saves to knowledge/AI-newsletter/YYYY-MM-DD-ai-newsletter.md
[ ] Refuses an ordinary same-day overwrite
[ ] Scans canonical [x] Interesting checkboxes before research
[ ] Keeps unlimited qualifying follow-ups separate from five to seven new stories
[ ] Lists every active mark and reminds about marks older than six months
[ ] Excludes government-operated and state-controlled sources in both languages
[ ] Requires two independent non-government reports for government-action stories
[ ] Moves only expired unmarked newsletters and purges only trash older than 30 days
[ ] Returns a clickable path followed by the complete Markdown edition
```

Expected RED result: the current skill omits persistence, checkbox state, retention, separated follow-ups, and the government-source prohibition.

- [ ] **Step 3: Preserve the baseline evidence**

Record the agent's response and failed checklist in the implementation log or task transcript. Do not edit the skill until the RED behavior has been observed.

### Task 2: Implement the State Parser and Validator with TDD

**Files:**
- Create: `tests/test_newsletter_state.py`
- Create: `skills/creating-ai-newsletters/scripts/newsletter_state.py`

**Interfaces:**
- Produces: `parse_edition(path: Path, today: date) -> Edition`
- Produces: `scan_archive(archive: Path, today: date) -> dict[str, object]`
- Produces: CLI `scan --archive PATH --today YYYY-MM-DD`
- Produces: CLI `validate FILE`
- `Interest` JSON fields: `edition_date`, `headline`, `anchor`, `path`, `relative_link`, `sources`, `overdue`

- [ ] **Step 1: Write failing parser tests**

Create `tests/test_newsletter_state.py` using `unittest`, temporary directories, and dynamic import of the helper. Include tests that construct canonical editions and assert:

```python
self.assertEqual(result["interests"][0]["headline"], "Example model ships")
self.assertEqual(result["interests"][0]["anchor"], "story-example-model-ships")
self.assertEqual(result["interests"][0]["sources"], ["https://example.com/release"])
self.assertTrue(result["interests"][0]["relative_link"].endswith(
    "2025-12-01-ai-newsletter.md#story-example-model-ships"
))
self.assertEqual(scan_with_unchecked_story["interests"], [])
self.assertIn("malformed checkbox/story association", malformed["errors"][0])
```

Also cover multiple marked stories, uppercase `[X]`, ignored checkboxes outside `New Stories`, invalid filenames, and symlinked editions.

- [ ] **Step 2: Run the parser tests and verify RED**

Run:

```bash
python3 -m unittest -v tests.test_newsletter_state
```

Expected: import or attribute failures because `newsletter_state.py` does not exist.

- [ ] **Step 3: Implement the minimal parser and scan CLI**

Implement immutable `Interest` and `Edition` dataclasses, exact active filename matching, canonical `## New Stories` section parsing, anchor/headline/checkbox association, Markdown URL extraction, six-calendar-month overdue calculation, and JSON serialization. Treat malformed matching files and symlinks as errors without mutating them.

The CLI grammar is:

```text
newsletter_state.py scan --archive PATH [--today YYYY-MM-DD]
newsletter_state.py validate FILE
```

Every command prints one JSON object. Operational or validation errors produce a nonzero exit status.

- [ ] **Step 4: Run parser tests and verify GREEN**

Run:

```bash
python3 -m unittest -v tests.test_newsletter_state
```

Expected: all parser, scan, and validation tests pass.

- [ ] **Step 5: Commit parser behavior**

```bash
git add tests/test_newsletter_state.py skills/creating-ai-newsletters/scripts/newsletter_state.py
git commit -m "feat: scan newsletter interest marks"
```

### Task 3: Implement Safe Retention with TDD

**Files:**
- Modify: `tests/test_newsletter_state.py`
- Modify: `skills/creating-ai-newsletters/scripts/newsletter_state.py`

**Interfaces:**
- Produces: `subtract_calendar_months(value: date, months: int) -> date`
- Produces: `cleanup_archive(archive: Path, trash: Path, today: date) -> dict[str, object]`
- Produces: CLI `cleanup --archive PATH --trash PATH --today YYYY-MM-DD`
- Produces: CLI `prepare --archive PATH --trash PATH --today YYYY-MM-DD`
- Result fields: `moved`, `purged`, `interests`, `errors`

- [ ] **Step 1: Write failing retention tests**

Add tests for:

```python
self.assertEqual(subtract_calendar_months(date(2026, 8, 31), 6), date(2026, 2, 28))
self.assertEqual(cleanup["moved"], [str(trash / expected_trash_name)])
self.assertTrue(marked_old.exists())
self.assertTrue(boundary_date.exists())
self.assertFalse(older_than_boundary.exists())
self.assertTrue(thirty_day_boundary.exists())
self.assertFalse(thirty_one_day_old.exists())
self.assertTrue(unrelated_file.exists())
self.assertTrue(symlink_path.is_symlink())
```

Test exact trash names in the form `TRASHED-YYYY-MM-DD--EDITION-YYYY-MM-DD-ai-newsletter.md`, collision refusal, malformed-file preservation, directory creation, and `prepare` returning post-cleanup interests.

- [ ] **Step 2: Run retention tests and verify RED**

Run:

```bash
python3 -m unittest -v tests.test_newsletter_state
```

Expected: failures for missing cleanup functions and CLI subcommands.

- [ ] **Step 3: Implement minimal safe cleanup**

Use `calendar.monthrange` for calendar subtraction, `Path.is_symlink()` before all file operations, exact regular expressions for active/trash targets, and `Path.replace()` only after confirming the destination does not exist. Purge only regular non-symlink trash files whose encoded trash date is strictly earlier than `today - timedelta(days=30)`.

`prepare` runs cleanup, stops with nonzero status on any error, then scans the remaining active archive and returns the combined JSON result.

- [ ] **Step 4: Run retention tests and verify GREEN**

Run:

```bash
python3 -m unittest -v tests.test_newsletter_state
```

Expected: all state-helper tests pass.

- [ ] **Step 5: Commit retention behavior**

```bash
git add tests/test_newsletter_state.py skills/creating-ai-newsletters/scripts/newsletter_state.py
git commit -m "feat: add safe newsletter retention"
```

### Task 4: Revise the Skill and Template from the RED Evidence

**Files:**
- Modify: `skills/creating-ai-newsletters/SKILL.md`
- Modify: `skills/creating-ai-newsletters/references/newsletter-template.md`
- Modify: `skills/creating-ai-newsletters/agents/openai.yaml`
- Modify: `README.md`

**Interfaces:**
- Consumes: helper `prepare` and `validate` commands from Tasks 2–3
- Produces: canonical edition Markdown parsable by the helper

- [ ] **Step 1: Add the preflight and source policy to `SKILL.md`**

Require this sequence before web discovery:

```text
1. Resolve the repository root and today's date in the user's timezone.
2. Refuse an ordinary save if today's target already exists.
3. Run newsletter_state.py prepare with the active archive, trash directory, and date.
4. Stop on a nonzero exit; report every moved and purged path.
5. Build follow-up queries for every returned active interest.
```

State the excluded government-operated source classes verbatim from the design. Keep public universities eligible. Require two reputable independent non-government sources when independently reporting government actions.

- [ ] **Step 2: Add the separate research and writing contracts**

Require:

```text
New Stories: five to seven independently selected items unless fewer pass.
Follow-ups to Interesting Stories: unlimited, meaningful in-window updates only.
Tracked Interests: every active mark, original relative link, update/no-update status,
six-month reminder, and explicit instruction to uncheck the original checkbox.
```

Forbid duplicate placement between new stories and follow-ups. State that follow-up priority never weakens the date, evidence, language, or source gates.

- [ ] **Step 3: Replace the reference template**

Define fixed top-level sections in this order:

```markdown
# {Newsletter title}
**Coverage:** ...
## Executive Brief
## New Stories
<a id="story-{stable-slug}"></a>
### {Headline}
- [ ] Interesting
...
## Follow-ups to Interesting Stories
...
## Tracked Interests
...
## Watch Next Week
## Sources
```

Require a stable unique anchor immediately before each new-story headline and the editable checkbox immediately below it. Follow-up and tracked-interest blocks link to the original anchored story but do not add checkboxes.

- [ ] **Step 4: Add save and post-save validation**

Require the agent to write the completed edition to the exact target, run:

```bash
python3 skills/creating-ai-newsletters/scripts/newsletter_state.py validate \
  knowledge/AI-newsletter/YYYY-MM-DD-ai-newsletter.md
```

On success, return a clickable path followed by the full saved Markdown. On validation failure, report the failure and do not present the edition as complete.

- [ ] **Step 5: Update discovery metadata**

Change the interface copy to mention a saved bilingual weekly digest with tracked follow-ups. Update the README catalog row and skill tree to include `scripts/newsletter_state.py`.

- [ ] **Step 6: Run structural and static checks**

Run:

```bash
python3 /home/rogu/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  skills/creating-ai-newsletters
rg -n "government|state-controlled|prepare|New Stories|Follow-ups to Interesting Stories|Tracked Interests|Interesting|AI-newsletter|six calendar months|30 days" \
  skills/creating-ai-newsletters/SKILL.md \
  skills/creating-ai-newsletters/references/newsletter-template.md
```

Expected: `Skill is valid!` and matches for every required behavior.

- [ ] **Step 7: Commit the skill revision**

```bash
git add README.md skills/creating-ai-newsletters
git commit -m "feat: persist and track AI newsletter interests"
```

### Task 5: Forward-Test and Verify the Complete Feature

**Files:**
- Modify only if a forward test exposes a concrete gap in the skill or template
- Test: helper suite, skill validator, fresh-agent scenarios, Git diff

**Interfaces:**
- Consumes: all prior tasks
- Produces: verified, merge-ready feature branch

- [ ] **Step 1: Run the same pressure scenario with the revised skill**

Give a fresh agent the revised skill, helper CLI help text, a synthetic archive with checked and unchecked old stories, and the original Task 1 request. Verify every Task 1 checklist item now passes.

- [ ] **Step 2: Run edge scenarios**

Test a same-day collision, a marked seven-month-old edition with no update, unlimited marked stories, an English government-action story supported by two independent sources, a Chinese state-controlled source, malformed Markdown, and a symlink in the archive. Tighten only guidance associated with observed failures and rerun affected scenarios.

- [ ] **Step 3: Run fresh full verification**

Run:

```bash
python3 -m unittest -v tests.test_newsletter_state
python3 /home/rogu/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  skills/creating-ai-newsletters
python3 -m py_compile skills/creating-ai-newsletters/scripts/newsletter_state.py
git diff --check main...HEAD
git status --short
```

Expected: all tests pass, the skill is valid, Python compiles, no whitespace errors exist, and only intended changes remain.

- [ ] **Step 4: Review requirements one-for-one**

Compare the implementation against every section of
`docs/superpowers/specs/2026-07-24-ai-newsletter-persistence-and-interests-design.md`.
Correct any uncovered gap under a RED-GREEN cycle.

- [ ] **Step 5: Commit any test-driven refinements**

```bash
git add README.md tests skills/creating-ai-newsletters
git diff --cached --quiet || git commit -m "test: harden newsletter interest workflow"
```

- [ ] **Step 6: Merge and verify**

Merge `feature/newsletter-interest-tracking` into `main`, rerun the full verification commands on `main`, and delete the merged feature branch only after verification succeeds.
