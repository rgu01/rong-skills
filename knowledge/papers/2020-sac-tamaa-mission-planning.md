---
id: gu2020sac-tamaa
title: "TAMAA: UPPAAL-based Mission Planning for Autonomous Agents"
authors:
  - Rong Gu
  - Eduard Enoiu
  - Cristina Seceleanu
affiliation: Mälardalen University, Västerås, Sweden
year: 2020
venue: SAC'20
venue_source: author's publications page (the PDF does not name the venue)
doi: null
document_type: conference paper
pages_in_pdf: 11
pdf_url: https://drive.google.com/file/d/1TTJi3mV6MoitayW70hbJsS6utTAyz7dA/view?usp=sharing
listing_url: https://sites.google.com/view/ronggu/publications
author_keywords: [autonomous agents, mission planning, UPPAAL]
topics: [mission planning, plan synthesis, model checking, autonomous vehicles, construction machinery, path planning, task scheduling, multi-agent systems, requirement formalization, model generation, tool integration]
formalisms: [timed automata, TCTL, CTL]
tools: [UPPAAL, TAMAA, MMT, Apache Thrift]
algorithms: [Theta*]
application: autonomous wheel loaders in a quarry
abbreviations: {TAMAA: Timed-Automata-based Planner for Multiple Autonomous Agents, AWL: autonomous wheel loader, AA: automated agent, TA: timed automata, TCTL: Timed Computation Tree Logic, CTL: Computation Tree Logic, MMT: Mission Management Tool, VCE: Volvo Construction Equipment, LTL: Linear Temporal Logic}
funding: DPAC project, Swedish Knowledge Foundation, grant 20150022
---

# TAMAA: UPPAAL-based Mission Planning for Autonomous Agents (Gu et al., SAC 2020)

## At a glance

This 2020 paper by Gu, Enoiu, and Seceleanu presents TAMAA, a tool that
synthesizes mission plans for autonomous vehicles with the UPPAAL model
checker. A mission plan is a path through milestones plus a schedule of
tasks. TAMAA computes travel times between milestones with Theta*. It then
generates timed automata for the movement, the tasks, and monitors for
events such as low battery. UPPAAL checks the model against TCTL queries.
TAMAA reads the witness trace back as a plan and shows it in the Mission
Management Tool (MMT). The paper implements the static layer of the
authors' two-layer framework. It evaluates TAMAA on autonomous wheel loader
(AWL) scenarios from Volvo Construction Equipment. One agent with 100
milestones and 100 tasks takes 14 s for reachability. Four agents run out
of memory for invariance, and five run out for reachability.

Page references `[p. N]` point to the 11-page PDF.

## Key facts

Each fact is a claim from the paper unless it is marked otherwise.

- TAMAA stands for "Timed-Automata-based Planner for Multiple Autonomous
  Agents". [p. 1]
- TAMAA covers only the static layer of the authors' two-layer framework:
  path planning and task scheduling. [p. 1]
- TAMAA assumes that the dynamic layer handles dynamic obstacles correctly,
  including overlapping paths of several vehicles. [p. 3]
- The TAMAA use case comes from Volvo Construction Equipment: AWLs dig,
  carry, load, and unload stones in a quarry and charge when the battery is
  low. [p. 1, p. 3]
- The TAMAA requirements have five categories: task coverage, task
  matching, task sequencing, timing, and event reaction. [p. 3]
- TAMAA models the environment as a weighted graph of milestones. Theta* on
  a Cartesian grid gives the travel time of each edge. [p. 4, p. 6]
- TAMAA builds a network of a movement automaton, a task automaton, and one
  monitor automaton per event. [p. 6]
- In TAMAA, the agent can move only during the no-op task T0. [p. 5, p. 7]
- TAMAA gets a mission plan from the diagnostic trace that UPPAAL produces
  for a satisfied reachability query. [p. 8]
- TAMAA is written in Java. It talks to MMT through Apache Thrift and calls
  UPPAAL on the command line with an XML model. [p. 8–9]
- The TAMAA evaluation runs on an Intel Core i5 with 16 GB of RAM and a
  64-bit Windows OS. [p. 9]
- In the TAMAA charging scenario, a query of the timing form explores
  113,719 states in 0.5 seconds. [p. 9]
- For one TAMAA agent, 100 milestones and 100 tasks take 14 s for
  reachability (712,721 states) and 29 s for invariance (1,429,903 states).
  [p. 9]
- For TAMAA with several agents, reachability runs out of memory at five
  agents and invariance at four agents. [p. 9]
- The TAMAA authors say that partial order reduction does not suit the
  model, because the model uses clocks at locations and edges. [p. 10]

## Questions this paper answers

**What does TAMAA do?** It generates timed automata from a mission
configuration, verifies them in UPPAAL, and turns the witness trace into a
mission plan. If no valid plan exists, it shows a counterexample in MMT.
[p. 2, p. 9]

**What does the user do?** The user formalizes the requirements as CTL/TCTL
queries and configures the environment and tasks in MMT. All other steps are
automatic. [p. 3]

**Which tool and logic does it use?** UPPAAL with timed automata, and
queries in the UPPAAL subset of CTL/TCTL. [p. 2]

**How does it put path planning into the model?** Theta* runs before model
generation. It computes the travel time between each pair of milestones on
a grid. The automata use these times as clock bounds. [p. 6]

**How are the requirements checked?** Task coverage and timing become
reachability queries. Task sequencing becomes a reachability query plus an
invariance query. Task matching holds by construction. Event reaction
follows from the coverage and timing queries through a deadlock argument.
[p. 8]

**Is the plan optimal?** The authors say a valid plan is correct and
optimal, because it comes from exhaustive model checking. [p. 2] UPPAAL can
return some trace, the shortest trace, or the fastest trace. [p. 8]

**How well does it scale?** Well in the number of milestones and tasks for
one agent, and badly in the number of agents. [p. 9–10]

## Scope: what this paper does not do

- It does not model vehicle dynamics or kinematics. Movement and tasks are
  only time durations. [p. 4]
- It does not handle dynamic or unforeseen obstacles. That is the job of the
  dynamic layer. [p. 3]
- It does not use feedback from the environment during execution. The agent
  is an "automated agent" that follows its plan. [p. 4]
- It does not model events that change in a non-monotonic way. All events
  concern indices that change monotonically and continuously. [p. 6]
- It does not prove the model-generation algorithms correct.
- It does not combine TAMAA with the dynamic layer. That is future work.
  [p. 10]
- It names no DOI and no venue inside the PDF.

## Requirements in natural language

These are the requirement categories from the industrial partner. [p. 3]

1. **Task coverage.** The AWL must execute all tasks and repeat them until
   the final goal is reached, for example until all stones are at the
   secondary crusher.
2. **Task matching.** The AWL must do a given task at its given milestone,
   for example digging only at stone piles.
3. **Task sequencing.** The order of task execution must be correct.
4. **Timing.** The AWL must finish the tasks within a given time, for
   example digging and carrying a ton of stones in 0.5 hours.
5. **Event reaction.** Some tasks start only on events. For example, a low
   battery level makes the AWL go to the charging point.

The overall challenge assumes one or more AWLs with accurate speed control
and a deterministic speed range, predefined milestones, and static
obstacles. [p. 3]

## Formal definitions

| Definition | Tuple | Content |
|---|---|---|
| Automated agent (Def. 1) | `AA = <S, M, T>` | Speed, motion primitives, tasks [p. 4] |
| Environment | `G = (Vg, Eg)` | Weighted graph; vertices are milestones; edge weights are travel times [p. 4] |
| Movement (Def. 2) | `Mm = <P, p0, xm, Am, Em, Im>` | Locations for vertices and for transitions between them; clock `xm`; action `move`; guards `xm >= ϒ`; invariants `xm <= ϒ` [p. 4–5] |
| Task (Def. 3) | `Task = (B, W, ∆, S, F, R, O, M, V, G)` | Best and worst execution time, elapsed time, start and finish flags, precondition, postcondition, allowed milestones, changed variables, triggering events [p. 5] |
| Task execution (Def. 4) | `Taa = (N, l0, xe, Ae, Ve, Ee, Ie, Me)` | One location per task; `l0` is the no-op task; every edge goes between `l0` and a task location [p. 5] |

Rules that the definitions set: [p. 5–6]

- `B <= ∆ <= W` for each task.
- The precondition is `Ti.R = θt(T0.F, ..., Tk.F) ∧ θe(ev0, ..., evm)`. It
  combines the order of tasks and the status of events.
- The postcondition clears the triggering events and sets `Ti.F`.
- The no-op task is `T0(0, ∞+, ∆, S, F, ∅, ∅, M, ∅, ∅)`. It is allowed at
  every milestone and has no time limit.
- The guard into a task is "at a milestone in `Ti.M`" and `Ti.R`. The
  guard out of a task is `xe >= Ti.B`. The invariant is `xe <= Ti.W`.

## Model generation

**Algorithm 1, movement automaton.** TAMAA puts the environment on a
Cartesian grid and runs Theta* between each pair of milestones. The results
go into an integer array `tt`. For each pair with `tt < MAX`, the algorithm
adds an intermediate location with the bound `c <= tt[A][B]`. It adds edges
in both directions with the channel `move?`, a clock reset, and the guard
`c >= tt`. The edges update the arrays `position` and `visited`. [p. 6–7]

**Grid abstraction.** Cells that obstacles occupy completely or partly are
forbidden. The authors call this conservative: it causes unnecessary
avoidance. A finer grid helps but can increase the computation time. [p. 7]

**Algorithm 2, task automaton.** The initial location `l0` is the no-op task
with a self-loop on `move!`. Each task gets a location with the invariant
`c <= Ti.W`. The edge from `l0` has the milestone-and-precondition guard. The
edge back to `l0` has the guard `c >= Ti.B` and, for event tasks, the
channel `done[i]!`. [p. 7]

**Monitor automaton.** A monitor has the locations M0, M1, and Stop. The
event becomes true when a clock reaches a threshold. The agent must react
before a deadline, or the monitor goes to Stop and the model deadlocks. The
deadlock stands for an agent without energy. [p. 6]

## Query design

| Requirement | Query | Kind |
|---|---|---|
| Task coverage | `E<> (F[1] ∧ F[2] ∧ ... ∧ F[j] ∧ stonePileVol == 0)` (5) | Reachability; the witness trace gives the plan |
| Task matching | none | Holds by the guards of the task automaton |
| Task sequencing | `E<> S[i+1]` (6) and `A[] S[i+1] imply F[i]` (7) | Reachability, then invariance |
| Timing | `E<> (F[1] ∧ ... ∧ F[j] ∧ stonePileVol == 0 ∧ c <= N)` (8) | Reachability with a clock bound |
| Event reaction | none separate | A deadlock in a monitor makes (5) and (8) unsatisfiable |

Source: Section 3.4.4. [p. 8]

## Tool architecture

| Module | Role |
|---|---|
| A | Communicates with UPPAAL: runs model checking and parses the trace |
| B | Generates the timed automata as an XML file and turns the trace into a plan |
| C | Communicates with MMT through Apache Thrift |

Source: Section 4.1 and Fig. 8. [p. 8–9] TAMAA appears in MMT as a planner
option. The user places milestones by drag and drop and assigns tasks to
them. [p. 8]

## Applicability results

All scenarios use a 50 × 50 2D space with 3 static obstacles and 4
milestones. [p. 9]

| Scenario | Content | Result |
|---|---|---|
| 1 | One AWL does 3 tasks in order, one round | All queries of the forms (5)–(8) pass; a few milliseconds |
| 2 | One AWL repeats four tasks until the pile is empty and charges on a low-battery event | Query of form (8): 0.5 s, 113,719 states; the trace reacts to the event in time |
| 3 | Three AWLs meet at one milestone, start one task together, then do their own tasks | Queries (5)–(8) pass; invariance (7) under 9 s, more than 770,000 states |

Source: Section 4.2. [p. 9]

## Scalability results

**One agent, more milestones and tasks (Table 1).** [p. 9]

| Query | Milestones | Tasks | Explored states | Time |
|---|---|---|---|---|
| Reachability | 30 | 30 | 20,363 | 0.2 s |
| Reachability | 60 | 60 | 157,033 | 2.2 s |
| Reachability | 100 | 100 | 712,721 | 14 s |
| Invariance | 30 | 30 | 41,193 | 0.3 s |
| Invariance | 60 | 60 | 317,703 | 4.5 s |
| Invariance | 100 | 100 | 1,429,903 | 29 s |

**More agents, 3 tasks among 3 milestones (Table 2).** The setup is
Scenario 3. [p. 9]

| Query | Agents | Explored states | Time |
|---|---|---|---|
| Reachability | 2 | 1,661 | 0.01 s |
| Reachability | 3 | 159,632 | 2.0 s |
| Reachability | 4 | 2,058,132 | 20160 s |
| Reachability | 5 | Out of memory | Out of memory |
| Invariance | 2 | 3,533 | 0.03 s |
| Invariance | 3 | 344,701 | 4.0 s |
| Invariance | 4 | Out of memory | Out of memory |

The queries are (5) for reachability and (7) for invariance. [p. 9] The
authors explain the growth with agents by more automata and clocks, more
time zones, and more interleaving. [p. 9–10]

## Limitations stated by the authors

- More than three agents is "problematic" because of computation time and
  explored states. [p. 10]
- Partial order reduction does not suit the model, because of the clocks.
  [p. 10]
- The grid abstraction is conservative and causes unnecessary avoidance.
  [p. 7]

## Future work stated by the authors

- Combine model checking with machine learning, for example reinforcement
  learning, to use the history of state-space exploration and so improve
  scalability. [p. 10]
- Integrate TAMAA with the two-layer framework, for static planning plus
  dynamic simulation and verification with agent dynamics and kinematics.
  [p. 10]

## Related work, as the paper positions itself

Earlier work uses LTL in a hierarchical three-level process, a
multi-layered synergistic framework with temporal goals, and temporal-logic
motion planning for several agents. The paper claims two differences.
TAMAA combines a path-planning algorithm with temporal logic. It also
connects a model checker with a mission-management tool on an industrial
case. It uses TCTL instead of LTL to express timing requirements as well as
functional ones. [p. 10]

## Reviewer notes on requirement fidelity

These notes are a reading of the paper, not claims from it.

- Queries (5) and (8) are `E<>` queries. They show that one plan exists.
  They do not show that all behaviors of the model meet the requirement.
  For plan synthesis, this is the intended reading.
- The claim that a plan is "optimal" needs the fastest-trace option of
  UPPAAL. The paper lists that option but does not say which option TAMAA
  uses. Optimality is also relative to the integer travel times from
  Theta*. [p. 2, p. 6, p. 8]
- Event reaction has no own query. The argument is that a missed event
  causes a deadlock, so (5) or (8) fails. This shows a reaction before the
  deadline. It does not check that the event task is "prioritized", as the
  requirement says. [p. 5, p. 8]
- Task matching holds by construction. So its correctness depends on the
  generation algorithm, which the paper does not verify. [p. 8]
- The invariance query (7) checks the order over the whole generated model.
  The preconditions in the guards already enforce that order, so the query
  mainly checks the generator.
- Table 2 gives 20160 s for 2,058,132 states with four agents. The other
  rows of Tables 1 and 2 take between 0.06 s and 0.2 s per 10,000 states.
  This row takes about 98 s per 10,000 states, more than 400 times slower.
  The text does not explain it. [p. 9]
- Section 4.3 says the state count grows "exponentially" with milestones and
  tasks. The conclusion says that milestones and tasks "do not significantly
  influence" the cost. The two statements do not agree. [p. 9–10]
- Scenario 3 has three agents and more than 770,000 states for invariance.
  Table 2 has three agents and 344,701 states. The setups differ: four
  milestones against three. [p. 9]
- Definition 2 lists edges only from vertex locations to transition
  locations, but the automaton also has edges back to vertex locations.
  [p. 4–5]
- Algorithm 1 calls `c <= tt[A][B]` on a location a "guard". On a location,
  it is an invariant. [p. 6]
- The text on Algorithm 1 refers to "Definition 4" for edge labels. The
  movement edges come from Definition 2. [p. 7]
- The environment definition says an edge connects two milestones only when
  the shortest path between them passes no other milestone. Algorithm 1
  adds an edge for every pair with a finite travel time, and does not check
  this rule. [p. 4, p. 6]
- AI aspect: the paper uses no learning in TAMAA. Reinforcement learning is
  future work for state-space search. [p. 10]

## Terms

| Term | Meaning in this paper |
|---|---|
| TAMAA | Timed-Automata-based Planner for Multiple Autonomous Agents, the tool of the paper |
| Mission plan | A path through milestones together with a schedule of tasks |
| Milestone | A point in the environment where a task can happen |
| Automated agent | An agent that follows its mission plan with no human control and no interaction with its environment |
| No-op task (T0) | The task "no task is running"; the only state in which the agent can move |
| Monitor automaton | An automaton that raises an event when a clock reaches a threshold, such as low battery |
| MMT | Mission Management Tool, a graphical tool to create missions for agents |
| Theta* | An any-angle variant of A* that makes paths with fewer turns |
| Timed automata (TA) | State machines with real-valued clocks, guards, and invariants |
| `E<> p` | Reachability: some path reaches a state where `p` holds |
| `A[] p` | Invariance: `p` holds in all reachable states |
| Diagnostic trace | The run that UPPAAL returns as a witness for a satisfied reachability query |
| Partial order reduction | A method that skips equivalent orders of independent transitions to make the state space smaller |
| Proposition-preserving decomposition | A split of the environment into regions that keeps the truth of the propositions of interest |

## Citation

Rong Gu, Eduard Enoiu, and Cristina Seceleanu. "TAMAA: UPPAAL-based Mission
Planning for Autonomous Agents." SAC'20, 2020.
