# AI Agents Learn to Last, Prove, and Stay Contained

**Coverage:** 2026-07-30–2026-08-05 (Europe/Stockholm)

## Executive Brief

LongHorizon-Harness reported large gains on extended computer-use tasks by separating agent planning, execution, and auditing, while four newly released projects turned persistent runtimes, cyber evaluation, containment, and shared security findings into concrete agent infrastructure.
LongHorizon-Harness 报告称，通过分离智能体的规划、执行与审计，它在长时程计算机使用任务上取得了显著提升；与此同时，四个新发布的项目把持久化运行时、网络安全评测、隔离约束和共享安全发现转化为具体的智能体基础设施。

SaferAI's evaluation of GLM-5.2 found open-weight capability nearing the frontier without comparable built-in safeguards, as capital and infrastructure continued flowing into human-ranked model evaluation and portable inference capacity.
SaferAI 对 GLM-5.2 的评测发现，开放权重模型的能力正接近前沿水平，但其内置安全防护并未同步跟上；与此同时，资金和基础设施继续流向基于人工排序的模型评测与便携式推理算力。

## AI Tools

<a id="story-longhorizon-harness"></a>

### LongHorizon-Harness gives computer-use agents a manager, executor, and auditor

- [X] Interesting

**Underlying event date:** 2026-08-03

**What happened**

On August 3, AMAP-ML published LongHorizon-Harness, a stateful execution and verification framework whose reported results raised Qwen 3.7-Plus with Claude Code from 51.8% to 80.7% pass rate on WeaveBench and improved Terminal-Bench success from 69.7% to 77.2% with 24% fewer tokens.
8 月 3 日，AMAP-ML 发布了 LongHorizon-Harness，这是一个带状态的执行与验证框架；据其报告，Qwen 3.7-Plus 配合 Claude Code 在 WeaveBench 上的通过率从 51.8% 提升至 80.7%，在 Terminal-Bench 上的成功率从 69.7% 提升至 77.2%，同时减少了 24% 的 token 用量。

**Why it matters**

The manager–executor–auditor split directly targets planning drift, lost state, and unverifiable completion in long-running GUI and terminal agents.
管理器、执行器与审计器的分工直接针对长时间运行的图形界面和终端智能体中的规划漂移、状态丢失与完成结果不可验证问题。

**Sources:** [arXiv paper](https://arxiv.org/abs/2608.01964) · [GitHub repository](https://github.com/AMAP-ML/LongHorizon-Harness)

<a id="story-nullspace-agent-runtime"></a>

### Nullspace packages persistent agent machines behind one runtime

- [ ] Interesting

**Underlying event date:** 2026-08-04

**What happened**

On August 4, Nullspace released an early open-source runtime that lets agents create, hibernate, resume, and fork Firecracker-backed machines through Python, TypeScript, CLI, MCP, or HTTPS interfaces.
8 月 4 日，Nullspace 发布了一个早期的开源运行时，使智能体能够通过 Python、TypeScript、CLI、MCP 或 HTTPS 接口创建、休眠、恢复和分叉由 Firecracker 支撑的机器。

**Why it matters**

Persistent isolated machines, external credential brokering, and egress controls address the continuity and least-privilege problems that appear when agents execute work across many sessions.
持久化隔离机器、外部凭据代理与出站流量控制，解决了智能体跨多个会话执行工作时出现的连续性与最小权限问题。

**Sources:** [Nullspace GitHub repository](https://github.com/ns-rocks/nullspace)

<a id="story-xorcise-cyber-agent-evals"></a>

### XORCISE turns cyber-agent activity into replayable evaluation evidence

- [ ] Interesting

**Underlying event date:** 2026-08-03

**What happened**

On August 3, XORCISE released an open-source harness that runs cyber-AI agents against live missions in contained environments, records their commands and tool calls as OpenTelemetry traces, and grades the resulting evidence against each mission.
8 月 3 日，XORCISE 发布了一个开源工具，它让网络安全 AI 智能体在受控环境中执行真实任务，将命令和工具调用记录为 OpenTelemetry 轨迹，并依据每项任务对所得证据进行评分。

**Why it matters**

Capturing successful steps, dead ends, and tool use makes high-risk cyber-agent behavior inspectable instead of reducing evaluation to a final-answer score.
记录成功步骤、无效路径与工具使用情况，使高风险网络安全智能体的行为可以被检查，而不是把评测简化为最终答案得分。

**Sources:** [XORCISE GitHub repository](https://github.com/xorcise-ai/xorcise)

<a id="story-custody-agent-containment"></a>

### CUSTODY moves agent containment out of prompts and into infrastructure

- [ ] Interesting

**Underlying event date:** 2026-08-03

**What happened**

On August 3, the CUSTODY project released an Apache-2.0 framework for classifying agent authority by level, mandate, and reach, with containment enforced at infrastructure boundaries the agent cannot modify.
8 月 3 日，CUSTODY 项目发布了一个采用 Apache-2.0 许可证的框架，按层级、授权范围与可达范围对智能体权限进行分类，并在智能体无法修改的基础设施边界上实施隔离约束。

**Why it matters**

Separating authority controls from model instructions gives practitioners a vendor-neutral way to reason about delegation and limit blast radius when an agent fails or is compromised.
将权限控制与模型指令分离，为从业者提供了一种厂商中立的方法，用于推理委托关系，并在智能体失效或遭入侵时限制影响范围。

**Sources:** [CUSTODY GitHub repository](https://github.com/malwarejake/CUSTODY-framework)

<a id="story-superblocks-aws-private-vibe-coding"></a>

### Superblocks and AWS bring AI app building inside customer clouds

- [ ] Interesting

**Underlying event date:** 2026-08-03

**What happened**

On August 3, Superblocks and AWS announced a joint marketing agreement under which Superblocks can run inside an AWS customer's private cloud, connect generated applications to Aurora and Bedrock, and keep application data within that environment.
8 月 3 日，Superblocks 与 AWS 宣布达成联合营销协议，使 Superblocks 能够在 AWS 客户的私有云中运行，将生成的应用连接到 Aurora 和 Bedrock，并让应用数据保留在该环境内。

**Why it matters**

Putting AI-assisted application generation behind an enterprise's existing identity, network, and audit controls reduces the governance gap between prototyping and production deployment.
把 AI 辅助应用生成置于企业现有的身份、网络与审计控制之后，可缩小原型开发与生产部署之间的治理差距。

**Sources:** [TechCrunch](https://techcrunch.com/2026/08/03/aws-is-helping-vibe-coding-startup-superblocks-and-the-implications-are-big/) · [Superblocks](https://www.superblocks.com/)

<a id="story-safe-ai-security-rfc"></a>

### SAFE proposes a shared incident language for AI security

- [ ] Interesting

**Underlying event date:** 2026-08-04

**What happened**

On August 4, the Open Source Security Foundation's Open Secure AI Alliance published an RFC for the Shared AI Findings Exchange, a proposed confidential process for reporting incidents and near misses, notifying affected parties, and conducting structured full-stack reviews.
8 月 4 日，Open Source Security Foundation 旗下的 Open Secure AI Alliance 发布了“共享 AI 发现交换”RFC，提出一套保密流程，用于报告事故与险情、通知受影响方并开展结构化的全栈审查。

**Why it matters**

A common, blame-free findings process could convert isolated failures into reusable tests, policies, detection rules, and reference configurations across the agent ecosystem.
一种通用且非归责式的发现流程，有望把孤立故障转化为可在智能体生态中复用的测试、策略、检测规则与参考配置。

**Sources:** [Linux Foundation](https://www.linuxfoundation.org/blog/proposing-the-safe-working-group-an-open-community-effort-to-improve-ai-security)

## Other AI Stories

<a id="story-glm-52-risk-evaluation"></a>

### SaferAI finds GLM-5.2's capabilities advancing faster than its safeguards

- [ ] Interesting

**Underlying event date:** 2026-08-02

**What happened**

On August 2, SaferAI published a preliminary independent evaluation finding GLM-5.2 roughly two to four months behind frontier models across selected loss-of-control, cyber, biological, and manipulation tests, while noting that the open-weight model refused none of its offensive-security or biological tasks.
8 月 2 日，SaferAI 发布了一份初步独立评测，发现 GLM-5.2 在选定的失控、网络安全、生物与操纵测试中大约落后前沿模型两到四个月，同时指出这款开放权重模型没有拒绝任何进攻性安全或生物任务。

**Why it matters**

The report does not make an overall risk judgment, but it sharpens the concern that removable safeguards can leave open-weight capability gains exposed to misuse.
该报告没有作出总体风险判断，但进一步凸显了一个问题：可移除的安全防护可能让开放权重模型的能力提升更容易被滥用。

**Sources:** [SaferAI](https://www.safer-ai.org/research/glm-5-2-evaluation-report) · [TechCrunch](https://techcrunch.com/2026/08/04/open-weight-ai-models-are-catching-up-to-the-frontier-the-safety-gap-remains/)

<a id="story-design-arena-seed-round"></a>

### Design Arena raises $7.9 million to turn human taste into model feedback

- [ ] Interesting

**Underlying event date:** 2026-08-03

**What happened**

On August 3, Intelligence announced a $7.9 million seed round led by Index Ventures for Design Arena, whose side-by-side human voting system ranks AI-generated designs and produces preference data for media models.
8 月 3 日，Intelligence 宣布为 Design Arena 完成由 Index Ventures 领投的 790 万美元种子轮融资；该平台通过人类对 AI 生成设计进行两两投票来排名，并为媒体模型生成偏好数据。

**Why it matters**

The funding reflects growing commercial value in evaluation systems that capture subjective human judgment where automated benchmarks are weakest.
这笔融资反映出，在自动化基准最薄弱的主观判断领域，能够采集人类偏好的评测系统正获得更高的商业价值。

**Sources:** [TechCrunch](https://techcrunch.com/2026/08/03/designarena-creators-raise-7-9-million-to-bring-taste-to-ai-models/) · [Design Arena](https://www.designarena.ai/)

<a id="story-runware-sonic-inference-pod"></a>

### Runware puts AI inference capacity into a portable pod

- [ ] Interesting

**Underlying event date:** 2026-08-04

**What happened**

On August 4, Runware introduced the Sonic Inference Pod, a portable modular data-center unit with closed-loop waterless cooling that the company says can add inference capacity across sites in the United States, Europe, and Asia-Pacific.
8 月 4 日，Runware 推出了 Sonic Inference Pod，这是一种采用闭环无水冷却的便携式模块化数据中心单元；该公司称，它可以在美国、欧洲与亚太地区的站点增加推理算力。

**Why it matters**

Deployable capacity closer to users could reduce inference latency and shorten infrastructure lead times, although the operating and economic claims still need proof at scale.
把可部署算力放到更靠近用户的位置，可能降低推理延迟并缩短基础设施交付周期，但其运营与经济性主张仍需通过规模化实践验证。

**Sources:** [TechCrunch](https://techcrunch.com/2026/08/04/is-the-future-of-data-centers-portable-runware-builds-a-pod-to-find-out/)

<a id="story-apple-openai-trade-secrets-escalation"></a>

### Apple broadens its trade-secret allegations involving former employees at OpenAI

- [ ] Interesting

**Underlying event date:** 2026-08-04

**What happened**

On August 4, Apple sought a preliminary injunction and expedited discovery after alleging that its investigation had identified 11 additional former employees who may be witnesses or involved in transferring confidential information to OpenAI, which disputed the request and said it neither has nor wants Apple's secrets.
8 月 4 日，Apple 在声称其调查发现另外 11 名前员工可能是证人或涉及向 OpenAI 转移机密信息后，申请了初步禁令与加速证据开示；OpenAI 对该请求提出异议，并表示自己既未持有也不希望获得 Apple 的秘密。

**Why it matters**

The dispute shows how competition for AI talent can turn employee mobility, data handling, and model-development provenance into material legal and operational risks.
这场争议表明，围绕 AI 人才的竞争可能把员工流动、数据处理与模型开发来源转化为实质性的法律和运营风险。

**Sources:** [TechCrunch](https://techcrunch.com/2026/08/04/apple-says-more-ex-employees-may-have-taken-confidential-data-to-openai/)

## Follow-ups to Interesting Stories

No tracked story produced a qualifying new event inside this edition's window.
本期追踪的故事均未在报道窗口内出现符合条件的新事件。

## Tracked Interests

- **[NVIDIA releases Cosmos 3 Edge for local physical AI](2026-07-24-ai-newsletter.md#story-nvidia-cosmos-3-edge-siggraph)** — Marked 2026-07-24. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[OpenAI rolls out Health in ChatGPT to U.S. users](2026-07-27-ai-newsletter.md#story-chatgpt-health-rollout)** — Marked 2026-07-27. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[月之暗面正式开源 Kimi K3](2026-07-29-ai-newsletter.md#story-kimi-k3-open-source)** — Marked 2026-07-29. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[Reader spotlight: SpecForge pairs LLMs with formal specifications](2026-07-29-ai-newsletter.md#story-imiron-specforge-ai-formal-specs)** — Marked 2026-07-29. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[LangSmith LLM Gateway enters public beta as a runtime control plane](2026-07-31-ai-newsletter.md#story-langsmith-llm-gateway-public-beta)** — Marked 2026-07-31. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[Deep Agents v0.7 cuts base input tokens by 65%](2026-07-31-ai-newsletter.md#story-deep-agents-v07-token-diet)** — Marked 2026-07-31. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[BrowserStack puts an agentic testing harness inside the IDE](2026-07-31-ai-newsletter.md#story-browserstack-test-companion-ide)** — Marked 2026-07-31. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[herdr 0.8.0 relicenses to Apache-2.0 and cuts multi-client CPU by 95%](2026-08-04-ai-newsletter.md#story-herdr-v080-agent-multiplexer)** — Marked 2026-08-04. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[OpenAI introduces Astra with ten Lean-certified mathematical results](2026-08-04-ai-newsletter.md#story-openai-astra-lean-certified-proofs)** — Marked 2026-08-04. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.

## Watch Next Week

Watch whether SAFE's draft RFC becomes concrete machine-readable policies and tests, and whether LongHorizon-Harness's benchmark gains reproduce outside its published setup.
下周值得关注的是，SAFE 的 RFC 草案是否会转化为具体的机器可读策略与测试，以及 LongHorizon-Harness 的基准提升能否在其公布的实验设置之外复现。

## Sources

- [EN] [LongHorizon-Harness paper](https://arxiv.org/abs/2608.01964)
- [EN] [Nullspace repository](https://github.com/ns-rocks/nullspace)
- [EN] [XORCISE repository](https://github.com/xorcise-ai/xorcise)
- [EN] [CUSTODY repository](https://github.com/malwarejake/CUSTODY-framework)
- [EN] [TechCrunch — Superblocks and AWS](https://techcrunch.com/2026/08/03/aws-is-helping-vibe-coding-startup-superblocks-and-the-implications-are-big/)
- [EN] [Linux Foundation — SAFE working group RFC](https://www.linuxfoundation.org/blog/proposing-the-safe-working-group-an-open-community-effort-to-improve-ai-security)
- [EN] [SaferAI — GLM-5.2 evaluation](https://www.safer-ai.org/research/glm-5-2-evaluation-report)
- [EN] [TechCrunch — Design Arena funding](https://techcrunch.com/2026/08/03/designarena-creators-raise-7-9-million-to-bring-taste-to-ai-models/)
- [EN] [TechCrunch — Runware Sonic Inference Pod](https://techcrunch.com/2026/08/04/is-the-future-of-data-centers-portable-runware-builds-a-pod-to-find-out/)
- [EN] [TechCrunch — Apple and OpenAI dispute](https://techcrunch.com/2026/08/04/apple-says-more-ex-employees-may-have-taken-confidential-data-to-openai/)
