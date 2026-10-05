---
id: gu2024tosem-mission-plans-complex-road-conditions
title: "Synthesis and Verification of Mission Plans for Multiple Autonomous Agents under Complex Road Conditions"
authors:
  - Rong Gu
  - Eduard Baranov
  - Afshin Ameri
  - Cristina Seceleanu
  - Eduard Paul Enoiu
  - Baran Cürüklü
  - Axel Legay
  - Kristina Lundqvist
affiliation: Mälardalen University, Sweden; UCLouvain, Belgium
year: 2024
venue: ACM Transactions on Software Engineering and Methodology (TOSEM)
venue_source: author's publications page (the PDF does not name the journal; every page carries the footer "Manuscript submitted to ACM")
doi: null
document_type: journal article
pdf_version: submitted manuscript (footer "Manuscript submitted to ACM" on every page; p. 1)
pages_in_pdf: 43
pdf_url: https://drive.google.com/file/d/1h0v2i3mmcU8RSsTHyBc1DnSw2IrCF_xZ/view?usp=drive_link
listing_url: https://sites.google.com/view/ronggu/publications
code_url: https://github.com/rgu01/MALTA
author_keywords: [mission-plan synthesis, autonomous agents, path planning, task scheduling, UPPAAL]
topics: [mission planning, plan synthesis, model checking, path planning, task scheduling, multi-agent systems, autonomous vehicles, construction machinery, temporary obstacles, requirement formalization, scalability, replanning]
formalisms: [timed automata, TCTL]
tools: [UPPAAL, MALTA, TAMAA, MMT, j2uppaal, Apache Thrift]
algorithms: [DALi, DALi*, A*, Dijkstra]
application: autonomous trucks in a quarry
abbreviations: {MALTA: the mission-planning toolset of this paper, TAMAA: Timed-Automata-based Mission planner for Autonomous Agents, DALi: Devices for Assisted Living path planner, MMT: Mission Management Tool, TA: timed automata, UTA: UPPAAL timed automata, TCTL: Timed Computation Tree Logic, BCET: best case execution time, WCET: worst case execution time, MCRL: model checking plus reinforcement learning, SAS: self-adaptive systems, GUI: graphical user interface}
funding: Swedish Knowledge Foundation (DPAC grant 20150022; ACICS grant 20190038); Walloon Region, Belgium (DeepConstruct, convention 8560)
---

# Synthesis and Verification of Mission Plans for Multiple Autonomous Agents under Complex Road Conditions (Gu et al., TOSEM 2024)

## At a glance

This 2024 article by Gu, Baranov, Ameri, Seceleanu, Enoiu, Cürüklü, Legay, and
Lundqvist builds a mission plan for several autonomous agents in two
parts. A path planner (DALi) finds paths between milestones. A task
scheduler (TAMAA) asks the UPPAAL model checker for the fastest run of a
timed-automata model that meets the task requirements. The two parts run in
a loop until no path crosses a temporary obstacle while it is active. The
authors implement the method in the tool MALTA. They test it on an
autonomous-quarry case. Path planning stays fast. Task scheduling does not
scale with the number of agents.

Page references `[p. N]` point to the 43-page PDF.

## Key facts

Each fact is a claim from the paper unless it is marked otherwise.

- The MALTA paper proposes a tool-supported method that combines path
  planning with task scheduling for multiple autonomous agents. [p. 1]
- The MALTA method adapts the DALi path planner for environments with
  temporary obstacles, heat areas, and soft constraints. [p. 3, p. 11]
- The MALTA method adapts TAMAA for task scheduling. TAMAA generates timed
  automata and gets a schedule from a UPPAAL witness trace. [p. 3, p. 14]
- The authors state that no earlier framework solves these problems
  together, in academia or in industry. [p. 3]
- The MALTA mission-planning loop runs DALi and TAMAA again and again until
  no scheduled travel crosses a temporary obstacle while it is active.
  [p. 10, p. 19–20]
- The first path computation in MALTA ignores temporary obstacles, because
  the start times of the travels are not yet known. [p. 13, p. 19]
- The authors add two speed-ups to DALi: a single-source multiple-target
  version, and DALi*, which uses the A* distance estimate. [p. 12–13]
- The two DALi speed-ups cannot be combined. The A* estimate needs one
  target. [p. 13]
- The TAMAA model of one agent has two timed automata: one for movement and
  one for task execution. [p. 14]
- The TAMAA model assumes that the agents control the task durations inside
  the interval from BCET to WCET (a 1-player game). [p. 16, p. 18]
- The MALTA scheduling query is a reachability query: all tasks finish
  `ALL` rounds within `LIMIT` time units. [p. 18]
- The authors call the resulting plan "correct-by-construction", because
  the model checker explores the whole state space. [p. 20]
- When new tasks appear, MALTA encodes the old plan as a constant array in
  the new model. Synthesis takes 44.5 s instead of 623 s, which is 14 times
  faster. [p. 20–21, p. 34]
- The MALTA source code and the experiment configurations are public at
  github.com/rgu01/MALTA. [p. 21, p. 25]
- MALTA has a client-server design with a GUI (MMT), a middleware for path
  planning and model generation, and a back end for scheduling. [p. 4, p. 22]
- In the experiments, DALi* is within 10% of A* run time in 98% of the
  parameter combinations. [p. 29]
- A graph with 400,000 nodes needs less than 1 minute for DALi* or A*
  planning. [p. 30]
- With a 1-hour timeout, MALTA times out for 3 agents with 5 milestones and
  for 4 agents with 3 milestones. [p. 27, p. 32]
- The authors conclude that MALTA does not scale with the number of agents,
  because of state-space explosion. [p. 32]
- In an adapted quarry case with 3 trucks and 90 tons of stone, the fastest
  plan takes 6.9 minutes. [p. 37]
- The authors state that safety has the highest priority and that high-level
  mission planning runs rarely, for example once per day. [p. 38]
- The authors state that the correctness guarantee is lacking in AI-based
  mission-planning algorithms. [p. 38]

## Questions this paper answers

**What problem does the paper solve?** It synthesizes a mission plan for
several agents. The plan holds a task schedule and a path for each travel
between milestones. [p. 5–7]

**Which tools and logic did they use?** UPPAAL with timed automata for the
model and TCTL queries for the requirements. The DALi path planner is
separate from UPPAAL. [p. 7–9, p. 10]

**How do path planning and task scheduling work together?** The planner gives
travel times to the scheduler. The scheduler gives start times to the
planner. They repeat until no path crosses an active temporary obstacle.
[p. 10, p. 19–20]

**How do natural-language requirements become queries?** Three requirement
categories (milestone matching, task sequence, and timing) become four
query templates, Queries (7) to (10). The tool generates the queries and the
user may edit them.
[p. 5, p. 14, p. 17–18]

**What happens when new tasks appear after planning?** MALTA reuses the old
plan and schedules only the new tasks. [p. 20–21]

**How do they adapt MALTA to a different quarry?** They edit the generated
models and queries by hand. They add a monitor automaton for one property
that UPPAAL cannot express. [p. 34–36]

**How well does it scale?** Path planning grows linearly with agents.
Task scheduling grows exponentially with agents. The tool times out at 3
agents with 5 milestones. [p. 32, p. 38]

**Where is the code?** github.com/rgu01/MALTA. [p. 21]

## Scope: what this paper does not do

- It does not check collisions between agents, and it does not handle moving
  obstacles. Path following and dynamic collision avoidance are outside the
  scope. [p. 6]
- It treats all obstacles as static. A temporary obstacle appears at a known
  time and disappears at a known time. [p. 5]
- It does not verify the DALi path planner. DALi is separate code outside
  UPPAAL. [p. 10]
- It does not handle an uncooperative environment, where the environment
  chooses against the agents. The authors refer to another article for it.
  [p. 18, p. 41]
- It does not handle unplanned changes of a self-adaptive system. The authors
  call adaptation to a dynamic environment out of scope. [p. 39]
- It does not include probabilities. [p. 40]
- It does not integrate machine learning into the evaluated method. The
  experiments use TAMAA only. [p. 26–32, p. 41]
- It prints no DOI, no volume, no article number, and no received or accepted
  date. The ACM reference line on p. 1 holds a placeholder DOI. [p. 1]
- It has no large language models.

## Problem definition

A mission-planning problem is a tuple of six parts. [p. 6]

| Part | Meaning |
|---|---|
| ℰ | A confined environment in 2 or 3 dimensions |
| Ab | Areas of environmental abnormality I, II, or III |
| ℳ | A set of milestones, the places where tasks run |
| 𝒯 | A set of tasks |
| f | An assignment of each task to one or more milestones |
| Req | Task requirements of category I, II, or III |

A solution is a pair `plan = <schedule, path>`. The schedule is a set of
start and finish times for the actions of an agent. The path is a set of
point sequences that lead to the milestones. A plan must satisfy all
environment constraints in E1, E2, and E3′. It must also satisfy all
requirements in Req. [p. 6–7]

E3′ is the part of the soft constraints that does not contradict E1 and E2.
When productivity has a higher priority, a plan may ignore a soft
constraint, so that E3′ is empty. [p. 7]

## Case study and requirements

The case study is an autonomous quarry from Volvo Construction Equipment in
Sweden. Crushers turn stones into set sizes. Wheel loaders dig stones.
Autonomous trucks carry stones to the crushers. The crushers are stationary
and manually controlled. [p. 4]

An example mission is to dig, crush, and transport 1000 m³ of stones in 24
hours. [p. 5]

**Task requirement categories** [p. 5]

- **Category I, milestone matching.** A task runs at the correct milestone.
- **Category II, task sequence.** Tasks run in the right order.
- **Category III, timing.** Tasks finish within a time frame, so that the
  productivity stays at a set level.

**Environmental abnormalities** [p. 5–6]

- **I, obstacles.** Permanent obstacles are always present. Temporary
  obstacles appear at known times and disappear later.
- **II, road conditions.** A muddy or bumpy road slows the vehicle. The
  planner decides between a detour and a slow passage.
- **III, soft constraints.** The planner avoids an undesirable area when an
  alternative path exists. It may ignore the constraint if it blocks a
  critical requirement, such as safety.

## Method

### Overall workflow

The workflow has six steps. [p. 10]

1. The mission planner reads the map, the abnormalities, the tasks, and the
   task constraints.
2. The path planner computes potential paths between every pair of
   milestones.
3. TAMAA builds UPPAAL models. UPPAAL returns execution traces that meet the
   task constraints. TAMAA turns a trace into a schedule.
4. The path planner checks if a scheduled travel crosses a temporary
   obstacle while it is active. If so, the flow returns to step 2 for the
   affected paths.
5. If the task and path constraints hold, the loop ends and returns the plan.
6. Optional: when new tasks or milestones appear, repeat steps 2 to 5. Path
   planning covers only paths to the new milestones. TAMAA builds a model
   that contains the existing plan.

The authors state that it is possible but not practical to use UPPAAL for
both parts, because of scalability. [p. 10]

### DALi path planning

DALi has a long-term planner and a short-term planner. This paper uses only
the long-term planner. It is based on Dijkstra's shortest-path algorithm.
[p. 9]

The authors turn the area into a Cartesian grid. Each cell is a graph node.
Neighbor cells connect by edges with the distance between cell centers.
[p. 11]

| Constraint | Encoding in the graph | Page |
|---|---|---|
| Permanent obstacle | Cells are not in the graph | p. 11 |
| Temporary obstacle | Cells stay in the graph with their inaccessible time periods | p. 11 |
| Heat area (bad road) | Edges hold a speed-reduction factor | p. 11 |
| Soft constraint (undesirable area) | A uniform virtual coefficient on the edge length. It does not change the real travel time. | p. 11 |

The original DALi uses a coefficient that falls with the distance from the
area center. The authors use one uniform coefficient. [p. 11]

Algorithm 1 (`FindPath`) takes a source, a target, a speed, and a start
time. The distance update multiplies the edge length by the soft-constraint
coefficient and divides it by `1 − heat`. A function
`IsInsideTemporaryObstacle` rejects an edge when the arrival time lies in
the inaccessible period. [p. 12]

**Two speed-ups** [p. 12–13]

- **Single-source multiple-target.** The loop continues until the distances
  to all milestones are known. This reduces the number of calls.
- **DALi*.** Each node stores the distance to the source plus the Euclidean
  distance to the target. The queue sorts by that estimate.

The two speed-ups are incompatible. The choice depends on the number of
milestones and the grid size. [p. 13]

**Use of the planner in the loop** [p. 13]

- Step 2 ignores temporary obstacles. The first paths may cross them.
- Step 4 recomputes the paths that cross an active temporary obstacle.
- If a detour for a soft constraint makes the mission too long, the planner
  recomputes the paths without soft constraints. TAMAA then reschedules.

### TAMAA task scheduling

TAMAA runs four steps: generate the UTA models, generate the TCTL queries,
run UPPAAL to get a trace, and parse the trace into a schedule. The user can
edit the models and the queries. [p. 14]

**Movement automaton** (Definition 4). Locations are the milestones and the
travels between them. The travel time sits in an invariant `x_m ≤ δ` and a
guard `x_m ≥ δ`. A Boolean array `position` records where the agent is.
[p. 14–15]

**Task** (Definition 5). A task has BCET, WCET, `isStarted`, `isFinished`, a
set of update functions, a precondition `pre`, and a set of allowed
milestones `Mil`. [p. 15–16]

| Task | BCET (min) | WCET (min) | Precondition | Milestone |
|---|---|---|---|---|
| Loading | 5 | 10 | none | B |
| Unloading | 8 | 14 | Loading.isFinished | C |

Source: Table 1 of the paper. [p. 16]

**Task-execution automaton** (Definition 6). It has an idle location and one
location per task. A self-loop on the idle location synchronizes with the
movement automaton on the channel `move`. An agent cannot move while it
executes a task. A guard `!tf[i]` forbids a second run of a task in one
iteration. A function `isBusy` forbids two agents on the same task.
[p. 16–17]

**Requirement queries** [p. 17–18]

| Category | Query | Meaning |
|---|---|---|
| Milestone matching | (7) `E<> ts_a[i]` | Task `Ti` ever starts |
| | (8) `A[] task_a.Ti imply (move_a.Pi \|\| ... \|\| move_a.Pk)` | Task `Ti` runs only at an allowed milestone |
| Task sequence | (9) `A[] ts_a[i] imply tf_a[j]` | Task `Ti` never starts before task `Tj` finishes |
| Timing | (10) `E<> iteration[a]>=ALL and gClock <= LIMIT` | All tasks finish `ALL` rounds within `LIMIT` |

The authors state that the construction of the automata guarantees Queries
(7) to (9). The user can still check them, but mission planning does not use
them. Only Query (10) drives synthesis. TAMAA always looks for the fastest
trace. [p. 18]

### Mission-planning algorithm (Algorithm 2)

1. Discretize the environment into a grid.
2. Compute a path for each pair of milestones and each agent, ignoring
   temporary obstacles and using soft constraints.
3. Generate the movement and task-execution automata and compose them.
4. Call UPPAAL with Query (10) and parse the trace.
5. If no schedule exists and soft constraints exist, recompute without soft
   constraints. If no schedule exists without them, return false.
6. If a scheduled travel crosses an active temporary obstacle, update the
   start times, recompute the affected paths, and go to step 3.
7. Split the schedule into one plan per agent.

[p. 19–20]

An empty schedule means that no plan exists. The authors state that this is
guaranteed, because UPPAAL explores the whole state space. [p. 20]

### Adaptability

A new task or milestone does not need a full recomputation. MALTA encodes
the old plan as a constant array of pairs of an agent state (`PState`) and an
action (`PAction`). Guards on the start of each action force the automata to
follow the old plan. The guards do not apply at the milestone of a new task.
The fastest trace of Query (10) then merges the new tasks into the old plan.
[p. 20–21]

## The MALTA tool

- **Front end.** MMT, a GUI where the operator defines the navigation area,
  special areas, tasks, vehicles, and home locations. It shows the plan on a
  map and as a Gantt chart. [p. 23–25]
- **Middleware.** Path planning (A* or DALi), UTA model generation with the
  library j2uppaal, and the Mission Plan Validator. [p. 22]
- **Back end.** The TAMAA scheduler. It calls UPPAAL and parses traces with
  the UPPAAL parsing library. It stores the schedule as XML. [p. 22]
- **Communication.** MMT and the planner exchange data through Apache Thrift.
  [p. 23]
- **Area types in MMT.** Forbidden, preferred, less preferred, and heat
  areas, with an intensity and a start and end time. [p. 24]
- **Task types in MMT.** Inspect tasks run at a location. Survey tasks run on
  an area. [p. 24]

The client-server split lets the user move expensive computation to a
dedicated server. [p. 21]

## Evaluation setup

**Research questions** [p. 26]

- **RQ1.** Can DALi or an optimization replace A* without a significant loss
  of performance?
- **RQ2.** Does MALTA scale with the number of tasks and road abnormalities?
- **RQ3.** How do heat areas and temporary obstacles affect performance?
- **RQ4.** Does MALTA scale with the number of agents?

**Setup** [p. 26–27]

- The mission comes from the MMT example. The area is about 1.5 square
  kilometers.
- Parameters: path-planning algorithm, granularity (cell size in meters),
  number of milestones, permanent obstacles, temporary obstacles, heat
  areas, and agents.
- Defaults: 1 agent, 10 milestones, 10 obstacles, 0 heat areas, and
  granularity 4.
- A* ignores heat areas and treats temporary obstacles as permanent.
- Hardware: Intel i5 CPU, 16 GB RAM, Windows 10. The back end runs in an
  Oracle VirtualBox 7.0 virtual machine with Ubuntu 20.04 LTS on the same PC.
- The timeout is 1 hour.
- Statistics: Welch's t-test with significance level 0.05.

| Group | Setting | Algorithms | Runs per combination |
|---|---|---|---|
| Preliminary | 1 agent, granularity 3–10, 1–10 tasks | DALi variants | 5 |
| 1 | 1 agent, no heat areas, temporary obstacles as permanent; 1–10 tasks and obstacles, granularity 3–10 (plus 1.5, 2, 2.5 with 10 obstacles) | A*, DALi, DALi* | 50 |
| 2 | 1 agent, all obstacle types, heat areas, varied tasks and granularity | DALi, DALi* | 50 |
| 3 | Several agents, granularity 4, 10 permanent obstacles, no temporary obstacles | A*, DALi* | 5 |

The paper states that groups 1 and 2 use 50 runs, and groups 3 and the
preliminary test use 5 runs. [p. 27]

## Results

All values come from the text. The figures hold the full curves.

| Result | Value | Page |
|---|---|---|
| Preliminary: DALi* against the single-source multiple-target version | The slowest DALi* run is faster than every run of DALi or the other version | p. 27 |
| Graph construction time at granularity 2.5, 2, 1.5 | 1.6 s, 3 s, 5.8 s | p. 28 |
| DALi path-planning time at granularity 1.5 and 2 | 1003 s and 418 s on average | p. 28 |
| A* against DALi* | No significant difference in 37% of combinations. A* is faster in the rest. | p. 29 |
| DALi* run time against A* | Less than 10% higher in 98% of combinations | p. 29 |
| Effect of more obstacles | Significant in 81% of combinations. Mean path-planning time falls 18% from 1 to 10 obstacles. | p. 29 |
| TAMAA time, 1 agent | Within 0.3 s, except for fewer than 1% outliers | p. 29 |
| Graph with 400,000 nodes (granularity 2) | A* and DALi* finish in under 1 minute in total | p. 29–30 |
| Extra graph time for temporary obstacles | 4 ms at granularity 10, up to 68 ms at granularity 3 | p. 30 |
| Extra graph time for 5 heat areas against 0 | 0.3 s on average at granularity 3 | p. 30 |
| Recompute with temporary obstacles, granularity 4 | DALi needs several seconds. DALi* needs under 1 second. | p. 30 |
| Mean time increase per call, 1 milestone, granularity 3 | Up to 0.1 s for DALi* and 0.2 s for DALi | p. 31 |
| Mean time increase per call, 10 milestones | Below 0.01 s for DALi* and 0.05 s for DALi | p. 31 |
| Heat areas | Significant in only 30% of the compared pairs | p. 31 |
| TAMAA time with temporary obstacles | No significant change in 76% of combinations. The rest differ by at most 0.07 s. | p. 31 |
| Multi-agent path planning | No significant difference between agent counts, on 5 runs | p. 32 |
| Multi-agent scheduling | Time out for 3 agents with 5 milestones and 4 agents with 3 milestones | p. 32 |

**Answers to the research questions**

- **RQ1.** DALi is much slower than A*. DALi* is much faster than DALi and
  stays within 10% of A* on almost all combinations. [p. 29]
- **RQ2.** Granularity matters most, because the graph size grows with its
  inverse square. MALTA stays below 1 minute at 400,000 nodes. [p. 30]
- **RQ3.** The extra constraints add recomputation. The impact is low. [p. 31]
- **RQ4.** MALTA does not scale with the number of agents, because of
  state-space explosion. [p. 32]

Group 3 ignores the case where two agents cross paths. It assumes that the
shortest path between two milestones is the same for every agent. All agents
start from the same point, so MALTA reuses all paths. [p. 31–32]

## Special industrial cases (Section 7)

The base MALTA model does not cover these cases, so the authors change the
models and queries. The cases use the machine data in Table 2. [p. 32–33]

| Machine | Speed | Rate | Capacity |
|---|---|---|---|
| Autonomous truck | 35 km/h | 1.5 tons/s | 15 tons |
| Wheel loader | none | 1.5 tons/s | none |
| Primary crusher | none | 0.25 tons/s | none |
| Charging station | none | 30 s per charge | none |

Source: Table 2 of the paper. [p. 33]

The mission goal is to move 90 tons of stone as fast as possible. A truck
fills in 60 s at the primary crusher and in 10 s at the wheel loader. The
paper assigns the distances in the quarry itself, because the use cases give
none. It picks them so that the trucks do not drain their batteries. [p. 33]

### Case i: additional tasks

Two agents have three existing tasks. Four more tasks appear after the plan
exists. Each new task has a new milestone and a random preceding task.
[p. 33]

| Method | Synthesis time |
|---|---|
| New plan built on the existing plan | 44.5 s |
| Recompute from the beginning | 623 s (14 times more) |

Source: text of Section 7.1.1. [p. 34]

### Case ii: special topology and tasks

The quarry has 3 identical trucks, a primary crusher, a secondary crusher, a
wheel loader, and two charging stations in the center. [p. 34]

The authors change the movement automaton to force the new topology. A
truck must charge every time it passes a charging station. A guard
`PCQueue > 2` on the edge to the wheel-loader task makes a truck prefer the
primary crusher. [p. 34–35]

| Query | Property | Page |
|---|---|---|
| (11) `E<> stone == 0` | All stone reaches the secondary crusher. Replaces Query (10). | p. 35 |
| (12) `A[] PCQueue < 2 imply !(task0.T2_2 \|\| ... \|\| taskn.T2_2)` | A truck loads at the wheel loader only when the crusher queue is full | p. 35 |
| (13) `A[] !monitor0.Error && ... && !monitorn.Error` | A truck always charges right after it arrives at a charging station | p. 36 |
| (14) `A[] forall(i:int[0,N]) battery[i]>0` | No battery runs empty | p. 36 |

UPPAAL cannot express "always next" in its TCTL subset. The authors add a
monitor automaton that moves to an `Error` location when a truck does
anything but charge after it arrives. Query (13) then checks that `Error` is
never reached. [p. 36]

The battery model subtracts `k × t` for each time `t` of movement or task
execution. The paper does not give the value of `k`. [p. 36]

**Result.** The fastest time to move the 90 tons is 6.9 minutes. The authors
state that showing the plan in MMT demonstrates that Queries (12) to (14)
hold. [p. 37]

## Limitations stated by the authors

- Task scheduling uses a composed model of all agents, so its time grows
  exponentially with the number of agents. [p. 38]
- Path-planning time grows linearly with agents, because agents plan
  separately. [p. 38]
- MALTA does not scale with the number of agents. [p. 32]
- The model is a 1-player game. The method assumes a collaborative
  environment. [p. 18, p. 41]
- Run times vary with other processes. The authors repeat runs and use
  Welch's t-test. The relative standard deviation is below 0.1 for 90% of the
  measurements. [p. 38]
- Group 3 uses only 5 runs. The authors argue that the growth in time is
  larger than the noise. [p. 38]
- MALTA suits high-level missions that run rarely. [p. 38]
- MALTA plans for known factors, such as obstacle positions and task order.
  Adaptation to a dynamic environment is out of scope. [p. 39]
- Learning methods such as MCRL scale better with agents. Search-based
  methods such as TAMAA are better with few agents and a goal deep in the
  state space. [p. 39]

## Future work stated by the authors

- Support more path-planning and task-scheduling algorithms, for more agents
  or larger environments. [p. 41]
- Integrate the toolset with machine learning techniques. [p. 41]
- Adapt the method to environments with competitive agents. [p. 41]

## Related work, as the paper positions itself

The paper names four groups. [p. 39–41]

- **Path and task planning.** Sampling-based planners (RRT, probabilistic
  roadmaps) and graph search (A*, Theta*). These do not guarantee
  correctness without formal verification. Task and motion planning methods
  often assume downward refinement. MALTA starts from collision-free paths
  instead, so its task plans are collision-free by construction. [p. 39–40]
- **Temporal logic.** Work with LTL. MALTA uses TCTL, which expresses timed
  requirements such as 1000 m³ per 24 hours. MALTA also integrates path
  planning and task scheduling. A model-checking motion-planning study
  models by hand and has no timing requirement. [p. 40]
- **Formal methods.** Tools such as Kronos, LTSmin, and SpaceEx. Controller
  synthesis from LTL and from metric interval temporal logic. The paper
  places itself in the 1-player game class. Stochastic and 2-player
  formulations are out of scope. [p. 40]
- **Mission GUIs.** Operator interfaces for UAV, AUV, and delivery missions.
  Many serve one use case. MMT can talk to different planners. [p. 40–41]

## Relation to other papers in this folder

- **2020-sac-tamaa-mission-planning.md.** The SAC 2020 paper introduces TAMAA.
  This paper cites it as [GES19]. [p. 3, p. 42] This paper states that the
  new TAMAA version works with DALi and temporary obstacles. The earlier
  version used the path-planning result once, with permanent obstacles only.
  [p. 3]
- **2022-sttt-verifiable-strategy-synthesis.md.** This paper cites the STTT
  2022 article as [GJP+22] for the uncooperative environment and for MCRL.
  [p. 18, p. 38–39, p. 42]
- **2022-phd-thesis-scalable-synthesis-verification.md.** The thesis holds a
  submitted version of this paper as Paper C. See the reviewer notes below
  for the differences.

## Reviewer notes on requirement fidelity

These notes are a reading of the paper, not claims from it.

**What the verification proves**

- UPPAAL checks a model of movement and task automata. The travel times in
  that model come from DALi. The model checker does not check the paths.
  The paper calls the whole plan "correct-by-construction". [p. 19–20]
  For the path part, this rests on the correctness of DALi, which the paper
  does not verify.
- Only Query (10) drives synthesis. It is a reachability query. It shows
  that one plan exists. Queries (7) to (9) hold by construction. [p. 18]
- The model lets the agent choose each task duration inside the interval
  from BCET to WCET. [p. 16, p. 18] A real task may take other times.
  A fixed schedule may then fail. The paper moves this case to another
  article. [p. 18]
- The path planner is a fast grid search with checks in a separate module.
  The Mission Plan Validator checks only for crossings of active temporary
  obstacles. [p. 20, p. 22]
- The grid hides the shape of obstacle boundaries. The paper says that a
  finer grid gives a more accurate boundary. It does not say how a partly
  covered cell is treated. [p. 29]
- The multi-agent runs ignore crossings between agent paths, and collision
  among agents is outside the scope. [p. 6, p. 31] The multi-agent plans
  therefore do not show safety between agents.

**"Optimal" and "guaranteed" claims**

- The paper says that the plan is guaranteed to be optimal. [p. 41] It also
  says that the traveling time is the shortest if users select the fastest
  trace. [p. 38]
- The scheduler gets one fixed path per pair of milestones. UPPAAL does not
  choose between paths. The schedule is the fastest for those paths.
  The authors give no proof that the DALi and TAMAA loop ends, or that it
  finds the best path and schedule together.
- DALi may return a path that is not the shortest, because of the virtual
  soft-constraint cost. [p. 9] The paper does not state the range of the
  soft-constraint coefficient. MMT has a "preferred area" type. [p. 24] A
  coefficient below 1 would make the Euclidean estimate of DALi* too high.
- Section 1 says that the planner should choose to wait, circumvent, or
  cross an area. [p. 2] Algorithm 1 only avoids a cell during its closed
  time. [p. 12] The paper does not describe a wait option.
- As the pseudocode reads, `IsInsideTemporaryObstacle` tests the arrival
  time at the end cell of an edge. [p. 12] The paper does not say how it
  treats the time that an agent spends inside a cell, or the slowdown in a
  heat area.
- For new tasks, the plan is the fastest extension of the old plan. [p. 21]
  This can be slower than a plan from scratch. The paper reports the
  synthesis times (44.5 s and 623 s) but not the two mission durations.
  [p. 34] The text calls the extension "fastest". [p. 21]

**Requirement fidelity**

- The requirement categories and the query templates (7) to (10) are a small
  fixed set. [p. 5, p. 17–18] The paper gives no check that the templates
  match the intent of a given quarry requirement.
- Query (10) has an agent index `a`. The paper does not show the form for
  several agents. [p. 18]
- In Case ii, the wheel-loader rule has four forms. The requirement says
  "two other vehicles at the primary crusher". The guard is `PCQueue > 2`.
  The text says "less than two". Query (12) uses `PCQueue < 2`. [p. 35]
  They do not agree on the threshold. The paper does not say how `PCQueue` changes while a truck
  loads at the wheel loader.
- The paper gives no states or run times for Queries (7) to (9) and (12) to
  (14). It says that the plan shown in MMT demonstrates Queries (12) to (14).
  [p. 37] The queries are `A[]` queries, so a plan alone does not show them.
- The battery check depends on `k`, the battery size, and the distances,
  which the paper does not give. The authors choose the distances so that
  the trucks do not drain. [p. 33, p. 36]
- The description of Case i gives no hardware and no number of runs for the
  two times. [p. 34]

**Inconsistencies inside the PDF**

- The text says that group 3 answers RQ3. RQ4 covers multiple agents.
  [p. 27, p. 31] This reads as a typing error.
- The caption of Fig. 21 says that a point at the boundary is 924 seconds.
  The timeout is 1 hour. [p. 27, p. 32]
- Section 8.1 says that the authors "measure results for all possible
  combinations" of parameters. [p. 38] Section 6.1 gives only ranges and
  fixed defaults for the other parameters. [p. 26–27]
- Section 8.2 says that path-planning time grows linearly with agents.
  [p. 38] Group 3 shows no significant difference, with reused paths.
  [p. 32] The linear growth is an argument, not a measurement.
- The page 3 claim that no such framework exists in academia or industry has
  no support beyond the related work.
- The ACM reference line prints the placeholder DOI
  `10.1145/nnnnnnn.nnnnnnn`, volume `1`, and number `1`. [p. 1]

**Changes against the thesis notes (Paper C)**

- The thesis notes say that Paper C leaves the integration of MCRL into
  MALTA as future work. This version does not change that. It says the back
  end can use schedulers that combine model checking and reinforcement
  learning. [p. 22] It says that MALTA provides both kinds of methods.
  [p. 39] The conclusion still lists machine learning integration as
  future work. [p. 41] The experiments use TAMAA only. The inconsistency
  stays.
- The thesis notes list six research questions for Paper C. This version
  lists seven challenges (path planning, task scheduling, mission planning,
  automation, adaptability, reusability, and visualization) and four
  evaluation questions. [p. 3, p. 26]
- The author order differs. The thesis lists Enoiu and Cürüklü before
  Seceleanu. This PDF lists Seceleanu before them. [p. 1]
- Three values in the thesis notes stay the same in this version. They are
  the 1-hour timeout, the timeouts at 3 agents with 5 milestones and at 4
  agents with 3 milestones, and the 6.9-minute plan. [p. 27, p. 32, p. 37]
- The thesis tool chapter lists Theta* among the MALTA planners. This paper
  lists A* and DALi with DALi*. It names Theta* only in related work.
  [p. 22, p. 39]

**AI and machine-learning aspects**

- The paper has no large language models.
- The paper contrasts its formal guarantee with "AI-based mission-planning
  algorithms". [p. 38] Its future work adds machine learning. [p. 41]
- The query templates (7) to (10) are a small target for a translation from
  natural-language requirements to TCTL. The paper does not try it. The user
  edits the queries by hand. [p. 14]

## Terms

| Term | Meaning in this paper |
|---|---|
| Mission plan | A pair of a task schedule and the paths between milestones |
| Milestone | A position where agents run tasks, such as a stone pile, a crusher, or a charging pole |
| Task schedule | An order of movement and task actions with start and finish times |
| Temporary obstacle | An area that vehicles cannot enter for a known time period |
| Heat area | An area with a bad road. Vehicles travel slower there by a set factor. |
| Soft constraint | An undesirable area that the planner avoids when it can. The cost is virtual. |
| Granularity | The size in meters of one grid cell |
| DALi | Path planner based on Dijkstra's algorithm that handles road conditions and user preferences |
| DALi* | DALi with the A* distance estimate |
| TAMAA | Task scheduler that generates UPPAAL models and reads the schedule from a trace |
| MALTA | The toolset of this paper, with GUI, middleware, and back end |
| MMT | Mission Management Tool, the GUI front end |
| UTA | UPPAAL timed automata: timed automata with data variables, channels, and urgent and committed locations |
| `A[] p` | Invariance: `p` holds in every state of every path |
| `E<> p` | Reachability: some path reaches a state where `p` holds |
| BCET, WCET | Best case and worst case execution time of a task |
| 1-player game | A model where the agents control all choices, including the task durations |
| Witness trace | An example run that UPPAAL returns for a satisfied reachability query |
| Welch's t-test | A test for equal means of two samples with unequal variances |

## Citation

Rong Gu, Eduard Baranov, Afshin Ameri, Cristina Seceleanu, Eduard Paul
Enoiu, Baran Cürüklü, Axel Legay, and Kristina Lundqvist. "Synthesis and
Verification of Mission Plans for Multiple Autonomous Agents under Complex
Road Conditions." ACM Transactions on Software Engineering and Methodology
(TOSEM), 2024.
