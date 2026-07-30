# Lilo Temporal Patterns

Authoritative 0.5.10 reference: <https://docs.imiron.io/v/0.5.10/en/index.html>.
This catalog maps natural language to Lilo. It does not define semantics: read
[lilo-temporal-semantics.md](lilo-temporal-semantics.md) for the exact readings,
interval rules, and boundary behavior.

An entry is reusable only when **every** field in its `Clarify` list matches the
user requirement. If any field is still open, ask about that field and do not
author the form. Examples use neutral symbols: `p` and `q` are Boolean
expressions, `x` is a value expression, and `a` and `b` are interval endpoints
in declared time units.

Every entry carries the same five fields:

- **Natural language** — a representative phrase.
- **Clarify** — the fields that must be confirmed first.
- **Safe Lilo** — the form to author after clarification.
- **Reading** — what the form means precisely.
- **Mistranslation** — the concrete failure to avoid.

## Entries

### Invariant

- **Natural language:** "`p` shall always hold."
- **Clarify:** the scope of "always" (whole trace or a window); that `p` is a
  persistent state condition, not a point transition; that `p` is Boolean and
  observable.
- **Safe Lilo:** `always p`
- **Reading:** at every evaluation point, `p` holds at every supported sample
  from that point onward; the omitted interval is `[0, infinity]`.
- **Mistranslation:** writing `always [a, b] p` for a whole-trace obligation.
  A bounded window is vacuous wherever the window misses the support, so the
  obligation silently disappears near the end of the trace.

### Bounded eventual response

- **Natural language:** "`p` shall become true within `b` time units."
- **Clarify:** the numeric value and declared unit of `b`; that the bound is
  elapsed time rather than sample movement; whether `a` is `0` or a nonzero
  delay; whether a finite trace must contain a witness.
- **Safe Lilo:** `eventually [0, b] p`
- **Reading:** some supported sample in the inclusive window `[0, b]` ahead
  satisfies `p`. Both endpoints are included.
- **Mistranslation:** meaning one cycle later but writing an elapsed-time
  window. If the requirement is sample movement, use the one-sample entry.
  Also note that `eventually` is false when the window misses the support
  entirely — there is no witness to find.

### Bounded history

- **Natural language:** "`p` shall have held throughout the last `b` time
  units."
- **Clarify:** the value and unit of `b`; that the requirement is universal
  over the window, not a single past occurrence; whether the window should
  start at the current sample (`a = 0`) or exclude it.
- **Safe Lilo:** `historically [0, b] p`
- **Reading:** `p` holds at every supported sample in the inclusive window
  `[0, b]` behind the evaluation point.
- **Mistranslation:** using `past [0, b] p`, which asks only for one occurrence.
  `historically` is also vacuous at the start of a trace where the window
  misses the support, so it cannot express "the trace must be at least `b`
  long."

### Occurrence in the past

- **Natural language:** "`p` shall have happened at some point in the last `b`
  time units."
- **Clarify:** the value and unit of `b`; whether the occurrence is a state
  condition holding at a sample or an explicit transition; whether a witness is
  required in a finite trace.
- **Safe Lilo:** `past [0, b] p`
- **Reading:** some supported sample in the inclusive window `[0, b]` behind
  the evaluation point satisfies `p`.
- **Mistranslation:** reading "has happened" as a transition. A persistent
  condition that was already true before the window satisfies `past`; if the
  requirement is about becoming true, combine with the explicit point
  transition entry.

### Strong until

- **Natural language:** "`p` shall hold until `q`."
- **Clarify:** the exact predicate for `q`; whether `q` is required to occur at
  all (strong reading) or `p` may simply hold forever (needs a different form);
  the interval in which `q` must occur; whether `p` must also hold at the
  sample where `q` occurs.
- **Safe Lilo:** `p until [0, b] q`
- **Reading:** a supported witness for `q` exists in the inclusive window
  `[0, b]`, and `p` holds at every supported sample strictly before that
  witness. `p` is not required at the witness sample.
- **Mistranslation:** assuming `p` must hold when `q` occurs. Also, this form
  is false when `q` never occurs in the window: a requirement that permits `p`
  to hold indefinitely is not `until` and must be reformulated.

### Since

- **Natural language:** "`p` has held ever since `q`."
- **Clarify:** the predicate for `q`; that `q` must actually have occurred in
  the past window; whether `p` is required at the sample where `q` occurred;
  the value and unit of `b`.
- **Safe Lilo:** `p since [0, b] q`
- **Reading:** a supported witness for `q` exists in the inclusive window
  `[0, b]` behind the evaluation point, and `p` holds at every supported sample
  strictly after that witness up to and including now.
- **Mistranslation:** using it where `q` may never have occurred. With no
  witness the form is false, which reports a violation rather than "not yet
  applicable."

### Releases

- **Natural language:** "`p` may stop holding only once `q` has released it."
- **Clarify:** that the requirement is genuinely the dual of `until` and not a
  simple guarded response; the predicate for `q`; the interval; that the
  no-witness case should be permissive rather than violating.
- **Safe Lilo:** `p releases [0, b] q`
- **Reading:** exactly `!(!p until [0, b] !q)`. Derive the meaning by expanding
  the negation; do not reason about `releases` informally.
- **Mistranslation:** treating `releases` as "`p` holds until `q`, and `q` need
  not occur." Expand it: because the expansion negates an `until`, its
  witness and endpoint obligations apply to `!p` and `!q`, not to `p` and `q`.

### One-sample movement

- **Natural language:** "on the next cycle, `x` shall …"
- **Clarify:** that "cycle" means one sample index, not a duration; the
  sampling arrangement, since sample spacing need not be uniform; the behavior
  wanted at the final sample.
- **Safe Lilo:** `next x`, and `previous x` for the backward direction.
- **Reading:** the value at the adjacent sample index. These operators take no
  interval, and at the terminal (`next`) or initial (`previous`) sample they
  retain the boundary value.
- **Mistranslation:** using `next` for an elapsed-time bound. `next` is sample
  movement; a duration requires an interval-qualified operator. Note also that
  the boundary retention makes `next x == x` at the last sample, so a
  difference computed from `next` is zero there.

### Value variation

- **Natural language:** "the value shall not change during the window."
- **Clarify:** the value and unit of `b`; whether the requirement is about any
  variation in the window or about a specific transition; whether direction of
  change matters; that at least two samples fall inside the window.
- **Safe Lilo:** `will_change [0, b] x` for the future window and
  `did_change [0, b] x` for the past window; negate for a no-change
  requirement.
- **Reading:** true when two distinct supported samples inside the inclusive
  window hold different values of `x`. Any type with equality is allowed.
- **Mistranslation:** this is window variation, **not a point transition**. It
  does not locate the change, gives no direction, and is false when the window
  contains one sample or none — so a negated form is trivially satisfied on a
  sparse window.

### Explicit point transition

- **Natural language:** "when `p` becomes true, …"
- **Clarify:** that "becomes" means a transition at this sample rather than a
  persistent condition; the direction (rising or falling); the intended
  behavior at the very beginning of the trace.
- **Safe Lilo:** `p && !previous p` for a rising edge; `!p && previous p` for a
  falling edge.
- **Reading:** `p` holds now and did not hold at the previous sample index.
- **Mistranslation:** no transition is ever detected at the **first sample**,
  because `previous p` retains the boundary value there. Do not substitute
  `did_change`, which reports variation anywhere in a window instead of an edge
  at this sample.

### Rolling extrema

- **Natural language:** "the peak value over the last `b` time units shall stay
  below the limit."
- **Clarify:** the value and unit of `b`; whether the window looks forward or
  backward; that the operand is numeric; the comparison and its bound;
  whether the current sample is included (it always is).
- **Safe Lilo:** `max_past [0, b] x` and `min_future [0, b] x`, always compared
  to a bound, as in `max_past [0, b] x <= limit`.
- **Reading:** the numeric extremum of `x` over the inclusive window. The
  window always contains the evaluation point, so it is never empty; on a
  singleton window the result is `x` at that point.
- **Mistranslation:** writing a nonzero lower bound. Sliding windows accept
  only `[0, b]`. Using the operator on its own is also wrong: it returns a
  number, not a property, so it must be compared.

### Nested temporal operators

- **Natural language:** "whenever `p` holds, `q` shall follow within `b` time
  units."
- **Clarify:** whether the trigger `p` is a state condition or a point
  transition; the value and unit of `b`; whether the response window starts at
  the trigger sample; whether traces in which `p` never holds should pass.
- **Safe Lilo:** `always (p => eventually [0, b] q)`
- **Reading:** at every supported sample where `p` holds, some supported sample
  in the inclusive window `[0, b]` ahead satisfies `q`.
- **Mistranslation:** an implication whose antecedent never holds is
  **vacuous**, so the spec passes without ever exercising the response. If the
  trigger must occur, state that as a separate obligation. Parenthesize the
  implication: writing the guard outside the `always` scope changes the
  requirement.

## Maintenance

Re-check <https://docs.imiron.io/v/0.5.10/en/index.html>, `specforge doc
lilo-language`, and `specforge doc semantics` before adding or editing an entry.
Add no project-specific vocabulary here; keep entries reusable.
