# One Plugin Format, One Browser, One Gateway: The Week Agent Plumbing Consolidated

**Coverage:** 2026-08-04–2026-08-10 (Europe/Stockholm, CEST)

## Executive Brief

Five rival platforms agreed on a single plugin format on August 6, and Cloudflare and LangChain both collapsed separate agent products into one control plane, making this a week about consolidation rather than new capability.
8 月 6 日，五家彼此竞争的平台就统一的插件格式达成一致；Cloudflare 与 LangChain 也各自把原本分离的智能体产品收拢为单一控制平面——本周的主题是整合，而非新增能力。

On the other side of the ledger, OpenAI publicly paused work on its unreleased Astra model on August 7 after preliminary evaluations put it at a critical cybersecurity capability level.
另一方面，8 月 7 日，OpenAI 在初步评估显示其未发布的 Astra 模型可能达到"关键"网络安全能力等级后，公开暂停了相关工作。

## AI Tools

<a id="story-agent-plugins-open-standard-1-0"></a>

### Five rival platforms agree on one plugin format with Agent Plugins 1.0

- [ ] Interesting

**Underlying event date:** 2026-08-06

**What happened**

On August 6, OpenAI, Amazon, Microsoft, Vercel, and Cursor maker Anysphere published Agent Plugins 1.0, a vendor-neutral packaging standard — a folder with a `plugin.json` manifest, an optional `skills/` directory, and an optional MCP server config — that ChatGPT, Codex, Cursor, GitHub Copilot, Kiro, and VS Code all support at launch, with Vercel having initiated the proposal and marketplaces, installation, permissions, sandboxing, and trust deliberately left to each client.
8 月 6 日，OpenAI、Amazon、Microsoft、Vercel 与 Cursor 母公司 Anysphere 发布 Agent Plugins 1.0：这是一个厂商中立的打包标准——一个包含 `plugin.json` 清单、可选 `skills/` 目录与可选 MCP 服务器配置的文件夹——ChatGPT、Codex、Cursor、GitHub Copilot、Kiro 与 VS Code 在发布时即全部支持；该提案由 Vercel 发起，而市场分发、安装、权限、沙箱与信任则被刻意留给各客户端自行决定。

**Why it matters**

Reusable skills and MCP servers have until now been repackaged per client, so a shared manifest turns "build once, run anywhere" from a slogan into a directory layout — and the standard's narrow scope means the hard parts, permissions and trust, still differ everywhere an agent runs.
此前可复用的技能与 MCP 服务器需要为每个客户端分别打包，统一清单让"一次构建、处处运行"从口号变成一种目录结构；而该标准刻意收窄的范围也意味着最难的部分——权限与信任——在每个智能体运行环境中依然各不相同。

**Sources:** [TNW](https://thenextweb.com/news/openai-agent-plugins-open-standard-skills-mcp)

<a id="story-cloudflare-kitesurf-agent-browser"></a>

### Cloudflare rebuilds the browser for agents and drops Chromium's memory footprint by 7x

- [ ] Interesting

**Underlying event date:** 2026-08-06

**What happened**

On August 6, Cloudflare launched Kitesurf, an agent-first browser assembled from the Blitz rendering engine, Firefox's Stylo CSS parser, and the Boa JavaScript engine, all compiled to WebAssembly and run inside V8 isolates on Workers; measured against Chromium across 14 sites it used 380ms versus 1,173ms of CPU for a screenshot and 39.4 MiB versus 273.7 MiB of memory for HTML extraction, while taking 1.7–1.8x longer in wall time, and it speaks the Chrome DevTools Protocol so Puppeteer and Playwright work unchanged, free during beta on Browser Run.
8 月 6 日，Cloudflare 发布 Kitesurf——一款面向智能体优先的浏览器，由 Blitz 渲染引擎、Firefox 的 Stylo CSS 解析器与 Boa JavaScript 引擎组装而成，三者均编译为 WebAssembly 并运行在 Workers 的 V8 isolate 内；在 14 个站点上与 Chromium 对比，截图任务 CPU 为 380 毫秒对 1,173 毫秒，HTML 抽取内存为 39.4 MiB 对 273.7 MiB，但墙钟耗时长 1.7–1.8 倍；它支持 Chrome DevTools 协议，因此 Puppeteer 与 Playwright 无需改动即可使用，公测期间在 Browser Run 上免费。

**Why it matters**

Browser automation is where agent runs get expensive and flaky, and stripping out tabs, themes, and extensions that no agent uses trades latency — which an async agent loop absorbs — for the memory ceiling that actually caps how many browser sessions a fleet can hold open at once.
浏览器自动化正是智能体运行既昂贵又不稳定的环节；砍掉标签页、主题与扩展这些智能体从不使用的部分，是用延迟（异步智能体循环本就能吸收）换取内存上限——而后者才真正决定一个集群能同时挂起多少个浏览器会话。

**Sources:** [Cloudflare Blog](https://blog.cloudflare.com/kitesurf/) · [TechCrunch](https://techcrunch.com/2026/08/07/cloudflare-launches-kitesurf-a-browser-built-for-ai-agents/)

<a id="story-cloudflare-workers-ai-gateway-unification"></a>

### Cloudflare folds Workers AI and AI Gateway into one binding

- [ ] Interesting

**Underlying event date:** 2026-08-07

**What happened**

On August 7, Cloudflare merged Workers AI and AI Gateway into a single control plane: one `env.AI` binding and one `/ai/` REST endpoint now reach both Cloudflare-hosted models and external providers, every new account gets a `default` gateway that activates on first authenticated request, AI Gateway credits now pay for Workers AI usage, and every request is logged with latency breakdowns, token usage, error rates, and the exact prompts and responses without any setup.
8 月 7 日，Cloudflare 将 Workers AI 与 AI Gateway 合并为单一控制平面：一个 `env.AI` 绑定和一个 `/ai/` REST 端点即可同时访问 Cloudflare 托管模型与外部供应商；每个新账户都会获得一个在首次认证请求时自动激活的 `default` 网关；AI Gateway 额度现在可用于支付 Workers AI 用量；并且每次请求都会自动记录延迟拆解、token 用量、错误率以及完整的提示与响应，无需任何配置。

**Why it matters**

Observability that requires a separate product is observability teams skip, and making the gateway the default path — rather than an opt-in proxy someone remembers to configure — is what turns per-request logging and spend visibility into something an agent fleet has by construction.
需要单独接入一个产品才能获得的可观测性，往往就是团队会跳过的可观测性；把网关变成默认路径，而不是需要有人记得去配置的可选代理，才让逐请求日志与花费可见性成为智能体集群天然具备的能力。

**Sources:** [Cloudflare Blog](https://blog.cloudflare.com/workers-ai-gateway-unification/)

<a id="story-langchain-managed-deep-agents-beta"></a>

### Managed Deep Agents turns an agent folder into a deployed runtime

- [ ] Interesting

**Underlying event date:** 2026-08-07

**What happened**

On August 7, LangChain opened Managed Deep Agents to public beta, letting a Deep Agent defined as a folder be scaffolded, run locally, and deployed with `mda init`, `mda dev`, and `mda deploy` onto LangSmith infrastructure that owns durable execution across pauses and restarts, sandbox lifecycle, persistent memory via Context Hub, OIDC identity, scheduled tasks, Slack and GitHub channels, and Harbor eval integration — initially on LangSmith Cloud in the US region only.
8 月 7 日，LangChain 将 Managed Deep Agents 推入公测：以文件夹形式定义的 Deep Agent 可通过 `mda init`、`mda dev`、`mda deploy` 完成脚手架、本地运行与部署，运行在由 LangSmith 托管的基础设施上，后者负责跨暂停与重启的持久化执行、沙箱生命周期、经由 Context Hub 的持久记忆、OIDC 身份、定时任务、Slack 与 GitHub 通道以及 Harbor 评测集成——初期仅在美国区域的 LangSmith Cloud 上提供。

**Why it matters**

The gap between a working agent script and a production agent is almost entirely infrastructure nobody wanted to write — persistence, sandbox teardown, auth, scheduling — and moving that boundary to a managed runtime while leaving models, tools, middleware, and subagents in the developer's code is a cleaner split than the hosted-agent-builder products that also take the business logic.
一个能跑通的智能体脚本与一个生产级智能体之间的差距，几乎全部是没人愿意写的基础设施——持久化、沙箱回收、鉴权、调度；把这条边界交给托管运行时，同时把模型、工具、中间件与子智能体留在开发者代码中，比那些连业务逻辑一并接管的托管式智能体搭建产品切得更干净。

**Sources:** [LangChain Blog](https://www.langchain.com/blog/managed-deep-agents-is-now-in-public-beta)

<a id="story-harnessopt-bench-agent-harness-optimization"></a>

### HarnessOpt-Bench asks whether a model can improve its own scaffolding

- [ ] Interesting

**Underlying event date:** 2026-08-06

**What happened**

Submitted to arXiv on August 6, HarnessOpt-Bench evaluates LLMs as harness optimizers — each is handed a target agent's seed harness, graded evaluation feedback, and a fixed evaluation budget, then edits the prompts, tools, and orchestration code and nominates a final candidate scored by normalized gain over the seed — and across 5 frontier models, 4 downstream tasks, and 111 scored runs it reports that optimizer models separate more than the coding harnesses they act through and that native harnesses are not consistently better than a shared one.
HarnessOpt-Bench 于 8 月 6 日提交至 arXiv，将大模型作为"harness 优化器"来评测：每个模型会拿到目标智能体的初始 harness、带评分的评测反馈以及固定的评测预算，随后修改提示词、工具与编排代码，并提名一个最终候选，按相对初始版本的归一化增益计分；在 5 个前沿模型、4 项下游任务、111 次计分运行中，论文报告优化器模型之间的差异大于它们所使用的编码 harness 之间的差异，且原生 harness 并不总是优于共享 harness。

**Why it matters**

Teams routinely hand a coding agent their own agent's prompts and tools and ask it to tune them, and this is the first dated attempt to measure that loop as a distinct capability rather than assume the strongest coding model is also the best at editing scaffolding.
团队经常把自家智能体的提示词与工具交给编码智能体去调优，而这是第一次有明确日期的工作，把这一循环当作一种独立能力来测量，而不是默认最强的编码模型同样最擅长修改脚手架。

**Sources:** [arXiv](https://arxiv.org/abs/2608.06301)

## Other AI Stories

<a id="story-anthropic-in-house-chip-team"></a>

### Anthropic confirms an in-house chip design team

- [ ] Interesting

**Underlying event date:** 2026-08-05

**What happened**

On August 5, Anthropic publicly confirmed it is assembling an in-house silicon team to co-design custom chips alongside Claude so the models "run faster and more efficiently at the scale our customers need," with semiconductor engineering roles posted at $320,000–$485,000, while keeping its existing Nvidia, AMD, Google TPU, and AWS Trainium arrangements in place.
8 月 5 日，Anthropic 公开确认正在组建自研芯片团队，与 Claude 协同设计定制芯片，使模型"在客户所需的规模下运行得更快、更高效"；半导体工程岗位薪资区间为 32 万至 48.5 万美元，同时保留其与 Nvidia、AMD、Google TPU 及 AWS Trainium 的现有合作。

**Why it matters**

Every frontier lab that has hit a serving-cost wall has eventually reached for custom silicon, and a model developer designing hardware around one model family — rather than buying general-purpose accelerators — is a bet that inference economics, not training capability, decides the next few years.
每一家撞上服务成本天花板的前沿实验室最终都会转向定制芯片；一家模型厂商围绕单一模型家族设计硬件、而非采购通用加速器，本质上是在押注未来几年的胜负由推理经济性、而非训练能力决定。

**Sources:** [SQ Magazine](https://sqmagazine.co.uk/anthropic-chip-design-team/)

<a id="story-openai-gpt-56-sol-luna-free-tier"></a>

### OpenAI tightens GPT-5.6 Sol and hands free users unlimited chats

- [ ] Interesting

**Underlying event date:** 2026-08-06

**What happened**

On August 6, OpenAI shipped an updated GPT-5.6 Sol to Plus and Pro users tuned for shorter, more direct answers and reporting about 68% fewer responses containing at least one factual error than GPT-5.5 Instant, added a reasoning-effort slider for paid tiers, made GPT-5.6 Luna the default for Free and Go users with unlimited text chats following, and gave those users a Think button that grants Luna more time without routing to Sol or Terra.
8 月 6 日，OpenAI 向 Plus 与 Pro 用户推送更新版 GPT-5.6 Sol，其回答更简短直接，据称包含至少一处事实错误的回复比 GPT-5.5 Instant 少约 68%，并为付费档位新增推理强度滑块；同时将 GPT-5.6 Luna 设为 Free 与 Go 用户的默认模型并随后开放无限文本对话，还为这些用户提供 Think 按钮，让 Luna 有更多思考时间，但不会转由 Sol 或 Terra 处理。

**Why it matters**

Unlimited free text chat moves the serving-cost question from rate limits to model tiering, and the Think button makes that explicit: free users get more compute on the same small model rather than access to a bigger one.
免费无限文本对话把服务成本问题从限流转移到了模型分层上，而 Think 按钮把这一点摆到了明面：免费用户获得的是同一个小模型上更多的算力，而不是更大模型的使用权。

**Sources:** [DataNorth](https://datanorth.ai/news/openai-updates-gpt-5-6-sol-and-gpt-5-6-luna)

<a id="story-salesforce-missionforce-il5-agents"></a>

### Salesforce clears IL5 and puts agents in front of 9.2 million Army records

- [ ] Interesting

**Underlying event date:** 2026-08-05

**What happened**

On August 5, Salesforce announced that its Missionforce National Security platform running Agentforce 360 received Impact Level 5 authorization to process controlled unclassified information and unclassified national-security data on AWS GovCloud, with Army Human Resources Command as the first component to deploy — handling over 1,500 personnel cases a day and a projected 55 million-plus agent conversations a month.
8 月 5 日，Salesforce 宣布其运行 Agentforce 360 的 Missionforce National Security 平台获得 Impact Level 5 授权，可在 AWS GovCloud 上处理受控非密信息与非密国家安全数据；陆军人力资源司令部成为首个部署单位，每天处理超过 1,500 起人事案件，预计满负荷时每月产生逾 5,500 万次智能体对话。

**Why it matters**

IL5 is the first time a commercially proven agentic platform has been cleared for sensitive unclassified work at this scale, which makes the audit and attribution tooling shipping elsewhere this year less of an enterprise nicety and more of a procurement precondition.
IL5 是首次有在商业环境中验证过的智能体平台获准以这一规模处理敏感非密业务，这让今年各处陆续推出的审计与归因工具，从企业的锦上添花变成了采购的前置条件。

**Sources:** [DefenseScoop](https://defensescoop.com/2026/08/05/salesforce-plans-deliver-newly-authorized-ai-agents-across-dod/) · [Military Times](https://www.militarytimes.com/news/your-military/2026/08/07/pentagon-ready-to-deploy-ai-agents-for-admin-tasks/)

<a id="story-zoox-paid-robotaxi-las-vegas"></a>

### Zoox starts charging for rides in a car with no steering wheel

- [ ] Interesting

**Underlying event date:** 2026-08-10

**What happened**

Zoox began charging for robotaxi rides in Las Vegas on August 10, its first commercial operation, using a base fare plus distance and time quoted before booking and fixed regardless of the route taken, made possible by a federal exemption from eight motor vehicle safety standards covering up to 2,500 vehicles for two years; its San Francisco and Austin services remain free pending further permits.
8 月 10 日，Zoox 在拉斯维加斯开始对机器人出租车收费，这是其首次商业运营，计价方式为起步价加里程与时长，下单前即报价并不因实际路线改变；这一切依托于联邦层面对八项机动车安全标准的豁免，覆盖两年内最多 2,500 辆车；其旧金山与奥斯汀的服务在获得进一步许可前仍然免费。

**Why it matters**

A purpose-built vehicle with no steering wheel taking paid passengers is the first commercial validation that autonomy can be sold without a human-controls fallback, and the two-year, volume-capped exemption is the template every competitor will now be measured against.
一辆没有方向盘的专用车辆开始载客收费，是自动驾驶可以在不保留人工操控后备方案的情况下商业化的首次验证；而这份为期两年、限定车辆数量的豁免，也成为此后每个竞争对手都将被对照衡量的样板。

**Sources:** [TechCrunch](https://techcrunch.com/2026/08/05/zoox-to-start-charging-for-robotaxi-rides-in-las-vegas/)

## Follow-ups to Interesting Stories

### OpenAI pauses Astra work after it nears a critical cyber capability level

**Original interest:** [OpenAI introduces Astra with ten Lean-certified mathematical results](2026-08-04-ai-newsletter.md#story-openai-astra-lean-certified-proofs)

**Underlying event date:** 2026-08-07

**What changed**

On August 7, six days after introducing Astra through ten Lean-certified mathematical results, OpenAI published a blog post pausing internal Astra activity that does not meet tightened guardrails, saying preliminary evaluations were strong enough that it "cannot rule out Critical capability level" on cybersecurity — meaning the model may independently identify and develop zero-day exploits against well-defended systems — and that it is working with government agencies and selected AI safety organizations to stress-test the model further.
8 月 7 日，即以十项 Lean 可验证数学结果引出 Astra 六天之后，OpenAI 发布博文，暂停所有不满足更严格防护要求的 Astra 内部活动，称初步评估结果强到"无法排除关键（Critical）能力等级"的网络安全风险——即该模型可能自主发现并开发针对防护良好系统的零日漏洞利用——并表示正与政府机构及部分 AI 安全组织合作，对模型做进一步压力测试。

**Why it matters**

The same model family whose proofs could be settled by a machine checker is the one whose cyber capability cannot be settled by any equivalent, and OpenAI making that asymmetry public for an unreleased model sets a disclosure precedent that its competitors will be asked about.
同一个模型家族，其数学证明可以交由机器检查器裁决，而其网络攻击能力却没有任何等价的裁决手段；OpenAI 就一个尚未发布的模型公开这种不对称性，树立了一个披露先例，其竞争对手今后会被要求对照。

**Sources:** [TechCrunch](https://techcrunch.com/2026/08/07/openai-says-it-slowed-astra-model-development-over-security-concerns/)

### LongHorizon-Harness goes from paper to four tagged releases in four days

**Original interest:** [LongHorizon-Harness gives computer-use agents a manager, executor, and auditor](2026-08-05-ai-newsletter.md#story-longhorizon-harness)

**Underlying event date:** 2026-08-04–2026-08-07

**What changed**

Between August 4 and August 7, AMAP-ML cut four tagged releases of LongHorizon-Harness — v0.1.0 on August 4, v0.1.1 on August 5 adding project config plus `init`, `doctor`, version and update-check commands along with MCP support and a dashboard showing live role status, and v0.1.2 and v0.1.3 both on August 7 bringing unified computer-use plugin management, stronger read-only enforcement and role isolation for the auditor, reliable process cleanup, and expanded diagnostics.
8 月 4 日至 8 月 7 日间，AMAP-ML 为 LongHorizon-Harness 连发四个带标签的版本——8 月 4 日的 v0.1.0；8 月 5 日的 v0.1.1，新增项目配置以及 `init`、`doctor`、版本与更新检查命令，并加入 MCP 支持和可显示实时角色状态的仪表盘；8 月 7 日的 v0.1.2 与 v0.1.3，带来统一的 computer-use 插件管理、更严格的审计器只读约束与角色隔离、可靠的进程清理以及更完整的诊断能力。

**Why it matters**

The benchmark numbers in the paper only matter if the harness is installable, and hardening the auditor's read-only boundary is the specific change that keeps the verification role from becoming another way for the agent to mutate state it was supposed to be checking.
论文里的基准数字只有在 harness 可安装的前提下才有意义；而强化审计器的只读边界正是那个关键改动，它避免了验证角色本身沦为智能体修改其本应检查之状态的又一条路径。

**Sources:** [GitHub Releases](https://github.com/AMAP-ML/LongHorizon-Harness/releases)

## Tracked Interests

- **[NVIDIA releases Cosmos 3 Edge for local physical AI](2026-07-24-ai-newsletter.md#story-nvidia-cosmos-3-edge-siggraph)** — Marked 2026-07-24. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[OpenAI rolls out Health in ChatGPT to U.S. users](2026-07-27-ai-newsletter.md#story-chatgpt-health-rollout)** — Marked 2026-07-27. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[月之暗面正式开源 Kimi K3](2026-07-29-ai-newsletter.md#story-kimi-k3-open-source)** — Marked 2026-07-29. No qualifying update found this week; researchers disclosed a Kimi K3 sandbox escape on 2026-08-07, but no source gives an exact date for the incident itself, so it fails this edition's date gate. Uncheck `Interesting` in the original story to stop tracking it.
- **[Reader spotlight: SpecForge pairs LLMs with formal specifications](2026-07-29-ai-newsletter.md#story-imiron-specforge-ai-formal-specs)** — Marked 2026-07-29. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[LangSmith LLM Gateway enters public beta as a runtime control plane](2026-07-31-ai-newsletter.md#story-langsmith-llm-gateway-public-beta)** — Marked 2026-07-31. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[Deep Agents v0.7 cuts base input tokens by 65%](2026-07-31-ai-newsletter.md#story-deep-agents-v07-token-diet)** — Marked 2026-07-31. No qualifying update found this week for the v0.7 release itself; LangChain's separate Managed Deep Agents launch is covered in AI Tools above. Uncheck `Interesting` in the original story to stop tracking it.
- **[BrowserStack puts an agentic testing harness inside the IDE](2026-07-31-ai-newsletter.md#story-browserstack-test-companion-ide)** — Marked 2026-07-31. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[herdr 0.8.0 relicenses to Apache-2.0 and cuts multi-client CPU by 95%](2026-08-04-ai-newsletter.md#story-herdr-v080-agent-multiplexer)** — Marked 2026-08-04. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[OpenAI introduces Astra with ten Lean-certified mathematical results](2026-08-04-ai-newsletter.md#story-openai-astra-lean-certified-proofs)** — Marked 2026-08-04. Qualifying follow-up included above. Uncheck `Interesting` in the original story to stop tracking it.
- **[LongHorizon-Harness gives computer-use agents a manager, executor, and auditor](2026-08-05-ai-newsletter.md#story-longhorizon-harness)** — Marked 2026-08-05. Qualifying follow-up included above. Uncheck `Interesting` in the original story to stop tracking it.
- **[Drata ships agent discovery, scoring, and blocking in limited availability](2026-08-06-ai-newsletter.md#story-drata-ai-agent-governance)** — Marked 2026-08-06. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[WriteGuard puts risk tiers and attribution in front of MCP writes](2026-08-06-ai-newsletter.md#story-cloudflare-writeguard-mcp-controls)** — Marked 2026-08-06. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.

## Watch Next Week

Agent Plugins deliberately leaves permissions, sandboxing, and trust to each client, so the first real test is whether ChatGPT, Cursor, GitHub Copilot, and VS Code diverge on what a plugin is allowed to do once the same folder runs in all of them.
Agent Plugins 刻意把权限、沙箱与信任留给各客户端决定，因此第一个真正的考验是：当同一个文件夹在 ChatGPT、Cursor、GitHub Copilot 与 VS Code 中同时运行时，它们对"插件被允许做什么"的判断会不会开始分道扬镳。

OpenAI said it is working with government agencies and selected AI safety organizations to stress-test Astra further, so the shape of that review — and whether any of it is published — determines whether this pause reads as a precedent or a one-off.
OpenAI 表示正与政府机构及部分 AI 安全组织合作，对 Astra 做进一步压力测试；因此这次评审的形式——以及其中是否有任何内容对外公开——将决定这次暂停被视为一个先例，还是一次孤例。

## Sources

- [EN] [TNW](https://thenextweb.com/news/openai-agent-plugins-open-standard-skills-mcp)
- [EN] [Cloudflare Blog — Kitesurf](https://blog.cloudflare.com/kitesurf/)
- [EN] [TechCrunch — Kitesurf](https://techcrunch.com/2026/08/07/cloudflare-launches-kitesurf-a-browser-built-for-ai-agents/)
- [EN] [Cloudflare Blog — AI control plane](https://blog.cloudflare.com/workers-ai-gateway-unification/)
- [EN] [LangChain Blog](https://www.langchain.com/blog/managed-deep-agents-is-now-in-public-beta)
- [EN] [arXiv](https://arxiv.org/abs/2608.06301)
- [EN] [SQ Magazine](https://sqmagazine.co.uk/anthropic-chip-design-team/)
- [EN] [DataNorth](https://datanorth.ai/news/openai-updates-gpt-5-6-sol-and-gpt-5-6-luna)
- [EN] [DefenseScoop](https://defensescoop.com/2026/08/05/salesforce-plans-deliver-newly-authorized-ai-agents-across-dod/)
- [EN] [Military Times](https://www.militarytimes.com/news/your-military/2026/08/07/pentagon-ready-to-deploy-ai-agents-for-admin-tasks/)
- [EN] [TechCrunch — Zoox](https://techcrunch.com/2026/08/05/zoox-to-start-charging-for-robotaxi-rides-in-las-vegas/)
- [EN] [TechCrunch — Astra](https://techcrunch.com/2026/08/07/openai-says-it-slowed-astra-model-development-over-security-concerns/)
- [EN] [GitHub Releases](https://github.com/AMAP-ML/LongHorizon-Harness/releases)
