---
id: gu2022phd-scalable-synthesis-verification
title: "Formal Methods for Scalable Synthesis and Verification of Autonomous Systems: Mission Planning and Collision Avoidance"
authors:
  - Rong Gu
affiliation: School of Innovation, Design and Engineering, Mälardalen University, Västerås, Sweden
year: 2022
venue: Mälardalen University Press Dissertations No. 359
venue_source: PDF, p. 1
doi: null
isbn: 978-91-7485-552-4
issn: 1651-4238
document_type: doctoral dissertation (compilation thesis, a summary part and six included papers)
degree: Doctor of Technology in Computer Science (teknologie doktorsexamen i datavetenskap)
defense: 15 June 2022, 13.00, Gamma and online, Mälardalen University, Västerås
faculty_opponent: Professor Rajeev Alur, University of Pennsylvania
grading_committee: [Kim Larsen, Jan Křetínský, Jana Tumova]
supervisors: [Cristina Seceleanu, Kristina Lundqvist, Eduard Enoiu, Raluca Marinescu (former)]
pages_in_pdf: 369
pdf_url: https://drive.google.com/file/d/1_GFZcnXlqcS9qlIsl8_mcnXA1kDYGNgA/view?usp=sharing
listing_url: https://sites.google.com/view/ronggu/publications
author_keywords: []  # the thesis prints no keyword list
topics: [formal verification, model checking, strategy synthesis, mission planning, path planning, task scheduling, collision avoidance, reach-avoid verification, multi-agent systems, autonomous vehicles, reinforcement learning, statistical model checking, strategy compression, hybrid systems, construction machinery]
formalisms: [timed automata, UPPAAL timed automata, timed games, stochastic timed games, hybrid automata, stochastic hybrid automata, TCTL, weighted metric temporal logic]
tools: [UPPAAL, UPPAAL TIGA, UPPAAL SMC, UPPAAL STRATEGO, MALTA, MMT]
algorithms: [A*, Theta*, DALi, DALi*, dipole flow field, Q-learning, TAMAA, MCRL, MoCReL]
application: autonomous quarry with autonomous wheel loaders and trucks
abbreviations: {MAS: multi-agent autonomous systems, TA: timed automata, UTA: UPPAAL timed automata, NUTA: network of UPPAAL timed automata, TG: timed game, STG: stochastic timed game, HA: hybrid automata, SHA: stochastic hybrid automata, STA: stochastic timed automata, SMC: statistical model checking, RL: reinforcement learning, BCET: best-case execution time, WCET: worst-case execution time, TAMAA: Timed Automata based Mission planning for Autonomous Agents, MCRL: Model Checking + Reinforcement Learning, MoCReL: Model-checked Compressed Reinforcement Learning, MMT: Mission Management Tool, PWC: piece-wise-continuous, AWL: autonomous wheel loader}
funding: Swedish Knowledge Foundation, DPAC profile grant 20150022 and ACICS synergy grant 20190038 (acknowledged in the included papers, not in Part I)
---

# Formal Methods for Scalable Synthesis and Verification of Autonomous Systems (Gu, PhD thesis, Mälardalen University 2022)

## At a glance

This 2022 doctoral dissertation by Rong Gu applies algorithmic formal methods
to two functions of autonomous agents. The first function is mission
planning: path finding plus task scheduling. The second function is
collision avoidance during plan execution, stated as a reach-avoid
requirement. A two-layer framework separates the two functions. The static
layer synthesizes mission plans with timed automata and timed games in the
UPPAAL tool family. The dynamic layer verifies the continuous motion of the
agents with hybrid automata.

Two synthesis families exist. Exhaustive graph search (TAMAA in UPPAAL and
UPPAAL TIGA) is sound and complete, but it stops at five agents.
Learning-based synthesis (MCRL and MoCReL in UPPAAL STRATEGO) is sound and
scales further, but it is not complete. Collision avoidance is verified by
statistical model checking. It is also verified by exhaustive model checking
of a proven discrete-time over-approximation of nonlinear trajectories. The
toolset MALTA automates the planning. All evaluation uses an autonomous
quarry case from Volvo Construction Equipment.

The thesis is a compilation thesis. Part I (PDF p. 23–109) is the summary.
Part II (PDF p. 111–365) holds six included papers, A to F. Page references
`[p. N]` use the PDF page number. The printed page number in Part I and
Part II is the PDF page number minus 22.

## Key facts

Each fact is a claim of the thesis unless it is marked otherwise.

- The thesis is Mälardalen University Press Dissertations No. 359, ISBN
  978-91-7485-552-4, ISSN 1651-4238. [p. 1–2, p. 4]
- The public defense of the thesis was on Wednesday 15 June 2022 at 13.00,
  in Gamma and online, at Mälardalen University in Västerås. [p. 3]
- The faculty opponent of the thesis was Professor Rajeev Alur, University
  of Pennsylvania. [p. 3]
- The grading committee of the thesis was Kim Larsen, Jan Křetínský, and
  Jana Tumova. [p. 14]
- The thesis states one overall goal and five subgoals. Table 5.3 maps the
  six included papers to the five subgoals. [p. 53–55, p. 86]
- The thesis treats mission planning in three environment types: a
  deterministic environment as a 1-player game, a stochastic environment as
  a 1½-player game, and a non-deterministic environment as a 2-player game.
  [p. 28–30, p. 66]
- The thesis counts more than four agents as "large", to match industrial
  systems such as autonomous quarries. [p. 54]
- In the thesis, UPPAAL TIGA synthesizes plans for up to 5 agents. Five
  agents take 33,312,229 states and 53.8 minutes; six agents run out of
  memory. [p. 70–71]
- The thesis states that TAMAA in UPPAAL and in UPPAAL TIGA is sound and
  complete, because the search is exhaustive. [p. 69–70]
- The thesis states that MCRL is sound but not complete, because it uses
  random simulation. Paper E holds the soundness proof. [p. 74, p. 315–316]
- In Paper B of the thesis, MCRL with internal Q-learning synthesizes a
  verified plan for 6 agents in 7.9 minutes. [p. 176]
- MoCReL, from Paper E of the thesis, compresses verified strategies to
  0.05% of their original size, a saving of up to 99.95%. [p. 30, p. 75,
  p. 321]
- The thesis verifies collision avoidance with UPPAAL SMC when obstacles are
  stochastic, and with exhaustive model checking when obstacles are
  non-deterministic. [p. 78–79]
- The thesis proves that a reach-avoid pass on a discrete-time trajectory
  implies a pass on the nonlinear trajectory, under two assumptions. The
  tracking errors must have a Lyapunov function, and the sampling period must
  satisfy ε ≤ L/‖V‖. [p. 80, p. 342–345]
- In Paper F of the thesis, model checking finds two faults in a dipole
  flow field collision-avoidance algorithm. The improved algorithm passes
  with one moving obstacle and fails with two. [p. 82, p. 351–352]
- The toolset MALTA has a GUI front end, a path-planning middleware, and a
  task-scheduling back end. MALTA is public at github.com/rgu01/MALTA.
  [p. 29, p. 82–84]
- In MALTA, path-finding time grows linearly with agents and milestones.
  Task-scheduling time grows exponentially with agents. [p. 84, p. 86]
- The thesis uses only algorithmic formal methods. It does not consider
  deductive verification. [p. 53]
- An errata sheet at the end of the PDF corrects the meaning of
  "completeness" in Table 9.4 and removes one example in Paper E. [p. 369]

## Questions this thesis answers

**What is the overall research problem?** How to synthesize
correctness-guaranteed mission plans for multi-agent systems, and verify
their reach-avoid behavior during execution, with scalability as the number
of agents grows. [p. 53]

**Why two layers?** Mission planning needs only discrete facts: milestones,
tasks, and static obstacles. Collision avoidance needs continuous motion and
moving obstacles. The two layers give a separation of concerns. [p. 26–27,
p. 59–61]

**Which method fits which environment?** A deterministic environment uses
TAMAA in UPPAAL. A non-deterministic environment uses TAMAA in UPPAAL TIGA,
or MCRL for more agents. A stochastic environment uses MCRL with statistical
model checking. [p. 66–67, p. 74]

**How does learning keep a correctness guarantee?** Q-learning produces a
strategy. The UPPAAL STRATEGO model checker then verifies the liveness query
`A<> φ under σ`, where only the highest-score actions of the strategy are
explored. A failed check starts a new learning round with more samples.
[p. 71–74]

**How does strategy compression work?** MoCReL labels each state-action pair
that the model checker visits. After a pass, it deletes the unlabeled pairs.
[p. 75]

**How is an undecidable hybrid problem made decidable?** A two-step proven
reduction goes from the nonlinear trajectory to a piece-wise-continuous
reference trajectory, and then to a sampled discrete-time trajectory.
UPPAAL STRATEGO checks the discrete-time model. [p. 79–81, p. 338–345]

**How is the collision-avoidance code put into the model?** The algorithm is
a C library, for example a DLL or a shared object. UPPAAL STRATEGO calls it
as a black box during model checking. [p. 81]

**What is the industrial evidence?** Experiments on models of an autonomous
quarry from Volvo Construction Equipment, with wheel loaders, trucks,
crushers, and chargers. [p. 32, p. 84]

## Scope: what this thesis does not do

- It does not use deductive methods such as theorem proving. [p. 53]
- It does not give a complete learning-based synthesis. MCRL and MoCReL can
  fail to find a plan that exists. [p. 74]
- It does not handle collisions between agents in mission planning. The
  static layer leaves agent-agent and moving-obstacle avoidance to the
  dynamic layer. [p. 65, p. 150]
- It does not compute the tracking-error bounds. It takes them from the
  method of Fan et al. [p. 81, p. 342]
- It does not show safety with two or more moving obstacles. The improved
  algorithm fails that case. [p. 352]
- It does not run the two layers together in real time. Real-time
  communication between the layers is future work. [p. 97]
- It reports experiments on models of the quarry. It reports no run on a
  real machine.
- It prints no DOI for the thesis.

## Research goals and research questions

The overall goal: "Determine how algorithmic formal methods can be employed
and scaled up to synthesize and verify autonomous systems with respect to
mission planning and dynamic collision avoidance." [p. 53]

| Subgoal | Statement (short form) | Page |
|---|---|---|
| Subgoal 1 | Decouple mission planning from the continuous operation of the agents, with model checking support | p. 53 |
| Subgoal 2 | For deterministic, stochastic, and non-deterministic environments, identify suitable planning methods and evaluate them | p. 54 |
| Subgoal 3 | Give scalable model-checking-based plan synthesis and compression for MAS, with reasonable time for many agents | p. 54 |
| Subgoal 4 | Ensure the reach-avoid requirement during plan execution with unforeseen static and dynamic obstacles | p. 54–55 |
| Subgoal 5 | Give automated tool support that integrates synthesis and verification, and assess it on an industrial case | p. 55 |

Chapter 3 also asks these research questions. The labels RQ-MP to RQ-RA3
are labels of this summary, not of the thesis. [p. 52–53]

- **RQ-MP.** How to find paths that avoid static obstacles, and schedule
  movement and tasks so that agents finish all tasks in time and obey task
  constraints?
- **RQ-S.** How to find a scalable method for this computation?
- **RQ-RA1.** With no moving obstacle, how to ensure that agents follow
  their planned paths closely enough to avoid collisions?
- **RQ-RA2.** With moving obstacles, how to ensure that agents deviate from
  their paths in time to avoid collisions?
- **RQ-RA3.** After a deviation, how to ensure that agents still reach their
  destinations?

The introduction also names four challenges, each with one contribution
section: (i) the gap between discrete planning and continuous avoidance,
Section 5.1; (ii) state-space explosion with many agents and different
environments, Section 5.2; (iii) undecidable hybrid models, Section 5.3; and
(iv) timing requirements in industrial cases, Section 5.4. [p. 26–27]

## Map: goals, questions, contributions, papers

| Subgoal | Research questions | Contribution (Part I section) | Papers (Table 5.3) | Main evidence |
|---|---|---|---|---|
| 1 | Overall problem | Two-layer framework and communication between the layers (5.1) | A, D | Framework in Paper A; travel-time estimation from the dynamic layer feeds a stochastic plan in Paper D [p. 60–63] |
| 2 | RQ-MP | Planning problem defined uniformly; methods per environment type (5.2, Table 5.1) | B | Strengths and weaknesses of TIGA and MCRL [p. 66–67, p. 176–179] |
| 3 | RQ-MP, RQ-S | TAMAA, MCRL, MoCReL (5.2.1–5.2.4) | B, C, D, E | MCRL for 6 agents; MoCReL soundness theorem and 99.95% compression [p. 176, p. 315, p. 321] |
| 4 | RQ-RA1, RQ-RA2, RQ-RA3 | Pattern-based hybrid models; Solution A (SMC); Solution B (proven discrete-time reduction) (5.3) | A, F | SMC probabilities in Paper A; Theorems and Table 13.1 in Paper F [p. 131–132, p. 342–351] |
| 5 | Tool and industrial use | MALTA and the external-library verification approach (5.4) | B, C, F | Quarry experiments [p. 84–86, p. 229–248] |

Sources: Table 5.3 and Section 5.5. [p. 86–88]

## The two-layer framework

- **Static layer.** It does mission planning from known information:
  static obstacles and milestones, which are positions where tasks happen.
  [p. 28, p. 60]
- **Dynamic layer.** It simulates and verifies agents that follow the
  reference path and avoid unforeseen static and moving obstacles. The
  models are hybrid automata built from reusable patterns. [p. 28, p. 61,
  p. 76–77]
- **Communication.** The dynamic layer can send a new map back to the static
  layer for re-planning. In Paper D, SMC estimates the travel time through a
  crossing with pedestrians. That estimate becomes a stochastic movement
  model for planning. [p. 61–63]
- **Example.** In the crossing example, the route via B2 takes 10 time units
  with 40% probability and 18 time units with 60% probability. The route via
  B1 takes a fixed 15 time units. [p. 63]

## Mission planning methods

| Method | Model | Game | Technique | Sound | Complete | Source |
|---|---|---|---|---|---|---|
| TAMAA | UTA | 1-player | Model checking in UPPAAL, fastest trace | Yes | Yes | p. 67–69 |
| TAMAA in TIGA | TG | 2-player | Symbolic on-the-fly algorithm | Yes | Yes | p. 69–70 |
| MCRL | TG and STG | 2-player | Reinforcement learning plus model checking | Yes | No | p. 71–74 |
| STRATEGO | STG | 1½-player | Reinforcement learning | — | — | p. 67 |
| MoCReL | TG and STG | 2-player | MCRL plus labeling and cleaning of the strategy | Yes (Theorem 2) | No | p. 74–75, p. 315 |

Source: Table 5.1 and Sections 5.2.1–5.2.4. The "Sound" and "Complete"
columns come from the text, not from Table 5.1. "—" means that the thesis
does not state it.

Key queries in the summary:

- TAMAA timing: `E<> ((forall(i:int[0,N-1]) ite[i]>=M) && x<=TL)`. All N
  agents finish M rounds of their tasks within TL time units. [p. 68]
- MCRL liveness: `A<> φ`, and in UPPAAL STRATEGO `A<> φ under σ`. [p. 72–73]
- In the TAMAA traces, two agents can be at the same milestone but cannot
  do the same mutually exclusive task. [p. 69]

UPPAAL TIGA scalability, 3 tasks among 3 milestones (Table 5.2) [p. 70]:

| Agents | Explored states | Time |
|---|---|---|
| 2 | 775 | 5 ms |
| 3 | 222,88 (as printed) | 220 ms |
| 4 | 764,001 | 18.1 s |
| 5 | 33,312,229 | 53.8 min |
| 6 | Out of memory (2 GB on Windows 10) | Unknown |

## Reach-avoid verification of nonlinear agents

The reach-avoid requirement: each agent travels from its initial area to its
goal area with no collision. [p. 31, p. 77] Two difficulties exist. The
planned path has sharp turns that cause tracking errors, and a moving
obstacle can cross the real trajectory. [p. 77]

**Solution A, statistical model checking (Paper A).** UPPAAL SMC samples
runs of the hybrid automata and gives a probability. Example queries:
`Pr[<=70](<> arrived && counter<=60)` and `Pr[<=110]([] !collided)`. The
thesis uses UPPAAL SMC 4.1.24 here. [p. 78] The method fits stochastic
obstacles, not non-deterministic ones. [p. 79]

**Solution B, exhaustive model checking (Paper F).** [p. 79–82]

- Step 1: if the tracking errors have a Lyapunov function, the real
  trajectory stays within distance L of the reference path (result of Fan et
  al.). [p. 80, p. 342]
- Step 2: sampling with period ε ≤ L/‖V‖ preserves the reach-avoid result.
  Here L = La + Lo, La is the tracking-error bound of the vehicle, Lo is the
  smallest bound among the dynamic obstacles, and V is the maximum obstacle
  velocity. [p. 80, p. 344]
- The discrete-time model is UPPAAL timed automata. The obstacles take
  non-deterministic start states. Each obstacle keeps a target for N sampling
  periods. [p. 343–344]
- Obstacles in the "closest area" cannot be avoided by any algorithm, so the
  model excludes them. Obstacles outside the "valid area" cannot reach the
  safety-critical area in the current detection period. [p. 349]
- A "true" result means that the agents satisfy reach-avoid under the
  current parameters. A "false" result gives a counterexample. [p. 81]

## Tool support: MALTA

- Front end: the GUI MMT, where users set the map, milestones, tasks, and
  agents. [p. 82–83]
- Middleware: path planning with A*, Theta*, DALi, and two improved DALi
  versions. DALi handles temporary forbidden areas and preferred areas
  ("heat" maps). [p. 84]
- Back end: TAMAA task scheduling with UPPAAL. Path planning and scheduling
  iterate until all environment constraints hold. [p. 84]
- MALTA uses a client-server design so that the expensive synthesis can run
  on a server. [p. 82–83]

## Included papers

Venue strings are as printed in the List of Publications. [p. 15–16]
Author contribution statements are on p. 33–37.

| Paper | Title | Venue as printed | Chapter pages |
|---|---|---|---|
| A | Towards a Two-Layer Framework for Verifying Autonomous Vehicles | NASA Formal Methods Symposium (NFM) 2019, LNCS 11460, pp. 186–203, Houston | p. 113–138 |
| B | Verifiable Strategy Synthesis for Multiple Autonomous Agents: A Scalable Approach | STTT, Special Issue FMICS 2019/2020, pp. 1–20, Springer, 2022 | p. 139–188 |
| C | Synthesis and Verification of Mission Plans for Multiple Autonomous Agents under Complex Road Conditions | Submitted to ACM TOSEM, 2022 | p. 189–258 |
| D | Probabilistic Mission Planning and Analysis for Multi-agent Systems | ISoLA, LNCS 12476, pp. 350–367, Rhodes, 2021 | p. 259–286 |
| E | Correctness-Guaranteed Strategy Synthesis and Compression for Multi-Agent Autonomous Systems | Submitted to Science of Computer Programming (SCP), Elsevier, 2022 | p. 287–330, Appendix A p. 359–365 |
| F | Model Checking Collision Avoidance of Nonlinear Autonomous Vehicle Models | FM 2021, LNCS 13047, pp. 676–694, online | p. 331–358 |

Related papers that are not included [p. 16]: FormaliSE 2018, "Formal
Verification of an Autonomous Wheel Loader by Model Checking"
(see `2018-formalise-autonomous-wheel-loader.md`); SAC 2020, "TAMAA:
UPPAAL-based Mission Planning for Autonomous Agents"
(see `2020-sac-tamaa-mission-planning.md`); and FMICS 2020, "Verifiable and
Scalable Mission-Plan Synthesis for Multiple Autonomous Agents", which
received a Best Paper Award (see `2020-fmics-mission-plan-synthesis.md`).

These files give separate summaries of the included papers:

| Paper | Summary file |
|---|---|
| A (NFM'19) | `2019-nfm-two-layer-framework-autonomous-vehicles.md` |
| B (STTT'22) | `2022-sttt-verifiable-strategy-synthesis.md` |
| C (TOSEM) | `2024-tosem-mission-plans-complex-road-conditions.md` |
| D (ISoLA'21) | `2021-isola-probabilistic-mission-planning.md` |
| E (SCP) | `2022-scp-strategy-synthesis-compression.md` |
| F (FM'21) | `2021-fm-collision-avoidance-nonlinear-vehicles.md` |

The notes below give only the role of each paper in the thesis.

### Paper A (NFM 2019)

- **Authors:** Rong Gu, Raluca Marinescu, Cristina Seceleanu, Kristina
  Lundqvist. [p. 113]
- **Contribution statement:** Gu was the main driver, wrote most of the
  text, implemented the model, and did the case study. [p. 33]
- **Main result:** It proposes the two-layer framework and models the
  dynamic layer as hybrid automata in UPPAAL SMC, with patterns. It uses
  Theta* for paths and dipole flow fields for avoidance. On a 55 × 55 map with
  5 static obstacles, 2 predefined moving obstacles, and 1 generated moving
  obstacle, the path-following and no-collision queries each hold with
  probability in [0.902606, 1] at 95% confidence from 36 runs. [p. 130–132]

### Paper B (STTT 2022)

- **Authors:** Rong Gu, Peter G. Jensen, Danny B. Poulsen, Cristina
  Seceleanu, Eduard Enoiu, Kristina Lundqvist. [p. 139]
- **Contribution statement:** Gu was the primary driver and wrote most of
  the text. Jensen and Poulsen (Aalborg University) did the technical part
  of UPPAAL STRATEGO. [p. 34]
- **Main result:** It extends the FMICS 2020 paper with TAMAA in UPPAAL
  TIGA and MCRL 2.0 inside UPPAAL STRATEGO. [p. 143, p. 184] With 3 milestones and
  3 tasks, TIGA fails at 6 agents, and MCRL with internal Q-learning needs
  7.9 minutes (external: 14.8 minutes). [p. 176] With 2 agents and 10
  milestones, TIGA needs 3.9 s and MCRL needs 33.7 to 46.4 minutes. [p. 178]
  The paper advises MCRL for many agents and TIGA for many milestones and
  tasks. [p. 179] Experiments ran on a 12-core Intel Core i7 laptop with
  16 GB RAM. [p. 174]

### Paper C (submitted to TOSEM)

- **Authors:** Rong Gu, Eduard Baranov, Afshin Ameri, Eduard Enoiu, Baran
  Cürüklü, Cristina Seceleanu, Axel Legay, Kristina Lundqvist. [p. 189]
- **Contribution statement:** Gu was the primary driver. Baranov designed
  and described DALi. Ameri and Cürüklü did the MMT front end. [p. 35]
- **Main result:** It combines DALi path planning with TAMAA task
  scheduling in MALTA, with a validator and an iteration for temporary
  obstacles. [p. 193] It asks six research questions: path planning, task
  scheduling, mission planning, automation, adaptability, visualization.
  [p. 192–193] With a 1-hour timeout, UPPAAL times out at 3 agents with 5
  milestones and at 4 agents with 3 milestones. [p. 241] An adapted quarry
  case gives a fastest plan of 6.9 minutes for three trucks that carry 90
  tons. [p. 247]

### Paper D (ISoLA 2021)

- **Authors:** Rong Gu, Eduard Enoiu, Cristina Seceleanu, Kristina
  Lundqvist. [p. 259]
- **Contribution statement:** Gu was the primary driver and wrote most of
  the text. [p. 36]
- **Main result:** It runs MCRL on stochastic timed automata in UPPAAL SMC
  with a Java Q-learning program. [p. 276] Task assignment, execution order,
  milestone exclusion, and timing queries each give probabilities above
  99.8%, with α = 0.001 and ε = 0.001. [p. 275–277] It also shows bottleneck
  analysis (milestone D has the highest waiting probability) and re-planning
  when pedestrians block one route. [p. 277–281]

### Paper E (submitted to SCP)

- **Authors:** Rong Gu, Peter G. Jensen, Cristina Seceleanu, Eduard Enoiu,
  Kristina Lundqvist. [p. 287]
- **Contribution statement:** Gu was the primary driver and wrote most of
  the text. Jensen (Aalborg University) did the technical part of UPPAAL
  STRATEGO. [p. 36–37]
- **Main result:** It defines MoCReL and proves two theorems. Theorem 1:
  the outcomes of the stochastic strategy are a subset of the outcomes of
  its non-deterministic abstraction. [p. 308] Theorem 2: if MoCReL returns a
  strategy σc, then `G | σc |= A<> φ` (soundness). [p. 315–316] In Table
  12.1, 21 listed models give 17 verified strategies and 4 failures. Up to 6
  agents and up to 6 crushers occur. [p. 318–319] Compression saves up to
  99.95%. In game4-A, about 78,000 rows shrink to fewer than 50. [p. 321]

### Paper F (FM 2021)

- **Authors:** Rong Gu, Cristina Seceleanu, Eduard Enoiu, Kristina
  Lundqvist. [p. 331]
- **Contribution statement:** Gu was the primary driver, proved the
  theorems, built the models, did the experiments, and wrote most of the
  text. [p. 37]
- **Main result:** It proves the reduction from nonlinear to PWC
  trajectories (Theorem 3) and from PWC to discrete-time trajectories
  (Theorem 4). [p. 342–345] Verification of a dipole flow field library in
  UPPAAL 4.1.20-stratego-7 finds two faults: the field can pull the vehicle
  toward a slower obstacle, and a head-on approach causes a livelock. [p.
  349, p. 351–352] The improved algorithm passes S1 to S4 with one obstacle.
  It fails obstacle avoidance in S5 with two obstacles. [p. 351–352]

Paper F verification results, improved algorithm (Table 13.1) [p. 351]:

| S | WP | TT | DO | VA | Avoid: states | Avoid: time | Avoid | Reach: states | Reach: time | Reach |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | 2 | 25 | 1 | 1 | 547,617 | 2.7 s | true | 545,505 | 5.5 s | true |
| S2 | 6 | 25 | 1 | 1 | 411,747 | 1.8 s | true | 411,168 | 3.6 s | true |
| S3 | 2 | 85 | 1 | 1 | 3,222,290 | 15.3 s | true | 3,217,767 | 31.8 (no unit) | true |
| S4 | 2 | 15 | 1 | 3 | 12,317,809 | 1.0 min | true | 12,498,924 | 2.1 min | true |
| S5 | 2 | 15 | 2 | 1 | 1,398,011 | 7.6 s | false | 226,896,902 | 43.2 min | true |

WP is waypoints, TT is travel time, DO is dynamic obstacles, VA is allowed
obstacle velocities. S3 is also split into three phases, S3.1 to S3.3, which
all pass. [p. 350–351] Reach holds in S5 because the vehicle model does not
stop after a collision. [p. 352]

## Research methods

The research process has five steps: formulate goals from industrial
problems, review literature, propose approaches, implement a prototype tool,
and evaluate on an industrial case. [p. 57–58] The methods are critical
analysis of literature, proof of concept, proof by demonstration, and
mathematical modeling and proof. [p. 57–58]

## Limitations stated in the thesis

- TAMAA in UPPAAL and in UPPAAL TIGA cannot solve problems with more than 5
  agents. [p. 70–71, p. 95–96]
- MCRL is not complete. [p. 74]
- When the goal is a rare event for random simulation, reinforcement
  learning finds results only with great difficulty. [p. 97, p. 320]
- MCRL performs worse than TIGA with many milestones and tasks. [p. 177–179]
- Statistical model checking does not fit non-deterministic obstacles.
  [p. 79]
- Solution B shows the absence of collisions only with one moving obstacle.
  [p. 82, p. 352]
- UPPAAL does not support hierarchical models, so the thesis uses patterns.
  [p. 77, p. 97]

## Future work stated in the thesis

- Make the two layers communicate in real time. [p. 97]
- Use a counterexample-guided method to help reinforcement learning with
  rare goals. [p. 97]
- Decompose the system into smaller sub-systems for scalable synthesis.
  [p. 97]
- Study agents with more complex kinematics and dynamics. [p. 97]
- Adapt barrier certificates or bounded model checking for engineers.
  [p. 97]

## Related work, as the thesis positions itself

- **Multi-layer frameworks.** Belta et al., Bhatia et al., Dimarogonas et
  al., and Saddem et al. The thesis claims that few of these put planning and
  reach-avoid verification in separate layers with suitable formal methods,
  and that its layer communication is bidirectional. [p. 89–90]
- **Mission planning.** The thesis uses TCTL instead of LTL, so that it can
  express timing requirements. It contrasts MCRL with RL-plus-verification
  work (Behjati et al., Bouton et al., Jothimurugan et al., Brázdil et al.,
  Legay et al.). MCRL uses RL to reduce state-space explosion. [p. 90–91]
- **UPPAAL-based planners.** Andersen et al. use only reachability queries.
  PuRSUE (Bersani et al.) handles only 2 robots. [p. 91]
- **Strategy compression.** dtControl (Ashok et al.) and neural or origami
  compression (Julian et al.) change the representation. MoCReL deletes
  unused data and gets correctness from exhaustive model checking. [p. 92]
- **Agent verification.** Automata-based methods, runtime verification,
  and KeYmaera theorem proving (Mitsch et al., Abhishek et al.). The thesis
  claims a proven reduction to a decidable discrete-time problem. [p. 92–93]

## Reviewer notes

These notes are a reading of the thesis, not claims from it.

**Requirement fidelity and what the verification proves**

- The reach-avoid requirement becomes two properties: an invariance (no
  collision) and a liveness (reach the goal). [p. 337] The no-collision
  check uses distances to obstacles, not vehicle shapes. In Paper A, a
  collision is a distance below 0.8. [p. 132]
- The Solution B reduction is only sufficient. Paper F states "without
  losing completeness" [p. 334]. The note after Theorem 3 says that the two
  problems are not equivalent [p. 342]. A "false" result can therefore be a
  false alarm, while a "true" result is safe under the assumptions.
- The proof of Solution B rests on assumptions: a Lyapunov function for the
  tracking error, the bound L from an external method, the sampling bound,
  obstacles that keep a target for N periods, and the exclusion of
  unavoidable obstacles. [p. 80, p. 343–344, p. 349] A pass says nothing
  about obstacles outside these assumptions.
- The MCRL guarantee is the liveness query under the strategy, `A<> φ under
  σ`. [p. 73] Other requirements, such as timing, enter through φ or the
  model, so each claim of correctness is relative to the chosen φ.
- The TAMAA timing query is a reachability query, `E<>`. [p. 68] This fits
  a 1-player game, where agents control all choices. It gives no guarantee
  against environment choices.
- The static layer assumes that the dynamic layer avoids agents and moving
  obstacles correctly. [p. 150] The dynamic layer assumes the planned path.
  The thesis gives no proof of the composition of the two layers.
- The SMC results are estimates. Paper A uses only 36 runs, which gives a
  lower bound of about 0.90 at 95% confidence. [p. 131–132]
- The thesis counts more than four agents as large [p. 54]. Volvo CE states
  2 to 8 agents [p. 299]. The reported experiments reach 6 agents. [p. 176,
  p. 319]

**AI and machine-learning aspects**

- The thesis uses Q-learning to synthesize strategies and model checking to
  verify them afterward. This is a "learn, then verify" pattern. [p. 71–74]
- The compressed strategies are smaller and easier for humans to read.
  [p. 321]
- The thesis has no large language models.

**Inconsistencies inside the PDF**

- Section 1.4 promises "conclusions, limitations and future work" in
  Chapter 7 [p. 33], but Chapter 7 has no separate limitations section.
  [p. 95–97]
- Part I says Theorem 1 and Theorem 2 in Paper F [p. 80]. In the thesis copy
  of Paper F, they are Theorem 3 and Theorem 4 [p. 342, p. 344]. Paper F
  then says "Based on Theorems 1 and 2". [p. 345]
- Chapter 4 says Paper B holds the mathematical proof of the synthesis
  methods. [p. 58] Paper B has no numbered theorem. The soundness theorem is
  in Paper E. [p. 315]
- Table 9.4 calls the strategies "complete" [p. 177]. The errata limits
  this to the satisfaction of the liveness query, and states that MCRL is not
  complete as a method. [p. 369]
- The errata also removes the example after Theorem 1 in Paper E, because
  both runs are possible in both strategy kinds. [p. 309, p. 369]
- The explored states for 3 agents in TIGA print as "222,88". [p. 70,
  p. 176]
- The Paper B conclusion says TIGA is better "when the number of agents is
  less than two". The matching experiment uses 2 agents. [p. 178, p. 181]
- Paper D gives 83% for the fast route and 33% for the slow route. The two
  values add to 116%. [p. 280]
- In Table 12.1, game1-B has an original size of 0.02 MB and a compressed
  size of 0.1 MB. [p. 319] The text says 41 of 50 cases pass, but the table
  lists 21 models. [p. 320]
- The thesis bibliography gives Paper D as 2020 [p. 102]. The List of
  Publications gives 2021. [p. 15] The bibliography entry for Paper E adds
  Danny Poulsen and a shorter title. [p. 102, p. 16]
- Paper C leaves the integration of MCRL into MALTA as future work [p. 241].
  Part I says that MCRL is adopted in MALTA in Paper B. [p. 88]
- Table 5.1 gives the 1½-player game to UPPAAL STRATEGO [p. 67]. Section
  5.2.3 and Paper D solve it with MCRL, UPPAAL SMC, and a Java Q-learning
  program. [p. 74, p. 276]

## Terms

| Term | Meaning in this thesis |
|---|---|
| Agent | An autonomous system that moves and does tasks with little or no human help |
| MAS | Multi-agent autonomous systems |
| Mission planning | Path finding plus task scheduling: an order of movement and task actions that meets the requirements |
| Milestone | A position where an agent does a task |
| Reach-avoid requirement | Each agent reaches its goal area and never collides with static or moving obstacles |
| Static layer | The framework layer for discrete mission planning |
| Dynamic layer | The framework layer for continuous motion and collision avoidance |
| UTA | UPPAAL timed automata: timed automata with data variables |
| TG | Timed game: a UTA whose actions are controllable or uncontrollable |
| STG | Stochastic timed game: a TG whose environment chooses with probabilities |
| HA | Hybrid automata: automata with continuous variables defined by differential equations |
| 1-player game | The agents control all actions and timing (deterministic environment) |
| 1½-player game | The environment ends actions at random times (stochastic environment) |
| 2-player game | The environment ends actions at any time in an interval (non-deterministic environment) |
| Strategy | A function that tells the agents which action or delay to take in each state; here the mission plan |
| Sound | Every result the method returns is correct |
| Complete | The method finds a result whenever one exists |
| TAMAA | The thesis method that generates UTA and uses UPPAAL to find the fastest plan |
| MCRL | Model Checking + Reinforcement Learning: learn a strategy, then model-check it |
| MoCReL | Model-checked Compressed Reinforcement Learning: MCRL plus removal of unused state-action pairs |
| MALTA | The toolset that integrates path planning, model generation, and task scheduling |
| MMT | Mission Management Tool, the GUI front end of MALTA |
| DALi, DALi* | A path-planning algorithm for complex road conditions, and its faster version with an A* heuristic |
| Theta* | An any-angle grid path planner, based on A*, with line-of-sight checks |
| Dipole flow field | A collision-avoidance method. Static fields pull the agent to its path and push it from obstacles. Dipole fields push moving objects apart. |
| Q-learning | A model-free reinforcement-learning algorithm. Its Q-table is the strategy. |
| SMC | Statistical model checking: random simulation that estimates a probability with a confidence level |
| Tracking error | The distance between the real trajectory and the reference path |
| Lyapunov function | A function that shows that the tracking error stays bounded |
| PWC trajectory | Piece-wise-continuous reference trajectory between waypoints |
| `A<> φ under σ` | The UPPAAL STRATEGO query: φ eventually holds on all paths when the agents follow strategy σ |
| BCET, WCET | Best-case and worst-case execution time of an action |

## Citation

Rong Gu. "Formal Methods for Scalable Synthesis and Verification of
Autonomous Systems: Mission Planning and Collision Avoidance." Doctoral
dissertation, Mälardalen University Press Dissertations No. 359, Mälardalen
University, Västerås, Sweden, 2022. ISBN 978-91-7485-552-4.
