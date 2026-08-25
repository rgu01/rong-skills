# Writing style

Every rule below applies to the whole edition. `newsletter_state.py validate`
enforces the countable ones and fails the edition on a breach; hold the rest
yourself.

## STE

Write every sentence in ASD-STE100 Simplified Technical English, with one
deliberate deviation: the sentence cap is relaxed from the specification's ~25
descriptive words to 40. Follow the STE writing rules and skip its ~900-word
approved dictionary, which would ban the subject matter — `orchestration`,
`observability`, `inference`, `checkpoint` and their neighbours all stay.

- One idea per sentence. A sentence covering two companies is two sentences.
- Active voice: `Anthropic shipped Skills`, not `Skills were shipped`.
- Plain verbs over nominalizations: `decided`, not `made a determination`;
  `chose`, not `carried out a selection`.
- Keep articles, relative pronouns, and auxiliaries. Shorten by cutting ideas,
  never by cutting grammar.
- Give each ordinary word one meaning across the edition.
- State a term the same way on its second appearance as on its first.

## Countable caps

| Rule | Limit | Scope |
|---|---|---|
| English sentence | 40 words | every sentence |
| English average | below 25 words | whole edition |
| Chinese sentence | 60 characters | every sentence |
| Sentences per paragraph | 6 | counted per language |
| English↔Chinese sentences | equal counts | each translated pair |

Scope covers story bodies, the executive brief, story headlines,
`Watch Next Week`, and `Tracked Interests`. Two exemptions: the `#` edition
title, which carries the voice, and the `## Sources` list.

## Chinese

Write Chinese a Chinese technical reader would write, not English wearing
Chinese characters.

- One Chinese sentence per English sentence, in the same order.
- Plain modern prose. Leave out 成语 and literary idiom.
- Split a long English sentence before translating it, rather than growing one
  Chinese sentence past 60 characters.

### Names stay English, vocabulary translates

Two tiers, and only two.

**Names stay English.** Proper nouns, product names, protocol and standard
names, file and API identifiers: `MCP`, `A2A`, `AGENTS.md`, `OAuth`, `eBPF`,
`gVisor`, `Managed Agents`, `Agent Skills`, `Claude Code`. Keep the source
capitalization, inflect the Chinese around the term, and leave it unglossed.

**Vocabulary translates.** A common technical word with a settled Chinese
equivalent takes that equivalent:

| English | Chinese |
|---|---|
| agent | 智能体 |
| prompt | 提示词 |
| prompt injection | 提示注入 |
| memory | 内存 |
| allowlist | 白名单 |
| sandbox | 沙箱 |
| context window | 上下文窗口 |
| embedding | 嵌入 |
| inference | 推理 |
| fine-tuning | 微调 |
| guardrail | 护栏 |
| observability | 可观测性 |
| runtime | 运行时 |
| benchmark | 基准测试 |
| checkpoint | 检查点 |

`token` stays English as a unit of measure: `每个 agent 的 token 支出`.

Write `Managed Agents 的白名单`, not `Managed Agents 的 allowlist`. Write
`智能体沙箱`, not `agent sandbox`. Treat a term the same way everywhere in an
edition and across editions.

## Origin language

Determine origin from the strongest eligible primary source. When an eligible
authoritative source offers parallel versions, use the original announcement
language.

- **English-origin story:** write each body sentence in English, followed
  immediately on the next line by exactly one faithful Simplified Chinese
  translation.
- **Chinese-origin story:** write its headline, labels, and body in Chinese
  only.

Keep newsletter-level headings exactly as the template specifies, and every
story headline in its primary source's language. Keep source names and URLs
unchanged. Show each selected primary URL once in its story and once in the
compact source list.

Translations preserve names, identifiers, numbers, dates, benchmarks,
confidence, and caveats. Every claim appears in both languages, or in neither.
