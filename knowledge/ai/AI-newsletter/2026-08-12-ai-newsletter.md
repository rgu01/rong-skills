# Agents Get Plumbing, Governance, and a Bill

**Coverage:** 2026-08-06–2026-08-12 (Europe/Stockholm)

## Executive Brief

The week's agent tooling split cleanly between new plumbing — Cloudflare's WebMCP preview and its stateless MCP support on Workers, both on August 6 — and new accounting, with GitHub shipping a per-model token breakdown and Anthropic extending its Compliance API to Cowork and Claude Code on August 11.
本周的智能体工具明显分为两条线：一是新的底层管道，Cloudflare 在 8 月 6 日推出 WebMCP 预览版并在 Workers 上支持无状态 MCP；二是新的成本与合规核算，GitHub 与 Anthropic 均在 8 月 11 日分别发布按模型细分的 token 用量报表，以及覆盖 Cowork 和 Claude Code 的合规 API。

Elsewhere, OpenAI split its Daybreak security programme into gated Blue and Red tiers on August 10, Anthropic signed a 20-year, $9.1 billion compute lease the same day, and Manus said on August 11 it would resume independent operations as Meta's acquisition unwinds.
其他方面，OpenAI 于 8 月 10 日将其 Daybreak 安全计划拆分为准入受控的 Blue 与 Red 两档，Anthropic 同日签下为期 20 年、总额 91 亿美元的算力租约，而 Manus 在 8 月 11 日表示将随着 Meta 收购案的解除而恢复独立运营。

## AI Tools

<a id="story-cloudflare-webmcp-developer-preview"></a>

### Cloudflare gives any website an agent-callable tool surface with WebMCP

- [ ] Interesting

**Underlying event date:** 2026-08-06

**What happened**

On August 6, Cloudflare shipped a developer preview of WebMCP that injects a small script into HTML responses so a visitor's agent can discover and call a site's tools through `document.modelContext`, with no origin code changes.
8 月 6 日，Cloudflare 发布了 WebMCP 的开发者预览版：它向 HTML 响应中注入一段小脚本，使访问者的智能体能够通过 `document.modelContext` 发现并调用站点的工具，而无需改动源站代码。

**Why it matters**

It moves tool exposure from a server-side integration project to a proxy-level toggle, and because every tool runs in the visitor's browser under their own session, the agent inherits the user's authentication instead of needing its own credentials.
它把「暴露工具」从一项服务端集成工程降级为代理层的一个开关；而且由于所有工具都在访问者浏览器中、以其自身会话运行，智能体直接继承用户的身份认证，无需另行配置凭据。

**Sources:** [Cloudflare Blog](https://blog.cloudflare.com/webmcp/)

<a id="story-cloudflare-stateless-mcp-workers"></a>

### Stateless MCP lets servers run on Workers without Durable Objects

- [ ] Interesting

**Underlying event date:** 2026-08-06

**What happened**

Also on August 6, Cloudflare announced support for the 2026-07-28 MCP specification, which removes the required handshake, the `Mcp-Session-Id` header, and protocol sessions from the core request path, and shipped updated TypeScript, Python, Go, and C# SDKs plus migration guidance from `McpAgent` to `createMcpHandler`.
同样在 8 月 6 日，Cloudflare 宣布支持 2026-07-28 版 MCP 规范——该版本从核心请求路径中移除了强制握手、`Mcp-Session-Id` 头以及协议会话，并同步发布了更新后的 TypeScript、Python、Go 和 C# SDK，以及从 `McpAgent` 迁移到 `createMcpHandler` 的指引。

**Why it matters**

Statelessness removes the per-connection state that forced MCP servers onto Durable Objects, so an MCP server becomes an ordinary horizontally scalable request handler, and the vendor reports Sentry and Linear already running the spec in production.
无状态化消除了此前迫使 MCP 服务器依赖 Durable Objects 的每连接状态，使 MCP 服务器变成一个普通的可水平扩展请求处理器；厂商称 Sentry 与 Linear 已在生产环境中运行该规范。

**Sources:** [Cloudflare Blog](https://blog.cloudflare.com/mcp-v2/)

<a id="story-anthropic-compliance-api-cowork-claude-code"></a>

### Anthropic's Compliance API now returns whole Cowork and Claude Code sessions

- [ ] Interesting

**Underlying event date:** 2026-08-11

**What happened**

On August 11, Anthropic extended its Compliance API in beta to Claude Cowork on desktop, web, and mobile and to Claude Code in the CLI and desktop app, with session endpoints returning prompts, responses, web and MCP tool-call content, skills and artifacts, plus verified user ID, organization ID, and per-message timestamps.
8 月 11 日，Anthropic 将其合规 API 以 beta 形式扩展至桌面端、网页端和移动端的 Claude Cowork，以及 CLI 和桌面端的 Claude Code；新的会话接口返回提示词、回复、网页与 MCP 工具调用内容、技能与产出物，另附经验证的用户 ID、组织 ID 和逐条消息时间戳。

**Why it matters**

Agentic sessions have been the blind spot in enterprise logging because tool calls happen outside the chat transcript, and returning them in one consolidated server-hosted record removes the need to build separate capture for each surface — though the beta still excludes Claude Code on the web and sessions running on Bedrock, Vertex AI, or Microsoft Foundry.
智能体会话一直是企业日志中的盲区，因为工具调用发生在对话记录之外；将其整合进一条服务端托管的完整记录，省去了为每个界面单独搭建采集的工作——但该 beta 目前仍不覆盖网页版 Claude Code，以及运行在 Bedrock、Vertex AI 或 Microsoft Foundry 上的会话。

**Sources:** [Claude by Anthropic](https://claude.com/blog/compliance-api-cowork-and-claude-code)

<a id="story-github-copilot-memory-ollama-jetbrains"></a>

### Copilot for JetBrains gains cross-session memory and local Ollama models

- [ ] Interesting

**Underlying event date:** 2026-08-11

**What happened**

GitHub's August 11 changelog added Copilot memory, which retains and recalls information across agent chat sessions and is toggled in the Copilot settings portal, and Ollama as a bring-your-own-key provider selectable directly inside JetBrains.
GitHub 在 8 月 11 日的更新日志中新增了 Copilot memory——可在多次智能体对话之间保留并调用信息，通过 Copilot 设置门户开关——并将 Ollama 作为自带密钥（BYOK）供应商，可直接在 JetBrains 中选择。

**Why it matters**

Memory attacks the repetitive re-briefing that makes long-running IDE agents expensive, and the Ollama path lets teams route agent work to locally hosted models when code cannot leave the machine.
记忆功能针对的是长期运行的 IDE 智能体反复「重新交代背景」所带来的高成本，而 Ollama 通道则让代码不能外传的团队把智能体工作路由到本地部署的模型。

**Sources:** [GitHub Changelog](https://github.blog/changelog/2026-08-11-copilot-memory-and-ollama-in-github-copilot-for-jetbrains/)

<a id="story-github-per-model-token-breakdown"></a>

### GitHub itemizes AI credits down to cache reads and writes per model

- [ ] Interesting

**Underlying event date:** 2026-08-11

**What happened**

On August 11, GitHub added a per-model token breakdown to the downloadable AI usage report, showing input, output, cache-read, and cache-write tokens alongside AI credit consumption for Copilot Business and Copilot Enterprise administrators and individual Copilot users.
8 月 11 日，GitHub 在可下载的 AI 用量报表中新增按模型细分的 token 明细，为 Copilot Business、Copilot Enterprise 管理员及个人用户展示输入、输出、缓存读取和缓存写入 token 及其对应的 AI 额度消耗。

**Why it matters**

Cache-read and cache-write are exactly where agent loops silently burn budget, so separating them from raw input and output turns an opaque credit figure into an attributable cost line a team can actually optimize.
缓存读取与写入正是智能体循环中悄悄烧掉预算的地方，把它们从原始输入输出中拆分出来，使一个笼统的额度数字变成团队真正可以优化的、可归因的成本项。

**Sources:** [GitHub Changelog](https://github.blog/changelog/2026-08-11-per-model-token-breakdown-in-the-usage-report/)

<a id="story-spacexai-grok-bot-beta"></a>

### Grok Bot gives each agent its own cloud computer and an approval checkpoint

- [ ] Interesting

**Underlying event date:** 2026-08-11

**What happened**

SpaceXAI and Cursor released Grok Bot in early beta on August 11 for macOS, iOS, Windows, and Linux CLI, where each bot runs on a dedicated cloud computer, signs into the user's existing apps, works in parallel with other bots in group chats, and pauses for user confirmation at checkpoints it learns over time.
8 月 11 日，SpaceXAI 与 Cursor 发布了 Grok Bot 早期 beta 版，覆盖 macOS、iOS、Windows 及 Linux 命令行：每个 bot 运行在专属云端计算机上，登录用户已有的应用，可在群聊中与其他 bot 并行工作，并在其逐步学会识别的检查点处暂停等待用户确认。

**Why it matters**

Giving every agent a persistent machine rather than an ephemeral container is what lets work continue after the laptop closes, and the beta is gated behind SuperGrok Heavy at $300 per month, Cursor Ultra at $200, or Cursor Teams Premium at $120 per seat — a price signal for what always-on agents actually cost.
为每个智能体分配一台持久机器而非临时容器，正是笔记本合上后任务仍能继续的前提；该 beta 仅向每月 300 美元的 SuperGrok Heavy、200 美元的 Cursor Ultra 或每席位 120 美元的 Cursor Teams Premium 用户开放——这也是常驻智能体真实成本的一个价格信号。

**Sources:** [MacRumors](https://www.macrumors.com/2026/08/11/grok-bot-macos-ios/) · [GIGAZINE](https://gigazine.net/gsc_news/en/20260812-spacexai-grok-bot/)

## Other AI Stories

<a id="story-openai-daybreak-blue-red-gpt56-cyber"></a>

### OpenAI splits Daybreak into gated Blue and Red tiers and ships GPT-5.6-Cyber

- [ ] Interesting

**Underlying event date:** 2026-08-10

**What happened**

On August 10, OpenAI restructured Daybreak into Blue, which gives approved defenders frontier models with system-level safeguards relaxed for vulnerability discovery, malware analysis, and incident response, and Red, which adds the purpose-trained GPT-5.6-Cyber; the new model completes 95% of sensitive requests involving exploit chains and privilege escalation against 1.5% for GPT-5.6 Sol and 57.3% for GPT-5.5-Cyber, and was used to find CVE-2026-15903 in Chrome.
8 月 10 日，OpenAI 将 Daybreak 重组为两档：Blue 面向获批的防守方，提供在漏洞发现、恶意软件分析和事件响应场景下放宽系统级安全限制的前沿模型；Red 则追加专门训练的 GPT-5.6-Cyber。该新模型在涉及漏洞利用链和权限提升的敏感请求上完成率为 95%，而 GPT-5.6 Sol 为 1.5%、GPT-5.5-Cyber 为 57.3%，并被用于发现 Chrome 中的 CVE-2026-15903。

**Why it matters**

The 95%-versus-1.5% gap is an explicit admission that offensive-capable models exist and are being rationed by access tier rather than by refusal training, which makes the eligibility review the actual safety control.
95% 对 1.5% 的差距等于公开承认：具备攻击能力的模型已经存在，其约束手段是按准入分级配给，而非拒答训练——这意味着资格审核才是真正的安全控制点。

**Sources:** [Infosecurity Magazine](https://www.infosecurity-magazine.com/news/openai-daybreak-blue-red-gpt-cyber/) · [Neowin](https://www.neowin.net/news/openai-launches-gpt-56-cyber-and-expands-daybreak-with-red-and-blue-access-tiers/)

<a id="story-anthropic-riot-compute-lease"></a>

### Anthropic leases 191 megawatts from a bitcoin miner for 20 years

- [ ] Interesting

**Underlying event date:** 2026-08-10

**What happened**

Anthropic and Riot Platforms announced on August 10 a $9.1 billion, 20-year lease running to June 2048 for 191 megawatts of IT capacity at Riot's Rockdale, Texas campus, staged to 96 megawatts by December 2027 and full capacity by June 2028, with $573 million of interim financing arranged through Morgan Stanley and two five-year extension options that could lift the total to $16.1 billion.
Anthropic 与 Riot Platforms 于 8 月 10 日宣布签署一份总额 91 亿美元、为期 20 年、延续至 2048 年 6 月的租约，租用 Riot 位于得克萨斯州 Rockdale 园区 191 兆瓦的 IT 容量；分阶段部署，2027 年 12 月达到 96 兆瓦，2028 年 6 月全量交付；由摩根士丹利安排 5.73 亿美元过桥融资，另含两个五年展期选项，可将总额推高至 161 亿美元。

**Why it matters**

A 22-year commitment signed before a single megawatt is live prices compute scarcity rather than compute, and it confirms that stranded bitcoin-mining power has become a first-class supply channel for frontier labs.
在一兆瓦都尚未上电前就签下长达 22 年的承诺，定价的是算力的稀缺性而非算力本身；这也印证了闲置的比特币矿场电力已成为前沿实验室的一线供给渠道。

**Sources:** [TNW](https://thenextweb.com/news/anthropic-riot-9bn-data-centre-deal) · [CNBC](https://www.cnbc.com/2026/08/11/riot-platforms-signs-anthropic-deal-as-miners-shift-to-ai-infrastructure-.html)

<a id="story-manus-independent-again"></a>

### Manus returns to independence and will delete eight months of user data

- [ ] Interesting

**Underlying event date:** 2026-08-11

**What happened**

Manus said on August 11 that it will soon resume operating as an independent company as Meta's $2 billion acquisition unwinds, and that data generated by certain users on or after December 29, 2025 will be deleted on August 23–24, with backup available until August 23 and account restoration from August 25.
Manus 于 8 月 11 日表示，随着 Meta 价值 20 亿美元的收购交易解除，公司将很快恢复独立运营；同时，特定用户在 2025 年 12 月 29 日及之后生成的数据将于 8 月 23 至 24 日删除，8 月 23 日前可自行备份，账户自 8 月 25 日起恢复。

**Why it matters**

An unwound acquisition forcing the deletion of eight months of agent history is a concrete reminder that an agent platform's memory is a corporate asset subject to the deal structure above it, not a durable user-owned artifact.
一桩被解除的收购迫使删除八个月的智能体历史记录，具体地提醒人们：智能体平台上的记忆是受上层交易结构约束的公司资产，而非用户可长期持有的资产。

**Sources:** [ChinaTechNews](https://www.chinatechnews.com/2026/08/12/127092-ai-startup-manus-to-go-independent-again-as-deal-with-meta-unwinds) · [Compsmag](https://www.compsmag.com/news/manus-to-resume-independent-operations-as-meta-unwinds-2-billion-acquisition/)

## AI at Work

No qualifying stance change was found this week. Every candidate examined either fell outside the coverage window — Microsoft's departmental GitHub Copilot token budget was reported on August 5, and the Associated Press issued its updated newsroom AI standards on July 24 — or concerned customer-facing AI rather than an organization's own employees.
本周未发现符合条件的立场变化。所有候选事项要么落在覆盖窗口之外——微软按部门分配 GitHub Copilot token 预算一事报道于 8 月 5 日，美联社更新新闻编辑部 AI 规范的时间为 7 月 24 日——要么涉及面向客户的 AI，而非组织对自身员工的规定。

## Follow-ups to Interesting Stories

### LongHorizon-Harness v0.1.4 adds unified computer-use plugins and Terminal-Bench

**Original interest:** [LongHorizon-Harness gives computer-use agents a manager, executor, and auditor](2026-08-05-ai-newsletter.md#story-longhorizon-harness)

**Underlying event date:** 2026-08-11

**What changed**

The project tagged v0.1.4 on August 11, adding unified computer-use plugin support carried forward from v0.1.2, Terminal-Bench evaluation, a final user-facing reply, and execution in the launch directory.
该项目于 8 月 11 日发布 v0.1.4 版本，新增自 v0.1.2 延续而来的统一 computer-use 插件支持、Terminal-Bench 评测、最终面向用户的回复，以及在启动目录中执行。

**Why it matters**

Adding a standard benchmark four releases into a two-week-old project turns the harness from a paper artifact into something whose long-horizon claims can be independently re-run and compared.
一个仅有两周历史的项目在第四个版本就接入标准基准，使该 harness 从论文产物变成其长程能力主张可被独立复现和横向比较的工具。

**Sources:** [GitHub Releases](https://github.com/AMAP-ML/LongHorizon-Harness/releases/tag/v0.1.4)

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
- **[LongHorizon-Harness gives computer-use agents a manager, executor, and auditor](2026-08-05-ai-newsletter.md#story-longhorizon-harness)** — Marked 2026-08-05. Qualifying follow-up included above. Uncheck `Interesting` in the original story to stop tracking it.
- **[Drata ships agent discovery, scoring, and blocking in limited availability](2026-08-06-ai-newsletter.md#story-drata-ai-agent-governance)** — Marked 2026-08-06. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[WriteGuard puts risk tiers and attribution in front of MCP writes](2026-08-06-ai-newsletter.md#story-cloudflare-writeguard-mcp-controls)** — Marked 2026-08-06. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[Anthropic puts a customer-run checkpoint in front of every Claude Enterprise prompt](2026-08-11-ai-newsletter.md#story-anthropic-inference-hooks)** — Marked 2026-08-11. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[Insygna offers a free security scorecard for agents before they get system access](2026-08-11-ai-newsletter.md#story-insygna-agent-report-card)** — Marked 2026-08-11. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[A probing method infers which training run a frontier model came from](2026-08-11-ai-newsletter.md#story-model-knowledge-cutoff-probing)** — Marked 2026-08-11. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.

## Watch Next Week

If stateless MCP servers and browser-side WebMCP tools both spread, the audit surface Anthropic's session endpoints and GitHub's per-model breakdown were built to capture will start splitting across origins that neither vendor controls.
如果无状态 MCP 服务器与浏览器端 WebMCP 工具同时铺开，Anthropic 会话接口与 GitHub 按模型用量报表所要采集的审计面，将开始分散到两家厂商都无法掌控的各个源站上。

Watch whether Daybreak Red's eligibility review holds as the only gate on a model that completes 95% of exploit-chain requests, and whether Grok Bot's learned approval checkpoints prove sufficient for agents running on their own persistent machines.
值得关注的是：对于一个漏洞利用链请求完成率达 95% 的模型，Daybreak Red 的资格审核能否作为唯一闸门站得住脚；以及 Grok Bot 通过学习形成的审批检查点，对于运行在专属持久机器上的智能体是否足够。

## Sources

- [EN] [Cloudflare Blog — WebMCP](https://blog.cloudflare.com/webmcp/)
- [EN] [Cloudflare Blog — The next generation of MCP](https://blog.cloudflare.com/mcp-v2/)
- [EN] [Claude by Anthropic — Compliance API coverage](https://claude.com/blog/compliance-api-cowork-and-claude-code)
- [EN] [GitHub Changelog — Copilot memory and Ollama for JetBrains](https://github.blog/changelog/2026-08-11-copilot-memory-and-ollama-in-github-copilot-for-jetbrains/)
- [EN] [GitHub Changelog — Per-model token breakdown](https://github.blog/changelog/2026-08-11-per-model-token-breakdown-in-the-usage-report/)
- [EN] [MacRumors — Grok Bot](https://www.macrumors.com/2026/08/11/grok-bot-macos-ios/)
- [EN] [GIGAZINE — Grok Bot](https://gigazine.net/gsc_news/en/20260812-spacexai-grok-bot/)
- [EN] [Infosecurity Magazine — Daybreak Blue and Red](https://www.infosecurity-magazine.com/news/openai-daybreak-blue-red-gpt-cyber/)
- [EN] [Neowin — GPT-5.6-Cyber](https://www.neowin.net/news/openai-launches-gpt-56-cyber-and-expands-daybreak-with-red-and-blue-access-tiers/)
- [EN] [TNW — Anthropic and Riot](https://thenextweb.com/news/anthropic-riot-9bn-data-centre-deal)
- [EN] [CNBC — Riot Platforms and Anthropic](https://www.cnbc.com/2026/08/11/riot-platforms-signs-anthropic-deal-as-miners-shift-to-ai-infrastructure-.html)
- [EN] [ChinaTechNews — Manus goes independent](https://www.chinatechnews.com/2026/08/12/127092-ai-startup-manus-to-go-independent-again-as-deal-with-meta-unwinds)
- [EN] [Compsmag — Manus resumes independent operations](https://www.compsmag.com/news/manus-to-resume-independent-operations-as-meta-unwinds-2-billion-acquisition/)
- [EN] [GitHub Releases — LongHorizon-Harness v0.1.4](https://github.com/AMAP-ML/LongHorizon-Harness/releases/tag/v0.1.4)
