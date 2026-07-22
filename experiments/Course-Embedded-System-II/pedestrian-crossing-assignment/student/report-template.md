# Pedestrian Crossing Verification Report

**Template convention:** Replace every `[Replace: ...]` marker and delete this instruction before submission. In tables, put exact evidence on one line and escape each vertical bar as `\|`; put multiline evidence in a code block. Copy queries and results exactly from the identified UPPAAL model/run, and record diagnostic evidence faithfully with its source.

## 1. Student and tools

Student/tool record: `[Replace: student name; student identifier; exact UPPAAL version; artificial intelligence (AI) assistant names/versions, or “None”.]`

## 2. Timing and interpretation

| Constant | Value | Calculation and rationale |
|---|---:|---|
| `WALK_TIME` | [Replace: integer 7–12] s | [Replace: calculation using 6 m, 1 m/s, and 1 s start allowance; justify any margin.] |
| `MAX_WAIT` | [Replace: integer 14–30] s | [Replace: show that clearance, 10 s minimum vehicle green, and clearance again fit at the least-favourable request point; justify the chosen bound.] |

Fixed facts used above and in the model: one UPPAAL time unit is 1 s; crossing width is 6 m; design pedestrian speed is 1 m/s; start allowance is 1 s; uninterrupted vehicle green is at least 10 s; all-red clearance before a conflicting movement is exactly 2 s.

- Request and service: requests may occur whenever WALK is inactive; the first creates a pending request preserved until service; repeats merge without queueing or restarting time; WALK requires a pending request, and entry serves and clears it. `[Replace: identify the representing event, state, guard, and updates.]`
- Phase timing: `[Replace: identify conflicting greens and explain exactly 2 s clearance after either movement stops, exactly WALK_TIME, return to vehicle operation, at least 10 s vehicle green, and how any longer green/phase delay still preserves MAX_WAIT.]`
- Bounded response: `[Replace: identify the request-created trigger, WALK-entry endpoint, clock/boundary convention, and concrete measurement/timeout mechanism.]`

## 3. Model architecture

Name concrete structures; do not repeat the semantic explanations above.

| Template | Responsibility | Locations/modes | Clocks/variables | Interactions |
|---|---|---|---|---|
| [Replace: environment/button name] | Issues/records requests | [Replace: names and meanings] | [Replace: names and purposes] | [Replace: channels/shared updates] |
| [Replace: controller name] | Controls vehicle, clearance, and WALK phases | [Replace: names and meanings] | [Replace: names and purposes] | [Replace: channels/shared updates] |
| [Replace: observer name, or delete row if absent] | Measures bounded response | [Replace: names and meanings] | [Replace: names and purposes] | [Replace: channels/shared updates] |
| [Replace: extension template, or “Existing template modified”] | Implements the timed extension | [Replace: new/changed modes] | [Replace: new/changed timing state] | [Replace: new/changed interactions] |

## 4. Requirement-to-query traceability

The final `model.xml` must embed every query below using the Timed Computation Tree Logic (TCTL) forms supported by the stated UPPAAL version.

| Requirement identifier | Informal requirement | Operational interpretation | Exact embedded query / query set | Expected result / result set | Actual UPPAAL result / result set | Engineering meaning and non-vacuity evidence |
|---|---|---|---|---|---|---|
| R1 | WALK is reachable. | [Replace: observable WALK condition] | [Replace: exact query] | [Replace: prediction before run] | [Replace: exact result] | [Replace: engineering meaning] |
| R2 | Vehicle green and WALK are never simultaneous. | [Replace: conflicting model states] | [Replace: exact query] | [Replace: prediction before run] | [Replace: exact result] | [Replace: meaning; reference R5 support] |
| R3 | Each request is eventually served at WALK entry and no later than the inclusive `MAX_WAIT` boundary. | [Replace: trigger and endpoint; explain how separate universal obligations or a combined construction cover every relevant execution and allow service exactly at equality] | [Replace: exact universal eventual-service and numeric-bound query set, or exact combined query and construction] | [Replace: prediction for each query/result] | [Replace: exact result set] | [Replace: why the evidence is complete for unserved and late executions, respects inclusive equality, and is non-vacuous; reference R5 trigger evidence] |
| R4 | The model is deadlock-free. | [Replace: network-level meaning] | [Replace: exact query] | [Replace: prediction before run] | [Replace: exact result] | [Replace: meaning and limit] |
| R5 | Relevant behaviour is non-vacuous/reachable. | [Replace: supported trigger/behaviour] | [Replace: exact supporting query; add rows only if needed] | [Replace: prediction before run] | [Replace: exact result] | [Replace: universal property or behaviour supported] |

## 5. Genuine failed run, diagnosis, and repair

| Evidence | Record |
|---|---|
| Defect/change and scope | [Replace: accidental defect or controlled change; core or extension] |
| Prediction before run | [Replace: predicted failure and reason] |
| Failed-model identifier | [Replace: filename, commit/hash, timestamp, or equivalent] |
| Trace source | [Replace: failed model/run, UPPAAL version, simulator location, and whether the record below is pasted output or a faithful transcription] |
| Exact failing query | [Replace: exact query] |
| Exact failing result | [Replace: exact UPPAAL result] |

### UPPAAL diagnostic trace record

Paste the relevant output if your UPPAAL version makes it copyable, or provide a faithful, clearly labelled transcription of the states and transitions displayed in the simulator. Include the relevant sequence through the violation; a saved location or unsupported story alone is insufficient.

```text
[Replace: pasted UPPAAL output, or clearly labelled faithful simulator transcription, tied to the failed model/run above]
```

### Hand reconstruction

Separately expand the diagnostic record semantically using the shortest relevant prefix through the violation. Include delays, clock values, synchronisations/updates, and enabling reasons needed to explain the sequence; omit irrelevant suffixes.

| Step | Delay/action | Locations | Clocks | Sync/updates | Why enabled |
|---:|---|---|---|---|---|
| [Replace: delete this row and add the necessary trace rows across all six columns] | — | — | — | — | — |

| Repair evidence | Record |
|---|---|
| Diagnosis | [Replace: causal modelling error demonstrated by the trace] |
| Repair | [Replace: concrete model correction] |
| Repaired/final model identifier | [Replace: filename, commit/hash, timestamp, or equivalent] |
| Re-verification query | [Replace: exact query run on this repaired/final version] |
| Re-verification result | [Replace: exact UPPAAL result] |
| Causal explanation | [Replace: why the repair blocks the traced cause and the re-run applies to the final version] |

## 6. Exactly one student-designed timed extension

The extension must concretely change timed behaviour; changing only a constant or query is insufficient.

| Evidence | Record |
|---|---|
| Requirement and usefulness | [Replace: precise timed informal requirement and engineering purpose] |
| Timed condition/effect | [Replace: exact trigger/guard/bound and resulting behaviour] |
| Concrete model delta | [Replace: changed templates, locations, transitions, clocks, variables, channels, guards, invariants, or updates] |
| Property class | [Replace: safety/invariant, liveness, or reachability; justify] |
| Exact embedded query | [Replace: exact query] |
| Expected / actual result | [Replace: Expected—prediction before run; Actual—exact UPPAAL result] |
| Non-vacuity evidence | [Replace: exact query and result, or “Not applicable” with a concrete reason why no non-vacuity check is relevant] |
| Engineering interpretation | [Replace: what the evidence establishes/does not establish and how behaviour changed] |

## 7. AI-assisted decision

No transcript is required.

- Suggestion and basis: `[Replace: significant AI suggestion in your own words; relevant requirement/assumption.]`
- Independent decision: `[Replace: semantic/formal check; accepted, modified, or rejected; reason.]`
- Verifier evidence: `[Replace: exact UPPAAL query/result that informed the decision.]`

## 8. Final consistency and responsibility

- [ ] `WALK_TIME` and `MAX_WAIT` match in the final model, embedded queries, calculations, and report; ranges are [7, 12] and [14, 30].
- [ ] Exact queries/results are copied from their identified model versions.
- [ ] The hand trace matches the failed-model diagnostic trace and identifier.
- [ ] Failed and repaired/final versions are clearly distinguished.
- [ ] Every claim/result except clearly labelled failed-version evidence refers to the identified submitted final model; failed evidence is clearly labelled.
- [ ] Final `model.xml` embeds all mandatory, extension, and supporting queries.
- [ ] The extension genuinely changes timed behaviour.
- [ ] Submission contains exactly `model.xml` and this completed template renamed `report.md`.

**Declaration:** I, `[Replace: name]`, understand and accept responsibility for the submitted model, queries, traces, results, and interpretations, including AI-assisted work.
