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
- `MAX_WAIT` in the inclusive range **[12, 30] s**. Explain why it is an
  appropriate service bound for your design.

Use the same chosen values in the model, embedded queries, and report.

## Request and service semantics

Use the following interpretation exactly:

- A request may occur whenever WALK is inactive.
- If no request is pending, that event creates a pending request.
- Repeated button presses while a request is pending merge into the existing
  request; they do not create a queue or restart its waiting-time measurement.
- The pending request is preserved until it is served.
- A request is served when the controller **enters WALK**.
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
  be stopped;
- after either vehicle movement or pedestrian movement is stopped, the system
  remains all-red for 2 seconds before enabling the conflicting movement;
- a pending request remains recorded until service;
- WALK lasts for the chosen `WALK_TIME`; and
- after serving the request, the controller returns to vehicle operation.

The automata must genuinely interact, for example through synchronisation or
shared state. You may add an observer automaton, but an observer is optional.
Choose your own locations, clocks, synchronisations, and updates; justify any
important modelling decisions in the report.

## Mandatory verification evidence

Embed your verification properties in `model.xml` using the **Timed
Computation Tree Logic (TCTL)** forms supported by your UPPAAL version. For
each item below, put the exact embedded query, the exact verifier result, and
your engineering interpretation in `report.md`:

1. WALK is reachable.
2. Vehicle green and pedestrian WALK are never active simultaneously.
3. Every request issued while WALK is inactive is served within `MAX_WAIT`,
   measured from the request event to entry into WALK.
4. The model is deadlock-free.
5. At least one supporting reachability or non-vacuity check demonstrates that
   the behaviours relevant to the properties above can actually occur.

For bounded response, you may introduce an observer that measures from the
request event and enters an error or timeout location if the bound is missed;
you can then verify the required outcome for that location. This is only a
possible technique: design the observer and the corresponding query yourself.
Do not rely on a passing universal property without checking that its trigger
is reachable.

## One failed run, diagnosis, and repair

Document **one genuine failed verification run**. It may be a failure you
encounter naturally. If your initial model passes, make a controlled, relevant
change to the core model or your added function, predict what it will break,
and run the verifier to produce a real failure. Restore or repair the model
afterwards. Do not invent a trace.

Your report must include:

- the accidental defect or controlled change and your prediction;
- the exact failing query and its exact UPPAAL result;
- the genuine UPPAAL counterexample;
- a hand reconstruction of the counterexample, showing component locations,
  elapsed delays, relevant clock values, synchronisations, and important
  updates at each step;
- your diagnosis of the cause;
- the repair; and
- the exact query and result from re-verifying the repaired model.

Explain why the trace demonstrates the violation and why the repair addresses
its cause.

## One student-designed timed function

Add one useful function that changes the crossing's timed behaviour. It must
not merely restate a mandatory requirement or add a query to an unchanged
model. Your function must:

- have a time-related condition or effect;
- require a concrete model change;
- be written first as a precise informal requirement;
- be formalised as a safety/invariant, liveness, or reachability property;
- include a supporting non-vacuity check where relevant; and
- be verified and interpreted using UPPAAL evidence.

Night operation, an audible signal, button debouncing, and bounded bus
priority are example **categories, not specifications**. If you use one, you
must define its precise timed behaviour and property yourself. Keep the
function small enough to complete and verify within the assignment time.

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

1. Fix and justify `WALK_TIME` and `MAX_WAIT`.
2. Build the two-automaton core and verify the mandatory properties.
3. Capture and repair one genuine failed run.
4. Add and verify one small timed function.
5. Complete the report and final consistency check.

Timebox the work. Once you have evidence for the core, one failed-run repair,
and one extension, **stop expanding the model** and finish the report.

## Submission

Submit exactly these two files:

- `model.xml`: the final runnable UPPAAL XML model, including all verification
  queries embedded in the model; and
- `report.md`: the supplied report template completed and renamed.

Before submitting, open `model.xml` in UPPAAL, run the embedded queries again,
and confirm that the model, chosen constants, reported results, and names used
in `report.md` are consistent.
