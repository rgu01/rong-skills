# Stateless MCP Lands, and the Agent Stack Gets Its Governance Layer

**Coverage:** 2026-07-23–2026-07-29 (CEST)

## Executive Brief

The 2026-07-28 Model Context Protocol specification shipped on July 28 with a stateless core, header-based routing, authorization hardening, and updated Tier 1 SDKs, and Anthropic shipped matching support in Claude the same day with connector observability, enterprise-managed auth, and an MCP tunnels research preview.
2026-07-28 版 Model Context Protocol 规范于 7 月 28 日发布，带来无状态协议核心、基于请求头的路由、授权加固以及更新的 Tier 1 SDK；同日 Anthropic 在 Claude 中上线了对应支持，包括连接器可观测性、企业级托管认证，以及 MCP tunnels 研究预览。

Governance and operations tooling dominated the week alongside it, as NVIDIA open-sourced its NOOA agent framework on July 27 for testing, tracing, and auditing agent behavior, Dynatrace announced no-code agent building and SRE agents on July 27, and Moonshot AI open-sourced the 2.8-trillion-parameter Kimi K3 the same evening.
本周与之并行的主线是治理与运维工具：NVIDIA 于 7 月 27 日开源了用于测试、追踪和审计智能体行为的 NOOA 智能体框架，Dynatrace 同日发布了无代码智能体构建与 SRE 智能体，月之暗面也在当晚开源了 2.8 万亿参数的 Kimi K3。

This edition also adds a reader-requested spotlight on Imiron's SpecForge, an LLM-assisted formal specification tool, and AI + Formal Methods is now a standing editorial interest of this newsletter.
本期还应读者要求增设了对 Imiron SpecForge（一款 LLM 辅助的形式化规约工具）的特别推介，"AI + 形式化方法"自本期起成为本刊的长期关注方向。

## AI Tools

<a id="story-mcp-2026-07-28-specification"></a>

### The 2026-07-28 MCP specification ships a stateless protocol core

- [ ] Interesting

**Underlying event date:** 2026-07-28

**What happened**

On July 28, the Model Context Protocol project published the 2026-07-28 specification, removing session handshakes and the `Mcp-Session-Id` header, adding Multi Round-Trip Requests, header-based method routing, cacheable list results with `ttlMs` and `cacheScope`, RFC 9207 issuer validation, a formal extensions framework, and a twelve-month minimum deprecation window, alongside updated TypeScript, Python, Go, and C# SDKs.
7 月 28 日，Model Context Protocol 项目发布了 2026-07-28 版规范，移除了会话握手和 `Mcp-Session-Id` 请求头，新增多轮往返请求（MRTR）、基于请求头的方法路由、带 `ttlMs` 与 `cacheScope` 的可缓存列表结果、RFC 9207 签发者校验、正式的扩展框架，以及至少十二个月的弃用过渡窗口，并同步更新了 TypeScript、Python、Go 和 C# SDK。

**Why it matters**

Statelessness removes sticky sessions and shared session stores from the deployment path, so remote tool servers can run behind ordinary load balancers on serverless and edge infrastructure — the single biggest operational constraint on production agent integrations to date.
无状态化把粘性会话和共享会话存储从部署链路中移除，使远程工具服务器可以在普通负载均衡器后、在 Serverless 与边缘基础设施上运行，而这正是此前生产级智能体集成最大的运维约束。

**Sources:** [Model Context Protocol Blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/) · [4sysops](https://4sysops.com/archives/2026-07-28-model-context-protocol-mcp-stateless-multi-round-trip-routable-headers-authorization-hardening/)

<a id="story-claude-mcp-connector-controls"></a>

### Anthropic ships connector observability, IdP-managed auth, and MCP tunnels in Claude

- [ ] Interesting

**Underlying event date:** 2026-07-28

**What happened**

On July 28, Anthropic brought the 2026-07-28 MCP spec to Claude and shipped an observability dashboard showing how published connectors perform across Claude surfaces, enterprise-managed auth that provisions connectors through an organization's identity provider such as Entra or Okta, versioned MCP Apps and Tasks extensions, and MCP tunnels in research preview for reaching servers inside a private network.
7 月 28 日，Anthropic 将 2026-07-28 版 MCP 规范引入 Claude，并上线了展示已发布连接器在各 Claude 界面表现的可观测性看板、通过 Entra 或 Okta 等企业身份提供商下发连接器的托管认证、带版本的 MCP Apps 与 Tasks 扩展，以及用于访问私有网络内服务器的 MCP tunnels 研究预览。

**Why it matters**

Connector authors have had almost no production telemetry and admins almost no central provisioning path, so per-connector latency and error data plus IdP-group-based access turn MCP integrations from unmanaged side channels into governable enterprise surface area.
连接器作者此前几乎没有生产遥测数据，管理员也缺少集中下发通道，因此按连接器统计的延迟与错误数据、加上基于身份提供商用户组的访问控制，把 MCP 集成从无人管理的旁路变成了可治理的企业资产。

**Sources:** [Claude by Anthropic](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude)

<a id="story-nvidia-nooa-agent-framework"></a>

### NVIDIA open-sources NOOA for testable, auditable agent behavior

- [ ] Interesting

**Underlying event date:** 2026-07-27

**What happened**

On July 27, NVIDIA published the NVIDIA Labs Object-Oriented Agent (NOOA) research framework on GitHub — which treats agents as native Python objects to make their behavior easier to test, trace, audit, and govern, with OS-level isolation such as a container, VM, or its OpenShell sandbox as the containment boundary — as part of launching the Open Secure AI Alliance with 36 other organizations including Microsoft, IBM, Hugging Face, LangChain, and Cloudflare.
7 月 27 日，NVIDIA 在 GitHub 上发布了 NVIDIA Labs Object-Oriented Agent（NOOA）研究框架，它把智能体视为原生 Python 对象，使其行为更易于测试、追踪、审计和治理，并以容器、虚拟机或自家 OpenShell 沙箱等操作系统级隔离作为收容边界；此举是 NVIDIA 与微软、IBM、Hugging Face、LangChain、Cloudflare 等另外 36 家机构共同成立 Open Secure AI Alliance 的一部分。

**Why it matters**

Agent harnesses are still mostly opaque at runtime, so a framework that makes each step inspectable — while explicitly keeping containment in the operating system rather than in the framework — gives teams a way to audit agent decisions without pretending tracing is a security boundary.
智能体框架在运行时大多仍不透明，因此一个让每一步都可检视、同时明确把收容职责留给操作系统而非框架本身的方案，让团队能够审计智能体决策，而不会误把追踪当成安全边界。

**Sources:** [NVIDIA Blog](https://blogs.nvidia.com/blog/open-secure-ai-alliance/) · [The Hacker News](https://thehackernews.com/2026/07/nvidia-forms-37-member-open-secure-ai.html)

<a id="story-dynatrace-agent-builder-sre-agents"></a>

### Dynatrace announces no-code Agent Builder and autonomous SRE agents

- [ ] Interesting

**Underlying event date:** 2026-07-27

**What happened**

On July 27, Dynatrace announced autonomous operations for Dynatrace Intelligence, making the Cloud SRE Agent, enhanced Dynatrace Assist, and an expanded integration ecosystem available to SaaS customers on DPS that day, with the no-code Agent Builder and the Autonomous SRE Agent — which triggers on newly detected problems and enriches the matching investigation — expected in August.
7 月 27 日，Dynatrace 发布了面向 Dynatrace Intelligence 的自主运维能力，其中 Cloud SRE Agent、增强版 Dynatrace Assist 和扩展的集成生态当日面向 DPS 上的 SaaS 客户开放，而无代码 Agent Builder 与在检测到新问题时自动触发、并为对应调查补充信息的 Autonomous SRE Agent 预计将在 8 月上线。

**Why it matters**

Operations teams are the group most exposed to agent output at scale, and pairing a no-code builder with agents that act inside an existing incident investigation targets the hard part — routing autonomous action through established remediation workflows instead of around them.
运维团队是最大规模承接智能体输出的一方，把无代码构建器与能在既有事件调查内部执行动作的智能体结合，正是瞄准了最难的一环：让自主动作走既有的修复流程，而不是绕开它。

**Sources:** [Dynatrace](https://www.dynatrace.com/news/press-release/autonomous-operations-enterprise-ai/) · [The New Stack](https://thenewstack.io/dynatrace-autonomous-sre-agents/)

<a id="story-hubspot-agent-hub-builder-beta"></a>

### HubSpot opens Agent Hub and Agent Builder in public beta

- [ ] Interesting

**Underlying event date:** 2026-07-23

**What happened**

On July 23, HubSpot launched Agent Hub and Agent Builder in public beta for all Professional and Enterprise customers, giving teams one place to discover, deploy, and monitor agents that share customer context, plus a low-code environment where non-developers build custom agents that consume HubSpot Credits.
7 月 23 日，HubSpot 面向所有 Professional 与 Enterprise 客户推出了 Agent Hub 和 Agent Builder 公测版，让团队在一处发现、部署和监控共享客户上下文的智能体，并提供让非开发者构建自定义智能体的低代码环境，这些自定义智能体按 HubSpot Credits 计费。

**Why it matters**

HubSpot's own framing — a prospecting agent contacting a customer the same week a service agent handles that account's open complaint — is the coordination failure most multi-agent deployments hit first, and shared context plus central monitoring is the practical fix.
HubSpot 自己给出的场景——某个客户的投诉尚未关闭，销售开拓智能体却在同一周联系了该客户——正是多智能体部署最先遇到的协同失灵，而共享上下文加集中监控是可落地的解法。

**Sources:** [CMSWire](https://www.cmswire.com/customer-experience/hubspot-debuts-agent-hub-to-unify-ai-agents/)

## Other AI Stories

<a id="story-kimi-k3-open-source"></a>

### 月之暗面正式开源 Kimi K3

- [X] Interesting

**事件发生日期：** 2026-07-27

**发生了什么**

7 月 27 日晚，月之暗面正式开源 Kimi K3 模型权重与技术报告，该模型拥有 2.8 万亿参数和 100 万 token 上下文窗口，同时开源了支撑其训练的 MoonEP 与 AgentEnv（FlashKDA 此前已开源），覆盖高性能通信、算子到分布式强化学习环境的关键链路。

**为什么重要**

一个 2.8 万亿参数、原生支持视觉理解的开放权重模型，加上配套开源的分布式强化学习环境工具链，把前沿规模的智能体训练与部署路径交到了自建基础设施的团队手中，而不再只属于闭源 API 的调用方。

**信息来源：** [IT之家](https://www.ithome.com/0/982/259.htm) · [新浪科技](https://finance.sina.com.cn/tech/roll/2026-07-28/doc-inikivui0406645.shtml)

<a id="story-meta-blackrock-el-paso-venture"></a>

### Meta and BlackRock form a $14 billion El Paso data center venture

- [ ] Interesting

**Underlying event date:** 2026-07-28

**What happened**

On July 28, Meta announced a strategic venture with BlackRock to develop and own a roughly $14 billion, 1-gigawatt AI data center campus in El Paso, Texas, with BlackRock-managed funds holding an 80% interest and Meta 20%, capital from BlackRock together with Global Infrastructure Partners and HPS Investment Partners, Meta managing construction and property services, and operations expected to begin in 2028.
7 月 28 日，Meta 宣布与贝莱德成立战略合资企业，在德克萨斯州埃尔帕索开发并持有一座总开发成本约 140 亿美元、装机 1 吉瓦的 AI 数据中心园区，其中贝莱德管理的基金持股 80%、Meta 持股 20%，资金由贝莱德连同 Global Infrastructure Partners 与 HPS Investment Partners 提供，Meta 负责施工与物业管理服务，园区预计 2028 年投入运营。

**Why it matters**

Handing majority ownership of a gigawatt-scale campus to asset managers moves frontier compute financing off the hyperscaler balance sheet, which changes who bears the risk if AI capacity demand comes in below plan.
把吉瓦级园区的多数股权交给资产管理机构，意味着前沿算力的融资正从超大规模厂商的资产负债表上移出，这也改变了一旦 AI 算力需求不及预期时由谁承担风险。

**Sources:** [Meta Investor Relations](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-New-Strategic-Venture-with-BlackRock-to-Develop-Data-Center-in-El-Paso/default.aspx) · [CNBC](https://www.cnbc.com/2026/07/28/meta-blackrock-partner-on-14-billion-el-paso-data-center.html)

<a id="story-siemens-nvidia-eda-agents"></a>

### Siemens expands its NVIDIA partnership for self-verifying EDA agents

- [ ] Interesting

**Underlying event date:** 2026-07-26

**What happened**

On July 26, Siemens announced an expanded strategic partnership with NVIDIA to bring self-verifying agentic AI workflows to semiconductor and PCB design, adding NVIDIA NeMo Gym, Nemotron models, and the OpenShell secure runtime to its Fuse EDA AI Agent system, extending the Questa One Agentic Toolkit, and reporting a 10x reduction in library characterization turnaround and 5x–10x lower token costs in its Solido Characterization Suite.
7 月 26 日，西门子宣布扩大与 NVIDIA 的战略合作，把自验证的智能体 AI 工作流引入半导体与印制电路板设计，在其 Fuse EDA AI Agent 体系中引入 NVIDIA NeMo Gym、Nemotron 模型和 OpenShell 安全运行时，扩展 Questa One Agentic Toolkit，并称其 Solido Characterization Suite 使库特征化周期缩短 10 倍、token 成本降低 5 至 10 倍。

**Why it matters**

Validating agent output against deterministic physics-based engines is the rare case where an industrial workflow can check an agent's work automatically, which is why chip design is becoming the clearest proving ground for long-running autonomous agents.
让智能体的输出接受确定性的物理引擎校验，是工业流程中少数能自动核验智能体工作的场景，这也是芯片设计正成为长时运行自主智能体最清晰试验场的原因。

**Sources:** [Siemens via PR Newswire](https://www.prnewswire.com/news-releases/siemens-advances-self-verifying-agentic-ai-workflows-for-semiconductor-and-pcb-design-302834767.html) · [New Electronics](https://www.newelectronics.co.uk/content/news/siemens-and-nvidia-expand-ai-partnership-for-semiconductor-and-pcb-design)

<a id="story-claude-voice-mode-opus-sonnet"></a>

### Anthropic upgrades Claude voice mode to Opus and Sonnet with connected tools

- [ ] Interesting

**Underlying event date:** 2026-07-23

**What happened**

On July 23, Anthropic updated Claude's voice mode so paid plans are no longer limited to Haiku, letting users run Opus and Sonnet in beta across mobile, desktop, and web, switch models mid-conversation, reach authorized connected tools such as Gmail, Google Calendar, and Slack during a voice session, and speak more languages on every plan including Free.
7 月 23 日，Anthropic 更新了 Claude 的语音模式，付费方案不再局限于 Haiku：用户可以在移动端、桌面端和网页端以 Beta 形式使用 Opus 与 Sonnet，在对话中途切换模型，在语音会话内调用已授权的 Gmail、Google 日历和 Slack 等连接器，并在包括免费方案在内的所有方案上使用更多语言。

**Why it matters**

Voice assistants have generally traded capability for latency, so letting a voice session run a frontier model and call authorized tools mid-conversation moves voice from quick lookups toward actually completing work.
语音助手通常以牺牲能力来换取低延迟，因此让语音会话运行前沿模型、并在对话中途调用已授权工具，使语音从快速查询转向真正完成工作。

**Sources:** [TechCrunch](https://techcrunch.com/2026/07/23/anthropic-updates-claude-voice-mode-with-more-capable-models/)

<a id="story-imiron-specforge-ai-formal-specs"></a>

### Reader spotlight: SpecForge pairs LLMs with formal specifications

- [X] Interesting

**Underlying event date:** 2025-06-13 (reader-requested spotlight; outside this week's window)

**What happened**

SpecForge, from Tokyo-based startup Imiron, is an AI-powered formal specification platform: its LLM features extract design intent from natural-language requirements and turn it into mathematically rigorous specifications based on Signal Temporal Logic (STL), which the tool then formally analyzes and verifies against system data, synthesizes test scenarios from, and monitors in real time.
SpecForge 是东京初创公司 Imiron 推出的 AI 驱动形式化规约平台：其 LLM 功能从自然语言需求中提取设计意图，并将其转化为基于信号时序逻辑（STL）的数学严谨规约，工具随后可对规约做形式化分析、用系统数据进行验证、从规约合成测试场景并开展实时监控。

Announced on June 13, 2025 and available since July 2025, the tool targets safety verification of AI systems such as autonomous vehicles and medical devices, and Imiron closed a ¥140 million pre-Series A round on June 1, 2026 to accelerate enterprise proofs of concept.
该工具于 2025 年 6 月 13 日发布、自 2025 年 7 月起可用，面向自动驾驶和医疗设备等 AI 系统的安全验证；Imiron 已于 2026 年 6 月 1 日完成 1.4 亿日元 pre-Series A 融资，用于加速企业级概念验证。

**Why it matters**

Formal methods have stayed niche because writing specifications demands mathematical-logic expertise, so letting LLMs draft the formal specs while deterministic analysis engines do the actual verification is a credible division of labor between AI and rigor — the AI-plus-formal-methods pattern this newsletter now tracks as a standing interest.
形式化方法长期小众，是因为编写规约需要数理逻辑专长；让 LLM 起草形式化规约、由确定性分析引擎完成真正的验证，是 AI 与严谨性之间可信的分工——这正是本刊自本期起作为长期关注方向持续跟踪的"AI + 形式化方法"模式。

**Sources:** [Imiron SpecForge](https://imiron.io/specforge/) · [Imiron](https://imiron.io/post/release-of-specforge/)

## Follow-ups to Interesting Stories

No marked interest produced a qualifying new event inside 2026-07-23–2026-07-29; both remain tracked below.
本期没有任何被标记的关注项在 2026-07-23 至 2026-07-29 区间内出现符合条件的新事件，两项均在下方继续跟踪。

## Tracked Interests

- **[NVIDIA releases Cosmos 3 Edge for local physical AI](2026-07-24-ai-newsletter.md#story-nvidia-cosmos-3-edge-siggraph)** — Marked 2026-07-24. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[OpenAI rolls out Health in ChatGPT to U.S. users](2026-07-27-ai-newsletter.md#story-chatgpt-health-rollout)** — Marked 2026-07-27. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.

## Watch Next Week

The MCP specification's twelve-month minimum deprecation window for Roots, Sampling, and the legacy HTTP+SSE transport sets the clock for migrating existing servers, while Dynatrace's Agent Builder and Autonomous SRE Agent are expected in August.
MCP 规范为 Roots、Sampling 和旧版 HTTP+SSE 传输设定的至少十二个月弃用窗口，为现有服务器的迁移定下了时间表；与此同时，Dynatrace 的 Agent Builder 和 Autonomous SRE Agent 预计将在 8 月上线。

## Sources

- [EN] [Model Context Protocol Blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/)
- [EN] [4sysops](https://4sysops.com/archives/2026-07-28-model-context-protocol-mcp-stateless-multi-round-trip-routable-headers-authorization-hardening/)
- [EN] [Claude by Anthropic](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude)
- [EN] [NVIDIA Blog](https://blogs.nvidia.com/blog/open-secure-ai-alliance/)
- [EN] [The Hacker News](https://thehackernews.com/2026/07/nvidia-forms-37-member-open-secure-ai.html)
- [EN] [Dynatrace](https://www.dynatrace.com/news/press-release/autonomous-operations-enterprise-ai/)
- [EN] [The New Stack](https://thenewstack.io/dynatrace-autonomous-sre-agents/)
- [EN] [CMSWire](https://www.cmswire.com/customer-experience/hubspot-debuts-agent-hub-to-unify-ai-agents/)
- [EN] [Meta Investor Relations](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-New-Strategic-Venture-with-BlackRock-to-Develop-Data-Center-in-El-Paso/default.aspx)
- [EN] [CNBC](https://www.cnbc.com/2026/07/28/meta-blackrock-partner-on-14-billion-el-paso-data-center.html)
- [EN] [Siemens via PR Newswire](https://www.prnewswire.com/news-releases/siemens-advances-self-verifying-agentic-ai-workflows-for-semiconductor-and-pcb-design-302834767.html)
- [EN] [New Electronics](https://www.newelectronics.co.uk/content/news/siemens-and-nvidia-expand-ai-partnership-for-semiconductor-and-pcb-design)
- [EN] [TechCrunch](https://techcrunch.com/2026/07/23/anthropic-updates-claude-voice-mode-with-more-capable-models/)
- [EN] [Imiron SpecForge](https://imiron.io/specforge/)
- [EN] [Imiron](https://imiron.io/post/release-of-specforge/)
- [中文] [IT之家](https://www.ithome.com/0/982/259.htm)
- [中文] [新浪科技](https://finance.sina.com.cn/tech/roll/2026-07-28/doc-inikivui0406645.shtml)
