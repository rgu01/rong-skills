---
id: gu2021fm-collision-avoidance-nonlinear
title: "Model Checking Collision Avoidance of Nonlinear Autonomous Vehicles"
authors:
  - Rong Gu
  - Cristina Seceleanu
  - Eduard Enoiu
  - Kristina Lundqvist
affiliation: Mälardalen University, Sweden
year: 2021
venue: FM'21
venue_source: author's publications page (the PDF does not name the venue)
doi: null
document_type: conference paper
pages_in_pdf: 18
pdf_url: https://drive.google.com/file/d/1JllhXoiipaHY71BxVhOs9vVZQdJkYGYX/view?usp=sharing
listing_url: https://sites.google.com/view/ronggu/publications
author_keywords: []  # the PDF prints no keywords
topics: [formal verification, model checking, autonomous vehicles, collision avoidance, nonlinear kinematics, hybrid systems, reach-avoid properties, discretization, state-space reduction, black-box algorithm verification]
formalisms: [hybrid transition systems, discrete-time transition systems, timed automata, TCTL]
tools: [UPPAAL STRATEGO 4.1.20-stratego-74]
algorithms: [dipole flow field, Theta*, RRT]
application: autonomous vehicle with a dipole-flow-field collision-avoidance algorithm, against static and dynamic obstacles
abbreviations: {AV: autonomous vehicle, PWC: piece-wise-continuous, HTS: hybrid transition system, UTA: Uppaal timed automata, CTL: computation tree logic, TCTL: timed computation tree logic, WP: waypoints, TT: travelling time, DO: dynamic obstacles, VA: allowed velocities, NOS: number of states, CT: computation time, DLL: dynamic-link library, SO: shared object}
funding: Swedish Knowledge Foundation, DPAC profile grant 20150022 and ACICS synergy grant 20190038
---

# Model Checking Collision Avoidance of Nonlinear Autonomous Vehicles (Gu et al., FM 2021)

## At a glance

This 2021 paper by Gu, Seceleanu, Enoiu, and Lundqvist verifies the
collision avoidance of autonomous vehicles (AV) with nonlinear kinematics.
Exhaustive model checking of nonlinear hybrid systems is undecidable. The
authors prove two theorems that reduce the check of the real nonlinear
trajectory to a check of a piece-wise-continuous (PWC) reference
trajectory, and then to a check of a discrete-time trajectory. They model
the discrete-time behavior as timed automata in UPPAAL STRATEGO. The
collision-avoidance algorithm runs as an external C library, so the model
treats it as a black box. Dynamic obstacles start and move
nondeterministically. Model checking finds two bugs in a dipole-flow-field
algorithm. The improved algorithm passes in scenarios with one dynamic
obstacle but fails with two.

Page references `[p. N]` point to the 18-page PDF. The PDF page numbers
match the printed page numbers.

## Key facts

Each fact is a claim from the paper unless it is marked otherwise.

- The FM'21 collision-avoidance paper checks two requirements: collision
  avoidance (an invariance property) and destination reaching (a liveness
  property). [p. 4]
- The FM'21 paper calls an AV "controllable" when its tracking error has a
  Lyapunov function. Then the deviation from the reference path is bounded.
  [p. 2]
- Theorem 1 of the FM'21 paper reduces collision-avoidance verification of
  the actual nonlinear trajectory to a check of the PWC reference
  trajectory with a distance margin L. [p. 8]
- Theorem 2 of the FM'21 paper reduces the PWC check to a check of
  discrete-time trajectories, if the sampling period ε is at most L / ||V||.
  [p. 9–10]
- The FM'21 paper states that the reduction is sufficient but not
  equivalent: a safe actual trajectory can have a reference trajectory
  nearer than L to an obstacle. [p. 8]
- The FM'21 model has four reusable UPPAAL templates: AV parameter, AV
  controller, obstacle initialization, and obstacle movement. [p. 11–12]
- The collision-avoidance algorithm runs as an external library (DLL on
  Windows, SO on Linux) that UPPAAL STRATEGO calls during model checking.
  [p. 11]
- The FM'21 approach uses only the exhaustive model checking of UPPAAL
  STRATEGO, not its strategy synthesis. [p. 10]
- Dynamic obstacles in the FM'21 model change acceleration and heading only
  every N sampling periods, with N > 1. [p. 9, p. 12]
- The FM'21 queries are `A[] !collision` for obstacle avoidance and
  `A<> controller.STOP` for destination reaching. [p. 12]
- The FM'21 experiments run on a server with Ubuntu 18.04, 48 CPUs, and
  256 GB memory, with UPPAAL 4.1.20-stratego-74. [p. 13]
- Model checking found two problems in the original dipole-flow-field
  algorithm: the AV is drawn toward the obstacle, and a livelock that ends in
  a collision at the map boundary. [p. 15]
- The improved FM'21 algorithm passes both requirements in scenarios S1 to
  S4, which have one dynamic obstacle. [p. 14–15]
- With two dynamic obstacles (S5), the improved algorithm fails obstacle
  avoidance. Destination reaching still holds, because the vehicle model
  does not stop after a collision. [p. 14–15]
- The largest FM'21 run is destination reaching in S5: 226,896,902 states in
  43.2 minutes. [p. 14]
- The models and the external library are at
  https://github.com/rgu01/FM2021. [p. 13]

## Questions this paper answers

**Why is the problem hard?** Model checking of nonlinear hybrid systems is
undecidable. Tracking errors and unpredictable dynamic obstacles make it
harder. [p. 2]

**How do the authors make it decidable?** They use bounded tracking errors
from Fan et al. as "safe zones" around the reference path. Then they
discretize time with a sampling period small enough for the obstacle speed.
Reach-avoid verification of discrete-time systems is decidable. [p. 2,
p. 10]

**How do they handle unknown obstacles?** An obstacle template chooses all
initial values nondeterministically. Exhaustive model checking then covers
every enumerated obstacle start and movement. [p. 12]

**Can a user verify their own algorithm?** Yes. The user compiles the
algorithm as a library, sets the parameters, and instantiates the
templates. A false result gives a counterexample for debugging. [p. 11]

**How do they fight state-space explosion?** They limit the initial
obstacle positions to a "valid area" and split long journeys into phases.
[p. 12–13]

**What did they find?** Two design bugs in a dipole-flow-field algorithm.
The fixed version still fails with two dynamic obstacles. [p. 15]

**How expensive is it?** From 1.8 seconds to 43.2 minutes per query, and
from about 0.4 million to 227 million states. [p. 14]

## Scope: what this paper does not do

- It does not compute the tracking-error bound L. It takes L from the
  method of Fan et al. [p. 8, p. 11]
- It does not choose the time span T of the safety-critical segment. The
  authors leave T to design engineers. [p. 8]
- It does not verify scenarios in which an obstacle appears in the
  "closest area", because no algorithm can avoid such an obstacle. [p. 13]
- It does not give the figures of the UPPAAL templates or the parameter
  specification. These are in a technical report. [p. 11–12]
- It does not verify the source code of the algorithm. It calls the
  compiled library inside an abstract vehicle model.
- It does not use statistical model checking. The authors list that as
  future work. [p. 16]
- It names no DOI and no venue inside the PDF.

## System under verification

The AV controller has a path planner (for example Theta* or RRT), a
reference controller, a tracking controller, and a collision-avoidance
module. [p. 3–4] The path planner gives waypoints W that avoid the known
static obstacles. The collision-avoidance module uses the map M, the
waypoints, and the perceived dynamic obstacles. [p. 4]

The algorithm under test uses dipole flow fields. Static flow fields pull
the AV along the reference path and push it from static obstacles. Dipole
fields around moving objects create magnetic moments that push the AV and
the obstacle apart. [p. 13–14]

## Requirements in natural language

The command controller must meet two requirements. [p. 4]

1. **Collision avoidance (invariance).** Always circumvent the static and
   dynamic obstacles.
2. **Destination reaching (liveness).** Always eventually reach the goal
   area.

## Formal definitions

| No. | Definition | Content |
|---|---|---|
| 1 | Map | M = <X, O_u, I, G>: moving space in R^d with d ∈ {2, 3}, unsafe area, initial area, goal area [p. 5] |
| 2 | Agent state | S = <p, v, a, θ, ω>: position, linear velocity (‖v‖ ≤ V_max), acceleration, heading in [−π, π], rotational velocity [p. 5] |
| 3 | Controller | C = <pl, ca, Λ>: path planner, collision-avoidance function, commands {ACC, BRK, TR+, TR−, STR} [p. 6] |
| 4 | Continuous trajectory | A run of a hybrid transition system with delayed and instantaneous transitions [p. 6] |
| 5 | Reference trajectory | PWC segments joined at waypoints; the heading changes only at waypoints, and ω = 0 [p. 6–7] |
| 6 | Safety-critical segment | sc(ξ) = ξ(C − T, C + T) around the current time C [p. 7] |
| 7 | Collision-avoidance verification | The actual trajectory reaches G, avoids O_u, and its safety-critical segment does not meet that of any obstacle [p. 8] |
| 8 | Discrete-time trajectory | Agents are sampled together every ε; an agent that passes its waypoint stops there until the next period [p. 8–9] |

The paper denotes the AV and the dynamic obstacles together as "agents".
[p. 5]

## Reduction theorems

- **Theorem 1 (nonlinearity to PWC).** Assume the tracking errors have a
  Lyapunov function, and a goal point p_g is at distance B from the edge of
  G. If ξ_r reaches p_g, d(ξ_r, O_u) > L, and d(sc(ξ_r), sc(ξ_o)) > L with
  L ≤ B, then the condition of Definition 7 holds. [p. 8]
- **Theorem 2 (PWC to discrete time).** Let L = L_a + L_o, where L_a is the
  AV tracking-error bound and L_o is the smallest tracking-error bound
  among the dynamic obstacles. If ε ≤ L / ||V||, then the reach-avoid
  condition on the discretized trajectories implies the same condition on
  the PWC trajectories. [p. 9]
- L_o is zero when no dynamic obstacle is detected. [p. 9]
- The proof of Theorem 1 uses Lemmas 2 and 3 of Fan et al. [p. 8]
- The proof of Theorem 2 argues by contradiction: an obstacle that crosses
  the margin between two samples must move more than L in one period, but it
  moves at most ||V|| × ε. [p. 10]

## Verification approach

The workflow has four steps. [p. 11]

1. The user supplies the nonlinear vehicle model to compute the
   tracking-error bound, with the method of Fan et al.
2. The user configures parameters, such as the minimum and maximum values of
   the agent-state elements.
3. The tool instantiates the UPPAAL templates and embeds the algorithm
   library.
4. The model checker explores the state space. "True" means that the
   algorithm is correct for this parameter configuration. "False" gives a
   counterexample.

The UPPAAL templates act only at the end of each sampling period. The
authors state that the discrete-time semantics conservatively abstracts the
template semantics. [p. 10–11]

| Template | Role |
|---|---|
| AV parameter | Holds one AV parameter and updates it at the end of each period [p. 11–12] |
| AV controller | Initializes the AV, triggers the parameter updates, turns at waypoints, and calls the collision-avoidance library [p. 12] |
| Obstacle initialization | Chooses each initial obstacle parameter nondeterministically from its range [p. 12] |
| Obstacle movement | Updates the obstacle every period, and changes its acceleration and heading every N periods [p. 12] |

`collision` becomes true when the distance from the AV's safety-critical
segment to any obstacle is less than the tracking-error bound. [p. 12]

## State-space reduction

- **Safety-critical area.** The area of Definition 6. [p. 13]
- **Closest area.** Positions within V × n × ε of the safety-critical
  segment. An obstacle that appears here cannot be avoided, so the model
  excludes it. [p. 13]
- **Valid area.** Positions between V × n × ε and V × m × ε. Here m depends
  on the sensor detection period. Only these positions are initial obstacle
  positions. [p. 13]
- The initial heading of an obstacle covers the full range from −π to π,
  and the linear velocity is not reduced. [p. 13]
- **Phased verification.** A long journey is split into phases. If the
  states that join the phases do not change, the conjunction of the phase
  results implies the result for the whole journey. [p. 13]

## Verification results

In S1 and S2, the obstacle moves at its highest speed and can appear at
any moment. S3 is a longer journey in three phases, S3.1 to S3.3. In S4,
the obstacle has three possible velocities. In S5, at most two dynamic
obstacles are in the map at the same time. No obstacle is known to the AV
before it comes near. [p. 14]

| S | WP | TT | DO | VA | Avoid: NOS | Avoid: CT | Avoid | Reach: NOS | Reach: CT | Reach |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | 2 | 25 | 1 | 1 | 547,617 | 2.7 s | true | 545,505 | 5.5 s | true |
| S2 | 6 | 25 | 1 | 1 | 411,747 | 1.8 s | true | 411,168 | 3.6 s | true |
| S3 | 2 | 85 | 1 | 1 | 3,222,290 | 15.3 s | true | 3,217,767 | 31.8 (no unit) | true |
| S3.1 | 1 | 30 | 1 | 1 | 1,532,082 | 7.4 s | true | 1,527,811 | 15.7 s | true |
| S3.2 | 1 | 30 | 1 | 1 | 1,183,792 | 5.5 s | true | 1,185,550 | 11.4 s | true |
| S3.3 | 1 | 25 | 1 | 1 | 506,416 | 2.4 s | true | 504,406 | 4.7 s | true |
| S4 | 2 | 15 | 1 | 3 | 12,317,809 | 1.0 min | true | 12,498,924 | 2.1 min | true |
| S5 | 2 | 15 | 2 | 1 | 1,398,011 | 7.6 s | false | 226,896,902 | 43.2 min | true |

Source: Table 1, "Verification results of the improved version of the
algorithm". [p. 14]

## Problems found by model checking

The original algorithm failed the reach-avoid verification in all
scenarios. [p. 14–15]

- **Problematic scenario 1.** One obstacle is slower than the AV. The dipole
  fields sometimes draw the AV toward the obstacle until they are too near,
  because magnetic moments can push or pull. Fix: turn the direction of the
  magnetic moments before the two get too close. [p. 15]
- **Problematic scenario 2.** The AV and the obstacle move straight toward
  each other. The moments act only on their common line, so the AV backs up,
  turns 180°, and meets the obstacle again. This repeats until the AV stops at
  the map boundary and the obstacle hits it. This is the livelock that the
  authors also found in their 2018 wheel-loader paper. Fix: force the AV to
  turn slightly when its heading is opposite to the obstacle heading.
  [p. 15]
- **Remaining failure.** The improved algorithm fails obstacle avoidance in
  S5 with two dynamic obstacles. [p. 15]

## Limitations stated by the authors

- The reductions are sufficient, not equivalent. [p. 8]
- Without phases or area reduction, the full enumeration of obstacle
  positions, speeds, and headings can make the state space infeasible.
  [p. 12]
- The approach assumes that acceleration and rotational velocity change
  discretely. If not, the authors say to discretize them like position and
  velocity. [p. 9]
- A "true" result holds only "under the current parameter configuration".
  [p. 11]

## Future work stated by the authors

- Handle more complex vehicle models with more kinematic detail. [p. 16]
- Use statistical verification for cases where the distance is smaller than
  the tracking-error bound but a collision does not necessarily occur.
  [p. 16]
- Improve the algorithm for multiple dynamic obstacles. [p. 15]

## Related work, as the paper positions itself

The paper cites theorem proving with differential dynamic logic in
KeYmaera, runtime verification of maneuver automata, maritime games in
UPPAAL STRATEGO, and the APEX tool. The authors claim two differences:
they prove a reduction to a decidable discrete-time problem, and they give
counterexamples that help to improve algorithms. They also claim a
generic interface for user algorithms. [p. 16] Their method is orthogonal
to controller synthesis: synthesis builds motion plans, and this method
verifies them. [p. 2, p. 16]

## Reviewer notes on requirement fidelity

These notes are a reading of the paper, not claims from it.

- **Completeness claim.** The introduction says the reduction is done
  "without losing completeness", and Section 4.3 says the same for state
  reduction. Section 3.2 says the problems "are not equivalent". The
  reduction is sound for "true" results. A "false" result can be a false
  alarm, because `collision` uses the conservative distance margin. [p. 2,
  p. 8, p. 12]
- **Destination reaching.** `A<> controller.STOP` holds in S5 although
  collisions occur, because the model does not stop at a collision. The
  liveness query therefore does not mean "reach the goal safely". The
  natural-language "reach-avoid" intent is the conjunction of both queries.
- **Excluded obstacles.** Obstacles that start in the closest area are
  removed. The "true" results say nothing about these starts.
- **Obstacle model.** Obstacles change direction only every N periods. A
  "true" result does not cover obstacles that change direction faster.
- **Choice of L_o.** Theorem 2 uses the smallest tracking-error bound among
  the obstacles. A sound margin for all obstacles would seem to need the
  largest one. The paper does not explain the choice. [p. 9]
- **Margin in Theorem 1.** Theorem 1 uses one margin L for the AV, but the
  obstacle trajectory is the actual one. Theorem 2 then adds L_o. The paper
  does not state how Theorem 1 accounts for obstacle tracking error.
- **Table 1.** The S3 row is the sum of S3.1 to S3.3 for states and time.
  The S3 reach time "31.8" has no unit. S3 has 2 waypoints, but each phase
  has 1. [p. 14]
- **Discrete values.** The paper does not state in this PDF the resolution
  of positions, speeds, and headings that the obstacle template enumerates.
  The coverage of "all circumstances" depends on that resolution.
- **Black-box library.** The model checker calls the compiled algorithm, so
  the verified behavior is that of the real library code inside the
  abstract vehicle model. This is a strength for fidelity to the
  implementation of the algorithm.
- **Running header.** The running header drops "Nonlinear" from the title.

## Terms

| Term | Meaning in this paper |
|---|---|
| AV | Autonomous vehicle |
| Agent | An AV or a dynamic obstacle |
| Reach-avoid requirement | Reach the goal and avoid all obstacles |
| Tracking error | The deviation of the actual trajectory from the reference trajectory |
| Lyapunov function | An energy-like function that proves the tracking error stays bounded |
| Safe zone | The band around the reference path that the tracking-error bound gives |
| PWC trajectory | Piece-wise-continuous reference trajectory, made of segments between waypoints |
| Hybrid transition system (HTS) | A transition system with continuous and discrete variables |
| Safety-critical segment | The part of a trajectory within ±T of the current time |
| Sampling period ε | The time step of the discrete-time model |
| Closest area, valid area | Zones for initial obstacle positions; only the valid area is checked |
| Phased verification | Splitting a long journey into shorter checks |
| UPPAAL STRATEGO | A UPPAAL branch for stochastic timed games that can call external C libraries |
| `A[] p` | `p` holds in every state of every path |
| `A<> p` | On every path, `p` holds at some time |
| Dipole flow field | A collision-avoidance method with static flow fields and dipole fields |
| Livelock | The AV moves forever without reaching its goal |
| NOS, CT | Number of explored states, computation time |

## Citation

Rong Gu, Cristina Seceleanu, Eduard Enoiu, and Kristina Lundqvist. "Model
Checking Collision Avoidance of Nonlinear Autonomous Vehicles." FM'21, 2021.
