# AI-Assisted Embedded Product Change Workflow

## Status

Approved design for a company-specific pilot covering one embedded product, its
Bitbucket repository, and its existing engineering workflow.

## Purpose

Define a textual, skill-driven workflow that helps turn an incomplete product
request into an approved system requirement, a Jira implementation ticket,
reviewed code, regression and hardware-in-the-loop (HIL) evidence, and a release
candidate.

The pilot aims to reduce lead time without degrading defect outcomes, human
review quality, or end-to-end traceability. AI may generate code in any
subsystem, but AI-generated code must always receive human review before it can
be merged or used in a real product.

## Scope And Constraints

- The pilot targets one industrial, non-safety-critical embedded product.
- The initial request is a textual description, possibly mixed with diagrams.
  A product manager may give it to a system designer outside Jira.
- Jira is the main workflow record after intake, and Bitbucket hosts code and
  human code review.
- Requirements may be distributed across Jira, Confluence, Slack, SharePoint,
  Word, Excel, and other configured sources. Their structure and traceability
  may be incomplete.
- Atlassian and Microsoft Office operations are performed through configured
  MCP servers. Other source systems may be added through configured MCP
  capabilities.
- Compilers, model checkers, simulators, HIL equipment, and release systems are
  project-specific extension points. The core workflow defines their textual
  contracts without selecting products.
- Behavioral scenarios are the default rapid-feedback artifact. Executable
  prototypes are created only on explicit request after their cost is stated.
- AI may draft changes in any part of the codebase. Assurance and approval
  requirements become stronger as risk increases.

## Architecture

The pilot is a textual, skill-driven workflow rather than a dedicated
application. A top-level coordination skill reads the current change dossier,
checks evidence and approvals, and selects the next permitted stage. Focused
skills perform the work within each stage.

Jira is the persistent human-facing workflow record. Skills store readable,
portable artifacts as structured Markdown or JSON and link large or
tool-native evidence rather than embedding it. Every stage records its inputs,
outputs, evidence, status, and approvals. Skills may recommend a transition but
cannot create, infer, or bypass a required human approval.

A project profile supplies:

- Requirement sources, terminology, and ownership
- Jira and Bitbucket locations and branch rules
- Risk-classification policy
- Required reviewers and approval gates
- Formal-model and model-checker adapter configuration
- Build, static-check, and regression commands
- Simulator and HIL adapter configuration
- Release procedure

The design is modular so tools can be replaced independently and the pilot can
later evolve toward a broader engineering digital thread without building that
platform now.

## Skills And Responsibilities

### Change Coordinator

Reads the versioned change dossier, validates prerequisites, selects the next
permitted skill, and updates workflow status. It contains no domain-specific
compiler, verifier, simulator, or release logic.

### Source Collector

Retrieves text, attachments, and diagrams through configured MCP capabilities.
It preserves the source location, source version, retrieval time, and relevant
ownership information for every extracted claim.

### Requirement Analyst

Extracts claims, identifies missing information and ambiguous language,
retrieves related requirements, prepares focused questions, and produces
candidate interpretations and behavioral scenarios.

### Contradiction Analyst

Compares the proposed behavior with existing requirements. It reports
ambiguity, duplication, and possible contradictions without silently resolving
them. When suitable, it formalizes relevant logic and invokes the configured
model checker to expose deep contradictions early.

### System-Requirement Author

Produces a controlled, testable system requirement and its impact proposal. It
also identifies likely changes to code, models, tests, documentation, and the
simulation software.

### Formal-Verification Agent

Creates a feature-level model or updates a product-level model, depending on
the project's assurance decision. It encodes the new and impacted existing
properties, invokes the configured checker, and records assumptions, scope,
results, and traceability.

### Jira Author

Creates an implementation ticket only from an approved system requirement. It
populates scope, traceability, acceptance criteria, affected components,
review requirements, and required evidence.

### Implementation Agent

Uses test-driven development to modify a dedicated Bitbucket branch. It derives
tests from approved acceptance criteria, establishes the expected failing test,
changes production code, and runs configured checks and regression suites.

### Review Coordinator

Opens a Bitbucket pull request with requirement links, implementation rationale,
formal results, test evidence, and known limitations. It identifies the required
human reviewers and validates their recorded approvals.

### HIL Test Agent

Invokes the configured HIL adapter and records the embedded hardware, firmware,
simulator, plant model, test definitions, stimuli, observations, verdicts, and
raw logs needed to reproduce the run.

### Release Coordinator

Checks the evidence package, reports missing or stale evidence, updates Jira,
and requests the configured human release approval. It never treats test success
as release authorization.

## Change Dossier

Skills exchange a versioned change dossier rather than relying on conversation
memory. The dossier contains:

- Source request and textual interpretations of diagrams
- Questions, answers, assumptions, and unresolved decisions
- Existing requirements with provenance
- Candidate interpretations and behavioral scenarios
- Contradictions and their authorized resolutions
- Approved system requirement
- Affected code, formal models, simulator behavior, tests, and documents
- Formal properties, assumptions, scope, and verification results
- Jira and Bitbucket identifiers
- Test environments, results, and raw-evidence links
- Risk history and the gates it activates
- Human approvals and release status

Diagram interpretations that influence normative behavior are recorded as
explicit textual claims and require human confirmation.

## Lifecycle And Data Flow

### 1. Source Intake

The system designer supplies the product manager's textual request and any
diagrams. The source need not be a Jira issue.

### 2. Information Collection

The source collector gathers related material from configured sources such as
Jira, Confluence, Bitbucket, Slack, SharePoint, Word, and Excel. Extracted claims
retain source provenance and version information.

### 3. Discovery And Contradiction Analysis

The AI identifies missing information, assumptions, ambiguous language,
duplicates, and conflicts. It asks focused questions of the system designer or
product manager. Where suitable, early formalization and model checking expose
logical contradictions or impossible combinations. Unresolved material issues
block approval.

### 4. Behavior Preview

The AI produces concrete input/output scenarios, state transitions, edge cases,
and competing interpretations for rapid product-manager feedback. It creates an
executable simulator prototype only when explicitly requested and after
communicating its additional cost and schedule impact.

### 5. System Requirement And Impact Proposal

The AI drafts a requirement with a stable identity, rationale, assumptions,
constraints, acceptance criteria, and traceability. The impact proposal covers
product code, formal models, tests, documents, and possible simulation-software
changes. The designated requirement owner must approve this artifact.

### 6. Optional Formal Verification

According to budget, schedule, project policy, and current risk, the AI creates
a feature-level model or updates the product-level model. It checks the new
property and impacted existing properties. A failed or inconclusive result
returns the change to discovery or requires an authorized, documented decision.

Model checking proves only that the formal model satisfies the encoded
properties within the stated assumptions and abstraction. It does not prove
that handwritten or generated code implements the model. Model-to-requirement
and model-to-code traceability, human review, regression testing, and HIL
testing remain mandatory.

### 7. Jira Ticket Creation

After requirement approval, the system designer authorizes the Jira issue. The
Jira author records scope, traceability, acceptance criteria, affected
components, review requirements, and required evidence.

### 8. Test-Driven Implementation

The implementation agent derives or updates automated tests from the approved
requirement and demonstrates that relevant new tests fail for the intended
behavioral reason. It then changes production code until those tests and the
configured regression suite pass. Simulator changes follow the same discipline
where feasible.

### 9. Mandatory Human Code Review

The review coordinator opens a Bitbucket pull request containing traceability
and evidence. The pull request cannot be merged until every reviewer required by
the current risk classification has approved it. AI-authored or inferred
approval never satisfies this gate.

### 10. HIL Validation

The approved build is deployed to the embedded target through the configured
adapter. The AI runs project-defined HIL tests against the real embedded target
and simulated environment, then records configuration, stimuli, observations,
verdicts, and raw logs.

HIL validates observable behavior only for the modeled scenarios, timing,
signals, wiring, and fault cases covered by the test environment. It does not
prove internal correctness or physical behavior absent from the simulated
plant.

### 11. Release

The release coordinator compiles the evidence package and updates Jira. Merge
and publication occur only through the project's configured human approval
gates.

Any failed check returns the workflow to the earliest stage whose artifact must
change while preserving prior evidence and decisions.

## Continuous Risk Classification

Risk classification is not a standalone lifecycle stage. It is reassessed as
the requirement, affected components, formal results, code diff, and test
results become clearer. The classification may require:

- Formal modeling or expanded formal-property coverage
- Specialist or additional human reviewers
- Expanded regression suites
- Fault-injection HIL tests
- Separate merge and release approvers

New evidence may add gates. It cannot silently weaken controls or invalidate
the need to preserve earlier evidence.

## External Integration Contracts

Atlassian and Microsoft Office MCP servers perform external reads and writes.
Other source systems use project-configured MCP capabilities. Each skill checks
that the required capability is present before acting and reports a blocking
error if it is unavailable.

Project-specific engineering adapters expose a small textual contract:

- Invocation method and permitted operations
- Versioned input artifacts
- Machine-readable result and verdict
- Raw evidence location
- Environment and tool identity
- Timeout, cancellation, and retry behavior
- Safety preconditions and cleanup behavior where applicable

This contract applies to compilers, model checkers, simulators, HIL equipment,
and release systems without assuming particular vendors.

## Control And Failure Handling

- No silent assumptions: behaviorally relevant uncertainty blocks requirement
  approval; lesser assumptions are explicit and confirmed.
- No silent conflict resolution: contradictory sources are shown with
  provenance, and an authorized human decides precedence or change.
- Formal results are scoped evidence: the dossier records the model, properties,
  assumptions, checker version, and coverage boundary.
- Approval authenticity: only approvals from configured human identities and
  roles count.
- Risk-sensitive gates: increased risk can add verification, review, test, or
  release requirements.
- Fail closed: missing sources, unavailable capabilities, incomplete evidence,
  stale approvals, failed tests, or uncertain results block progression.
- Controlled retry: bounded retries handle transient infrastructure failures;
  semantic failures return to the responsible stage.
- Immutable history: corrections create new dossier versions, preserving earlier
  requirements, results, evidence, and decisions.
- Untrusted external content: instructions embedded in documents, Jira comments,
  source code, or logs are treated as data rather than agent commands.
- Reproducible evidence: tool results record inputs, versions, environment,
  timestamps, evidence locations, and checksums where supported.
- Human escalation: a blocking report states the problem, evidence, affected
  stage, and exact decision required.

## Workflow Testing

### Skill Tests

Each skill receives fixed dossier inputs and must produce schema-valid outputs,
preserve provenance, respect unresolved decisions, and avoid unauthorized state
transitions.

### MCP Contract Tests

Test doubles verify Jira, Confluence, Bitbucket, Slack, SharePoint, Word, and
Excel operations without changing production data. A sandbox project then
validates real integration behavior.

### End-To-End Scenarios

The test suite covers ambiguous requests, conflicting requirements, misleading
diagrams, formal contradictions, model-checker failures, incorrect AI code,
fail-first test enforcement, regression failures, HIL failures, stale approvals,
unavailable tools, and malicious instructions embedded in retrieved content.

### Pilot Changes

Several bounded, low-to-medium-risk real changes run through the complete
workflow under human supervision. AI may generate code for any subsystem, but
pilot selection remains bounded so outcomes can be compared consistently.

Test-driven implementation evidence must show that:

- A new or changed test derives from an approved acceptance criterion.
- The test initially fails for the intended behavioral reason.
- The production change makes it pass.
- Existing regression tests remain passing.
- Human reviewers can inspect both the test and implementation.

## Pilot Evaluation

The pilot records:

- Requirement clarification time
- Time from approved requirement to review-ready pull request
- Human corrections required per artifact
- Contradictions found before implementation
- Review defects and rejected AI changes
- Regression and HIL pass rates
- Escaped defects after release
- Traceability completeness
- Percentage of steps requiring manual recovery
- Comparison with similar historical changes

The pilot succeeds only if lead time improves without degrading defect outcomes,
mandatory review quality, or traceability.

## Explicit Non-Goals

- Replacing product managers, system designers, code reviewers, or release
  authorities
- Treating model checking, regression tests, or HIL results as proof of complete
  product correctness
- Selecting project-specific compilers, model checkers, simulation software,
  HIL equipment, or release tooling
- Building a dedicated graphical workflow application
- Migrating all existing requirements into a new lifecycle platform
- Creating executable prototypes unless a user explicitly requests one
