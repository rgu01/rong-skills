# Expected solution shape

> **Confidential teacher material. Do not distribute to students.**

## Boundaries of the expectation

There is no golden Extensible Markup Language (XML) file and no required single topology. Different clocks, channels, shared variables, observers, committed/urgent locations, and decompositions can all be acceptable when they implement the stated semantics and support the reported evidence. Judge behaviour and traceability, not resemblance to one diagram.

The fixed facts are:

- one UPPAAL time unit is 1 s;
- crossing width is 6 m;
- design pedestrian speed is 1 m/s;
- pedestrian start allowance is 1 s;
- uninterrupted vehicle green is at least 10 s; and
- all-red clearance before a conflicting movement is exactly 2 s.

The selected constants must be integers: `WALK_TIME` is in the inclusive range [7, 12] s and `MAX_WAIT` is in the inclusive range [14, 30] s. A basic crossing calculation is 6 m ÷ 1 m/s + 1 s = 7 s; a larger `WALK_TIME` needs a stated margin. The `MAX_WAIT` rationale must be compatible with the model, including the least-favourable combination of clearance, the 10 s minimum green interval, and clearance before WALK.

## Minimal credible model family

A minimal credible network contains:

- an Environment/Button timed automaton (TA) that can issue a request whenever WALK is inactive; and
- a Controller TA that represents vehicle, clearance, and pedestrian phases.

An observer or a separate extension template is optional. Shared state, rendezvous, or another valid interaction style may be used, but the request interaction must influence the controller. An environment that never requests, or a controller whose WALK cycle is independent of requests, is not a credible implementation.

A typical phase family is:

> vehicle green → exactly 2 s all-red clearance → exactly `WALK_TIME` WALK → exactly 2 s all-red clearance → vehicle green

WALK is entered only with a pending request, and entry serves and clears that request. The implementation must also explain requests during every period in which WALK is inactive, including the post-WALK clearance. Repeated presses while pending merge into one request, preserve the original wait start, and do not form a queue. A design may preserve the pending flag across phases or transfer equivalent state between components, but it must not lose the trigger. During WALK, request generation is outside the assignment semantics; immediately after WALK becomes inactive, requests must again be possible and handled consistently.

## Typical timing mechanisms

Names and clock allocation may vary, but a sound design usually exhibits these concepts:

- The minimum vehicle-green time is a lower-bound guard on leaving vehicle green. It is not an upper-bound invariant. If vehicle green may continue beyond 10 s, the design must still ensure every pending request can reach WALK by `MAX_WAIT`.
- An exact-duration phase normally combines an upper-bound location invariant with a matching departure guard. For example, conceptually, a phase clock cannot exceed its duration and the exit is enabled only at that duration. The boundary transition must be available; otherwise an invariant can produce deadlock rather than progress.
- A request-wait clock starts only when the first request creates pending work. Repeated presses while pending must not reset it.
- Bounded response has two obligations: every pending request is eventually served, and service occurs no later than the inclusive `MAX_WAIT` boundary. A directly observable pending/clock condition needs universal service/liveness evidence as well as universal numeric-bound evidence and non-vacuity. Alternatively, a sound observer or construction may combine both obligations if every unserved or late request necessarily becomes observable.
- An observer timeout/error transition must be forced or otherwise unavoidable when service is missed, not an optional edge the model can ignore. Its service and timeout synchronisation/ordering must allow valid service at elapsed time exactly equal to `MAX_WAIT` without an erroneous timeout race, while necessarily exposing service after the boundary or no service at all. The observer must stop measuring after service.
- Clearance and WALK must have neither early exits nor lingering executions. Exact timing claims require both sides of the bound, not merely a lower-bound guard.

“Within `MAX_WAIT`” includes service exactly when elapsed time equals `MAX_WAIT`. A timeout/error construction must respect that equality boundary: it must distinguish a genuinely late service from a service transition taken at the allowed boundary, including UPPAAL's discrete-transition ordering at the same time instant.

## Suitable query shapes

The report should spell out every acronym on first use, including **Timed Computation Tree Logic (TCTL)**. Query syntax depends on the student's observable state and UPPAAL version, so the patterns below are deliberately generic rather than a ready-to-submit set:

- Reachability: `E<> <controller-is-in-WALK>`.
- Universal safety: `A[] not (<vehicle-green> and <WALK>)`.
- Bounded response: either separate universal evidence for eventual service and for the inclusive numeric bound, plus non-vacuity, or a universal check over a sound construction that necessarily exposes every unserved or late request and therefore covers both. A clock-bound invariant alone does not prove eventual service, and existential reachability of service on some other path is insufficient. Conversely, an unbounded service/liveness property alone does not establish a numeric deadline.
- Deadlock freedom: `A[] not deadlock`.
- Non-vacuity: one or more existential reachability checks for `<request-created>`, `<request-pending>`, `<service/WALK-entry reached>`, or an extension trigger and outcome.

Process and location placeholders must be replaced by actual model expressions. A passing universal formula needs a reachable trigger. Results establish only the submitted formula over the submitted model; interpretations should remain conservative. `A[] not deadlock` does not by itself exclude a zero-time infinite loop or time-lock, so it cannot fill the eventual-service gap in R3.

## Frequent failure and vacuity patterns

Look especially for:

- an environment with no reachable request transition;
- unreachable WALK;
- periodic or spontaneous WALK that ignores pending requests;
- a pending trigger that disappears during clearance or a phase change;
- a wait clock reset by repeated requests;
- `MAX_WAIT` claimed in prose but absent from both model mechanism and effective query;
- a clearance location that can leave before 2 s or linger after 2 s;
- WALK that can linger beyond `WALK_TIME`;
- a 10 s green minimum plus additional uncontrolled delay that makes the selected `MAX_WAIT` impossible, especially at the 14 s lower boundary;
- a deadlock-freedom claim with no explicit deadlock query;
- trace rows containing locations, clocks, synchronisations, or updates not present in the identified failed model; and
- an “extension” consisting only of a renamed core element, changed constant, new query, or prose with no model delta.

Also check whether a superficially correct property is vacuous. If requests cannot happen, a response property may pass without demonstrating service. If WALK is unreachable, mutual exclusion may pass for the wrong reason. Supporting reachability should expose the relevant trigger and behaviour.

## Expected failed-run and repair evidence

There is no required counterexample sequence. Credible evidence has these characteristics:

- it identifies the exact failed model or run and the exact failing universal safety, bounded-response, or deadlock query;
- it includes a genuine UPPAAL diagnostic trace excerpt;
- its hand reconstruction follows a shortest relevant prefix, with enough delays and transitions to justify component locations, clock values, synchronisations, and updates;
- the diagnosis names the modelling cause revealed by the trace rather than merely restating the violated requirement;
- the repair changes that cause; and
- re-verification reports the relevant query and result from the repaired/final model.

A false existential reachability query does **not** yield the diagnostic counterexample required here and must not be presented as one. The final repaired model need not reproduce the old trace; without a submitted failed version, trace credibility is judged from the report's captured evidence and internal consistency.

## Extension quality

An acceptable extension specifies one useful timed behaviour precisely, identifies its model delta, verifies a matching safety/invariant, liveness, or reachability property, and supplies non-vacuity where relevant. Possible categories include night operation, an audible signal, button debouncing, and bounded bus priority, but the category name is not a specification and this guide intentionally gives no complete design.

Insufficient extensions merely rename a state, change a constant, add a query, or restate a core requirement. The requirement, new timing mechanism, query, result, and engineering interpretation must describe the same changed behaviour.

## AI judgment evidence

Strong evidence selects a concrete artificial intelligence (AI) suggestion, tests it against a named requirement or assumption, checks the resulting mechanism with an exact query and actual result, and explains why it was accepted, modified, or rejected. “AI helped with the model” or a transcript without an independent technical judgment is insufficient. AI prose is not verifier evidence.
