# Employer watch (local only)

## Why this track is separate

A reader sometimes wants the AI news about one specific organization, usually
their own employer. That coverage cannot go in a published edition of this
repository: `AGENTS.md` forbids any employer information here, and the archive
under `knowledge/ai/AI-newsletter/` is committed and public. Genericizing the
name does not help, because the cited URLs, source names, and article titles
still carry it.

So the employer watch is a parallel, local-only track. It uses the same window,
date gate, and evidence rules as the edition, and it writes to a gitignored
directory that never enters git history.

This track is not a standing topic. A standing topic competes for a place in
`AI Tools` or `Other AI Stories`; an employer-watch story never appears in the
committed edition at all.

## Paths

| Purpose | Path |
| --- | --- |
| Watchlist (input, user-maintained) | `$REPO_ROOT/knowledge/ai/.employer-watch/watchlist.local.md` |
| Local edition (output) | `$REPO_ROOT/knowledge/ai/.employer-watch/YYYY-MM-DD-employer-watch.local.md` |

`knowledge/ai/.employer-watch/` is listed in `.gitignore`. Never move either
file into the archive directory: the state helper rejects any `.md` file there
whose name is not `YYYY-MM-DD-ai-newsletter.md`, and that failure blocks
generation.

Never commit either file, never quote the watchlist terms in a commit message,
and never write them into a tracked file, including `README.md`, `AGENTS.md`,
this reference, or a saved edition.

## Watchlist format

The watchlist is optional. When it is missing or has no `name`, the track is
off: run no employer queries, write no local edition, and report one line
saying the watch was skipped.

```markdown
---
name: {organization name as news sources write it}
aliases: [{legal entity}, {former name}, {common misspelling}]
domains: [{primary web domain}]
brands: [{product, division, or subsidiary name worth its own query}]
languages: [en, zh]
---

{Optional free prose: what the reader cares about, which divisions matter,
which unrelated same-name organizations to reject.}
```

`aliases`, `domains`, `brands`, and the prose are optional. `languages`
defaults to `[en, zh]`.

## Research

Build the query set from `name` plus every alias and brand, crossed with the
AI topics the reader cares about, in each configured language. Issue these
queries inside the same parallel batches as the mark, bucket, and vendor-feed
queries; they are independent of all of them.

Useful query shapes, per name and language:

- the name with `AI`, `artificial intelligence`, `人工智能`, `machine learning`,
  or `automation`
- the name with `agent`, `copilot`, `LLM`, or `generative AI`
- the name with an AI-adjacent business event: partnership, acquisition,
  pilot, deployment, product launch, robotics or vision system
- the name with an employee AI-use stance: policy, guidelines, internal
  assistant, ban, approval — the `AI at Work` vocabulary applied to one
  organization
- `site:{domain}` news and press releases, and the organization's own
  newsroom feed

A story qualifies when the material event names the organization **and** is
about AI, and when it passes the same date gate, source-eligibility, and
independence rules the edition uses. Apply the same rejections: outside the
window, promotional-only, government-operated source, unreachable material
claim.

Two extra rejections belong to this track:

- **Name collision.** An unrelated organization that shares the name is not a
  hit. Confirm the entity from the source, not from the query.
- **AI as decoration.** A press release that mentions AI only as a slogan,
  with no AI event, does not qualify. The reader wants what changed, not that
  the word appeared.

There is no minimum or maximum item count. Publish every qualifying story, and
write the local edition with an explicit "no qualifying story this window" line
when none qualifies. The employer watch never changes the `AI Tools`,
`Other AI Stories`, or `AI at Work` counts.

## Local edition format

Use the writing rules from `writing-style.md` — the same sentence caps, the
same English-to-Simplified-Chinese pairing, the same term tiers. Omit anchors
and `- [ ] Interesting` checkboxes: the state helper only scans the committed
archive, so a mark here would track nothing.

```markdown
# Employer watch — {YYYY-MM-DD}

**Coverage:** {YYYY-MM-DD}–{YYYY-MM-DD} ({timezone})
**Watchlist:** {name and every alias or brand queried}

> Local only. This file is gitignored. Do not copy any part of it into the
> committed newsletter edition.

## Stories

### {Headline in the strongest eligible primary source's language}

**{Underlying event date label}:** {Exact material event date or date range}

**{What happened label}**

{One sentence in the origin language.}
{Its immediate Simplified Chinese translation, for English origin only.}

**{Why it matters label}**

{One sentence in the origin language, on what the event changes for the
reader's own work.}
{Its immediate Simplified Chinese translation, for English origin only.}

**{Sources label}:** [{Primary source name}]({primary_url}) · [{Optional secondary}]({secondary_url})

{Repeat for every qualifying story, or write `No qualifying story this window.`}

## Queries run

- {Exact query} — {candidates opened} — {selection or rejection reason}
```

## Leakage guard

Before saving the committed edition, confirm it names none of the watchlist
terms. Run the check with the terms read from the watchlist, and expect no
output:

```bash
grep -inE "{term}|{alias}|{domain}" \
  "$REPO_ROOT/knowledge/ai/AI-newsletter/YYYY-MM-DD-ai-newsletter.md"
```

Any hit blocks the edition. Two cases produce a hit:

- An employer-watch story reached the committed edition. Remove it, and keep it
  in the local file only.
- A candidate found for `AI Tools`, `Other AI Stories`, or `AI at Work`
  genuinely involves the organization — a vendor announcing a deal with it, for
  example. The committed edition may keep such a story only when it stays
  accurate without naming or linking the organization, which the cited sources
  rarely allow. Otherwise drop it from the edition and record it in the local
  file.

Report the guard result in the final response, together with the local edition
path and its item count.
