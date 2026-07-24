# AI Newsletter Persistence and Interests Design

## Purpose

Extend `creating-ai-newsletters` so editions are saved persistently, users can
mark stories as interesting through Markdown checkboxes, and future editions
research qualifying follow-ups without displacing new-story coverage.

The revision also excludes government-operated sources in both English and
Chinese while retaining independently reported stories about government
actions.

## Source Policy

Government agencies, ministries, regulators, legislatures, courts,
intergovernmental bodies, and state-controlled media are ineligible as cited or
supporting sources in every language.

Public universities and publicly funded research institutions remain eligible.
Independent reporting about government actions remains eligible when:

- the underlying event date is exact and inside the coverage window; and
- at least two reputable, independent, non-government sources confirm the
  material claims.

Company, laboratory, academic, repository, and independent-media sources retain
the existing evidence hierarchy. The four discovery buckets remain models and
research, products and tools, business and industry, and policy, safety, and
security.

## Archive Layout

Saved editions use:

```text
knowledge/AI-newsletter/
└── YYYY-MM-DD-ai-newsletter.md
```

The date is the edition publication date. A normal generation must not overwrite
an existing same-day edition. Updating or replacing an existing edition requires
an explicit user request.

The assistant returns a clickable path to the saved edition and then reproduces
the complete newsletter inline.

## Story Marking

Every story in `New Stories` includes a stable HTML anchor immediately before
its headline and an editable checkbox immediately below the headline:

```markdown
<a id="story-example-headline"></a>

### Example headline

- [ ] Interesting
```

Changing `[ ]` to `[x]` marks the story. Changing `[x]` back to `[ ]` removes
the mark. Anchors are unique within an edition and remain unchanged when a story
is marked or unmarked.

The original checked story block is the authoritative interest record.
Follow-up blocks reference that original story but do not create duplicate
checked records.

## Newsletter Structure

Each edition contains:

1. Title and exact coverage period
2. Executive Brief
3. `New Stories`
4. `Follow-ups to Interesting Stories`
5. `Tracked Interests`
6. `Watch Next Week`
7. Sources

`New Stories` always contains five to seven independently selected new stories,
unless fewer candidates satisfy the existing evidence gate.

`Follow-ups to Interesting Stories` is separate and has no numerical limit. A
marked story receives a follow-up only when a meaningful event occurred inside
the current seven-day window and satisfies the same date, evidence, source, and
language rules as a new story. A follow-up never appears again in `New Stories`.

`Tracked Interests` lists every active mark with:

- the original headline;
- the original newsletter date and a relative link to the anchored story block
  containing its checkbox;
- whether a qualifying follow-up was found in the current edition;
- an overdue-review warning after six months; and
- an instruction to uncheck the original story to stop tracking it.

Marked stories with no qualifying update remain listed with
`No qualifying update found this week`.

## Research Flow

Before general discovery:

1. Scan saved newsletters for checked new-story blocks.
2. Build follow-up queries from each marked story's headline, story content,
   entities, products, and source links.
3. Research all active interests.
4. Freeze qualifying follow-ups in a follow-up manifest.
5. Run the normal bilingual discovery workflow for five to seven new stories.
6. Reject new-story candidates duplicating a selected follow-up.

Follow-up priority never weakens the date or evidence gates.

## State Helper

Add `skills/creating-ai-newsletters/scripts/newsletter_state.py` as a
standard-library-only Python CLI. It provides deterministic operations for:

- scanning newsletter files and returning active interests as JSON;
- associating a checkbox with its story headline, block, sources, and edition
  date;
- identifying overdue marked interests;
- moving expired unmarked editions out of the active archive;
- purging old trash entries;
- validating the filename and checkbox structure of a saved edition.

Markdown newsletters remain the only source of truth. No separate interest
database or generated index is introduced.

## Retention

Before generating an edition:

- move an unmarked newsletter older than six calendar months from
  `knowledge/AI-newsletter/` to the recoverable trash directory
  `knowledge/.AI-newsletter-trash/`;
- preserve any newsletter containing at least one checked story regardless of
  age;
- mark preserved interests older than six months as overdue for review;
- permanently delete newsletter trash entries more than 30 days after their
  trash date.

Trash filenames use
`TRASHED-YYYY-MM-DD--EDITION-YYYY-MM-DD-ai-newsletter.md`, recording both the
trash date and original edition date so cleanup does not depend on filesystem
timestamp behavior. An edition is expired when its edition date is earlier than
the current date minus six calendar months. A trash entry is purgeable when its
recorded trash date is earlier than the current date minus 30 days. Cleanup
targets only regular files matching the applicable active or trash filename
contract and reports every moved or permanently deleted path.

## Failure Handling

- Missing archive directories are created.
- Malformed newsletter filenames or malformed checkbox/story associations are
  reported and left untouched.
- An existing same-day output blocks ordinary save rather than being
  overwritten.
- Cleanup never follows symlinks or deletes unrelated files.
- A marked old newsletter cannot be moved to trash.
- Failure to scan interests or complete retention cleanup blocks generation so
  follow-up state is not silently ignored.
- Source-policy ambiguity rejects the source rather than assuming independence.

## Validation

Use test-driven development for the helper and skill revisions.

Automated tests cover:

- checkbox detection and unmarking;
- story-block association;
- multiple marked stories;
- malformed Markdown;
- six-calendar-month boundaries;
- preservation and overdue reporting for marked old editions;
- trash naming and 30-day purge boundaries;
- unrelated-file and symlink protection;
- same-day collision behavior;
- JSON output and saved-edition validation.

Behavioral forward tests cover:

- exclusion of English and Chinese government-operated sources;
- independent reporting about government actions with two-source confirmation;
- five to seven new stories remaining separate from unlimited follow-ups;
- no qualifying update for a tracked interest;
- reminder rendering and unmark instructions;
- saved file plus complete inline response;
- use by a less capable agent.

Structural validation continues to use the standard skill validator.

## Out of Scope

- Email delivery, scheduling, RSS aggregation, or HTML output
- A separate graphical marking interface
- A persistent database or interest registry
- Automatic semantic merging of two independently marked stories
- Automatic overwriting of an existing same-day edition
