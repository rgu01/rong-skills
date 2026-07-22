# Research Plan: Embedded Requirement Validation

## Main question

What combination of rapid prototyping and lightweight formal methods can
validate ambiguous or contradictory feature requests for a non-safety-critical
embedded product before implementation?

## Subtopics

1. **Requirements-first methods**
   - Goal: find tools that turn constrained requirements into analyzable formal
     semantics and expose inconsistency or unrealizability.
   - Key aspects: controlled natural language, traceability, consistency,
     realizability, suitability for embedded control behavior.
   - Queries: official FRET documentation; official contract/realizability tools.

2. **Behavioral model checkers**
   - Goal: compare tools for state logic, concurrency, and real-time behavior.
   - Key aspects: modeling cost, counterexamples, timing support, executable
     simulation, integration suitability.
   - Queries: official UPPAAL, SPIN, TLA+/TLC, and nuXmv documentation.

3. **Code-level verification and pragmatic workflow**
   - Goal: distinguish requirement/model validation from verification of C code
     and combine formal evidence with scenarios, prototypes, tests, and HIL.
   - Key aspects: bounded verification, abstraction gap, staged adoption.
   - Queries: official CBMC and Frama-C documentation; relevant official guidance.

## Synthesis

Recommend a layered workflow, a decision table for selecting tools by feature
type, and a deliberately small pilot that fits the existing
`experiments/AI-New-Feature-workflow/design.md` lifecycle.
