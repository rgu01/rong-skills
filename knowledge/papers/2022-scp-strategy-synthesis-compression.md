---
id: gu2022scp-strategy-synthesis-compression
title: "Correctness-Guaranteed Strategy Synthesis and Compression for Multi-Agent Autonomous Systems"
authors:
  - Rong Gu
  - Peter G. Jensen
  - Cristina Seceleanu
  - Eduard Enoiu
  - Kristina Lundqvist
affiliation: Mälardalen University, Sweden (Gu, Seceleanu, Enoiu, Lundqvist); Aalborg University, Denmark (Jensen)
year: 2022
venue: Science of Computer Programming (SCP), vol. 224
venue_source: author's publications page (the PDF prints no journal name, volume, or year)
doi: null
document_type: journal article
pdf_version: author-typeset manuscript; p. 1 has no journal header, DOI, article number, or preprint note; PDF metadata creation date 2024-07-25
pages_in_pdf: 27
pdf_url: https://drive.google.com/file/d/192LIHkLsOqizZJQ5bSyCqfUQ0-QWJXUE/view?usp=drive_link
listing_url: https://sites.google.com/view/ronggu/publications
author_keywords: [Planning, Multi-Agent Systems, Timed Games, Reinforcement Learning, Strategy Compression]
topics: [strategy synthesis, strategy verification, strategy compression, multi-agent systems, mission planning, task scheduling, post-verification of learned strategies, state-space explosion, soundness proof, construction machinery]
formalisms: [timed automata, timed games, stochastic timed games, TCTL]
tools: [UPPAAL, UPPAAL Stratego, UPPAAL TiGa, UPPAAL SMC]
algorithms: [MoCReL, MCRL, Q-learning, A*]
application: autonomous quarry with wheel loaders, trucks, and crushers
abbreviations: {MAS: multi-agent autonomous systems, TG: timed game, STG: stochastic timed game, UTA: UPPAAL timed automata, RL: reinforcement learning, MCRL: Model Checking + Reinforcement Learning, MoCReL: Model-checked Compressed Reinforcement Learning, BCET: best-case execution time, WCET: worst-case execution time, TCTL: Timed Computation Tree Logic, IQR: interquartile range}
funding: Swedish Knowledge Foundation, DPAC profile grant 20150022 and ACICS synergy grant 20190038
---

# Correctness-Guaranteed Strategy Synthesis and Compression for Multi-Agent Autonomous Systems (Gu et al., SCP 2022)

## At a glance

This paper by Gu, Jensen, Seceleanu, Enoiu, and Lundqvist presents MoCReL. MoCReL
plans the paths and tasks of many autonomous agents. It learns a strategy with
Q-learning, then proves the strategy correct with exhaustive model checking in
UPPAAL Stratego. It then deletes the state-action pairs that the model checker
never needed. The compressed strategy keeps the proven property and can be as
small as 0.05% of the original. The paper proves two theorems and tests MoCReL
on 21 generated autonomous-quarry models. Of these, 17 pass verification and 4
fail.

Page references `[p. N]` point to the 27-page PDF. Printed page numbers equal
PDF page numbers.

## Key facts

Each fact is a claim from the paper unless it is marked otherwise.

- MoCReL stands for Model-checked Compressed Reinforcement Learning. It is a new
  version of the MCRL method of the same authors. [p. 1–2]
- MoCReL synthesizes a strategy by repeated random simulation and reinforcement
  learning. It then verifies the strategy by model checking and compresses it.
  [p. 2, p. 8]
- MoCReL adds three things to MCRL: parameterized model templates, support for
  collaborative and event-driven tasks, and strategy compression. [p. 2]
- MoCReL is built into a new version of UPPAAL Stratego. That version calls an
  external C/C++ library for learning and verification. [p. 1, p. 8, p. 26–27]
- The planning problem is a liveness property `A<> p` over a timed game. The
  strategy must make `p` hold on every run, whatever the environment does.
  [p. 11]
- A strategy in MoCReL is memoryless, non-lazy, and has no clocks. It maps
  discrete states to actions with the highest score in a score table. [p. 12]
- Learning-based synthesis alone gives no correctness guarantee. The paper
  names three causes: unknown convergence, rare events, and the trade-off of
  safety against performance in the reward function. [p. 7]
- Theorem 1 says that the runs of the stochastic strategy are a subset of the
  runs of its non-deterministic abstraction. [p. 13]
- Theorem 2 (soundness) says that if Algorithm 3 returns a strategy σc, then
  the game under σc satisfies `A<> φ`. [p. 17]
- MoCReL labels each state-action pair that the model checker chooses during
  verification. It removes the unlabelled pairs to compress the strategy.
  [p. 15–16]
- The experiments use an autonomous quarry from an industrial case study. The
  case study comes from Volvo Construction Equipment. [p. 7, p. 18]
- The experiments run on an Intel Xeon E5-2678 with 256 GB of RAM and Ubuntu
  20.04 LTS. [p. 18]
- Table 3 lists 21 models. 17 pass verification and 4 fail: game2-B, game6-B,
  game6-C, and game8-C. [p. 19]
- The largest size reduction is from 103 MB to 0.05 MB for game5-E, which is
  99.95%. [p. 19–20]
- For game4-A, the score table shrinks from almost 78,000 rows to fewer than 50
  rows. [p. 20]
- The text says "41/50" cases pass verification. Table 3 shows only 21 models.
  [p. 19–20]
- When reaching the goal is a rare event, the learning efficiency drops
  dramatically. [p. 20, p. 22]
- Future work is to repair failed strategies with counterexamples and to add
  clocks to strategies. [p. 22]

## Questions this paper answers

**What problem does MoCReL solve?** It plans paths and task orders for many
agents so that the agents finish their tasks whatever the environment does. The
plan must be correct and small.

**Why not use only reinforcement learning?** A learned strategy can contain wrong
or useless entries, and nothing proves it correct. MoCReL adds an exhaustive
check after learning.

**Why not use only model checking or timed-game solving?** Exhaustive methods
such as UPPAAL TiGa do not scale. The state space grows exponentially with the
number of agents. [p. 2, p. 6]

**How does MoCReL prove the strategy correct?** It model-checks the game model
under the control of the strategy, with the query `A<> φ under σ`. The check is
exhaustive. [p. 15]

**How does MoCReL compress a strategy?** The model checker labels the pairs it
selects. MoCReL deletes the other pairs. The check can be repeated on the
compressed strategy. [p. 15–16]

**Did the compressed strategies stay correct?** In Table 3, all 17 compressed
strategies pass verification. The 4 failed strategies are not compressed.
[p. 19–20]

**What are the limits?** Strategies have no clocks, and learning fails when the
goal is a rare event. [p. 20–21]

## Scope: what this paper does not do

- It does not give a correct-by-construction learner. Correctness comes from
  verification after learning. [p. 7, p. 8]
- It does not include clocks or other continuous variables in strategies.
  [p. 20]
- It does not verify safety properties in the experiments. The tables report
  only the liveness query `A<> φ`. [p. 19–20]
- It does not use counterexamples to repair or guide learning. The authors list
  this as future work. [p. 8, p. 22]
- It does not model concrete trajectories. Movement is a travel time between two
  positions. [p. 8–9]
- It does not use large language models. The learning method is Q-learning.
  [p. 18]
- It does not run on real agents. All results come from generated models.
  [p. 18]
- It prints no DOI, journal name, volume, or year in the PDF. [p. 1]

## Problem: multi-agent planning

Planning for multi-agent autonomous systems (MAS) means ordering the movement
and task actions of all agents. The environment decides how long each action
takes. The plan must finish all tasks and meet the requirements. [p. 5]

The authors name four challenges. [p. 6]

1. **Uncertainty.** Agents choose actions, but not their duration.
2. **Variety of task constraints.** Some tasks need an order. Some start on
   events.
3. **Complexity.** Scheduling is NP-hard. The state space grows exponentially
   with the number of agents.
4. **Large plans.** The plan grows with the state space. Some entries are never
   used.

Limits of the two older approaches. [p. 6–7]

- Search-based methods give concise and correct plans, but they do not scale.
- A learned score table holds many useless entries. Its highest-scoring actions
  may still violate the requirements.

## Use case: the autonomous quarry

Wheel loaders dig stones and load trucks. Trucks also load at primary crushers.
Trucks carry stones to a secondary crusher. Agents charge at a charging
station when the energy level is low. [p. 7, p. 18]

- Volvo CE says the number of agents varies from 2 to 8. [p. 7]
- The motivating requirement is to quarry 2000 m3 of stones per day. [p. 7]
- A special Referee game judges whether enough stones are moved or the maximum
  simulation time is reached. Then no controllable action is allowed. [p. 18]
- The experiment goal is a target amount of stones. The amount is the same for
  all models. [p. 19]

## Method

### Workflow

The workflow has five steps. [p. 8]

1. Probabilistic quantification turns the timed game (TG) into a stochastic
   timed game (STG).
2. Synthesis simulates the STG and samples runs. A learning module builds a
   strategy. The loop stops at an iteration limit or a sample limit.
3. The stochastic strategy becomes a non-deterministic strategy by abstraction.
4. The model checker asks the strategy for the preferred action. It labels each
   chosen pair as "visited".
5. If verification fails, the iteration limit grows and synthesis runs again. If
   verification passes, the unlabelled pairs are removed.

Raising the iteration limit helps only when the counterexample shows missing
coverage. If a controllable action from the strategy causes the violation, the
user must examine the model or the reward function. [p. 8]

### Model templates

A MAS model is a network of three kinds of timed games. [p. 8–11]

| Template | What it models | Parameters |
|---|---|---|
| Movement | Travel between two positions, in one direction | agent, start, end, `down`, `up`, tasks at both ends |
| Task execution | Switch between idle, waiting, and executing | BCET, WCET, preconditions, event |
| Monitor | A signal that triggers an event | `event`, `warning`, `shutdown` |

- A movement instance covers one direction. A car that moves between two points
  needs two instances. [p. 9–10]
- The guard function `isReady` blocks movement when time is up, the goal is won,
  or the monitor has stopped. [p. 10]
- The task execution guard is a conjunction of five conditions, C1 to C5. [p. 10]
- The task can end only between BCET and WCET. [p. 11]
- The monitor assumes that a signal changes monotonically with time. It watches
  time, not the signal. The authors leave ordinary differential equations as
  future work. [p. 11]
- The movement template of MCRL lists all positions in one template. The new
  template needs only new parameter values when the map changes. [p. 9]

Guard on the edge from `Idle` to `Executing`. [p. 10]

| Part | Condition |
|---|---|
| C1 | `!isBusy(agentID, task)` |
| C2 | `isExecutable(agentID, task)` |
| C3 | `precondition[agentID][task] = FINISHED` |
| C4 | `task status[task] = FINISHED` |
| C5 | `!isMonitorAlert(agentID)` |

Source: Table 1 of the paper. The guard is `C1 && C2 && C3 && C4 && C5`.

### Strategy definition and partial observation

- A strategy is a function from a discrete state to a set of allowed
  controllable actions (Definition 4). [p. 12]
- If the score table has no entry for the state, all enabled actions are
  allowed. If it has entries, only the highest-scoring actions are allowed. Ties
  are non-deterministic or uniform. [p. 12]
- The learner sees only the discrete variables named in the query. It does not
  see clocks. [p. 11–12, p. 14]
- The authors cite a class of "must" specifications that cannot be violated.
  They say these need exhaustive verification. [p. 12]
- A strategy without clocks can still be checked against timing properties.
  The reward function must then take the time limit into account. [p. 12]

### Probabilistic quantification and abstraction

- Probabilistic quantification gives bounded delays and discrete actions a
  uniform distribution. Unbounded delays get an exponential distribution. [p. 13]
- The task templates have BCET and WCET, so no unbounded task delay occurs. [p. 13]
- Synthesis uses exploration: unexplored pairs are as likely as the best pairs.
  Verification uses exploitation: only the best actions are chosen. [p. 13]
- Abstraction replaces stochastic ties with non-deterministic ties. [p. 13]

**Theorem 1.** Given a TG G, the STG P from G, a stochastic strategy σ° for P, and
its abstraction σ, then `Out(P | σ°) ⊆ Out(G | σ)`. The proof is by induction on
the three outcome conditions of Definition 2. [p. 13]

The authors conclude that σ may show behaviour that is highly unlikely or does
not exist under σ°. Hence the exhaustive post-verification is necessary. [p. 13]

### Synthesis query

The synthesis query has this form. [p. 14]

```
strategy policy = minE(x)[<=T]{dv}-->{cv}:<> P
```

`minE(x)` minimizes the reward expression `x`. `dv` and `cv` list the discrete
and continuous features. MoCReL allows only discrete features. The formula
`<> time >= C` makes the simulator pass all runs of length `C` to the learner,
good and bad. [p. 14]

The cat-and-robot example shows two mistakes. [p. 14]

- **Mistake 1.** The user runs `maxE` with a reward that must be minimized. The
  tool still returns a strategy, but it prefers the slowest actions.
- **Mistake 2.** The reward `time - caught × REWARD` has no time limit. The robot
  can catch the cat too late. The fix is `time - caught × (time<=N) × REWARD`.

The authors add that a plan can still be wrong when samples are too few or when
the model violates requirements that the query does not express. [p. 14]

### Verification

Verification uses `A<> ϕ under σ`. It returns true or false. A second query,
`Pr[<=T] ϕ under σ`, returns a probability. The paper extends UPPAAL Stratego
to support the first query on learned strategies. [p. 15]

Algorithm 2 adapts a liveness-checking algorithm from Behrmann et al. A
counterexample is a loop, a maximal run that ends in an unbounded state, or a
deadlock. The `Allow` function asks the strategy at each controllable choice
and labels the chosen pair. [p. 15–16, p. 25–26]

### Compression and soundness

- Labelled pairs reach the goal whatever the environment does, because the
  verification is exhaustive. The paper calls unlabelled pairs "useless". [p. 16]
- Algorithm 3 loops: quantify, learn, abstract, update limits, and verify. It
  then cleans σ into σc. [p. 17]

**Theorem 2 (soundness).** If Algorithm 3 terminates and returns σc, then
`G | σc |= A<> ϕ`. The proof treats two cases: complete and incomplete labelling.
It shows that neither can hide a violation. [p. 17]

### External library interface

The library has these C/C++ functions: `alloc`, `dealloc`, `print`, `clone`,
`sample_handler`, `predict`, and `flush`. `predict` returns the value of an
action and, during verification, marks the chosen pair. The query
`saveStrategy(path)` prints a strategy. [p. 26–27]

## Experiments

### Set-up

- The learning algorithm is Q-learning. [p. 18]
- Models, tool, and full results are in the repository `MoCReL-Experiments` on
  GitHub, under the user `rgu01`. A shortened link holds the full results.
  [p. 18, p. 20]
- Models come from a generator that assigns random parameter values. [p. 18]
- Task types are individual tasks, tasks with preconditions, collaborative tasks,
  and event-triggered tasks. The event is a low-energy refuel. [p. 18]
- Movement granularity is one step between milestones. Travel times come from
  A*. [p. 18]
- The number of runs in Table 3 was "picked empirically". [p. 19]
- Series 1 studies synthesis time and compression on all models. Series 2
  studies the effect of the number of runs on one model and two variants. [p. 18]

Problems that each method solves. [p. 18]

| Method | Agents | Tasks | Events | Task types |
|---|---|---|---|---|
| TAMAA | 2–4 | 3 | Yes | 2 |
| MCRL | 2–6 | 3 | No | 2 |
| MoCReL | 2–6 | 3–6 | Yes | 4 |

Source: Table 2 of the paper.

Model categories. [p. 19]

| Category | Description |
|---|---|
| I | No charging, no choice of crusher, up to 6 agents, 2 crushers, truck capability 20 |
| II | No charging, choice of crusher, 2–5 agents, 3–6 crushers, truck capability 10–30 |
| III | Charging, no choice of crusher, 2–3 agents, 2 crushers, truck capability 50 |

### Results

Abbreviations: CAT category, WL wheel loaders, TK trucks, PC primary crushers,
SC secondary crushers, CH chargers, CAP truck capability, INT task times are
intervals, RUNS sampled runs, STIME synthesis time in seconds, ORI original size
in MB, COM compressed size in MB, VER result of verification on the compressed
strategy. [p. 19]

| CAT | Model | WL | TK | PC | SC | CH | CAP | INT | RUNS | STIME | ORI | COM | VER |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I | game1-A | 2 | 4 | 1 | 1 | 0 | 20 | YES | 2000 | 3,902 | 27 | 0.13 | TRUE |
| I | game3-A | 1 | 2 | 1 | 1 | 0 | 20 | YES | 200 | 16 | 0.08 | 0.02 | TRUE |
| I | game4-A | 2 | 4 | 1 | 1 | 0 | 20 | YES | 5,000 | 772 | 5.6 | 0.03 | TRUE |
| I | game6-A | 2 | 1 | 1 | 1 | 0 | 20 | YES | 200 | 175 | 0.09 | 0.02 | TRUE |
| I | game7-A | 1 | 4 | 1 | 1 | 0 | 20 | YES | 5,000 | 575 | 4.7 | 0.03 | TRUE |
| I | game8-A | 1 | 2 | 1 | 1 | 0 | 20 | YES | 200 | 14 | 0.08 | 0.02 | TRUE |
| I | game9-A | 1 | 4 | 1 | 1 | 0 | 20 | YES | 5,000 | 640 | 4.4 | 0.05 | TRUE |
| II | game0-B | 1 | 2 | 3 | 1 | 0 | 10 | YES | 500 | 92 | 0.9 | 0.2 | TRUE |
| II | game1-B | 1 | 1 | 4 | 1 | 0 | 10 | YES | 500 | 71 | 0.02 | 0.1 | TRUE |
| II | game3-B | 1 | 2 | 1 | 2 | 0 | 10 | YES | 100,000 | 17,297 | 1.4 | 0.6 | TRUE |
| II | game1-E | 1 | 3 | 1 | 2 | 0 | 30 | NO | 500 | 88 | 5.9 | 0.03 | TRUE |
| II | game5-E | 1 | 3 | 4 | 2 | 0 | 30 | NO | 5000 | 1,705 | 103 | 0.05 | TRUE |
| II | game2-B | 1 | 4 | 1 | 2 | 0 | 10 | YES | 100,000 | 800 | 112 | - | FALSE |
| II | game6-B | 1 | 3 | 3 | 2 | 0 | 10 | YES | 100,000 | 893 | 121 | - | FALSE |
| III | game4-C | 1 | 2 | 1 | 1 | 2 | 50 | YES | 2,000 | 270 | 9.4 | 0.03 | TRUE |
| III | game5-C | 1 | 2 | 1 | 1 | 1 | 50 | YES | 5000 | 410 | 2.8 | 0.03 | TRUE |
| III | game3-D | 1 | 2 | 1 | 1 | 1 | 50 | NO | 500 | 68 | 1.4 | 0.03 | TRUE |
| III | game6-D | 1 | 2 | 1 | 1 | 2 | 50 | NO | 500 | 80 | 2.6 | 0.03 | TRUE |
| III | game9-D | 1 | 2 | 1 | 1 | 2 | 50 | NO | 500 | 84 | 7.0 | 0.03 | TRUE |
| III | game6-C | 1 | 1 | 1 | 1 | 2 | 50 | YES | 100,000 | 8,629 | 0.7 | - | FALSE |
| III | game8-C | 1 | 2 | 1 | 1 | 2 | 50 | YES | 100,000 | 12,457 | 49 | - | FALSE |

Source: Table 3 of the paper. [p. 19] The PDF text order of the table columns is
scrambled. The layout view gives the row values above. A "-" means that the
strategy failed verification and was not compressed. [p. 20]

What the text says about the results. [p. 19–20]

- **Category I.** The text says most cases take "several seconds". game1-A takes
  more than 1 hour (3,902 s) and produces the largest strategy of the category,
  27 MB.
- **Category II.** game3-B needs 100,000 runs and more than 4 hours (17,297 s).
  game5-E needs 5000 runs and half an hour (1,705 s), although it is more complex.
  The cause is that game5-E has fixed task times and game3-B has intervals.
  Intervals cause many interleavings.
- **Category III.** Successful strategies take at most several minutes. Some
  models in categories II and III fail even with 100,000 runs.
- **Verification.** The text says "41/50" of the cases pass. In some cases, such
  as game2-B, a counterexample shows the liveness property fails. More runs can
  help. Reaching the goal is a rare event in these models.

### Learning efficiency (series 2)

- The models are game6-B and two variants, game6B-7 and game6B-8. The variants
  lower the truck capability from 10 to 7 and 8. [p. 19–20]
- Each setting runs 100 to 500 sampled runs. The authors repeat each setting 10
  times and take the mean probability of reaching the goal. The probability comes
  from `Pr[<=T] ϕ under σ`. [p. 19]
- For game6-B, every setting gives a probability above 97%, with a standard
  deviation of 0. [p. 20]
- The probabilities of game6B-7 and game6B-8 rise with the number of runs. The
  IQR for game6B-7 is the largest. [p. 20]
- The authors conclude that more runs help little when the goal is rare. [p. 20]

### Compression

- Reductions reach 99.95% of the original size, for game5-E. [p. 20]
- Compression also helps explainability. The game4-A score table drops from almost
  78,000 rows to fewer than 50 rows. [p. 20]

## Limitations stated by the authors

- Continuous variables are not in strategies. The score table would be infinite.
  Zones could give a finite representation. [p. 20]
- Learning efficiency drops when the goal is a rare event. Rare-event simulation
  is a long-standing problem. Importance sampling is one known technique. [p. 21]
- The monitor template assumes monotone signals. [p. 11]

## Future work stated by the authors

- Use counterexamples to repair unsuccessful strategies and raise learning
  efficiency. [p. 8, p. 21–22]
- Add clocks to strategies. [p. 22]
- Remove the monotone-signal assumption with differential equations. [p. 11]

## Related work, as the paper positions itself

- **Formal methods for MAS.** Alur et al. use LTL and compositional synthesis.
  Křetínský combines LTL and steady-state policy synthesis. Gleirscher et al.
  select a safe controller from several models. The authors say their problem
  needs one goal for all agents and TCTL properties. [p. 21]
- **UPPAAL-based synthesis.** Andersen et al., Basile et al., and Bersani et al.
  (PuRSUE) use UPPAAL tools. The paper says the first uses reachability only, the
  second uses statistical checking, and the third searches exhaustively and does
  not scale. [p. 21]
- **Formal methods with RL.** Behjati et al., Bouton et al., and Jothimurugan et
  al. add guarantees during learning. MoCReL gives an exhaustive check after
  learning. [p. 21]
- **Strategy compression.** Julian et al. use origami and neural networks. Ashok
  et al. (dtControl) use decision trees. Piterman et al. remove redundant states.
  MoCReL removes unused data and relies on model checking for safety. [p. 21]

## Relation to other papers

- `2020-fmics-mission-plan-synthesis.md` describes the earlier MCRL method. This
  paper lists three limits of MCRL: hard manual models, only simple periodic
  tasks, and plans larger than needed. [p. 2]
- `2022-sttt-verifiable-strategy-synthesis.md` is the STTT paper, which the paper
  cites as [13]. MoCReL reuses its learning algorithm (Algorithm 4). [p. 17, p. 25]
- `2022-phd-thesis-scalable-synthesis-verification.md` holds a submitted version
  of this paper as Paper E. The thesis summary lists problems in that version. See
  "Reviewer notes".

## Reviewer notes on requirement fidelity and verification

These notes are a reading of the paper, not claims from it.

**Status of problems found in the thesis version (Paper E).**

- *Compressed size larger than original (Table 12.1, game1-B).* Still present.
  Table 3 gives ORI 0.02 MB and COM 0.1 MB for game1-B. [p. 19] The text says
  compression saves memory and does not mention this row. The paper gives no
  reason for the larger size.
- *"41 of 50 cases" against 21 models.* Still present. The text says "41/50"
  pass. [p. 20] Table 3 lists 21 models, of which 17 pass. [p. 19] The 21 models
  are not a subset the text names. The other 29 models are not in the PDF.
- *Example after Theorem 1.* Fixed. The thesis errata removes an example with a
  state of 10 controllable actions, of which 4 have the highest score. [thesis p.
  309, errata p. 369] This version has no example after Theorem 1. The proof is
  followed by one paragraph. [p. 13] A later example about the reward function
  appears in Section 4.4.3. It is a different example. [p. 14] The wording changed
  from "do not exist" to "highly unlikely or even do not exist". [p. 13]

**What the verification proves.**

- The proof covers the model G under σc for the liveness property `A<> φ`. It
  does not cover the real quarry. The model has coarse movement, interval task
  times, and monotone monitors. [p. 8–11]
- The check is exhaustive for the abstraction. Theorem 1 says the abstraction
  includes every run of the learned stochastic strategy. A failure can therefore
  be a run that the stochastic strategy almost never takes. The game6-B result
  fits this reading: probability above 97%, but the exhaustive check fails.
  [p. 13, p. 20]
- Only the liveness query is verified in the experiments. Safety queries, such as
  collision freedom (Query 13), appear only in the cat example. [p. 15, p. 19–20]
- Algorithm 3 verifies σ and then cleans σ into σc. The proof of Theorem 2 argues
  about the verification of σ. It does not argue separately that removing the
  unlabelled pairs keeps the property. Table 3 gives an empirical re-check on
  the 17 compressed strategies. [p. 17, p. 19]
- The intro calls the plans "correct-by-construction". [p. 2] Section 4.1 and
  Section 4.4.1 say that learned strategies have no guarantee and that the
  verification gives it. [p. 8, p. 12] The two statements use the word in
  different senses.

**Requirement fidelity.**

- The requirement in the motivating text is "2000 m3 of stones per day". The
  experiments verify that "a target amount of stones" is moved. The Referee game
  encodes the goal. The paper gives no check that the Referee matches the
  natural-language requirement. [p. 7, p. 18–19]
- The goal in the models is the same for all models. The paper does not give its
  value. [p. 19]
- Other requirements, such as "never let two agents execute a task
  simultaneously", appear as examples. [p. 5] The paper does not list which of them
  the generated models enforce.
- The paper shows no independent specification for the queries. The synthesis
  query and the verification query come from the same team that builds the
  models.

**Other inconsistencies.**

- Volvo CE reports 2 to 8 agents. The experiments reach 6. Table 2 gives 2–6
  agents for MoCReL. [p. 7, p. 18]
- The text says most category I cases take "several seconds". Table 3 gives 14
  to 3,902 s, with five of seven cases above 100 s. [p. 19]
- The text says series 2 uses 100 to 500 runs on game6-B. Table 3 gives 100,000
  runs and VER FALSE for game6-B. [p. 19–20]
- Models are generated at random, and the number of runs is "picked empirically".
  The paper gives no stopping rule for the run count. [p. 18–19]

**AI aspects.** The AI part is Q-learning. The paper has no large language model.
The pattern "learn, then verify exhaustively, then compress" fits other
untrusted generators, but the paper does not claim this.

## Terms

| Term | Meaning in this paper |
|---|---|
| MAS | Multi-agent autonomous system: several agents with a common goal |
| Timed game (TG) | A timed automaton whose actions split into controllable and uncontrollable |
| Stochastic timed game (STG) | A timed game where choices follow probability distributions |
| Strategy | A function that picks allowed actions in each state |
| Memoryless strategy | A strategy that looks only at the current state |
| Non-lazy strategy | A strategy that picks an action at once or waits for the environment |
| Score table | A table of state-action pairs and their learned scores |
| Probabilistic quantification | Giving non-deterministic choices a probability distribution |
| Abstraction | Turning a stochastic strategy into a non-deterministic one |
| Exploration / exploitation | Trying unexplored actions / choosing the best-scored actions |
| `A<> p` | Liveness: on every run, `p` is true in some state |
| `A[] p` | Invariance: `p` is true in every state of every run |
| `A<> ϕ under σ` | Liveness check of the game controlled by strategy σ |
| Labelling | Marking the state-action pairs that the model checker selects |
| Compression | Removing the unlabelled pairs from a strategy |
| BCET / WCET | Best-case and worst-case execution time of a task |
| Rare event | An event that random simulation seldom reaches |
| MCRL | Earlier method: Model Checking + Reinforcement Learning |
| IQR | Interquartile range: the 75th percentile minus the 25th percentile |

## Citation

Rong Gu, Peter G. Jensen, Cristina Seceleanu, Eduard Enoiu, and Kristina
Lundqvist. "Correctness-Guaranteed Strategy Synthesis and Compression for
Multi-Agent Autonomous Systems." Science of Computer Programming, vol. 224,
2022.
