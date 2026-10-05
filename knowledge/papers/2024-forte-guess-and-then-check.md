---
id: gu2024forte-guess-and-then-check
title: "Guess and then Check: Controller Synthesis for Safe and Secure Cyber-Physical Systems"
running_title_in_pdf: "Safety and Security Guaranteed Construction of Cyber-Physical Systems"
authors:
  - Rong Gu
  - Zahra Moezkarimi
  - Marjan Sirjani
affiliation: Mälardalen University, Västerås, Sweden
year: 2024
venue: FORTE'24
venue_full: 44th International Conference on Formal Techniques for Distributed Objects, Components, and Systems
publisher: Springer
month: July
venue_source: university repository page (es.mdu.se/publications/6877); the PDF does not name the venue
doi: null
document_type: conference paper (short paper on ongoing work)
pages_in_pdf: 8
pdf_url: https://www.es.mdu.se/pdf_publications/6877.pdf
repository_url: https://www.es.mdu.se/publications/6877-Guess_and_then_Check__Safety_and_Security_Guaranteed_Construction_of_Cyber_Physical_Systems
listing_url: https://sites.google.com/view/ronggu/publications
code_url: https://github.com/rgu01/RebecaLearning
author_keywords: []
topics: [controller synthesis, cyber-physical systems, safety, security, state-space explosion, reinforcement learning, model checking, two-player games, hyperproperties, opacity, multi-robot systems]
formalisms: [Markov decision process, two-player game, temporal logic (reachability and invariance), hyperproperties]
tools: [Rebeca, Timed Rebeca, Probabilistic Timed Rebeca]
algorithms: [Guess and Check, depth-first state-space exploration, Q-learning, Monte-Carlo simulation]
application: two robots that deliver goods on a 7 x 4 factory grid with obstacles, wet floors, and an intruder
abbreviations: {CPS: cyber-physical system, MDP: Markov decision process, ECS: edge-computing server, CCS: cloud-computing server, NN: neural network, C4SA: check for safety (Algorithm 2), C4CE: check for security (Algorithm 3)}
funding: null
---

# Guess and then Check: Controller Synthesis for Safe and Secure Cyber-Physical Systems (Gu, Moezkarimi, Sirjani, FORTE 2024)

## At a glance

This 2024 short paper by Gu, Moezkarimi, and Sirjani reports ongoing work on
controller synthesis for cyber-physical systems (CPS). The method, "Guess
and Check", has three phases. Phase 1 guesses a controller. It explores all
controllable actions and only some uncontrollable actions, guided by
learning. Phase 2 checks the guess for safety and explores all environment
actions. Phase 3 checks the result for security. The authors model the CPS
and its environment as a Markov decision process (MDP) for a two-player
game. A preliminary experiment on a two-robot grid example shows that
phases 1 and 2 explore fewer states than the full state space.

Page references `[p. N]` point to the 8-page PDF.

## Key facts

Each fact is a claim from the paper unless it is marked otherwise.

- The Guess-and-Check paper describes itself as a report of "ongoing work"
  on safe and secure controller synthesis for CPS. [p. 1]
- The Guess-and-Check method alternates exhaustive and selective
  exploration of the state space in three phases. [p. 1–2]
- The Guess-and-Check paper models the CPS and its environment as an MDP.
  CPS actions are controllable and environment actions are uncontrollable.
  [p. 2, p. 4]
- The Guess-and-Check paper defines three requirements on the controlled
  traces: functional correctness (reach a goal state), safety (avoid unsafe
  states), and security (hidden information cannot be deduced from the
  observable part). [p. 3]
- The Guess-and-Check paper formulates security as a hyperproperty,
  because it involves more than one trace. [p. 3]
- Phase 1 of Guess and Check explores all controllable actions and
  explores uncontrollable actions selectively. The result is an
  "optimistic controller". [p. 5]
- In phase 1, a learning algorithm, for example Q-learning, computes a
  policy that lets the environment win the game faster. [p. 5]
- Phase 2 of Guess and Check explores only the controllable actions in the
  optimistic controller and explores all uncontrollable actions. [p. 6]
- When phase 2 reaches a system state that is not in the controller,
  it calls the guess phase again from that state. [p. 6]
- The authors state that after phase 2 they have "a safe and functionally
  correct controller". [p. 6]
- Phase 3 of Guess and Check prunes each trace that satisfies the secret
  property when no similar enough trace satisfies the public property.
  [p. 6]
- The Guess-and-Check platform plans a GUI for Game Timed Rebeca and Game
  Probabilistic Timed Rebeca, an explorer, and an external learning
  library. [p. 6]
- The preliminary Guess-and-Check experiment uses random simulation
  instead of learning in phase 1 and repeats each run 10 times. [p. 7]
- In the Guess-and-Check experiment, phases 1 and 2 explore "much less"
  states than the total number of states. [p. 7]
- The code of the Guess-and-Check experiment is published at
  https://github.com/rgu01/RebecaLearning. [p. 7]
- The authors state that they "will finish implementing" the platform in
  the open-source Rebeca toolset. [p. 7]

## Questions this paper answers

**What problem does the paper address?** Synthesis of a controller for a
nondeterministic, Markovian CPS that is functionally correct, safe, and
secure. Exhaustive search gives a guarantee but does not scale. Learning
scales but gives no guarantee. [p. 1–2]

**How does Guess and Check combine search and learning?** Learning (or
random search) selects environment actions in phase 1. Exhaustive
exploration of environment actions in phases 2 and 3 then gives the
guarantee. [p. 2, p. 5–6]

**What does "security" mean here?** Confidentiality. An intruder sees the
observable part of a trace, such as robot trajectories. The intruder must
not deduce hidden information, such as the task order. [p. 3–4]

**What tool implements the method?** A platform based on Rebeca. The paper
describes the architecture, and the future-work section says the
implementation is not finished. [p. 6–7]

**How large is the evaluation?** Four model sizes (step = 3 to 6), with
total state spaces of about 2,000 to 8,000 states, read from Figure 4.
The paper gives no table of numbers. [p. 7]

**Does the paper prove the algorithms correct?** No. It gives no theorem
and no proof of soundness or completeness.

## Scope: what this paper does not do

- It gives no proof of soundness, completeness, or termination for the
  three algorithms.
- It does not evaluate phase 3. A footnote says that the phase 3 state
  count depends on the controller size, not on the approach. [p. 7]
- It does not use learning in the experiment. Phase 1 uses random
  simulation. [p. 7]
- It reports no run times, no memory use, and no hardware.
- It does not compare with another synthesis tool or with pure
  reinforcement learning on the same models.
- It does not define the trace distance function D. It refers the reader
  to Liu et al. [14]. [p. 6]
- It does not use the transition probabilities of the MDP in the checks.
  The environment is treated as an adversary.
- It does not model time, although the example asks for task completion
  "within a time frame". [p. 4]
- It names no DOI and no venue inside the PDF.

## Problem definition

The paper adapts the definitions of Liu et al. [14]. [p. 2–3]

| Item | Definition in the paper |
|---|---|
| CPS | A quadruple C = (X, X0, A, T): states X, initial states X0 ⊆ X, actions A, transition relation T ⊆ X × A × X. Each set can be infinite. |
| Trace | A state sequence π induced by an action sequence. πf is a finite part of a trace. O(π) is the observable part and H(π) the hidden part. |
| Controller | A partial function σ : πf → A. For a Markovian CPS, it can be memoryless: σ : last(πf) → A. |
| Functional correctness | ∀π ∈ Πσ, ∃x ∈ π such that x ∈ G (goal states) |
| Safety | ∀π ∈ Πσ, ∀x ∈ π, x ∩ U = ∅ (U = unsafe states) |
| Security | ∀π ∈ Πσ, ∃π′ ∈ Πσ such that H(π) ≠ H(π′) and O(π) = O(π′) |

The paper expresses functional correctness as a reachability property and
safety as an invariance property of temporal logic. [p. 3]

## Illustrative example

The example comes from an industrial use case of goods delivery by robots
in a factory. [p. 3–4]

- **Grid.** The environment is a 7 × 4 grid. Grey cells are obstacles,
  which the robots must not enter. Blue cells are wet floors. [p. 3–4]
- **Tasks.** Robot R1 must do tasks T1 and T2, and robot R2 must do tasks
  J1 and J2, at the correct cells. Then both robots meet at an M cell.
  The robots can go through task cells without doing the task. [p. 3–4]
- **Uncertainty.** A robot can slip on a wet floor and end one cell below
  its target. [p. 4]
- **Architecture.** An edge-computing server (ECS) plans the trajectories.
  A cloud-computing server (CCS) schedules the high-level tasks. [p. 4]
- **Intruder.** The intruder attacks the ECS to change the task order. The
  intruder cannot access the CCS but can deduce the task order from the
  trajectories. [p. 4]
- **MDP.** Each state holds both robot positions, for example
  (0,0),(6,3). The robot chooses a controllable move, and then the
  environment decides the end position. [p. 4]

The paper gives two traces of R1 to show security. [p. 4]

| Trace | Cells | Secure? | Reason given |
|---|---|---|---|
| trace1 | (0,0)→(0,1)→(1,1)→(2,1)→(2,2)→(2,3)→(3,3) | No | R1 can do T1 only at (2,1), and that cell comes before the T2 cells |
| trace2 | (0,0)→(0,1)→(1,1)→(2,1)→(2,2)→(2,1)→(2,2)→(2,3)→(3,3) | Yes | R1 visits the T1 and T2 cells alternately more than once |

## Method: the three phases

Figure 1 shows a loop between "Guess" and "Check for Safety", followed by
"Check for Security". [p. 2]

### Phase 1: guess for a controller (Algorithm 1, GUESS)

- The search is recursive and depth-first. The authors state that another
  exploration order does not affect correctness. [p. 5]
- The controller σ is a global set of state-action pairs that all three
  algorithms share. [p. 5]
- When the search reaches a goal state, LEARN&ADD feeds the trace to the
  learner and adds it to σ. [p. 5]
- When the search reaches an unsafe state, a loop, or a deadlock,
  LEARN&PRUNE feeds the trace to the learner and prunes it from σ. [p. 5]
- At an environment state, the search follows only the action that BEST
  returns. The learned policy makes the environment win faster, that is,
  reach an unsafe state. [p. 5]
- At a system state, the search follows every action. [p. 5]
- The result is an optimistic controller that "may be correct", because
  phase 1 explores the environment only partially. [p. 5]

### Phase 2: check for safety (Algorithm 2, C4SA)

- At an environment state, the check explores every environment action and
  combines the results with ∧. All environment actions must pass. [p. 6]
- At a system state, the check explores only the actions in σ and combines
  the results with ∨. One passing action is enough. [p. 6]
- A failing trace is pruned from σ with LEARN&PRUNE. [p. 5–6]
- At a system state that σ does not contain, the check calls GUESS from
  that state. [p. 6]

### Phase 3: check for security (Algorithm 3, C4CE)

- EXPLORE collects the trace set Πσ of the controlled system. [p. 6]
- Ps is the confidential property and Pc is the public property. [p. 6]
- For each trace π1 that satisfies Ps, a trace π2 in Πσ must satisfy Pc
  with D(π1, π2) ≤ τ. Otherwise LEARN&PRUNE removes π1 from σ. [p. 6]
- For discrete state spaces, the condition O(π1) = O(π2) can replace the
  distance D. [p. 6]

## Platform

Figure 3 shows the planned architecture. [p. 6]

| Part | Content |
|---|---|
| GUI | Modelling in Game Timed Rebeca and Game Probabilistic Timed Rebeca, both based on Rebeca and extended with controllable and uncontrollable actions |
| Explorer | A simulator for Monte-Carlo simulation, a set of model checkers, and a synthesizer that calls them |
| Learner | An external library, for example Q-learning and deep learning |

The paper says "We aim to realize the algorithms in a platform". [p. 6]

## Preliminary evaluation

The authors build several models from the two-robot example. Each model
sets a maximum number of robot steps and adjusts the goals. They generate
the full state space, synthesize a controller, and count the states that
phases 1 and 2 explore. Phase 1 uses random simulation, and each model runs
10 times. [p. 7]

The paper gives the results only as a box plot (Figure 4). The values below
are approximate readings from that plot, not numbers printed in the paper.
[p. 7]

| Max steps | Total states (approx.) | Phase 1 median (approx.) | Phase 2 median (approx.) |
|---|---|---|---|
| 3 | 2,050 | 650 | 200 |
| 4 | 3,850 | 1,300 | 700 |
| 5 | 6,000 | 2,200 | 1,700 |
| 6 | 8,100 | 2,200 | 1,850 |

At step 6, the plot also shows outliers near 4,300 to 4,600 states. At
step 5, the phase 2 box spans about 900 to 2,650 states. [p. 7]

The authors conclude that the approach "has the potential" to solve
problems that are too complex for exhaustive search. They also say that it
keeps a guarantee that pure reinforcement learning cannot give. [p. 7]

## Future work stated by the authors

- Finish the platform in the open-source Rebeca toolset. Integrate
  Rebeca, Timed Rebeca, and Probabilistic Timed Rebeca. [p. 7]
- Apply the algorithms to real-world CPS applications of Rebeca. [p. 7]
- Try other learning models, such as neural networks, through the
  external learning library. [p. 7]
- Study how model checking and machine learning can help each other in
  controller synthesis. [p. 7]
- Consider human factors, for example best-effort strategies when the
  constraints are too strict to reach all goals. [p. 7]
- Make the approach adaptive for multiple objectives that follow human
  preferences. [p. 7]

## Related work, as the paper positions itself

The paper compares itself only with recent work, because of the page
limit. Křetínský et al. [11] guess winning strategies in parity games from
LTL synthesis by learning. Parker et al. [15, 13] use binary decision
diagrams and synthesis based on probabilistic model checking. The paper
claims that its main difference is the integration of exhaustive search
and learning. [p. 7]

The introduction cites crashes with Tesla's driver-assistance system, a
remote Jeep hack, and a fatal Uber self-driving crash as motivation. [p. 2]

## Reviewer notes

These notes are a reading of the paper, not claims from it.

- **Two titles.** The running head on pages 3, 5, and 7 is "Safety and
  Security Guaranteed Construction of Cyber-Physical Systems". The
  university repository URL uses the same alternative title. The body text
  calls the method "Guess and Check", not "Guess and then Check".
- **Repository abstract against the PDF.** The repository page claims that
  the method is "sound and complete". The PDF has no such claim, no
  theorem, and no proof. The PDF claims only that the exploration order
  does not affect correctness, and that phase 2 gives a safe and
  functionally correct controller. [p. 5–6]
- **Implementation claim.** The PDF abstract says "We implement the
  synthesis algorithms in the Rebeca … platform". Section 3 says "We aim to
  realize", and Section 4 says "We will finish implementing". The PDF
  therefore supports a partial implementation only. [p. 1, p. 6–7]
- **Experiment claim.** The PDF supports the claim of an experiment. It
  is preliminary: four small models, state counts only, random simulation
  instead of learning, and no evaluation of phase 3. [p. 7]
- **What phase 2 proves.** The guarantee rests on exhaustive exploration of
  environment actions from the states that σ reaches. The paper does not
  show that pruning in one branch leaves earlier passed branches valid.
- **Phase 3 and safety.** Phase 3 prunes traces from σ, and Figure 1 shows
  no path back to phase 2. The paper does not say whether the pruned
  controller still reaches the goal from every state. [p. 2, p. 6]
- **Requirement fidelity.** The example asks the robots to finish all tasks
  "within a time frame". The formal functional-correctness property has
  no time bound. It only asks that each trace reaches G. [p. 3–4]
- **Security notion.** The intruder in the example wants to "change the
  task order", which is an integrity attack. The formal property is about
  confidentiality: the intruder must not deduce the order. [p. 3–4]
- **Safety formula.** The safety property writes x ∩ U = ∅ for a state x.
  For a single state, the intended meaning is x ∉ U. [p. 3]
- **Trace set.** Algorithm 3 line 3 loops over Π, but line 2 defines Πσ.
  [p. 6]
- **Loop pruning.** Algorithms 1 and 2 prune a trace when it revisits a
  state. The trace2 example of a secure trace, however, revisits (2,1) and
  (2,2). If a state holds only the position, the guess phase prunes the
  secure trace. The paper does not say what a state holds beyond the
  positions. [p. 4–5]
- **Possible off-by-one.** Algorithm 1 line 13 loops while NEXT is not
  LAST. Read literally, this skips the last system action. [p. 5]
- **MDP and probabilities.** The paper calls the model an MDP, but the
  checks treat the environment as nondeterministic. No step uses the
  probabilities. [p. 3–6]
- **Evaluation scale.** The largest model has about 8,100 states. This
  size is easy for exhaustive search, so the experiment does not yet show
  a case that exhaustive search cannot solve. The paper does not say
  whether a state explored in both phases is counted twice.
- **AI aspect.** Learning is used only to choose environment actions in
  the guess phase. The learner does not decide correctness. In the
  reported experiment, random simulation replaces the learner. [p. 5, p. 7]
- **Agreement with 2024-live-ml-and-model-checking.md.** The LiVe'24 paper
  gives the same three phases and the same split: safe after phase II and
  secure after phase III. It differs in these details:
  - It says the MDP is modelled in Timed Rebeca. This paper names Game
    Timed Rebeca and Game Probabilistic Timed Rebeca as planned GUI
    languages, and it does not name the language of the experiment models.
  - It describes phase 1 selection by "accumulated reward". This paper
    describes a learned policy that makes the environment win faster.
  - It describes phase 3 as pruning of transitions. This paper prunes
    traces.
  - It cites the method as a technical report from January 2024. This
    paper does not mention a technical report.

## Terms

| Term | Meaning in this paper |
|---|---|
| CPS | Cyber-physical system: cyber parts and physical parts that interact closely |
| Controller synthesis | Automatic construction of a controller that satisfies given requirements |
| Controllable action | An action that the CPS chooses (blue arrows in Figure 2(b)) |
| Uncontrollable action | An action that the environment takes (dotted violet arrows in Figure 2(b)) |
| MDP | Markov decision process: a model where states have choices and the result of a choice can be uncertain |
| Two-player game | A model where the CPS and the environment take turns; the CPS wins when it meets the requirements whatever the environment does |
| Optimistic controller | The phase 1 result: it may be correct, because phase 1 does not explore all environment actions |
| Hyperproperty | A property of a set of traces, not of one trace |
| Observable part O(π) | The part of a trace that an intruder can see, for example the robot trajectory |
| Hidden part H(π) | The confidential part of a trace, for example the task order |
| State-space explosion | Fast growth of the number of states with model size, so that exhaustive search fails |
| Q-learning | A reinforcement-learning method that learns action values from rewards |
| Monte-Carlo simulation | Random exploration of runs through the state space |
| Rebeca | Reactive Objects Language, an actor-based modelling language with verification tools |
| LEARN&ADD, LEARN&PRUNE | Helper steps that give a trace to the learner and then add it to, or remove it from, the controller σ |

## Citation

Rong Gu, Zahra Moezkarimi, and Marjan Sirjani. "Guess and then Check:
Controller Synthesis for Safe and Secure Cyber-Physical Systems." 44th
International Conference on Formal Techniques for Distributed Objects,
Components, and Systems (FORTE'24), Springer, 2024.
