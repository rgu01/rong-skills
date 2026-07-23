# Newsletter template

Use the structure below; replace instructional braces and omit unused secondary links.

```markdown
# {One English or Chinese newsletter title}

**Coverage:** {YYYY-MM-DD}–{YYYY-MM-DD} ({timezone})

## {Executive Brief heading in the newsletter's authored language}

{First source-grounded briefing sentence in its origin language.}
{If English-origin: its Simplified Chinese translation. If Chinese-origin: omit this line.}

{Second source-grounded briefing sentence in its origin language.}
{If English-origin: its Simplified Chinese translation. If Chinese-origin: omit this line.}

## 1. {Headline in the strongest primary source's language}

**{What happened label in the story's origin language}**

{For English origin: one English sentence.}
{Its Simplified Chinese translation.}

{For Chinese origin: one Chinese sentence only.}

**{Why it matters label in the story's origin language}**

{For English origin: one English sentence.}
{Its Simplified Chinese translation.}

{For Chinese origin: one Chinese sentence only.}

**{Sources label in the story's origin language}:** [Primary source]({url}) · [Secondary context]({url})

{Repeat the story block for each selected story.}

## {Watch Next Week heading in the newsletter's authored language}

{English-origin sentence.}
{Immediate Simplified Chinese translation.}

{Or one Chinese-origin sentence without translation.}

## {Sources heading in the newsletter's authored language}

- [EN] [Source name]({url})
- [中文] [来源名称]({url})
```

## Contract

- Return the completed Markdown newsletter inline as the entire response; do not substitute a file link, completion note, or artifact list.
- Choose one authored language for newsletter-level headings, keep it consistent, and write each heading once.
- Keep every story headline in its strongest primary source's language.
- Write each story's labels in that story's origin language.
- Pair prose by origin language, not by the language of a secondary article.
- Put each Simplified Chinese translation on the line immediately after its English sentence.
- Do not repeat a link in a translation.
- Render each source as one standard `[name](URL)` Markdown link; never nest link syntax.
- Put clickable links on every story-level source line; the final source list does not replace them.
- Keep the executive brief to two source-grounded sentences.
- Include five to seven story blocks unless fewer candidates qualify.
- If publishing fewer than five stories, state in the executive brief that only that number met the date-and-evidence standard.
- Keep `Watch Next Week` short and evidence-based; do not turn speculation into fact.
