---
name: creating-ai-newsletters
description: Use when a user asks for the latest or past week's AI news, an AI roundup or weekly digest, a saved Markdown AI newsletter, or an English and Simplified-Chinese AI news brief for mixed business and technical readers.
---

# Creating AI Newsletters

## Reader

The reader is an embedded software developer who works in C/C++, RTOS, and
firmware. The reader integrates AI agents into development CI/CD pipelines. The
reader wants methods that make AI output safe, secure, and correct, such as
formal methods.

A typical problem: an AI misreads a natural-language requirement and makes wrong
or useless artefacts. A formal specification, for example a temporal-logic
requirement that a tool such as SpecForge/Lilo or FRET checks, makes the
requirement unambiguous and checkable. Judge every candidate by its value to
this reader.

## Core principle

Research the event, not the headline. Publish fewer stories rather than relax
the date, evidence, source-quality, or language rules. Explain what each change
can and cannot do for embedded software development, especially the path from
requirements through generated code to independent verification.

Rank news in this order of editorial priority:

1. AI agents in coding and in the development pipeline.
2. Correctness, safety, and security of AI output.
3. Coding-model progress with measured evidence.
4. Everything else. Include it only when it is strong, and keep it short.

Track separately how employers govern their own employees' AI use. Follow-ups
add a separate view of marked interests; they never displace or weaken
new-story selection. One organization can be watched by name, but only outside
the committed edition.

## Defaults

Unless the user overrides them:

- Audience: the reader described in `Reader`; keep business news short
- Window: publication date plus the six preceding dates in the user's timezone
- AI Tools: five to seven
- Correctness and Formal Methods: one to four; omit the heading when none qualify
- Other AI Stories: three to five
- Diversity cap: two stories at most from one organization in the edition
- AI at Work: every qualifying story; omit the heading when none qualify
- Employer watch: on only when a local watchlist exists, and local-only always;
  see `references/employer-watch.md`
- Voice: sharp and professional, inside the ASD-STE100 rules in
  `references/writing-style.md`
- Format: polished Markdown with stable HTML story anchors
- Archive: `<rong-skills-repo>/knowledge/ai/AI-newsletter/`
- Trash: `<rong-skills-repo>/knowledge/ai/.AI-newsletter-trash/`
- Employer watch (gitignored): `<rong-skills-repo>/knowledge/ai/.employer-watch/`
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
entries older than 30 days, and splits every `[x] Interesting` record into an
`interests` list and an `expired` list. It preserves every edition that carries
a mark. Report each moved path, purged path, and expired mark in the final
response.

A mark expires one calendar month after the edition that carried it, whatever
the run frequency. Expiry is absolute: a qualifying follow-up reports the update
and never restarts the clock. Research the `interests` records only. Name each
`expired` record in the final response and leave its checkbox untouched, so
re-marking the original story stays a one-line edit.

A nonzero exit or any returned error blocks generation. Never work around a
malformed edition, symlink, cleanup collision, or incomplete interest scan.

Then check for the optional local watchlist:

```bash
cat "$REPO_ROOT/knowledge/ai/.employer-watch/watchlist.local.md" 2>/dev/null
```

A watchlist turns on the employer watch described in
`references/employer-watch.md`. Read that reference before running its queries.
No watchlist means the track is off for this run: run no employer queries, write
no local edition, and report one line saying the watch was skipped. A missing
watchlist is normal and never blocks generation.
Never send watchlist terms, aliases, domains, or work context to a public search
tool or third-party service. If no approved private research channel is
available, skip this optional track, write no local edition, and report that it
was skipped for privacy; continue the public edition.

## Evidence

Read `references/evidence-rules.md` before screening the first candidate. It
owns source eligibility, the date gate, and the scoring table.

Two rules decide most rejections. Government-operated and state-controlled
sources are ineligible in every language. The underlying event date, not the
publication date, must fall wholly inside the window.

## Research

### Cover the standing topics

Every edition runs a dedicated query for each standing topic below, in English
and Simplified Chinese, batched with the mark and bucket queries. A standing
topic earns its place under the same date, evidence, and source rules as any
other story. Name each standing topic that found nothing in the final response.

- **AI and formal methods** — AI-assisted formal specification and
  verification, translating natural-language requirements into checkable
  properties, model checking state machines and timing behavior, proof-guided
  code generation, and checking generated C/C++ against its specification.
  Track whether the generated specification actually preserves the original
  requirement; a successful model check cannot establish that by itself.
- **Post-training** — reinforcement learning from verifiable rewards, agentic
  and tool-use RL, distillation, and post-training-only releases. Compare
  whether gains come from a changed base model, post-training, inference, or
  agent scaffolding; do not present a benchmark as a firmware guarantee.
- **Embedded AI coding** — in-window releases for generating or reviewing
  firmware, drivers, RTOS code, and tests; compiler and static-analysis
  integration; hardware-in-the-loop tests; code-size, memory, timing, and
  safety checks. Keep on-device AI inference separate from AI that writes
  embedded software.

This list is the only home for standing topics. Add one here rather than in a
napkin entry or a memory note.

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

Qualifying tools help developers use AI agents to write, review, test, and ship
code. Cover coding agents and the development pipeline:

- coding agents, agentic code review, test generation, and pull-request
  automation;
- agents that run headless in CI/CD (GitHub Actions, GitLab CI, Jenkins,
  Bitbucket Pipelines);
- agent permissions, sandboxes, and approval steps in CI;
- secrets and supply-chain risk of agents in a pipeline;
- cost and reliability of agents in a pipeline;
- requirement-to-test, code-generation, compiler-feedback, static-analysis, and
  hardware-in-the-loop workflows for embedded C/C++ and RTOS projects.

General agent infrastructure without a direct coding or pipeline use does not
qualify. Examples: web search APIs, payment rails, publisher pay-per-crawl,
generic model routers, and consumer assistants. Such an item can go to Other AI
Stories only when its impact is major.

A meaningful launch, release, material update, or ecosystem change must occur
inside the coverage window. Exclude model releases without agent-development
capabilities from this section; cover them under models and research instead.
Exclude minor features marketed as agentic and the mere rediscovery of an
existing tool. Put a formal-methods tool release in `Correctness and Formal
Methods`, not here. An event lands in exactly one section.

Sweep the dated vendor feeds first, then use open search to fill the gaps. A feed
is a screening aid. Its date helps screen candidates, but a feed date alone never
passes the underlying event date gate. A busy feed never raises the diversity cap
for its organization.

- `claude.com/blog`, `platform.claude.com/docs` changelogs, and the Claude Code
  changelog
- OpenAI Codex changelog and Cursor changelog
- `github.blog/changelog` (Copilot coding agent, Actions)
- GitLab releases and blog (Duo)
- JetBrains AI blog
- `aws.amazon.com/about-aws/whats-new`, the AgentCore release notes, and Kiro
- `langchain.com/blog` and the LangSmith changelog
- `devblogs.microsoft.com/agent-framework`, `developers.googleblog.com`
- GitHub releases pages for tools already covered

### Discover Correctness and Formal Methods

This section serves the standing topic "AI and formal methods" and the AI safety,
security, and correctness work of editorial priority 2. Qualifying items:

- formal specification and verification with AI;
- translation of natural-language requirements into formal properties, and the
  fidelity of that translation;
- detection of ambiguity in requirements;
- verified or proof-carrying code generation;
- static analysis and model checking of generated code;
- test oracles and evaluation of correctness;
- prompt-injection and agent-security work.

Look for the NL-requirement-misread problem: an AI reads a requirement in a
wrong way and builds wrong artefacts. Check requirement fidelity in every item.
A checker proves a property only. It does not prove that the property captured
the intent of the natural-language requirement.

Sweep these feeds for candidates, then use open search:

- arXiv cs.SE and cs.LO listings
- AWS Automated Reasoning blog and Kiro
- Galois blog and Imiron/SpecForge news
- NASA FRET releases on GitHub
- Frama-C, CBMC, and Kani release pages

The same date, evidence, and source rules apply. A formal-methods tool release
goes in this section, not in AI Tools.

Aggregator digests and weekly-roundup sites are discovery aids only. Their dates
and attributions have proven unreliable — a hobby project reported as a
university study, a June government directive listed under an August date — so
re-derive every event and date from the primary source before scoring.

### Discover Other AI Stories

Preserve the existing broader AI coverage across:

- models and research: coding and reasoning ability, post-training methods,
  cost per completed task, inference efficiency, context and tool use,
  evaluation design, and reported failure modes;
- non-agent products
- business and industry
- policy, safety, and security

Search model-maker announcements, model cards, technical reports, and
independent evaluations, not only agent-vendor feeds. Compare a new model with
its predecessor using a named task, metric, setting, and price when the source
provides them. Label vendor measurements as such. Do not infer that a general
coding score demonstrates correct interrupt behavior, bounded latency,
resource limits, or conformance to a firmware requirement.

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

### Watch one organization, locally

This track exists only when the preflight found a watchlist. It reports the AI
news about one named organization, usually the reader's employer.

It is not a standing topic and it never reaches the committed edition. This
repository forbids employer information, and the archive under
`knowledge/ai/AI-newsletter/` is committed and public, so an employer-watch
story is written to the gitignored
`$REPO_ROOT/knowledge/ai/.employer-watch/YYYY-MM-DD-employer-watch.local.md`
instead. Genericizing the name does not make such a story publishable, because
the cited URLs, source names, and article titles still carry it.

`references/employer-watch.md` owns the watchlist format, the query shapes, the
two extra rejections — name collision and AI-as-decoration — the local edition
format, and the leakage guard. The window, date gate, source eligibility, and
independence rules are the same ones the edition uses.

Only if a private research channel is available, issue these queries inside
the same parallel batches as the mark, bucket, and vendor-feed queries.
The employer watch has no item count and never changes the
`AI Tools`, `Other AI Stories`, or `AI at Work` counts.

### Research every selection

Run this work in parallel batches. Every mark query, every language-by-bucket
query, and every vendor-feed sweep is independent of the others, so issue them as
concurrent groups in one step and wait once, rather than one call at a time. Only
two points genuinely serialize: a candidate's primary-source check depends on
that candidate existing, and scoring depends on the ledgers being complete.
Serial execution of independent lookups has been the single largest cost in past
editions.

1. State the exact start date, end date, and timezone.
2. Search in English and Simplified Chinese for AI Tools, for Correctness and
   Formal Methods, for each of the four Other AI Stories buckets, and for AI at
   Work.
   Run dedicated queries in both languages for embedded-code generation and
   for requirement formalization plus machine-checked verification. Search
   model-development sources separately from agent tooling.
3. Build separate private candidate ledgers for AI Tools, Correctness and
   Formal Methods, Other AI Stories, and AI at Work. Each row records the
   material event, origin language, exact underlying event date or date range,
   date-evidence source, gating earlier material activity and its exact date
   evidence or `N/A`, optional non-gating background, source-operator class, `Date gate: PASS/REJECT`,
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
   citations. If a primary page is inaccessible at the material-claim level,
   use a dated, opened, reputable independent report that states the claim
   directly, or omit the claim.
6. For a default edition, run at least one English query and one
   Simplified-Chinese query, written in Simplified Chinese, for AI Tools, for
   Correctness and Formal Methods, for each of the four Other AI Stories
   buckets, and for AI at Work. Record the exact query, candidates opened, and
   selection or rejection reasons for all fourteen language-by-bucket audit
   entries before scoring.

Apply the date gate in `references/evidence-rules.md` to every follow-up,
AI Tools, Correctness and Formal Methods, Other AI Stories, and AI at Work row
before scoring it.

## Select

Reject candidates that are outside the window, inaccessible at the
material-claim level, primarily promotional, government-operated, or duplicates
of a stronger entry.

Score and rank the rest with the scoring table in
`references/evidence-rules.md`.
Prefer stories that change the ability to generate, test, or verify real code.
Rank by the editorial priorities in the core principle. Use the "Reader
relevance" score in `references/evidence-rules.md`. Reserve room in Other AI
Stories for meaningful model-development evidence when it qualifies. Do not fill
a quota with generic agent infrastructure or weakly dated papers when stronger
coding-model news exists.

Apply the diversity cap: select at most two stories from one organization in
the whole edition, all new-story sections together. Follow-ups do not count. A
vendor launch week, such as a "birthday week" or a "dev day", does not change the
cap. Pick the two strongest stories for this reader and skip the rest.

Select five to seven AI Tools, one to four Correctness and Formal Methods
stories, and three to five Other AI Stories, or fewer in any section when fewer
meet the standard. Publish every AI at Work story that passes the gate, and omit
that section when none does. Omit the `Correctness and Formal Methods` heading
when none qualifies. The counts are independent and do not change with the
number of follow-ups or with the size of `AI at Work`.

Freeze separate manifests for AI Tools, Correctness and Formal Methods, Other AI
Stories, and AI at Work containing each selected headline, event, exact date,
primary URL, and `Date gate: PASS`. Reject any event duplicating a selected
follow-up or appearing in another manifest. A follow-up never appears in any new-story
section.

## Write

Read `references/newsletter-template.md` completely and follow its fixed section
order.

- Give every story in `AI Tools`, `Correctness and Formal Methods`,
  `Other AI Stories`, and `AI at Work` a unique stable HTML anchor immediately
  before its headline and `- [ ] Interesting` immediately below it.
- For every Correctness and Formal Methods item, state which requirement or
  property the tool checks, which tool or method checks it, what the checker
  proved, and what stays unverified. Say whether the formal property captured the
  intent of the natural-language requirement. Omit the heading when no item
  qualifies.
- For every AI Tools item, identify what shipped, the agent-lifecycle problem
  it addresses, and why it matters to practitioners.
- For relevant tools and models, add an **Embedded-code lens** after
  **Why it matters**. State a concrete potential use (such as driver generation
  or requirement-derived tests) and the independent check still needed
  (compiler, static analysis, property checker, timing test, or hardware test).
  Distinguish a demonstrated capability from a proposed workflow. Do not imply
  that a general coding benchmark certifies safety or requirements conformance.
- Synthesize model, tool, and verification trends in the Executive Brief, in
  two to four sentences. Lead with priority 1 and 2 news (coding agents, the
  development pipeline, and correctness) when it exists. Make its claims
  traceable to selected sources. When the
  formal-methods or embedded-coding query finds no eligible in-window event,
  say so in the final digest rather than inserting an older paper as news.
  If a directly relevant older paper explains a specific verification gap,
  it may appear as dated background inside a selected story's engineering
  lens, with a direct citation and an explicit outside-window label.
- For every AI at Work item, state the organization, the stance as
  `Encouraging`, `Discouraging`, or `Disallowing`, the employee scope, and
  whether the measure is enforced or only recommended. Omit the `AI at Work`
  heading entirely when no candidate qualifies.
- Do not add interest checkboxes to follow-ups or tracked-interest reminders.
- Put qualifying updates only in `Follow-ups to Interesting Stories`.
- List every active mark in `Tracked Interests`, linking to its original
  anchored story. State whether a qualifying update was found. Otherwise write
  `No qualifying update found this week`.
- Give each tracked item the date it was marked and the date it expires. Every
  tracked item tells the user to uncheck the original story to stop tracking it.

Read `references/writing-style.md` completely before writing any prose. It owns
the ASD-STE100 rules, origin-language handling, and the Chinese term tiers.

`newsletter_state.py validate` fails the edition on these caps:

- 40 words maximum per English sentence, averaging under 25 across the edition
- 60 characters maximum per Chinese sentence
- six sentences maximum per paragraph, counted per language
- one Chinese sentence per English sentence in every translated pair

They cover every headline, body sentence, and list item, with two exemptions:
the `#` edition title and the `## Sources` list.

`Watch Next Week` contains only forward-looking implications supported by
sources already cited in a selected new story or follow-up.

## Save and return

For ordinary generation, write the completed edition to a new output target and
never overwrite an existing file. When the user explicitly asks to update or
replace an existing same-day edition, follow that request in place and preserve
any existing interest marks unless the user explicitly changes them. Then run:

```bash
python3 "$REPO_ROOT/skills/ai/creating-ai-newsletters/scripts/newsletter_state.py" validate \
  "$REPO_ROOT/knowledge/ai/AI-newsletter/YYYY-MM-DD-ai-newsletter.md"
```

Validation failure blocks the edition. Readability errors name the offending
sentence: rewrite it and validate again rather than presenting the edition as
complete.

When a watchlist exists, save the local edition to
`$REPO_ROOT/knowledge/ai/.employer-watch/YYYY-MM-DD-employer-watch.local.md`,
then run the leakage guard from `references/employer-watch.md` with the terms
read from the watchlist and expect no output:

```bash
grep -inE "{term}|{alias}|{domain}" \
  "$REPO_ROOT/knowledge/ai/AI-newsletter/YYYY-MM-DD-ai-newsletter.md"
```

Any hit blocks the edition until the organization is removed from it. Do not run
`newsletter_state.py` against the local file, and never commit it or name its
terms in a commit message.

On success, report in this order:

1. The cleanup result, naming every moved or purged path.
2. A clickable link to the saved path.
3. A short digest: the coverage window, the count in each section (including
   Correctness and Formal Methods), every
   selected headline with its exact event date, any section that published
   fewer items than its range with the reason, and any standing topic that
   found nothing.
4. Every mark that expired this run, with the story it came from.
5. The employer watch: skipped for want of a watchlist or a private research
   channel, or the local edition path, its item count, and the leakage-guard
   result. Never restate the
   watchlist terms in a tracked file; the response is the only place they
   belong.
6. Anything else the user must act on, such as a validation warning or an
   unresolved source limitation.

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
- AI Tools, Correctness and Formal Methods, Other AI Stories, AI at Work, and
  follow-up manifests are separate; no event appears in more than one.
- No organization has more than two stories across the new-story sections, even
  in a vendor launch week.
- Every AI Tools item has a direct coding or pipeline use.
- `AI Tools` contains five to seven items and `Other AI Stories` three to five,
  unless fewer pass. `Correctness and Formal Methods` contains one to four
  items, and its heading is absent when none qualifies. `AI at Work` carries
  every qualifying story, and its heading is absent when none qualifies. The
  counts are independent; follow-ups are uncapped and do not affect any of them.
- Every standing topic ran a query in both languages, and any that found
  nothing is named in the final response.
- Every `AI at Work` item names one organization, one stance, and an employee
  scope, and no public employer's stance rests on fewer than two qualifying
  independent non-government sources.
- Helper validation reports `"contract": "current"`; an older contract label
  means a required story section is missing.
- Every Correctness and Formal Methods item states the property checked, the
  tool, what the checker proved, and what stays unverified.
- Every new story has one unique anchor and one unchecked interest checkbox.
- Every active mark appears in `Tracked Interests` with an original link,
  status, uncheck instruction, and its expiry date.
- Every mark that expired this run is named in the final response, and its
  checkbox is untouched.
- Every English-origin body sentence has one immediate Simplified Chinese pair.
- Names stayed English inside Simplified Chinese prose, and common technical
  vocabulary took its settled Chinese equivalent.
- Every sentence obeys the caps, and the edition passes helper validation with
  no readability error.
- Chinese-origin text and unchanged source names and URLs are not redundantly
  translated.
- The ledger, query audit, manifests, story blocks, and compact source list
  reconcile one-for-one on headline, exact date, and primary URL.
- Every `Watch Next Week` implication uses an already-cited source.
- The saved file passes helper validation, and any inline copy the user asked for
  matches it.
- Independent lookups ran in parallel batches, and no email was composed or sent
  unless the user asked for one.
- The employer watch ran only through an approved private channel. If none
  exists, report that it was skipped for privacy. Any watch stories live only
  in the gitignored local edition, and the leakage guard found no watchlist
  term in the saved edition.

If a date, source independence, or material claim cannot be verified, state the
limitation precisely or omit the story.

## Common mistakes

Read `references/common-mistakes.md` when a judgement call feels close, and
after any run that produced a validation error.
