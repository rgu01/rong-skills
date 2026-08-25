# Evidence rules

Source eligibility, the date gate, and scoring. `SKILL.md` owns the procedure
that applies them.

## Source eligibility

Government agencies, ministries, regulators, legislatures, courts,
intergovernmental bodies, and state-controlled media are ineligible as primary,
secondary, date-evidence, or supporting sources in every language. Do not cite
or rely on them.

Public universities and publicly funded research institutions remain eligible.
Independent reporting about a government action is eligible only when the
underlying event date is exact and wholly inside the coverage window and at
least two reputable, independent, non-government sources confirm every material
claim. Reject a source when its operational independence is ambiguous.

Company, laboratory, academic, repository, and independent-media sources retain
the existing evidence hierarchy. Prefer original company, laboratory, academic,
or repository sources and established independent technology or business
reporting. Seek strong coverage in both languages when available; add a
second-language source only when it improves evidence or context.

Category, tag, index, search-result, and homepage pages are discovery aids, not
story citations. Aggregator digests and weekly-roundup sites are discovery aids
too: their dates and attributions have proven unreliable, so re-derive every
event and date from the primary source before scoring.

## Date gate

Apply this gate to every follow-up, AI Tools, Other AI Stories, and AI at Work
row:

- Record the exact underlying event date or date range, opened source URL, and
  source passage supporting that date.
- If an earlier incident, failure, evaluation, pause, or deployment is material
  to eligibility, record it separately with exact date evidence. Pure context
  is non-gating.
- Mark `Date gate: PASS` only when the event and every gating earlier activity
  have exact dates wholly inside the window. Confirm with a literal ISO-date
  comparison.
- Reject missing, relative-only, undated, partly out-of-window, or
  publication-date-only evidence, even when fewer stories remain.
- A dated partnership or remediation does not make an older or undated incident
  eligible. Report a retrospective disclosure under the date of the disclosure
  only when the disclosure itself is the event.

The underlying event date controls eligibility. An announcement date qualifies
only when the announcement itself creates the event, such as a launch.

## Scoring

Score each eligible candidate from 0 to 2:

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Recency | outside window; reject | first four dates | latest three dates |
| Impact | narrow update | meaningful sector effect | major technical, market, or policy effect |
| Credibility | unsupported; reject | reputable secondary evidence | direct authoritative evidence |
| Mixed-audience relevance | little value | business or technical value | clear value to both |

For AI Tools, also score practical agent-workflow relevance: reject a tool with
no direct agent-lifecycle use, score 1 for a useful narrow capability, and score
2 for clear day-to-day value in building or operating agents.

For AI at Work, also score stance clarity: reject a story whose stance or
employee scope stays ambiguous, score 1 for a stance affecting one team,
function, or data class, and score 2 for an organization-wide stance with a
stated scope and enforcement.

Rank by score and editorial judgment. Prefer broadly useful agent lifecycle
infrastructure within AI Tools, reasonable bucket balance within Other AI
Stories, and a spread across encouraging, discouraging, and disallowing stances
within AI at Work when candidates allow it. Admit a story on its own merit;
balance never justifies a weaker one. Merge only reports about the same event.
