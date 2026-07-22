# Embedded Requirement Validation: Research Synthesis

## Conclusion

Formal methods are useful here, but not as a mandatory full formal model of the
existing product. The practical choice is a layered workflow: retrieve and
structure impacted requirements, validate examples with stakeholders, check
assume/guarantee contracts for consistency and realizability, and create a
small behavioral model only for features whose state, timing, or concurrency
risk justifies it.

## Recommended baseline

1. Express each impacted requirement as a structured behavioral rule with
   trigger, precondition, response, timing, priority, and exceptions.
2. Give each rule concrete examples and counterexamples and replay them in a
   lightweight product simulator or executable state-machine prototype.
3. Translate only the new requirement and its impact cone into synchronous
   assume/guarantee contracts.
4. Use Kind 2 to check satisfiability, realizability, non-vacuity, and safety
   properties and to obtain counterexample traces.
5. Add a domain-specific behavioral model only when needed:
   - UPPAAL for deadlines, timeouts, task interactions, and real-time protocols.
   - SPIN for asynchronous processes, message channels, deadlock, and liveness.
   - TLA+/TLC for complex concurrent or distributed algorithms without central
     real-time constraints.
6. After implementation, use CBMC for bounded C/C++ memory-safety and assertion
   checks. This validates code, not the requirements model.

## Tool assessment

### FRET

NASA FRET is a good front end for restricted-English requirements. It provides
formal and visual representations, consistency checking, export, and
requirement-based test generation. It can improve stakeholder review, but its
controlled language still requires domain decisions and reviewed translations.

Source: https://github.com/NASA-SW-VnV/fret

### Kind 2

Kind 2 is the strongest default back end for the proposed pilot. It targets
synchronous reactive systems in Lustre, supports assume/guarantee contracts,
satisfiability and realizability checks, non-vacuity checks, counterexamples,
assumption generation, compositional verification, and test generation. This
matches embedded control requirements and can work on an impacted subsystem
without requiring a complete product model.

Source: https://kind2-mc.github.io/kind2/

### AGREE

AGREE is suitable if the product already uses AADL or is willing to adopt an
architecture model. It allocates assume/guarantee contracts to components and
checks composition. Introducing AADL only to analyze occasional feature
requests would add substantial modeling overhead, so it is not the first pilot
choice without an existing architecture-modeling practice.

Source: https://loonwerks.com/tools/agree.html

### UPPAAL

UPPAAL combines graphical timed-automata modeling, simulation, trace
visualization, and checking of real-time safety/liveness behavior. It is the
recommended specialist tool when milliseconds, deadlines, scheduling,
timeouts, or concurrent timed components are central. Commercial licensing
must be evaluated for company use.

Sources: https://uppaal.org/ and
https://docs.uppaal.org/gui-reference/verifier/

### SPIN and TLA+

SPIN is a good specialist checker for communicating concurrent processes,
deadlocks, invariants, and LTL properties in Promela. TLA+/TLC is strong for
high-level concurrent and distributed algorithms and supports executable model
simulation plus safety/liveness checking. Neither is the best universal front
end for ordinary product-manager requirements.

Sources: https://spinroot.com/spin/Man/Manual.html and
https://lamport.azurewebsites.net/tla/tools.html

### CBMC

CBMC verifies C/C++ after implementation by unwinding loops and checking such
properties as array bounds, pointer safety, and user assertions. It complements
requirements validation but cannot determine whether an informal requested
behavior is the right one.

Source: https://github.com/diffblue/cbmc

## Pilot recommendation

Use one representative feature and model only its impact cone. Compare three
artifacts with the product manager: scenario tables, an executable behavioral
prototype, and counterexample traces from contract checking. Measure modeling
hours, questions discovered, contradictions found before coding, stakeholder
corrections, and defects found later. Continue formalization only where the
early-detection value exceeds model-maintenance cost.
