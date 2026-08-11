# Gemini Enterprise Agent Platform

A discussion summary recorded on 2026-08-04. The concrete example is the
[AI-assisted embedded product-change workflow](../../experiments/AI-New-Feature-workflow/design.md),
used only as a thought experiment for understanding the platform—not as an
implementation plan.

## Central mental model

Gemini Enterprise Agent Platform is a managed operating environment for agents.
It is not itself the engineering workflow or the agent's domain knowledge.

```text
agent = model + instructions/workflow + tools + state

Agent Platform = runtime + identity + connectivity governance
               + registry + observability + evaluation
```

A **model** such as Gemini, Claude, or Llama supplies reasoning and language
generation. An **agent** is software that uses a model together with
instructions, tools, memory or persistent state, and workflow logic.

In the Gemini Enterprise app, Google's Core Assistant is the default front-door
agent. That does not mean every agent deployed on Agent Platform must use a
Gemini model.

## App versus platform

- **Gemini Enterprise app** is an employee-facing interface where people can
  discover and interact with approved agents.
- **Gemini Enterprise Agent Platform** is the developer and operations layer for
  building, deploying, governing, and evaluating agents.
- A company can use Agent Runtime through its interfaces without making the
  Gemini Enterprise app its employee front end. Using the app introduces a
  separate per-seat subscription.

For individual, interactive work such as coding, creating slides, writing
skills, or building harnesses, Claude and Codex remain natural tools. Agent
Platform becomes relevant when an agent workflow should become a shared,
repeatable, access-controlled, monitored company service.

## Models and external agents

Agents running on the platform can use different models:

- Gemini models;
- managed partner models, including Anthropic Claude;
- self-deployed open models such as Llama;
- external model endpoints called by custom agent code, subject to networking,
  authentication, and policy constraints.

Support is not identical for every model. Availability, data location, pricing,
tool support, and integrated platform capabilities can differ.

A self-deployed Llama model is still only a model endpoint. Agent logic must be
built around it to add instructions, tools, state, and workflow behavior.

External complete agents can be connected to the Gemini Enterprise app through
the open **Agent2Agent (A2A) protocol**. An agent that does not implement A2A
needs an adapter. Codex currently exposes a software development kit and a
**Model Context Protocol (MCP)** server, but is not documented as a native A2A
server; using Codex as an external Gemini Enterprise agent would therefore
require a small A2A-facing integration layer.

## Concrete product-change example

The full embedded product-change design covers eleven stages from incomplete
request through release. It is a plausible long-term platform use case but too
broad for a first platform pilot because it combines many source systems,
formal verification, software development, hardware-in-the-loop testing, human
approvals, and release integration.

A more useful bounded example is:

```text
product-change request
    -> collect relevant company sources
    -> identify ambiguities and contradictions
    -> produce behavioral scenarios
    -> draft a system requirement
    -> obtain human approval
    -> create a Jira implementation ticket
```

This example demonstrates the platform without assuming that P currently
has one standard company-wide verification workflow.

### Why the workflow may be valuable

The intended benefit is not merely automatic Jira creation. It is a helpful,
standardized entrance into engineering:

- The product manager can describe an incomplete idea conversationally.
- The agent can retrieve related company information and explain relevant
  constraints.
- It can identify ambiguity, contradictions, dependencies, and unrealistic
  expectations before implementation work begins.
- It can help the product manager clarify the idea for the system engineer.
- It can create a structured, traceable requirement and Jira ticket after human
  approval.

The platform does not make this the only entrance automatically. The company
must establish that process rule and configure surrounding systems and
permissions accordingly.

Questionable requests should not be discarded. The original request and its
provenance should be preserved, while unresolved material problems block its
promotion to an approved requirement or implementation ticket.

## What P defines versus what the platform supplies

| P and the agent define | Agent Platform supplies |
|---|---|
| Workflow stages and transition rules | Managed execution environment |
| Requirement-analysis behavior | Compute and scaling |
| Change-dossier schema and authoritative storage | Session and optional memory services |
| Approval rules and required human roles | Agent identity and access controls |
| Jira ticket structure | Agent and skill registration |
| Source and engineering-tool behavior | Governed connectivity |
| Quality and success criteria | Logs, traces, monitoring, and evaluation infrastructure |

The platform does not inherently know what a good system requirement is, what
constitutes valid approval, or which Jira fields are required. Those remain
company-defined behavior.

## Runtime and asynchronous human interaction

Agent Runtime is not conceptually a loop that continuously listens and creates
new agents. It is managed application hosting:

```text
request -> deployed agent endpoint -> agent code runs -> response
```

The deployed agent exists as a service. Runtime routes a request to it, starts
or scales the necessary compute, invokes a supported operation, and returns or
streams the result. Longer operations can be submitted as asynchronous jobs,
currently for up to seven days.

An agent should not remain running while it waits hours or days for a human:

```text
draft requirement saved
    -> invocation ends
    -> human approves later
    -> a new invocation starts
    -> approval is verified
    -> Jira ticket is created
```

The authoritative workflow state therefore belongs in the versioned change
dossier, Jira, or another durable store—not only in conversation memory. This
pause-and-resume pattern is a major benefit of using managed asynchronous agent
infrastructure for human-in-the-loop work.

## Agent, skill, and coordinator

- The **agent** is the running worker.
- A **skill** is a reusable procedure the worker follows.
- A **coordinator** is the role or control logic that selects the next permitted
  procedure.

In the example design, coordination is explicitly a skill: the Change
Coordinator reads the dossier, checks prerequisites and approvals, and selects
the next focused skill. It does not have to be a separate agent. It could be a
skill interpreted by one agent, deterministic orchestration code, or a
dedicated orchestration agent. Hard approval gates are generally better
enforced with deterministic code.

## Identity, Gateway, and Registry

- **Agent Identity** gives the product-change agent its own auditable identity
  and least-privilege permissions. It might read approved sources and create a
  Jira draft, while being unable to approve requirements, merge code, or
  release products.
- **Agent Gateway** governs which tools and other agents it may communicate
  with. It can apply connection and security policies, while the workflow still
  decides whether a valid business approval exists.
- **Agent Registry** records approved agents, endpoints, capabilities, versions,
  and ownership so employees use a governed agent rather than unofficial
  copies.

These services place organizational controls around the workflow; they do not
define the workflow.

## Observability and evaluation

**Observability** answers what the agent did: source retrievals, model and tool
calls, errors, timings, approval events, and Jira writes.

**Evaluation** asks whether the result was good. Suitable company-specific
measures include:

- provenance completeness;
- detection of material ambiguity;
- absence of unauthorized assumptions or transitions;
- requirement quality against a defined rubric;
- amount of human correction required;
- valid approval before ticket creation;
- clarification time relative to comparable historical changes.

Agent Platform supplies the evaluation machinery, but P must define what a
good system requirement and a successful workflow mean.

## Cost snapshot

Current public prices as of 2026-08-04 are in United States dollars:

| Component | List price |
|---|---:|
| Agent Runtime compute | $0.085 per virtual central processing unit-hour |
| Runtime memory | $0.009 per gibibyte-hour |
| Agent storage | $0.30 per gibibyte-month |
| Agent Gateway | $0.085 per 15,000 calls |
| Gemini Enterprise app | Starting at $30 per user/month |

The monthly platform free tier includes 50 compute hours, 100 memory
gibibyte-hours, and one gibibyte of storage. Model input and output tokens are
charged separately. For light use, model consumption or the optional app seat
licenses are likely to dominate raw runtime cost; engineering and maintenance
effort may dominate both.

An illustrative ten-minute run using one virtual central processing unit, two
gibibytes of memory, 50,000 Claude Sonnet 5 input tokens, and 10,000 output
tokens was estimated at roughly $0.24 under the August 2026 European Union
promotional model price, or about $0.35 after the promotion. Actual multi-step
document analysis may consume much more.

## Atlassian alternative

Atlassian Rovo Studio may be a more natural first platform for this bounded
example when Jira and Confluence contain most of the workflow:

- Rovo agents live inside Jira, Confluence, and Atlassian automation.
- They can use Atlassian and connected third-party knowledge.
- Jira Automation can invoke an agent asynchronously.
- Forge functions can add custom company logic and external integrations.
- Human approval can be represented as Jira workflow state.

One useful separation is that a Rovo agent invoked by automation cannot itself
invoke create, update, delete, or trigger actions. The automation can consume
the agent's result, verify workflow state, and then perform a deterministic Jira
create action.

Rovo is attractive for a Jira-centered workflow and faster no-code or low-code
adoption. Gemini Enterprise Agent Platform is broader and better suited to
heterogeneous systems, custom runtimes, custom model selection, and agents that
must operate independently of Atlassian products.

## Microsoft Copilot Studio alternative

Microsoft Copilot Studio is a graphical, low-code platform for building agents
and deterministic **agent flows**. For the bounded product-change workflow, it
could combine conversational assistance with an explicit flow:

```text
product manager in Teams, Microsoft 365, or a custom channel
    -> Copilot Studio agent clarifies the request
    -> agent retrieves Microsoft 365 and connected company data
    -> agent flow assembles the draft requirement
    -> flow pauses for named human reviewers
    -> approved data resumes the flow
    -> premium Jira connector creates the issue
```

This is a particularly close match for human-in-the-loop work. Copilot Studio's
human-review action can pause a flow, request structured information from
designated reviewers through Outlook, and resume with the submitted values.
The Jira connector can then create the issue as a deterministic step. The
current review action uses the first response received, sends requests only
through Outlook, and does not support reviewers outside the Microsoft tenant;
those constraints would matter when modeling approval authority.

Copilot Studio's strongest fit is an organization where Teams, Outlook,
SharePoint, Word, and Power Platform already form the working environment. It
provides many prebuilt and custom connectors, graphical workflow authoring,
Dataverse for structured state, administrative environments, analytics, and
cost controls. Compared with building on Gemini Enterprise Agent Platform, it
would require less custom infrastructure for approvals and Microsoft 365
integration.

The trade-offs are:

- It is more opinionated around Microsoft 365 and Power Platform than Google's
  general-purpose agent runtime.
- Sophisticated engineering tools still need custom connectors or remotely
  hosted services.
- The Jira connector is premium and has limitations: it requires Jira
  credentials, does not support Jira Server behind a firewall, and its issue
  creation action supports only simple field types in the dynamic schema.
- Complex behavior crosses several concepts—agent instructions, generative
  orchestration, agent flows, connectors, Dataverse, environments, and credit
  billing—which can make architecture and cost less transparent.
- Model choice is expanding through Microsoft Foundry, but bring-your-own-model
  support applies to prompt steps and has model/API limitations; it is not as
  unconstrained as deploying arbitrary custom agent containers.

Current pricing offers three routes: Microsoft 365 Copilot at $30 per
user/month for internal agents, a tenant-wide Copilot Studio capacity pack at
$200/month for 25,000 Copilot Credits, or pay-as-you-go billing through an Azure
subscription. Different operations consume different numbers of credits, and
connected Azure models can be billed separately. This makes a per-workflow cost
estimate dependent on the chosen orchestration, knowledge, tools, and model
calls.

For the example considered here:

- **Choose Rovo Studio** when Jira and Confluence are the center of gravity.
- **Choose Copilot Studio** when Microsoft 365, Power Platform, and explicit
  human-approval flows are the center of gravity, while Jira is one connected
  destination.
- **Choose Gemini Enterprise Agent Platform** when P needs a broader
  developer platform with custom runtimes, heterogeneous engineering services,
  and greater freedom over agent frameworks and models.

Amazon Web Services, Salesforce, and ServiceNow were identified as other
comparable platform families but were not yet examined in the discussion.

## Sources

- [What's new in Gemini Enterprise Agent Platform](https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise-agent-platform)
- [Gemini Enterprise Agent Platform overview](https://cloud.google.com/products/gemini-enterprise-agent-platform)
- [Agent Runtime](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime)
- [Agent Runtime contract](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/runtime-contract)
- [Register external A2A agents](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-a2a-agent)
- [Claude models on Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude)
- [Self-deployed models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/self-deployed-models)
- [Agent Platform infrastructure pricing](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing)
- [Agent Platform model pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)
- [Gemini Enterprise app and seat pricing](https://cloud.google.com/gemini-enterprise)
- [OpenAI Codex SDK](https://learn.chatgpt.com/docs/codex-sdk)
- [Codex as an MCP server](https://learn.chatgpt.com/docs/mcp-server)
- [Atlassian Rovo agents](https://support.atlassian.com/rovo/docs/agents/)
- [Rovo agents in automation](https://support.atlassian.com/rovo/docs/agents-in-automations/)
- [Rovo actions](https://developer.atlassian.com/platform/forge/manifest-reference/modules/rovo-action/)
- [Rovo Studio](https://www.atlassian.com/software/rovo/studio)
- [Microsoft Copilot Studio overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio)
- [Human review in Copilot Studio agent flows](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-request-for-information)
- [Call an agent flow from an agent](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-use-flow)
- [Microsoft Jira connector](https://learn.microsoft.com/en-us/connectors/jira/)
- [Bring a Microsoft Foundry model into a prompt](https://learn.microsoft.com/en-us/microsoft-copilot-studio/bring-your-own-model-prompts)
- [Microsoft Copilot Studio pricing](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing/copilot-studio)
