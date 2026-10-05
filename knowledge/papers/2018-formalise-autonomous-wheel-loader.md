---
id: gu2018formalise-wheel-loader
title: "Formal Verification of an Autonomous Wheel Loader by Model Checking"
authors:
  - Rong Gu
  - Raluca Marinescu
  - Cristina Seceleanu
  - Kristina Lundqvist
affiliation: Mälardalen University, Västerås, Sweden
year: 2018
venue: FormaliSE'18
venue_source: author's publications page (the PDF does not name the venue)
doi: null
document_type: conference paper
pages_in_pdf: 10
pdf_url: https://drive.google.com/file/d/18bBbX9Uu-V7bl220oUfQd9w2cMhlqpeB/view?usp=sharing
listing_url: https://sites.google.com/view/ronggu/publications
author_keywords: [autonomous vehicle, collision avoidance, formal verification, timed automata, UPPAAL, model checking]
topics: [formal verification, model checking, autonomous vehicles, construction machinery, path planning, collision avoidance, real-time systems, requirement formalization]
formalisms: [timed automata, TCTL]
tools: [UPPAAL]
algorithms: [A*, dipole flow field]
application: autonomous wheel loader in a quarry
abbreviations: {AWL: autonomous wheel loader, TA: timed automata, TCTL: Timed Computation Tree Logic, SMC: statistical model checking, IMU: inertial measurement unit}
funding: DPAC project, Swedish Knowledge Foundation, grant 20150022
---

# Formal Verification of an Autonomous Wheel Loader by Model Checking (Gu et al., FormaliSE 2018)

## At a glance

This 2018 paper by Gu, Marinescu, Seceleanu, and Lundqvist models the control
system of an autonomous wheel loader (AWL) as a network of timed automata. It
verifies the model with the UPPAAL model checker. The model includes two
navigation algorithms as C functions: A* for the initial path and the dipole
flow field algorithm for collision avoidance. Four natural-language
requirements from industry become 16 TCTL queries, and all 16 queries pass on
the abstract model. When the obstacle moves freely, UPPAAL finds a collision
and a livelock.

Page references `[p. N]` point to the 10-page PDF.

## Key facts

Each fact is a claim from the paper unless it is marked otherwise.

- The AWL paper verifies an industrial prototype of an autonomous wheel loader
  that carries rocks between a stone pile and a crusher in a quarry. [p. 1–2]
- The AWL control system has a vision unit, a control unit, and an execution
  unit, connected by Ethernet, with seven tasks in total. [p. 2]
- The AWL tasks communicate asynchronously: a task does not wait for a reply
  after it sends data. [p. 2]
- The AWL paper formalizes four natural-language requirements: initial path
  computation, obstacle avoidance, mode switch on error, and an end-to-end
  deadline. [p. 3]
- The AWL model has 12 timed automata, 61 C functions, 23 clocks, 49 global
  variables, and 4 data structures. [p. 6–7]
- The authors built the AWL timed automata by hand from UML activity diagrams
  with a one-to-one mapping. [p. 5–6]
- The AWL map is an integer grid, and the AWL moves only along cell edges or
  diagonals. [p. 5]
- The AWL model uses integer arithmetic for the dipole field forces, because
  classic UPPAAL supports only integers. [p. 9]
- All 16 AWL queries pass. The largest query, the end-to-end deadline Q4.0,
  explores 590,326 states in 36,641 ms. [p. 8]
- With a dynamic obstacle on a preset path, the AWL never collides with it
  (query Q2.0). [p. 8]
- With injected faults, the AWL enters safety mode within 20 time units for
  error A and 15 time units for error B. [p. 8]
- The fastest AWL round trip in a witness trace is 1620 ms, against a
  deadline of 2200. [p. 9]
- When the obstacle moves freely instead of on a preset path, UPPAAL finds an
  AWL collision and a livelock. [p. 9]
- The conclusion claims that the TCTL queries "completely express" the
  natural-language requirements from industry. [p. 10]

## Questions this paper answers

**What did the authors verify?** A design-level abstract model of the AWL
control system, its environment, and its planning and avoidance algorithms.
They did not verify the implementation code.

**Which tool and logic did they use?** UPPAAL with timed automata for the
model and TCTL queries for the properties.

**How did they put algorithms into a timed-automata model?** They wrote A*
and the dipole flow field algorithm as C functions in UPPAAL declarations.
The automata call these functions on their edges.

**How did they get from design documents to a formal model?** They mapped
each activity-diagram element to timed-automaton elements by hand, with four
mapping rules (see "Diagram-to-automata mapping").

**How did they check error handling?** They injected two faults through
Boolean variables and checked a bounded reaction time with "leads to"
queries.

**Did they find problems?** Yes. A freely moving obstacle causes a
collision, a livelock, or an obstacle that pushes the AWL to the map edge.

**How large was the verification effort?** The largest query took about 37
seconds and 590,326 states. The paper does not state the hardware.

## Scope: what this paper does not do

- It does not verify source code or a binary. The model is an abstraction.
- It does not prove that the diagram-to-automata mapping is correct. The
  authors list that as future work. [p. 10]
- It does not model vehicle dynamics or Newton's law of motion. [p. 9]
- It does not model the obstacle-recognition algorithm. The model reads
  occupied grid points within 3 cells of the AWL. [p. 5]
- It does not use probabilities. UPPAAL SMC is discussed only as a possible
  next step. [p. 9]
- It does not cover digging or unloading. [p. 2]
- It gives no independent check that the 16 queries match the intent of the
  four requirements.
- It names no DOI and no venue inside the PDF.

## System under verification

| Unit | Role | Tasks |
|---|---|---|
| Vision unit | Detects obstacles with LIDAR and camera | Do Obstacle Task |
| Control unit | Plans the path, schedules tasks, sends commands | Read Position Task, Main Task, Calculate Path Task |
| Execution unit | Controls steering and brakes; reads GPS and IMU | Receive Command Task, Do Command Task, Calculate Position Task |

Main Task takes a path segment from Path Stack 1 and checks it with the Valid
Path Function. If the segment is not safe, Calculate Path Task runs the
dipole flow field algorithm. If no safe segment exists, it sends a brake
command. [p. 2–3]

## Requirements in natural language

These are the four AWL requirements as the paper states them. [p. 3]

1. **Initial path computation.** During initialization, the AWL must compute
   an initial path to the destination that avoids all static obstacles.
2. **Obstacle avoidance and path recalculation.** The AWL must avoid static
   and dynamic objects "in due time" before it returns to the initial path.
3. **Mode switch.** After a critical error, the AWL must switch to safety
   mode and freeze all motion within an error-specific time limit.
4. **End-to-end deadline.** The AWL must reach the destination within 2200
   milliseconds.

## Modelling abstractions

- **Map.** A 2D grid with resolution ε. Each grid point holds 0 (empty) or 1
  (occupied). Coordinates go from 0 to `N = 15`. A dynamic obstacle
  occupies one point, and a static obstacle can occupy many points. [p. 5]
- **Movement.** Speed goes from 0 to a maximum of 2. One time unit is the
  execution period of Main Task. [p. 5]
- **Dynamic obstacle.** One timed automaton with a self-loop edge. A function
  on that edge moves the obstacle along a preset path. [p. 5]
- **Forces.** The next position comes from the sign of the summed forces on
  each axis against an integer threshold T. [p. 9]
- **Task timing.** Extra locations and invariants model task periods and
  start order. Main Task waits until `taskDelay = 7`, so that obstacle and
  position tasks run first. [p. 6]
- **Time-outs.** Get Path Function waits for position data under an
  invariant. If the data does not come in time, it goes back to `Start`.
  [p. 6–7]

## Diagram-to-automata mapping

The authors used these four rules to build each automaton from its activity
diagram. [p. 5–6]

1. An action node becomes a function and its locations and edges, in the
   same order as in the diagram.
2. A decision node becomes a location with several guarded outgoing edges.
3. An action node that calls another function becomes a channel
   synchronization between two automata.
4. A* and the dipole field algorithm become C functions inside the automata.

## Verification results

Map 1 has one static obstacle of 10 grid points, with the pile at (1,1) and
the crusher at (14,6). Map 2 adds one dynamic obstacle that starts at (9,8),
follows a preset path, and does not try to avoid the AWL. [p. 7–8]

| Requirement | Query | Result | States | Time |
|---|---|---|---|---|
| Initial path (map 1) | Q1.0 `E<> mainTask.Wait` | Pass | 2 | 110 ms |
| | Q1.1 `A<> mainTask.Wait imply lenOfPathStack > 0` | Pass | 8,780 | 484 ms |
| | Q1.2 `E<> currentPosition == pile and destination == crusher` | Pass | 1 | 0 ms |
| | Q1.3 `(currentPosition == pile and destination == crusher) --> currentPosition == crusher` | Pass | 14,191 | 1,125 ms |
| | Q1.4 `E<> currentPosition == crusher and destination == pile` | Pass | 2,339 | 297 ms |
| | Q1.5 `(currentPosition == crusher and destination == pile) --> currentPosition == pile` | Pass | 14,204 | 782 ms |
| | Q1.6 `A[] forall(i:int[0,9]) currentPosition != staticObstacle[i]` | Pass | 8,780 | 485 ms |
| Obstacle avoidance (map 2) | Q2.0 `A[] currentPosition != currentObstacle` | Pass | 125,941 | 6,297 ms |
| | Q1.3 on map 2 | Pass | 227,646 | 13,969 ms |
| | Q1.4 on map 2 | Pass | 2,678 | 375 ms |
| | Q1.5 on map 2 | Pass | 192,406 | 10,656 ms |
| Mode switch, error A | Q3.1 `E<> errorStart == true` | Pass | 30 | 234 ms |
| | Q3.2 `error_start==true --> (SYSTEM_ERROR==true and reaction_time<=20)` | Pass | 91 | 250 ms |
| Mode switch, error B | Q3.1 `E<> errorStart == true` | Pass | 29 | 234 ms |
| | Q3.2 `error_start==true --> (SYSTEM_ERROR==true and reaction_time<=15)` | Pass | 320 | 266 ms |
| End-to-end deadline | Q4.0 `(currentPosition==pile and destination==crusher) --> (currentPosition==pile and destination==pile and gClock <= 2200)` | Pass | 590,326 | 36,641 ms |

Source: Table 1 of the paper. [p. 8]

How the queries work:

- A "leads to" query `p --> q` is true when `p` is never reached. The authors
  therefore check each antecedent with a reachability query first, for
  example Q1.2 before Q1.3. [p. 8]
- Error A sets `do_obstacle_heartbeat` to false, so obstacle data does not
  reach the control unit. Error B sets `position_udp` to false, so position
  data is lost on Ethernet. [p. 8]
- Without injected faults, `A[] !SYSTEM_ERROR` holds. [p. 8]
- Reachability queries such as `E<> currentPosition == pile and destination
  == pile` produce witness traces. The trajectory figures of the paper come
  from these traces. [p. 8]

## Problems found by model checking

With a freely moving obstacle, UPPAAL produced these AWL scenarios. [p. 9]

- **Collision.** The AWL collides with the dynamic obstacle.
- **Livelock.** The AWL and the obstacle move back and forth on the same
  axis. No force on the other axis turns the AWL, so it never reaches the
  destination.
- **Pushed to the edge.** The obstacle keeps pushing the AWL until both stop
  at the edge of the map.

The authors propose to change the dipole field implementation so that the
AWL turns and passes behind the obstacle.

## Limitations stated by the authors

- On the grid, the A* shortest path is not the continuous shortest path.
  Any-angle planners such as Theta* fix this but need real numbers. [p. 9]
- Classic UPPAAL has only integers, so the algorithms are simplified. UPPAAL
  SMC supports floating point and stochastic behavior, but it gives
  probabilities, not exhaustive results. [p. 9]
- The model is a design-level abstraction of the actual system. [p. 10]

## Future work stated by the authors

- Prove the transformation from activity diagrams to UPPAAL automata
  correct, and automate it. [p. 10]
- Model the dynamics of the AWL. [p. 10]
- Add probabilistic events to get closer to the real system. [p. 10]

## Related work, as the paper positions itself

Earlier work cited by the paper uses mCRL2 and the modal µ-calculus, LTL
with Büchi automata, hybrid automata with SMV, timed automata for
multi-robot planning, and Z with theorem proving for A*. The paper claims a
more detailed model than those works. The model has the control tasks and
their communication, the planning and avoidance algorithms, and
acceleration. It also checks timed safety properties, such as a bounded
reaction to an error. [p. 9–10]

## Reviewer notes on requirement fidelity

These notes are a reading of the paper, not claims from it.

- The paper gives no separate check of its claim that the 16 queries
  "completely express" the four requirements.
- Requirement 2 says "in due time", but no query has a time bound for
  avoidance. Q2.0 checks only that the AWL never shares a grid point with
  the obstacle.
- The deadline is "2200 milliseconds" on p. 3 and "2200 time units" on p. 8.
  One time unit is defined as the Main Task period, so the two units are
  not obviously equal.
- The text says Q1.2 to Q1.4 are checked again on map 2, but Table 1 lists
  Q1.3 to Q1.5. [p. 8]
- Each pass holds only under the stated assumptions: the grid, the integer
  forces, and the preset obstacle path. A free-moving obstacle broke the
  safety and the liveness properties.

## Terms

| Term | Meaning in this paper |
|---|---|
| AWL | Autonomous wheel loader, the machine under verification |
| Timed automata (TA) | State machines with real-valued clocks, guards, and invariants |
| TCTL | Timed Computation Tree Logic, the query language of UPPAAL |
| `A[] p` | Invariance: `p` holds in every state of every path |
| `E<> p` | Reachability: some path reaches a state where `p` holds |
| `p --> q` | Leads to: whenever `p` holds, `q` holds later on every path |
| Dipole flow field | A collision-avoidance method. Static forces pull the vehicle to its goal and push it from static obstacles. Dipole forces push it from moving obstacles. |
| A* | A heuristic shortest-path search on a graph |
| Witness trace | An example run that UPPAAL returns for a satisfied reachability query |

## Citation

Rong Gu, Raluca Marinescu, Cristina Seceleanu, and Kristina Lundqvist.
"Formal Verification of an Autonomous Wheel Loader by Model Checking."
FormaliSE'18, 2018.
