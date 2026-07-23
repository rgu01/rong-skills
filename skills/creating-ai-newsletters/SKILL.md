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
3. Build a private candidate ledger with event, origin language, underlying event date, bucket, primary source, useful secondary source, duplicate group, conflicts, and scores.
4. Open every source used. Prefer original announcements, papers, repositories, filings, laboratories, regulators for English-language material, official company or laboratory channels for Chinese-language material, and established institutional, technology, or business reporting.
5. Seek strong coverage in both languages when available. Never add a weak source for symmetry.

The underlying event or announcement date controls eligibility. An article published inside the window about an older event is ineligible.

## Select

Reject candidates that are outside the window, inaccessible at the material-claim level, primarily promotional, or duplicates of a stronger entry.

Score each remaining candidate from 0 to 2 on:

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Recency | outside window; reject | first four dates | latest three dates |
| Impact | narrow update | meaningful sector effect | major technical, market, or policy effect |
| Credibility | unsupported; reject | reputable secondary evidence | direct authoritative evidence |
| Mixed-audience relevance | little value | business or technical value | clear value to both |

Rank by total score, then apply editorial judgment and reasonable bucket balance. Merge coverage of one event into one story. Select five to seven; use fewer if fewer meet the standard.

## Write

Read `references/newsletter-template.md` before drafting and follow its order exactly.

Determine origin language from the strongest primary source:

- English-origin story: write each body sentence in English, followed immediately on the next line by exactly one faithful Simplified Chinese translation.
- Chinese-origin story: write its headline, story labels, and body in Chinese only; do not back-translate them into English.
- Write each newsletter-level heading once in its authored language. Keep each story headline in the strongest primary source's language.
- Keep source names and URLs unchanged, and show each link once.

Translations must preserve names, model identifiers, numbers, dates, benchmark values, technical terms, confidence, and caveats. Do not add a claim to only one language.

## Verify before publishing

- Coverage dates and timezone are explicit.
- Every underlying event date is inside the window.
- Every material claim is supported by an opened citation.
- Original sources lead; secondary sources are clearly contextual.
- Duplicate events are merged and credible conflicts remain explicit.
- The edition is brief, balanced, and free of unsupported superlatives.
- Every English-origin body sentence has one immediate Simplified Chinese pair.
- Chinese-origin text, headings, headlines, source names, and URLs are not redundantly translated.
- Source-list links carry `[EN]` or `[中文]`.

If a date or material claim cannot be verified, or credible sources conflict irreconcilably, state the limitation precisely or omit the story.

## Common mistakes

| Mistake | Correction |
|---|---|
| Using an article's date for an older announcement | Verify and use the underlying event date. |
| Treating several reports as several stories | Merge them under the strongest primary source. |
| Adding weak Chinese coverage for symmetry | Keep only sources that improve evidence or context. |
| Translating a Chinese-origin story into English | Keep its headline and body Chinese-only. |
| Counting a translation as a new claim | Keep each language pair semantically identical. |
