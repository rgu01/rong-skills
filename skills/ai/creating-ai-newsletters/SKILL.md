---
name: creating-ai-newsletters
description: Use when a user asks for the latest or past week's AI news, an AI roundup or weekly digest, a saved Markdown AI newsletter, or an English and Simplified-Chinese AI news brief for mixed business and technical readers.
---

# Creating AI Newsletters

## Core principle

Research the event, not the headline. Publish fewer stories rather than relax
the date, evidence, source-quality, or language rules. Lead with tools for
building and operating AI agents. Follow-ups add a separate view of marked
interests; they never displace or weaken either new-story selection.

## Defaults

Unless the user overrides them:

- Audience: mixed business and technical
- Window: publication date plus the six preceding dates in the user's timezone
- AI Tools: five to seven
- Other AI Stories: three to five
- Voice: sharp and professional
- Format: polished Markdown with stable HTML story anchors
- Archive: `<rong-skills-repo>/knowledge/ai/AI-newsletter/`
- Trash: `<rong-skills-repo>/knowledge/ai/.AI-newsletter-trash/`
- Email recipient: `ronggufly@gmail.com`

## Preflight: archive and interests

Always save under the `rong-skills` repository that contains this skill,
wherever that repo is checked out — never under the current working directory.
This skill lives at `<rong-skills-repo>/skills/ai/creating-ai-newsletters`, so
the repo root is three directories above the skill directory — skills are
grouped by topic (`ai/`, `formal-methods/`, `engineering/`). Resolve it by
following symlinks, for example:

```bash
REPO_ROOT="$(cd "$(dirname "$(readlink -f "$0")")/../../.." && pwd)"   # conceptually
# In practice, resolve the real path of the creating-ai-newsletters skill
# directory and take its great-grandparent as REPO_ROOT. Verify the result by
# checking that "$REPO_ROOT/knowledge" exists before writing anything.
```

Resolve that `REPO_ROOT` and today's date in the user's timezone. The ordinary
output target is
`$REPO_ROOT/knowledge/ai/AI-newsletter/YYYY-MM-DD-ai-newsletter.md`.
If that target already exists, stop before research; update or replace it only
when the user explicitly requests that action.

Run (with `REPO_ROOT` resolved to the rong-skills repo, using absolute paths):

```bash
python3 "$REPO_ROOT/skills/ai/creating-ai-newsletters/scripts/newsletter_state.py" prepare \
  --archive "$REPO_ROOT/knowledge/ai/AI-newsletter" \
  --trash "$REPO_ROOT/knowledge/ai/.AI-newsletter-trash" \
  --today YYYY-MM-DD
```

This creates missing directories, moves unmarked editions older than six
calendar months to recoverable trash, permanently purges newsletter trash
entries older than 30 days, and returns all active `[x] Interesting` records as
JSON. It preserves old editions containing a mark. Report every moved or purged
path in the final response.

A nonzero exit or any returned error blocks generation. Never work around a
malformed edition, symlink, cleanup collision, or incomplete interest scan.

## Source eligibility

Government agencies, ministries, regulators, legislatures, courts,
intergovernmental bodies, and state-controlled media are ineligible as primary,
secondary, date-evidence, or supporting sources in every language. Do not cite
or rely on them.

Public universities and publicly funded research institutions remain eligible.
Independent reporting about a government action is eligible only when the
underlying event date is exact and wholly inside the coverage window and at
least two reputable, independent, non-government sources confirm every material
claim. Reject a source when its operational independence is ambiguous.

Company, laboratory, academic, repository, and independent-media sources retain
the existing evidence hierarchy.

## Research

### Follow marked interests

Before general discovery, build queries for every active interest returned by
the helper using its headline, original story text, entities, products, and
source links. Research every mark; there is no numerical limit.

A follow-up qualifies only when a meaningful new event occurred wholly inside
the current window and passes the same date, evidence, source, and language
rules as a new story. A recent article about an unchanged old event is not a
follow-up. Freeze qualifying results in a separate follow-up manifest. Keep
marks with no qualifying update for `Tracked Interests`.

### Discover AI Tools

Treat AI Tools as the primary editorial selection. Qualifying tools help
developers or operators build, use, integrate, deploy, evaluate, observe,
secure, govern, or manage AI agents. Prioritize:

- agent orchestration frameworks, SDKs, workflow builders, and multi-agent
  coordination;
- tool calling, MCP, A2A, connectors, memory, data access, and reusable skills;
- agent runtimes, sandboxes, durable execution, checkpointing, deployment, and
  human approval;
- registries, identity, permissions, versioning, security, governance, and cost
  control;
- tracing, debugging, observability, evaluation, testing, monitoring, and
  feedback pipelines.

A meaningful launch, release, material update, or ecosystem change must occur
inside the coverage window. Exclude model releases without agent-development
capabilities, consumer AI applications, generic developer tools without a
direct agent-workflow use, minor features marketed as agentic, and the mere
rediscovery of an existing tool.

### Discover Other AI Stories

Preserve the existing broader AI coverage across:

- models and research
- non-agent products
- business and industry
- policy, safety, and security

### Research both selections

1. State the exact start date, end date, and timezone.
2. Search in English and Simplified Chinese for AI Tools and for each of the
   four Other AI Stories buckets.
3. Build separate private candidate ledgers for AI Tools and Other AI Stories.
   Each row records the material event, origin language,
   exact underlying event date or date range, date-evidence source, gating
   earlier material activity and its exact date evidence or `N/A`, optional
   non-gating background, source-operator class, `Date gate: PASS/REJECT`,
   bucket, primary source, useful secondary source, duplicate group, conflicts,
   and scores.
4. Open every source used. Cite the exact article, announcement, paper,
   repository release, company filing, or independent report containing the
   date evidence and material claims. Category, tag, index, search-result, and
   homepage pages are discovery aids, not story citations.
5. Prefer original company, laboratory, academic, or repository sources and
   established independent technology or business reporting. Seek strong
   coverage in both languages when available; never add a weak source for
   symmetry.
6. For a default edition, run at least one English query and one
   Simplified-Chinese query, written in Simplified Chinese, for AI Tools and
   each of the four Other AI Stories buckets. Record the exact query, candidates
   opened, and selection or rejection reasons for all ten language-by-bucket
   audit entries before scoring.

Apply this gate to every follow-up, AI Tools, and Other AI Stories row:

- Record the exact underlying event date or date range, opened source URL, and
  source passage supporting that date.
- If an earlier incident, failure, evaluation, pause, or deployment is material
  to eligibility, record it separately with exact date evidence. Pure context
  is non-gating.
- Mark `Date gate: PASS` only when the event and every gating earlier activity
  have exact dates wholly inside the window. Confirm with a literal ISO-date
  comparison.
- Reject missing, relative-only, undated, partly out-of-window, or
  publication-date-only evidence, even when fewer stories remain.
- A dated partnership or remediation does not make an older or undated incident
  eligible. Never rename a retrospective disclosure as a new event.

The underlying event date controls eligibility. An announcement date qualifies
only when the announcement itself creates the event, such as a launch.

## Select

Reject candidates that are outside the window, inaccessible at the
material-claim level, primarily promotional, government-operated, or duplicates
of a stronger entry.

Score each eligible candidate from 0 to 2:

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Recency | outside window; reject | first four dates | latest three dates |
| Impact | narrow update | meaningful sector effect | major technical, market, or policy effect |
| Credibility | unsupported; reject | reputable secondary evidence | direct authoritative evidence |
| Mixed-audience relevance | little value | business or technical value | clear value to both |

For AI Tools, also score practical agent-workflow relevance: reject a tool with
no direct agent-lifecycle use, score 1 for a useful narrow capability, and score
2 for clear day-to-day value in building or operating agents.

Rank by score and editorial judgment. Prefer broadly useful agent lifecycle
infrastructure within AI Tools and reasonable bucket balance within Other AI
Stories. Merge only reports about the same event. Select five to seven AI Tools
and three to five Other AI Stories, or fewer in either section when fewer meet
the standard. The counts are independent and do not change with the number of
follow-ups.

Freeze separate manifests for AI Tools and Other AI Stories containing each
selected headline, event, exact date, primary URL, and `Date gate: PASS`.
Reject any event duplicating a selected follow-up or appearing in the other
manifest. A follow-up never appears in either new-story section.

## Write

Read `references/newsletter-template.md` completely and follow its fixed section
order.

- Give every story in `AI Tools` and `Other AI Stories` a unique stable HTML
  anchor immediately before its headline and `- [ ] Interesting` immediately
  below it.
- For every AI Tools item, identify what shipped, the agent-lifecycle problem
  it addresses, and why it matters to practitioners.
- Do not add interest checkboxes to follow-ups or tracked-interest reminders.
- Put qualifying updates only in `Follow-ups to Interesting Stories`.
- List every active mark in `Tracked Interests`, linking to its original
  anchored story. State whether a qualifying update was found. Otherwise write
  `No qualifying update found this week`.
- For a mark older than six months, add a prominent review reminder. Every
  tracked item tells the user to uncheck the original story to stop tracking it.

Determine origin language from the strongest eligible primary source:

- When an eligible authoritative source offers parallel versions, use the
  original announcement language to determine origin.
- English-origin story: write each body sentence in English, followed
  immediately on the next line by exactly one faithful Simplified Chinese
  translation.
- Chinese-origin story: write its headline, labels, and body in Chinese only;
  do not back-translate it into English.
- Keep newsletter-level headings exactly as the template specifies and every
  story headline in its primary source's language.
- Keep source names and URLs unchanged. Show each selected primary URL once in
  its story and once in the compact source list.
- `Watch Next Week` contains only forward-looking implications supported by
  sources already cited in a selected new story or follow-up.

Translations preserve names, identifiers, numbers, dates, benchmarks, technical
terms, confidence, and caveats. Never add a claim to only one language.

## Save and return

For ordinary generation, write the completed edition to a new output target and
never overwrite an existing file. When the user explicitly asks to update or
replace an existing same-day edition, follow that request in place and preserve
any existing interest marks unless the user explicitly changes them. Then run:

```bash
python3 "$REPO_ROOT/skills/ai/creating-ai-newsletters/scripts/newsletter_state.py" validate \
  "$REPO_ROOT/knowledge/ai/AI-newsletter/YYYY-MM-DD-ai-newsletter.md"
```

If validation fails, report the errors and do not present the edition as
complete. If it succeeds, first report the cleanup result, then return a
clickable link to the saved path followed immediately by the complete saved
newsletter inline.

## Email delivery

After the edition is saved and the validation command succeeds, email the exact
saved Markdown to `ronggufly@gmail.com`:

- Subject: `AI Newsletter — YYYY-MM-DD` using the edition date.
- Body: the complete saved Markdown, byte-for-byte equivalent to the validated
  file. Do not send the private ledger, query audit, manifests, or cleanup
  diagnostics.
- Attach the saved `.md` file only when the available email connector supports
  attachments; the Markdown body remains required.
- Use the available email connector or app tool and follow any required
  confirmation step. Do not invent an email API, SMTP command, or delivery
  result when no connector is available.
- Send only after validation; never email a draft or an edition that failed
  validation.

If no email connector is available, state that the newsletter was saved and
validated but was **not sent** to `ronggufly@gmail.com` because email delivery
is unavailable; do not claim delivery. If the connector reports a send error,
preserve the saved newsletter, report the error, and do not claim delivery.
Successful delivery must be reported separately from the saved-file link and
inline newsletter. Attempt delivery before composing the final response; then
report cleanup, delivery status, the saved-file link, and the complete inline
newsletter in that response.

## Verify before publishing

- Coverage dates and timezone are explicit.
- Every selected underlying event and gating activity is exactly dated inside
  the window and supported by an opened eligible source.
- No government-operated or state-controlled source supports any claim.
- Every government-action story has two qualifying independent confirmations.
- AI Tools, Other AI Stories, and follow-up manifests are separate; no event
  appears in more than one.
- `AI Tools` contains five to seven items and `Other AI Stories` contains three
  to five items unless fewer pass. Their counts are independent; follow-ups are
  uncapped and do not affect either count.
- Every new story has one unique anchor and one unchecked interest checkbox.
- Every active mark appears in `Tracked Interests` with an original link,
  status, uncheck instruction, and overdue reminder when applicable.
- Every English-origin body sentence has one immediate Simplified Chinese pair.
- Chinese-origin text and unchanged source names and URLs are not redundantly
  translated.
- The ledger, query audit, manifests, story blocks, and compact source list
  reconcile one-for-one on headline, exact date, and primary URL.
- Every `Watch Next Week` implication uses an already-cited source.
- The saved file passes helper validation and the inline copy matches it.

If a date, source independence, or material claim cannot be verified, state the
limitation precisely or omit the story.

## Common mistakes

| Mistake | Correction |
|---|---|
| Treating a regulator page as authoritative evidence | Government-operated sources are excluded; use qualifying independent evidence. |
| Treating a consumer AI app as an AI Tool | Require a direct use in building, integrating, deploying, evaluating, or operating AI agents. |
| Letting one selection reduce the other | Select five to seven AI Tools and three to five Other AI Stories independently of follow-ups. |
| Dropping a mark when no update exists | Keep it in `Tracked Interests` with the exact no-update status. |
| Copying a checkbox into a follow-up | Only the original new-story block owns the checkbox. |
| Deleting an old marked edition | Preserve it and remind the user to review the mark. |
| Using an article's date for an older event | Verify and use the underlying event date. |
| Adding weak Chinese coverage for symmetry | Keep only sources that improve evidence or context. |
| Returning only a saved path | Return the clickable path and the complete saved Markdown. |
