# Agent Operations Gets Its Control Plane

**Coverage:** 2026-07-24–2026-07-30 (Europe/Stockholm)

## Executive Brief

Grafana used two consecutive AI Week releases to move agent operations from reactive troubleshooting toward autonomous investigation, scheduled automation, continuous watching, observability, and natural-language testing.
Grafana 在 AI Week 连续两天的发布中，将智能体运维从被动故障排查推进到自主调查、定时自动化、持续监控、可观测性和自然语言测试。

At the same time, AWS and GitHub closed or froze older AI-building paths, making migration planning part of the agent-platform lifecycle rather than an optional cleanup task.
与此同时，AWS 和 GitHub 关闭或冻结了较旧的 AI 构建路径，使迁移规划成为智能体平台生命周期的一部分，而不再只是可选的清理工作。

## AI Tools

<a id="story-grafana-autonomous-operations"></a>

### Grafana ships autonomous investigations, automations, and telemetry watchers

- [ ] Interesting

**Underlying event date:** 2026-07-29

**What happened**

On July 29, Grafana made Assistant Investigations and Automations generally available and put Assistant Watchers into public preview, giving its AI agents parallel incident analysis, scheduled prompt execution, and always-on telemetry monitoring.
7 月 29 日，Grafana 正式发布 Assistant Investigations 和 Automations，并将 Assistant Watchers 推入公开预览，使其 AI 智能体具备并行事件分析、定时提示词执行和持续遥测监控能力。

**Why it matters**

The release addresses the operational gap between an agent that can answer questions and one that can repeatedly inspect production systems, surface problems, and leave an auditable conversation for each run.
该版本弥合了“能回答问题的智能体”与“能反复检查生产系统、主动暴露问题，并为每次运行留下可审计对话记录的智能体”之间的运维差距。

**Sources:** [Grafana Labs AI Week — Operations and maintenance](https://grafana.ai/events/ai-week#operations-and-maintenance)

<a id="story-grafana-agent-observability-testing"></a>

### Grafana makes agent observability generally available and previews natural-language k6 testing

- [ ] Interesting

**Underlying event date:** 2026-07-30

**What happened**

On July 30, Grafana made Agent Observability generally available for tracing conversations, costs, behavior, and output quality, while placing k6 agentic testing—plain-language user journeys converted into runnable browser tests—into public preview.
7 月 30 日，Grafana 正式发布 Agent Observability，用于追踪对话、成本、行为和输出质量；同时将 k6 智能体测试推入公开预览，可把自然语言用户旅程转换为可运行的浏览器测试。

**Why it matters**

The pair gives practitioners a tighter build-measure-test loop for production agents by connecting runtime evidence with repeatable end-user validation.
这组功能把运行时证据与可重复的终端用户验证连接起来，为生产智能体提供了更紧密的“构建—度量—测试”闭环。

**Sources:** [Grafana Labs AI Week — Trust and evaluation](https://grafana.ai/events/ai-week#trust-and-evaluation)

<a id="story-aws-bedrock-agents-classic-maintenance"></a>

### AWS moves Bedrock Agents Classic into maintenance mode

- [ ] Interesting

**Underlying event date:** 2026-07-30

**What happened**

On July 30, AWS stopped opening Bedrock Agents Classic to new customers, froze its model catalog, and directed new and migrating workloads toward AgentCore's managed harness or code-defined agent runtime.
7 月 30 日，AWS 停止向新客户开放 Bedrock Agents Classic，冻结其模型目录，并引导新建和迁移中的工作负载转向 AgentCore 的托管式执行框架或代码定义智能体运行时。

**Why it matters**

Teams must now treat orchestration-platform migration as active architecture work, especially where agents depend on memory, identity, observability, human approval, sandboxed execution, or MCP-wrapped tools.
团队现在必须把编排平台迁移视为主动的架构工作，尤其是当智能体依赖记忆、身份、可观测性、人工审批、沙箱执行或 MCP 封装工具时。

**Sources:** [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-classic-maintenance-mode.html)

<a id="story-github-models-retirement"></a>

### GitHub fully retires its Models playground and inference API

- [ ] Interesting

**Underlying event date:** 2026-07-30

**What happened**

On July 30, GitHub fully retired GitHub Models, removing its playground, model catalog, inference API, and bring-your-own-key endpoints for all remaining customers.
7 月 30 日，GitHub 全面退役 GitHub Models，面向所有剩余客户移除其游乐场、模型目录、推理 API 和自带密钥端点。

**Why it matters**

Agent builders using GitHub-hosted model experimentation or inference need an explicit replacement path, with GitHub pointing workflow users toward Copilot and broader model access toward Microsoft Foundry.
使用 GitHub 托管模型实验或推理的智能体构建者需要明确的替代路径；GitHub 将工作流用户引向 Copilot，将更广泛的模型访问需求引向 Microsoft Foundry。

**Sources:** [GitHub Changelog](https://github.blog/changelog/2026-07-01-github-models-is-being-fully-retired-on-july-30-2026/)

<a id="story-github-copilot-jetbrains-agent-controls"></a>

### GitHub adds agent telemetry, MCP, and model controls to Copilot for JetBrains

- [ ] Interesting

**Underlying event date:** 2026-07-27

**What happened**

On July 27, GitHub updated Copilot for JetBrains with OpenTelemetry export for agent workflows, token and model controls, MCP servers and custom agents inside Claude agent flows, and richer Copilot CLI sessions.
7 月 27 日，GitHub 更新了 JetBrains 版 Copilot，加入智能体工作流的 OpenTelemetry 导出、token 与模型控制、Claude 智能体流程内的 MCP 服务器和自定义智能体，以及更丰富的 Copilot CLI 会话能力。

**Why it matters**

The release puts observability, cost limits, specialized tools, and reusable agent configurations closer to the IDE where practitioners diagnose and govern long-running coding work.
该版本把可观测性、成本限制、专用工具和可复用智能体配置带到更靠近 IDE 的位置，便于从业者诊断和治理长时间运行的编码工作。

**Sources:** [GitHub Changelog](https://github.blog/changelog/2026-07-27-github-copilot-for-jetbrains-adds-improvved-opentelemetry-configuration-and-model-management/)

<a id="story-github-copilot-managed-agent-settings"></a>

### GitHub extends enterprise guardrails to the Copilot app and cloud agent

- [ ] Interesting

**Underlying event date:** 2026-07-27

**What happened**

On July 27, GitHub made enterprise `managed-settings.json` policies apply to the Copilot app and Copilot cloud agent, covering approved plugins, marketplaces, prompt bypass rules, and default model selection.
7 月 27 日，GitHub 将企业级 `managed-settings.json` 策略扩展到 Copilot 应用和 Copilot 云端智能体，覆盖获批插件、插件市场、提示绕过规则和默认模型选择。

**Why it matters**

Central policy now follows agent work across more execution surfaces, reducing the chance that a cloud task or desktop app silently escapes the controls already enforced in CLI and VS Code workflows.
集中式策略现在可跨更多执行界面跟随智能体工作，从而降低云端任务或桌面应用悄然绕过 CLI 和 VS Code 工作流既有控制的风险。

**Sources:** [GitHub Changelog](https://github.blog/changelog/2026-07-27-enterprise-managed-settings-now-apply-to-the-github-copilot-app/)

## Other AI Stories

<a id="story-dxc-elevenlabs-enterprise-voice"></a>

### DXC and ElevenLabs partner on enterprise voice agents

- [ ] Interesting

**Underlying event date:** 2026-07-28

**What happened**

On July 28, DXC announced a partnership to embed ElevenLabs voice AI into its internal operations and customer offerings, alongside DXC's participation in ElevenLabs' recent $500 million Series D at an approximately $11 billion valuation.
7 月 28 日，DXC 宣布建立合作关系，把 ElevenLabs 语音 AI 嵌入其内部运营和客户产品；DXC 同时披露参与了 ElevenLabs 近期 5 亿美元的 D 轮融资，该公司估值约为 110 亿美元。

**Why it matters**

The deal tests whether multilingual voice agents can move from contact-center demos into mission-critical service desks, training, knowledge management, and industry workflows at global-enterprise scale.
该合作将检验多语言语音智能体能否从联络中心演示走向全球企业规模的关键服务台、培训、知识管理和行业工作流。

**Sources:** [DXC Technology via PR Newswire](https://www.prnewswire.com/news-releases/dxc-and-elevenlabs-announce-strategic-partnership-to-scale-enterprise-ai-and-voice-innovation-302835510.html)

<a id="story-fractureagent-rehabilitation-research"></a>

### FractureAgent coordinates five rehabilitation tools behind a deterministic safety gate

- [ ] Interesting

**Underlying event date:** 2026-07-28

**What happened**

Published on July 28, FractureAgent combines a QLoRA-adapted Qwen3.5-9B model, five typed rehabilitation tools, and a deterministic safety gate, reaching 91.4% task completion across 210 simulated-patient scenarios.
7 月 28 日发表的 FractureAgent 将经 QLoRA 适配的 Qwen3.5-9B 模型、五种类型化康复工具和确定性安全门组合起来，在 210 个模拟患者场景中达到 91.4% 的任务完成率。

**Why it matters**

The study offers a concrete pattern for separating probabilistic planning from hard safety escalation, but its simulated evaluation does not establish clinical effectiveness or deployment readiness.
该研究给出了将概率式规划与硬性安全升级机制分离的具体模式，但其模拟评估尚不能证明临床有效性或部署就绪度。

**Sources:** [Scientific Reports](https://www.nature.com/articles/s41598-026-63557-1)

<a id="story-clinical-encoder-outperforms-llms"></a>

### A domain-specific encoder beats larger LLMs on clinical text extraction

- [ ] Interesting

**Underlying event date:** 2026-07-28

**What happened**

Published on July 28, a 20-report proof-of-concept benchmark found MediAlbertina-1.5B achieved a micro-F1 of 0.430 versus no more than 0.123 for the tested quantized Llama variants, which also ran 23–95 times longer on the study's local CPU setup.
7 月 28 日发表的一项 20 份报告概念验证基准发现，MediAlbertina-1.5B 的 micro-F1 达到 0.430，而测试中的量化 Llama 变体最高不超过 0.123；在该研究的本地 CPU 配置上，后者运行时间还长 23 至 95 倍。

**Why it matters**

The result is a useful warning against defaulting to general LLMs for structured extraction when a smaller domain model may be faster, cheaper, more private, and more accurate, though the tiny benchmark limits generalization.
这一结果提醒人们：在结构化抽取任务中，不应默认采用通用大模型，因为更小的领域模型可能更快、更便宜、更保护隐私且更准确；不过，极小的基准规模限制了结论的泛化。

**Sources:** [Scientific Reports](https://www.nature.com/articles/s41598-026-62884-7)

<a id="story-stpa-clinician-ai-safety-guidelines"></a>

### STPA turns clinician–AI hazards into traceable interface safety rules

- [ ] Interesting

**Underlying event date:** 2026-07-29

**What happened**

Published on July 29, researchers applied System-Theoretic Process Analysis to clinician–AI interaction, deriving traceable design guidelines for explanation clarity, system status, on-demand clarification, calibrated trust, cross-method consistency, and cognitive load.
7 月 29 日发表的一项研究将系统理论过程分析应用于临床医生与 AI 的交互，推导出可追踪的设计指南，涵盖解释清晰度、系统状态、按需澄清、校准信任、跨方法一致性和认知负荷。

**Why it matters**

The work shows how formal safety analysis can translate broad AI-risk concerns into unsafe control actions, constraints, measurable explanation checks, and concrete interface requirements.
该研究展示了形式化安全分析如何把宽泛的 AI 风险关切转化为不安全控制动作、约束、可度量的解释检查和具体界面要求。

**Sources:** [Scientific Reports](https://www.nature.com/articles/s41598-026-64180-w)

## Follow-ups to Interesting Stories

No tracked story had a distinct, meaningful in-window event that passed the date and evidence gates.
本期没有任何已跟踪故事出现通过日期与证据门槛的、独立且有实质意义的窗口内新事件。

## Tracked Interests

- **[NVIDIA releases Cosmos 3 Edge for local physical AI](2026-07-24-ai-newsletter.md#story-nvidia-cosmos-3-edge-siggraph)** — Marked 2026-07-24. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[OpenAI rolls out Health in ChatGPT to U.S. users](2026-07-27-ai-newsletter.md#story-chatgpt-health-rollout)** — Marked 2026-07-27. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[月之暗面正式开源 Kimi K3](2026-07-29-ai-newsletter.md#story-kimi-k3-open-source)** — Marked 2026-07-29. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[Reader spotlight: SpecForge pairs LLMs with formal specifications](2026-07-29-ai-newsletter.md#story-imiron-specforge-ai-formal-specs)** — Marked 2026-07-29. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.

## Watch Next Week

Watch whether teams respond to the July 30 AWS and GitHub cutovers with concrete migration tooling, and whether Grafana's newly released agent telemetry produces reproducible evaluation workflows rather than another disconnected dashboard.
下周可关注团队是否会针对 7 月 30 日 AWS 与 GitHub 的切换推出具体迁移工具，以及 Grafana 新发布的智能体遥测能力能否形成可复现的评估工作流，而不是又一个孤立仪表板。

## Sources

- [EN] [Grafana Labs AI Week — Operations and maintenance](https://grafana.ai/events/ai-week#operations-and-maintenance)
- [EN] [Grafana Labs AI Week — Trust and evaluation](https://grafana.ai/events/ai-week#trust-and-evaluation)
- [EN] [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-classic-maintenance-mode.html)
- [EN] [GitHub Changelog — GitHub Models retirement](https://github.blog/changelog/2026-07-01-github-models-is-being-fully-retired-on-july-30-2026/)
- [EN] [GitHub Changelog — Copilot for JetBrains](https://github.blog/changelog/2026-07-27-github-copilot-for-jetbrains-adds-improvved-opentelemetry-configuration-and-model-management/)
- [EN] [GitHub Changelog — enterprise managed settings](https://github.blog/changelog/2026-07-27-enterprise-managed-settings-now-apply-to-the-github-copilot-app/)
- [EN] [DXC Technology via PR Newswire](https://www.prnewswire.com/news-releases/dxc-and-elevenlabs-announce-strategic-partnership-to-scale-enterprise-ai-and-voice-innovation-302835510.html)
- [EN] [Scientific Reports — FractureAgent](https://www.nature.com/articles/s41598-026-63557-1)
- [EN] [Scientific Reports — clinical model benchmark](https://www.nature.com/articles/s41598-026-62884-7)
- [EN] [Scientific Reports — clinician–AI safety guidelines](https://www.nature.com/articles/s41598-026-64180-w)
