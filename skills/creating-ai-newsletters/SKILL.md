---
name: creating-ai-newsletters
description: Use when a user asks for the latest or past week's AI news, an AI roundup or weekly digest, a Markdown AI newsletter, or an English and Simplified-Chinese AI news brief for mixed business and technical readers.
---

# Creating AI Newsletters

## Core principle

Research the event, not the headline. Publish fewer stories rather than relax the date, evidence, source-quality, or language rules.

## Defaults

Unless the user overrides them:

- Audience: mixed business and technical
- Window: publication date plus the six preceding dates in the user's timezone
- Length: five to seven stories
- Voice: sharp and professional
- Format: polished Markdown

## Research

1. State the exact start date, end date, and timezone.
2. Search in English and Chinese across:
   - models and research
   - products and tools
   - business and industry
   - policy, safety, and security
3. Build a private candidate ledger with event, origin language, exact underlying event date or date range, date-evidence source, `Date gate: PASS/REJECT`, bucket, primary source, useful secondary source, duplicate group, conflicts, and scores.
4. Open every source used. For each selected story, cite the exact opened article, announcement, paper, repository release, filing, or regulator page that contains its date evidence and material claims. Category pages, tag or index pages, search-result pages, and homepages are discovery aids, not valid story citations. Prefer original sources for English-language material, official company or laboratory channels for Chinese-language material, and established institutional, technology, or business reporting.
5. Seek strong coverage in both languages when available. Never add a weak source for symmetry.
6. For a default edition, keep a query audit alongside the ledger: record at least one English-language query and one Chinese-language query for each of models and research, products and tools, business and industry, and policy, safety, and security. Do not score or draft until all eight language-by-bucket query-audit entries exist. For every entry, record the candidates opened and their selection or rejection reasons; a combined search counts only when the audit records a separate query and outcome for each bucket. If no Chinese candidate qualifies, record that outcome rather than add a weak source.

Before scoring, apply this eligibility gate to every ledger row:

- Record `Date evidence` as the exact underlying event date or date range, the opened source URL, and the source passage that supports that date.
- Mark `Date gate: PASS` only when a literal ISO-date comparison shows the underlying date or entire range is on or after the coverage start and on or before the coverage end; otherwise mark `REJECT`. Only `PASS` rows may be scored or selected.
- Reject the row if the date evidence is missing, relative-only, or not wholly inside the window. Do this even when rejection leaves fewer than five stories.
- Treat an in-window article or disclosure about an undated or older incident as ineligible; its publication or disclosure date cannot become the incident date.
- A dated partnership or remediation announcement does not make an earlier undated incident eligible. If that incident is the story's material focus, reject the story rather than recast the later response as its underlying event.
- Do not rename a retrospective disclosure as a new publication, lessons, or update event. If its material claims concern an earlier breach, evaluation, failure, pause, or deployment, date that underlying activity or reject it.

The underlying event date controls eligibility. Use an announcement date only when the announcement itself creates the event, such as launching a model, product, policy, or programme; never use it when a source discloses, reports, or describes an earlier incident. An article published inside the window about an older event is ineligible.

## Select

Reject candidates that are outside the window, inaccessible at the material-claim level, primarily promotional, or duplicates of a stronger entry.

Score each remaining candidate from 0 to 2 on:

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Recency | outside window; reject | first four dates | latest three dates |
| Impact | narrow update | meaningful sector effect | major technical, market, or policy effect |
| Credibility | unsupported; reject | reputable secondary evidence | direct authoritative evidence |
| Mixed-audience relevance | little value | business or technical value | clear value to both |

Rank by total score, then apply editorial judgment and reasonable bucket balance. Merge only reports about the same underlying event; keep related but distinct events separate, and never let an eligible event lend its date or evidence to an ineligible one. Select five to seven; use fewer if fewer meet the standard.

## Write

Read `references/newsletter-template.md` before drafting and follow its order exactly.

Determine origin language from the strongest primary source:

- When an authoritative source offers parallel language versions, use and cite the original announcement language rather than a translated edition to determine origin. For an event from a Chinese institution, an English translation or mirror cannot establish English origin; open the original Chinese announcement when available.
- English-origin story: write each body sentence in English, followed immediately on the next line by exactly one faithful Simplified Chinese translation.
- Chinese-origin story: write its headline, story labels, and body in Chinese only; do not back-translate them into English.
- Write each newsletter-level heading once in its authored language. Keep each story headline in the strongest primary source's language.
- Keep source names and URLs unchanged, and show each link once.

Translations must preserve names, model identifiers, numbers, dates, benchmark values, technical terms, confidence, and caveats. Do not add a claim to only one language.

## Verify before publishing

- Coverage dates and timezone are explicit.
- Every underlying event date is inside the window.
- Every story's `What happened` text states its exact underlying event date or date range.
- For every selected story, the cited primary page states the exact date or date range of its material underlying activity; a retrospective page's publication date alone cannot satisfy this check.
- Every selected incident story states its exact underlying event date or date range; a disclosure date alone is insufficient.
- Every selected story cites an exact opened primary page containing its date evidence and material claims; no category, tag, index, search-result, or homepage URL supports a story.
- Original sources lead; secondary sources are clearly contextual.
- Duplicate events are merged and credible conflicts remain explicit.
- The edition is brief, balanced, and free of unsupported superlatives.
- Every English-origin body sentence has one immediate Simplified Chinese pair.
- Chinese-origin text, headings, headlines, source names, and URLs are not redundantly translated.
- Source-list links carry `[EN]` or `[中文]`.
- The compact source list includes every selected story's exact primary link.

If a date or material claim cannot be verified, or credible sources conflict irreconcilably, state the limitation precisely or omit the story.

## Common mistakes

| Mistake | Correction |
|---|---|
| Using an article's date for an older announcement | Verify and use the underlying event date. |
| Treating several reports as several stories | Merge them under the strongest primary source. |
| Adding weak Chinese coverage for symmetry | Keep only sources that improve evidence or context. |
| Translating a Chinese-origin story into English | Keep its headline and body Chinese-only. |
| Counting a translation as a new claim | Keep each language pair semantically identical. |
