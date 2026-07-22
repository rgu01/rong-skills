# Assignment: Verify a Signalised Pedestrian Crossing

## Learning objective

Build and analyse a network of timed automata in UPPAAL, connect informal
real-time requirements to verification evidence, diagnose one failed
verification run, and use AI assistance critically.

This is an **individual assignment** for one lecture. Plan to spend **2–3
hours** on the model, verification, and report together.

## Scenario and timing facts

Model an embedded controller for a signalised pedestrian crossing. The
controller coordinates vehicle traffic, an all-red clearance phase, and a
pedestrian WALK phase. A separate environment/button component represents
pedestrian requests.

Use these fixed facts throughout your model and report:

| Fact | Required value |
|---|---:|
| UPPAAL time unit | 1 second |
| Crossing width | 6 m |
| Design pedestrian speed | 1 m/s |
| Pedestrian start allowance | 1 s |
| Minimum uninterrupted vehicle-green time | 10 s |
| All-red clearance before a conflicting movement | 2 s |

Choose and justify two integer timing constants:

- `WALK_TIME` in the inclusive range **[7, 12] s**. Relate your choice to the
  supplied crossing width, design speed, and start allowance.
- `MAX_WAIT` in the inclusive range **[14, 30] s**. Explain why it is an
  appropriate service bound for your design.

The lower end of the `MAX_WAIT` range allows for a request at the least
favourable point in the cycle: clearance, the minimum vehicle-green interval,
and clearance again must all fit before WALK begins.

Use the same chosen values in the model, embedded queries, and report.

## Request and service semantics

Use the following interpretation exactly:

- A request may occur whenever WALK is inactive.
- If no request is pending, that event creates a pending request.
- Repeated button presses while a request is pending merge into the existing
  request; they do not create a queue or restart its waiting-time measurement.
- The pending request is preserved until it is served.
- The controller may enter WALK only while a request is pending; WALK must not
  occur spontaneously or as an unrequested periodic phase.
- A request is served when the controller **enters WALK**, and that entry
  clears the pending request.
- Bounded response is measured from the request event that created the pending
  request to entry into WALK. The elapsed time must not exceed `MAX_WAIT`.

State how your automata and variables represent these semantics.

## Mandatory model behaviour

Submit a network with at least two interacting timed automata:

1. an environment/button automaton capable of issuing requests as described
   above; and
2. a controller automaton.

Your controller must model vehicle, clearance, and pedestrian phases and must
enforce all of the following behaviour:

- vehicle green remains uninterrupted for at least 10 seconds before it can
  be stopped; it may last longer only if every pending request can still meet
  `MAX_WAIT`;
- after either vehicle movement or pedestrian movement is stopped, the system
  remains all-red for exactly 2 seconds before enabling the conflicting
  movement: it must neither leave clearance early nor linger there;
- a pending request remains recorded until service;
- the controller enters WALK only in response to that pending request and
  clears the request on entry;
- WALK lasts for exactly the chosen `WALK_TIME`; and
- after serving the request, the controller returns to vehicle operation.

The automata must genuinely interact, for example through synchronisation or
shared state, and the request interaction must influence the controller's
behaviour. The vehicle, clearance, and WALK phases must not be able to delay
indefinitely in a way that makes bounded response meaningless. You may add an
observer automaton, but an observer is optional. Choose your own locations,
clocks, synchronisations, and updates; justify any important modelling
decisions in the report.

## Mandatory verification evidence

Embed your verification properties in `model.xml` using the **Timed
Computation Tree Logic (TCTL)** forms supported by your UPPAAL version. For
each item below, put the exact embedded query, the exact verifier result, and
your engineering interpretation in `report.md`:

1. WALK is reachable.
2. Vehicle green and pedestrian WALK are never active simultaneously.
3. Every request issued while WALK is inactive satisfies two universal
   obligations: it is eventually served when the controller enters WALK, and
   that service occurs no later than the inclusive `MAX_WAIT` boundary,
   measured from the request event to entry into WALK. Service exactly at
   `MAX_WAIT` is allowed.
4. The model is deadlock-free.
5. At least one supporting reachability or non-vacuity check demonstrates that
   the behaviours relevant to the properties above can actually occur.

For bounded response, provide either separate universal evidence for eventual
service and the numeric deadline, or a sound combined construction and query
set that establishes both obligations. A clock bound alone is insufficient: a
request could remain unserved. If you use a combined observer, its checked
properties must expose every execution in which a request is never served or
is served late, while accepting service exactly at `MAX_WAIT`. An observer is
optional; choose your own construction and query syntax. Do not rely on a
passing universal property without checking that its trigger is reachable.

## One failed run, diagnosis, and repair

Document **one genuine failed verification run**. It may be a failure you
encounter naturally in either the core or your timed extension; you do not
need to introduce a separate fault if the extension already gives you a
suitable failure. If your initial model and extension pass, make one
controlled, relevant change, predict what it will break, and run the verifier
to produce a real failure. Restore or repair the model afterwards. Do not
invent a trace.

Choose a failed query/result for which UPPAAL supplies a diagnostic trace that
can be reconstructed. A violated universal safety, bounded-response, or
deadlock property is usually suitable. A false existential reachability query
is not suitable for the required hand-traced failure because it does not
provide the diagnostic violation trace this task requires.

Your report must include:

- the accidental defect or controlled change and your prediction;
- the exact failing query and its exact UPPAAL result;
- a record of the genuine UPPAAL diagnostic trace tied to the identified
  failed model/run and UPPAAL version: paste the relevant tool output if your
  version makes it copyable, or provide a faithful, clearly labelled
  transcription of the relevant states and transitions exactly as displayed
  in the UPPAAL simulator;
- a hand reconstruction of the shortest relevant counterexample trace or
  prefix through the violation, showing component locations, elapsed delays,
  relevant clock values, synchronisations, and important updates at each
  step; omit any irrelevant suffix;
- your diagnosis of the cause;
- the repair; and
- the exact query and result from re-verifying the repaired model.

Explain why the trace demonstrates the violation and why the repair addresses
its cause. Do not invent the diagnostic record. You do not need a separate
trace export or conversion tool, and you must not submit a third file.

## One student-designed timed extension

Add exactly one useful extension that changes the crossing's timed behaviour.
It must not merely restate a mandatory requirement or add a query to an
unchanged model. Your extension must:

- have a time-related condition or effect;
- require a concrete model change;
- be written first as a precise informal requirement;
- be formalised as a safety/invariant, liveness, or reachability property;
- include a supporting non-vacuity check where relevant; and
- be verified and interpreted using UPPAAL evidence.

Night operation, an audible signal, button debouncing, and bounded bus
priority are example **categories, not specifications**. If you use one, you
must define its precise timed behaviour and property yourself. Keep the
extension small enough to complete and verify within the assignment time.

## AI-assisted work

AI assistance is allowed and expected. Select one significant AI suggestion
that affected your modelling or verification work. In the report, record:

- the suggestion in your own words;
- the relevant requirement or assumption;
- how you checked it independently;
- whether you accepted, modified, or rejected it, and why; and
- the UPPAAL evidence that informed your decision.

An AI transcript is not required. AI output is not verification evidence; you
remain responsible for the model, queries, results, and interpretations.

## Suggested workflow and timebox

Use this compact allocation as a guide:

1. Fix the semantics and justify `WALK_TIME` and `MAX_WAIT`: about 15 minutes.
2. Build the two-automaton core: 40–50 minutes.
3. Add and run the mandatory verification properties: 25–30 minutes.
4. Capture, reconstruct, diagnose, and repair one failed run: 20–25 minutes.
5. Add and verify exactly one small timed extension: 25–30 minutes.
6. Complete the report and final consistency check: 15–20 minutes.

Timebox the work. Once you have evidence for the core, one failed-run repair,
and one extension, **stop expanding the model** and finish the report. The
report template is supplied separately alongside this assignment.

Keep the report concise: target approximately three pages, plus diagnostic and
hand-trace material or tables as needed. Prioritise exact evidence over prose.

## Submission

Submit exactly these two files:

- `model.xml`: the final runnable UPPAAL XML model, including all verification
  queries embedded in the model; and
- `report.md`: the supplied report template completed and renamed.

Before submitting, open `model.xml` in UPPAAL, run the embedded queries again,
and confirm that the model, chosen constants, reported results, and names used
in `report.md` are consistent.
