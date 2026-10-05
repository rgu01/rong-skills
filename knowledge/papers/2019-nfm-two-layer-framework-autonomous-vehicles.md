---
id: gu2019nfm-two-layer-framework
title: "Towards a Two-layer Framework for Verifying Autonomous Vehicles"
authors:
  - Rong Gu
  - Raluca Marinescu
  - Cristina Seceleanu
  - Kristina Lundqvist
affiliation: Mälardalen University, Västerås, Sweden
year: 2019
venue: NFM'19
venue_source: author's publications page (the PDF does not name the venue)
doi: null
document_type: conference paper
pages_in_pdf: 17
pdf_url: https://drive.google.com/file/d/1IoIML_okCZHX4PigA20LZyGdzi_5ws-C/view?usp=sharing
listing_url: https://sites.google.com/view/ronggu/publications
author_keywords: null
topics: [formal verification, statistical model checking, autonomous vehicles, construction machinery, path planning, collision avoidance, hybrid systems, embedded control systems, modelling patterns, separation of concerns]
formalisms: [hybrid automata, weighted metric temporal logic, ordinary differential equations]
tools: [UPPAAL SMC]
algorithms: [Theta*, dipole flow field]
application: autonomous wheel loader on a construction site
abbreviations: {AWL: autonomous wheel loader, HA: hybrid automata, SMC: statistical model checking, ODE: ordinary differential equation, LOS: line of sight, BDI: Beliefs Desires Intentions, MMT: Mission Management Tool, CTL: Computation Tree Logic}
funding: DPAC project, Swedish Knowledge Foundation, grant 20150022
---

# Towards a Two-layer Framework for Verifying Autonomous Vehicles (Gu et al., NFM 2019)

## At a glance

This 2019 paper by Gu, Marinescu, Seceleanu, and Lundqvist proposes a
conceptual framework with two layers for the verification of autonomous
vehicles. A static layer does path and mission planning on a discrete grid.
A dynamic layer checks the execution of the plan with continuous vehicle
motion and moving obstacles. The paper builds only the dynamic layer. It
models it as hybrid automata in UPPAAL SMC, with reusable patterns for the
vehicle motion, the scheduler, and the processes. The case study is an
industrial prototype of an autonomous wheel loader (AWL). Statistical model
checking gives a probability interval of [0.902606, 1] at 95% confidence
from 36 runs for path following and for collision avoidance.

Page references `[p. N]` point to the 17-page PDF.

## Key facts

Each fact is a claim from the paper unless it is marked otherwise.

- The two-layer framework separates static high-level planning from dynamic
  functions such as collision avoidance. [p. 1–2]
- The static layer of the framework is a tuple of a discrete environment,
  known static obstacles, and milestones with mission order and timing
  requirements. [p. 6]
- The dynamic layer of the framework is a tuple of a continuous environment,
  the trajectory plan from the static layer, static obstacles, predefined
  moving obstacles, and unforeseen moving obstacles. [p. 7]
- The static layer is "still at the conceptual stage". The paper lists
  DRONA, Rebeca, and MMT as possible options for it. [p. 7]
- The framework design allows exhaustive verification in the static layer
  but only probabilistic verification in the dynamic layer. [p. 7]
- The AWL dynamic-layer model uses hybrid automata in UPPAAL SMC, with ODEs
  for the vehicle motion. [p. 2, p. 8]
- The AWL model uses the Theta* algorithm for the initial path and the
  dipole flow field algorithm for collision avoidance, both as C functions
  in UPPAAL SMC. [p. 2]
- The AWL control unit has three parallel processes: ReadSensor, Main, and
  CalculateNewPath, on independent cores. [p. 5]
- In the AWL paper, CAN buses connect the vision unit, the control unit, and
  the execution unit. [p. 5]
- The AWL scheduler pattern is parallel, predictable, and non-preemptive. It
  is inspired by Timed Multitasking. [p. 9]
- The AWL case study uses a continuous 55 × 55 map with five static
  obstacles, two predefined moving obstacles, and one obstacle that the
  model generates during verification. [p. 13]
- For the AWL path-following queries, UPPAAL SMC gives a probability
  interval of [0.902606, 1] with 95% confidence from 36 runs. [p. 14]
- For the AWL collision query `Pr[<=110]([] !collided)`, UPPAAL SMC gives
  the same interval [0.902606, 1] with 95% confidence from 36 runs. [p. 14]
- The AWL collision monitor counts a collision when the AWL is closer than a
  distance threshold of 0.8 to an obstacle. [p. 14]
- In the AWL model, Theta* runs in a preprocessing step of process Main. The
  authors plan to move it to the static layer later. [p. 12]

## Questions this paper answers

**What is the two-layer framework?** A separation of the verification of an
autonomous vehicle into a static planning layer and a dynamic execution
layer. The layers exchange data through a communication protocol. [p. 6]

**What did the authors build and verify?** Only the dynamic layer. It is a
network of hybrid automata in UPPAAL SMC for the AWL control unit, the
vehicle motion, and the obstacles. The static layer is not built.

**Which tool and logic did they use?** UPPAAL SMC with hybrid automata and
queries in an extension of weighted metric temporal logic, of the form
`Pr[bound](ap)`. [p. 3]

**How does this paper relate to the 2018 AWL paper?** The paper says that
it improves on earlier formal models of vehicle movement, its own 2018 AWL
model included, with a continuous motion model. It uses Theta*, where the
earlier study used A*. [p. 2, p. 4]

**What are the modelling patterns?** Reusable automata skeletons for the
linear motion and rotation of the vehicle, for the scheduler, and for a
generic process with a state module and an operation module. [p. 8–11]

**What were the results?** Path following and collision avoidance each have
an estimated probability of at least 0.902606, at 95% confidence, from 36
runs. [p. 14]

**Is the verification exhaustive?** No. UPPAAL SMC gives statistical
estimates from simulation runs, not proofs over all behaviors. [p. 7]

## Scope: what this paper does not do

- It does not build or verify the static layer. [p. 7, p. 16]
- It does not define the communication protocol between the two layers.
- It does not give exhaustive results. The dynamic layer supports only
  probabilistic verification. [p. 7]
- It does not model digging or loading. [p. 6]
- It does not model computation in the vision unit and the vision sensors.
  They are data structures only. [p. 8]
- It does not use user-defined probability distributions. Only the default
  uniform distributions for time-bounded delays are used. [p. 3]
- It does not model obstacles with arbitrary motion. The moving obstacles
  go at a constant speed, in the same or the opposite direction of the AWL.
  [p. 13]
- It does not give the model size, the run time, or the hardware of the
  verification.
- It names no DOI and no venue inside the PDF.

## The two-layer framework

| Layer | Definition | Environment | Verification | Status in the paper |
|---|---|---|---|---|
| Static | `< Es, Ss, Ms >`: discrete environment, known static obstacles, milestones with order and timing | Discrete Cartesian grid | Exhaustive is possible | Conceptual; DRONA, Rebeca, or MMT proposed |
| Dynamic | `< Ed, Ts, Sd, Md, Dd >`: continuous environment, trajectory plan, static obstacles, predefined and unforeseen moving obstacles | Continuous, with ODEs | Probabilistic only | Modelled and verified for the AWL |

Source: Section 4. [p. 6–7]

Benefits that the authors claim for the two-layer design: [p. 7]

- A separation of concerns for design, modelling, and verification.
- A change to an algorithm or a design stays inside its layer, so errors do
  not propagate to the entire system.
- The framework is open for more layers, for example for artificial
  intelligence or centralized control.

## System under verification

The AWL control system has a vision unit, a control unit, and an execution
unit. CAN buses connect them. The paper focuses on the control unit. [p. 5]

| Element | Role |
|---|---|
| ReadSensor process | Reads LIDAR, GPS, angle, and speed sensors, and writes to shared memory |
| Main process | Runs path planning and calls the Execution Function |
| AdjustAngle function | Adjusts the moving angle from the positions of the AWL and the obstacles |
| Turn function | Checks if the AWL is at a milestone and changes direction |
| Arrive function | Checks if the AWL is at the destination and sends commands |
| CalculateNewPath process | Runs collision avoidance and makes a new safe path segment, if one exists |

Source: Section 3. [p. 5–6]

## Modelling patterns

**Execution unit (the plant).** Two hybrid automata, for linear motion and
for rotation. The motion follows three ODEs: `ẋ = v cos θ`, `ẏ = v sin θ`,
`θ̇ = ω`. The linear motion pattern has four locations: Idle, Acc (acceleration),
Constant, and Dec (deceleration). At Acc, the instance sets
`v' == (AF − k*m)/m`. A brake channel or the maximum speed `maxS` moves the
automaton to Dec or Constant. [p. 8]

**Scheduler.** The scheduler discretizes time into basic units with an
invariant `xd <= UNIT` and a guard `xd == UNIT`. A `PROCESS` structure holds
an id, a running flag, a period counter, and an execution-time counter. The
scheduler puts processes into a `ready` queue and a `done` queue. It uses the
channels `execute`, `finish`, and `output`. A process consumes input at its
trigger and produces output at its deadline. [p. 9–11]

**Process.** A state module (discrete automata) plus an operation module
(automata or code). The skeleton has the locations Start, O1, Idle, and
Notification. All locations except Start and Idle are urgent. A process with
invalid input goes back to Start with no output. A broadcast channel
`notify[id]` tells other processes that output is ready. [p. 9–11]

**AWL instance.** The motion patterns and the scheduler go into the AWL
model with parameter values only. The state module of Main extends the
process pattern with a Theta* preprocessing step. Main calls the Execution
Function through channel `invoke[0]`. [p. 11–13]

## Verification setup

- Map: continuous, 55 × 55. [p. 13]
- Obstacles: five static, two predefined moving, and one moving obstacle
  that an automaton called `generator` spawns during verification. [p. 13]
- Moving obstacles: one unit distance per second, in the same or the
  opposite direction of the AWL. [p. 13]
- AWL parameters: weight, acceleration and deceleration force, friction
  coefficient, and maximum speed, all constants. [p. 13]
- A `monitor` automaton, triggered by the scheduler each time unit, updates
  the Boolean variables `followedPath` and `collided`. [p. 14]

## Verification results

| Requirement | Query | Result |
|---|---|---|
| Path generation and following | `simulate 1[<=110] {pcx, pcy}` | One trace; the AWL follows the path and avoids all static obstacles |
| | `Pr[<=70](<> arrived && counter <= 60)` | [0.902606, 1], 95% confidence, 36 runs |
| | `Pr[<=110]([] followedPath)` | [0.902606, 1], 95% confidence, 36 runs |
| Collision avoidance | `simulate 1[<=110] {pcx, pcy, ocx[0], ocy[0], ocx[1], ocy[1], ocx[3], ocy[3]}` | One trace with three moving obstacles (Fig. 11) |
| | `Pr[<=110]([] !collided)` | [0.902606, 1], 95% confidence, 36 runs |

Source: Section 6.2. [p. 13–14] The paper reports one interval for the two
path-following queries together. [p. 14]

How the queries work:

- `arrived` is a Boolean variable for arrival at the destination.
  `counter` is a clock for the time to arrive. [p. 14]
- `followedPath` shows whether the AWL went to the destination and back to
  the start through all milestones in order. [p. 14]
- In the trace of Fig. 11, obstacle "C" moves "recklessly" towards the AWL,
  and the AWL turns around to avoid it. The two trajectories overlap, but
  the authors say the AWL and "C" are not at the same position at the same
  time. [p. 14]

## Limitations stated by the authors

- The static layer is at the conceptual stage. [p. 7]
- The dynamic layer gives only probabilistic verification, as a trade-off
  for more realistic models. [p. 7]
- The discrete grid of the static layer is "not entirely faithful to
  reality". [p. 7]
- Theta* runs inside the dynamic-layer model for now. [p. 12]

## Future work stated by the authors

- Report on the static layer and on the combination of the two layers.
  [p. 16]
- Move Theta* from process Main to the static layer. [p. 12]

## Related work, as the paper positions itself

- Automata-based planning methods use temporal logic for vehicle routing.
  They do not consider sensor transmission times or unforeseen obstacles.
  [p. 15]
- Runtime verification adds monitors to a running system. Its usual
  problem is runtime overhead. [p. 15]
- Agent-based methods translate BDI agent languages into formal languages.
  They usually do not cover the embedded control system or the vehicle
  dynamics. [p. 15]
- Framework approaches include a Kripke model for an unmanned aerial vehicle
  checked against CTL, and a combination of model checking and runtime
  verification for robots. The paper claims that its framework adds the
  collision-avoidance algorithm and a continuous environment. [p. 15]

## Reviewer notes on requirement fidelity

These notes are a reading of the paper, not claims from it.

- The interval [0.902606, 1] equals the two-sided 95% Clopper-Pearson
  interval for 36 successes in 36 runs. The results therefore show no
  failed run, but they bound the failure probability only at about 10%.
- One interval covers both path-following queries, so the paper does not
  separate their results. [p. 14]
- The query `Pr[<=110]([] followedPath)` uses "always". But the text
  defines `followedPath` as true after a full round trip. Taken literally,
  the variable is false at the start. The text does not explain how the
  query can then pass. [p. 13–14]
- The `monitor` samples the state once per time unit, with a distance
  threshold of 0.8. A collision between two samples can stay undetected.
  The result depends on this sampling assumption. [p. 14]
- Requirement "run the dipole flow field algorithm timely" has no time bound
  in any query. The collision query checks only that `collided` stays false.
  [p. 14]
- The text gives `v(t) = (F − k×M)/M` as the velocity. The automaton in
  Fig. 4(b) uses the same expression for the derivative `v'`. The second
  form is the acceleration. [p. 8]
- Theta* uses a Euclidean `g(n)` and a Manhattan `h(n)`. A Manhattan
  heuristic can overestimate the Euclidean cost, so the path is not
  guaranteed to be the shortest. [p. 4]
- The section heading says "Two-level Framework", but the rest of the paper
  says "two-layer". [p. 6]
- The paper calls the framework "conceptual". Only one of the two layers
  has a model and results, so the main claim of the framework, the
  decoupling of the layers, is not tested.

## Terms

| Term | Meaning in this paper |
|---|---|
| AWL | Autonomous wheel loader, the machine in the case study |
| Hybrid automata (HA) | State machines with continuous variables whose rates follow differential equations in each location |
| UPPAAL SMC | The statistical model checker of the UPPAAL tool, for stochastic hybrid automata |
| Statistical model checking (SMC) | Verification by many random simulation runs, with a probability estimate and a confidence level |
| `Pr[bound](<> p)` | The probability that `p` becomes true within the time bound |
| `Pr[bound]([] p)` | The probability that `p` stays true for the whole time bound |
| Static layer | The planning layer, with a discrete map, static obstacles, and milestones |
| Dynamic layer | The execution layer, with continuous motion and moving obstacles |
| Milestone | A point of operation of the vehicle, for example for digging or loading |
| Theta* | An any-angle variant of A* that uses line-of-sight checks to make paths with fewer turns |
| Dipole flow field | A collision-avoidance method. A static flow field pulls the vehicle to the path and pushes it from obstacles. A dipole field around each moving object pushes moving objects apart. |
| Urgent location | A location where time cannot pass |
| Broadcast channel | A non-blocking synchronization: the sender does not wait for receivers |
| Non-preemptive scheduling | A running process is not interrupted by another process |

## Citation

Rong Gu, Raluca Marinescu, Cristina Seceleanu, and Kristina Lundqvist.
"Towards a Two-layer Framework for Verifying Autonomous Vehicles." NFM'19,
2019.
