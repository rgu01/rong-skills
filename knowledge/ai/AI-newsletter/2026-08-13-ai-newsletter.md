# Routing, Residency, and the Bill: Agent Tooling Grows a Cost Conscience

**Coverage:** 2026-08-07–2026-08-13 (Europe/Stockholm, CEST)

## Executive Brief

The week's agent tooling converged on two questions practitioners now ask before capability — where inference runs and what each call costs — with Claude Managed Agents gaining a pinnable inference geo on August 7, AgentCore bringing memory, policy, and harness into AWS GovCloud the same day, LangSmith going bring-your-own-cloud on AWS on August 12, and NVIDIA open-sourcing a model router on August 11.
本周的智能体工具集中回答了从业者在能力之前就会追问的两个问题——推理在哪里运行、每次调用花多少钱：8 月 7 日 Claude Managed Agents 支持固定推理地域，同日 AgentCore 将记忆、策略与托管 harness 带入 AWS GovCloud，8 月 12 日 LangSmith 在 AWS 上支持自带云部署，8 月 11 日 NVIDIA 开源了一个模型路由库。

Outside the toolchain, Anthropic said on August 11 that it will watermark text from its models, Google's Gemini app crossed a billion monthly users the same day, and Fortune's August 12 reporting put named CIOs on the record capping their own employees' AI spend.
在工具链之外，Anthropic 于 8 月 11 日宣布将为其模型生成的文本加水印，Google 的 Gemini 应用同日突破十亿月活，而《财富》8 月 12 日的报道让多位具名 CIO 公开承认，他们正在为本公司员工的 AI 支出设上限。

## AI Tools

<a id="story-claude-code-auto-mode-default"></a>

### Auto mode becomes the default in Claude Code

- [ ] Interesting

**Underlying event date:** 2026-08-07

**What happened**

On August 7, Anthropic announced that auto mode becomes the default in Claude Code for Pro, Max, and Team plans from August 14, routing each tool call through a classifier that blocks irreversible, destructive, or environment-escaping actions instead of prompting for every approval, reverting to manual approval after three consecutive blocks or twenty in a session, and it stopped charging those plans for the classifier's overhead as of the announcement.
8 月 7 日，Anthropic 宣布自 8 月 14 日起，auto 模式将成为 Pro、Max 与 Team 方案中 Claude Code 的默认模式：每次工具调用都经过一个分类器，拦截不可逆、破坏性或指向环境之外的操作，而不再逐条请求批准；若连续三次被拦截或单次会话累计二十次，则回退到手动批准模式；自公告起，这些方案不再为分类器开销付费。

**Why it matters**

Permission fatigue is the practical ceiling on how long an agent can run unattended, and shifting from per-call prompting to classifier-gated execution — with a measured 89% catch rate on dangerous commands against 13.6% for human review in Anthropic's 1,053-tester study — changes the default posture of every long Claude Code session.
批准疲劳是智能体无人值守运行时长的实际上限；从逐次询问转向由分类器把关的执行方式——在 Anthropic 面向 1,053 名测试者的研究中，危险命令的拦截率为 89%，而人工审查为 13.6%——改变了每一个长时间 Claude Code 会话的默认姿态。

**Sources:** [Claude Blog](https://claude.com/blog/auto-mode-default-in-claude-code)

<a id="story-managed-agents-advisor-inference-geo"></a>

### Claude Managed Agents gain an advisor model, a pinnable inference geo, and repo-loaded skills

- [ ] Interesting

**Underlying event date:** 2026-08-07

**What happened**

On August 7, Anthropic added three capabilities to Claude Managed Agents: an `{"type": "advisor"}` roster entry that lets a session's primary thread consult a model at least as capable as the agent's own mid-turn, an `inference_geo` setting that pins where inference runs per agent or per session, and automatic discovery of skills in a mounted GitHub repository's root `.claude/skills` directory at session start.
8 月 7 日，Anthropic 为 Claude Managed Agents 增加了三项能力：在多智能体名册中通过 `{"type": "advisor"}` 配置顾问模型，使会话主线程可在回合中途咨询一个能力不低于智能体自身的模型；通过 `inference_geo` 设置按智能体或按会话固定推理运行的地域；以及在会话启动时自动发现已挂载 GitHub 仓库根目录 `.claude/skills` 下的技能。

**Why it matters**

The three additions map to three separate blockers — a weak agent stuck on a hard turn, a data-residency requirement that would otherwise rule the platform out, and skills that had to be provisioned outside the repository that defines them — and each is now configuration rather than scaffolding code.
这三项新增分别对应三个不同的阻碍：能力不足的智能体卡在困难回合、若不满足数据驻留要求就无法采用该平台、以及技能必须在定义它们的仓库之外单独配置；如今每一项都变成配置项，而不再需要自建脚手架代码。

**Sources:** [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/api)

<a id="story-agentcore-govcloud-memory-policy-harness"></a>

### AgentCore brings memory, policy, and managed harness into AWS GovCloud

- [ ] Interesting

**Underlying event date:** 2026-08-07

**What happened**

On August 7, AWS made Amazon Bedrock AgentCore memory, policy, and harness available in the AWS GovCloud (US-West) region, adding short-term and long-term memory, natural-language policies that compile to Cedar for authorization and content control, and a managed harness that runs an agent from a declared model, tools, and instructions with no orchestration code or container, alongside runtime, gateway, identity, built-in tools, observability, and evaluations already in the region.
8 月 7 日，AWS 在 AWS GovCloud（US-West）区域提供 Amazon Bedrock AgentCore 的记忆、策略与 harness 能力：包括面向即时上下文的短期记忆与跨会话提炼洞见的长期记忆、可编译为 Cedar 以实现授权与内容管控的自然语言策略，以及只需声明模型、工具与指令即可运行智能体、无需编排代码或容器的托管 harness；该区域此前已提供 runtime、gateway、identity、内置工具、可观测性与评估能力。

**Why it matters**

Regulated buyers usually get agent infrastructure last and end up rebuilding memory and authorization themselves, so a region-complete AgentCore is the difference between a compliance-bounded team shipping agents and writing its own orchestration layer.
受监管的客户通常最后才拿到智能体基础设施，最终不得不自行重建记忆与授权机制；因此一个在该区域功能完整的 AgentCore，决定了受合规约束的团队是能交付智能体，还是要自己写一层编排代码。

**Sources:** [AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/08/agentcore-memory-policy-harness-govcloud/)

<a id="story-nemo-switchyard-model-router"></a>

### NVIDIA open-sources a model router for agent workflows

- [ ] Interesting

**Underlying event date:** 2026-08-11

**What happened**

On August 11, NVIDIA released NeMo Switchyard, an open-source model routing library that directs each step of an agent workflow to the most suitable model across a team's mix of open, proprietary, and NVIDIA models without rewriting the application, launched alongside Nemotron 3.5 Lightning, a 30-billion-parameter mixture-of-experts model NVIDIA measures at up to 4x faster output and 30% faster agentic task completion than its class.
8 月 11 日，NVIDIA 发布开源模型路由库 NeMo Switchyard：它在不改写应用的前提下，把智能体工作流的每一步分派给最合适的模型，可跨团队自有的开源、专有与 NVIDIA 模型组合进行路由；同期发布的 Nemotron 3.5 Lightning 是一款 300 亿参数的混合专家模型，NVIDIA 测得其输出速度最高提升 4 倍、智能体任务完成速度提升 30%。

**Why it matters**

LangChain's August 11 study of 145 multi-step agentic tasks found only 7% of calls needed a frontier model while 93% ran on Nemotron 3.5 Lightning for a 74% cost reduction at a six-point accuracy cost, which turns per-step routing from a micro-optimization into the main lever on an agent's bill.
LangChain 8 月 11 日针对 145 个多步智能体任务的研究发现，仅 7% 的调用需要前沿模型，93% 由 Nemotron 3.5 Lightning 承担，成本下降 74%，准确率代价为 6 个百分点；这让逐步路由从微优化变成影响智能体账单的主要杠杆。

**Sources:** [NVIDIA Blog](https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/) · [LangChain Blog](https://www.langchain.com/blog/switchyard-agent-routing-benchmark)

<a id="story-langsmith-byoc-aws-ga"></a>

### LangSmith bring-your-own-cloud reaches general availability on AWS

- [ ] Interesting

**Underlying event date:** 2026-08-12

**What happened**

On August 12, LangChain made LangSmith BYOC generally available on AWS, letting an enterprise run LangSmith inside its own AWS account so traces, datasets, and any PII or PHI they contain stay within its network boundary while LangChain still manages the service.
8 月 12 日，LangChain 宣布 LangSmith BYOC 在 AWS 上正式可用：企业可在自有 AWS 账户中运行 LangSmith，使追踪数据、数据集以及其中包含的个人身份或健康信息留在自身网络边界之内，同时服务仍由 LangChain 托管。

**Why it matters**

Agent traces are the most sensitive artifact a team produces, because they contain whatever the agent actually saw, and data residency has been the standard reason regulated teams run agents with observability switched off.
智能体追踪是团队产出中最敏感的数据，因为它记录了智能体实际看到的一切；而数据驻留一直是受监管团队关闭可观测性来运行智能体的常见理由。

**Sources:** [LangChain Blog](https://www.langchain.com/blog/langsmith-byoc-is-now-generally-available-on-aws)

<a id="story-vercel-ai-gateway-coding-agents"></a>

### One Vercel command puts nine coding agents behind a metered gateway

- [ ] Interesting

**Underlying event date:** 2026-08-12

**What happened**

On August 12, Vercel shipped `vercel ai-gateway coding-agents setup`, a single command that configures Claude Code, Codex, OpenCode, Pi, Cline, Cursor, Hermes, Kilo Code, and OpenClaw to run through AI Gateway, preserving each tool's existing config formatting while adding gateway credentials, 200-plus models, per-key budgets with reset and expiry, team-wide policies such as Zero Data Retention, and request-level tracing of cost and model.
8 月 12 日，Vercel 发布 `vercel ai-gateway coding-agents setup` 命令：一条命令即可将 Claude Code、Codex、OpenCode、Pi、Cline、Cursor、Hermes、Kilo Code 与 OpenClaw 接入 AI Gateway，在保留各工具原有配置格式的同时写入网关凭据，并提供 200 多个模型、带重置与过期设置的按密钥预算、诸如零数据保留的团队级策略，以及按请求粒度记录成本与模型的追踪。

**Why it matters**

Every coding agent a team adopts otherwise arrives with its own account, key, and invisible spend, and collapsing nine of them onto one gateway makes budget and retention policy a platform setting rather than nine separate conversations.
否则，团队每采用一个编码智能体，就多出一套账号、密钥与看不见的开销；把其中九个收拢到同一个网关之后，预算与数据保留策略变成一项平台设置，而不是九场各自为政的讨论。

**Sources:** [Vercel Changelog](https://vercel.com/changelog/set-up-coding-agents-in-one-command-with-ai-gateway)

<a id="story-agent-plugins-github-clients"></a>

### GitHub ships Agent Plugins 1.0 across its clients with managed-settings governance

- [ ] Interesting

**Underlying event date:** 2026-08-12

**What happened**

On August 12, GitHub shipped support for the Agent Plugins 1.0 specification — published August 6 with AWS, Anysphere, Microsoft, OpenAI, Vercel, and Google as a core maintainer — in VS Code, Copilot CLI, the GitHub Copilot app, and the Copilot cloud agent, letting one plugin package carry skills and MCP server configuration across compatible clients while Copilot Business and Enterprise administrators govern plugins through existing `managed-settings.json` controls, with existing Copilot plugins still supported.
8 月 12 日，GitHub 在 VS Code、Copilot CLI、GitHub Copilot 应用与 Copilot 云端智能体中支持 Agent Plugins 1.0 规范——该规范于 8 月 6 日发布，参与方包括 AWS、Anysphere、Microsoft、OpenAI、Vercel，Google 为核心维护者——使同一个插件包可在兼容客户端间携带 skills 与 MCP 服务器配置，同时 Copilot Business 与 Enterprise 管理员可通过既有的 `managed-settings.json` 控制项治理插件，现有 Copilot 插件继续受支持。

**Why it matters**

A cross-vendor spec only pays off once a major client enforces it end to end, and pairing plugin portability with the same managed-settings surface administrators already use is what lets an organization allow a plugin once instead of per tool.
跨厂商规范只有在某个主流客户端端到端落实之后才真正见效；把插件可移植性与管理员已在使用的同一套 managed-settings 面板结合起来，才使组织能够一次性放行某个插件，而不必逐个工具重复配置。

**Sources:** [GitHub Changelog](https://github.blog/changelog/2026-08-12-agent-plugins-1-0-in-vs-code-copilot-cli-and-the-copilot-app)

## Other AI Stories

<a id="story-anthropic-text-watermarking"></a>

### Anthropic says it will watermark text its models generate

- [ ] Interesting

**Underlying event date:** 2026-08-11

**What happened**

On August 11, Anthropic said every model released after August 2 automatically watermarks generated text and files, using an imperceptible mark carried inside the text itself across the platform API, Claude, Claude Code, Claude Cowork, and Claude Tag, the C2PA open standard for files such as JPEG and PNG, with support to be extended to older models.
8 月 11 日，Anthropic 表示，8 月 2 日之后发布的每个模型都会自动为生成的文本与文件加水印：文本采用嵌入其中、不可感知的标记，覆盖平台 API、Claude、Claude Code、Claude Cowork 与 Claude Tag，文件（如 JPEG 与 PNG）采用 C2PA 开放标准，并将把支持范围扩展到更早的模型。

**Why it matters**

The mark travels with copied text and may survive some editing, which is a real change for anyone reviewing submitted work, but Anthropic itself calls the signal not fully conclusive — it can indicate AI involvement without establishing who was responsible or what was altered afterward.
该标记会随复制的文本一起传播，并可能在部分编辑后仍然保留，这对任何审阅他人提交内容的人来说都是实质变化；但 Anthropic 自己也称这一信号并非完全确定——它能提示 AI 参与，却无法确定责任人，也无法说明事后被改动了什么。

**Sources:** [TechCrunch](https://techcrunch.com/2026/08/11/anthropic-says-it-will-watermark-text-generated-by-its-ai-models/) · [Gizmodo](https://gizmodo.com/anthropics-claude-will-start-adding-invisible-watermarks-to-ai-generated-text-2000797759)

<a id="story-gemini-one-billion-users"></a>

### Google's Gemini app passes one billion monthly users

- [ ] Interesting

**Underlying event date:** 2026-08-11

**What happened**

On August 11, Google said the Gemini app had crossed one billion monthly active users, making it the fastest-growing product in the company's history, with 63% of users speaking to Gemini directly, more than 150 million images generated daily, over 100 million active users on iOS, and one in five Gemini Live interactions using a live camera feed or screen share.
8 月 11 日，Google 表示 Gemini 应用月活跃用户已突破十亿，成为公司历史上增长最快的产品：63% 的用户直接与 Gemini 语音交互，每日生成图像超过 1.5 亿张，iOS 上活跃用户超过 1 亿，并且每五次 Gemini Live 交互中就有一次使用实时摄像头画面或屏幕共享。

**Why it matters**

Distribution at this scale sets the assumptions builders inherit — voice-first input and live camera context are now mainstream expectations rather than differentiators — and it lands weeks after ChatGPT was reported at a billion weekly users, on a different clock.
这种规模的分发决定了开发者继承的默认假设——语音优先输入与实时摄像头上下文如今是主流预期，而非差异化卖点；而它出现在有报道称 ChatGPT 达到十亿周活之后数周，两者的统计周期并不相同。

**Sources:** [Google Blog](https://blog.google/innovation-and-ai/products/gemini-app/one-billion-monthly-users/) · [Forbes](https://www.forbes.com/sites/antoniopequenoiv/2026/08/11/gemini-becomes-googles-fastest-growing-product-ever-after-hitting-1-billion-monthly-users/)

<a id="story-ibm-together-ai-inference-cluster"></a>

### IBM and Together AI sign a $240 million open-model inference cluster

- [ ] Interesting

**Underlying event date:** 2026-08-11

**What happened**

On August 11, IBM and Together AI signed a multi-year $240 million agreement to build a US-based inference cluster on IBM Cloud with roughly 2,000 NVIDIA Blackwell B300 chips in HGX B300 systems and Spectrum-X Ethernet networking, serving open-source models, with availability expected in the first quarter of 2027.
8 月 11 日，IBM 与 Together AI 签署为期多年、金额 2.4 亿美元的协议，在 IBM Cloud 上于美国建设推理集群：初期约 2,000 张 NVIDIA Blackwell B300 芯片，采用 HGX B300 系统与 Spectrum-X 以太网网络，用于服务开源模型，预计 2027 年第一季度可用。

**Why it matters**

Dedicated capacity aimed specifically at open-weight inference gives cost- and control-sensitive buyers a credible third path between proprietary APIs and self-hosting, and it prices that path more than a year ahead of delivery.
专门面向开源权重推理的算力，为对成本与控制敏感的客户提供了介于专有 API 与自建之间的可信第三条路径，并且在交付一年多之前就为这条路径定了价。

**Sources:** [IBM Newsroom](https://newsroom.ibm.com/2026-08-11-IBM-and-Together-AI-Sign-Multi-Year-Agreement-to-Scale-Open-Source-AI-Inference-with-NVIDIA-AI-Infrastructure-on-IBM-Cloud) · [BNN Bloomberg](https://www.bnnbloomberg.ca/business/2026/08/11/ibm-together-ai-ink-240-million-deal-for-nvidia-powered-ai-inference-cluster/)

<a id="story-lovable-series-c"></a>

### Lovable raises $400 million at a $13.3 billion valuation

- [ ] Interesting

**Underlying event date:** 2026-08-12

**What happened**

On August 12, Stockholm-based Lovable announced a $400 million Series C at a $13.3 billion valuation led by Menlo Ventures with the EQT-managed Scaleup Europe Fund, reporting more than 60 million projects built since its November 2024 launch, over 900 million monthly visits to Lovable-built apps, reach into nearly two-thirds of the Fortune 500, and more than a third of users already earning revenue from what they built.
8 月 12 日，总部位于斯德哥尔摩的 Lovable 宣布完成 4 亿美元 C 轮融资，估值 133 亿美元，由 Menlo Ventures 领投，EQT 管理的 Scaleup Europe Fund 联合领投；公司称自 2024 年 11 月上线以来已创建超过 6,000 万个项目，用 Lovable 构建的应用每月访问量超过 9 亿次，客户覆盖近三分之二的《财富》500 强，超过三分之一的用户已从所构建的产品中获得收入。

**Why it matters**

The valuation roughly doubled in seven months on usage rather than promise, and a European vendor at this size changes procurement conversations for teams that treat data location as a requirement.
其估值在七个月内大约翻倍，依据是实际使用量而非愿景；而一家达到这一体量的欧洲厂商，会改变那些把数据存放地点视为硬性要求的团队的采购讨论。

**Sources:** [Lovable Blog](https://lovable.dev/blog/series-c) · [TechCrunch](https://techcrunch.com/2026/08/12/lovable-confirms-new-13-3b-valuation-raises-another-400m/)

## AI at Work

<a id="story-samsara-employee-ai-caps"></a>

### Samsara's CIO puts caps on non-technical employees' AI use

- [ ] Interesting

**Stance:** Discouraging — Samsara

**Underlying event date:** 2026-08-12

**What happened**

On August 12, Samsara CIO Stephen Franchetti stated publicly for the first time that the company has capped AI usage for some non-technical employees while leaving groups such as research and development more room to experiment, saying "It took us a while to settle on the right caps, to make sure everyone was well served," with employees still choosing which models they use inside the cap across a roughly 4,100-person workforce.
8 月 12 日，Samsara 首席信息官 Stephen Franchetti 首次公开表示，公司已对部分非技术岗员工的 AI 使用量设上限，同时为研发等团队保留更多试验空间；他说："我们花了一段时间才定下合适的上限，以确保每个人都被妥善照顾"；在约 4,100 人的员工队伍中，员工仍可在上限内自行选择使用哪些模型。

**Why it matters**

The instrument here is a per-population quota rather than a tool ban, so the governed variable is spend by job family, and it is enforced by the cap itself rather than recommended in a policy document.
这里的手段是按人群设定配额，而不是禁用工具，因此被治理的变量是按职能划分的支出，且由上限本身强制执行，而非在政策文件中建议执行。

**Sources:** [Fortune](https://fortune.com/2026/08/12/cios-and-ctos-spent-years-lauding-ai-now-with-costs-rising-theyre-putting-limits-on-how-its-used/)

<a id="story-cigna-approved-model-list"></a>

### Cigna authorizes more than 70 internal models to steer staff off expensive ones

- [ ] Interesting

**Stance:** Discouraging — The Cigna Group

**Underlying event date:** 2026-08-12

**What happened**

On August 12, Cigna Group Chief Data, Digital and AI Officer Katya Andresen stated publicly for the first time that the insurer has authorized more than 70 AI models for internal use so its workforce can route simpler tasks to cheaper models, saying "the way you really run up costs is you use the most expensive models with no guardrails around them," and reporting that total spend has grown more slowly than compute usage as a result.
8 月 12 日，Cigna Group 首席数据、数字与 AI 官 Katya Andresen 首次公开表示，公司已批准 70 多个 AI 模型供内部使用，让员工把较简单的任务交给更便宜的模型；她说："真正让成本失控的方式，就是在毫无护栏的情况下使用最贵的模型"；她还表示，因此总支出的增速已慢于算力用量的增速。

**Why it matters**

An approved-model list is the softer end of restriction — employees keep AI but lose free choice of frontier models by default — and it is the pattern most likely to spread among regulated employers that cannot simply cap a clinician's or adjuster's tooling.
批准模型清单属于限制中较温和的一端——员工保留 AI，但默认失去自由选用前沿模型的权利——并且这是最可能在受监管雇主中扩散的模式，因为这些雇主无法简单地对临床或理赔人员的工具设上限。

**Sources:** [Fortune](https://fortune.com/2026/08/12/cios-and-ctos-spent-years-lauding-ai-now-with-costs-rising-theyre-putting-limits-on-how-its-used/)

## Follow-ups to Interesting Stories

No marked interest had a qualifying update this week: every development found for a tracked story either fell outside the 2026-08-07–2026-08-13 window or was already published in an earlier edition.
本周没有任何已标记的关注条目获得符合条件的更新：为被跟踪故事找到的所有进展，要么落在 2026-08-07 至 2026-08-13 的窗口之外，要么已在此前的期次中发布过。

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
- **[LongHorizon-Harness gives computer-use agents a manager, executor, and auditor](2026-08-05-ai-newsletter.md#story-longhorizon-harness)** — Marked 2026-08-05. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[Drata ships agent discovery, scoring, and blocking in limited availability](2026-08-06-ai-newsletter.md#story-drata-ai-agent-governance)** — Marked 2026-08-06. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[WriteGuard puts risk tiers and attribution in front of MCP writes](2026-08-06-ai-newsletter.md#story-cloudflare-writeguard-mcp-controls)** — Marked 2026-08-06. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[Anthropic puts a customer-run checkpoint in front of every Claude Enterprise prompt](2026-08-11-ai-newsletter.md#story-anthropic-inference-hooks)** — Marked 2026-08-11. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[Insygna offers a free security scorecard for agents before they get system access](2026-08-11-ai-newsletter.md#story-insygna-agent-report-card)** — Marked 2026-08-11. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[A probing method infers which training run a frontier model came from](2026-08-11-ai-newsletter.md#story-model-knowledge-cutoff-probing)** — Marked 2026-08-11. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.

## Watch Next Week

Auto mode reaches Pro, Max, and Team plans on August 14, so next week is the first with classifier-gated execution as the default for most Claude Code users rather than an opt-in.
auto 模式将于 8 月 14 日覆盖 Pro、Max 与 Team 方案，因此下周将是多数 Claude Code 用户首次以分类器把关的执行方式作为默认设置，而不再是可选项。

Anthropic has said watermark support will extend to models released before August 2, which would widen how much existing Claude output becomes detectable.
Anthropic 表示水印支持将扩展到 8 月 2 日之前发布的模型，这会扩大现有 Claude 输出中可被检测的范围。

## Sources

- [EN] [Claude Blog — Auto mode is now the default in Claude Code](https://claude.com/blog/auto-mode-default-in-claude-code)
- [EN] [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/api)
- [EN] [AWS What's New — AgentCore memory, policy, and harness in GovCloud](https://aws.amazon.com/about-aws/whats-new/2026/08/agentcore-memory-policy-harness-govcloud/)
- [EN] [NVIDIA Blog — Nemotron 3.5 Lightning and NeMo Switchyard](https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/)
- [EN] [LangChain Blog — Switchyard agent routing benchmark](https://www.langchain.com/blog/switchyard-agent-routing-benchmark)
- [EN] [LangChain Blog — LangSmith BYOC generally available on AWS](https://www.langchain.com/blog/langsmith-byoc-is-now-generally-available-on-aws)
- [EN] [Vercel Changelog — Coding agents in one command](https://vercel.com/changelog/set-up-coding-agents-in-one-command-with-ai-gateway)
- [EN] [GitHub Changelog — Agent Plugins 1.0 in VS Code, Copilot CLI, and the Copilot app](https://github.blog/changelog/2026-08-12-agent-plugins-1-0-in-vs-code-copilot-cli-and-the-copilot-app)
- [EN] [TechCrunch — Anthropic says it will watermark generated text](https://techcrunch.com/2026/08/11/anthropic-says-it-will-watermark-text-generated-by-its-ai-models/)
- [EN] [Gizmodo — Claude will add invisible watermarks to AI-generated text](https://gizmodo.com/anthropics-claude-will-start-adding-invisible-watermarks-to-ai-generated-text-2000797759)
- [EN] [Google Blog — Gemini app hits 1 billion monthly active users](https://blog.google/innovation-and-ai/products/gemini-app/one-billion-monthly-users/)
- [EN] [Forbes — Gemini becomes Google's fastest-growing product](https://www.forbes.com/sites/antoniopequenoiv/2026/08/11/gemini-becomes-googles-fastest-growing-product-ever-after-hitting-1-billion-monthly-users/)
- [EN] [IBM Newsroom — IBM and Together AI multi-year agreement](https://newsroom.ibm.com/2026-08-11-IBM-and-Together-AI-Sign-Multi-Year-Agreement-to-Scale-Open-Source-AI-Inference-with-NVIDIA-AI-Infrastructure-on-IBM-Cloud)
- [EN] [BNN Bloomberg — IBM and Together AI ink $240 million deal](https://www.bnnbloomberg.ca/business/2026/08/11/ibm-together-ai-ink-240-million-deal-for-nvidia-powered-ai-inference-cluster/)
- [EN] [Lovable Blog — Series C](https://lovable.dev/blog/series-c)
- [EN] [TechCrunch — Lovable confirms $13.3B valuation](https://techcrunch.com/2026/08/12/lovable-confirms-new-13-3b-valuation-raises-another-400m/)
- [EN] [Fortune — CIOs and CTOs are putting limits on AI use](https://fortune.com/2026/08/12/cios-and-ctos-spent-years-lauding-ai-now-with-costs-rising-theyre-putting-limits-on-how-its-used/)
