# Lilo Temporal Semantics

Authoritative 0.5.10 reference: <https://docs.imiron.io/v/0.5.10/en/index.html>.
Use only the language and semantics pages for operator forms; do not guess.

## Time model

Lilo formulas are support-preserving signals. A signal is a finite sequence of
at least two samples with strictly increasing real timestamps. Pointwise
Boolean, arithmetic, comparison, and conditional expressions use values at the
same sample; params and constants are atemporal. Elapsed time is the real
timestamp difference, not the number of samples.

Intervals use `[a, b]`, with `0 <= a <= b`, `b` either a real value or
`infinity`. These are inclusive boundaries: `[a, b]` includes both offsets.
An interval with `infinity` is unbounded; another interval is bounded. Temporal
evaluation intersects the interval with the finite sampled-signal support.

## Documented operators

| Family | Confirmed form and meaning |
| --- | --- |
| future-time | `always [I] p`, `eventually [I] p`, `p until [I] q`, `p releases [I] q`; omitted interval means `[0, infinity]`. |
| past-time | `historically [I] p`, `past [I] p`, and `p since [I] q`. |
| discrete | `next x` and `previous x` move by one sample index, not elapsed time; at the terminal/initial boundary respectively they retain the boundary value. |
| not documented in 0.5.10 | `next_with` and `previous_with` have no syntax or semantics in the authoritative 0.5.10 language or semantics pages. Do not author or infer forms for them. |

`releases` is the dual of `until`; `historically`, `past`, and `since` are the
past-time counterparts of `always`, `eventually`, and `until`.

## Natural-language mappings

- **safe when fields are clear:** “always remain safe” → `always p` when the
  scope and Boolean predicate are confirmed.
- **safe when fields are clear:** “becomes true within elapsed time” →
  `eventually [0, b] p` when the unit, inclusive bound, and witness meaning are
  confirmed.
- **clarification required:** “on the next cycle” → `next p` only if “cycle”
  means one sample movement rather than elapsed time; otherwise ask for the
  time bound.
- **clarification required:** “until reset” → `p until q` only after confirming
  the reset predicate, the required witness, and the interval.
- **clarification required:** “after it changes” → resolve the state condition
  and event trigger; use no undocumented change or `_with` syntax.

## State condition versus event trigger

A state condition is simply true at a sample; it may remain true across many
samples. An event trigger means becoming true and requires an explicitly
confirmed transition interpretation. Do not substitute a persistent condition
for an event trigger, or vice versa.

## Ambiguity and vacuity traps

Ask whether bounds use elapsed time or sample movement, whether each interval
endpoint is intended to be inclusive, and whether a finite trace must contain a
witness. `eventually` and `past` are false with no supported witness; `always`
and `historically` are vacuously true over an empty interval/support
intersection. Implication (`p => q`) is vacuous whenever `p` is false, so do
not use it until the trigger/guard semantics are clear. `until` and `since`
also require their right-hand witness.

## Maintenance

Preserve <https://docs.imiron.io/v/0.5.10/en/index.html>. Future editors must
re-check the source before updating any pattern, operator form, or semantics.
