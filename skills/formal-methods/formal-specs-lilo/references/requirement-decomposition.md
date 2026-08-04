# Requirement Decomposition

## Atomicity first

Split before translating. One sentence containing independent responses,
different triggers, or different timing clauses must be split into atomic
obligations. Keep each atomic obligation traceable to its source text.

## FRET-inspired fields

Use these internal fields to expose meaning, not to prescribe FRET syntax:

- **scope:** the mode, phase, or domain in which the obligation applies.
- **condition:** the state, event, or precondition that activates it.
- **responsible component:** the system or component that owns the obligation.
- **timing:** when, for how long, or within what elapsed-time bound it applies.
- **response:** the observable property required of the responsible component.

Do not emit FRETish. Use these fields only to elicit a precise Lilo requirement.

## Symbol inventory

Inventory every referenced concept: its candidate name, meaning, type, unit,
whether it varies over time, observability, owner, and any matching existing
declaration. Treat names from prose as candidates until confirmed against the
project or user clarification.

## Ambiguity checklist

Clarify each of the following before editing when it affects the obligation:

- state condition versus event/rising-edge trigger;
- inclusive versus exclusive threshold;
- elapsed-time unit versus sample count;
- bounded value and interval boundary;
- signal versus fixed parameter;
- type and unit;
- observable interface versus implementation detail;
- missing default values; and
- whether two clauses are one obligation or multiple obligations.

## Internal interpretation record

Record one mapping per atomic obligation:

```text
requirement_id:
source_text:
scope:
condition:
responsible_component:
timing:
response:
symbols:
existing_declarations_reused:
new_declarations_needed:
clarifications:
```

The interpretation record is internal preparation, not a substitute for asking
the user. Do not persist invented assumptions into project files.
