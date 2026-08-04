# Agent Evaluation Leaves the Toy Box

**Coverage:** 2026-07-28–2026-08-03 (Europe/Stockholm)

## Executive Brief

Agent evaluation became strikingly more operational this week, with new benchmarks for patient-facing care, post-compromise incident response, stateful personal assistants, and open-ended AI research.
本周，智能体评估明显走向实际运用，新基准覆盖了患者面向型医疗、入侵后事件响应、有状态个人助理与开放式 AI 研究。

At the deployment edge, Microsoft's Project Perception entered public preview on August 3, while the EU's Article 50 transparency rules became applicable on August 2 for chatbots and synthetic media.
在部署前沿，微软 Project Perception 于 8 月 3 日进入公开预览；欧盟《人工智能法案》第 50 条针对聊天机器人与合成媒体的透明度义务则于 8 月 2 日开始适用。

## AI Tools

<a id="story-microsoft-project-perception-preview"></a>

### Microsoft opens Project Perception's closed-loop cyber defense to public preview

- [ ] Interesting

**Underlying event date:** 2026-08-03

**What happened**

On August 3, Microsoft put Project Perception into public preview, combining red-team, blue-team, and green-team agents with security context, multiple models, a coordination harness, and product actuators in a continuous defense loop.
8 月 3 日，微软将 Project Perception 推入公开预览，把红队、蓝队与绿队智能体同安全上下文、多模型、协调框架及产品执行器整合到一个持续防御闭环中。

**Why it matters**

Security operators can now evaluate an agent system designed to carry findings through prioritization and remediation while keeping human control in the loop, rather than stopping at alert generation.
安全运营团队现在可以评估一套能将发现继续推进到优先级判定与修复、同时保留人类控制权的智能体系统，而不再止步于生成告警。

**Sources:** [Microsoft](https://blogs.microsoft.com/blog/2026/07/27/rethinking-security-for-the-age-of-ai/)

<a id="story-patientagentbench-health-agent-evaluation"></a>

### PatientAgentBench tests health agents in sustained, tool-using conversations

- [ ] Interesting

**Underlying event date:** 2026-07-28

**What happened**

On July 28, researchers released PatientAgentBench, a reproducible framework that evaluates models as patient-facing agents across 1,200 simulated scenarios, sandboxed healthcare tools, and more than 100 clinician-grounded criteria.
7 月 28 日，研究人员发布了 PatientAgentBench，这是一个可复现的框架，通过 1,200 个模拟场景、沙箱化医疗工具与 100 多项临床依据准则，将模型作为患者面向型智能体进行评估。

**Why it matters**

Teams building health agents gain a test harness that exposes triage mistakes, fabricated actions, and failures around unverified tool output that static medical question-answer benchmarks miss.
构建医疗智能体的团队获得了一套测试框架，可暴露静态医疗问答基准难以发现的分诊错误、虚构执行动作，以及未验证工具输出导致的失败。

**Sources:** [arXiv — PatientAgentBench](https://arxiv.org/abs/2607.25485)

<a id="story-secrespond-post-compromise-benchmark"></a>

### SecRespond benchmarks agents after the attacker is already inside

- [ ] Interesting

**Underlying event date:** 2026-07-29

**What happened**

On July 29, the SecRespond team published a benchmark built from 10 compromised cloud-host cyber ranges across five operating systems and evaluated 23 frontier models through the OpenCode agent harness.
7 月 29 日，SecRespond 团队发布了一套基准，其基于覆盖五种操作系统的 10 个已被入侵云主机网络靶场，并通过 OpenCode 智能体框架评估了 23 个前沿模型。

**Why it matters**

Incident-response agent builders can now test proactive forensic discovery and verified remediation planning, two areas where the paper found every evaluated model incomplete.
事件响应智能体的构建者现在可以测试主动取证发现与经验证的修复规划，论文发现所有受测模型在这两方面都不完整。

**Sources:** [arXiv — SecRespond](https://arxiv.org/abs/2607.26791)

<a id="story-pause-stateful-assistant-benchmark"></a>

### PAUSE makes agent evaluation stateful, permission-aware, and multi-service

- [ ] Interesting

**Underlying event date:** 2026-07-29

**What happened**

On July 29, researchers introduced PAUSE, a benchmark that evaluates personal assistants across persistent user state, heterogeneous services, simulated user interaction, authorization constraints, and both semantic and deterministic scoring regimes.
7 月 29 日，研究人员推出了 PAUSE，该基准从持久用户状态、异构服务、模拟用户交互、授权约束，以及语义与确定性评分机制等方面评估个人助理。

**Why it matters**

Practitioners get a more realistic way to catch agents that complete an isolated tool call but lose user configuration, violate permissions, or drift during a long multi-service task.
从业者获得了一种更贴近现实的检测方式，能捕捉那些虽然完成单次工具调用，却丢失用户配置、违反权限或在长周期多服务任务中偏离目标的智能体。

**Sources:** [arXiv — PAUSE](https://arxiv.org/abs/2607.27354)

<a id="story-shadow-evaluations-ai-research-agents"></a>

### Shadow evaluations put AI research agents in front of the original authors

- [ ] Interesting

**Underlying event date:** 2026-07-29

**What happened**

On July 29, a 24-author team released a shadow-evaluation method plus expert reviews, surveys, agent repositories, and logs from two six-day attempts to reproduce the central research contribution of unpublished NeurIPS papers.
7 月 29 日，一支由 24 名作者组成的团队发布了“影子评估”方法，并公开了两次为期六天、尝试复现未发表 NeurIPS 论文核心研究贡献的专家评审、问卷、智能体仓库与日志。

**Why it matters**

AI-lab operators gain an auditable evaluation pattern for open-ended research agents that measures scientific judgment, backtracking, resource awareness, and instruction fidelity rather than only engineering completion.
AI 实验室运营者因此获得了一种可审计的开放式研究智能体评估模式，它测量科学判断、回退能力、资源感知与指令忠实度，而非只看工程任务是否完成。

**Sources:** [arXiv — Shadow evaluations](https://arxiv.org/abs/2607.27191)

## Other AI Stories

<a id="story-eu-ai-act-article-50-transparency"></a>

### EU AI Act transparency duties start applying while high-risk rules wait

- [ ] Interesting

**Underlying event date:** 2026-08-02

**What happened**

On August 2, the EU AI Act's Article 50 transparency duties began applying to chatbot disclosure, synthetic-content marking, deepfake labelling, emotion recognition, and biometric categorization, while the amended timetable deferred the heavier high-risk-system obligations.
8 月 2 日，欧盟《人工智能法案》第 50 条的透明度义务开始适用，涵盖聊天机器人告知、合成内容标记、深度伪造标注、情绪识别与生物特征分类，而修订后的时间表推迟了更严格的高风险系统义务。

**Why it matters**

AI product teams serving Europe now face live disclosure and labelling engineering work even though many older compliance plans incorrectly assume that the broader high-risk delay moved the transparency deadline too.
服务欧洲市场的 AI 产品团队现在必须实际完成告知与标注工程，尽管许多旧版合规计划误以为范围更广的高风险义务延期也同时推迟了透明度截止日期。

**Sources:** [AP](https://apnews.com/article/eu-ai-regulation-deepfakes-hacking-f4fcee1f9750e2b32cdf26ad73ee5ec2) · [European Express](https://www.european.express/2026/07/17/eu-ai-act-what-actually-applies-on-2-august-2026/)

<a id="story-drivecentric-service-to-sales-ga"></a>

### DriveCentric's Service-to-Sales Agent reaches general availability

- [ ] Interesting

**Underlying event date:** 2026-08-01

**What happened**

On August 1, DriveCentric made its Service-to-Sales Agent generally available inside its dealership engagement platform to score service customers for trade-in potential, start personalized conversations, and create sales opportunities from existing CRM data.
8 月 1 日，DriveCentric 在其汽车经销商互动平台内正式推出 Service-to-Sales Agent，利用现有 CRM 数据评估售后客户的置换潜力、发起个性化对话并创建销售机会。

**Why it matters**

This is a concrete vertical-agent deployment in which consent, customer identity, valuation data, messaging, and human handoff share one operational system instead of being stitched across separate vendors.
这是一个具体的垂直行业智能体部署案例：用户同意、客户身份、估值数据、消息与人工交接共用同一套运营系统，而不是跨多家供应商拼接。

**Sources:** [DriveCentric via PR Newswire](https://www.prnewswire.com/news-releases/drivecentric-continues-expansion-of-native-ai-agents-with-the-service-to-sales-agent-turning-service-appointments-into-trade-in-opportunities-302827361.html)

<a id="story-copyable-context-safety-trilemma"></a>

### Researchers formalize a safety trilemma for copyable context

- [ ] Interesting

**Underlying event date:** 2026-07-30

**What happened**

On July 30, researchers published a formal result showing that safeguards relying on copyable context face a worst-case floor on attacker assistance and cannot simultaneously guarantee useful capability, reliable safety, and open access.
7 月 30 日，研究人员发布了一项形式化结果，表明依赖可复制上下文的安全机制存在对攻击者提供帮助的最坏情形下限，无法同时保证有用能力、可靠安全与开放访问。

**Why it matters**

The result shifts dual-use access control from better prompt inspection toward hard-to-copy evidence such as trusted credentials, giving safety teams a clearer boundary for what model-side filtering can achieve.
该结果将双重用途访问控制的重心，从“更好地检查提示词”转向可信凭证等难以复制的证据，为安全团队更清晰地划定模型侧过滤能力的边界。

**Sources:** [arXiv](https://arxiv.org/abs/2607.27951)

## Follow-ups to Interesting Stories

No marked story had a qualifying update wholly inside this edition's coverage window.
没有任何已标记故事在本期覆盖窗口内出现完整落入时间范围且符合要求的新进展。

## Tracked Interests

- **[NVIDIA releases Cosmos 3 Edge for local physical AI](2026-07-24-ai-newsletter.md#story-nvidia-cosmos-3-edge-siggraph)** — Marked 2026-07-24. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[OpenAI rolls out Health in ChatGPT to U.S. users](2026-07-27-ai-newsletter.md#story-chatgpt-health-rollout)** — Marked 2026-07-27. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[月之暗面正式开源 Kimi K3](2026-07-29-ai-newsletter.md#story-kimi-k3-open-source)** — Marked 2026-07-29. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[Reader spotlight: SpecForge pairs LLMs with formal specifications](2026-07-29-ai-newsletter.md#story-imiron-specforge-ai-formal-specs)** — Marked 2026-07-29. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[LangSmith LLM Gateway enters public beta as a runtime control plane](2026-07-31-ai-newsletter.md#story-langsmith-llm-gateway-public-beta)** — Marked 2026-07-31. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[Deep Agents v0.7 cuts base input tokens by 65%](2026-07-31-ai-newsletter.md#story-deep-agents-v07-token-diet)** — Marked 2026-07-31. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[BrowserStack puts an agentic testing harness inside the IDE](2026-07-31-ai-newsletter.md#story-browserstack-test-companion-ide)** — Marked 2026-07-31. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.

## Watch Next Week

Project Perception's public preview will provide the first customer-facing evidence for whether its red, blue, and green agent loop can turn Microsoft's benchmark claims into repeatable operational outcomes.
Project Perception 的公开预览将带来首批面向客户的证据，用于判断其红、蓝、绿三类智能体闭环能否将微软的基准声称转化为可复现的运营结果。

The EU transparency deadline now makes implementation details—especially machine-readable marking and deployer disclosure—more important than the broader headline that high-risk rules were delayed.
欧盟透明度截止日期已经生效，因此机器可读标记与部署方告知等实施细节，现在比“高风险规则已延期”这个宏观标题更为重要。

## Sources

- [EN] [Microsoft — Project Perception](https://blogs.microsoft.com/blog/2026/07/27/rethinking-security-for-the-age-of-ai/)
- [EN] [arXiv — PatientAgentBench](https://arxiv.org/abs/2607.25485)
- [EN] [arXiv — SecRespond](https://arxiv.org/abs/2607.26791)
- [EN] [arXiv — PAUSE](https://arxiv.org/abs/2607.27354)
- [EN] [arXiv — Shadow evaluations](https://arxiv.org/abs/2607.27191)
- [EN] [AP — EU AI Act enforcement](https://apnews.com/article/eu-ai-regulation-deepfakes-hacking-f4fcee1f9750e2b32cdf26ad73ee5ec2)
- [EN] [European Express — Article 50 timetable](https://www.european.express/2026/07/17/eu-ai-act-what-actually-applies-on-2-august-2026/)
- [EN] [DriveCentric via PR Newswire](https://www.prnewswire.com/news-releases/drivecentric-continues-expansion-of-native-ai-agents-with-the-service-to-sales-agent-turning-service-appointments-into-trade-in-opportunities-302827361.html)
- [EN] [arXiv — Copyable-context safety](https://arxiv.org/abs/2607.27951)
