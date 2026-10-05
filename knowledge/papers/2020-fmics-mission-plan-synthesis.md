---
id: gu2020fmics-mcrl
title: "Verifiable and Scalable Mission-Plan Synthesis for Autonomous Agents"
authors:
  - Rong Gu
  - Eduard Enoiu
  - Cristina Seceleanu
  - Kristina Lundqvist
affiliation: Mälardalen University, Västerås, Sweden
year: 2020
venue: FMICS'20
venue_source: author's publications page (the PDF does not name the venue)
award: Best-paper Award
award_source: author's publications page
doi: null
document_type: conference paper
pages_in_pdf: 17
pdf_url: https://drive.google.com/file/d/1JIh2VVOmzgEObCkyUbzQCO3i_suL54Bu/view?usp=sharing
listing_url: https://sites.google.com/view/ronggu/publications
author_keywords: null
topics: [mission planning, plan synthesis, model checking, reinforcement learning, state-space explosion, multi-agent systems, autonomous vehicles, construction machinery, task scheduling, scalability, formal methods and machine learning]
formalisms: [timed automata, TCTL, timed games]
tools: [UPPAAL, UPPAAL STRATEGO, TAMAA]
algorithms: [Q-learning, Theta*]
application: autonomous trucks and wheel loaders in a quarry
abbreviations: {MCRL: "the method of the paper, which combines model checking and reinforcement learning", TA: timed automata, TCTL: Timed Computation Tree Logic, RL: reinforcement learning, BCET: best-case execution time, WCET: worst-case execution time, EST: execution status of tasks, NoS: number of explored states, NoA: number of agents, OOM: out of memory, POMDP: partially observable Markov decision process, MITL: Metric Interval Temporal Logic, VOLVO CE: Volvo Construction Equipment}
funding: null
---

# Verifiable and Scalable Mission-Plan Synthesis for Autonomous Agents (Gu et al., FMICS 2020)

## At a glance

This 2020 paper by Gu, Enoiu, Seceleanu, and Lundqvist proposes MCRL, a
method that combines model checking with reinforcement learning to
synthesize mission plans for many autonomous agents. MCRL starts from the
timed-automata model that the TAMAA tool generates. It runs random UPPAAL
simulations, rewards traces that finish all tasks, and penalizes traces
that deadlock. Q-learning turns these traces into one Q-table per agent. A
new "conductor" automaton per agent follows the Q-table, so the state space
becomes much smaller. The model with the Q-tables can then be verified in
UPPAAL. On a quarry case with 2 to 6 agents, MCRL gives results for all
cases. TAMAA runs out of memory above 4 agents and UPPAAL STRATEGO above 2.
The publications page marks the paper with a Best-paper Award.

Page references `[p. N]` point to the 17-page PDF.

## Key facts

Each fact is a claim from the paper unless it is marked otherwise.

- MCRL combines model checking and reinforcement learning, specifically
  Q-learning, to restrict the state space of a timed-automata model. [p. 1]
- MCRL reuses the timed-automata model of agents that TAMAA generates.
  [p. 2, p. 7]
- MCRL explores the state space by random simulation instead of by
  exhaustive search and storage of states. [p. 2]
- MCRL rewards each state-action pair in a good trace with `(T − C)²`,
  where T is the simulation time and C is the time when all tasks finish.
  Deadlocked traces get a fixed penalty. [p. 9–10]
- In MCRL, the Q-learning program is in Java. It writes the Q-table as C
  code, which goes back into the UPPAAL model. [p. 10]
- Each MCRL agent has one conductor automaton. The conductor holds the
  Q-tables of all agents, so that it can decide which agent acts first.
  [p. 10]
- MCRL handles uncertain task execution times and uncertain movement times.
  TAMAA does not. [p. 2, p. 15]
- MCRL models the two uncertainties as time-bounded delays with a uniform
  distribution. [p. 10]
- The MCRL experiments use UPPAAL 4.1.22 and UPPAAL STRATEGO 4.1.20-7 on a
  laptop with an Intel Core i5 and 16 GB of RAM. [p. 12–13]
- The MCRL experiment environment has 4 static obstacles, 6 milestones,
  several autonomous trucks, and 1 autonomous wheel loader. [p. 13]
- In the MCRL experiments, TAMAA fails above 4 agents and UPPAAL STRATEGO
  fails above 2 agents. MCRL gives results for 2 to 6 agents. [p. 14]
- With 4 agents, TAMAA takes more than 5 hours and MCRL about 3 minutes.
  [p. 14]
- With 3 agents, TAMAA is the fastest of the three methods. [p. 14]
- The MCRL computation time grows nearly linearly with the number of
  agents, from 2 to 6. [p. 14]
- MCRL can fail to find a valid or optimal plan when the simulation rounds
  are too few, even if the original model has a solution. [p. 14]

## Questions this paper answers

**What problem does MCRL solve?** Mission-plan synthesis (path planning
plus task scheduling) for many agents, where exhaustive model checking runs
out of memory. [p. 1–2, p. 6]

**How does MCRL work?** In three phases: data gathering by UPPAAL
simulation, model training by Q-learning, and model reforming with a
conductor automaton that reads the Q-table. [p. 8, Fig. 5]

**What is the mission plan in MCRL?** The Q-table itself. [p. 2]

**How is the plan verified?** The reformed model, with the Q-tables and
conductors, is checked in UPPAAL against TCTL queries for milestone
matching, task sequencing, timing, and event reaction. [p. 12]

**How does MCRL compare with TAMAA and UPPAAL STRATEGO?** MCRL scales to 6
agents in the experiment. TAMAA fails above 4 agents and UPPAAL STRATEGO
above 2. For 3 or fewer agents, TAMAA is faster. [p. 14]

**Why is the verification still possible?** The conductors restrict the
behavior of the agents, so the reformed model has far fewer states.
[p. 2, p. 12]

**What are the AI or learning aspects?** The method uses Q-learning, a
model-free reinforcement learning algorithm. UPPAAL simulation supplies the
training data. Model checking then checks the learned policy. [p. 4, p. 8]

## Scope: what this paper does not do

- It does not cover the dynamic layer. It assumes that collision avoidance
  of dynamic obstacles works correctly. [p. 5]
- It does not prove that MCRL finds a plan when one exists. Too few
  simulation rounds can miss it. [p. 14]
- It does not give a method to choose the number of simulation rounds. The
  designer chooses it from experience. [p. 14]
- It does not use the statistical model checking of UPPAAL. The simulation
  only explores the state space. [p. 10]
- It does not report the verification results of the requirement queries
  (3) to (6) on the reformed model.
- It does not give the learning rate, the discount value, the penalty
  value, or the number of simulation rounds used.
- It names no DOI and no venue inside the PDF. The PDF prints a Zenodo DOI
  for TAMAA mission-plan graphics, not for the paper. [p. 13]

## System under study

The use case is an autonomous quarry from VOLVO CE. Wheel loaders dig and
load stones. Trucks carry the stones from stone piles to primary crushers
and then to secondary crushers. The vehicles must avoid static obstacles
and go to a charging point when the battery is low. [p. 4]

In the example of Fig. 3(a), four trucks start at milestone A. They take
stones from B to a primary crusher at C or D, and then go to the secondary
crusher at E. Wheel loaders work at B. The charging point is at F. [p. 7]

## Requirements in natural language

These are the requirement categories as the paper states them. [p. 5]

1. **Milestone matching.** Tasks must happen at the right milestones.
2. **Task sequencing.** The task execution order must be correct.
3. **Timing.** Tasks must be done within a given time limit.
4. **Event reaction.** Some tasks start on events. For example, when the
   battery level is low, the agents must go to charge.

## Problem analysis

- The task scheduling is similar to the job-shop problem, which is NP-hard.
  [p. 5]
- The problem adds two uncertainties: task execution time between BCET and
  WCET, and movement time, because an agent can wait for an occupied
  milestone. [p. 6]
- TAMAA handles up to 100 milestones and tasks. But its plans are only the
  fastest, shortest, or random diagnostic traces, and it runs out of memory
  at 5 agents. [p. 6]
- UPPAAL STRATEGO synthesizes strategies over all execution and travel
  times. But it gives results only for fewer than 3 agents, because it
  depends on exhaustive model checking in UPPAAL TIGA. [p. 6]

## The MCRL method

**Base model.** TAMAA generates a movement automaton and a task execution
automaton per agent. Theta* gives the travel times `TT[m1][m2]`. The guard
function `occupied` checks exclusive milestones. Every `MW` time units, the
task automaton tells the movement automaton through `go[id]` that the agent
can move. [p. 7–8]

**Q-state (Definition 1).** `QS = <TP, MATCH>`. TP is the time point of
leaving the state. MATCH is `<RT, CT, CP, EV, ST>`: rounds, current task,
current milestone, event values, and the execution status of the tasks of
all agents. [p. 8–9]

**Q-action (Definition 2).** `QA = <BT, WT, MT, TT>`: BCET, WCET, motion
type (0 movement, 1 execution), and the target milestone or the next task.
[p. 9]

**Execution status (ST).** 0 means unfinished, 1 finished, and 2 "will be
finished" when the current agent arrives. Each agent needs this status of
the others to avoid unnecessary waiting. [p. 9]

**Data gathering.** A UPPAAL simulation query with a predicate prints data
only for good traces: `simulate[<=T; R]{...} : taskAllFinish == true`.
Traces that neither finish nor deadlock are ignored. [p. 8–9] The time T of
a round must be at least the shortest time for the whole mission. [p. 10]

**Training.** A Java program runs Q-learning on the printed state-action
pairs. The Q-table is a two-dimensional array:
`{Agent ID} | {Q-state, Q-action, Q-value}`. [p. 10]

**Reforming.** A conductor automaton per agent starts in an urgent location
`Init`. Its function `makeDecision` picks the action with the highest value
that matches the current MATCH tuple. It ignores TP. For a move to an
exclusive milestone, the agent with the highest value moves and the others
wait. The conductor uses the channels `exe[id]`, `run[id]` (broadcast),
`done[id]`, and `restart`. When an agent finishes its rounds, it goes to
location `Disappear` and releases its milestone. [p. 10–11]

**Changes to the TAMAA automata.** Channel `go[id]` becomes `run[id]`. The
self-loop of location `Idle` in the task automaton is removed. [p. 11]

## Verification queries for the synthesized plan

In these queries, `ten` and `moven` are the task and movement automata of
agent n. [p. 12]

| Requirement | Query |
|---|---|
| Milestone matching | (3) `A[] (ten.Ti imply moven.Pi)` |
| Task sequencing | (4) `A[] (ten.Ti imply tasks[n][i-1]==FIN)` |
| Timing | (5) `A[] ((forall(i:int[0,M-1]) tasks[n][i]==FIN) imply x<=TL)` |
| Event reaction | (6) `event[i][j] --> (moven.Pk && x <= EL)` |

The paper says that these queries cannot be checked by traditional model
checking alone when there are many agents. [p. 12]

## Comparison setup

| Method | Query or procedure | Note |
|---|---|---|
| TAMAA | (7) `E<> (stone==0 && x<=LIMIT)`, fastest diagnostic trace | Plans only of the fastest, shortest, or random type [p. 13] |
| UPPAAL STRATEGO | (8) `strategy MP = control: A<> stone==0`, then (9) `E<> (stone==0 && x<=LIMIT) under MP` | Arrival edges of movement and edges into `Idle` become uncontrollable [p. 13] |
| MCRL | Train and reform the TAMAA model, then synthesize plans for 2 to 6 agents | [p. 13] |

## Results

The text gives these results. [p. 14]

- MCRL gives a result for all cases and explores far fewer states than the
  other two methods.
- TAMAA and UPPAAL STRATEGO fail for more than 4 and more than 2 agents.
  They return "out of memory" after long times.
- With 3 agents, TAMAA takes the least time, because the other two methods
  consider all uncertain times.
- With 4 agents, TAMAA takes more than 5 hours and MCRL about 3 minutes.
- The MCRL time grows nearly linearly with the number of agents.

Values printed as labels in Fig. 7(a), number of explored states. [p. 14]

| Method | Agents | Explored states |
|---|---|---|
| TAMAA | 4 | 2,923,415 |
| MCRL | 5 | 113,494 |
| MCRL | 6 | 285,647 |

The assignment of the two MCRL labels to 5 and 6 agents is a reading of the
bar lengths. Confidence: medium. Fig. 7(b) shows the times in minutes on a
y-axis that is not equidistant above 8. [p. 14]

## Limitations stated by the authors

- Too few simulation rounds give too little data. Then MCRL cannot
  synthesize a valid or optimal plan, even if one exists. [p. 14]
- The designer chooses the number of rounds from experience. [p. 14]
- The simulation time of each round must not be shorter than the shortest
  mission time, or no good trace appears. [p. 10]

## Future work stated by the authors

- Integrate Q-learning directly into the state-space generation of UPPAAL.
  [p. 15]
- Apply other machine-learning or AI algorithms to tame verification
  scalability or to guide the model checking. [p. 15]
- Synthesize plans for agents that work for much longer times. [p. 15]
- Find a method to infer the number of simulation rounds. [p. 14]

## Related work, as the paper positions itself

- Policy synthesis with POMDPs, and automata-based controller synthesis
  with MITL for multi-agent path planning. MCRL instead combines model
  checking with reinforcement learning. [p. 15]
- Formal specifications that build interpretable reward functions, and
  probabilistic guarantees on reinforcement-learning agents. [p. 15]
- UPPAAL STRATEGO uses reinforcement learning to refine strategies for
  priced timed games. [p. 15]
- Bounded rational search uses reinforcement learning against state-space
  explosion in on-the-fly model checking, but only for LTL without timing.
  [p. 15]
- The paper claims that MCRL uses reinforcement learning to replace
  exhaustive model checking for multi-agent mission-plan synthesis. [p. 15]

## Reviewer notes on requirement fidelity

These notes are a reading of the paper, not claims from it.

- The title says "verifiable", and queries (3) to (6) are defined. But the
  paper reports no result for these queries. Fig. 7 reports only the
  synthesis queries (7) or (8). [p. 12, p. 14]
- A pass of (3) to (6) on the reformed model proves the property for the
  model with the conductors. It covers all orders of the conductors and all
  delays in the model. It says nothing about states that the Q-table does
  not cover, because the Q-table is the plan. [p. 11–12]
- Query (5) is `A[]` over "all tasks finished imply x <= TL". If the clock
  x keeps running after the tasks finish, the query fails later. The paper
  does not say whether x stops or how the model ends. [p. 12]
- Query (6) names "agent i" and "event j" in the text, but the formula uses
  `moven`. The index of the agent is not consistent. [p. 12]
- Query (4) checks only the task `i-1` before task `i`. This captures the
  requirement only for a linear order of tasks. [p. 12]
- The paper says that Equation 1 "guarantees" that the Q-values converge.
  Q-learning converges only under conditions, such as enough visits of each
  state-action pair. The paper does not discuss them. [p. 10]
- The method is incomplete: a "no plan" result from MCRL does not show that
  no plan exists. [p. 14]
- The data gathering uses uniform delays. The verification of the reformed
  model uses non-deterministic delays. The learned policy can thus meet
  delay combinations that the training saw rarely.
- The abstract says MCRL is better for more than three agents. The results
  show that TAMAA is faster at 3 agents and still gives a result at 4.
  [p. 1, p. 14]
- The Fig. 7 caption says "Query (7) or (8)" for all three methods. The
  paper does not say which query gives the MCRL numbers. [p. 14]

## Terms

| Term | Meaning in this paper |
|---|---|
| MCRL | The method of the paper, which combines model checking and reinforcement learning |
| Mission plan | A path through milestones together with a schedule of tasks; in MCRL, a Q-table |
| TAMAA | The authors' earlier tool that generates timed automata for mission planning |
| UPPAAL STRATEGO | A UPPAAL tool that synthesizes strategies for stochastic priced timed games |
| UPPAAL TIGA | A UPPAAL tool that synthesizes strategies for timed games |
| Reinforcement learning | Machine learning in which an agent learns actions that maximize an accumulated reward |
| Q-learning | A model-free reinforcement learning algorithm that learns a value for each state-action pair |
| Q-table | The table of state-action pairs and their values that Q-learning fills |
| Bellman optimality equation | `q*(s,a) = E[R(s,a) + γ max q*(s',a')]`: the value of an action is its reward plus the discounted best future value |
| Conductor | A new automaton per agent that reads the Q-table and tells the agent what to do |
| Controllable / uncontrollable edge | In a timed game, an edge that the player chooses, or that the environment chooses |
| BCET / WCET | Best-case and worst-case execution time of a task |
| Job-shop problem | A classic NP-hard problem that schedules jobs on machines |
| State-space explosion | The fast growth of the number of model states with the number of components |
| `A[] p` | Invariance: `p` holds in all reachable states |
| `E<> p` | Reachability: some path reaches a state where `p` holds |
| `p --> q` | Leads to: whenever `p` holds, `q` holds later on every path |

## Citation

Rong Gu, Eduard Enoiu, Cristina Seceleanu, and Kristina Lundqvist.
"Verifiable and Scalable Mission-Plan Synthesis for Autonomous Agents."
FMICS'20, 2020.
