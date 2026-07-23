# AI News Newsletter Skill Design

## Purpose

Create a reusable Codex skill that researches the latest artificial intelligence news and produces a brief, polished Markdown newsletter for a mixed business and technical audience.

The default edition covers the publication date and the six preceding calendar dates in the user's timezone, contains five to seven strong stories, uses a sharp professional voice, and pairs every English body sentence with an immediate Simplified Chinese translation. Newsletter and story headings remain in English.

## Skill Shape

Use a tool-independent workflow skill with a separate newsletter template:

```text
creating-ai-newsletters/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    └── newsletter-template.md
```

`SKILL.md` defines the research, verification, ranking, translation, and quality-control workflow. `references/newsletter-template.md` defines the exact Markdown output contract. No feed-collection script is included because search tools and network access vary between agents. The prescriptive workflow and template are designed to remain usable by less capable agents.

## Research Scope

Search the publication date and the six preceding calendar dates in both English and Chinese across four coverage buckets:

1. Models and research
2. Products and tools
3. Business and industry
4. Policy and safety

Treat the date of the underlying event or announcement as the relevant date, not merely the publication date of an article discussing an older event.

Prefer authoritative sources in their original language:

- English sources: official company or laboratory announcements, research papers, repositories, regulators, filings, and established technology or business reporting.
- Chinese sources: official company or research-laboratory channels, government or regulator publications, major institutional media, and established technology or business publications.

For each major story, seek strong English and Chinese coverage when available. Never include a weak source merely to create language symmetry. Use the original announcement, paper, filing, or official publication as primary evidence; use high-quality secondary reporting for confirmation, context, or an independent regional perspective.

## Candidate Selection

A candidate story qualifies only when:

- The underlying event falls inside the seven-day window.
- Its material claims can be traced to an accessible direct source.
- It has meaningful technical or business impact.
- It is not primarily promotional or duplicative.
- Its importance is sufficient for a brief mixed-audience edition.

Score qualifying candidates on recency, impact, source credibility, and relevance to a mixed audience. Rank the candidates and select the best five to seven while maintaining reasonable balance across the four coverage buckets. Editorial importance takes precedence over artificial category quotas.

If fewer than five stories meet the quality threshold, publish a shorter edition rather than lowering the standard.

## Newsletter Contract

Produce polished Markdown in this order:

1. English title and exact seven-day coverage period
2. Two-sentence executive briefing
3. Five to seven ranked stories
4. A short `Watch Next Week` section
5. A compact source list

Each story contains:

- An English-only headline
- What happened
- Why it matters to business and/or technical readers
- A primary-source link and, only when useful, a secondary-source link

Every English body sentence is followed on the next line by exactly one Simplified Chinese translation. Do not translate the newsletter title, section headings, story headlines, source names, or URLs. Show each link once rather than duplicating it in the translation.

The source list labels links with `[EN]` or `[中文]`.

## Translation Rules

The Simplified Chinese sentence must preserve the English sentence's meaning, confidence, and emphasis. Preserve names, product and model identifiers, numbers, dates, benchmark values, and technical terminology accurately. Use established Chinese technical terms where they exist; retain the English term when translation would introduce ambiguity.

The English and Chinese sentences form a semantic pair. Do not add claims, interpretation, or caveats to only one language.

## Reliability and Error Handling

Before publishing:

- Confirm the coverage period and underlying event date for every story.
- Open cited pages and verify that each citation supports its associated claim.
- Prefer original sources and identify secondary reporting clearly.
- Remove duplicate events and unsupported superlatives.
- Check the edition for appropriate business and technical balance.
- Verify that every English body sentence has exactly one immediate Simplified Chinese translation.
- Confirm that headings, headlines, source names, and URLs remain untranslated.
- Check names, numbers, benchmarks, and uncertainty across both languages.
- Tighten the prose until the edition remains brief and sharp.

If a source is inaccessible, the event date cannot be established, or credible sources conflict, either state the limitation precisely or omit the story. Do not merge conflicting reports into an unsupported fact.

## Validation Strategy

Validate the skill structurally with the standard skill validator and behaviorally with realistic forward tests. Tests cover:

- A normal week with abundant news
- A sparse week with fewer than five qualifying stories
- Multiple articles covering the same underlying event
- Conflicting credible sources
- A strong English source with no worthwhile Chinese-language counterpart
- Sentence-pair formatting and translation fidelity
- Use by a less capable agent

Run a baseline task without the skill before authoring it, then repeat the task with the completed skill. The completed skill succeeds when the agent follows the date window, selects credible non-duplicative stories, produces the prescribed brief Markdown structure, and maintains correct English–Simplified Chinese sentence pairs.

## Out of Scope

- Automated email delivery or mailing-list management
- Scheduled execution
- RSS aggregation or persistent source databases
- HTML output
- A hardcoded whitelist of publications
- Guaranteed equal representation of all four coverage buckets or both source languages
