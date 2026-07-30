# Temperature Controller Tour Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a valid SpecForge 0.5.10 temperature-controller project that demonstrates Lilo authoring, static analysis, exemplification readiness, and monitoring against satisfying and deliberately faulty traces.

**Architecture:** A single Lilo system owns all signals, parameters, reusable definitions, assumptions, and specifications. Two small comma-separated values traces exercise the same system schema: one satisfies the requirements, while the other violates only the heater-control requirement at a known sample.

**Tech Stack:** SpecForge 0.5.10, Lilo, Z3 4.14.1, TOML project configuration, comma-separated values trace data.

## Global Constraints

- Use SpecForge 0.5.10 and a single system named `temperature_controller`.
- Keep all Lilo source in `src/temperature_controller.lilo`.
- Keep the committed source parseable and type-correct.
- Use default-valued parameters so monitoring needs no separate parameter file.
- Keep trace timestamps strictly increasing.
- Make `faulty.csv` structurally valid and fail only the heater-control requirement at its deliberately incorrect sample.
- Do not add components, modules, Python integration, falsification, animation, export, or language-model configuration.

## File Map

- `specforge.toml`: declares the project name and `src/` source directory.
- `src/temperature_controller.lilo`: defines the complete temperature-controller system.
- `data/safe.csv`: satisfies safety, heater control, and timed recovery.
- `data/faulty.csv`: preserves safety and recovery but violates heater control once.

---

### Task 1: Valid Temperature-Controller System

**Files:**
- Create: `specforge.toml`
- Create: `src/temperature_controller.lilo`

**Interfaces:**
- Consumes: SpecForge 0.5.10 project discovery and Lilo syntax.
- Produces: system `temperature_controller`; signals `temperature: Float` and `heater_on: Bool`; default-valued parameters `min_safe_temperature`, `max_safe_temperature`, and `target_temperature`; specifications `temperature_stays_safe`, `heater_engages_below_target`, and `reaches_target_in_time`.

- [ ] **Step 1: Run the type-check acceptance test before implementation**

Run:

```bash
specforge check
```

Expected: exit 1 with `No .lilo files found in system.`

- [ ] **Step 2: Create the project configuration**

Create `specforge.toml`:

```toml
[project]
name = "specforge-tutorial"
source = "src/"
```

- [ ] **Step 3: Create the minimal complete Lilo system**

Create `src/temperature_controller.lilo`:

```lilo
system temperature_controller

/// Current measured temperature.
signal temperature: Float

/// Whether the heater is currently active.
signal heater_on: Bool

/// Lowest permitted operating temperature.
#[default = 16.0]
param min_safe_temperature: Float

/// Highest permitted operating temperature.
#[default = 28.0]
param max_safe_temperature: Float

/// Temperature that the controller should reach.
#[default = 22.0]
param target_temperature: Float

def below_target: Bool = temperature < target_temperature
def at_or_above_target: Bool = temperature >= target_temperature
def inside_safe_range: Bool =
  min_safe_temperature <= temperature &&
  temperature <= max_safe_temperature

/// Temperatures outside this broad physical range are excluded from analysis.
assumption physically_meaningful_temperature =
  always (-50.0 <= temperature && temperature <= 150.0)

/// The measured temperature must always remain within the configured safe range.
spec temperature_stays_safe = always inside_safe_range

/// Whenever the temperature is below target, the heater must be active.
spec heater_engages_below_target = always (below_target => heater_on)

/// Whenever temperature is below target, it must reach target within ten time units.
spec reaches_target_in_time =
  always (below_target => eventually[0, 10] at_or_above_target)
```

- [ ] **Step 4: Run parser, type checker, and fast diagnostics**

Run:

```bash
specforge parse
specforge check
specforge lint
```

Expected: all commands exit 0 with no unintended diagnostics.

- [ ] **Step 5: Run solver-backed analysis**

Run:

```bash
specforge analyze --all --system temperature_controller
```

Expected: exit 0; all three specifications are satisfiable under the physical-range assumption, with no unintended inconsistency.

- [ ] **Step 6: Commit the valid system**

```bash
git add specforge.toml src/temperature_controller.lilo
git commit -m "feat: add temperature controller specifications"
```

---

### Task 2: Satisfying Monitoring Trace

**Files:**
- Create: `data/safe.csv`

**Interfaces:**
- Consumes: system signals `temperature` and `heater_on`, parameter defaults, and all three specifications from Task 1.
- Produces: a strictly increasing four-sample trace that satisfies safety, heater control, and timed recovery.

- [ ] **Step 1: Run the schema acceptance test before the trace exists**

Run:

```bash
specforge schema --system temperature_controller --only signals --diff --datafile data/safe.csv
```

Expected: nonzero exit because `data/safe.csv` does not exist.

- [ ] **Step 2: Create the satisfying trace**

Create `data/safe.csv`:

```csv
time,temperature,heater_on
0,18.0,true
5,21.0,true
10,22.0,false
15,23.0,false
```

- [ ] **Step 3: Validate the trace against the system schema**

Run:

```bash
specforge schema --system temperature_controller --only signals --diff --datafile data/safe.csv
```

Expected: exit 0 with no missing or mismatched signal fields.

- [ ] **Step 4: Monitor every requirement**

Run:

```bash
specforge monitor temperature_controller data/safe.csv temperature_stays_safe --tree
specforge monitor temperature_controller data/safe.csv heater_engages_below_target --tree
specforge monitor temperature_controller data/safe.csv reaches_target_in_time --tree
```

Expected: each root monitoring result is true at the first timestamp; no requirement violation appears in the trace.

- [ ] **Step 5: Commit the satisfying trace**

```bash
git add data/safe.csv
git commit -m "test: add satisfying temperature trace"
```

---

### Task 3: Deliberately Faulty Monitoring Trace

**Files:**
- Create: `data/faulty.csv`

**Interfaces:**
- Consumes: the same system schema and specifications as `safe.csv`.
- Produces: a valid trace whose sample at time 5 has `temperature = 20.0` and `heater_on = false`, violating `heater_engages_below_target` while still satisfying safety and timed recovery.

- [ ] **Step 1: Run the schema acceptance test before the trace exists**

Run:

```bash
specforge schema --system temperature_controller --only signals --diff --datafile data/faulty.csv
```

Expected: nonzero exit because `data/faulty.csv` does not exist.

- [ ] **Step 2: Create the deliberately faulty trace**

Create `data/faulty.csv`:

```csv
time,temperature,heater_on
0,18.0,true
5,20.0,false
10,22.0,false
15,23.0,false
```

- [ ] **Step 3: Prove that the fault is semantic, not structural**

Run:

```bash
specforge schema --system temperature_controller --only signals --diff --datafile data/faulty.csv
```

Expected: exit 0 with no missing or mismatched signal fields.

- [ ] **Step 4: Establish the passing controls**

Run:

```bash
specforge monitor temperature_controller data/faulty.csv temperature_stays_safe --tree
specforge monitor temperature_controller data/faulty.csv reaches_target_in_time --tree
```

Expected: both requirements hold at the first timestamp.

- [ ] **Step 5: Demonstrate the intended heater-control failure**

Run:

```bash
specforge monitor temperature_controller data/faulty.csv heater_engages_below_target --tree --verdicts
```

Expected: the monitoring tree reports a false heater-control result caused by `temperature < target_temperature` while `heater_on` is false at time 5.

- [ ] **Step 6: Re-run the complete project gate**

Run:

```bash
specforge parse
specforge check
specforge lint
specforge analyze --all --system temperature_controller
curl --fail --silent --show-error http://localhost:8080/health
```

Expected: every command exits 0; the health endpoint returns `OK: VERSION=0.5.10`.

- [ ] **Step 7: Commit the faulty trace**

```bash
git add data/faulty.csv
git commit -m "test: add heater-control violation trace"
```
