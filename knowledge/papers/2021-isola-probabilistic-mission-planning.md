---
id: gu2021isola-probabilistic-mission-planning
title: "Probabilistic Mission Planning and Analysis for Multi-agent Systems"
authors:
  - Rong Gu
  - Eduard Enoiu
  - Cristina Seceleanu
  - Kristina Lundqvist
affiliation: Mälardalen University, Västerås, Sweden
year: 2021
venue: ISoLA'21
venue_source: author's publications page (the PDF does not name the venue)
doi: null
document_type: conference paper
pages_in_pdf: 17
pdf_url: https://drive.google.com/file/d/1_3nLViqoVJHmcCiuyZCxzgtYpU-iiWGW/view?usp=sharing
listing_url: https://sites.google.com/view/ronggu/publications
author_keywords: [MAS, mission planning, Q-learning, statistical model checking]
topics: [mission planning, multi-agent systems, task scheduling, path planning, statistical model checking, reinforcement learning, autonomous vehicles, construction machinery, bottleneck analysis, re-planning]
formalisms: [stochastic timed automata, hybrid automata, timed automata, UPPAAL SMC probability-estimation queries]
tools: [UPPAAL SMC, UPPAAL 4.1.24, TAMAA]
algorithms: [Q-learning, Theta*, dipole flow field, Monte Carlo simulation]
application: autonomous quarry with one wheel loader and three trucks
abbreviations: {MAS: multi-agent systems, MCRL: Model Checking + Reinforcement Learning, STA: stochastic timed automata, HA: hybrid automata, TA: timed automata, SMC: statistical model checking, BCET: best-case execution time, WCET: worst-case execution time, ODE: ordinary differential equation}
funding: DPAC project, Swedish Knowledge Foundation, grant 20150022
---

# Probabilistic Mission Planning and Analysis for Multi-agent Systems (Gu et al., ISoLA 2021)

## At a glance

This 2021 paper by Gu, Enoiu, Seceleanu, and Lundqvist extends MCRL, the
authors' earlier method that combines model checking and Q-learning for
mission planning. Mission planning here means path planning plus task
scheduling for many autonomous agents. The new version models the agents
as stochastic timed automata (STA) and analyzes them with statistical model
checking in UPPAAL SMC. A hybrid-automata (HA) model of the agents and of
randomly appearing pedestrians gives the probable delays in travel time.
On an autonomous-quarry case with four agents, the synthesized plans satisfy
four requirement types with probabilities above 99.8%. The paper also shows
a bottleneck analysis of waiting times and a re-planning case when
pedestrians block one route.

Page references `[p. N]` point to the 17-page PDF. The PDF page numbers
match the printed page numbers.

## Key facts

Each fact is a claim from the paper unless it is marked otherwise.

- The ISoLA'21 mission-planning paper extends MCRL (Model Checking +
  Reinforcement Learning) from timed automata to stochastic timed automata.
  [p. 2, p. 8]
- MCRL has three phases: data gathering by Monte Carlo simulation in UPPAAL
  SMC, model training by Q-learning, and injection of the Q-table back into
  the model. [p. 7–8]
- In MCRL, a successful simulation trace gets the value (ST − FT)², where ST
  is the simulation time and FT is the time to reach the desired state. A
  failed trace gets a fixed negative value. [p. 8]
- In MCRL, a "conductor" automaton for each agent reads the Q-table and
  picks the available action with the highest value. [p. 8]
- In MCRL, the Q-table is the synthesized mission plan. When two agents
  want the same exclusive milestone, the agent with the higher reward goes.
  [p. 8]
- A Java program parses the UPPAAL SMC simulation output and runs the
  Q-learning algorithm. [p. 4, p. 12]
- The ISoLA'21 paper uses an HA model with Newtonian motion and a
  dipole-flow-field collision-avoidance algorithm to estimate travel-time
  delays caused by pedestrians. [p. 2, p. 5, p. 10]
- The estimated travel times and their probabilities become probability
  weights on branches of the movement STA. [p. 10–11]
- Path planning in the ISoLA'21 paper uses the Theta* algorithm on a 2D map.
  [p. 6]
- The quarry case has one wheel loader (Agent 0) and three trucks (Agents 1
  to 3), with milestones A to D. [p. 12, Fig. 7]
- The experiments use UPPAAL 4.1.24 with α = 0.001 and ε = 0.001. [p. 12]
- For the quarry case, the task-assignment, execution-order,
  milestone-exclusion, and timing queries all give probabilities above
  99.8%. [p. 12–13]
- The timing query uses a limit of 10 time units for the wheel loader and 25
  time units for the trucks. [p. 13]
- In the bottleneck analysis, milestone D (the secondary crusher) has the
  highest probability of waiting, about 13.3% to 14.5%. [p. 13, Fig. 8]
- The waiting time at milestone D is most likely less than 2 time units.
  [p. 13]
- With many pedestrians near milestone C, the synthesized plan sends the
  single truck via milestone B instead of milestone C. [p. 14]
- The paper gives no state counts, run times, or hardware for the
  experiments.

## Questions this paper answers

**What problem does the paper solve?** It synthesizes mission plans for
many autonomous agents when task times, waiting times, and the environment
are uncertain. It also analyzes these plans statistically.

**What is new compared with the earlier MCRL?** The earlier MCRL used
timed automata and could not model stochastic events. This version uses STA
and statistical model checking. It can estimate delays from pedestrians and
measure waiting at shared milestones. [p. 8]

**How do reinforcement learning and model checking work together?** UPPAAL
SMC simulates the model and prints state-action pairs. Q-learning turns
them into a Q-table. The Q-table goes back into the model, and UPPAAL SMC
checks the controlled model against probability queries. [p. 7–8, p. 11]

**How do the authors get the travel-time distribution?** They simulate the
HA model of an agent and of spawned pedestrians. They check queries of the
form `Pr[<=T]([] arrived imply t <= TL)` for different TL values. [p. 10–11]

**What does the verification show?** Each requirement type holds with a
probability above 99.8% on the quarry case. [p. 12–13]

**Can the method re-plan?** Yes, in one demonstrated case. The authors
change the travel-time weights to the C route, and the new plan prefers the
B route. [p. 14]

**How large is the case?** Four agents, four milestones, and six tasks. The
paper gives no performance numbers.

## Scope: what this paper does not do

- It does not give exhaustive guarantees. All results are statistical
  estimates from simulation. [p. 12–13]
- It does not report computation time, number of simulation runs, or the
  size of the Q-table.
- It does not compare MCRL with another planner on the quarry case. It
  refers to earlier work for a comparison with UPPAAL STRATEGO. [p. 16]
- It does not check the HA collision-avoidance model for collisions here.
  It uses the HA model only to estimate travel times. [p. 5]
- It does not describe the state and action definitions of the Q-learning.
  It refers to earlier work. [p. 11]
- It does not automate the step from requirements to queries. The authors
  list that as future work. [p. 16]
- It names no DOI and no venue inside the PDF.

## Requirements in natural language

The authors extract four requirement categories from their industrial
partner. [p. 6]

1. **Task assignment.** The task must go to the right milestone that has
   the corresponding device.
2. **Execution order.** The task order must be correct. For example,
   unloading into the primary crusher starts only after digging finishes.
3. **Milestone exclusion.** A milestone whose device allows only one agent at
   a time is exclusive when it is occupied.
4. **Timing.** Tasks must finish within a prescribed time frame.

The paper names three uncertainties: task execution time between BCET and
WCET, waiting time at occupied milestones, and human workers that appear
irregularly. [p. 6–7]

## Method

### Stochastic timed automata in UPPAAL SMC

- In an STA, time-bounded delays follow a uniform distribution, and
  unbounded delays follow an exponential distribution with a user rate.
  [p. 3]
- A choice between enabled edges is probabilistic, with integer weights on
  the edges. [p. 3–4]
- UPPAAL SMC supports only broadcast channels. [p. 3]

### Task-execution STA

- Location `Idle` means no task runs. Only in `Idle` can the agent move. A
  self-loop sends `go[id]` every MT time units, so a waiting agent checks
  again whether its target milestone is free. [p. 9]
- The edge to task location T1 has a guard with four parts: the agent is at
  milestone B (`cp[id]==B`), `isReady(TK1)` holds, the precedent task is done
  (`tasks[TK2]`), and no event is active (`!event[id][0]`). [p. 9]
- `isReady` also checks that collaborating agents are at the same milestone
  for a collaborative task. [p. 9]
- An event, such as a low-battery warning, has priority over regular tasks.
  [p. 9–10]
- The invariant of T1 bounds the clock by the WCET. The guard on the exit
  edge requires at least the BCET. [p. 10]
- `start(TK1)` stores the current state-action pair in an array, which is
  the execution trace. [p. 10]

### Movement STA

- In the Fig. 6 example, an agent goes from A1 to A2. The direct route
  crosses pedestrians. The detour via B1 has no pedestrians and takes at
  least 15 time units. [p. 10]
- The direct route takes 10 time units with probability 40% or 18 time
  units with probability 60%. The authors get these values from the HA
  model. [p. 11]
- A movement edge enters a milestone only if the milestone is not occupied.
  [p. 11, Fig. 6]

### Queries used in the method

| No. | Query | Purpose |
|---|---|---|
| (2) | `Pr[<=T](<> arrived)` | Probability that the agent reaches the destination [p. 10] |
| (3) | `Pr[<=T]([] arrived imply t <= TL)` | Probability that the agent arrives within TL [p. 10] |
| (4) | `simulate[<=T;R] {ds[0].cs, ds[0].act, ds[0].value, ...} : tasks[TK1]` | R simulation runs that print state, action, and value when T1 finishes [p. 11] |
| (5) | `Pr[<=T]([] te_n.T_i imply m_n.P_i)` | Task assignment [p. 12] |
| (6) | `Pr[<=T]([] te_n.T_i imply te_n.tasks[j])` | Execution order [p. 12] |
| (7) | `Pr[<=T]([] m_n.P_i imply !(m_0.P_i && ... && m_n-1.P_i && m_n+1.P_i ...))` | Milestone exclusion [p. 13] |
| (8) | `Pr[<=T]([] (te_n.tasks[0] && ... && te_n.tasks[M-1]) imply x < TL)` | Timing [p. 13] |
| (9) | `Pr[<=T](<> m0.wt[i] + m1.wt[i] + ... + mn.wt[i] > TL)` | Waiting time at milestone i [p. 13] |
| (10) | `Pr[<=T]([] m0.D imply (viaC && !viaB))` | The truck reaches D via C and not via B [p. 14] |

`te_n` is the task-execution STA of agent n, and `m_n` is its movement STA.
`x` is a global clock that resets only when all tasks finish. [p. 13]

### Hybrid-automata layer

- The two-layer framework from earlier work has a static layer for mission
  planning and a dynamic layer with HA for continuous movement. [p. 4]
- A pedestrian-generator HA spawns pedestrian instances with exponential
  rate 0.1 while their number is below M. [p. 5]
- The agent HA has four locations: idle, acceleration, constant movement,
  and deceleration. ODEs give the speed and position. [p. 5]

## Case study: an autonomous quarry

A wheel loader digs stones at the stone pile and loads trucks. The trucks
carry the stones to a primary crusher and then the crushed stones to the
secondary crusher. [p. 5–6] Milestones A to D are exclusive. There are two
primary crushers, B and C. [p. 12]

| Agent | Task | BCET | WCET | Precedent task | Milestone |
|---|---|---|---|---|---|
| Wheel loader | Dig | 2 | 2 | none | Stone pile (A) |
| Wheel loader | Unload | 1 | 4 | Dig | Stone pile (A) |
| Truck | Load I | 1 | 4 | Dig | Stone pile (A) |
| Truck | Unload I | 4 | 4 | Load I | Primary crusher (B or C) |
| Truck | Load II | 2 | 3 | Unload I | Primary crusher (B or C) |
| Truck | Unload II | 3 | 5 | Load II | Secondary crusher (D) |

Source: Table 1 of the paper. [p. 12]

## Results

### Mission-plan synthesis

| Requirement | Query | Result |
|---|---|---|
| Task assignment | (5), for all tasks in Table 1 | Above 99.8% |
| Execution order | (6), for tasks with a precedent task | Above 99.8% |
| Milestone exclusion | (7), for milestones A to D | Above 99.8% |
| Timing | (8), TL = 10 (wheel loader), TL = 25 (trucks) | Above 99.8% |

Source: Section 5.1. [p. 12–13]

### Bottleneck analysis

Query (9) with TL = 0 gives the probability of any waiting at each
milestone. [p. 13]

| Milestone | Lower bound | Upper bound |
|---|---|---|
| A | 7.1% | 8.1% |
| B | 1.6% | 2.6% |
| C | 10.0% | 11.1% |
| D | 13.3% | 14.5% |

Query (9) at milestone D with different TL values gives the waiting time.
[p. 13]

| Waiting time at D | Lower bound | Upper bound |
|---|---|---|
| > 0 | 13.3% | 14.5% |
| > 1 | 7.4% | 8.2% |
| > 2 | 0% | 0.02% |

Source: bar values in Fig. 8(a) and Fig. 8(b). [p. 13]

### Travel-time estimation and re-planning

- With only one truck, Q-learning makes the truck go via C, because C is
  nearer to the secondary crusher D. Query (10) checks this. [p. 14]
- Few pedestrians: generator rate 0.1, existing time 1. The movement STA to
  C gets weights 83 (t ≥ 3) and 33 (t ≥ 10). [p. 14–15, Fig. 9]
- Many pedestrians: generator rate 0.2, existing time 5. The weights become
  5 (t ≥ 3) and 71 (t ≥ 10). [p. 15, Fig. 9]
- With many pedestrians, Query (10) gives a range of low probabilities. The
  same query for the route via B gives a much higher probability. The paper
  gives no exact numbers. [p. 14]

## Limitations stated by the authors

- The earlier MCRL with timed automata cannot handle unpredictable events
  or give statistical analysis. This paper addresses that limit. [p. 8]
- The Q-values converge only "as long as the simulation has produced enough
  data". [p. 8]

## Future work stated by the authors

- Integrate the new MCRL with the TAMAA tool, to get a complete solution
  with a graphical user interface. [p. 16]
- Automate the transformation of requirements into temporal logic queries.
  [p. 16]

## Related work, as the paper positions itself

The paper cites controller synthesis for multi-agent systems under
uncertainty, strategy synthesis with Signal Temporal Logic, and policy
synthesis for POMDPs. It also cites PRISM-based verification of
autonomous vehicles with PCTL. The authors claim that their approach
estimates the disturbance from unpredictable moving obstacles in a
systematic way and enables re-planning. [p. 15] UPPAAL STRATEGO also has
Q-learning. The authors claim that MCRL supports more agents. [p. 15–16]

## Reviewer notes on requirement fidelity

These notes are a reading of the paper, not claims from it.

- **Exclusion query.** Query (7) negates a conjunction: "not all other
  agents are at P_i". The requirement says "no other agent is at P_i",
  which needs a disjunction inside the negation. As printed, the query is
  much weaker than the requirement.
- **Exclusion and collaboration.** Milestone A is exclusive, but Load I
  needs the wheel loader and a truck at A at the same time. The paper does
  not say how Query (7) treats this collaborative case.
- **Probability weights.** The text calls the Fig. 9(b) weights 83% and 33%.
  These sum to 116%. In UPPAAL SMC, branch weights are relative, so the
  actual probabilities are about 72% and 28%. [p. 14]
- **Interval width.** The paper sets ε = 0.001, but the intervals in Fig. 8
  are about one percentage point wide. The paper does not explain this
  difference. [p. 12–13]
- **What "above 99.8%" proves.** Each result is a statistical estimate on
  the model with the Q-table. It is not a proof that the plan always meets
  the requirement. The paper does not say what happens in the remaining
  runs, up to 0.2%.
- **Model assumptions.** Every result rests on the uniform distribution of
  task times, the travel-time weights from the HA model, and the abstract
  movement STA. The paper does not validate these against the real quarry.
- **"Statistically optimal".** The abstract and Section 4.2 call the plans
  statistically optimal. The paper gives no optimality measure or
  comparison that supports this claim. [p. 1, p. 11]
- **Evaluation depth.** The paper gives no run times, simulation counts, or
  scalability data, although scalability is a stated reason for MCRL.
- **AI aspect.** The paper uses Q-learning, a reinforcement learning
  method, as the planner. Statistical model checking then checks the
  learned plan. The learned Q-table is part of the verified model.

## Terms

| Term | Meaning in this paper |
|---|---|
| Mission planning | Path planning plus task scheduling for autonomous agents |
| Milestone | A position where an agent does a task, such as a stone pile or a crusher |
| Exclusive milestone | A milestone that only one agent can use at a time |
| MCRL | Model Checking + Reinforcement Learning, the authors' method |
| STA | Stochastic timed automata: timed automata with probability distributions on delays and on edge choices |
| HA | Hybrid automata: automata with continuous variables that change by ODEs |
| SMC | Statistical model checking: estimating the probability of a property from many simulation runs |
| `Pr[<=T](...)` | UPPAAL SMC query that estimates a probability within T time units |
| α, ε | Probability of a false negative, and the probability uncertainty of the estimate |
| Q-learning | A reinforcement learning algorithm that learns the value of each state-action pair |
| Q-table | The table of state-action values; here it is the mission plan |
| Conductor | An automaton that chooses each agent's action from the Q-table |
| BCET, WCET | Best-case and worst-case execution time of a task |
| Theta* | An any-angle path-planning algorithm on grids |
| Dipole flow field | A collision-avoidance method with attracting and repelling forces |
| Spawning | A UPPAAL SMC function that creates new automaton instances during a run |
| TAMAA | The authors' UPPAAL-based mission-planning tool from earlier work |

## Citation

Rong Gu, Eduard Enoiu, Cristina Seceleanu, and Kristina Lundqvist.
"Probabilistic Mission Planning and Analysis for Multi-agent Systems."
ISoLA'21, 2021.
