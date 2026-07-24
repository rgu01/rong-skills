---
name: creating-ai-newsletters
description: Use when a user asks for the latest or past week's AI news, an AI roundup or weekly digest, a saved Markdown AI newsletter, or an English and Simplified-Chinese AI news brief for mixed business and technical readers.
---

# Creating AI Newsletters

## Core principle

Research the event, not the headline. Publish fewer stories rather than relax
the date, evidence, source-quality, or language rules. Follow-ups add a separate
view of marked interests; they never displace or weaken new-story coverage.

## Defaults

Unless the user overrides them:

- Audience: mixed business and technical
- Window: publication date plus the six preceding dates in the user's timezone
- New stories: five to seven
- Voice: sharp and professional
- Format: polished Markdown with stable HTML story anchors
- Archive: `knowledge/AI-newsletter/`
- Trash: `knowledge/.AI-newsletter-trash/`
- Email recipient: `ronggufly@gmail.com`

## Preflight: archive and interests

Resolve the repository root and today's date in the user's timezone. The
ordinary output target is
`knowledge/AI-newsletter/YYYY-MM-DD-ai-newsletter.md`. If that target already
exists, stop before research; update or replace it only when the user explicitly
requests that action.

Run from the repository root:

```bash
python3 skills/creating-ai-newsletters/scripts/newsletter_state.py prepare \
  --archive knowledge/AI-newsletter \
  --trash knowledge/.AI-newsletter-trash \
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

### Discover new stories

1. State the exact start date, end date, and timezone.
2. Search in English and Simplified Chinese across:
   - models and research
   - products and tools
   - business and industry
   - policy, safety, and security
3. Build a private candidate ledger with material event, origin language,
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
   Simplified-Chinese query, written in Simplified Chinese, for each of the four
   buckets. Record the exact query, candidates opened, and selection or
   rejection reasons for all eight language-by-bucket audit entries before
   scoring.

Apply this gate to every follow-up and new-story row:

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

Score each eligible new-story candidate from 0 to 2:

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Recency | outside window; reject | first four dates | latest three dates |
| Impact | narrow update | meaningful sector effect | major technical, market, or policy effect |
| Credibility | unsupported; reject | reputable secondary evidence | direct authoritative evidence |
| Mixed-audience relevance | little value | business or technical value | clear value to both |

Rank by score, editorial judgment, and reasonable bucket balance. Merge only
reports about the same event. Select five to seven new stories, or fewer when
fewer meet the standard, independently of the number of follow-ups.

Freeze a new-story manifest containing each selected headline, event, exact
date, primary URL, and `Date gate: PASS`. Reject any new story duplicating a
selected follow-up. A follow-up never appears in `New Stories`.

## Write

Read `references/newsletter-template.md` completely and follow its fixed section
order.

- Give every new story a unique stable HTML anchor immediately before its
  headline and `- [ ] Interesting` immediately below it.
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
python3 skills/creating-ai-newsletters/scripts/newsletter_state.py validate \
  knowledge/AI-newsletter/YYYY-MM-DD-ai-newsletter.md
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
- New and follow-up manifests are separate; no story appears in both.
- `New Stories` contains five to seven items unless fewer pass; follow-ups are
  uncapped and do not affect that count.
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
| Letting marked stories reduce new coverage | Keep follow-ups in their own uncapped section and still select five to seven new stories. |
| Dropping a mark when no update exists | Keep it in `Tracked Interests` with the exact no-update status. |
| Copying a checkbox into a follow-up | Only the original new-story block owns the checkbox. |
| Deleting an old marked edition | Preserve it and remind the user to review the mark. |
| Using an article's date for an older event | Verify and use the underlying event date. |
| Adding weak Chinese coverage for symmetry | Keep only sources that improve evidence or context. |
| Returning only a saved path | Return the clickable path and the complete saved Markdown. |
