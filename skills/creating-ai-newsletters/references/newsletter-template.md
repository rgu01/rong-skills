# Newsletter template

Use the structure below exactly. Replace every instructional brace. Keep the
English section names unchanged because the state helper uses them as the saved
edition contract.

```markdown
# {Sharp English or Chinese newsletter title}

**Coverage:** {YYYY-MM-DD}–{YYYY-MM-DD} ({timezone})

## Executive Brief

{First source-grounded briefing sentence in its origin language.}
{If English-origin: its faithful Simplified Chinese translation. If Chinese-origin: omit this line.}

{Second source-grounded briefing sentence in its origin language.}
{If English-origin: its faithful Simplified Chinese translation. If Chinese-origin: omit this line.}

## AI Tools

<a id="story-{stable-lowercase-hyphenated-slug}"></a>

### {Headline in the strongest eligible primary source's language}

- [ ] Interesting

**{Underlying event date label in the story's origin language}:** {Exact material event date or date range}

**{What happened label in the story's origin language}**

{For English origin: state what happened and its exact event date in one English sentence.}
{Its immediate Simplified Chinese translation.}

{For Chinese origin: state the date and event in one Chinese sentence only.}

**{Why it matters label in the story's origin language}**

{For English origin: one English sentence explaining which agent-lifecycle problem the tool addresses and why it matters to practitioners.}
{Its immediate Simplified Chinese translation.}

{For Chinese origin: one Chinese sentence explaining which agent-lifecycle problem the tool addresses and why it matters to practitioners.}

**{Sources label in the story's origin language}:** [{Eligible primary source name}]({primary_url}) · [{Optional eligible secondary context name}]({secondary_url})

{Repeat for five to seven independent AI Tools stories, or fewer only when fewer qualify.}

## Other AI Stories

<a id="story-{stable-lowercase-hyphenated-slug}"></a>

### {Headline in the strongest eligible primary source's language}

- [ ] Interesting

**{Underlying event date label in the story's origin language}:** {Exact material event date or date range}

**{What happened label in the story's origin language}**

{For English origin: state what happened and its exact event date in one English sentence.}
{Its immediate Simplified Chinese translation.}

{For Chinese origin: state the date and event in one Chinese sentence only.}

**{Why it matters label in the story's origin language}**

{For English origin: one English sentence.}
{Its immediate Simplified Chinese translation.}

{For Chinese origin: one Chinese sentence only.}

**{Sources label in the story's origin language}:** [{Eligible primary source name}]({primary_url}) · [{Optional eligible secondary context name}]({secondary_url})

{Repeat for three to five independent Other AI Stories, or fewer only when fewer qualify.}

## Follow-ups to Interesting Stories

### {Follow-up headline in its origin language}

**Original interest:** [{Original headline}]({relative_newsletter_path}#{original_anchor})

**{Underlying event date label in the follow-up's origin language}:** {Exact new event date or date range}

**{What changed label in the follow-up's origin language}**

{For English origin: one English sentence describing the meaningful in-window update.}
{Its immediate Simplified Chinese translation.}

{For Chinese origin: one Chinese sentence only.}

**{Why it matters label in the follow-up's origin language}**

{For English origin: one English sentence.}
{Its immediate Simplified Chinese translation.}

{For Chinese origin: one Chinese sentence only.}

**{Sources label in the follow-up's origin language}:** [{Eligible primary source name}]({primary_url}) · [{Optional eligible secondary context name}]({secondary_url})

{Repeat for every marked story with a qualifying update; omit story blocks and state that none qualified when applicable.}

## Tracked Interests

- **[{Original headline}]({relative_newsletter_path}#{original_anchor})** — Marked {original_edition_date}. {`Qualifying follow-up included above` or `No qualifying update found this week`}. {If older than six months: `Review reminder: this interest has been tracked for more than six months.`} Uncheck `Interesting` in the original story to stop tracking it.

{Repeat once for every active mark; state that there are no active interests when the helper returns none.}

## Watch Next Week

{English-origin forward-looking implication supported by a source already cited above.}
{Its immediate Simplified Chinese translation.}

{Or one Chinese-origin supported implication without translation.}

## Sources

- [EN] [Source name]({url})
- [中文] [来源名称]({url})
```

## Contract

- The seven `##` section headings and their order are fixed.
- Every `AI Tools` and `Other AI Stories` block has one unique stable anchor
  immediately before its `###` headline and one `- [ ] Interesting`
  immediately after that headline.
  Blank lines may separate these elements; no other nonblank content may.
- Anchors use lowercase ASCII letters, numbers, and hyphens, begin with a letter
  or number, and remain unchanged when a checkbox is edited.
- The checkbox is manually editable: `[x]` or `[X]` marks the story and `[ ]`
  removes the mark.
- Follow-up and tracked-interest blocks link to the original anchor and never
  contain an interest checkbox.
- `AI Tools` contains five to seven independent stories and `Other AI Stories`
  contains three to five independent stories unless fewer pass the evidence
  gate. These counts are independent, and the follow-up section has no
  numerical limit.
- Never publish the same event in both `AI Tools` and `Other AI Stories`.
- Include every active interest in `Tracked Interests`, even with no update.
- State the exact underlying event date in every new story and follow-up.
- Pair English-origin prose sentence by sentence with immediate faithful
  Simplified Chinese. Keep Chinese-origin story prose Chinese-only.
- Do not repeat links in translations. Render standard `[name](URL)` Markdown.
- Each selected primary URL appears once in its story block and once in the
  compact source list. Tracked-interest relative links are not source links.
- Use only eligible non-government-operated sources. A government-action story
  cites at least two reputable independent non-government sources.
- Keep the executive brief to two source-grounded sentences.
- `Watch Next Week` introduces no new factual claim or source.
- For ordinary generation, save the completed Markdown without overwriting at
  `knowledge/AI-newsletter/YYYY-MM-DD-ai-newsletter.md`, validate it with the
  state helper, and return a clickable path followed by the complete saved
  Markdown inline.
