---
id: gu2023amost-policy-synthesis-test-generation
title: "Model-Based Policy Synthesis and Test-Case Generation for Autonomous Systems"
authors:
  - Rong Gu
  - Eduard Enoiu
affiliation: Mälardalen University, Sweden
year: 2023
venue: A-MOST'23
venue_source: author's publications page (the PDF does not name the venue)
doi: null
document_type: workshop paper
pages_in_pdf: 13
pdf_url: https://drive.google.com/file/d/1zw0c1ym-zGmpplDc-Ot-YgN7YgqcKABi/view?usp=share_link
listing_url: https://sites.google.com/view/ronggu/publications
website: https://sites.google.com/view/mbpt4as
author_keywords: [autonomous systems, model checking, testing, test-case generation]
topics: [policy synthesis, model-based testing, test-case generation, reinforcement learning, timed games, autonomous vehicles, multi-agent systems, trajectory tracking, mission planning]
formalisms: [timed games, priced timed games, timed automata, CTL, ordinary differential equations]
tools: [UPPAAL Stratego]
algorithms: [Q-learning, graph-search-based synthesis, learning-based synthesis, strategy compression, safe envelope, Lyapunov function]
application: autonomous quarry with a truck and a wheel loader
abbreviations: {HL: high-level layer, LL: low-level layer, TA: timed automaton, TG: timed game, PTG: priced timed game, NPTG: network of priced timed games, MTG: movement timed game, RTG: reference controller timed game, TPTG: priced timed game for tracking controllers, MBT: model-based testing, CTL: computation tree logic, ODE: ordinary differential equation, BCET: best-case execution time, WCET: worst-case execution time, MAS: multi-agent systems}
funding: Synergy ACICS (Assured Cloud Platforms for Industrial Cyber-Physical Systems), Swedish Knowledge Foundation, grant 20190038
---

# Model-Based Policy Synthesis and Test-Case Generation for Autonomous Systems (Gu and Enoiu, A-MOST 2023)

## At a glance

This 2023 paper by Gu and Enoiu proposes a two-layer framework for
autonomous systems, built in UPPAAL Stratego. The high-level layer
synthesises a mission policy from timed games, by graph search or by
learning, with a model-checking guarantee. The low-level layer generates
test cases for the tracking controller that executes the policy. A test case
is a reference trajectory. Q-learning finds the trajectories, and model
checking shows that they faithfully realise the policy. In an autonomous
quarry case study, shorter sampling periods find more faults (1, 2, and 11)
but take longer (1.5 s to 26.4 s per ten test cases).

Page references `[p. N]` point to the 13-page PDF. Pages 11 to 13 are an
appendix.

## Key facts

Each fact is a claim from the paper unless it is marked otherwise.

- The policy-synthesis paper splits the problem into a high-level layer (HL)
  for policy synthesis and a low-level layer (LL) for policy execution.
  [p. 1, p. 5]
- The two-layer framework continues the authors' earlier two-layer
  framework for verifying autonomous vehicles (NFM 2019, reference [5]).
  [p. 1, p. 9]
- The framework uses timed games for policy synthesis and priced timed games
  with ordinary differential equations for the tracking controller. [p. 2,
  p. 5]
- The HL offers a graph-search-based method and a learning-based method to
  synthesise policies. The paper only summarises both methods and refers to
  earlier work for them. [p. 5, p. 11]
- A policy can be a score table or an artificial neural network. The paper
  suggests a C-code array for a table and an external library for a neural
  network. [p. 5–6]
- The paper defines a mission map as a 5-tuple of state space, unsafe area,
  initial area, goal areas, and temporal-logic requirements. [p. 3]
- The paper requires four features of a reference trajectory: physical
  feasibility, the policy premises, faithful realisation of the policy, and
  the reach-avoid requirement. [p. 4]
- The test-case generator learns a decision strategy for the reference
  controller with the UPPAAL Stratego query
  `strategy δ = maxE(x)[<=T]{dv}-->{cv}:<> CO`. [p. 6–7]
- Three model-checking queries under the learned strategy check
  synchronisation, realisation, and faithfulness of the test cases. [p. 7–8]
- An external library removes the state-action pairs that the model checker
  does not visit. This step reuses the authors' strategy-compression method.
  [p. 7–8]
- The tolerance of a reference trajectory is the width of a safe envelope
  from the literature. The bound holds when the tracking-error dynamics have
  a Lyapunov function. [p. 8]
- The quarry case study is provided by Volvo Construction Equipment, Sweden.
  It has one wheel loader, one truck, two primary crushers, and one
  secondary crusher. [p. 8]
- In the quarry case study, the test cases are stored as a JSON file. The
  system under test is a Java program with the truck kinematics and a
  tracking controller. [p. 8]
- With a sampling period of 10, 5, and 1, the generator needs 1.5 s, 4.2 s,
  and 26.4 s per ten test cases and detects 1, 2, and 11 faults. [p. 8]
- The verification time of Queries (2) to (4) is under one second in all
  cases, so Table I does not include it. [p. 8]
- The authors observe that the tracking controller loses control when the
  turning angle changes sharply. [p. 9]

## Questions this paper answers

**What does the framework produce?** Two products. The HL produces a
winning policy for the mission. The LL produces test cases for the tracking
controller. Each test case is a set of sampled points on a reference
trajectory. [p. 5]

**Why test the controller instead of verifying it?** The kinematics are
nonlinear and the environment is uncertain. The paper says that formal
verification of the real trajectories is "extremely difficult" (p. 4) and,
in the appendix, "undecidable" (p. 11).

**Where does machine learning come in?** At two places. The learning-based
policy synthesis uses reinforcement learning such as Q-learning. The
test-case generator uses Q-learning in UPPAAL Stratego to decide the speed
and the turning of the reference controller. [p. 6, p. 8, p. 11]

**What does model checking guarantee about the test cases?** If Queries (2)
to (4) hold, the learned strategy keeps the reference controller in step
with the policy. It also includes all and only the paths of the policy that
accomplish the mission. [p. 7–8]

**What counts as a fault?** A point where the tracking error goes past the
threshold and the tracking controller cannot bring the system back within a
time frame. [p. 5, p. 9]

**How large was the evaluation?** One quarry scenario, one policy, and three
sampling periods. [p. 8]

## Scope: what this paper does not do

- It does not evaluate the policy-synthesis methods. Earlier papers [13]
  and [14] evaluate them. [p. 8]
- It does not present the tracking-controller model (TPTG). The authors
  leave it as future work. [p. 6]
- It does not verify the tracking controller formally. It tests the
  controller.
- It does not use continuous variables in learning, because the exhaustive
  model checker runs afterwards. [p. 7]
- It assumes that all obstacles are fixed and permanent. [p. 3]
- It does not test a real vehicle. The system under test is a Java
  simulation of the truck. [p. 8]
- It does not compare the generator with other test-generation methods.
- It names no DOI and no venue inside the PDF.

## System and problem

The paper describes an autonomous system that works in a confined
environment. [p. 3–4]

| Component | Input | Output |
|---|---|---|
| Mission planner | Mission map | Policy |
| Reference controller | Policy and the environment state `state_e` | Reference trajectories |
| Tracking controller | Reference trajectory and the real-time system state | Commands such as acceleration and turning |
| Physical system | Commands | Real trajectory |

- A **policy** maps each state to controllable actions so that the model
  eventually reaches a winning state. A policy alone is not executable; a
  controller executes it. [p. 2, p. 4]
- The **premises** of a policy are its assumptions, for example the time
  intervals of actions. [p. 4]
- A **trajectory** over a duration D is a function ψ : [0, D] → X. [p. 4]
- The paper uses two kinds of state: `state_s` of the autonomous system,
  such as its speed, and `state_e` of the environment, such as the time
  when an action finishes. [p. 4]
- One policy usually gives several reference trajectories, because the
  environment reacts in different ways. [p. 5]

### Mission map (Definition III.1)

A mission map is `M = <X, O_u, I, G, Req>`. [p. 3]

| Element | Meaning |
|---|---|
| X ∈ R^d | State space of the map |
| O_u ⊆ X | Unsafe area |
| I ⊆ X | Initial area |
| G | Set of goal areas, each a subset of X |
| Req | Set of temporal-logic formulas |

The paper notes that the state space can have more than two dimensions. For
a robotic arm, time and speed are extra dimensions. [p. 3]

### Reach-avoid requirement (Proposition III.1)

A reference trajectory ψ and a real trajectory ρ with error
e = ρ(t) − ψ(t) are valid if all four conditions hold. [p. 4]

1. ψ(0) + e ∈ I.
2. For all t ∈ [0, D], (ψ(t) + e) ∩ O_u = ∅.
3. For every goal G, there is a t ∈ [0, D] with (ψ(t) + e) ∩ G ≠ ∅.
4. For every r ∈ Req, ψ(t) + e ⊨ r.

## Required features of a reference trajectory

| Feature | Meaning | How the method achieves it |
|---|---|---|
| 1. Physical capability | The trajectory obeys system limits, such as the highest speed | Constants in the model, for example speed in `[0, SPEEDMAX]` [p. 6] |
| 2. Policy premises | The trajectory keeps the policy assumptions, such as action time intervals | Synchronisation of MTG and RTG, checked by Query (2) [p. 7] |
| 3. Faithful realisation | No behaviour outside the policy (faithfulness), and no policy behaviour missed (realisation) | Strategy compression and Queries (3) and (4) [p. 7–8] |
| 4. Reach-avoid | The trajectory satisfies Proposition III.1 with a tolerance | Width of a safe envelope as the tolerance e [p. 8] |

Source: Section III-B and Section IV-D. [p. 4, p. 6–8]

## Method

### Models for policy synthesis

The paper abstracts two kinds of action and builds one timed game for each.
[p. 5]

- **Movement TG.** Locations P1 and P2 are positions. Location F1T2 models
  the travel duration (the cost) from P1 to P2.
- **Task-execution TG.** It models the best-case and the worst-case
  execution time (BCET and WCET) of a task.
- In both models, the controller chooses only when to start an action. The
  environment decides when the action finishes. [p. 5]

### Controller models for test generation

- **MTG** (adjusted movement TG). Function `allow()` looks up the policy to
  check whether a move from P1 to P2 is allowed. [p. 6]
- **RTG** (reference controller TG). On channel `drive`, it goes to the
  committed location D1 and chooses a speed in `[0, SPEEDMAX]`. Turning is
  modelled in the same way but is not shown. [p. 6]
- At location `Moving`, the RTG goes back to D1 every `period` time units.
  Function `move()` samples one point of the reference trajectory there.
  [p. 6]
- On channel `leave`, the RTG and the MTG reach P2 together. Function
  `assignReward()` gives a reward when the trajectory meets conditions, for
  example a full stop at P2 after `cost` time units. [p. 6]

### Learning the decision strategy

The generator runs Query (1) on the network of MTG and RTG. [p. 6–7]

    strategy δ = maxE(x)[<=T]{dv}-->{cv}:<> CO     (1)

| Parameter | Setting in this paper |
|---|---|
| `x` | The reward that `assignReward()` updates |
| `T` | The maximum simulation time |
| `CO` | `time >= MAX`. `time` is a global clock that is never reset, and `MAX` is an estimate of the mission time |
| `dv` | The discrete variables that hold the sampled trajectory points |
| `cv` | Empty |

UPPAAL Stratego simulates the model. It keeps only the "good" runs, which
reach a state that satisfies `CO`. The learning algorithm sees the states
only through `dv` and `cv`. It scores the state-action pairs and updates the
strategy. Learning stops after a user-defined number of good runs or after
the total number of runs. [p. 6–7]

An external library is the learning algorithm. The same library stores the
outputs of the reference controller, and these outputs are the test cases.
[p. 7]

### Verification queries under the learned strategy

| Query | Formula | What it shows |
|---|---|---|
| (2) | `A[] forall (id:ValidID) syn[id] under δ` | MTG and RTG stay synchronised when actions start and finish, so the trajectories keep the policy premises |
| (3) | `A<> C.m under σ` | Every run of the policy σ accomplishes the mission |
| (4) | `A<> C*\|σ.m under δ` | Every run of the reference controller under σ and δ accomplishes the mission |

Source: Section IV-D. [p. 7–8]

- `syn` is an auxiliary variable. The emitting edge in MTG sets it to false,
  and the receiving edge in RTG sets it back to true. The query needs it
  because Query (1) allows only broadcast channels, so MTG can move without
  RTG. [p. 7]
- `C` is MTG alone, and `C*` is MTG with RTG. `m` turns true only when the
  mission is accomplished. [p. 7]
- The keyword `under` makes the model checker ask the external library for
  the best action whenever several controllable actions exist. [p. 7]
- During Queries (3) and (4), the library marks every visited state-action
  pair. After a pass, it removes the unmarked pairs from σ and δ. [p. 8]
- The paper states that if Queries (2) to (4) hold, δ stores the sampled
  points of the reference trajectories that realise σ. Faithfulness follows
  from the same queries. [p. 8]

## Case study: autonomous quarry

- Wheel loaders dig stones at stone piles and load them into trucks. Trucks
  carry the stones to a primary crusher and then to a secondary crusher.
  [p. 8]
- The scenario comes from the earlier paper [14]: one wheel loader, one
  truck, two primary crushers to choose from, and one secondary crusher.
  [p. 8]
- The policy sends the truck to the stone pile, then to a primary crusher,
  and then to the secondary crusher. The reference trajectories fill in when
  to accelerate, when to brake, and where to turn. [p. 8]
- The authors trained the model with Q-learning, removed the unused
  information, and saved the strategy as JSON. A Java program reads the
  JSON and contains the truck kinematics and tracking controller. [p. 8]

### Kinematics and tracking controller (appendix)

The truck is a unicycle model on a 2D map. [p. 11]

| Equation | Content |
|---|---|
| (5) Kinematics | ẋ = v·cos θ, ẏ = v·sin θ, θ̇ = w |
| (6) Tracking error | Rotation of (x_ref − x, y_ref − y) by θ; e_θ = θ_ref − θ |
| (7) Error dynamics | ė_x = w·e_y − v + v_ref·cos e_θ; ė_y = −w·e_x + v_ref·sin e_θ; ė_θ = w_ref − w |
| (8) Control law, speed | v = v_ref·cos e_θ + e_x |
| (9) Control law, turn | w = w_ref + v_ref·(e_y + sin e_θ) |
| (10) Lyapunov function | V = 1 + ½(e_x² + e_y²) − cos e_θ |

The tracking error on line segment i is bounded by √(l² + 4i), where l is
the initial deviation. The authors set a smaller bound in the Java program
to test against a stricter boundary. [p. 11]

## Results

| Sampling period | Efficiency | Effectiveness |
|---|---|---|
| 10 | 1.5 s per 10 test cases | 1 fault |
| 5 | 4.2 s per 10 test cases | 2 faults |
| 1 | 26.4 s per 10 test cases | 11 faults |

Source: Table I of the paper. [p. 8]

- Efficiency is the generation time per ten test cases. It does not include
  the verification time, which is under one second. [p. 8]
- Effectiveness is the number of faults detected in the same system under
  test. [p. 8]
- Generation time grows 17.6 times (26.4 / 1.5) when the period is ten
  times shorter. [p. 8]
- A shorter period gives more accurate sampling and more detected faults.
  [p. 8–9]
- The faults appear when the turning angle changes sharply. [p. 9]

## Limitations stated by the authors

- Graph-search-based synthesis suffers from state-space explosion and fails
  to finish in reasonable time for many models. [p. 11]
- Formal verification results depend on known and sometimes abstracted
  assumptions about the environment. [p. 4]
- Testing gives only finite results and says nothing outside the tested
  scenarios. [p. 4]
- UPPAAL Stratego supports only a subset of C, so a neural-network policy
  must run as an external library. [p. 6]
- The external-function feature needs the Stratego version of UPPAAL,
  4.1.20-7 or later. [p. 6]

## Future work stated by the authors

- Model the tracking controllers (TPTG) to select error-prone test cases.
  [p. 6, p. 9]
- Try other learning algorithms for test-case generation. [p. 9]
- Build the framework on an existing multi-agent platform such as GAMA.
  [p. 9]

## Related work, as the paper positions itself

- Araujo et al. review testing of autonomous systems. The paper claims to
  fill two gaps: a holistic framework for discrete and continuous aspects,
  and formal analysis of the generated test cases. [p. 9]
- Tao et al. generate test cases from ontologies with UML. This paper uses
  formal models to guarantee test-case quality. [p. 9]
- CPN4M (Gonçalves et al.) uses coloured Petri nets for the social level of
  multi-agent systems. The paper calls that work orthogonal, because it
  focuses on control. [p. 9]
- D'Urso et al. simulate multiple autonomous systems. Bersani et al.
  (PuRSUE) synthesise run-time control strategies with UPPAAL Tiga by graph
  search. [p. 9]
- The paper claims to be the first framework that combines policy synthesis
  and testing for multi-agent systems. [p. 2, p. 9]

## Reviewer notes

These notes are a reading of the paper, not claims from it.

- **What the guarantee covers.** Queries (2) to (4) check the model of MTG
  and RTG under the learned strategy. They show that the test cases match
  the policy. They do not show that the tracking controller or the real
  truck is safe. Safety of the real system rests on testing only.
- **Reach-avoid fidelity.** Feature 4 rests on a safe envelope from the
  literature and on a Lyapunov function for one chosen control law. The
  paper does not check Proposition III.1 on the generated trajectories with
  a query.
- **What a fault is.** The authors set a stricter bound than the Lyapunov
  bound in the Java program. The "faults" are therefore points that pass a
  bound that the authors chose. The paper does not seed known faults, and
  it does not say whether the 11 faults are distinct defects or violation
  points.
- **Evaluation size.** One scenario, one policy, and one controller. No
  baseline method and no repeated runs are reported. Learning is random, so
  the spread of the timings is unknown.
- **"All" trajectories.** The conclusion says the method finds "all the
  reference trajectories" that realise the policy (p. 9). The trajectories
  are sampled points, and `dv` holds only discrete values, so "all" applies
  to the discretised model.
- **Inconsistent references.** The main text cites graph-search synthesis
  as [13] and learning-based synthesis as [14] (p. 2, p. 5). The appendix
  cites them as [32] and [13] (p. 11).
- **Proposition III.1.** Condition (iv) uses t without a quantifier.
  Conditions (ii) and (iii) intersect a point with a set.
- **Verification versus undecidable.** The paper calls real-trajectory
  verification "extremely difficult" on p. 4 and "undecidable" on p. 11.
- **AI aspect.** Reinforcement learning proposes the behaviour, and the
  exhaustive model checker accepts or rejects it. This is a pattern of a
  learned component with a formal check after it.

## Terms

| Term | Meaning in this paper |
|---|---|
| Timed game (TG) | A timed automaton whose actions are split into controllable and uncontrollable ones |
| Priced timed game (PTG) | A TG with clock rates defined by ODEs, for example `pos' == cos(PI/4)` |
| Controllable / uncontrollable edge | Solid edge chosen by the controller / dashed edge chosen by the environment |
| Winning policy | A function from states to controllable actions that eventually reaches a winning state |
| Premises of a policy | The assumptions of a policy, such as the time intervals of actions |
| Reference trajectory | A path that the reference controller computes from the policy for the system to follow |
| Tracking error | The difference between the real and the reference trajectory |
| Faithfulness | No reference trajectory has behaviour that the policy does not allow |
| Realisation | Every path of the policy has a reference trajectory |
| Safe envelope | A region around a reference trajectory that bounds the tracking error |
| Lyapunov function | An energy-like function whose decrease shows that the error stays bounded |
| `maxE(x)` | UPPAAL Stratego query that learns a strategy to maximise the expected value of `x` |
| `under δ` | Model-check the model while strategy δ chooses the controllable actions |
| `A[] p` | Invariance: `p` holds in all states of all traces |
| `A<> p` | Liveness: every trace reaches a state where `p` holds |
| Committed location | A location with no delay; the next transition must leave a committed location |
| Broadcast channel | A channel whose sender can move even when no receiver is ready |
| Q-learning | A reinforcement-learning method that learns a score table of state-action pairs |

## Citation

Rong Gu and Eduard Enoiu. "Model-Based Policy Synthesis and Test-Case
Generation for Autonomous Systems." A-MOST'23, 2023.
