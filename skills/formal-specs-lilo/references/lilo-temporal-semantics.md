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
| future-time | `always [I] p`, `eventually [I] p`, `p until [I] q`, `p releases [I] q`; an omitted interval means `[0, infinity]`. |
| past-time | `historically [I] p`, `past [I] p`, `p since [I] q`. |
| window variation | `will_change [I] p` and `did_change [I] p` are true when two distinct supported samples inside the interval hold different values of `p`; `p` may be any type with equality, not only `Bool`. |
| discrete | `next x` and `previous x` move by one sample index, not elapsed time, and take no interval; at the terminal/initial boundary respectively they retain the boundary value. |
| sliding window | `max_future [0, b] x`, `min_future [0, b] x`, `max_past [0, b] x`, `min_past [0, b] x` return the numeric extremum over the window. The interval must start at `0`; `b` may be `infinity`. |
| not documented in 0.5.10 | `next_with` and `previous_with` have no syntax or semantics in the authoritative 0.5.10 language or semantics pages. Do not author or infer forms for them. |

`releases` is the dual of `until`; `historically`, `past`, and `since` are the
past-time counterparts of `always`, `eventually`, and `until`.

## Endpoint obligations

`p until [I] q` requires a supported witness `t'` for `q` inside `t + I`, and
`p` at every supported sample `t''` with `t <= t'' < t'`: the witness sample
itself is excluded, so `p` need not hold there. `p since [I] q` requires a
supported witness `t'` for `q` inside `t - I` and `p` at every supported sample
`t''` with `t' < t'' <= t`, again excluding the witness sample. When no
supported sample lies between the evaluation point and the witness, neither
form constrains `p` at all. `p releases [I] q` is exactly `!(!p until [I] !q)`
and inherits these obligations through that expansion.

## Window variation versus point transition

`will_change` and `did_change` observe variation across a window: two distinct
supported samples with different values anywhere in the interval. They do not
locate the change, do not give its direction, and are false whenever the
interval intersects the support in one sample or none. An explicit rising
transition at the current sample is `p && !previous p`; a falling transition is
`!p && previous p`. Because `previous p` retains the boundary value at sample
index `0`, no transition is ever detected at the first sample of a signal.

## Sliding-window restriction

Author sliding windows only as `[0, b]`. Because the window always contains the
evaluation point, the intersection with the support is never empty, and a
singleton window returns the value of the operand at the evaluation point
itself. These operators return a numeric value, not a Boolean; compare them to
obtain a property, as in `max_past [0, b] x <= limit`.

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
