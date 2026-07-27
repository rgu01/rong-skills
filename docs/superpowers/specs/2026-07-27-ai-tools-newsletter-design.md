# AI Tools–First Newsletter Design

## Goal

Refocus every generated AI newsletter on tools that help practitioners build,
use, integrate, deploy, evaluate, observe, secure, govern, or manage AI agents.
Preserve a smaller selection of the broader AI coverage already produced by the
skill.

## Editorial Mix

Every edition contains two independent story selections:

1. `AI Tools`: five to seven qualifying stories.
2. `Other AI Stories`: three to five qualifying stories selected under the
   existing general AI-news criteria.

The two counts are independent. A shortage in one section does not increase or
reduce the other section. Publish fewer items in a section only when fewer
candidates pass the existing date, evidence, source-quality, and language
rules.

`AI Tools` appears before `Other AI Stories` because agent tooling is the
newsletter's primary editorial focus.

## AI Tools Scope

An AI-tools story concerns developer- or operator-facing software that
materially supports at least one stage of an AI agent's lifecycle:

- construction: frameworks, SDKs, agent builders, workflow composition, and
  multi-agent orchestration;
- integration: tool calling, MCP, A2A, connectors, data access, memory, and
  reusable skills;
- execution and deployment: runtimes, sandboxes, durable execution,
  checkpointing, scaling, and human approval;
- operations: registries, versioning, permissions, identity, cost control,
  security, governance, and lifecycle management;
- quality: tracing, debugging, observability, evaluation, testing, monitoring,
  and feedback pipelines.

Model releases without agent-development capabilities, consumer AI
applications, generic developer tools without a direct agent-workflow use, and
minor features marketed as agentic do not qualify.

A story must cover a meaningful launch, release, material update, or ecosystem
change inside the coverage window. Merely discovering an existing tool is not a
new story.

## Research and Selection

Research AI tools as a first-class discovery bucket in both English and
Simplified Chinese. Maintain separate candidate ledgers and frozen manifests
for AI Tools and Other AI Stories.

Apply the skill's existing event-date gate, source eligibility, bilingual
writing, scoring, deduplication, and evidence standards to both selections.
When one event could fit either section, place it in `AI Tools` if its material
impact is primarily on agent builders or operators. Never publish the same
event in both sections.

Within AI Tools, prefer broadly useful agent lifecycle infrastructure over
narrow end-user features. Rank practical relevance to day-to-day agent work
alongside recency, impact, credibility, and mixed-audience relevance.

## Story Shape and Interest Tracking

Both story sections use the existing anchored story format and `Interesting`
checkbox. This lets the existing follow-up and tracked-interest workflow work
uniformly across agent-tool and broader AI stories.

Each AI Tools item states:

- the exact material event date;
- what shipped or changed;
- which agent-lifecycle problem it addresses;
- why it matters to practitioners;
- eligible primary and optional secondary sources.

Follow-ups remain in the existing follow-up section rather than returning to
either new-story section.

## Template and Compatibility

Replace the current `New Stories` section with two explicit sections in this
order:

1. `AI Tools`
2. `Other AI Stories`

The remaining sections retain their behavior and relative order:

- `Executive Brief`
- `Follow-ups to Interesting Stories`
- `Tracked Interests`
- `Watch Next Week`
- `Sources`

Update the state helper to parse interest checkboxes from both new story
sections. Continue accepting archived editions that use the legacy
`New Stories` section so archive scanning, retention, and existing marked
interests remain intact.

Newly generated editions must use the new two-section contract. Validation
accepts the legacy contract for existing archive files and the new contract for
new editions, but rejects mixed or incomplete contracts.

## Verification

Add tests before implementation that demonstrate:

- a new-format edition exposes marked interests from both story sections;
- a legacy edition remains valid and retains its interests;
- a mixed or incomplete story-section contract is rejected;
- the template and skill require five to seven AI Tools stories and three to
  five Other AI Stories;
- duplicate events cannot be assigned to both selections by the written
  contract.

Run the complete newsletter state and contract test suites, then validate the
skill metadata with the repository's skill validator.

## Non-Goals

- Do not rewrite existing archived newsletters.
- Do not change follow-up, retention, cleanup, translation, sourcing, email, or
  delivery behavior except where section names must be recognized.
- Do not alter unrelated newsletter files already present in the worktree.
