# Temperature Controller SpecForge Tour

## Purpose

Create a compact SpecForge 0.5.10 project that teaches the core authoring and
analysis workflow through a temperature-controller example. The project should
be broad enough to demonstrate temporal requirements and trace analysis while
remaining understandable as a single Lilo system.

## Project Structure

```text
specforge-tutorial/
├── specforge.toml
├── src/
│   └── temperature_controller.lilo
└── data/
    ├── safe.csv
    └── faulty.csv
```

The project configuration points SpecForge at `src/`. The data directory holds
two deterministic comma-separated values traces used for monitoring.

## Lilo System

The `temperature_controller` system contains:

- A `Float` temperature signal.
- A `Bool` heater-state signal.
- Parameters for minimum safe temperature, maximum safe temperature, and target
  temperature. Defaults make the project immediately analyzable.
- Reusable definitions for low, high, safe, and target-temperature conditions.
- A hard assumption limiting temperatures to a physically meaningful range.
- A safety specification requiring temperature to remain inside the configured
  safe range.
- A control specification requiring the heater to be active when temperature
  is below the target.
- A timed recovery specification requiring a temperature below the target to
  reach the target within ten time units.

Each requirement has a docstring so the Visual Studio Code outline, status
pane, and future language-model features have useful natural-language context.

## Learning Flow

1. Open the project root as the sole Visual Studio Code workspace.
2. Inspect syntax highlighting, outline entries, diagnostics, and code lenses.
3. Run parsing, type checking, and static analyses.
4. Inspect satisfiability and generate an example trace.
5. Monitor `safe.csv` and confirm that the selected requirements hold.
6. Monitor `faulty.csv`, locate a deliberate violation, and drill down through
   the monitoring tree to identify its cause.

The project starts in a valid state. Any syntax or type-error exercises will be
temporary edits performed during a lesson, not defects committed to the
baseline.

## Trace Design

Both traces use the exact columns required by the system schema:
`time`, `temperature`, and `heater_on`. Times are strictly increasing.

- `safe.csv` remains within the configured bounds, activates the heater below
  the target, and reaches the target within ten time units.
- `faulty.csv` keeps the temperature within its configured bounds and reaches
  the target in time, but leaves the heater off at one sample below the target.
  It remains structurally valid so monitoring reports a heater-control failure
  rather than a file-format error.

## Error Handling and Diagnostics

- The committed Lilo source must parse and type-check successfully.
- The schema command must accept both trace files without missing fields or
  type mismatches.
- Static analysis timeouts use SpecForge defaults unless a demonstrated query
  requires more time.
- The faulty trace must fail for its intended semantic reason, not because of
  malformed data, absent parameters, or inconsistent timestamps.

## Verification

Before the tutorial is considered ready:

- `specforge parse` succeeds for the project.
- `specforge check` succeeds for the project.
- Project diagnostics complete without unintended errors.
- Schema comparison accepts both data files.
- Monitoring the selected safety and control requirements on `safe.csv`
  produces the expected satisfying result.
- Monitoring the heater-control requirement on `faulty.csv` produces the
  expected failing result at the deliberately incorrect sample.
- The SpecForge server health endpoint reports version 0.5.10.

## Out of Scope

- Component hierarchies and modules.
- Python Software Development Kit integration.
- Falsification against an executable system model.
- Animation and export.
- External or locally hosted language-model configuration.
