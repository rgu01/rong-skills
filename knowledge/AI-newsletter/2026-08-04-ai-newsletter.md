# The Week Agent Runtimes Grew Up

**Coverage:** 2026-07-29–2026-08-04 (Europe/Stockholm)

## Executive Brief

Agent infrastructure consolidated this week: herdr shipped 0.8.0 under Apache-2.0, Google took the Gemini Enterprise Agent Platform's identity, gateway, registry, runtime, evaluation, and observability layers to general availability, and AWS closed Bedrock Agents Classic to new customers in favor of AgentCore.
本周智能体基础设施明显收敛：herdr 以 Apache-2.0 许可发布 0.8.0，谷歌将 Gemini Enterprise Agent Platform 的身份、网关、注册表、运行时、评估与可观测性层推向正式可用，AWS 则关闭 Bedrock Agents Classic 的新客户入口、转向 AgentCore。

On the model side, DeepSeek, Alibaba, and MiniMax all shipped open-weight releases within four days, while OpenAI introduced its Astra family by publishing ten previously unsolved mathematics results with machine-checkable Lean certificates.
模型侧则在四天内接连出现开放权重发布：DeepSeek、阿里与 MiniMax 各自上线新模型；OpenAI 则以十项此前未解数学问题的结果、并附可机器校验的 Lean 证明，正式引出其 Astra 模型家族。

## AI Tools

<a id="story-herdr-v080-agent-multiplexer"></a>

### herdr 0.8.0 relicenses to Apache-2.0 and cuts multi-client CPU by 95%

- [X] Interesting

**Underlying event date:** 2026-08-03

**What happened**

On August 3, herdr — the terminal-native multiplexer that runs coding agents in workspaces, tabs, and panes — released v0.8.0, relicensing from AGPL-3.0-or-later to Apache-2.0 and adding `herdr --skill` to print the agent skill bundled with the running binary, Grok CLI and Antigravity CLI session restore, workspace reordering via `workspace.move_block`, configurable scrollbars and bottom tab bar, live filtering in keybind help, Windows Korean IME switching, and a Simplified Chinese README; a companion engineering post the same day reported that skipping renders for panes no client can see took a ten-pane, three-client workload from 13.014% to 0.617% CPU on Linux, replacing animated spinners with static dots took one working agent from 1.467% to 0.133%, and dropping redraws on inert mouse motion took 9.450% to 0.667%.
8 月 3 日，终端原生多路复用器 herdr——它把编码智能体组织为工作区、标签页与窗格——发布 v0.8.0，许可证从 AGPL-3.0-or-later 改为 Apache-2.0，并新增 `herdr --skill` 以打印随二进制捆绑的 agent skill、Grok CLI 与 Antigravity CLI 会话恢复、通过 `workspace.move_block` 重排工作区、可配置滚动条与底部标签栏、快捷键帮助内的实时过滤、Windows 韩文输入法切换，以及简体中文 README；同日的工程博文称，跳过任何客户端都看不到的窗格渲染，使十窗格、三客户端场景的 Linux CPU 占用从 13.014% 降至 0.617%，将动画转轮换成静态圆点使单个工作中智能体从 1.467% 降至 0.133%，而对无效鼠标移动不再重绘则从 9.450% 降至 0.667%。

**Why it matters**

Watching several long-running agents at once is a supervision problem before it is a compute problem, and a permissive license plus a runtime whose idle cost is now rounding error makes it defensible to keep ten agents attached from three machines all day instead of closing panes to save the laptop.
同时盯住多个长时间运行的智能体，首先是监督问题、其次才是算力问题；宽松许可加上空闲开销已可忽略的运行时，让"从三台机器整天挂着十个智能体"成为站得住脚的做法，而不必为省电关掉窗格。

**Sources:** [herdr GitHub Releases](https://github.com/herdrdev/herdr/releases/tag/v0.8.0) · [herdr Blog](https://herdr.dev/blog/ten-agents-three-clients-95-percent-less-cpu/)

<a id="story-gemini-enterprise-agent-platform-ga"></a>

### Google takes Gemini Enterprise Agent Platform's control plane to GA

- [ ] Interesting

**Underlying event date:** 2026-07-30

**What happened**

On July 30, Google Cloud announced general availability for Agent Runtime, which keeps an agent running continuously for up to seven days, plus Agent Memory Bank, Agent Identity as a native IAM type with least-privilege permissions and non-repudiable auditing, Agent Gateway with Model Armor protection, Agent Registry as a single library of agents and servers, Agent Evaluation with online monitors and LLM-as-a-judge metrics, and Agent Observability, alongside CodeMender, a managed agent that remediates code rather than only scanning it.
7 月 30 日，谷歌云宣布 Agent Runtime 正式可用——智能体可连续运行最多七天——同时正式可用的还有 Agent Memory Bank、作为原生 IAM 类型并提供最小权限与不可否认审计的 Agent Identity、带 Model Armor 防护的 Agent Gateway、作为智能体与服务器统一目录的 Agent Registry、支持在线监控与 LLM-as-a-judge 指标的 Agent Evaluation，以及 Agent Observability；此外还发布了托管型代码修复智能体 CodeMender，它不止扫描、还会直接修复代码。

**Why it matters**

The pieces that block production agents are rarely reasoning quality; they are who the agent is, what it may touch, whether the run is auditable, and whether it survives past a session — and a hyperscaler declaring all six GA at once turns those from bespoke plumbing into procurement line items.
阻碍智能体进入生产的通常不是推理质量，而是"智能体是谁、能碰什么、这次运行是否可审计、会话结束后能否存活"；一家超大规模云厂商一次性把这六项宣布为正式可用，意味着它们从定制管道变成了可采购的清单项。

**Sources:** [Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise-agent-platform) · [SecurityBrief](https://securitybrief.com.au/story/google-cloud-expands-gemini-enterprise-agent-controls)

<a id="story-bedrock-agents-classic-maintenance-mode"></a>

### AWS closes Bedrock Agents Classic and points everyone at AgentCore

- [ ] Interesting

**Underlying event date:** 2026-07-30

**What happened**

Effective July 30, 2026, Amazon Bedrock Agents became Bedrock Agents Classic in maintenance mode: `CreateAgent` and `InvokeInlineAgent` now return `AccessDeniedException` for accounts without Bedrock Agents activity in the prior twelve months, the Classic model catalog is frozen as of that date with no exception process, and AWS documents migration to AgentCore — either the config-based managed harness that exposes action groups as MCP tools through the gateway, or code-defined agents on AgentCore runtime running Strands, LangChain, the OpenAI Agents SDK, or the Claude Agent SDK.
自 2026 年 7 月 30 日起，Amazon Bedrock Agents 更名为处于维护模式的 Bedrock Agents Classic：对过去十二个月内没有 Bedrock Agents 使用记录的账户，`CreateAgent` 与 `InvokeInlineAgent` 将返回 `AccessDeniedException`，Classic 的模型目录自该日冻结且不设例外流程；AWS 同时给出迁移到 AgentCore 的路径——既可用基于配置的托管 harness（通过网关把 action group 暴露为 MCP 工具），也可在 AgentCore 运行时上部署自定义代码智能体，运行 Strands、LangChain、OpenAI Agents SDK 或 Claude Agent SDK。

**Why it matters**

A 2023-era managed agent loop being frozen rather than extended is the clearest signal yet that the durable layer is runtime, gateway, memory, identity, and observability as separate services — and teams still on Classic now have a no-deadline but no-new-features road ahead of them.
把 2023 年那代托管智能体循环冻结而非继续演进，是迄今最清晰的信号：真正持久的分层是把运行时、网关、记忆、身份与可观测性拆成独立服务；仍留在 Classic 上的团队面前是一条没有截止期、但也不会再有新功能的路。

**Sources:** [AWS Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-classic-maintenance-mode.html)

<a id="story-langchain-reviewbench-code-review-agents"></a>

### ReviewBench scores code-review agents against real reviewer findings

- [ ] Interesting

**Underlying event date:** 2026-07-31

**What happened**

On July 31, LangChain published ReviewBench, 59 reproducible Harbor tasks covering 64 baseline issues curated from substantive human review comments in the LangSmith mono-repo — including codebase-specific standards such as missing tenant constraints on database queries and production crons that must follow existing locking patterns — and reported that strongest baseline runs under a basic Deep Agents harness recovered roughly 30% of curated reviewer findings across Claude Opus 4.8, Kimi K3, and Luna, with a structured review prompt lifting Luna to 0.32 F1 on a 20-task slice.
7 月 31 日，LangChain 发布 ReviewBench：从 LangSmith 单体仓库中真实、有实质内容的人工评审意见整理出 59 个可复现的 Harbor 任务、覆盖 64 个基线问题——其中包含仓库特有规范，例如数据库查询缺少租户约束、生产环境定时任务必须遵循既有加锁模式；结果显示，在基础 Deep Agents harness 下，Claude Opus 4.8、Kimi K3 与 Luna 的最佳基线运行仅找回约 30% 的评审发现，而结构化评审提示词把 Luna 在 20 任务子集上提升到 0.32 F1。

**Why it matters**

Code review is where agent-written code either gets caught or ships, and a benchmark built from one team's own reviewer comments measures the thing that actually matters — repo-specific standards no general model has read — while showing the gap is still large enough that prompt structure moves the needle as much as model choice.
代码评审是智能体所写代码被拦下或被放行的关口；用某个团队自己的评审意见构建基准，衡量的正是真正要紧的东西——通用模型没读过的仓库专有规范——同时也说明差距仍大到"提示词结构"与"换模型"影响相当。

**Sources:** [LangChain Blog](https://www.langchain.com/blog/evaluating-code-review-agents-with-reviewbench)

<a id="story-cequence-ai-gateway-agentic-zero-trust"></a>

### Cequence binds MCP, LLM, and API calls to one agent identity

- [ ] Interesting

**Underlying event date:** 2026-07-30

**What happened**

On July 30, Cequence announced four AI Gateway capabilities — AI Discovery, API Registry, LLM Registry, and Skill Registry — and upgraded Agent Personas so that an agent's job description binds directly to its model, tools, access, and guardrails, with MCP governing tool discovery and invocation, the LLM Registry governing every model call, and the API Registry governing backend and data reach under a single agent-bound identity the company calls Agentic Zero Trust.
7 月 30 日，Cequence 宣布 AI Gateway 新增四项能力——AI Discovery、API Registry、LLM Registry 与 Skill Registry——并升级 Agent Personas，使智能体的职责描述直接绑定其模型、工具、访问权限与防护策略：MCP 管控工具发现与调用，LLM Registry 管控每一次模型调用，API Registry 管控对后端与数据的访问，全部收归到公司称为 Agentic Zero Trust 的单一智能体身份之下。

**Why it matters**

Most agent governance today is three disconnected policies — one for tools, one for models, one for APIs — and collapsing them onto a single identity is what lets a finance or HR team stand up a governed agent without a bespoke security review for each integration.
如今多数智能体治理其实是三套互不相连的策略——工具一套、模型一套、API 一套；把它们折叠到同一个身份上，才使财务或人力团队能自行搭起受治理的智能体，而不必为每个集成单独走一遍安全评审。

**Sources:** [GlobeNewswire](https://finance.yahoo.com/technology/ai/articles/cequence-brings-agentic-zero-trust-130000691.html) · [SecurityBrief UK](https://securitybrief.co.uk/story/cequence-adds-ai-gateway-controls-for-agentic-zero-trust)

<a id="story-nimble-web-search-agents"></a>

### Nimble ships domain-learning web search agents over API, SDK, and MCP

- [ ] Interesting

**Underlying event date:** 2026-07-29

**What happened**

On July 29, Nimble launched Web Search Agents, which learn a customer's domain to run complex web research — low-latency search, deep research, and structured dataset generation — exposed via API, SDK, and MCP, with published benchmarks claiming a 21-point gain in answer quality and 51% fewer tokens per query against leading alternatives, on infrastructure the company says already serves more than 90 million searches daily.
7 月 29 日，Nimble 发布 Web Search Agents：它会学习客户所在领域，以执行复杂的网络研究——低延迟搜索、深度研究与结构化数据集生成——并通过 API、SDK 与 MCP 提供；公开基准称相较主流替代方案，答案质量提升 21 分、每次查询 token 消耗减少 51%，其底层设施据称日均已承载超过 9000 万次搜索。

**Why it matters**

Retrieval is where research agents quietly burn most of their context budget, so a tool that halves tokens per query while raising answer quality changes the economics of every deep-research loop — and shipping it as an MCP server means the swap is a config change, not a rewrite.
检索是研究型智能体悄悄消耗大部分上下文预算的地方；一个把每次查询 token 减半、同时提升答案质量的工具会改变每一轮深度研究的经济性——而以 MCP server 形式提供，意味着替换只是改配置、而非重写。

**Sources:** [VentureBeat](https://venturebeat.com/orchestration/nimble-claims-its-new-domain-specialized-web-search-agents-cut-token-costs-in-half-while-boosting-retrieval-accuracy) · [SiliconANGLE](https://siliconangle.com/2026/07/29/nimble-launches-web-search-agents-cut-ai-research-token-costs/)

## Other AI Stories

<a id="story-openai-astra-lean-certified-proofs"></a>

### OpenAI introduces Astra with ten Lean-certified mathematical results

- [X] Interesting

**Underlying event date:** 2026-08-01

**What happened**

On August 1, OpenAI revealed its next major model family, Astra, by publishing new results on ten problems open for at least a decade — spanning high-dimensional geometry, coding theory, group theory, quantum complexity, lattice cryptography, and extremal combinatorics, including the existence of non-sofic groups — together with machine-checkable Lean proofs and reasoning walkthroughs, stating the tokens behind all ten solutions would have cost roughly $2,000 at Sol API rates, with the model itself still unreleased.
8 月 1 日，OpenAI 通过公布十个至少悬置十年的问题的新结果，正式引出其下一代主要模型家族 Astra——涵盖高维几何、编码理论、群论、量子复杂性、格密码与极值组合，其中包括非 sofic 群的存在性——同时发布可机器校验的 Lean 证明与推理过程说明，并称按 Sol 的 API 价格，产生这十个解所用的 token 约合 2000 美元；模型本身尚未发布。

**Why it matters**

Publishing Lean certificates alongside the prose is the difference between a claim a reader must trust and one a proof checker can settle, which is exactly the division of labor that makes machine-generated mathematics reviewable — and it sets a bar that "our model solved it" announcements without certificates now fall short of.
在文字论证之外附上 Lean 证明，区别在于读者只能选择相信，还是证明检查器可以直接裁决——这正是让机器生成的数学变得可复核的分工方式，也让此后没有证明附件的"我们的模型解出来了"式公告显得不足。

**Sources:** [The Decoder](https://the-decoder.com/openai-announces-its-next-major-model-astra-by-dropping-ten-previously-unsolved-math-solutions/) · [Forbes](https://www.forbes.com/sites/jonmarkman/2026/08/03/openais-astra-solved-10-decades-old-math-problems-for-just-2000/)

<a id="story-deepseek-v4-flash-0731-open-weights"></a>

### DeepSeek-V4-Flash-0731 正式版上线，智能体能力大幅跃升

- [ ] Interesting

**事件发生日期：** 2026-07-31

**发生了什么**

7 月 31 日，DeepSeek 未开发布会、仅通过 API 更新日志上线 DeepSeek-V4-Flash-0731 正式版并同步以 MIT 许可在 Hugging Face 放出权重，模型结构与规模与此前预览版一致（2840 亿总参数、130 亿激活的 MoE、100 万 token 上下文），提升全部来自重新后训练：Terminal-Bench 2.1 从 56.9 升至 82.7，DeepSWE 从 7% 升至 54.4%，Cybergym 从 52.7 升至 76.7，并原生支持 Responses API 以适配 Codex。

**为什么重要**

在结构与参数完全不变的前提下，仅靠后训练就把终端与代码智能体基准推高二十余分，说明当前开放权重模型在智能体能力上的余量更多藏在训练数据与流程里，而不是继续堆参数；MIT 许可则让这份提升可以直接进入商业自建部署。

**信息来源：** [IT之家](https://www.ithome.com/0/984/116.htm) · [观察者网](https://www.guancha.cn/economy/2026_07_31_825764.shtml)

<a id="story-qwen38-max-open-weights"></a>

### 阿里发布 Qwen3.8-Max：2.4 万亿参数，Max 级别首次开放权重

- [ ] Interesting

**事件发生日期：** 2026-08-03

**发生了什么**

8 月 3 日，阿里通义千问团队正式发布 Qwen3.8-Max，这是 7 月 19 日预览版的正式版本：2.4 万亿总参数、约 950 亿激活的 MoE 稀疏架构、100 万 token 上下文并支持多模态输入，官方称其可连续自主工作 16 天端到端交付一个真实项目，权重将于下周开源并同步开源 Qwen3.8-27B。

**为什么重要**

Max 级别旗舰首次开放权重，意味着参数规模突破 2 万亿的模型不再只属于闭源 API 调用方；而"连续自主工作十六天交付项目"这一宣称，把评价重心从单轮代码质量转向长程任务的可持续执行，这恰恰是自建智能体基础设施的团队最难自行验证的一环。

**信息来源：** [AIHub](https://www.aihub.cn/news/qwen3-8-max-release/) · [少数派](https://sspai.com/post/113053)

<a id="story-minimax-h3-open-source-video"></a>

### MiniMax H3 开源：33B 多模态视频模型，支持 15 秒 2K 原生立体声

- [ ] Interesting

**事件发生日期：** 2026-08-03

**发生了什么**

8 月 3 日，MiniMax 正式开源 7 月 31 日发布的通用多模态生成模型 H3：模型体量仅 330 亿参数，可统一理解文本、图像、视频与音频构成的多模态上下文，并输出带原生立体声的视听内容，最高支持 15 秒 2K 分辨率，定价 0.8 元/秒（2K）约为同级旗舰的三分之一，Hugging Face、魔搭与 ComfyUI 等社区已完成适配。

**为什么重要**

把带原生音轨的视频生成压到 330 亿参数并开源，意味着这类生成能力可以进入本地与私有部署的流水线，而不必每一帧都经过外部 API——对需要控制素材与数据流向的团队，这比再高一点的榜单分数更有意义。

**信息来源：** [腾讯新闻](https://news.qq.com/rain/a/20260803A064OC00) · [新京报](https://www.bjnews.com.cn/detail/1785474644129260.html)

<a id="story-horizon3-series-e-autonomous-pentesting"></a>

### Horizon3 raises $250M for autonomous pentesting at a $2B+ valuation

- [ ] Interesting

**Underlying event date:** 2026-08-03

**What happened**

On August 3, Horizon3 announced an oversubscribed $250 million Series E co-led by existing investors NightDragon and NEA at a valuation above $2 billion — roughly triple its $650 million Series D from just over a year earlier, bringing total funding to $428.5 million — to expand sales into Australia and Singapore and to fund autonomous blue-team agents that remediate the vulnerabilities its NodeZero pentesting product finds.
8 月 3 日，Horizon3 宣布完成 2.5 亿美元超额认购的 E 轮融资，由现有投资方 NightDragon 与 NEA 联合领投，估值超过 20 亿美元——约为一年多前 D 轮 6.5 亿美元估值的三倍，累计融资达 4.285 亿美元——资金将用于向澳大利亚和新加坡拓展销售，并投入自主蓝队智能体，直接修复其 NodeZero 渗透测试产品发现的漏洞。

**Why it matters**

Tripling a security valuation on the promise of agents that both find and fix is a bet that the scarce resource is remediation capacity, not detection — and it puts autonomous change-making agents inside production infrastructure, where the approval and audit questions raised by this week's identity and gateway launches stop being hypothetical.
以"既能发现又能修复的智能体"为前提让安全公司估值翻三倍，赌的是稀缺资源在修复能力而非检测能力；这也把会自主实施变更的智能体放进了生产基础设施——本周身份与网关类发布所提出的审批与审计问题，在这里不再是假设。

**Sources:** [TechCrunch](https://techcrunch.com/2026/08/03/horizon3-hits-2-billion-valuation-with-250m-series-e-as-ai-threats-escalate/) · [Help Net Security](https://www.helpnetsecurity.com/2026/08/03/horizon3-ai-250-million-funding/)

## Follow-ups to Interesting Stories

### Stripe ships a company-wide Deep Agents deployment to 5,000 users

**Original interest:** [Deep Agents v0.7 cuts base input tokens by 65%](2026-07-31-ai-newsletter.md#story-deep-agents-v07-token-diet)

**Underlying event date:** 2026-08-03

**What changed**

On August 3, LangChain published Stripe's account of Kai, its Knowledge AI Platform built on Deep Agents in one week by a single staff engineer, which grew from 296 to 5,000 users in about four weeks, now sees 83% of its users weekly across more than 60,000 sessions, and layers S3-backed filesystem, sandbox, and summarization middleware under a two-pass skill selector drawing on 1,000+ skills from 100+ teams and 500+ internal MCP tools.
8 月 3 日，LangChain 发布了 Stripe 关于 Kai 的实践记录：这一知识 AI 平台由一名资深工程师基于 Deep Agents 在一周内建成，约四周内用户从 296 增至 5000，目前每周有 83% 的用户使用、累计超过 6 万个会话；其架构在 S3 支撑的文件系统、沙箱与摘要中间件之上，用两轮技能选择器调度来自 100 多个团队的 1000 多项 skill 与 500 多个内部 MCP 工具。

**Why it matters**

The token-diet release read as a cost optimization; this deployment shows what the same middleware stack carries at scale — federated skill ownership across a hundred teams, with dynamic tool loading rather than one giant tool list — which is the part that decides whether an internal agent platform survives its second year.
上一期的"省 token"发布看起来只是成本优化；这次落地则显示同一套中间件在规模化时承担了什么——上百个团队各自维护 skill、通过动态加载而非一份巨大的工具清单来调度——而这恰恰决定一个内部智能体平台能否活到第二年。

**Sources:** [LangChain Blog](https://www.langchain.com/blog/how-stripe-built-their-knowledge-ai-platform-on-deep-agents)

## Tracked Interests

- **[NVIDIA releases Cosmos 3 Edge for local physical AI](2026-07-24-ai-newsletter.md#story-nvidia-cosmos-3-edge-siggraph)** — Marked 2026-07-24. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[OpenAI rolls out Health in ChatGPT to U.S. users](2026-07-27-ai-newsletter.md#story-chatgpt-health-rollout)** — Marked 2026-07-27. No qualifying update found this week; the in-window coverage found reported the same July 23 rollout. Uncheck `Interesting` in the original story to stop tracking it.
- **[月之暗面正式开源 Kimi K3](2026-07-29-ai-newsletter.md#story-kimi-k3-open-source)** — Marked 2026-07-29. No qualifying update found this week; the reported August pre-IPO round has no exact dated event yet. Uncheck `Interesting` in the original story to stop tracking it.
- **[Reader spotlight: SpecForge pairs LLMs with formal specifications](2026-07-29-ai-newsletter.md#story-imiron-specforge-ai-formal-specs)** — Marked 2026-07-29. No qualifying update found this week; Imiron's newsroom shows nothing after June 10, 2026. Uncheck `Interesting` in the original story to stop tracking it.
- **[LangSmith LLM Gateway enters public beta as a runtime control plane](2026-07-31-ai-newsletter.md#story-langsmith-llm-gateway-public-beta)** — Marked 2026-07-31. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[Deep Agents v0.7 cuts base input tokens by 65%](2026-07-31-ai-newsletter.md#story-deep-agents-v07-token-diet)** — Marked 2026-07-31. Qualifying follow-up included above. Uncheck `Interesting` in the original story to stop tracking it.
- **[BrowserStack puts an agentic testing harness inside the IDE](2026-07-31-ai-newsletter.md#story-browserstack-test-companion-ide)** — Marked 2026-07-31. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.

## Watch Next Week

Whether Alibaba actually publishes the Qwen3.8-Max and Qwen3.8-27B weights on the stated next-week schedule is the near-term test of how open the 2-trillion-parameter tier really becomes.
阿里是否按其所述的"下周"节奏真正放出 Qwen3.8-Max 与 Qwen3.8-27B 权重，是万亿级参数这一档究竟有多开放的近期检验。

With AWS freezing Bedrock Agents Classic and Google declaring its identity, gateway, and registry layers GA in the same week, expect the next round of agent-platform announcements to be judged on migration paths rather than new primitives.
在 AWS 冻结 Bedrock Agents Classic、谷歌同周宣布身份、网关与注册表层正式可用之后，下一轮智能体平台公告更可能以迁移路径、而非新原语来衡量。

## Sources

- [EN] [herdr GitHub Releases](https://github.com/herdrdev/herdr/releases/tag/v0.8.0)
- [EN] [herdr Blog](https://herdr.dev/blog/ten-agents-three-clients-95-percent-less-cpu/)
- [EN] [Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise-agent-platform)
- [EN] [SecurityBrief](https://securitybrief.com.au/story/google-cloud-expands-gemini-enterprise-agent-controls)
- [EN] [AWS Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-classic-maintenance-mode.html)
- [EN] [LangChain Blog — ReviewBench](https://www.langchain.com/blog/evaluating-code-review-agents-with-reviewbench)
- [EN] [GlobeNewswire — Cequence](https://finance.yahoo.com/technology/ai/articles/cequence-brings-agentic-zero-trust-130000691.html)
- [EN] [SecurityBrief UK](https://securitybrief.co.uk/story/cequence-adds-ai-gateway-controls-for-agentic-zero-trust)
- [EN] [VentureBeat](https://venturebeat.com/orchestration/nimble-claims-its-new-domain-specialized-web-search-agents-cut-token-costs-in-half-while-boosting-retrieval-accuracy)
- [EN] [SiliconANGLE](https://siliconangle.com/2026/07/29/nimble-launches-web-search-agents-cut-ai-research-token-costs/)
- [EN] [The Decoder](https://the-decoder.com/openai-announces-its-next-major-model-astra-by-dropping-ten-previously-unsolved-math-solutions/)
- [EN] [Forbes](https://www.forbes.com/sites/jonmarkman/2026/08/03/openais-astra-solved-10-decades-old-math-problems-for-just-2000/)
- [EN] [TechCrunch](https://techcrunch.com/2026/08/03/horizon3-hits-2-billion-valuation-with-250m-series-e-as-ai-threats-escalate/)
- [EN] [Help Net Security](https://www.helpnetsecurity.com/2026/08/03/horizon3-ai-250-million-funding/)
- [EN] [LangChain Blog — Stripe Kai](https://www.langchain.com/blog/how-stripe-built-their-knowledge-ai-platform-on-deep-agents)
- [中文] [IT之家](https://www.ithome.com/0/984/116.htm)
- [中文] [观察者网](https://www.guancha.cn/economy/2026_07_31_825764.shtml)
- [中文] [AIHub](https://www.aihub.cn/news/qwen3-8-max-release/)
- [中文] [少数派](https://sspai.com/post/113053)
- [中文] [腾讯新闻](https://news.qq.com/rain/a/20260803A064OC00)
- [中文] [新京报](https://www.bjnews.com.cn/detail/1785474644129260.html)
