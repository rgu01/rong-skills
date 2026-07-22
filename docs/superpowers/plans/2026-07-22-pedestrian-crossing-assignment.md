# Pedestrian-Crossing Assignment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a standalone student assignment and teacher grading package for a two-to-three-hour individual UPPAAL pedestrian-crossing exercise.

**Architecture:** Place distributable student material under `student/` and confidential assessment material under `teacher/`. Use the student report template as the common interface: the assignment tells students what evidence to enter, while every teacher check and pass criterion points to a specific report section.

**Tech Stack:** Markdown, UPPAAL networks of timed automata and embedded Timed Computation Tree Logic queries, repository shell checks with `rg` and `git diff --check`.

---

### Task 1: Write the student assignment instruction

**Files:**
- Create: `experiments/Course-Embedded-System-II/pedestrian-crossing-assignment/student/assignment.md`

- [ ] **Step 1: Create the student directory**

Run:

```bash
mkdir -p experiments/Course-Embedded-System-II/pedestrian-crossing-assignment/student
```

Expected: the directory exists and contains no assignment file yet.

- [ ] **Step 2: Write the scenario and fixed timing context**

Write an assignment introduction that states:

- individual work, expected effort of two to three hours;
- one time unit equals one second;
- crossing width is 6 metres;
- design pedestrian speed is 1 metre per second;
- pedestrian start allowance is 1 second;
- minimum uninterrupted vehicle green is 10 seconds;
- all-red clearance is exactly 2 seconds before a conflicting movement;
- students choose `WALK_TIME` in `[7,12]` seconds and `MAX_WAIT` in `[14,30]` seconds.

Explain that the 14-second lower bound for `MAX_WAIT` covers the
least-favourable path of 2 seconds clearance + 10 seconds minimum vehicle green
+ 2 seconds clearance before WALK begins.

Explain that a request may occur whenever WALK is inactive, repeated presses
while one request is pending merge without resetting its wait measurement, and
the pending request must be preserved until entry into WALK serves and clears
it. WALK must be request-driven.

- [ ] **Step 3: Write the mandatory modelling and verification work**

Require at least a controller and environment/button timed automaton, while allowing an observer. Require embedded UPPAAL queries and report evidence for:

```text
WALK reachability
no simultaneous vehicle green and pedestrian WALK
universal eventual service at WALK entry for every request issued while WALK is inactive
service no later than the inclusive MAX_WAIT boundary, using separate universal evidence or a sound combined construction
deadlock freedom
supporting reachability/non-vacuity
```

Describe outcomes rather than prescribing location names or one automaton topology.

- [ ] **Step 4: Write the failure-repair, extension, and AI requirements**

Require one genuine failed run, a prediction, an UPPAAL counterexample, a hand trace, diagnosis, repair, and re-verification. Require exactly one student-designed timed extension that changes timed behavior and is formalised as a safety/invariant, liveness, or reachability property with a non-vacuity check. Require one significant AI suggestion and an explanation of its independent validation.

- [ ] **Step 5: Write the submission and timebox instructions**

Require:

```text
model.xml   one runnable final UPPAAL model with embedded queries
report.md   the completed supplied report template
```

Tell students to stop expanding the model after the core, one failed-run repair, and one extension are evidenced.

- [ ] **Step 6: Check the assignment for accidental solution disclosure**

Run:

```bash
rg -n "complete solution|use exactly|must name|golden model" experiments/Course-Embedded-System-II/pedestrian-crossing-assignment/student/assignment.md
```

Expected: no matches. Review example extension categories to ensure they do not specify a complete automaton and query.

- [ ] **Step 7: Commit the student assignment**

```bash
git add experiments/Course-Embedded-System-II/pedestrian-crossing-assignment/student/assignment.md
git commit -m "docs: add pedestrian crossing assignment"
```

### Task 2: Write the structured student report template

**Files:**
- Create: `experiments/Course-Embedded-System-II/pedestrian-crossing-assignment/student/report-template.md`

- [ ] **Step 1: Add identity, constants, and requirement interpretation tables**

Include fields for student name, UPPAAL version, chosen `WALK_TIME`, chosen `MAX_WAIT`, calculation/rationale, and explicit interpretations of request, service, green conflict, and clearance.

- [ ] **Step 2: Add the model architecture table**

Use columns:

```text
Template | Responsibility | Locations/modes | Clocks and variables | Interactions
```

Add short prompts asking how requests are stored and how each timing interval is forced.

- [ ] **Step 3: Add the requirement traceability matrix**

Use columns:

```text
ID | Informal requirement | Operational interpretation | Exact embedded query | Expected result | Actual result | Engineering meaning/non-vacuity evidence
```

Pre-create rows for reachability, conflicting greens, bounded response, deadlock freedom, and supporting non-vacuity. Do not pre-fill formulas that depend on student location names.

- [ ] **Step 4: Add the failed-run and hand-trace tables**

Collect the changed condition, prediction, exact query, actual result, trace source, and a genuine diagnostic trace record as pasted output or a faithful, provenance-labelled transcription of the relevant UPPAAL simulator sequence. Keep this record in `report.md`; require no separate export/conversion tool or third submission file. Collect diagnosis, repair, and re-verification separately. Use a hand-trace table for the student's semantic expansion with:

```text
Step | Delay/action | Component locations | Relevant clock values | Synchronisation/updates | Why enabled
```

- [ ] **Step 5: Add extension and AI-decision sections**

For the extension, collect informal requirement, timed behavior, model delta, property class, exact query, non-vacuity query, result, and interpretation. For AI use, collect suggestion, relevant requirement, independent check, decision, and UPPAAL evidence.

- [ ] **Step 6: Add a concise final self-check**

Require affirmative checks that constants match, query results are copied from UPPAAL, the hand trace matches the failed model version, the final model contains embedded queries, and all report claims refer to the submitted model except the clearly labelled failed version.

- [ ] **Step 7: Verify template-to-assignment coverage**

Run:

```bash
rg -n "WALK_TIME|MAX_WAIT|counterexample|hand trace|non-vacu|AI|extension|embedded" experiments/Course-Embedded-System-II/pedestrian-crossing-assignment/student/{assignment.md,report-template.md}
```

Expected: every concept appears in both files with compatible terminology.

- [ ] **Step 8: Commit the report template**

```bash
git add experiments/Course-Embedded-System-II/pedestrian-crossing-assignment/student/report-template.md
git commit -m "docs: add structured assignment report template"
```

### Task 3: Write the teacher grading guide and expected solution shape

**Files:**
- Create: `experiments/Course-Embedded-System-II/pedestrian-crossing-assignment/teacher/grading-guide.md`
- Create: `experiments/Course-Embedded-System-II/pedestrian-crossing-assignment/teacher/expected-solution-shape.md`

- [ ] **Step 1: Create the confidential teacher directory**

Run:

```bash
mkdir -p experiments/Course-Embedded-System-II/pedestrian-crossing-assignment/teacher
```

- [ ] **Step 2: Write the report-first grading workflow**

In `grading-guide.md`, specify this order:

```text
1. Read constants and interpretations.
2. Inspect architecture and request handling.
3. Follow each traceability row from requirement to meaning.
4. Check the failed trace, diagnosis, and repair causally agree.
5. Check that the extension changes timed behavior.
6. Check that the AI contribution was independently evaluated.
7. Decide pass or revision from the essential outcomes.
8. Run model.xml only if desired or if evidence is inconsistent.
```

State explicitly that fluent prose and attractive diagrams are not substitutes for evidence.

- [ ] **Step 3: Add optional UPPAAL spot-check instructions**

Tell teachers to verify that the model loads, queries are embedded, results agree with the report, and reported state/location names exist. Explain that a spot-check is diagnostic and does not replace holistic report assessment.

- [ ] **Step 4: Write acceptable solution families**

In `expected-solution-shape.md`, describe a minimal credible controller/environment decomposition, typical phase progression, request-memory choices, query-relative observer-based bounded response, suitable query patterns, and why no single XML structure is required. Require universal eventual-service and inclusive numeric-deadline evidence, separately or through a sound combined construction.

- [ ] **Step 5: Write common failure and vacuity patterns**

Include:

```text
environment cannot actually issue a request
WALK is unreachable, making safety trivial
request predicate disappears before a leads-to query can observe it
MAX_WAIT is stated but not enforced or monitored
clearance exists as a location but time need not elapse there
deadlock freedom is claimed without a query
counterexample locations or clocks do not exist in the described model
extension adds only a query and no timed behavior
```

- [ ] **Step 6: Write examples of extension quality without giving solutions**

Contrast acceptable extensions, which have a precise timed behavior and model delta, with insufficient ones such as renaming a state, changing only a constant, or adding an unrelated reachability query.

- [ ] **Step 7: Commit the teacher guide and reference**

```bash
git add experiments/Course-Embedded-System-II/pedestrian-crossing-assignment/teacher/{grading-guide.md,expected-solution-shape.md}
git commit -m "docs: add assignment grading guidance"
```

### Task 4: Write checking points and pass criteria

**Files:**
- Create: `experiments/Course-Embedded-System-II/pedestrian-crossing-assignment/teacher/checking-points.md`
- Create: `experiments/Course-Embedded-System-II/pedestrian-crossing-assignment/teacher/pass-criteria.md`

- [ ] **Step 1: Build a report-order checking sheet**

In `checking-points.md`, create a compact table with columns:

```text
Report section | Checking point | Satisfactory evidence | Concern requiring model spot-check | Outcome
```

Cover every report section exactly once in reading order. Use `OK`, `Concern`, and `Missing` as the allowed outcome marks.

- [ ] **Step 2: Define the seven essential pass outcomes**

In `pass-criteria.md`, define requirements, model, properties, evidence, diagnosis/repair, extension, and AI judgment as essential outcomes. For each, state observable evidence and revision triggers.

- [ ] **Step 3: Define holistic pass/revision decision rules**

Specify:

```text
PASS: all seven essential outcomes are demonstrated; minor defects do not break the evidence chain.
REVISION: one or more essential outcomes are missing, contradicted, vacuous, fabricated, or cannot be connected to the requirement.
```

Do not use a numerical point total. Explain that an optional model run may confirm a concern but is not mandatory for an otherwise coherent report.

- [ ] **Step 4: Map criteria back to report headings**

Run:

```bash
rg '^## ' experiments/Course-Embedded-System-II/pedestrian-crossing-assignment/student/report-template.md
rg '^## ' experiments/Course-Embedded-System-II/pedestrian-crossing-assignment/teacher/{checking-points.md,pass-criteria.md}
```

Expected: each substantive student report heading has an explicit teacher checkpoint, and each pass outcome points to one or more report headings.

- [ ] **Step 5: Commit the assessment criteria**

```bash
git add experiments/Course-Embedded-System-II/pedestrian-crossing-assignment/teacher/{checking-points.md,pass-criteria.md}
git commit -m "docs: define assignment pass criteria"
```

### Task 5: Cross-document verification and handoff

**Files:**
- Verify: `experiments/Course-Embedded-System-II/pedestrian-crossing-assignment/student/assignment.md`
- Verify: `experiments/Course-Embedded-System-II/pedestrian-crossing-assignment/student/report-template.md`
- Verify: `experiments/Course-Embedded-System-II/pedestrian-crossing-assignment/teacher/grading-guide.md`
- Verify: `experiments/Course-Embedded-System-II/pedestrian-crossing-assignment/teacher/checking-points.md`
- Verify: `experiments/Course-Embedded-System-II/pedestrian-crossing-assignment/teacher/pass-criteria.md`
- Verify: `experiments/Course-Embedded-System-II/pedestrian-crossing-assignment/teacher/expected-solution-shape.md`

- [ ] **Step 1: Check fixed facts are identical everywhere**

Run:

```bash
rg -n "6 metres|1 metre per second|1 second|10 seconds|2 seconds|7.*12|14.*30" experiments/Course-Embedded-System-II/pedestrian-crossing-assignment
```

Expected: student files state all facts; teacher references repeat them only where needed and never contradict them.

- [ ] **Step 2: Scan for placeholders and accidental teacher leakage**

Run:

```bash
rg -n "TBD|TODO|FIXME|placeholder|golden XML|expected counterexample sequence" experiments/Course-Embedded-System-II/pedestrian-crossing-assignment
```

Expected: no unresolved placeholders; student files contain no answer-specific teacher hints.

- [ ] **Step 3: Check Markdown and whitespace quality**

Run:

```bash
git diff --check -- experiments/Course-Embedded-System-II/pedestrian-crossing-assignment
```

Expected: no output.

- [ ] **Step 4: Perform a workload audit**

Read `student/assignment.md` and confirm the required work is exactly:

```text
one small core model
five categories of core verification evidence
one failed-run diagnosis and repair
one timed extension
one AI-assisted decision
one concise structured report
```

Remove any extra mandatory task discovered during the audit.

- [ ] **Step 5: Perform a grading-path audit**

Read a blank report template alongside `checking-points.md`. Confirm a teacher can decide pass/revision from the completed fields without routinely opening `model.xml`.

- [ ] **Step 6: Commit any verification corrections**

```bash
git add experiments/Course-Embedded-System-II/pedestrian-crossing-assignment
git commit -m "docs: align assignment and grading materials"
```

If verification requires no corrections, do not create an empty commit.
