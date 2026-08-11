# AI-Assisted Model Checker: A Product-Controlled Agent Harness

A concept note recorded on 2026-08-05. The idea was inspired by
[LongHorizon Harness](https://github.com/AMAP-ML/LongHorizon-Harness) and explores
how a similar orchestration pattern could make artificial intelligence (AI) an
integrated, controlled part of a model-checking workflow.

This is an architectural direction, not an implementation specification. Names
such as **AI-assisted model checker**, **Manager**, **Designer**, and **Auditor**
are provisional.

## Executive summary

The central proposal is to move from optional AI tools to a product-controlled
AI-assisted workflow:

```text
Current model

user prompt -> AI agent -> optional MCP tools -> model checker

Proposed model

user -> product harness -> model checker + AI agents + human review
                        -> persistent state, evidence, and workflow dashboard
```

With a Model Context Protocol (MCP) server that exposes model-checking tools, an
AI agent can invoke the checker, but only when a user chooses an agent and asks
a question that triggers the appropriate tool. A user can ignore the agent,
invoke the wrong tool, or bypass the assisted workflow entirely.

An AI-assisted model checker would invert this relationship. The customer would
start an installable model-checking product with an integrated orchestration
harness. The harness would own the workflow and invoke the model checker, AI
agents, and human-review gates when appropriate. Users could monitor,
intervene, or take control, but they would not have to discover the correct
prompts or orchestrate the agents themselves.

The essential idea is:

> The harness controls the engineering workflow, while AI agents act as
> replaceable components within that workflow.

## Inspiration: LongHorizon Harness

A LongHorizon Harness job can be started with a command such as:

```bash
lh-harness run \
  --task @job-description.md \
  --agent codex \
  --dashboard
```

The harness creates three logical responsibilities:

- **Manager:** maintains the original goal, current state, verified progress,
  and next focused task.
- **Executor:** performs the focused task in the real environment, normally
  starting the round with a fresh agent context.
- **Auditor:** independently inspects the resulting environment, artifacts,
  logs, and tests.

The same agent backend can serve all three roles, or different backends and
models can be selected for different roles. The separation is primarily a
separation of context, instructions, and responsibility; it is not necessarily
organizational or safety independence.

### Round-based workflow

LongHorizon Harness proceeds in repeated Manage-Execute-Audit rounds:

1. **Initialize the run.** The command-line interface reads the task text or
   task file and creates an isolated run directory, workspace, log area, and
   harness state directory. It configures the selected agent adapter,
   execution environment, role budgets, and optional dashboard.

2. **Construct the Manager context.** The harness builds a controlled Manager
   prompt containing the original task, the maintained task state, relevant
   prior audit reports, harness feedback, and any human instructions injected
   through the dashboard. It does not simply replay one ever-growing
   conversation.

3. **Select one next step.** The Manager updates the task state and chooses one
   focused GUI or command-line subtask. It may alternatively declare the job
   complete, report that it is blocked, or ask for human input. The Manager also
   identifies the audit reports relevant to the next task.

4. **Run the Executor.** The harness constructs an Executor prompt from the
   original task, the Manager's task contract, maintained state, and selected
   audit evidence. The Executor operates in the actual workspace and reports
   what it changed, which commands or applications it used, what it produced,
   and what remains unresolved.

5. **Run the Auditor.** The harness gives the Auditor the assigned task, the
   Executor's report, the task state, and relevant prior evidence. The Auditor
   inspects the real environment and classifies the result as complete,
   incomplete, or blocked, together with an integrity classification. The
   Auditor is instructed to inspect rather than silently finish the Executor's
   task.

6. **Persist the round.** The harness stores role prompts, outputs, raw
   trajectories, task state, audit reports, events, and artifacts. The next
   Manager round receives the verified intermediate state instead of depending
   on an agent to remember the entire history.

7. **Apply completion and human gates.** Completion is accepted only when it is
   supported by a suitable audit result. The dashboard can stop and ask for
   human action when the Manager requests input, the job is blocked, repeated
   failures occur, the round budget is exhausted, or completion needs review.
   A user can continue, stop, or inject instructions into a later round.

8. **Produce the final record.** The run ends with a report and a preserved
   management transcript. The complete run remains inspectable and resumable
   through its files and dashboard representation.

The dashboard therefore shows mediated role trajectories, plans, execution
results, audit evidence, artifacts, rework reasons, and human gates. It should
not be understood as three agents freely chatting with each other: the harness
constructs and records the information passed from one role to the next.

## Proposed AI-assisted model checker

The product would apply the same general control pattern to a domain-specific,
potentially safety-relevant verification workflow. It could be distributed as
a signed binary and started with a selected agent backend, for example:

```text
ai-model-checker.exe --project <project> --agent codex --dashboard
```

The exact user interface is not important to the architecture. The same
harness could be started from a command line, a desktop icon, a project action,
or a separate workflow dashboard. What matters is that all entry points call
the same workflow engine rather than reimplementing orchestration in prompts or
user-interface code.

### Illustrative workflow

An AI-assisted model-checking workflow might contain stages such as:

```text
model, properties, requirements, test data, and project material
    -> inventory and validate inputs
    -> identify missing or ambiguous information
    -> human clarification/approval when required
    -> create or update the model-checking project
    -> generate or update formal properties and test scenarios
    -> run the prescribed model-checking strategies
    -> collect proofs, counterexamples, logs, and generated artifacts
    -> classify and explain findings
    -> propose corrections or additional tests
    -> human review of safety-relevant changes
    -> rerun affected stages
    -> assemble the final evidence and report
```

This flow is illustrative. The production workflow should be derived from the
actual verification process, model-checker APIs, assurance requirements, and
customer constraints. It should not copy LongHorizon Harness roles or routing
rules mechanically.

### Main components

#### Workflow engine

The workflow engine is the authority for sequencing. It should:

- define stages, prerequisites, transitions, retry rules, and termination
  conditions;
- prevent agents from bypassing required product runs or human approvals;
- construct the context supplied to each agent role;
- invoke only permitted model-checker operations;
- persist state after every material transition;
- resume safely after interruption; and
- create a complete event and evidence trail.

The first implementation could use Python, but the architecture should be a
typed state machine rather than a loose collection of prompt templates. A
production package may compile or bundle the implementation into a signed
executable.

#### Model-checker adapters

Product-specific adapters would invoke the model checker and turn its outputs
into structured results. The harness should make decisions from exit status,
machine-readable output, expected artifacts, checksums, and other deterministic
evidence whenever possible. Natural-language agent claims should not replace
model-checker evidence.

#### Agent adapters and roles

Agent adapters would allow a customer to select an approved backend such as
Codex or Claude Code. The harness would supply role-specific system
instructions, task contracts, allowed tools, evidence, and execution budgets.

Possible roles include Designer, Tester, Analyst, Manager, Executor, Reviewer,
and Auditor. These labels are secondary. A role should be introduced only when
it has a clear responsibility, input, output, permission set, and acceptance
rule.

For example, an agent may explain a counterexample or propose a model
correction, but the resulting explanation remains advisory until a new
model-checker run and any required human review confirm the new state.

#### Persistent run state

Each run should preserve at least:

- the original goal and input-material inventory;
- tool, product, agent, model, prompt, and workflow versions;
- current stage and remaining work;
- inputs and outputs for every stage;
- product logs, proofs, counterexamples, and generated artifacts;
- agent prompts, responses, tool calls, and role trajectories;
- human questions, approvals, rejections, and instructions;
- hashes or checksums linking evidence to the exact artifacts reviewed; and
- the final outcome and report.

Files are a simple and transparent starting point. A database could later be
added for indexing or collaboration, while the run manifest and evidence
artifacts remain exportable.

#### Workflow dashboard

The workflow dashboard could become the monitoring and control interface for
the harness. It could show:

- current workflow stage and verification status;
- completed, active, blocked, and pending work;
- agent-role activity and controlled conversations;
- product outputs and supporting evidence;
- proposed changes and their consequences;
- security and approval gates; and
- controls to provide input, approve, reject, retry, pause, resume, or take
  over a task.

The dashboard is a user interface, not the owner of workflow truth. The
underlying harness state should remain authoritative so that command-line,
desktop, dashboard, and other clients behave consistently.

## Security and human review

The harness can provide a stronger security boundary than an open-ended agent
conversation because it controls which information and tools enter each agent
context. Relevant controls include:

- allowlisted tools and product operations for each stage and role;
- least-privilege file and project access;
- policy-based selection and redaction of project information;
- explicit approval before sensitive information enters an external model
  context;
- approval before an agent-proposed change is applied;
- immutable or tamper-evident audit records; and
- separation between advisory AI output and authoritative model-checker
  evidence.

The outbound boundary includes more than the initial prompt. Project excerpts,
retrieved files, tool results, logs, screenshots, and conversation history may
all become model input. A security gate must therefore govern the complete
model-bound context, including later tool results, rather than review only the
first prompt.

Hardcoding a workflow and controlling prompts improves consistency and reduces
accidental misuse, but it does not automatically make the system safe. Safety
depends on correct transition rules, robust product adapters, access controls,
evidence validation, model-data policy, and well-defined human authority.

## Packaging and intellectual property

The AI-assisted model checker could be delivered as a signed executable instead
of distributing a readable Python MCP-server repository. This would provide a
cleaner product boundary and meaningful practical protection:

- customers would not receive ordinary source files;
- internal prompts and workflow logic would not be casually editable;
- code signing could authenticate official releases and detect modification;
- licensing and version compatibility could be enforced at the product
  boundary; and
- installation and support could follow the existing model-checker product
  model.

This should be described as **source concealment and reverse-engineering
resistance**, not absolute source-code protection. Python packaged with a tool
installer or a Python wheel may still expose source or recoverable bytecode.
Bundlers such as PyInstaller mainly package Python; compilation with tools such
as Nuitka or implementation in a native compiled language raises the reverse-
engineering cost but cannot eliminate it. Copyright protects both source and
binary forms, but packaging determines how easily implementation details can be
inspected.

Secrets such as private licensing keys or organization-owned agent credentials
must not be embedded in the executable. Customers would normally configure
their approved agent backend and credentials separately.

## Expected benefits

### 1. Productization and practical source-code protection

AI assistance becomes an integrated model-checker capability rather than a
repository of MCP tools, skills, and source code that customers must assemble.
A signed executable provides a familiar deployment, licensing, update, and
support boundary while making casual inspection or modification harder.

### 2. Controlled and repeatable AI usage

The product team defines the workflow, prompts, permitted operations, evidence
requirements, transition rules, and human gates. Users no longer need to know
which question triggers which tool. If a user only watches the dashboard, the
workflow still follows the prescribed sequence and stops where human input is
required.

### 3. Familiar user experience

Existing model-checker users can retain the project concepts and operations
they already know. They select or configure an AI backend when starting the
product or creating a project, while the product manages agent interaction,
state, and verification orchestration. A dashboard can provide a common place
to monitor and intervene without requiring users to conduct every step as an
open-ended chat.

### 4. Comparatively direct path to a prototype

The proposal can reuse an existing model-checker command-line interface, Python
integration code, agent command-line interfaces, MCP tools, and dashboard
components. A first prototype does not require embedding a general-purpose chat
interface directly inside the model checker's graphical user interface or
adopting a commercial agent platform. Its core can be a local workflow runner
that:

- reads project material;
- stores task and artifact state;
- constructs controlled prompts;
- launches configured agents and model-checker operations;
- applies human gates; and
- exposes run data to a dashboard.

This makes a prototype comparatively straightforward, but a supported product
is not merely a few prompt-generating scripts. Production quality requires
reliable interruption recovery, concurrency control, versioning, deterministic
evidence parsing, permissions, data-loss prevention, installation, upgrades,
diagnostics, and testing of both successful and failed workflows.

## Relationship to MCP and conversational agents

This concept does not make MCP useless. MCP can remain an internal integration
mechanism through which an agent or harness invokes narrowly defined product
operations. The distinction is who owns orchestration:

```text
MCP-led conversational use
    user and agent decide what to do
    MCP exposes optional capabilities

Harness-led product use
    product workflow decides what must happen
    harness invokes agents and product capabilities at defined stages
```

Conversation also remains useful. A user may clarify an ambiguity, ask for an
explanation, modify a plan, or take over an operation. The difference is that
conversation is one controlled interaction surface within the workflow rather
than the only place where workflow state and sequencing exist.

## Success criterion

The concept succeeds if a user can start an AI-assisted model-checking job,
provide only the required human decisions, and obtain a complete, traceable run
in which:

- required engineering and verification stages cannot be silently skipped;
- AI agents receive only approved context and permissions;
- model-checker evidence remains authoritative;
- every material transition and human decision is recorded;
- interrupted jobs can resume from a known state; and
- users can understand progress and take control through the dashboard.

## Open design questions

Before implementation, the following questions need explicit decisions:

1. Which narrow model-checking workflow should be the first prototype?
2. Which stages are deterministic product operations, which use agents, and
   which require human judgment?
3. What evidence is authoritative for each transition?
4. Which project information may be sent to each supported agent backend?
5. How will security review cover dynamic tool results and later agent turns?
6. Should the ordinary model checker remain directly launchable, or is the
   AI-assisted product intended to be the primary entry point for selected
   workflows?
7. Which role boundaries are useful, and do any require different models,
   permissions, or organizational independence?
8. How will the dashboard read and modify harness state without duplicating the
   workflow engine?
9. What packaging technology provides an acceptable balance of development
   speed, supportability, and reverse-engineering resistance?
10. How should offline or restricted customer environments configure agent
    backends and data policies?

## Concise formulation

> The AI-assisted model checker is a packaged, product-controlled orchestration
> harness that governs how users, AI agents, and the model checker collaborate
> throughout a verification workflow. It replaces prompt-dependent, optional
> AI assistance with a repeatable, stateful, auditable process that users can
> monitor and control through a workflow dashboard.

The proposed shift is therefore:

> **From:** AI agents may use model-checking tools when prompted correctly.  
> **To:** A product-controlled workflow invokes AI agents and the model checker
> when appropriate.
