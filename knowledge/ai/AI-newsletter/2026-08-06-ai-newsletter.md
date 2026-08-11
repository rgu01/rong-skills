# Agents Get a Computer, a Wallet, and a Compliance Officer

**Coverage:** 2026-07-31–2026-08-06 (Europe/Stockholm)

## Executive Brief

Cloudflare's second Agents Week ran August 3–5 with the agent lifecycle as its spine, shipping a per-agent runtime, a programmable wallet with spend caps, and a fine-grained policy layer for MCP servers.
Cloudflare 第二届 Agents Week 于 8 月 3 日至 5 日举行，以智能体生命周期为主线，先后推出按智能体分配的运行时、带额度上限的可编程钱包，以及面向 MCP 服务器的细粒度策略层。

Alongside it, Meta entered the terminal-agent market with Muse Code, Alibaba's Qwen team published a screenshot-only computer-use agent, and Drata began shipping agent discovery and enforcement for enterprises that cannot yet prove what their agents did.
与此同时，Meta 以 Muse Code 进入终端智能体市场，阿里 Qwen 团队发布了仅依赖屏幕截图的计算机操作智能体，而 Drata 开始向尚无法证明其智能体做过什么的企业交付智能体发现与策略执行能力。

## AI Tools

<a id="story-cloudflare-computer-agent-runtime"></a>

### Cloudflare gives each agent a computer instead of a container

- [ ] Interesting

**Underlying event date:** 2026-08-03

**What happened**

On August 3, opening Agents Week, Cloudflare released `@cloudflare/computer` as an open-source early preview: an npm package that gives an agent a virtual filesystem backed by SQLite plus two interchangeable execution backends — fast isolates by default and containers only when a command needs Linux, npm, or a native binary — with an AI SDK-compatible toolset for read, write, edit, list, and execute.
8 月 3 日，Cloudflare 在 Agents Week 首日以开源早期预览形式发布 `@cloudflare/computer`：这个 npm 包为智能体提供由 SQLite 支撑的虚拟文件系统，以及两种可互换的执行后端——默认使用快速 isolate，仅当命令需要 Linux、npm 或原生二进制时才启用容器——并附带兼容 AI SDK 的读取、写入、编辑、列举与执行工具集。

**Why it matters**

Putting every agent in a container is the expensive default that makes agent fleets stop scaling, and letting one shared filesystem span isolates and containers means the cheap path handles file, data, and git work while the costly path is reserved for the commands that genuinely need a Linux box.
把每个智能体都塞进容器，是让智能体集群无法继续扩展的昂贵默认做法；让同一个共享文件系统横跨 isolate 与容器，意味着文件、数据和 git 操作走便宜的路径，而昂贵的路径只留给真正需要一台 Linux 机器的命令。

**Sources:** [Cloudflare Blog](https://blog.cloudflare.com/cloudflare-computer/)

<a id="story-qwen-cua-native-computer-use"></a>

### Qwen-CUA drives a desktop from screenshots alone

- [ ] Interesting

**Underlying event date:** 2026-08-03

**What happened**

On August 3, the Qwen team and XLang Lab published Qwen-CUA, a native computer-use agent on a 397B-A17B mixture-of-experts backbone that observes only screenshots and acts through keyboard and mouse events — no DOM tree, accessibility metadata, or task-specific API — trained on roughly 40,000 verifiable tasks across a rollout fleet of nearly 100,000 vCPUs, reaching 86.2 on OSWorld-Verified while cutting prompt-injection attack success from 36.6% to 16.4%.
8 月 3 日，Qwen 团队与 XLang Lab 发布 Qwen-CUA：这是一个基于 397B-A17B 混合专家骨干的原生计算机操作智能体，仅观察屏幕截图并通过键盘鼠标事件行动——不依赖 DOM 树、无障碍元数据或任务专用 API——在近 10 万 vCPU 的采样集群上以约 4 万个可验证任务训练，OSWorld-Verified 得分 86.2，同时把提示注入攻击成功率从 36.6% 降至 16.4%。

**Why it matters**

Agents that need accessibility trees or per-app APIs break on every application that does not expose them, so a screenshot-only controller with published attack-success numbers is the more honest baseline for automating legacy desktop and professional software.
依赖无障碍树或逐应用 API 的智能体，在任何不提供这些接口的软件上都会失效；因此一个只靠屏幕截图、并公开了攻击成功率数据的控制器，是自动化遗留桌面与专业软件时更诚实的基线。

**Sources:** [arXiv paper](https://arxiv.org/abs/2608.02352) · [GitHub repository](https://github.com/xlang-ai/Qwen-CUA)

<a id="story-cloudflare-wallets-agent-identity"></a>

### Cloudflare Wallets gives agents an identity and a spending cap

- [ ] Interesting

**Underlying event date:** 2026-08-04

**What happened**

On August 4, Cloudflare announced Cloudflare Wallets and opened handle claiming at cloudflare.pay, describing a two-tier design in which a human-held Account Wallet stores stablecoins and per-agent Virtual Wallets spend against x402 with allowances, allowlists, per-transaction maximums, and a ceiling set by the account owner, with the wallet functionality itself shipping later.
8 月 4 日，Cloudflare 发布 Cloudflare Wallets，并在 cloudflare.pay 开放账号名注册，其两级设计中由人持有的 Account Wallet 存放稳定币，按智能体分配的 Virtual Wallet 则基于 x402 支付，并受额度、白名单、单笔上限以及账户所有者设定的天花板约束；钱包功能本身将在之后上线。

**Why it matters**

An agent that must pay for an API, a dataset, or a service currently borrows a human's card with no per-agent ceiling, so a human-readable identifier plus an owner-set spend limit turns "what did this agent buy" from a reconstruction exercise into a policy question.
需要为 API、数据集或服务付费的智能体，目前只能借用人的银行卡，且没有按智能体的额度上限；一个可读的标识加上由所有者设定的支出上限，让"这个智能体买了什么"从事后追溯变成一个策略问题。

**Sources:** [Cloudflare Blog](https://blog.cloudflare.com/wallets/) · [Fortune](https://fortune.com/2026/08/04/cloudflare-ai-agents-wallets-id/)

<a id="story-drata-ai-agent-governance"></a>

### Drata ships agent discovery, scoring, and blocking in limited availability

- [X] Interesting

**Underlying event date:** 2026-08-04

**What happened**

On August 4, Drata opened limited availability of AI Agent Governance, pairing a device-side sensor with an MCP proxy that evaluates each tool call against policy, surfaces shadow agents, scores agent trustworthiness, flags behavioral drift, blocks violating actions before execution, and writes tamper-evident evidence logs — end to end for Anthropic first, with OpenAI, Google Vertex AI, and AWS Bedrock coverage in development.
8 月 4 日，Drata 开放 AI Agent Governance 的限量可用版本：端侧传感器与 MCP 代理配合，对每次工具调用按策略评估，发现影子智能体、为智能体可信度打分、标记行为漂移、在执行前拦截违规动作，并写入防篡改的证据日志——首先端到端支持 Anthropic，OpenAI、Google Vertex AI 与 AWS Bedrock 的原生覆盖仍在开发中。

**Why it matters**

Audit questions about agents arrive as "prove what it accessed and what it did," and a proxy that both enforces policy at the tool-call boundary and emits tamper-evident evidence answers that without asking every application team to instrument itself.
关于智能体的审计问题往往是"证明它访问了什么、做了什么"；一个既在工具调用边界执行策略、又输出防篡改证据的代理，可以在不要求每个应用团队自行埋点的前提下回答这一问题。

**Sources:** [Drata](https://drata.com/about/news/drata-extends-trust-management-platform-to-continuously-monitor-and-govern-ai-agents) · [Security Boulevard](https://securityboulevard.com/2026/08/drata-opens-limited-availability-for-ai-agent-governance-product/)

<a id="story-cloudflare-writeguard-mcp-controls"></a>

### WriteGuard puts risk tiers and attribution in front of MCP writes

- [X] Interesting

**Underlying event date:** 2026-08-05

**What happened**

On August 5, Cloudflare introduced WriteGuard in private beta, a middleware policy, attribution, and auditing layer that sits between MCP clients and servers, sorting tools into four risk tiers — read only, minimal impact, contained write, and critical — enabling or disabling each tool without changing MCP server code, labeling write actions with the agent that performed them, logging invocations as successful, failed, or blocked, and blocking critical-tier actions until a human intervenes.
8 月 5 日，Cloudflare 以私有测试形式推出 WriteGuard：这是一个位于 MCP 客户端与服务器之间的中间层，提供策略、归因与审计能力，把工具划分为只读、影响极小、受限写入与关键四个风险等级，可在不修改 MCP 服务器代码的前提下逐个启用或停用工具，为写操作标注执行它的智能体，把调用记录为成功、失败或被拦截，并在人工介入前拦截关键等级的动作。

**Why it matters**

Most MCP servers expose read and destructive tools through the same undifferentiated interface, so classifying tools by blast radius and attributing writes downstream is what lets a team enable a server at all instead of banning it.
多数 MCP 服务器把只读工具与破坏性工具暴露在同一个无区分的接口后面；按影响范围为工具分级、并在下游标注写操作的来源，才让团队有可能真正启用某个服务器，而不是一律封禁。

**Sources:** [Cloudflare Blog](https://blog.cloudflare.com/mcp-portal-writeguard-private-beta/)

<a id="story-meta-muse-code-terminal-agent"></a>

### Meta ships Muse Code with a replay-exact event log

- [ ] Interesting

**Underlying event date:** 2026-08-05

**What happened**

On August 5, Meta released Muse Code in beta for macOS and Linux, a terminal coding agent powered by the new Muse Spark 1.2 model that keeps async background sub-agents alive for a whole session instead of spawning one per task, writes an append-only local event log of every model call, tool run, approval, and edit that Meta calls replay-exact and restart-safe, and ships `/plan`, `/grill`, and `/goal` as built-in skills.
8 月 5 日，Meta 面向 macOS 与 Linux 发布 Muse Code 测试版：这是由新模型 Muse Spark 1.2 驱动的终端编码智能体，异步后台子智能体在整个会话期间保持存活，而非按任务逐次启动；它把每一次模型调用、工具执行、审批与编辑写入仅追加的本地事件日志，Meta 称其可精确重放且可安全重启；`/plan`、`/grill` 与 `/goal` 作为内置 skill 一同提供。

**Why it matters**

The hardest part of running a long coding agent is not generating the diff but reconstructing what it did after it went wrong, and an append-only log of calls, approvals, and edits makes a session reviewable and resumable rather than something you rerun from scratch.
运行长时间编码智能体最难的部分，不是生成 diff，而是在它出错后重建它究竟做了什么；一份记录调用、审批与编辑的仅追加日志，让一次会话变得可复核、可续跑，而不是只能从头重来。

**Sources:** [MarkTechPost](https://www.marktechpost.com/2026/08/05/meta-superintelligence-labs-releases-muse-code/) · [CNBC](https://www.cnbc.com/2026/08/05/meta-debuts-muse-code-to-take-on-anthropic-and-openai-.html)

## Other AI Stories

<a id="story-sensenova-u15-lite-preview"></a>

### 商汤开源 SenseNova U1.5-Lite-Preview

- [ ] Interesting

**事件发生日期：** 2026-08-03

**发生了什么**

8 月 3 日，商汤科技开源轻量级统一多模态模型 SenseNova U1.5-Lite-Preview，该模型基于 NEO-Unify 架构，以 8B-MoT 体量贯通视觉理解、推理、生成与编辑，原生支持 4K 图像生成，并在多项基准上明显超过上一代 U1（Qwen-Image-Bench 由 47.14 升至 55.20，ImgEdit-Bench 由 3.90 升至 4.37，GEdit-Bench-en 由 7.47 升至 8.17），已通过 GitHub、Hugging Face 与魔搭社区发布。

**为什么重要**

把理解、推理、生成与编辑压进 8B 量级并原生输出 4K，意味着统一多模态不再只属于需要整机集群的团队，而这一系列此前已获十余家国产芯片厂商适配，进一步降低了本地部署的门槛。

**信息来源：** [IT之家](https://www.ithome.com/0/985/044.htm) · [北京商报](https://www.bbtnews.com.cn/2026/0803/601196.shtml)

<a id="story-mistral-shieldstral-safety-classifier"></a>

### Mistral open-sources a 3B guard model that reads policies at inference time

- [ ] Interesting

**Underlying event date:** 2026-08-04

**What happened**

On August 4, Mistral released Shieldstral, a 3B open-weights multimodal safety classifier under Apache 2.0 on Hugging Face that frames moderation as question answering — an operator supplies an instruction setting context and strictness, a yes/no query such as whether content promotes physical violence, and the text or image to judge — which Mistral says matches or outperforms open guard models up to seven times its size across text safety, refusal detection, policy adaptability, and multimodal safety.
8 月 4 日，Mistral 在 Hugging Face 以 Apache 2.0 许可发布 Shieldstral，这是一个 30 亿参数的开放权重多模态安全分类器，它把内容审核建模为问答任务——运营方提供设定语境与严格程度的指令、一个是非问题（例如内容是否鼓励肢体暴力），以及待判定的文本或图像——Mistral 称其在文本安全、拒答识别、策略适配与多模态安全四个维度上，达到或超过参数量最多为其七倍的开放守卫模型。

**Why it matters**

Guard models with hard-coded harm taxonomies force teams to retrain whenever their policy changes, so accepting the policy as plain-language input at inference time moves moderation from a model-ownership problem back to a configuration one.
把危害分类硬编码在模型里的守卫模型，迫使团队在策略变化时重新训练；把策略改为推理时的自然语言输入，让内容审核从"必须自己拥有模型"退回为一个配置问题。

**Sources:** [Mistral AI](https://mistral.ai/news/shieldstral/) · [SiliconANGLE](https://siliconangle.com/2026/08/05/mistral-introduces-shieldstral-provide-lightweight-policy-aware-moderation-ai-models/)

<a id="story-deepmind-leadership-shakeup"></a>

### Hassabis moves to chair as Jeff Dean leaves Google for Discovery Loop

- [ ] Interesting

**Underlying event date:** 2026-08-05

**What happened**

On August 5, Google announced that Demis Hassabis steps down as Google DeepMind CEO to become its Chair and Alphabet's Chief Scientist while remaining CEO of Isomorphic Labs, that CTO Koray Kavukcuoglu becomes the SVP leading Google DeepMind and its Gemini and frontier-research work, and that Jeff Dean is leaving Google to launch Discovery Loop, an independent public benefit corporation applying machine learning to scientific discovery, joined by Gemini co-lead Oriol Vinyals and with Google as a founding investor.
8 月 5 日，谷歌宣布 Demis Hassabis 卸任 Google DeepMind 首席执行官，转任其主席兼 Alphabet 首席科学家，同时继续担任 Isomorphic Labs 首席执行官；原首席技术官 Koray Kavukcuoglu 出任高级副总裁，领导 Google DeepMind 及其 Gemini 与前沿研究工作；Jeff Dean 则离开谷歌创办 Discovery Loop，这是一家把机器学习用于科学发现的独立公益公司，Gemini 联合负责人 Oriol Vinyals 一同加入，谷歌为其创始投资方。

**Why it matters**

Losing an operational CEO, a chief scientist, and a Gemini co-lead in one day concentrates Gemini's direction in a single new SVP while placing some of the lab's most senior research judgment inside a company Google funds but does not run.
在同一天失去一位负责日常运营的首席执行官、一位首席科学家和一位 Gemini 联合负责人，会把 Gemini 的方向集中到一位新任高级副总裁手中，同时把该实验室最资深的部分研究判断，放进一家由谷歌出资却不由谷歌经营的公司里。

**Sources:** [9to5Google](https://9to5google.com/2026/08/05/demis-hassabis-deepmind/) · [The Decoder](https://the-decoder.com/google-deepmind-loses-both-its-ceo-and-chief-scientist-as-demis-hassabis-and-jeff-dean-step-down-simultaneously/)

<a id="story-bytedance-seedrealtime"></a>

### 字节跳动发布音视频全双工大模型 SeedRealtime

- [ ] Interesting

**事件发生日期：** 2026-08-05

**发生了什么**

8 月 5 日，字节跳动发布原生音视频全双工大模型 SeedRealtime 并上线豆包，该模型以统一端到端架构原生融合音频、视频与文本，在连续多模态信息流中同时完成感知、理解、决策与表达，实现"边看、边听、边说"，不再依赖 ASR、视觉模型与 TTS 级联，也不再依赖外部 VAD 判断话轮；字节称端到端人工评测显示，其音视频对话节奏问题相比级联方案减少约一半。

**为什么重要**

级联式语音方案的每一层都在累积延迟与信息损失，而话轮判断交给外部 VAD 常导致抢话与误触发；把感知与表达收进同一个模型，是让实时语音交互从"能用"走向"自然"的必要一步。

**信息来源：** [IT之家](https://www.ithome.com/0/985/891.htm) · [新浪财经](https://finance.sina.com.cn/stock/t/2026-08-05/doc-inimfsht1538490.shtml)

## Follow-ups to Interesting Stories

No marked interest produced a qualifying update inside this coverage window. Every candidate found was either an event dated before 2026-07-31, an article restating an unchanged earlier event, or an announcement without exact in-window date evidence.
本刊在本期覆盖窗口内没有为任何已标记关注找到符合条件的更新。所有候选材料要么事件发生于 2026-07-31 之前，要么只是对未发生变化的旧事件的重述，要么缺乏窗口内的确切日期证据。

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

## Watch Next Week

Three of this week's controls are still gated — Cloudflare Wallets has opened only handle claiming with the wallet itself to follow, WriteGuard is in private beta ahead of general availability, and Drata's coverage beyond Anthropic is still in development — so next week's question is which of them a team can actually put in front of production traffic.
本周的三项控制能力仍处于受限状态——Cloudflare Wallets 目前只开放了账号名注册、钱包本身尚未上线，WriteGuard 在正式可用前处于私有测试，Drata 对 Anthropic 之外的覆盖仍在开发中——因此下周的问题是，其中哪一项已经可以真正挡在生产流量之前。

## Sources

- [EN] [Cloudflare Blog — @cloudflare/computer](https://blog.cloudflare.com/cloudflare-computer/)
- [EN] [arXiv — Qwen-CUA](https://arxiv.org/abs/2608.02352)
- [EN] [GitHub — xlang-ai/Qwen-CUA](https://github.com/xlang-ai/Qwen-CUA)
- [EN] [Cloudflare Blog — Cloudflare Wallets](https://blog.cloudflare.com/wallets/)
- [EN] [Fortune](https://fortune.com/2026/08/04/cloudflare-ai-agents-wallets-id/)
- [EN] [Drata](https://drata.com/about/news/drata-extends-trust-management-platform-to-continuously-monitor-and-govern-ai-agents)
- [EN] [Security Boulevard](https://securityboulevard.com/2026/08/drata-opens-limited-availability-for-ai-agent-governance-product/)
- [EN] [Cloudflare Blog — WriteGuard](https://blog.cloudflare.com/mcp-portal-writeguard-private-beta/)
- [EN] [MarkTechPost](https://www.marktechpost.com/2026/08/05/meta-superintelligence-labs-releases-muse-code/)
- [EN] [CNBC](https://www.cnbc.com/2026/08/05/meta-debuts-muse-code-to-take-on-anthropic-and-openai-.html)
- [EN] [Mistral AI](https://mistral.ai/news/shieldstral/)
- [EN] [SiliconANGLE](https://siliconangle.com/2026/08/05/mistral-introduces-shieldstral-provide-lightweight-policy-aware-moderation-ai-models/)
- [EN] [9to5Google](https://9to5google.com/2026/08/05/demis-hassabis-deepmind/)
- [EN] [The Decoder](https://the-decoder.com/google-deepmind-loses-both-its-ceo-and-chief-scientist-as-demis-hassabis-and-jeff-dean-step-down-simultaneously/)
- [中文] [IT之家 — SenseNova U1.5-Lite-Preview](https://www.ithome.com/0/985/044.htm)
- [中文] [北京商报](https://www.bbtnews.com.cn/2026/0803/601196.shtml)
- [中文] [IT之家 — SeedRealtime](https://www.ithome.com/0/985/891.htm)
- [中文] [新浪财经](https://finance.sina.com.cn/stock/t/2026-08-05/doc-inimfsht1538490.shtml)
