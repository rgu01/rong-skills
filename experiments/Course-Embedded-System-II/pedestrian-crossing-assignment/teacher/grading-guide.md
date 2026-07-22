# Teacher grading guide

> **Confidential teacher material. Do not distribute to students.**

## Grading principle

Grade the report first and holistically as **pass or revision needed**. The checking-points and pass-criteria files define the eventual boundary; this guide does not add marks or a numerical scheme.

The golden rule is to look for one concrete, consistent chain:

> requirement → operational interpretation → model mechanism → exact query → actual tool evidence → engineering meaning

Artificial intelligence (AI) can generate fluent prose and plausible-looking models. Fluency, diagram beauty, and the amount or sophistication of AI use are therefore not evidence. A submission is credible when its claims are supported by specific model elements and UPPAAL results, and when those elements agree across the report.

Contradictions matter even when every individual paragraph sounds reasonable. Also flag causal gaps: for example, an invariant named as a timing mechanism without the departure guard that makes the duration exact, or a passing universal property without evidence that its trigger can occur.

## Report-first reading workflow

Read in the report's order. Keep a short list of names, constants, and claims to compare later.

### 1. Student and tools

Strong evidence gives the student's complete identity, the exact UPPAAL version, and each artificial intelligence (AI) assistant and version used, or explicitly records “None.”

Weak evidence omits identity or leaves the UPPAAL or AI tool record missing, partial, or ambiguous.

### 2. Timing and semantics

Strong evidence uses one-second time units; derives a baseline pedestrian time from 6 m at 1 m/s plus the 1 s start allowance; selects integer `WALK_TIME` in [7, 12] s and `MAX_WAIT` in [14, 30] s; and explains the selected margin. It identifies the first request that creates pending work, says repeats merge without resetting the wait, preserves the request until WALK entry, and treats entry into WALK as service. It also states whether service exactly at `MAX_WAIT` is allowed—it is, because “within” is inclusive.

Weak evidence merely repeats the ranges, gives a preference rather than a calculation, times every button press separately, clears pending before service, or measures to the end of WALK. Flag any claim that `MAX_WAIT` is met without accounting for the least-favourable path through 2 s clearance, 10 s minimum green, and 2 s clearance.

### 3. Architecture

Strong evidence names an environment/button template and a controller, their real locations, clocks, variables, and interactions. The request interaction changes controller behaviour. Optional observer or extension structures have a distinct, explained role.

Weak evidence lists generic components but never connects a request event to controller state. Flag a button that cannot actually issue requests, a controller that cycles independently of requests, invented names, or a table that disagrees with later queries and traces.

### 4. R1–R5 traceability

For each row, follow the entire golden-rule chain. Strong evidence gives the exact embedded query, an actual UPPAAL result, a conservative interpretation, and relevant non-vacuity support:

- R1 establishes that WALK can be reached.
- R2 universally excludes simultaneous vehicle green and WALK.
- R3 establishes two universal obligations for each newly pending request: eventual service at WALK entry, and service no later than the inclusive `MAX_WAIT` boundary. Strong evidence either supplies separate universal service/liveness and numeric-bound evidence, with a reachable trigger, or uses a sound construction that necessarily exposes every unserved or late request and thereby combines both obligations.
- R4 uses an explicit network-level deadlock query and does not overstate what deadlock freedom proves.
- R5 shows that request, service, and other triggers relied on by universal claims can actually occur.

Weak evidence substitutes expected results for actual results, paraphrases rather than copies a query, treats one simulation as proof, or infers all requirements from `A[] not deadlock`. For R3, a clock-bound invariant alone is weak: it can allow an unserved request with time stalled or zero-time behaviour at the boundary. Existential service reachability on a different path does not establish universal service. For an observer, check that missed service makes timeout/error unavoidable rather than merely enabling an optional edge; that timeout does not race with valid service at elapsed time exactly equal to `MAX_WAIT`; and that service/timeout ordering and synchronisation implement the inclusive boundary. Flag mismatched process/location names, unsupported bounded-response claims, a false existential reachability result described as a counterexample, and universal claims whose antecedent is unreachable. Deadlock freedom alone does not exclude a zero-time infinite loop or time-lock.

### 5. Failed trace, diagnosis, and repair

Strong evidence identifies the failed model/version, records a genuine diagnostic trace from that version, reconstructs a short relevant prefix with locations, delays, clocks, synchronisations, and updates, and ties the observed violation to one causal defect. The repair changes that cause, and the same relevant query is rerun on an identified repaired/final version.

Weak evidence gives a story with no tool-produced trace, a sequence that cannot establish the shown clock values, or a repair unrelated to the violation. Flag trace names absent from the stated failed model, a failed existential reachability check offered as the required diagnostic violation trace, and re-verification performed on an unidentified or different model.

### 6. Timed extension

Strong evidence states one precise and useful timed requirement, identifies a concrete model delta, embeds a suitable property, reports the actual result, supplies non-vacuity evidence where relevant, and explains the changed behaviour.

Weak evidence only renames a core phase, changes a constant, adds a query to an unchanged model, or restates a mandatory requirement. Flag extensions whose prose, mechanism, and property concern different triggers or time bounds.

### 7. AI decision

Strong evidence describes one consequential suggestion, connects it to a requirement or assumption, independently checks it against the model and a query/result, and explains an accept/modify/reject decision.

Weak evidence says only that “AI helped,” reports a prompt transcript, or treats AI output as verification evidence. The quality of the student's judgment is relevant; the quantity of AI usage is not.

### 8. Final consistency

Strong evidence confirms that constants, names, model versions, embedded queries, actual results, failed/repaired evidence, and the single extension agree throughout. The final model includes all mandatory and supporting queries, and the student completes the responsibility declaration accepting responsibility for the submitted model, queries, traces, results, interpretations, and AI-assisted work.

Weak evidence leaves template markers or the responsibility declaration incomplete, mixes failed-model and final-model results, uses different timing values in prose and queries, or claims structures that do not appear elsewhere. Treat unexplained inconsistencies as evidence-chain failures, not cosmetic errors.

### 9. Decide

Decide pass or revision needed from the whole chain, using the separate checking points and pass criteria for the final boundary. A locally polished section cannot compensate for missing actual verification evidence. Conversely, harmless topology or naming differences are not defects when the semantics and evidence are sound.

### 10. Optional XML check

Escalate to the final `model.xml` only when the report leaves a material doubt or a quick confirmation is useful. This check is diagnostic, not a replacement for holistic report grading.

Check only that:

- the model loads;
- final `WALK_TIME` and `MAX_WAIT` values match the report and allowed ranges;
- cited template, state, clock, variable, and channel names exist;
- mandatory and extension queries are embedded;
- verifier results agree with reported final-model results;
- the extension exists as a model change; and
- the failed trace is assessed from report evidence unless the failed model/version was separately submitted. A repaired final model should not reproduce the old failed trace.

Do not reverse-engineer or re-grade the entire design from XML when the report already establishes a consistent chain. If the XML contradicts the report, record the exact contradiction and return to the holistic decision.

## Efficient procedure

Allow roughly **10–15 minutes for a first pass**:

1. Record the two constants, request trigger, service endpoint, and main model names from timing/semantics and architecture.
2. Scan R1–R5 for exact queries, actual results, and non-vacuity; mark any broken link in the chain.
3. Read the failed run for trace provenance and a causal repair, then test the extension and AI sections against the same standard.
4. Run the final-consistency checklist and decide pass or revision needed under the separate criteria.

Escalate to XML when a name, constant, query, result, timing mechanism, extension delta, or final-version claim is contradictory, absent, or too ambiguous to judge. Also escalate when the report is suspiciously generic or when a claimed causal repair cannot be reconciled with the trace. Do not escalate merely because the student chose an unfamiliar but coherent automaton topology.
