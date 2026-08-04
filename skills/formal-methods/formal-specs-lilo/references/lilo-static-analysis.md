# Lilo Static Analysis Diagnostics

Authoritative 0.5.10 reference: <https://docs.imiron.io/v/0.5.10/en/index.html>.
Owning page: `specforge doc lilo-static-analysis`. Consult it rather than
guessing whenever a construct here leaves a case open.

**Boundary.** These are diagnostics SpecForge reports about specification
quality. Recognize them and design against them. **Do not run** them: this
skill validates syntax only, per [lilo-authoring.md](lilo-authoring.md). Do not
invoke consistency, redundancy, satisfiability, exemplification, falsification,
or monitoring to check your own work.

## Consistency checking

A spec that no system could satisfy produces a warning:

```lilo
spec main = always (x > 0 && x < 0)
```

Inconsistency **between** specs is also reported. Each of these is satisfiable
alone but they cannot hold together:

```lilo
spec always_positive = always (x > 0)
spec always_negative = always (x < 0)
```

Authoring guidance: if a new requirement makes an existing spec inconsistent,
that is a conflict between requirements. Report it to the user with both specs
named. Do not resolve it by weakening or rewriting the existing spec — that
decision belongs to the user.

## Redundancy checking

A spec implied by others is reported as redundant. In the documented example,
`sometimes_negative` is redundant because it follows from the other two:

```lilo
spec positive_becomes_negative = always (x > 0 => eventually x < 0)
spec sometimes_positive = eventually x > 0
spec sometimes_negative = eventually x < 0
```

Authoring guidance: report the redundancy rather than deleting the user's spec.
A redundant spec is often kept deliberately as a standalone statement of a
requirement, in which case `#[disable(redundancy)]` records that intent — see
[lilo-attributes.md](lilo-attributes.md).

## Guard analysis for case expressions

When a spec is a `cases` expression, its guards are checked for three
properties:

- **satisfiability** — whether each guard can hold on its own;
- **exhaustiveness** — whether the guards together cover every case; and
- **disjointness** — whether the guards are mutually exclusive.

Authoring guidance: this is why `cases` is preferable to a hand-written chain of
implications for a multi-regime requirement. The guards become explicit, and
these three checks then apply to them. Write guards that are exhaustive and
mutually exclusive; if the requirement genuinely leaves a regime unconstrained,
say so rather than padding with a `-> true` branch. See
[lilo-expressions.md](lilo-expressions.md) for the `cases` form.

## Recognizing versus causing a diagnostic

Before reporting, separate diagnostics that were already present from those the
edit introduced. Inspect the project's state before editing, and attribute only
new diagnostics to the change. Never claim to have caused or repaired a
pre-existing one — the same discipline the skill applies to dirty files and
unrelated parse errors.
