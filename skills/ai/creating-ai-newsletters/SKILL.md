---
name: creating-ai-newsletters
description: Use when a user asks for the latest or past week's AI news, an AI roundup or weekly digest, a saved Markdown AI newsletter, or an English and Simplified-Chinese AI news brief for mixed business and technical readers.
---

# Creating AI Newsletters

## Core principle

Research the event, not the headline. Publish fewer stories rather than relax
the date, evidence, source-quality, or language rules. Lead with tools for
building and operating AI agents, and track separately how employers govern
their own employees' AI use. Follow-ups add a separate view of marked
interests; they never displace or weaken either new-story selection.

## Defaults

Unless the user overrides them:

- Audience: mixed business and technical
- Window: publication date plus the six preceding dates in the user's timezone
- AI Tools: five to seven
- Other AI Stories: three to five
- AI at Work: two to four
- Voice: sharp and professional
- Format: polished Markdown with stable HTML story anchors
- Archive: `<rong-skills-repo>/knowledge/ai/AI-newsletter/`
- Trash: `<rong-skills-repo>/knowledge/ai/.AI-newsletter-trash/`
- Email delivery: off. Send only when the request asks for it; the recipient is
  then `ronggufly@gmail.com`
- Final response: cleanup result, saved-file link, and a headline-and-date digest;
  the full edition inline only on request

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

Build queries for every active interest returned by the helper using its
headline, original story text, entities, products, and source links. Research
every mark; there is no numerical limit.

Marks and new-story discovery share no data, so this is a completeness
requirement, not an ordering one: issue mark queries in the same parallel batches
as discovery queries rather than finishing all marks first. Only the follow-up
manifest must be frozen before selection, because a follow-up outranks a
duplicate new story.

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

Sweep the dated vendor feeds first, then use open search to fill the gaps. These
feeds carry their own publication dates, so they satisfy the date gate without a
second lookup, and they have repeatedly supplied most of a week's selection:

- `claude.com/blog` and `platform.claude.com/docs` changelogs
- `aws.amazon.com/about-aws/whats-new` and the AgentCore release notes
- `github.blog/changelog`
- `blog.cloudflare.com`
- `langchain.com/blog` and the LangSmith changelog
- `devblogs.microsoft.com/agent-framework`, `developers.googleblog.com`
- GitHub releases pages for tools already covered

Aggregator digests and weekly-roundup sites are discovery aids only. Their dates
and attributions have proven unreliable — a hobby project reported as a
university study, a June government directive listed under an August date — so
re-derive every event and date from the primary source before scoring.

### Discover Other AI Stories

Preserve the existing broader AI coverage across:

- models and research
- non-agent products
- business and industry
- policy, safety, and security

### Discover AI at Work

`AI at Work` tracks how employers govern their own employees' use of AI in daily
work.

Read `$REPO_ROOT/knowledge/ai/workplace-ai-policy-survey.md` before researching
this section. It records each employer's already-known stance with an evidence
label, so a candidate can be judged as a change rather than a restatement of a
policy that was already in force. After publishing an `AI at Work` story, add or
update that organization's row there with the new stance, the exact date, and the
edition that carried it. Never lift a row marked `Single source` or `Unverified`
into an edition without confirming it independently first.

A qualifying story names one organization and a stance change or first public
statement of a stance that occurred inside the coverage window:

- **Encouraging** — mandating, funding, licensing, training, incentivizing, or
  measuring AI use; shipping internal assistants; making AI use part of reviews
  or hiring criteria.
- **Discouraging** — restricting AI to approved tools, teams, data classes, or
  tasks; requiring disclosure or human review; withdrawing licenses; warning
  employees against use.
- **Disallowing** — prohibiting AI tools for employees outright or for a named
  function, business unit, or data class.

Classify by what the organization does to its own workforce, not by its opinion
about AI in general. Record the stance, the organization, the employee scope,
the named tools if stated, and whether the measure is enforced by policy or
merely recommended.

Evidence rules add to the general gate:

- Cite the organization's own memo, policy, handbook, filing, or executive
  statement when available, or reputable independent reporting that quotes or
  publishes it.
- A leaked or reported internal memo qualifies only when the exact memo or
  effective date is inside the window and at least two reputable, independent,
  non-government sources confirm its content.
- A public employer is a government-operated source: report its stance only
  through two qualifying independent non-government confirmations.
- Employee anecdotes, recruiter posts, and single anonymous forum claims do not
  establish an organizational stance.

Exclude vendor-authored adoption marketing, surveys and analyst reports about
employers in aggregate, national or sector-wide regulation of employers, an
organization's product decisions about customer-facing AI, and the restatement
of an existing unchanged policy.

### Research every selection

Run this work in parallel batches. Every mark query, every language-by-bucket
query, and every vendor-feed sweep is independent of the others, so issue them as
concurrent groups in one step and wait once, rather than one call at a time. Only
two points genuinely serialize: a candidate's primary-source check depends on
that candidate existing, and scoring depends on the ledgers being complete.
Serial execution of independent lookups has been the single largest cost in past
editions.

1. State the exact start date, end date, and timezone.
2. Search in English and Simplified Chinese for AI Tools, for each of the
   four Other AI Stories buckets, and for AI at Work.
3. Build separate private candidate ledgers for AI Tools, Other AI Stories, and
   AI at Work. Each row records the material event, origin language,
   exact underlying event date or date range, date-evidence source, gating
   earlier material activity and its exact date evidence or `N/A`, optional
   non-gating background, source-operator class, `Date gate: PASS/REJECT`,
   bucket, primary source, useful secondary source, duplicate group, conflicts,
   and scores. An AI at Work row also records the organization, the stance, the
   employee scope, and whether the measure is enforced or only recommended.
4. Screen cheaply before verifying expensively. Opening a page costs far more
   than reading a result, so before spending an open, require a date signal that
   is compatible with the window: a dated URL path, an explicit date in the
   snippet, or a dated feed entry. Discard a candidate whose only visible date is
   already outside the window, and record it as a snippet-level rejection. Open a
   page with no date signal only when the candidate would otherwise make the
   selection.
5. Open every source used for a candidate that survives screening. Cite the
   exact article, announcement, paper, repository release, company filing, or
   independent report containing the date evidence and material claims. Category,
   tag, index, search-result, and homepage pages are discovery aids, not story
   citations.
6. Prefer original company, laboratory, academic, or repository sources and
   established independent technology or business reporting. Seek strong
   coverage in both languages when available; never add a weak source for
   symmetry.
7. For a default edition, run at least one English query and one
   Simplified-Chinese query, written in Simplified Chinese, for AI Tools, for
   each of the four Other AI Stories buckets, and for AI at Work. Record the
   exact query, candidates opened, and selection or rejection reasons for all
   twelve language-by-bucket audit entries before scoring.

Apply this gate to every follow-up, AI Tools, Other AI Stories, and AI at Work
row:

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

For AI at Work, also score stance clarity: reject a story whose stance or
employee scope stays ambiguous, score 1 for a stance affecting one team,
function, or data class, and score 2 for an organization-wide stance with a
stated scope and enforcement.

Rank by score and editorial judgment. Prefer broadly useful agent lifecycle
infrastructure within AI Tools, reasonable bucket balance within Other AI
Stories, and a spread across encouraging, discouraging, and disallowing stances
within AI at Work when candidates allow it — never invent balance by admitting a
weaker story. Merge only reports about the same event. Select five to seven AI
Tools, three to five Other AI Stories, and two to four AI at Work items, or
fewer in any section when fewer meet the standard. The three counts are
independent and do not change with the number of follow-ups.

Freeze separate manifests for AI Tools, Other AI Stories, and AI at Work
containing each selected headline, event, exact date, primary URL, and
`Date gate: PASS`. Reject any event duplicating a selected follow-up or
appearing in another manifest. A follow-up never appears in any new-story
section.

## Write

Read `references/newsletter-template.md` completely and follow its fixed section
order.

- Give every story in `AI Tools`, `Other AI Stories`, and `AI at Work` a unique
  stable HTML anchor immediately before its headline and `- [ ] Interesting`
  immediately below it.
- For every AI Tools item, identify what shipped, the agent-lifecycle problem
  it addresses, and why it matters to practitioners.
- For every AI at Work item, state the organization, the stance as
  `Encouraging`, `Discouraging`, or `Disallowing`, the employee scope, and
  whether the measure is enforced or only recommended. Keep the section heading
  even when no candidate qualifies and say so in place of the story blocks.
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

Translations preserve names, identifiers, numbers, dates, benchmarks, confidence,
and caveats. Never add a claim to only one language.

Keep every technical term in English inside the Simplified Chinese translation
instead of rendering it in Chinese. This covers product, protocol, and standard
names (`MCP`, `A2A`, `AGENTS.md`, `OAuth`, `eBPF`, `gVisor`), file and API
identifiers, and the field's working vocabulary — `prompt`, `prompt injection`,
`token`, `agent`, `sandbox`, `context`, `context window`, `embedding`,
`checkpoint`, `benchmark`, `fine-tuning`, `inference`, `guardrail`,
`observability`, `runtime`. Write `prompt injection 风险`, not `提示注入风险`;
`每个 agent 的 token 支出`, not `每个智能体的令牌支出`; `context window 上限`, not
`上下文窗口上限`. Inflect the surrounding Chinese around the English term, keep the
term in its source capitalization, and do not gloss it in parentheses. Translate
only ordinary prose. This rule governs translations of English-origin prose; a
Chinese-origin story is written natively and keeps whatever vocabulary its own
primary source uses.

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
complete. If it succeeds, report in this order:

1. The cleanup result, naming every moved or purged path.
2. A clickable link to the saved path.
3. A short digest: the coverage window, the count in each section, every selected
   headline with its exact event date, and any section that published fewer items
   than its range with the reason.
4. Anything the user must act on, such as a validation warning, an unresolved
   source limitation, or a mark that is now overdue.

Do not paste the complete edition inline by default. The file is the deliverable
and the link reaches it; a full paste repeats the largest artifact of the run for
no gain. Paste the complete saved Markdown only when the user asks for it, and
when they do, paste it once.

## Email delivery

Email is **opt-in**. Send the edition only when the user's request for this run
asks for it — for example "send me an email", "email it to me", or "mail the
newsletter". Absent such a request, do not send, do not compose a body, and do
not ask whether to send; the saved file and its link are the delivery.

When the user does ask, first confirm that an email connector or app tool is
actually available, then compose the body. Composing a full edition body for a
connector that turns out to be unavailable wastes the largest artifact of the run.

- Send only after the edition is saved and the validation command succeeds; never
  email a draft or an edition that failed validation.
- Recipient: `ronggufly@gmail.com` unless the user names another.
- Subject: `AI Newsletter — YYYY-MM-DD` using the edition date.
- Body: the complete saved Markdown, byte-for-byte equivalent to the validated
  file. Do not send the private ledger, query audit, manifests, or cleanup
  diagnostics.
- Attach the saved `.md` file only when the connector supports attachments; the
  Markdown body remains required.
- Follow any required confirmation step. Do not invent an email API, SMTP
  command, or delivery result when no connector is available.

If the user asked for email and no connector is available, state that the
newsletter was saved and validated but was **not sent**, and name the reason; do
not claim delivery. If the connector reports a send error, preserve the saved
newsletter, report the error, and do not claim delivery. Report delivery status
separately from the cleanup result and the saved-file link.

## Verify before publishing

- Coverage dates and timezone are explicit.
- Every selected underlying event and gating activity is exactly dated inside
  the window and supported by an opened eligible source.
- No government-operated or state-controlled source supports any claim.
- Every government-action story has two qualifying independent confirmations.
- AI Tools, Other AI Stories, AI at Work, and follow-up manifests are separate;
  no event appears in more than one.
- `AI Tools` contains five to seven items, `Other AI Stories` three to five, and
  `AI at Work` two to four, unless fewer pass. The counts are independent;
  follow-ups are uncapped and do not affect any of them.
- Every `AI at Work` item names one organization, one stance, and an employee
  scope, and no public employer's stance rests on fewer than two qualifying
  independent non-government sources.
- Helper validation reports `"contract": "current"`; an older contract label
  means a required story section is missing.
- Every new story has one unique anchor and one unchecked interest checkbox.
- Every active mark appears in `Tracked Interests` with an original link,
  status, uncheck instruction, and overdue reminder when applicable.
- Every English-origin body sentence has one immediate Simplified Chinese pair.
- Every technical term inside a Simplified Chinese translation stayed in English.
- Chinese-origin text and unchanged source names and URLs are not redundantly
  translated.
- The ledger, query audit, manifests, story blocks, and compact source list
  reconcile one-for-one on headline, exact date, and primary URL.
- Every `Watch Next Week` implication uses an already-cited source.
- The saved file passes helper validation, and any inline copy the user asked for
  matches it.
- Independent lookups ran in parallel batches, and no email was composed or sent
  unless the user asked for one.

If a date, source independence, or material claim cannot be verified, state the
limitation precisely or omit the story.

## Common mistakes

| Mistake | Correction |
|---|---|
| Treating a regulator page as authoritative evidence | Government-operated sources are excluded; use qualifying independent evidence. |
| Treating a consumer AI app as an AI Tool | Require a direct use in building, integrating, deploying, evaluating, or operating AI agents. |
| Letting one selection reduce another | Select five to seven AI Tools, three to five Other AI Stories, and two to four AI at Work items independently of follow-ups. |
| Filing an employer's AI stance under business and industry | Employee AI-use stances belong in `AI at Work`, one organization and one stance per story. |
| Treating a survey of employers as an AI at Work story | Require a named organization changing its own employees' AI use inside the window. |
| Reading a vendor's adoption case study as a stance change | Vendor-authored adoption marketing is excluded; use the employer's own memo or independent reporting. |
| Dropping a mark when no update exists | Keep it in `Tracked Interests` with the exact no-update status. |
| Copying a checkbox into a follow-up | Only the original new-story block owns the checkbox. |
| Deleting an old marked edition | Preserve it and remind the user to review the mark. |
| Using an article's date for an older event | Verify and use the underlying event date. |
| Adding weak Chinese coverage for symmetry | Keep only sources that improve evidence or context. |
| Rendering a technical term in Chinese, such as `提示注入` for `prompt injection` | Keep the English term inside the Chinese sentence and inflect the Chinese around it. |
| Returning only a saved path | Return the clickable path plus the cleanup result and a headline-and-date digest. |
| Pasting the whole edition inline unasked | The link is the deliverable; paste the full Markdown only on request, once. |
| Running independent searches one at a time | Batch mark queries, bucket queries, and feed sweeps concurrently; only source checks and scoring serialize. |
| Opening a page to learn a date the snippet already ruled out | Screen on the snippet or URL date first and record a snippet-level rejection. |
| Trusting an aggregator's date or attribution | Re-derive both from the primary source; aggregators are discovery aids. |
| Emailing the edition by default | Email is opt-in; send only when this run's request asks for it. |
| Composing an email body before checking the connector | Confirm the connector exists, then compose. |
