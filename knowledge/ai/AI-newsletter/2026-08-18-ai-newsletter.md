# Agent Plumbing Moves to Neutral Ground

**Coverage:** 2026-08-12–2026-08-18 (Europe/Stockholm, CEST)

## Executive Brief

On August 17 the Agentic AI Foundation accepted Google's Agent2Agent protocol as a hosted project, putting agent-to-agent communication under the same Linux Foundation governance as MCP, AGENTS.md, goose, and agentgateway.
8 月 17 日，Agentic AI Foundation 接纳 Google 的 Agent2Agent 协议成为托管项目，使智能体之间的通信与 MCP、AGENTS.md、goose 和 agentgateway 归入同一个 Linux Foundation 治理体系。

The week's other through-line was the money and control layer around agents: Stripe closed a reported $7 billion-plus purchase of model gateway OpenRouter on August 16, and DoiT bought Attribute on August 17 to attribute token spend down to individual agents.
本周另一条主线是围绕智能体的资金与控制层：Stripe 于 8 月 16 日完成对模型网关 OpenRouter 报道称超过 70 亿美元的收购，DoiT 则在 8 月 17 日收购 Attribute，以便把 token 支出归因到单个智能体。

## AI Tools

<a id="story-a2a-joins-aaif"></a>

### Agent2Agent joins the Agentic AI Foundation alongside MCP

- [ ] Interesting

**Underlying event date:** 2026-08-17

**What happened**

On August 17 the Agentic AI Foundation announced that Agent2Agent — the inter-agent communication standard Google launched in April 2025 and donated to the Linux Foundation with AWS, Cisco, Microsoft, Salesforce, SAP, and ServiceNow as founding organizations — has been accepted as a hosted project, joining AGENTS.md, goose, MCP, and agentgateway under the foundation's Governing Board and Technical Committee.
8 月 17 日，Agentic AI Foundation 宣布 Agent2Agent 已被接纳为托管项目——该智能体间通信标准由 Google 于 2025 年 4 月发布，并与 AWS、Cisco、Microsoft、Salesforce、SAP、ServiceNow 作为创始组织一同捐赠给 Linux Foundation——它由此与 AGENTS.md、goose、MCP 和 agentgateway 一起，纳入该基金会治理委员会与技术委员会的管辖之下。

**Why it matters**

A2A and MCP cover complementary halves of a multi-agent system — how agents reach tools and data, and how they reach each other — and having both governed by the same neutral body means a team standardizing on the pair no longer inherits two separate vendors' roadmaps and release cycles.
A2A 与 MCP 分别覆盖多智能体系统互补的两半——智能体如何连接工具与数据，以及智能体之间如何相互连接——两者由同一个中立机构治理，意味着以这一组合为标准的团队不再需要承受两家供应商各自的路线图与发布节奏。

**Sources:** [Agentic AI Foundation](https://aaif.io/blog/a2a-joins-aaif) · [Techzine](https://www.techzine.eu/news/devops/143659/google-transfers-a2a-to-the-agentic-ai-foundation/)

<a id="story-google-zero-trust-agents-adk"></a>

### Google open-sources a zero-trust reference implementation for ADK agents

- [ ] Interesting

**Underlying event date:** 2026-08-17

**What happened**

On August 17 Google published `zero-trust-agents`, an open-source reference implementation built on its Agent Development Kit and Gemini that layers hardware-backed per-agent keys signing every database mutation, gVisor kernel-level sandboxing with zero network egress and strict resource limits for dynamically generated code, and deterministic input/output validation enforced by CI/CD test suites — shipped with a runnable CLI demo, a browser dashboard, and a customer-support-and-returns agent as the worked example.
8 月 17 日，Google 发布开源参考实现 `zero-trust-agents`：它基于自家 Agent Development Kit 与 Gemini，叠加三层机制——为每个智能体分配硬件支撑的密钥并对每一次数据库变更签名；对动态生成的代码使用 gVisor 内核级沙箱，禁止任何网络出站并施加严格资源限制；以及由 CI/CD 测试套件强制执行的确定性输入输出校验——随附可运行的 CLI 演示、浏览器仪表板，以及一个客服与退货智能体作为示例实现。

**Why it matters**

Perimeter security cannot see inside an agent whose execution path is chosen by an LLM at runtime, so a runnable reference that pins down signing, sandboxing, and validation gives teams something concrete to copy instead of inventing a prompt-injection defence per project.
当执行路径由 LLM 在运行时决定时，边界安全无法看清智能体内部，因此一个把签名、沙箱与校验都落到实处的可运行参考实现，让团队有具体范本可循，而不必为每个项目各自发明一套提示注入防御。

**Sources:** [Google Developers Blog](https://developers.googleblog.com/en/build-zero-trust-ai-agents-with-googles-agent-development-kit/)

<a id="story-cloudflare-gateway-mcp-detection"></a>

### Cloudflare Gateway can now see MCP traffic and force it through a Portal

- [ ] Interesting

**Underlying event date:** 2026-08-14

**What happened**

On August 14 Cloudflare made generally available a protocol-level heuristic that identifies MCP traffic from `MCP-Protocol-Version` headers and exposes it to Zero Trust customers as an `experimental.is_mcp == true` selector, together with a dedicated MCP dashboard showing request volume, unique servers and users, Portal-proxied versus direct connections, and shadow MCP servers reached outside approved controls; new traffic-source selectors let a policy block direct connections with `experimental.is_mcp == true and not traffic.onramp in ("mcp_portal")`, and MCP Portals gained manual pre-registered OAuth credentials.
8 月 14 日，Cloudflare 正式发布一项协议层启发式检测：它依据 `MCP-Protocol-Version` 请求头识别 MCP 流量，并以 `experimental.is_mcp == true` 选择器提供给 Zero Trust 客户；同时上线专门的 MCP 仪表板，展示请求量、唯一服务器与用户数、经 Portal 代理与直连的对比，以及绕过既有管控的影子 MCP 服务器；新的流量来源选择器允许策略以 `experimental.is_mcp == true and not traffic.onramp in ("mcp_portal")` 拦截直连，MCP Portals 也新增了手动预注册的 OAuth 凭据支持。

**Why it matters**

An organization cannot govern MCP servers it cannot enumerate, and a network-layer detector plus a hard "Portal or nothing" policy converts MCP access from something each employee configures locally into something the security team can inventory and route.
组织无法治理自己都列举不出来的 MCP 服务器；一个网络层探测器加上"只走 Portal，否则不通"的硬性策略，把 MCP 访问从每位员工各自本地配置的事情，转变为安全团队可以清点并统一路由的事情。

**Sources:** [Cloudflare Blog](https://blog.cloudflare.com/mcp-security-updates/)

<a id="story-cloudflare-access-for-workers"></a>

### Access for Workers puts company login in front of every Worker deployment

- [ ] Interesting

**Underlying event date:** 2026-08-14

**What happened**

On August 14 Cloudflare made Access for Workers available to everyone, letting an Access authentication policy attach directly to a Worker and cover custom domains, routes, `workers.dev` subdomains, and preview URLs without per-hostname configuration, with an account-level policy option that puts all preview and production deployments behind company login by default and a `ctx.access.getIdentity()` call that returns the authenticated user's email, name, and groups without manual JWT validation.
8 月 14 日，Cloudflare 向所有用户开放 Access for Workers：Access 认证策略可直接附加到 Worker 上，覆盖自定义域名、路由、`workers.dev` 子域与预览 URL，无需逐个主机名配置；账户级策略选项可让所有预览与生产部署默认置于公司登录之后，而 `ctx.access.getIdentity()` 调用则直接返回已认证用户的邮箱、姓名与所属组，无需手动校验 JWT。

**Why it matters**

Cloudflare framed the launch around AI-assisted development letting any employee deploy an internal app to the public internet by accident, which makes a default-deny account policy the cheapest available control over what agent-written and vibe-coded services expose.
Cloudflare 为这次发布给出的背景是：AI 辅助开发让任何员工都可能不经意间把内部应用部署到公网，因此一条默认拒绝的账户级策略，是对智能体编写与随手写就的服务所暴露内容最廉价的管控手段。

**Sources:** [Cloudflare Blog](https://blog.cloudflare.com/workers-protected-by-access/)

<a id="story-doit-attribute-token-attribution"></a>

### DoiT buys Attribute to price agents individually

- [ ] Interesting

**Underlying event date:** 2026-08-17

**What happened**

On August 17 DoiT announced its acquisition of Israeli startup Attribute for an estimated $65 million, taking ownership of a platform that gives organizations real-time visibility into AI and cloud spend attributed at the level of teams, products, features, individual AI agents, and individual customers; DoiT had introduced the Attribute product line on July 7, 2026 as an eBPF kernel sensor that installs in about fifteen minutes and maps token, GPU, CPU, memory, network, and I/O consumption back to the processes and requests responsible with no SDK, tagging policy, or code changes.
8 月 17 日，DoiT 宣布以估计 6500 万美元收购以色列初创公司 Attribute，接手一个能让组织实时看清 AI 与云支出、并把支出归因到团队、产品、功能、单个 AI 智能体以及单个客户层级的平台；DoiT 曾在 2026 年 7 月 7 日推出 Attribute 产品线，其形态是一个约十五分钟即可安装的 eBPF 内核传感器，能在无需 SDK、无需打标策略、无需修改代码的前提下，把 token、GPU、CPU、内存、网络与 I/O 消耗映射回产生它们的进程与请求。

**Why it matters**

Every agent cost control published this summer — spend caps, cheaper-model routing, per-engineer budgets — depends on knowing which agent spent what, and kernel-level attribution answers that without asking each application team to instrument its own calls.
今年夏天公布的每一种智能体成本管控手段——支出上限、路由到更便宜的模型、按工程师分配预算——都取决于弄清哪个智能体花了多少钱，而内核级归因无需要求每个应用团队自行为调用埋点即可给出答案。

**Sources:** [Calcalist CTech](https://www.calcalistech.com/ctechnews/article/sycvenedzx) · [DoiT](https://www.doit.com/blog/doit-launches-attribute-ai-tokenomics-without-tags-sdks-or-code-changes)

## Other AI Stories

<a id="story-stripe-acquires-openrouter"></a>

### Stripe closes a reported $7 billion-plus deal for OpenRouter

- [ ] Interesting

**Underlying event date:** 2026-08-16

**What happened**

On August 16 Stripe finalized a reported acquisition of OpenRouter for more than $7 billion, buying a gateway that gives customers one access point to over 400 models chosen by task, price, and budget, roughly five times the $1.3 billion valuation of OpenRouter's $113 million Series B that closed months earlier and below the roughly $10 billion figure reported during talks.
8 月 16 日，Stripe 完成了据报超过 70 亿美元的 OpenRouter 收购：该网关为客户提供单一接入点，可按任务、价格与预算从 400 多个模型中选择；这一价格约为数月前完成的 1.13 亿美元 B 轮融资所对应 13 亿美元估值的五倍，但低于谈判期间报道的约 100 亿美元。

**Why it matters**

A payments company owning the layer that decides which model serves a request puts routing, metering, and billing for AI in one place, and it prices model choice as infrastructure at a moment when falling model prices reportedly cut about 30% off the deal.
一家支付公司拥有决定由哪个模型响应请求的这一层，意味着 AI 的路由、计量与计费被收拢到同一处；而在模型价格下行据报使这笔交易缩水约三成之际，它把模型选择本身定价为基础设施。

**Sources:** [Fortune](https://fortune.com/2026/08/16/stripe-7-billion-deal-ai-firm-openrouter-acquisition/) · [TechCrunch](https://techcrunch.com/2026/08/16/stripe-will-reportedly-acquire-ai-gateway-startup-openrouter-for-7b/)

<a id="story-higgsfield-series-b"></a>

### Higgsfield raises $400 million at a $5.4 billion valuation

- [ ] Interesting

**Underlying event date:** 2026-08-17

**What happened**

On August 17 Higgsfield announced a $400 million Series B led by DST Global with Tribe Capital, Goldman Sachs Alternatives' Growth Equity, Smash Capital, Fifth Wall, Valor Capital, and Intel Capital participating, valuing the generative video and image company at $5.4 billion — four times its January valuation — on annualized revenue of $700 million, up from about $20 million a year earlier, and more than 30 million users across 238 countries and territories.
8 月 17 日，Higgsfield 宣布完成 4 亿美元 B 轮融资，由 DST Global 领投，Tribe Capital、Goldman Sachs Alternatives 旗下 Growth Equity、Smash Capital、Fifth Wall、Valor Capital 与 Intel Capital 参投；这家生成式视频与图像公司估值达到 54 亿美元，为其 1 月估值的四倍，年化收入 7 亿美元，一年前约为 2000 万美元，全球用户超过 3000 万，覆盖 238 个国家和地区。

**Why it matters**

A thirty-five-fold revenue increase in twelve months is the clearest datapoint yet that generative media has a paying professional market rather than only a consumer novelty one, which is what the valuation multiple is being asked to justify.
十二个月内收入增长三十五倍，是迄今最清晰的证据，表明生成式媒体拥有付费的专业市场，而不仅是面向消费者的新鲜玩物——而这正是其估值倍数需要撑起的论断。

**Sources:** [PR Newswire](https://www.prnewswire.com/news-releases/higgsfield-raises-400-million-series-b-financing-at-5-4-billion-valuation-with-annualized-revenue-reaching-700-million-302852430.html) · [TechCrunch](https://techcrunch.com/2026/08/17/higgsfield-raises-400m-series-b-quadrupling-its-valuation-in-8-months-to-5-4b/)

<a id="story-ibm-openai-partnership"></a>

### IBM puts OpenAI models inside its consulting platform

- [ ] Interesting

**Underlying event date:** 2026-08-13

**What happened**

On August 13 IBM and OpenAI announced a partnership under which IBM integrates OpenAI frontier models including GPT-5.6, plus Codex and ChatGPT Work, into IBM Consulting Advantage, with IBM consultants and engineers deploying them into customer operations, application modernization, software development, and cybersecurity, initially targeting financial services, government, telecommunications, and retail.
8 月 13 日，IBM 与 OpenAI 宣布合作：IBM 将把包括 GPT-5.6 在内的 OpenAI 前沿模型，以及 Codex 与 ChatGPT Work，集成进 IBM Consulting Advantage 平台，由 IBM 的顾问与工程师把它们部署到客户的运营、应用现代化、软件开发与网络安全场景中，初期聚焦金融服务、政府、电信与零售行业。

**Why it matters**

Frontier model access has stopped being the scarce input and delivery capacity has become it, so a systems integrator wiring one lab's models into its standard consulting platform decides what a large share of regulated enterprises will actually deploy.
前沿模型的可获得性已不再是稀缺投入，交付能力才是；因此一家系统集成商把某个实验室的模型接入自己的标准咨询平台，实际上决定了很大一部分受监管企业最终会部署什么。

**Sources:** [IBM Newsroom](https://newsroom.ibm.com/2026-08-13-ibm-partners-with-openai-to-accelerate-secure-ai-deployment-for-enterprises-across-core-operations) · [TechCrunch](https://techcrunch.com/2026/08/13/ibm-partners-with-openai-to-bolster-enterprise-ai-push/)

<a id="story-openai-computer-history"></a>

### ChatGPT starts recording what you do on your Mac

- [ ] Interesting

**Underlying event date:** 2026-08-13–2026-08-17

**What happened**

Between August 13 and August 17 OpenAI launched Computer History on macOS for ChatGPT Pro, Business, and Enterprise, an opt-in feature requiring ChatGPT Memories that records clicks, typing, keyboard shortcuts, and app switches across user-selected apps and websites into memories and a timeline that ChatGPT and Codex can reference, taking no screenshots, screen recordings, microphone, or system audio, excluding private browsing, deleting temporary event files within 48 hours, keeping generated memory files locally as unencrypted plain text readable by other programs under the same macOS account, and unavailable in the EEA, Switzerland, and the UK; OpenAI warns the feature raises prompt-injection risk from instructions embedded in websites and applications.
在 8 月 13 日至 8 月 17 日之间，OpenAI 面向 ChatGPT Pro、Business 与 Enterprise 在 macOS 上推出 Computer History：这是一项需用户主动开启、且依赖 ChatGPT Memories 的功能，它把用户选定的应用与网站中的点击、键入、键盘快捷键与应用切换记录为记忆和时间线，供 ChatGPT 与 Codex 引用；它不截屏、不录屏、不采集麦克风与系统音频，排除隐私浏览，临时事件文件在 48 小时内删除，生成的记忆文件以未加密纯文本保存在本地、同一 macOS 账户下的其他程序可以读取，且在欧洲经济区、瑞士与英国不可用；OpenAI 警告该功能会提高来自网站与应用内嵌指令的提示注入风险。

**Why it matters**

A local plain-text log of everything typed and clicked is exactly the artifact an approved-tools policy is written to prevent, and OpenAI's own prompt-injection warning means enabling it widens the attack surface of every agent that can read those memories.
一份记录所有键入与点击内容的本地纯文本日志，正是"仅允许审批工具"类政策想要阻止的产物；而 OpenAI 自己的提示注入警告意味着，启用它会扩大每一个能够读取这些记忆的智能体的攻击面。

**Sources:** [TechRepublic](https://www.techrepublic.com/article/ews-openai-computer-history-chatgpt-mac-activity/) · [The Next Web](https://thenextweb.com/news/openai-chatgpt-computer-history-mac-keystrokes)

## AI at Work

No qualifying stance change was found this week. Searches in English, Simplified Chinese, and Japanese covered internal memos, union bargaining, newsroom and education policies, banks, law and accounting firms, and named large employers, and every candidate failed the gate: the Associated Press newsroom AI standards update is dated 2026-07-24, Alibaba's ban on Anthropic tools took effect 2026-07-10, Okta's Cross App Access rollout to workforce customers is dated only to "August 2026" with no exact date, and the remaining material was aggregate survey data or sector-wide regulation, both excluded by rule.
本周未发现符合条件的立场变更。以英文、简体中文与日文进行的检索覆盖了内部备忘录、工会谈判、新闻编辑室与教育机构政策、银行、律所与会计师事务所，以及具名的大型雇主，所有候选项均未通过门槛：美联社新闻编辑室 AI 标准更新的日期为 2026 年 7 月 24 日，阿里巴巴对 Anthropic 工具的禁用自 2026 年 7 月 10 日生效，Okta 面向员工客户的 Cross App Access 上线仅标注为"2026 年 8 月"而无确切日期，其余材料则属于汇总调查数据或行业层面的监管，二者均按规则排除。

## Follow-ups to Interesting Stories

No marked story had a qualifying update this week. Every candidate either restated an unchanged earlier event or fell outside the coverage window: NVIDIA Cosmos 3 Edge remains its 2026-07-16 launch, ChatGPT Health remains its 2026-07-23 US rollout, BrowserStack Test Companion remains its 2026-07-29 launch, herdr's latest stable release remains v0.8.0, LangSmith LLM Gateway is still in public beta with no GA date announced, and LongHorizon-Harness v0.1.4 was already carried in the 2026-08-12 and 2026-08-14 editions.
本周没有任何已标记报道获得符合条件的更新。所有候选项要么只是重述未发生变化的旧事件，要么落在覆盖窗口之外：NVIDIA Cosmos 3 Edge 仍停留在 2026 年 7 月 16 日的发布，ChatGPT Health 仍停留在 2026 年 7 月 23 日的美国上线，BrowserStack Test Companion 仍停留在 2026 年 7 月 29 日的发布，herdr 的最新稳定版仍为 v0.8.0，LangSmith LLM Gateway 仍处于公开测试且未公布正式可用日期，而 LongHorizon-Harness v0.1.4 已在 2026-08-12 与 2026-08-14 两期中报道过。

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
- **[WriteGuard puts risk tiers and attribution in front of MCP writes](2026-08-06-ai-newsletter.md#story-cloudflare-writeguard-mcp-controls)** — Marked 2026-08-06. No qualifying update found this week; Cloudflare's 2026-08-14 Gateway MCP detection release is a separate product surface and is carried as a new story above. Uncheck `Interesting` in the original story to stop tracking it.
- **[Anthropic puts a customer-run checkpoint in front of every Claude Enterprise prompt](2026-08-11-ai-newsletter.md#story-anthropic-inference-hooks)** — Marked 2026-08-11. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[Insygna offers a free security scorecard for agents before they get system access](2026-08-11-ai-newsletter.md#story-insygna-agent-report-card)** — Marked 2026-08-11. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[A probing method infers which training run a frontier model came from](2026-08-11-ai-newsletter.md#story-model-knowledge-cutoff-probing)** — Marked 2026-08-11. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.

## Watch Next Week

Cloudflare listed MCP Portals reaching private-network servers through Gateway routing as still in active development, so the next step in the same programme is whether internal MCP servers become governable without being exposed publicly.
Cloudflare 把"MCP Portals 通过 Gateway 路由访问私有网络中的服务器"列为仍在积极开发中，因此同一计划的下一步，是内部 MCP 服务器能否在不对外暴露的前提下变得可治理。

OpenAI's own prompt-injection warning about Computer History and Google's zero-trust reference implementation point at the same unresolved question, which is whether an agent reading local activity memories can be sandboxed by the patterns already published rather than by a new control.
OpenAI 自己针对 Computer History 发出的提示注入警告，与 Google 的零信任参考实现指向同一个尚未解决的问题：读取本地活动记忆的智能体，能否用已经公开的模式加以沙箱化，而不必依赖某种新的管控手段。

## Sources

- [EN] [Agentic AI Foundation](https://aaif.io/blog/a2a-joins-aaif)
- [EN] [Techzine](https://www.techzine.eu/news/devops/143659/google-transfers-a2a-to-the-agentic-ai-foundation/)
- [EN] [Google Developers Blog](https://developers.googleblog.com/en/build-zero-trust-ai-agents-with-googles-agent-development-kit/)
- [EN] [Cloudflare Blog — MCP security updates](https://blog.cloudflare.com/mcp-security-updates/)
- [EN] [Cloudflare Blog — Access for Workers](https://blog.cloudflare.com/workers-protected-by-access/)
- [EN] [Calcalist CTech](https://www.calcalistech.com/ctechnews/article/sycvenedzx)
- [EN] [DoiT](https://www.doit.com/blog/doit-launches-attribute-ai-tokenomics-without-tags-sdks-or-code-changes)
- [EN] [Fortune](https://fortune.com/2026/08/16/stripe-7-billion-deal-ai-firm-openrouter-acquisition/)
- [EN] [TechCrunch — Stripe and OpenRouter](https://techcrunch.com/2026/08/16/stripe-will-reportedly-acquire-ai-gateway-startup-openrouter-for-7b/)
- [EN] [PR Newswire](https://www.prnewswire.com/news-releases/higgsfield-raises-400-million-series-b-financing-at-5-4-billion-valuation-with-annualized-revenue-reaching-700-million-302852430.html)
- [EN] [TechCrunch — Higgsfield Series B](https://techcrunch.com/2026/08/17/higgsfield-raises-400m-series-b-quadrupling-its-valuation-in-8-months-to-5-4b/)
- [EN] [IBM Newsroom](https://newsroom.ibm.com/2026-08-13-ibm-partners-with-openai-to-accelerate-secure-ai-deployment-for-enterprises-across-core-operations)
- [EN] [TechCrunch — IBM and OpenAI](https://techcrunch.com/2026/08/13/ibm-partners-with-openai-to-bolster-enterprise-ai-push/)
- [EN] [TechRepublic](https://www.techrepublic.com/article/ews-openai-computer-history-chatgpt-mac-activity/)
- [EN] [The Next Web](https://thenextweb.com/news/openai-chatgpt-computer-history-mac-keystrokes)
