# Pedestrian Crossing Verification Report

**How to use this template:** Every `[Replace: ...]` marker is instructional text for the student, not an unresolved author note. Replace each marker with concise evidence and delete this instruction before submission. Copy queries and verifier results exactly from the submitted UPPAAL model/run. If an exact query contains a vertical bar, escape it as `\|` so the Markdown table still renders.

## 1. Student and tool information

| Field | Value |
|---|---|
| Student name | [Replace: full name] |
| Student identifier | [Replace: student identifier] |
| UPPAAL version | [Replace: exact version used for the final verification] |
| Artificial intelligence (AI) assistant(s), if any | [Replace: names and versions if known, or “None”] |

## 2. Timing and requirement interpretation

### Chosen constants

| Constant | Chosen value | Calculation and rationale |
|---|---:|---|
| `WALK_TIME` | [Replace: integer from 7 to 12] s | [Replace: show the calculation using 6 m, 1 m/s, and the 1 s start allowance; explain any additional margin.] |
| `MAX_WAIT` | [Replace: integer from 14 to 30] s | [Replace: show how clearance, the minimum vehicle-green interval, and clearance again fit at the least-favourable cycle point; explain why the chosen service bound suits your design.] |

### Fixed facts confirmation

| Fixed fact | Required value | Confirmed in the final model and report? |
|---|---:|---|
| UPPAAL time unit | 1 second | [Replace: Yes, after checking] |
| Crossing width | 6 m | [Replace: Yes, after checking] |
| Design pedestrian speed | 1 m/s | [Replace: Yes, after checking] |
| Pedestrian start allowance | 1 s | [Replace: Yes, after checking] |
| Minimum uninterrupted vehicle-green time | 10 s | [Replace: Yes, after checking] |
| All-red clearance before a conflicting movement | exactly 2 s | [Replace: Yes, after checking] |

### Operational meanings

| Term or rule | Meaning in this model and how it is represented |
|---|---|
| Request | [Replace: confirm that it may occur whenever WALK is inactive; define the event that creates a pending request and identify the model state/update that stores it.] |
| Service | [Replace: state that service occurs on entry into WALK and identify how that entry clears the pending request.] |
| Repeated press | [Replace: explain how presses merge while a request is pending, without queuing or restarting the waiting-time measurement.] |
| Conflicting greens | [Replace: identify exactly which vehicle-green and pedestrian-WALK states are considered conflicting.] |
| Clearance | [Replace: explain how the model enforces exactly 2 s of all-red after either movement stops, with neither early departure nor lingering.] |
| WALK duration | [Replace: explain how WALK lasts exactly `WALK_TIME`, with neither early departure nor lingering.] |
| Vehicle minimum and service bound | [Replace: explain how at least 10 s of uninterrupted vehicle green is enforced and how later delay is limited so a pending request is served within `MAX_WAIT`.] |

Bounded response is measured from `[Replace: the precise request event that creates the pending request]` to `[Replace: the precise transition entering WALK]`. The mechanism that records or observes this interval is `[Replace: clock, variable, observer, or other concrete mechanism]`.

## 3. Model architecture

| Template | Responsibility | Locations/modes | Clocks/variables | Interactions |
|---|---|---|---|---|
| [Replace: environment/button template name] | [Replace: when requests can be issued, how the first request is stored, and how repeated presses merge.] | [Replace: relevant locations/modes and their meanings.] | [Replace: relevant local/shared state, including request storage and waiting-time state.] | [Replace: exact synchronisations/shared updates through which it affects the controller.] |
| [Replace: controller template name] | [Replace: vehicle operation, exact clearance, exact WALK duration, and return to vehicle operation.] | [Replace: vehicle-green, all-red, WALK, and other relevant locations/modes.] | [Replace: clocks/variables enforcing exactly 2 s clearance, exactly `WALK_TIME`, and at least 10 s vehicle green.] | [Replace: request acceptance, WALK entry/service, and other synchronisations/updates.] |
| [Replace: observer template name, or delete row if absent] | [Replace: how bounded response is measured and a missed `MAX_WAIT` is exposed.] | [Replace: idle, measuring, error/timeout, or actual modes.] | [Replace: observer clock and variables.] | [Replace: request-start and service interactions.] |
| [Replace: extension template name, or “Existing template modified”] | [Replace: timed extension responsibility.] | [Replace: new or changed modes.] | [Replace: new or changed timing state.] | [Replace: new or changed interactions.] |

Architecture consistency note: `[Replace: explain briefly why requests cannot be lost, WALK cannot begin spontaneously, clearance/WALK cannot linger, and the bounded-response trigger is reachable.]`

## 4. Requirement-to-query traceability

The final `model.xml` must embed every query below using the Timed Computation Tree Logic (TCTL) forms supported by the stated UPPAAL version. Replace each prompt with the exact submitted evidence; do not paraphrase verifier output.

| ID | Informal requirement | Operational interpretation | Exact embedded query | Expected result | Actual UPPAAL result | Engineering meaning and non-vacuity evidence |
|---|---|---|---|---|---|---|
| R1 | WALK is reachable. | [Replace: identify the observable model condition that means WALK has begun.] | [Replace: copy the exact embedded reachability query.] | [Replace: expected satisfied/not satisfied before running.] | [Replace: copy the exact verifier result.] | [Replace: explain what reachable execution this establishes and why it is meaningful.] |
| R2 | Vehicle green and pedestrian WALK are never active simultaneously. | [Replace: identify the exact model states representing the two conflicting movements.] | [Replace: copy the exact embedded safety query.] | [Replace: expected result before running.] | [Replace: copy the exact verifier result.] | [Replace: interpret absence of conflicting greens and cite a supporting reachability result showing the relevant phases occur.] |
| R3 | Every request issued while WALK is inactive is served within `MAX_WAIT`. | [Replace: state the exact trigger, endpoint, clock/boundary convention, and timeout/error meaning.] | [Replace: copy the exact embedded bounded-response query.] | [Replace: expected result before running.] | [Replace: copy the exact verifier result.] | [Replace: explain the service guarantee and cite the exact query/result proving that the trigger and service path are reachable.] |
| R4 | The model is deadlock-free. | [Replace: define what UPPAAL deadlock freedom rules out in this network.] | [Replace: copy the exact embedded deadlock query.] | [Replace: expected result before running.] | [Replace: copy the exact verifier result.] | [Replace: explain the engineering meaning and distinguish deadlock freedom from timely service.] |
| R5 | Relevant behaviour is non-vacuous and supported by reachability evidence. | [Replace: name the request, pending/waiting, clearance, WALK, or return behaviour demonstrated.] | [Replace: copy the exact embedded supporting query; add additional trace rows below if needed.] | [Replace: expected result before running.] | [Replace: copy the exact verifier result.] | [Replace: state which universal-property trigger or behaviour this proves can actually occur.] |

## 5. Genuine failed run, diagnosis, and repair

| Evidence item | Record |
|---|---|
| Defect or controlled change | [Replace: describe the accidental defect or the single controlled, relevant change.] |
| Scope | [Replace: core model or timed extension.] |
| Prediction before running | [Replace: state which behaviour/property you predicted would fail and why.] |
| Failed-model version | [Replace: saved filename, commit/hash, timestamp, or other unambiguous version identifier distinct from the final model.] |
| Trace source | [Replace: UPPAAL diagnostic/counterexample trace from that failed-model version and how it was saved or identified.] |
| Exact failing query | [Replace: copy the query exactly.] |
| Exact failing result | [Replace: copy the UPPAAL result exactly.] |

### Exact UPPAAL diagnostic trace excerpt

Copy a sufficient verbatim, tool-produced excerpt of the genuine diagnostic trace below. It must show the states/transitions through the violation and come from the failed-model version identified above; a filename or saved location alone is not evidence.

```text
[Replace: exact UPPAAL diagnostic trace excerpt]
```

### Hand reconstruction of the diagnostic trace

Reconstruct the shortest relevant counterexample trace or prefix **through the violation** from the genuine UPPAAL diagnostic trace. Include all steps needed to establish clock values and enabled transitions; omit an irrelevant suffix.

| Step | Delay/action | Locations | Clocks | Sync/updates | Why enabled |
|---:|---|---|---|---|---|
| 0 | [Replace: initial state/action.] | [Replace: location of every relevant component.] | [Replace: relevant initial clock values.] | [Replace: initial values/updates, or none.] | [Replace: initial-state explanation.] |
| 1 | [Replace: elapsed delay or discrete action.] | [Replace: resulting relevant locations.] | [Replace: clock values before/after as needed.] | [Replace: channel and updates.] | [Replace: guard, invariant, urgency, and enabling state.] |
| … | [Replace: add rows until the violating state/transition is shown.] | [Replace.] | [Replace.] | [Replace.] | [Replace.] |
| Violation | [Replace: final relevant delay/action.] | [Replace: violating locations/state.] | [Replace: values demonstrating the violation.] | [Replace: synchronisation/updates.] | [Replace: why this step is possible and exactly how it violates the query.] |

Diagnosis: `[Replace: identify the causal modelling error, referring to the trace rather than only restating the failed property.]`

Repair: `[Replace: describe the concrete model correction.]`

Re-verification query: `[Replace: copy the exact query run on the repaired model.]`

Re-verification result: `[Replace: copy the exact UPPAAL result.]`

Causal explanation: `[Replace: explain why the repair blocks the traced cause, and why the re-run is evidence for the repaired—not failed—model version.]`

## 6. Exactly one student-designed timed extension

Changing only a constant or adding/changing a query is insufficient: this extension must add or alter concrete model behaviour and must not merely restate a mandatory requirement.

| Field | Extension evidence |
|---|---|
| Precise informal requirement | [Replace: one testable sentence specifying the timed extension.] |
| Engineering usefulness | [Replace: why this behaviour is useful at a pedestrian crossing.] |
| Timed condition and effect | [Replace: exact time-related trigger/guard/bound and resulting behaviour.] |
| Concrete model delta | [Replace: templates, locations, transitions, clocks, variables, channels, guards, invariants, and/or updates added or changed.] |
| Property class | [Replace: safety/invariant, liveness, or reachability, and why.] |
| Exact embedded extension query | [Replace: copy the exact query.] |
| Expected result | [Replace: prediction before running.] |
| Actual UPPAAL result | [Replace: copy the exact verifier result.] |
| Exact non-vacuity query | [Replace: copy the query showing the extension trigger/effect can occur.] |
| Non-vacuity result | [Replace: copy the exact verifier result.] |
| Engineering interpretation | [Replace: what the two results establish, their limits, and how the extension genuinely changes timed behaviour.] |

## 7. AI-assisted decision

Do not include a transcript. Analyse one significant suggestion that affected modelling or verification.

| Decision evidence | Record |
|---|---|
| Suggestion in my own words | [Replace: concise restatement of the AI suggestion.] |
| Relevant requirement or assumption | [Replace: assignment requirement or modelling assumption against which it was judged.] |
| Independent semantic/formal check | [Replace: your own reasoning, calculation, documentation check, or property used to test it.] |
| Decision and reason | [Replace: accepted, modified, or rejected; explain why.] |
| Exact UPPAAL evidence | [Replace: exact query or queries and exact result or results that informed the decision.] |

## 8. Final consistency and responsibility check

Replace each marker only after performing the check.

- [Replace: Confirmed] `WALK_TIME` and `MAX_WAIT` match in the final model, embedded queries, calculations, and this report; `WALK_TIME` is in [7, 12] and `MAX_WAIT` is in [14, 30].
- [Replace: Confirmed] Every reported verifier result is copied exactly from a run of the identified model version.
- [Replace: Confirmed] The hand trace matches the identified failed-model version and its genuine diagnostic trace.
- [Replace: Confirmed] The report clearly distinguishes the failed version from the repaired, submitted final model.
- [Replace: Confirmed] The final `model.xml` contains all mandatory, extension, and supporting/non-vacuity queries embedded in the model.
- [Replace: Confirmed] The extension includes a concrete timed-behaviour model change, not only a constant or query change.
- [Replace: Confirmed] The submission contains exactly `model.xml` and this completed template renamed to `report.md`.

**Declaration of responsibility:** I, `[Replace: name]`, confirm that I understand and take responsibility for the submitted model, queries, traces, verifier results, and engineering interpretations, including work developed with AI assistance.
