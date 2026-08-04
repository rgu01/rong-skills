# Agent Plumbing Gets Serious: Gateways, Harnesses, and Cheaper Tokens

**Coverage:** 2026-07-25–2026-07-31 (Europe/Stockholm)

## Executive Brief

The week's agent tooling converged on control rather than capability: LangChain put its LLM Gateway into public beta on July 30 with spend caps, rate limits, and provider fallbacks, while Microsoft's Agent Framework shipped reusable session stores and bounded MCP skill discovery the same day.
本周的智能体工具进展集中在"控制"而非"能力"：LangChain 于 7 月 30 日将 LLM Gateway 推入公测，提供额度上限、限流与供应商回退；同日微软 Agent Framework 发布了可复用会话存储与有界的 MCP 技能发现。

On the economics side, OpenAI cut GPT-5.6 Luna prices by 80% and Terra by 20% on July 30, and Moonshot AI closed an oversubscribed F round of more than $3.5 billion on July 29 days after open-sourcing Kimi K3.
在经济层面，OpenAI 于 7 月 30 日将 GPT-5.6 Luna 价格下调 80%、Terra 下调 20%；月之暗面则在开源 Kimi K3 数天后，于 7 月 29 日完成超 35 亿美元的超募 F 轮融资。

## AI Tools

<a id="story-langsmith-llm-gateway-public-beta"></a>

### LangSmith LLM Gateway enters public beta as a runtime control plane

- [X] Interesting

**Underlying event date:** 2026-07-30

**What happened**

On July 30, LangChain moved LangSmith LLM Gateway into public beta for Plus and Enterprise plans, adding spend caps and rate limits at organization, workspace, API-key, and user level, automatic model fallbacks across OpenAI, Anthropic, Fireworks, and custom endpoints, per-customer multi-tenant policies via custom headers, and Enterprise-only PII and secrets redaction before data reaches a provider.
7 月 30 日，LangChain 将 LangSmith LLM Gateway 推入面向 Plus 与 Enterprise 套餐的公测，新增组织、工作区、API 密钥与用户四级的额度上限与限流，支持在 OpenAI、Anthropic、Fireworks 及自定义端点之间自动回退模型，可通过自定义请求头实现按客户的多租户策略，并为 Enterprise 提供在数据到达模型供应商前的 PII 与密钥脱敏。

**Why it matters**

Cost overruns and data leakage are the two failure modes that most often stop an agent from reaching production, and putting both behind one gateway that also routes Claude Code, Codex, and Deep Agents Code traffic means governance stops being per-application glue code.
成本失控与数据泄露是阻止智能体进入生产环境的两大典型故障模式；把两者一并收归到同一个网关，并让它同时代理 Claude Code、Codex 与 Deep Agents Code 的流量，意味着治理不再依赖每个应用各自的胶水代码。

**Sources:** [LangChain Blog](https://www.langchain.com/blog/langsmith-llm-gateway-runtime-controls-for-production-agents)

<a id="story-deep-agents-v07-token-diet"></a>

### Deep Agents v0.7 cuts base input tokens by 65%

- [X] Interesting

**Underlying event date:** 2026-07-29

**What happened**

LangChain released Deep Agents v0.7 on July 29, reporting 65% fewer base input tokens at comparable performance by dropping the default system prompt, trimming tool descriptions by 43%, and making TodoListMiddleware opt-in, alongside overridable built-in middleware, `write_file` overwrite semantics, paginated reads that report remaining lines, and grep/glob calls that return truncated partial results instead of hanging on large trees.
LangChain 于 7 月 29 日发布 Deep Agents v0.7，通过移除默认系统提示词、将工具描述精简 43%、并把 TodoListMiddleware 改为按需启用，在性能相当的前提下将基础输入 token 减少 65%；同时支持覆盖内置中间件，`write_file` 改为直接覆盖已有文件，分页读取会报告剩余行数，grep/glob 在大型目录树上返回带截断标记的部分结果而不再挂起。

**Why it matters**

A harness that spends fewer tokens before the agent does any work lowers the per-run floor on every deep-research or coding loop, and the middleware-override path lets teams tune summarization thresholds without forking the framework.
在智能体尚未开始工作前就少花 token 的框架，会拉低每一次深度研究或编码循环的成本下限；而中间件覆盖机制让团队可以在不 fork 框架的前提下调整摘要触发阈值。

**Sources:** [LangChain Blog](https://www.langchain.com/blog/deep-agents-v0-7)

<a id="story-microsoft-agent-framework-session-stores"></a>

### Microsoft Agent Framework ships session stores and bounded MCP skill discovery

- [ ] Interesting

**Underlying event date:** 2026-07-30

**What happened**

Microsoft published Agent Framework `python-1.13.0` and `dotnet-1.16.0` on July 30, adding bounded in-memory archive skill discovery for MCP sources and reusable session stores that persist complete Foundry Responses sessions on the Python side, and in-memory chat-history persistence plus a GitHub Copilot agent graduating to stable on the .NET side.
微软于 7 月 30 日发布 Agent Framework `python-1.13.0` 与 `dotnet-1.16.0`：Python 侧新增面向 MCP 源的有界内存归档技能发现，以及可复用的会话存储（可完整持久化 Foundry Responses 会话）；.NET 侧新增内存内聊天历史持久化，并将 GitHub Copilot 智能体提升为稳定版。

**Why it matters**

Durable session state and a bounded skill index are the unglamorous pieces that decide whether a long-running agent can be resumed and audited after a crash, and stable-graduating packages signal the surface is safe to build against.
持久化的会话状态与有界的技能索引，正是决定长时运行智能体在崩溃后能否恢复与审计的"不起眼"组件；而软件包升为稳定版，则表明该接口面已可安全地作为构建基础。

**Sources:** [Microsoft Agent Framework releases](https://github.com/microsoft/agent-framework/releases)

<a id="story-browserstack-test-companion-ide"></a>

### BrowserStack puts an agentic testing harness inside the IDE

- [X] Interesting

**Underlying event date:** 2026-07-29

**What happened**

BrowserStack launched Test Companion on July 29 from Dublin, an IDE-resident agent that generates test cases, authors and runs scripts, diagnoses failures, and validates across more than 30,000 real devices and browsers for functional, visual, accessibility, and API testing, installing from the VS Code, JetBrains, Cursor, and Antigravity marketplaces and working with existing Playwright, Selenium, Cypress, and Appium suites.
BrowserStack 于 7 月 29 日在都柏林发布 Test Companion，这是一个驻留在 IDE 内的智能体，可生成测试用例、编写并运行脚本、诊断失败，并在 3 万多台真实设备与浏览器上完成功能、视觉、无障碍与 API 测试；它从 VS Code、JetBrains、Cursor 与 Antigravity 的应用市场安装，并可直接对接既有的 Playwright、Selenium、Cypress 与 Appium 测试套件。

**Why it matters**

Coding agents have widened the gap between commits and releases, and a testing agent that owns authoring, execution, and maintenance against real devices attacks the verification bottleneck rather than adding more generated code to review.
编码智能体已经拉大了提交量与发布量之间的差距；一个同时负责编写、执行与维护、并在真实设备上验证的测试智能体，直接针对验证瓶颈发力，而不是再产出更多需要人工审阅的代码。

**Sources:** [PR Newswire](https://www.prnewswire.com/news-releases/browserstack-launches-test-companion-agentic-ai-that-brings-complete-test-automation-into-the-ide-302837727.html)

<a id="story-openai-terraform-provider"></a>

### OpenAI ships an official Terraform provider for platform governance

- [ ] Interesting

**Underlying event date:** 2026-07-29

**What happened**

OpenAI released its official Terraform provider on July 29, letting teams provision and manage projects, users, groups, roles, access assignments, service accounts, certificates, invitations, rate limits, and spend alerts through the Administration API with standard plan/apply workflows, resource import, and drift detection.
OpenAI 于 7 月 29 日发布官方 Terraform provider，团队可通过 Administration API，以标准的 plan/apply 流程、资源导入与配置漂移检测，来创建和管理项目、用户、用户组、角色、访问授权、服务账号、证书、邀请、速率限制与消费告警。

**Why it matters**

Agent fleets multiply service accounts and API keys faster than any console workflow can track, so declaring identity, permissions, and spend limits as reviewable code is what makes agent access auditable instead of accreted.
智能体集群产生服务账号与 API 密钥的速度，快过任何控制台流程所能跟踪的范围；把身份、权限与消费上限声明为可评审的代码，才能让智能体的访问权限可审计，而不是层层堆积。

**Sources:** [OpenAI API Changelog](https://developers.openai.com/api/docs/changelog) · [OpenAI Terraform guide](https://developers.openai.com/api/docs/guides/terraform)

<a id="story-exabase-m1-beam-memory"></a>

### Exabase M-1 tops the BEAM memory benchmark at every scale

- [ ] Interesting

**Underlying event date:** 2026-07-29

**What happened**

Exabase reported on July 29 that its M-1 memory engine holds the highest published BEAM scores at every evaluated corpus size — 76.9% at 100K tokens, 75.0% at 1M, and 68.0% at 10M — leading the previous best system by 3.9 points at 10M while running on Gemini 3 Flash and consuming roughly 20% fewer tokens per query.
Exabase 于 7 月 29 日公布，其 M-1 记忆引擎在 BEAM 基准的每个语料规模上都取得已公开的最高分——10 万 token 下 76.9%、100 万 token 下 75.0%、1000 万 token 下 68.0%——在 1000 万 token 规模上领先此前最佳系统 3.9 个百分点，且运行在 Gemini 3 Flash 上、每次查询消耗的 token 约减少 20%。

**Why it matters**

Long-horizon agents fail on recall long before they fail on reasoning, and a retrieval layer that beats larger-model baselines on 10M-token corpora suggests memory quality is an engineering problem teams can buy down without upgrading the model.
长周期智能体往往先在"记得住"上失败，而不是先在推理上失败；一个在 1000 万 token 语料上击败更大模型基线的检索层，说明记忆质量是可以通过工程投入解决、而无需升级模型的问题。

**Sources:** [Exabase](https://exabase.io/blog/exabase-m1-achieves-state-of-the-art-on-beam-benchmark)

## Other AI Stories

<a id="story-openai-gpt56-price-cuts-fast-mode"></a>

### OpenAI cuts GPT-5.6 Luna 80% and replaces Priority Processing with Fast mode

- [ ] Interesting

**Underlying event date:** 2026-07-30

**What happened**

On July 30 OpenAI lowered GPT-5.6 Luna to $0.20 per million input and $1.20 per million output tokens and Terra to $2 and $12 while leaving Sol at $5 and $30, and introduced Fast mode in place of Priority Processing at up to 2.5× standard speed for twice the price, attributing the cuts to GPU kernel work that reduced serving cost by 20% and improved token-generation efficiency by over 15%.
7 月 30 日，OpenAI 将 GPT-5.6 Luna 降至每百万输入 token 0.20 美元、输出 1.20 美元，Terra 降至 2 美元与 12 美元，Sol 维持 5 美元与 30 美元；同时以 Fast mode 取代 Priority Processing，以两倍价格提供最高 2.5 倍于标准处理的速度，并将降价归因于 GPU 内核优化——服务成本下降 20%、token 生成效率提升超过 15%。

**Why it matters**

An 80% cut three weeks after general availability resets the unit economics of high-volume classification, extraction, and agent sub-calls, and it moves the cost lever from model choice to explicit speed purchasing.
在正式可用仅三周后就降价 80%，重置了大批量分类、抽取与智能体子调用的单位经济性，也把成本杠杆从"选哪个模型"转向"显式地购买速度"。

**Sources:** [Unite.AI](https://www.unite.ai/openai-cuts-api-prices-on-its-two-cheaper-gpt-5-6-tiers/)

<a id="story-stairwell-backstory-blast-radius"></a>

### Stairwell launches Backstory to map malware blast radius

- [ ] Interesting

**Underlying event date:** 2026-07-29

**What happened**

Stairwell announced Backstory on July 29, an agentic investigation platform that starts from files collected on customer endpoints rather than alerts, tracing related malware variants, where they appeared, and how long they have been present, backed by a preserved corpus of more than 1.5 billion executables, 110,000 detection rules, and 8.7 billion historical rule matches.
Stairwell 于 7 月 29 日发布 Backstory，这是一个以智能体驱动的调查平台，从客户端点收集到的文件出发（而非从告警出发），追溯相关恶意软件变种、其出现位置及潜伏时长；其底层留存了超过 15 亿个可执行文件、11 万条检测规则与 87 亿次历史规则命中记录。

**Why it matters**

Stairwell's own report finds an average of 2.4 additional variants behind every published hash, so an investigation loop that enumerates variants and affected hosts targets exactly the residue that signature-based containment leaves behind.
Stairwell 自身的报告发现，每一个已公开的哈希背后平均还有 2.4 个额外变种；因此一个能够枚举变种与受影响主机的调查闭环，正好针对基于签名的处置所留下的残余风险。

**Sources:** [Help Net Security](https://www.helpnetsecurity.com/2026/07/29/stairwell-backstory-agentic-investigation/)

<a id="story-moonshot-series-f-oversubscribed"></a>

### 月之暗面完成超 35 亿美元 F 轮融资

- [ ] Interesting

**事件发生日期：** 2026-07-29

**发生了什么**

7 月 29 日消息，月之暗面已完成 F 轮融资，金额超过 35 亿美元，投后估值达 350 亿美元；由于实际认购规模超出目标金额三倍多，本轮提前关闭，原定 8 月启动的 G 轮（Pre-IPO 轮）已提前开始，投前估值升至 500 亿美元，公司最初的融资区间仅为 10 亿至 20 亿美元。

**为什么重要**

一家刚刚把 2.8 万亿参数旗舰模型完整开源的公司，在数天内以超募三倍的规模关闭融资并提前启动 Pre-IPO 轮，说明"开放权重"路线在资本市场上已不再被视为对商业化的让步，而是估值的支撑面。

**信息来源：** [澎湃新闻](https://m.thepaper.cn/newsDetail_forward_33682828) · [IT之家](https://www.ithome.com/0/983/170.htm)

## Follow-ups to Interesting Stories

No marked story had a qualifying update inside this week's coverage window. Every tracked item is listed below with its exact status.
本周覆盖窗口内，没有任何已标记故事出现符合条件的新进展。所有跟踪条目及其确切状态均列于下方。

## Tracked Interests

- **[NVIDIA releases Cosmos 3 Edge for local physical AI](2026-07-24-ai-newsletter.md#story-nvidia-cosmos-3-edge-siggraph)** — Marked 2026-07-24. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[OpenAI rolls out Health in ChatGPT to U.S. users](2026-07-27-ai-newsletter.md#story-chatgpt-health-rollout)** — Marked 2026-07-27. No qualifying update found this week; the all-plans expansion and connected-records change were reported on 2026-07-24, before this window opened. Uncheck `Interesting` in the original story to stop tracking it.
- **[月之暗面正式开源 Kimi K3](2026-07-29-ai-newsletter.md#story-kimi-k3-open-source)** — Marked 2026-07-29. No qualifying update found this week; the F-round financing reported on 2026-07-29 is a separate corporate event and appears above as its own story. Uncheck `Interesting` in the original story to stop tracking it.
- **[Reader spotlight: SpecForge pairs LLMs with formal specifications](2026-07-29-ai-newsletter.md#story-imiron-specforge-ai-formal-specs)** — Marked 2026-07-29. No qualifying update found this week; Imiron's most recent dated announcement remains its 2026-06-10 accelerator selection. Uncheck `Interesting` in the original story to stop tracking it.

## Watch Next Week

Moonshot's G round was described on July 29 as possibly closing within the following week at a $50 billion pre-money valuation, so the next dated financing disclosure is the one to watch.
月之暗面的 G 轮在 7 月 29 日被描述为"可能下周关闭"、投前估值 500 亿美元，因此下一份带日期的融资披露值得重点关注。

LangChain's gateway ships PII redaction only on Enterprise while Microsoft's Agent Framework has just stabilized its Copilot agent surface, which sets up a near-term split between governance sold as a plan tier and governance shipped in the runtime.
LangChain 的网关仅在 Enterprise 套餐提供 PII 脱敏，而微软 Agent Framework 刚刚稳定了其 Copilot 智能体接口面，这在短期内构成一种分野：治理能力究竟作为套餐档位出售，还是直接内置于运行时。

## Sources

- [EN] [LangChain Blog — LangSmith LLM Gateway](https://www.langchain.com/blog/langsmith-llm-gateway-runtime-controls-for-production-agents)
- [EN] [LangChain Blog — Deep Agents v0.7](https://www.langchain.com/blog/deep-agents-v0-7)
- [EN] [Microsoft Agent Framework releases](https://github.com/microsoft/agent-framework/releases)
- [EN] [PR Newswire — BrowserStack Test Companion](https://www.prnewswire.com/news-releases/browserstack-launches-test-companion-agentic-ai-that-brings-complete-test-automation-into-the-ide-302837727.html)
- [EN] [OpenAI API Changelog](https://developers.openai.com/api/docs/changelog)
- [EN] [OpenAI Terraform guide](https://developers.openai.com/api/docs/guides/terraform)
- [EN] [Exabase — M-1 on BEAM](https://exabase.io/blog/exabase-m1-achieves-state-of-the-art-on-beam-benchmark)
- [EN] [Unite.AI — OpenAI GPT-5.6 price cuts](https://www.unite.ai/openai-cuts-api-prices-on-its-two-cheaper-gpt-5-6-tiers/)
- [EN] [Help Net Security — Stairwell Backstory](https://www.helpnetsecurity.com/2026/07/29/stairwell-backstory-agentic-investigation/)
- [中文] [澎湃新闻 — 月之暗面 F 轮融资](https://m.thepaper.cn/newsDetail_forward_33682828)
- [中文] [IT之家 — 月之暗面融资](https://www.ithome.com/0/983/170.htm)
