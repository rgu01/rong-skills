# Pass criteria

> **Confidential teacher material. Do not distribute to students.**

Assess the submission as **pass** or **revision needed**, without numerical points. Follow the evidence chain from requirement through operational interpretation, model mechanism, exact query, actual UPPAAL evidence, and engineering meaning. There is no golden model or required automaton topology, and polished prose is not required when the technical chain is clear.

## Requirements — report sections 2, 4, and 6

- **Observable report evidence:** The report states the fixed timing facts and selected integer constants; gives `WALK_TIME` in [7, 12] s and `MAX_WAIT` in [14, 30] s with calculations; defines request, merged repeats, pending preservation, service at WALK entry, the inclusive wait boundary, exact phase timing, and one precise timed-extension requirement; and connects R1–R5 and the extension property to those requirements.
- **Minor defects tolerated:** A small notation slip or concise rationale is acceptable when the intended requirement is unique and all mechanisms, queries, and results use it consistently.
- **Revision triggers:** A mandatory semantic or timing requirement is absent or contradicted; the least-favourable wait path is incompatible with the selected bound; service is measured to the wrong endpoint; or a claimed property cannot be connected to a stated requirement.

## Model — report sections 2, 3, 6, and 8

- **Observable report evidence:** Concrete environment/button and controller structures, locations, clocks, variables, interactions, guards, invariants, and updates implement the stated request and phase behaviour; the request changes controller behaviour; optional observer and extension structures have explained roles; the final consistency record links these names to one model.
- **Minor defects tolerated:** Unusual topology, naming, decomposition, shared-state use, or an omitted nonessential structural detail is acceptable when behaviour and evidence remain unambiguous.
- **Revision triggers:** The report describes no credible interacting model; requests are unreachable, lost, reset, or irrelevant; WALK can occur spontaneously; exact-duration or bounded-delay mechanisms are incompatible with the claims; or model names and mechanisms cannot be reconciled across the report.

## Properties — report sections 4 and 8

- **Observable report evidence:** R1–R5 provide exact embedded Timed Computation Tree Logic (TCTL) queries, actual results, meanings, and non-vacuity support. R1 reaches WALK; R2 universally excludes simultaneous vehicle green and WALK; R4 explicitly checks network deadlock freedom; R5 reaches relied-on triggers and behaviours. R3 proves two obligations for every newly pending request: universal eventual service at WALK entry and service no later than the inclusive `MAX_WAIT` boundary, either with separate universal queries or one sound combined construction. Observer soundness is judged relative to the checked query, including complete detection of relevant unserved/late paths and no erroneous timeout race against valid service at equality.
- **Minor defects tolerated:** Conservative imprecision in explaining a query's limits is acceptable when the formula, result, trigger reachability, and required guarantee are otherwise correct.
- **Revision triggers:** A mandatory property or actual result is missing; a passing property is vacuous; R3 supplies only a numeric clock invariant, unbounded liveness, or existential service; timeout/equality handling invalidates the bound; or a query does not establish the requirement attributed to it.

## Evidence — report sections 1, 4, 5, 6, and 8

- **Observable report evidence:** The stated UPPAAL version is exact; queries and genuine exact UPPAAL results are copied from identified runs/models; the failed run includes a tool-produced diagnostic excerpt and a plausible hand-reconstructed trace with defensible delays, locations, clock values, synchronisations, and updates; failed, repaired, extension, and final evidence are linked to the correct model versions.
- **Minor defects tolerated:** A diagnostic excerpt may omit an irrelevant suffix, and a hand trace may omit irrelevant state, provided the shortest relevant prefix still proves the violation and its values can be derived.
- **Revision triggers:** There is no real tool evidence; evidence is fabricated or impossible; a supposed counterexample comes from a false existential reachability query; reported values cannot arise from the cited model; or final-model and failed-model queries/results are mixed so provenance cannot be recovered.

## Diagnosis and repair — report section 5

- **Observable report evidence:** A prediction precedes a genuine failed run; the trace is explained causally; the diagnosis identifies the modelling defect; the repair changes that cause; and the exact relevant query is rerun with its actual result on an identified repaired/final version.
- **Minor defects tolerated:** The trace need not be globally shortest or beautifully formatted when it is a concise relevant prefix and contains enough state and timing evidence to justify the causal account.
- **Revision triggers:** The failure is invented or unsuitable for diagnostic reconstruction; the diagnosis merely restates the failed requirement; the repair is unrelated to the traced cause; or re-verification is absent or tied to the wrong version.

## Timed extension — report sections 3, 6, and 8

- **Observable report evidence:** Exactly one useful timed extension states a precise requirement and purpose, changes the model's timed behaviour through a concrete delta, uses a matching safety/invariant, liveness, or reachability query with actual result, supplies relevant non-vacuity evidence, and interprets what changed.
- **Minor defects tolerated:** A small extension and a familiar category are acceptable; novelty is not required, and non-vacuity may be marked inapplicable when the report gives a sound concrete reason.
- **Revision triggers:** The extension makes no behavioural model change, merely changes a constant/name/query, restates a core requirement, has an unreachable trigger/outcome, or disconnects its requirement, mechanism, property, and evidence.

## AI judgment — report sections 1, 7, and 8

- **Observable report evidence:** One concrete artificial intelligence (AI) suggestion is stated in the student's words, checked independently against a named requirement or assumption and exact verifier evidence, and accepted, modified, or rejected with a technical reason; tools are declared consistently.
- **Minor defects tolerated:** The suggestion may be simple and no transcript is needed when the student's independent check and judgment are specific.
- **Revision triggers:** The account is a generic statement that AI helped, substitutes a transcript or AI assertion for verification, or contains no independent technical judgment tied to the model and evidence.

## Holistic decision

**PASS** if all seven essential outcomes are demonstrated and minor defects do not break the evidence chain.

**REVISION** if one or more essential outcomes are missing, contradicted, vacuous, fabricated, or cannot connect to a requirement.

Hard revision cases include a fabricated or impossible trace; no real tool evidence; a vacuous proof presented as a guarantee; mixed final-model and result versions; a timed extension with no behaviour change; or a generic AI statement without independent judgment. Do not require one topology or perfect prose.

An optional final `model.xml` run may confirm a concern but is not mandatory when the report is coherent. If XML contradicts the report, record the exact contradiction as evidence and apply the holistic rules. The responsibility declaration in section 8 is a consistency signal, not a substitute for evidence.
