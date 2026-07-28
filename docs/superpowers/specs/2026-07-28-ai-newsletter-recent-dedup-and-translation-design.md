# AI Newsletter Recent Deduplication and Translation Design

## Goal

Prevent a newly requested AI newsletter from repeating events already published
in the preceding seven calendar days, even when requests arrive on consecutive
days or the same event has a different headline. Improve Simplified-Chinese
translations by preserving technical vocabulary when a literal translation
would be nonstandard, awkward, or misleading.

Apply the corrected workflow to future editions and revise the existing
`2026-07-28-ai-newsletter.md` edition.

## Recent-edition preflight

Before researching a new edition:

1. Resolve `knowledge/AI-newsletter/` under the `rong-skills` repository.
2. Select dated newsletter `.md` files whose edition dates fall within the
   seven dates preceding the new edition date.
3. Read every selected file completely.
4. Build a private prior-event exclusion ledger from each story's headline,
   exact event date, entities, product or project, material change, and source
   URLs.

Do not change `newsletter_state.py` or introduce a database, index, or new
archive format. The Markdown editions remain the source of truth.

## Event-level exclusion

Compare every candidate against the prior-event ledger before scoring. Reject a
candidate when its material underlying event has already appeared, regardless
of headline wording, source, section, language, or later retrospective
coverage.

A genuinely new material event involving the same entity or product remains
eligible when it has its own exact in-window date and distinct material change.
Record the prior story and the reason for either exclusion or eligibility in
the candidate ledger.

The new-edition manifests must reconcile only to events absent from the
preceding seven calendar days.

## Translation contract

Translate for technical accuracy and natural usage rather than word-for-word
symmetry.

Keep names, product names, model identifiers, protocol names, API and SDK names,
commands, code identifiers, filenames, platform names, and technical phrases
in English when that is the established or clearer industry form. For example,
retain `headless Linux`; do not write `无头 Linux`.

Use an established Simplified-Chinese technical term when it is conventional
and unambiguous. When uncertain, retain the English term and translate the
surrounding sentence naturally. Preserve all claims, dates, numbers,
benchmarks, confidence, and caveats.

## Current-edition revision

Read all qualifying prior editions, compare their events with
`2026-07-28-ai-newsletter.md`, and remove repeated stories. Research distinct
replacement events that satisfy the existing date and evidence gates; publish
fewer stories if enough replacements do not qualify.

Review every Chinese sentence in the revised edition for technical vocabulary,
natural phrasing, and semantic fidelity. Preserve existing interest marks,
validate the revised Markdown, and do not alter unrelated archive files.

## Verification

Before changing the workflow, run static regression checks that demonstrate the
current skill lacks:

- a mandatory seven-day recent-edition read;
- event-level exclusion against prior Markdown editions;
- an explicit prohibition on literal translations such as `无头 Linux`.

After the edit, repeat those checks, run the newsletter content-contract tests,
run the full newsletter state tests, validate the skill folder, and validate
the revised current edition.

## Non-goals

- No helper-script changes.
- No persistent story database or generated index.
- No headline-only or URL-only deduplication.
- No automatic rewriting of older editions.
