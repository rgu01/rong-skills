# SpecForge Learning Notes

These notes summarize the SpecForge 0.5.10 setup and the concepts explored in
the temperature-controller tutorial.

## What SpecForge Is

SpecForge is a formal-requirements authoring and analysis tool. Its Lilo
language describes constraints that observable system behavior must satisfy
over time.

A Lilo `system` is not normally an executable implementation or simulation
model. It declares the signals and parameters visible to analysis and states
formal requirements over them.

```text
real system, simulator, or hand-written scenario
                    │
                    ▼
             time-series trace
                    │
                    ▼
Lilo requirements ──┴──► SpecForge monitoring ──► satisfied / violated
```

Trace signals may represent inputs, outputs, environmental measurements, or
internal observable state. They are not limited to outputs.

## Installed Components

The Visual Studio Code extension and server both use version 0.5.10.

```text
Visual Studio Code
  └─ SpecForge extension
       └─ managed SpecForge server
            ├─ parser and type checker
            ├─ static and temporal analyses
            ├─ monitoring and exemplification
            ├─ Z3 formal solver
            └─ optional language-model provider
```

- Extension:
  `/home/rogu/.vscode-server/extensions/imiron.specforge-0.5.10`
- Shell command:
  `/home/rogu/.local/bin/specforge`
- Installed executable:
  `/home/rogu/.local/share/specforge/0.5.10/bin/specforge`
- Z3:
  `/home/rogu/.local/bin/z3`, version 4.14.1

`~/.local/bin` is in the shell `PATH`, so `specforge serve` resolves the
symbolic link and starts the installed executable without requiring its full
path.

The extension is configured to manage the server process itself. It may use a
different free port if its preferred port, 8080, is occupied.

## Lilo Building Blocks

The tutorial uses four main declaration kinds:

- `signal`: a value that varies over time, such as `temperature` or
  `heater_on`.
- `param`: a value fixed for one analysis, such as safe limits or target
  temperature.
- `def`: a reusable expression that gives domain vocabulary to lower-level
  logic.
- `spec`: a formal requirement that should hold.

An `assumption` is background knowledge taken as given during analyses such as
satisfiability and exemplification. It constrains the behaviors that SpecForge
considers.

The temperature-controller project defines:

- A safe temperature range from 16 to 28 by default.
- A target temperature of 22 by default.
- A safety requirement that temperature always remains in range.
- A control requirement that the heater is active whenever temperature is
  below target.
- A recovery requirement that a below-target temperature reaches target within
  ten time units.

## Temporal Logic Learned

The main operators explored were:

- `always expression`: the expression must hold at all relevant future samples.
- `eventually[0, 10] expression`: a satisfying sample must exist between the
  current time and ten time units into the future, inclusive.
- `condition => consequence`: if the condition is true, the consequence must be
  true; if the condition is false, the implication is true.

A local violation can affect earlier samples. If a requirement is
`always local_rule` and `local_rule` fails at time 5, the outer `always` result
is false at both time 0 and time 5 because the bad sample is in the future of
both evaluations.

The slow-recovery experiment illustrates interval boundaries. If target is
first reached at time 15:

- A recovery obligation created at time 0 fails because its `[0, 10]` window
  ends at time 10.
- An obligation created at time 5 succeeds because time 15 is exactly ten time
  units later.

## Monitoring Versus Static Analysis

Monitoring evaluates a specification against one concrete trace:

```bash
specforge monitor temperature_controller data/safe.csv temperature_stays_safe
```

Static analysis reasons about the requirement without a trace:

```bash
specforge analyze --all --system temperature_controller
```

Static analyses include:

- Satisfiability: whether at least one behavior can satisfy a specification.
- Consistency: whether the system's specifications can hold together.
- Redundancy: whether other requirements already imply a specification.

The deliberately impossible experiment used:

```lilo
spec impossible_temperature =
  always (temperature < 0.0 && temperature > 100.0)
```

Z3 proves this unsatisfiable because one number cannot satisfy both comparisons
at the same timestamp.

## Trace Files

SpecForge accepts comma-separated values, JSON, and JSON Lines trace data. The
tutorial uses comma-separated values with a required `time` column and columns
matching the Lilo signal names.

`safe.csv` is a hand-authored satisfying scenario. `faulty.csv` is also
hand-authored and deliberately leaves the heater off at time 5 while the
temperature is below target.

```text
time,temperature,heater_on
5,20.0,false
```

The file itself performs no action. It represents recorded or invented
behavior that monitoring evaluates.

The schema command checks that trace columns match the system:

```bash
specforge schema \
  --system temperature_controller \
  --only signals \
  --diff \
  --datafile data/faulty.csv
```

## Language-Model Features

Language-model features are optional. Z3 remains responsible for formal
results; a language model generates candidate Lilo or explains diagnostics in
natural language.

```text
Z3                         language model
formal result              generated Lilo or prose explanation
```

The extension stores provider keys in Visual Studio Code SecretStorage rather
than the repository. OpenAI was tested first, but its request returned HTTP 429
because the Platform Application Programming Interface account had no
available quota or had reached its spending limit. ChatGPT and Platform
Application Programming Interface billing are separate.

The active provider was then changed to Anthropic using model
`claude-haiku-4-5`. No secret key is recorded in these notes or in the project.

## Useful Commands

Run these from the tutorial project root:

```bash
specforge --version
specforge doctor
specforge parse
specforge check
specforge lint
specforge analyze --all --system temperature_controller
specforge schema --system temperature_controller
specforge monitor temperature_controller data/safe.csv temperature_stays_safe
```

Use `specforge COMMAND --help` for exact options.

## Current Experimental State

The tutorial repository contains user-created, uncommitted learning changes:

- `data/slow_recovery.csv`
- A temporary `impossible_temperature` specification in the Lilo source

These are intentionally preserved for continued experimentation. Remove the
temporary impossible specification when a clean, consistent baseline is
needed.

## Suggested Next Experiments

1. Compare monitoring trees for `safe.csv`, `faulty.csv`, and
   `slow_recovery.csv`.
2. Change one parameter default and predict which traces will fail.
3. Add a requirement that the heater is off at or above target.
4. Use exemplification to generate a satisfying trace.
5. Create a spec stub with a clear docstring and try language-model generation.
