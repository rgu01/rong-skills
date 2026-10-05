---
id: gu2022sttt-verifiable-strategy-synthesis
title: "Verifiable strategy synthesis for multiple autonomous agents: a scalable approach"
authors:
  - Rong Gu
  - Peter G. Jensen
  - Danny B. Poulsen
  - Cristina Seceleanu
  - Eduard Enoiu
  - Kristina Lundqvist
affiliation: Mälardalen University, Västerås, Sweden (Gu, Seceleanu, Enoiu, Lundqvist); Aalborg University, Ålborg, Denmark (Jensen, Poulsen)
year: 2022
venue: International Journal on Software Tools for Technology Transfer (STTT), vol. 24, pp. 395–414, Special Issue FMICS 2019/2020
venue_source: PDF, p. 1
doi: 10.1007/s10009-022-00657-z  # printed on PDF p. 1
document_type: journal article
pages_in_pdf: 20
pdf_url: https://link.springer.com/article/10.1007/s10009-022-00657-z
listing_url: https://sites.google.com/view/ronggu/publications
author_keywords: [autonomous agents, synthesis, model checking, reinforcement learning]
topics: [mission planning, strategy synthesis, multi-agent systems, task scheduling, path planning, timed games, reinforcement learning, post-verification of learned strategies, state-space explosion, construction machinery]
formalisms: [timed automata, timed games, stochastic timed games, timed Markov decision processes, TCTL]
tools: [UPPAAL, UPPAAL TIGA, UPPAAL STRATEGO, UPPAAL SMC, TAMAA, MALTA]
algorithms: [Q-learning, Theta*, A*, DALi, symbolic on-the-fly timed-game algorithm]
application: autonomous quarry with autonomous trucks and wheel loaders
abbreviations: {TA: timed automata, UTA: UPPAAL timed automata, TG: timed games, STG: stochastic timed games, TMDP: timed Markov decision process, TCTL: Timed Computation Tree Logic, MCRL: Model Checking + Reinforcement Learning, TAMAA: Timed-Automata-based Mission planner for Autonomous Agents, MMT: Mission Management Tool, RL: reinforcement learning, BCET: best-case execution time, WCET: worst-case execution time, EST: execution statuses of tasks}
funding: Swedish Knowledge Foundation, DPAC profile grant 20150022 and ACICS synergy grant 20190038; open access funding by Mälardalen University
---

# Verifiable Strategy Synthesis for Multiple Autonomous Agents: A Scalable Approach (Gu et al., STTT 2022)

## At a glance

This 2022 journal article by Gu, Jensen, Poulsen, Seceleanu, Enoiu, and
Lundqvist synthesizes mission plans for many autonomous agents. A mission
plan combines path planning and task scheduling. The paper gives two
solutions. Solution 1 recasts the TAMAA timed-automata models as timed
games and solves them in UPPAAL TIGA. Solution 2 is a new version of MCRL
inside UPPAAL STRATEGO: Q-learning learns a strategy from simulation, and
exhaustive model checking then verifies the learned strategy. The authors
extend UPPAAL STRATEGO so that it can verify strategies learned without
clocks. On an autonomous-quarry case, UPPAAL TIGA runs out of memory at 6
agents. Both MCRL versions synthesize verified strategies for 6 agents in
7.9 or 14.8 minutes. With 2 agents and 8 or 10 milestones, UPPAAL TIGA is
much faster than MCRL.

Page references `[p. N]` point to the 20-page PDF. PDF page N is printed
journal page N + 394.

## Key facts

Each fact is a claim from the paper unless it is marked otherwise.

- The STTT 2022 article is an extension of the authors' FMICS 2020 paper
  on MCRL. [p. 2]
- The STTT 2022 article states two limits of the earlier TAMAA tool: it
  cannot cover uncertain durations, and it does not scale with the number
  of agents. [p. 2]
- TAMAA handles up to 100 milestones and tasks, but it exhausts physical
  memory with more than 5 agents. [p. 6]
- Solution 1 of the STTT 2022 article marks the arrival edges and the
  task-finish edges as uncontrollable, so the environment decides the
  durations. [p. 9]
- The STTT 2022 article states that UPPAAL TIGA is sound and complete: a
  synthesized strategy is correct by construction, and UPPAAL TIGA finds a
  strategy if one exists. [p. 6]
- MCRL in the STTT 2022 article is not complete: it does not guarantee to
  find a strategy even if one exists. [p. 7]
- In the new MCRL, each good simulation run goes to Q-learning at once,
  and the intermediary strategy biases the next simulation runs. [p. 10–11,
  p. 15]
- The STTT 2022 article defines a Q-state as <RT, CT, CP, ST> and a
  Q-action as <MT, TT>. Neither one contains clocks. [p. 12]
- The authors extend UPPAAL STRATEGO so that the query `A<> P under opt`
  can verify learned strategies that have no clock variables. [p. 13]
- During verification, the model checker explores all actions with the
  highest Q-value and ignores actions with lower values. [p. 14–15]
- The learning algorithm can be an external C or C++ library, so users can
  replace Q-learning with their own algorithm. [p. 15]
- The STTT 2022 experiments run on a laptop with an Intel Core i7 with 12
  cores, 16 GB of RAM, and 64-bit Linux. Each result is the mean of 5 runs.
  [p. 15–16]
- With 3 milestones and 3 tasks, UPPAAL TIGA needs 53.8 minutes for 5
  agents and runs out of memory for 6 agents. [p. 17]
- For 6 agents, MCRL with internal Q-learning needs 7.9 minutes, and MCRL
  with external Q-learning needs 14.8 minutes. [p. 17]
- All MCRL strategies in Table 4 pass the post-verification for 4, 5, and 6
  agents. [p. 17]
- With 2 agents and 10 milestones and tasks, UPPAAL TIGA needs 3.9 seconds,
  but each MCRL version needs more than 33 minutes. [p. 17]
- The STTT 2022 article states that with 10 milestones and tasks, fewer
  than 10% of the MCRL attempts give complete strategies. [p. 16]
- The MALTA toolset is at https://github.com/rgu01/MALTA. [p. 14]

## Questions this paper answers

**What problem does the article solve?** It synthesizes path and task
plans for many agents when movement and task durations are uncertain. It
also proves that the plans meet the requirements. [p. 2, p. 6]

**What is new compared with the FMICS 2020 MCRL?** Three changes. MCRL now
runs inside UPPAAL STRATEGO. Sampling and learning are merged, so the
intermediary strategy guides the simulation. The model checker verifies
the original timed games under the learned strategy, without a "conductor"
automaton. [p. 2–3, p. 15]

**How is a learned strategy made trustworthy?** UPPAAL STRATEGO model
checks the timed-game model under the strategy with exhaustive search. If
the check fails, the user runs a new round with more simulation runs.
[p. 11]

**Why is the verification still exhaustive if learning uses
probabilities?** The probabilities exist only in the learning model (STG).
The verification uses the timed game, where uncontrollable actions are
nondeterministic. [p. 4, p. 12]

**When should a user pick which method?** Many agents: MCRL with internal
Q-learning. Many milestones and tasks: UPPAAL TIGA. A user-supplied
learning algorithm: MCRL with external Q-learning. [p. 17]

**How large were the experiments?** Up to 6 agents with 3 milestones, and
up to 10 milestones with 2 agents. [p. 17]

## Scope: what this article does not do

- It does not handle collision avoidance between agents or with dynamic
  obstacles. It assumes that this function works. [p. 5]
- It does not put clocks or other continuous variables in Q-states or
  strategies. The authors list continuous variables as future work.
  [p. 12, p. 18]
- It does not estimate in advance whether a strategy exists. That is
  future work. [p. 18]
- It does not compare MCRL with methods outside the authors' toolchain on
  the same benchmarks.
- It does not report how often MCRL fails to produce a strategy, except for
  the 10-milestone remark. [p. 16]
- It does not use negative rewards for failed runs. The authors expect that
  such penalties would improve MCRL. [p. 17]

## Case study and requirements

The case study is an autonomous quarry from VOLVO Construction Equipment.
Wheel loaders dig stones and load trucks. Trucks carry stones to primary
crushers and then carry the crushed stones to secondary crushers. A sample
production requirement is 1500 m³ of stones per day. [p. 5]

The authors state three task requirements from the industrial partner.
[p. 6]

1. **Milestone matching.** Tasks must be done at the right milestones, for
   example digging at stone piles.
2. **Task sequencing.** The task order must be correct. For example,
   unloading into the primary crusher comes after digging and before
   loading.
3. **Timing.** All tasks that contribute to the goal must finish within a
   prescribed time, for example 1 hour.

The two uncertainties are task execution time between BCET and WCET, and
movement time that includes waiting at exclusive milestones. [p. 6]

## Methods compared

| | TAMAA | TIGA | MCRL | STRATEGO |
|---|---|---|---|---|
| Model | UTA | TG | TG & STG | STG |
| Game | 1 player | 2 player | 2 player | 1½ player |
| Technique | Model checking | Symbolic on-the-fly algorithm | Reinforcement learning & model checking | Reinforcement learning |

Source: Table 1. [p. 7]

- In a 1-player game, the agents control everything. TAMAA finds the run
  that finishes all tasks fastest. [p. 6]
- In a 2-player game, the environment chooses uncontrollable actions
  nondeterministically. The goal is a strategy that wins for every
  environment choice. [p. 6]
- In a 1½-player game, the environment chooses stochastically. The goal is
  the strategy with the highest probability to finish all tasks. [p. 6]

## Formal definitions

| No. | Definition | Content |
|---|---|---|
| 1 | Timed automaton | A = <L, l0, X, Σ, E, I> [p. 3] |
| 2 | Strategy | A partial function from finite runs to a controllable action or a delay λ [p. 3] |
| 3 | Stochastic timed game | A TMDP <G, μu>, with densities for uncontrollable actions after a delay [p. 4] |
| 4 | Stochastic strategy | A family of densities for controllable actions after a delay [p. 4] |
| 5 | Q-state | <RT, CT, CP, ST>: task iterations per agent, current task, current milestone, task execution statuses of all agents [p. 12] |
| 6 | Q-action | <MT, TT>: motion type (1 move, 2 execute a task) and target milestone or task [p. 12] |

The article uses memoryless and non-lazy winning strategies. Such a
strategy either picks a controllable action at once or waits for the
environment. [p. 3–4]

## Solution 1: timed-game synthesis with UPPAAL TIGA

- TAMAA builds a Cartesian grid, runs Theta* between milestones, and
  generates movement and task-execution automata. [p. 7–8]
- The guard to task T2 (unload at a primary crusher) needs four
  conditions: loading is done, the agent is at C or D, no other agent does
  this task, and the task is still needed in this round. [p. 8]
- The original TAMAA finds a run with the reachability query
  `E<> ((forall(i:int[0,N-1]) ite[i]>=M) && x ≤ TL)`. [p. 8]
- For UPPAAL TIGA, the arrival edges and the task-finish edges become
  uncontrollable. The synchronization between the two automata is replaced
  by a global Boolean array `idle`. [p. 9]
- The synthesis query is
  `strategy st = control: A<> ((forall(i:int[0,N-1]) ite[i] ≥ M) && x ≤ TL)`.
  [p. 9]

| Agents | Explored states | Computation time |
|---|---|---|
| 2 | 775 | 5 ms |
| 3 | 222,88 (as printed) | 220 ms |
| 4 | 764,001 | 18.1 s |
| 5 | 33,312,229 | 53.8 min |
| 6 | Out of memory | Unknown |

Source: Table 2, UPPAAL TIGA with 3 tasks among 3 milestones. [p. 11]

## Solution 2: MCRL in UPPAAL STRATEGO

### Workflow

1. **Probabilistic quantification.** The TG becomes an STG. Task finish
   times are uniform between BCET and WCET, the default of UPPAAL SMC.
   [p. 11–12]
2. **Synthesis.** Simulation and Q-learning learn a stochastic strategy.
   [p. 12]
3. **Abstraction.** The stochastic strategy becomes a deterministic
   priority: the highest Q-value wins. Ties are all explored. [p. 13–14]
4. **Verification.** UPPAAL STRATEGO model checks the TG under the
   strategy. [p. 12–13]

### Learning query and Algorithm 1

- The learning query is `strategy opt = minE(x)[<=T]{dv}->{cv}: <> P`.
  Here x is the global clock `gt`, dv holds the Q-state attributes, and cv is
  empty. [p. 12–13]
- P is `(forall(i:int[0,N-1]) ite[i] ≥ M) && gt ≤ TL`. [p. 13]
- Algorithm 1 sends only "good" runs, which satisfy `<> P`, to the learner.
  [p. 13]
- Learning stops when the total runs reach `totalNum` (no strategy) or the
  good runs reach `goodNum` (a strategy). [p. 13]
- The fitness of a strategy is the expected value of x under the strategy.
  The algorithm keeps the best strategy over the iterations. [p. 13]

### Verification queries

| Requirement | Query | Source |
|---|---|---|
| Whole mission | `A<> P under opt` | Query (7) [p. 13] |
| Milestone matching | `A[] (te_n.T_i imply move_n.P_i) under opt` | Query (8) [p. 14] |
| Task sequencing | `A[] (te_n.T_i imply tf[n][i-1]==true) under opt` | Query (9) [p. 14] |
| Timing | `A<> ((forall(i:int[0,N-1]) fin[i] ≥ M) imply x ≤ TL) under opt` | Query (10) [p. 14] |

### Tool support (MALTA)

MALTA has four levels. [p. 14]

1. Mission Management Tool (MMT), a GUI for the map, agents, tasks, and
   milestones.
2. Path Planner, with A*, Theta*, and DALi.
3. Model Generator, and a Strategy & Run Parser.
4. Task Scheduler, which calls TAMAA, UPPAAL TIGA, or UPPAAL STRATEGO.

The earlier MCRL wrote runs to text files and used a "conductor"
automaton. The new MCRL calls back the learning library from inside UPPAAL
STRATEGO. [p. 15]

## Experimental results

### Number of agents (3 milestones, 3 tasks)

| Agents | Method | States | Time |
|---|---|---|---|
| 3 | TIGA | 222,88 (as printed) | 220 ms |
| 3 | MCRL, internal Q-learning | 143,044 | 572 ms |
| 3 | MCRL, external Q-learning | 428,550 | 2.0 s |
| 4 | TIGA | 764,001 | 18.1 s |
| 4 | MCRL, internal Q-learning | 772,619 | 2.2 s |
| 4 | MCRL, external Q-learning | 1,150,349 | 7.3 s |
| 5 | TIGA | 33,312,229 | 53.8 min |
| 5 | MCRL, internal Q-learning | 9,822,914 | 38.2 s |
| 5 | MCRL, external Q-learning | 6,700,782 | 53.0 s |
| 6 | TIGA | Out of memory | Unknown |
| 6 | MCRL, internal Q-learning | 10,322,666 | 7.9 min |
| 6 | MCRL, external Q-learning | 100,901,760 | 14.8 min |

Source: Table 3. [p. 17]

### Sampling effort and completeness

| Agents | Method | Sampled traces | Total runs | Completeness |
|---|---|---|---|---|
| 4 | External Q-learning | 100 | 2,000 | True |
| 4 | Internal Q-learning | 100 | 2,000 | True |
| 5 | External Q-learning | 200 | 10,000 | True |
| 5 | Internal Q-learning | 200 | 20,000 | True |
| 6 | External Q-learning | 200 | 100,000 | True |
| 6 | Internal Q-learning | 200 | 150,000 | True |

Source: Table 4. "Completeness" means that the strategy satisfies the
liveness query (7). [p. 16–17]

### Number of milestones and tasks (2 agents)

| Milestones & tasks | Method | States | Time |
|---|---|---|---|
| 5 | TIGA | 11,746 | 61 ms |
| 5 | MCRL, internal Q-learning | 136,113 | 347 ms |
| 5 | MCRL, external Q-learning | 200,963 | 1.1 s |
| 8 | TIGA | 161,953 | 1 s |
| 8 | MCRL, internal Q-learning | 49,489,463 | 3.4 min |
| 8 | MCRL, external Q-learning | 63,858,459 | 8.2 min |
| 10 | TIGA | 586,124 | 3.9 s |
| 10 | MCRL, internal Q-learning | 324,257,087 | 33.7 min |
| 10 | MCRL, external Q-learning | 324,283,558 | 46.4 min |

Source: Table 5. [p. 17]

### Explanations given by the authors

- The MCRL state counts include repeated random exploration, so they do not
  show the size of the model. [p. 16]
- The UPPAAL TIGA counts show that the number of agents drives the state
  space most. Milestones and tasks also give exponential growth, but much
  less. [p. 16]
- External Q-learning needs fewer simulation rounds, because it uses
  intermediary strategies to guide exploration. [p. 16]
- MCRL learns only from good runs. With many milestones and tasks, random
  runs rarely reach the goal, so learning needs many rounds. [p. 16]

## Limitations stated by the authors

- MCRL gives up completeness for speed. [p. 7, p. 10]
- A strategy from simulation alone has no correctness guarantee, so
  post-verification is always necessary. [p. 11–12]
- The Q-state needs the task statuses of all agents. This requires
  communication between agents, which adds overhead and unreliability.
  [p. 12]
- MCRL performs much worse than UPPAAL TIGA with many milestones and tasks.
  [p. 16]

## Future work stated by the authors

- Improve the learning algorithm for many milestones and tasks, for example
  with penalties for failed runs. [p. 17–18]
- Estimate whether a timed-game strategy exists before synthesis. [p. 18]
- Add continuously changing variables, such as time or energy, to models and
  strategies. [p. 18]

## Related work, as the article positions itself

The article cites POMDP methods with safe-reachability objectives, POMDP
planning at intersections, and controller synthesis for coupled agents.
The authors claim that these lack formal guarantees or scalability proofs.
[p. 17–18] UPPAAL STRATEGO alone learns under a safe controller built
first. MCRL learns on the original model and verifies afterwards. [p. 18]
PuRSUE and the work of Gleirscher et al. use graph search, so the authors
see them as limited in scalability. [p. 18] The authors call their work
orthogonal to MDP learning-based verification by Brázdil, Legay, and
Bouton. [p. 18]

## Reviewer notes on requirement fidelity

These notes are a reading of the article, not claims from it.

- **Timing query (10) can hold trivially.** It has the form
  `A<> (allDone imply x ≤ TL)`. At the initial state, `allDone` is false, so
  the implication is already true. As printed, the query does not check
  the time limit. Query (7) with P from Formula (6) uses a conjunction
  and does check it. Table 4 reports results for Query (7). [p. 13–14,
  p. 16]
- **Variable names.** Query (10) uses `fin[i]`, but Queries (3), (4), and (6)
  use `ite[i]`. Query (7) uses `gt`, and Query (10) uses `x`. [p. 8–9,
  p. 13–14]
- **Task sequencing.** Query (9) checks only the task with index i−1. This
  matches the requirement only if the task indices follow the required
  order.
- **What "verified" means.** A "true" result proves the requirement on the
  timed-game model under the learned strategy, for all durations in the
  BCET-to-WCET intervals. It does not cover collisions or real vehicle
  behavior. [p. 5]
- **Unseen states.** The article does not say how the model checker picks
  an action in a state that has no entry in the Q-table.
- **Two meanings of "complete".** A complete strategy covers all
  environment choices. A complete method finds a strategy whenever one
  exists. MCRL gives the first, after verification, but not the second.
  [p. 6–7, p. 14]
- **Inconsistent thresholds.** Section 8.2 says MCRL performs much worse
  when milestones and tasks are "greater than 5". Section 8.3 says "more
  than 8". [p. 16]
- **Conclusion and data.** The conclusion says UPPAAL TIGA is better "when
  the number of agents is less than two" with many milestones. Table 5 uses
  2 agents. [p. 17–18]
- **Table value.** The 3-agent UPPAAL TIGA count prints as "222,88" in
  Table 2 and Table 3. A digit seems to be missing. [p. 11, p. 17]
- **Case description.** Section 5.2 says trucks take stones from milestone B,
  but a wheel loader digs at milestone C, which is also a primary crusher.
  [p. 7]
- **Missing number.** The text gives a success rate below 10% for 10
  milestones and tasks, but no table shows this rate. [p. 16]
- **AI aspect.** The learner is Q-learning, a reinforcement learning
  method. The article verifies the learned policy, not the learner. Because
  the learner is a replaceable library, the same post-verification can
  check strategies from other learning methods.

## Terms

| Term | Meaning in this article |
|---|---|
| Mission plan | A combined path plan and task schedule |
| Milestone | A target position where an agent does tasks |
| Strategy | A function that suggests the next controllable action or a wait to each agent |
| Timed game (TG) | Timed automata with controllable and uncontrollable actions |
| Stochastic timed game (STG) | A timed game where the environment acts by probability densities |
| 1-player, 2-player, 1½-player game | Agents control all; environment chooses nondeterministically; environment chooses stochastically |
| UPPAAL TIGA | The UPPAAL branch that solves timed games |
| UPPAAL STRATEGO | A UPPAAL branch that combines model checking, statistical model checking, game solving, and learning |
| TAMAA | The authors' UPPAAL-based mission planner |
| MCRL | Model Checking + Reinforcement Learning |
| Q-learning | A model-free reinforcement learning algorithm that learns a value for each state-action pair |
| Q-table | The learned table of state-action values; here it is the strategy |
| Good run | A simulation run that satisfies the goal property `<> P` |
| Post-verification | Exhaustive model checking of the model under a learned strategy |
| `A<> P under opt` | On every path under strategy `opt`, P holds at some time |
| MALTA | The authors' toolset for model generation, path planning, and task scheduling |
| BCET, WCET | Best-case and worst-case execution time of a task |

## Citation

Rong Gu, Peter G. Jensen, Danny B. Poulsen, Cristina Seceleanu, Eduard
Enoiu, and Kristina Lundqvist. "Verifiable strategy synthesis for multiple
autonomous agents: a scalable approach." International Journal on Software
Tools for Technology Transfer 24, 395–414 (2022).
https://doi.org/10.1007/s10009-022-00657-z
