# Control planes arrive, and the plugin supply chain cracks

**Coverage:** 2026-09-15–2026-09-21 (Europe/Stockholm)

## Executive Brief

Four vendors shipped agent governance this week, and each one put a scoped permission in front of tools, code, or data.
本周有四家厂商发布了智能体治理能力，每一家都在工具、代码或数据前面加了一层受限权限。

Security moved as well, because a researcher showed that a pinned plugin can still install attacker code in four coding agents.
安全侧同样有进展：一位研究者证明，被固定版本的插件仍然可以在四款编码智能体中装入攻击者的代码。

## AI Tools

<a id="story-wso2-agent-manager-ga"></a>

### WSO2 Agent Manager reaches general availability under Apache-2.0

- [ ] Interesting

**Underlying event date:** 2026-09-15

**What happened**

On September 15 WSO2 released Agent Manager, an open control plane for AI agents, under the Apache 2.0 licence.
9 月 15 日，WSO2 以 Apache 2.0 许可发布了 Agent Manager，这是一个面向智能体的开放控制平面。

It gives each agent a verifiable identity, more than 40 guardrails, OpenTelemetry tracing, and a Kubernetes-native sandbox.
它为每个智能体提供可验证身份、40 多项护栏、OpenTelemetry 链路追踪和 Kubernetes 原生沙箱。

It manages agents in LangChain, CrewAI, and other frameworks that emit OpenTelemetry.
它可以管理 LangChain、CrewAI 等发出 OpenTelemetry 数据的框架中的智能体。

**Why it matters**

Most teams run agents on several frameworks at once, so a control plane outside the framework keeps one set of rules.
多数团队同时在几个框架上运行智能体，把控制平面放在框架之外可以保持同一套规则。

**Sources:** [WSO2](https://www.globenewswire.com/news-release/2026/09/15/3362114/0/en/wso2-agent-manager-brings-sovereign-ai-governance-to-enterprise-agent-sprawl.html) · [InfoQ](https://www.infoq.com/news/2026/09/ws02-agent-manager/)

<a id="story-cloudflare-workers-granular-roles"></a>

### Cloudflare scopes Workers access for each teammate and agent

- [ ] Interesting

**Underlying event date:** 2026-09-15

**What happened**

On September 15 Cloudflare added four Developer Platform roles that apply to a single Worker.
9 月 15 日，Cloudflare 新增了四种可作用于单个 Worker 的 Developer Platform 角色。

The four roles are Metadata Read-Only, Content Read-Only, Editor, and Admin.
四种角色是 Metadata Read-Only、Content Read-Only、Editor 和 Admin。

Only the Admin role can delete a Worker.
只有 Admin 角色可以删除 Worker。

You can create an API token with that narrow scope and give the token to an agent.
你可以用这种受限范围创建 API token，再把该 token 交给智能体。

**Why it matters**

An agent with account-wide credentials can change production by accident, and a per-Worker role removes that risk.
持有账户级凭据的智能体可能误改生产环境，按 Worker 划分的角色可以消除这种风险。

**Sources:** [The Cloudflare Blog](https://blog.cloudflare.com/workers-granular-authorization/)

<a id="story-salesforce-in-claude-beta"></a>

### Claude gets a Salesforce plugin with 37 seller skills

- [ ] Interesting

**Underlying event date:** 2026-09-15

**What happened**

On September 15 Anthropic released Salesforce in Claude as a beta plugin.
9 月 15 日，Anthropic 以测试版插件的形式发布了 Salesforce in Claude。

It carries 37 skills for daily sales work, including account research, call preparation, pipeline review, and CRM updates.
它包含 37 项面向日常销售工作的 skills，涵盖客户调研、通话准备、管道复盘和 CRM 更新。

The plugin reads accounts, opportunities, and pipeline data, and it keeps the permissions each seller already has.
该插件读取客户、商机和管道数据，并沿用每位销售已有的权限。

**Why it matters**

Agent work on CRM data usually fails on access control, so a plugin that inherits record permissions removes the main objection.
智能体处理 CRM 数据时通常卡在访问控制上，沿用记录权限的插件消除了主要顾虑。

**Sources:** [Claude by Anthropic](https://www.claude.com/blog/salesforce-in-claude)

<a id="story-gitlab-19-4-agent-governance"></a>

### GitLab 19.4 governs MCP server tools and adds open-weight models

- [ ] Interesting

**Underlying event date:** 2026-09-17

**What happened**

On September 17 GitLab released 19.4.
9 月 17 日，GitLab 发布 19.4。

An administrator can now govern GitLab MCP server tools beside the internal Duo Agent Platform tools.
管理员现在可以和内部 Duo Agent Platform 工具一起治理 GitLab MCP 服务端工具。

Read-only tools default to Always Allow, and write or delete tools default to Always Ask.
只读工具默认为 Always Allow，写入或删除工具默认为 Always Ask。

The release also hosts three open-weight models, GLM 5.3, Kimi K3, and MiniMax M3, which a user can pick for conversations.
该版本还托管了三个开放权重模型：GLM 5.3、Kimi K3 和 MiniMax M3，用户可以在对话中选用。

**Why it matters**

Third-party agents reach a repository through MCP, so one policy page for internal and external tools closes a real gap.
第三方智能体通过 MCP 访问仓库，把内外部工具放在同一个策略页面上填补了一个真实缺口。

**Sources:** [GitLab Docs](https://docs.gitlab.com/releases/19/gitlab-19-4-released/)

<a id="story-agent-framework-mcp-session-scope"></a>

### Microsoft Agent Framework scopes MCP sessions per invocation

- [ ] Interesting

**Underlying event date:** 2026-09-18

**What happened**

On September 18 Microsoft released Agent Framework dotnet-1.22.0.
9 月 18 日，Microsoft 发布 Agent Framework dotnet-1.22.0。

The release scopes a provider-backed MCP session to a single invocation.
该版本把由提供方支撑的 MCP 会话限制在单次调用内。

The same day the Python package 1.19.0 limited MCP skill archives to ZIP files and deprecated the MCP sampling callback.
同一天发布的 Python 包 1.19.0 把 MCP skill 归档限制为 ZIP 文件，并弃用了 MCP 采样回调。

**Why it matters**

A session that outlives one call can carry state between users, so per-invocation scoping is the safer default for shared agents.
跨越单次调用的会话可能在用户之间携带状态，按调用划分范围对共享智能体是更安全的默认设置。

**Sources:** [Microsoft Agent Framework releases](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.22.0)

<a id="story-agentcore-runtime-v2"></a>

### AWS ships the next AgentCore Runtime with elastic memory

- [ ] Interesting

**Underlying event date:** 2026-09-18

**What happened**

On September 18 AWS made the next AgentCore Runtime available in Amazon Bedrock AgentCore.
9 月 18 日，AWS 在 Amazon Bedrock AgentCore 中推出了新一代 AgentCore Runtime。

It reclaims unused memory during a session, so you pay for actual use rather than the peak.
它在会话期间回收闲置内存，因此你按实际用量付费，而不是按峰值付费。

It reports a P75 cold start of 1.9 to 2.0 seconds for images from 200 MB to 2 GB, against 5.4 to 30 seconds before.
对 200 MB 到 2 GB 的镜像，它的 P75 冷启动为 1.9 到 2.0 秒，此前为 5.4 到 30 秒。

You get the new behaviour when you set platformVersion to V2, and it runs in five regions.
把 platformVersion 设为 V2 即可启用新行为，目前覆盖五个区域。

**Why it matters**

Cold start and peak memory set both the bill and the latency of a serverless agent, so these numbers change deployment choices.
冷启动和峰值内存同时决定无服务器智能体的账单与延迟，这些数字会改变部署选择。

**Sources:** [AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/09/new-agentcore-runtime-generally-available/)

<a id="story-huawei-thinkprocess-agent-toolchain"></a>

### 华为开源昇腾 Agent 工具链，并提出“思程”运行单元

- [ ] Interesting

**事件日期：** 2026-09-19

**发生了什么**

9 月 19 日，华为在全联接大会上提出面向超节点与集群的 Agentic 计算开发方式。
华为把“思程”（ThinkProcess）定义为 Agent 的基本运行单元，并开放 PTO-ISA 虚拟指令集。
华为同时开源了全链路 Agent 工具，包括算子生成工具 CANNBot 和模型适配工具 Model Agent。
昇腾社区上线万卡算力资源，并推出“100 卡时计划”。

**为何重要**

国产算力栈此前缺少统一的智能体运行抽象，思程和开源工具链让开发者在昇腾上复用同一套接口。

**来源：** [华为](https://www.huawei.com/cn/news/2026/9/hc-agentic-thinkpro-pto-cann)

## Other AI Stories

<a id="story-plugin4shell-coding-agents"></a>

### Plugin4Shell breaks SHA pinning in four AI coding agents

- [ ] Interesting

**Underlying event date:** 2026-09-17

**What happened**

On September 17 AIR Security published Plugin4Shell, a zero-click flaw in the plugin systems of four AI coding agents.
9 月 17 日，AIR Security 公布了 Plugin4Shell，这是四款 AI 编码智能体插件机制中的零点击漏洞。

An attacker names a branch after the pinned commit hash, and the checkout then resolves the branch instead of the commit.
攻击者把分支命名为被固定的提交哈希，检出时就会解析到该分支，而不是那个提交。

Anthropic fixed Claude Code in 2.1.179 and OpenAI fixed Codex in 0.146.0.
Anthropic 在 2.1.179 中修复了 Claude Code，OpenAI 在 0.146.0 中修复了 Codex。

GitHub Copilot has no fix, and Google deprecated Gemini CLI instead of patching it.
GitHub Copilot 尚无修复，Google 则选择弃用 Gemini CLI，而不是打补丁。

**Why it matters**

A reviewed plugin from a trusted marketplace was the trusted part of the agent supply chain, and this flaw removes that assumption.
来自可信市场且经过审核的插件，本是智能体供应链中可信的一环，这个漏洞推翻了这个前提。

**Sources:** [AIR Security](https://www.air.security/blog-posts/plugin4shell) · [Help Net Security](https://www.helpnetsecurity.com/2026/09/18/plugin4shell-ai-coding-agents-vulnerability/)

<a id="story-anthropic-rd-automation-index"></a>

### Anthropic measures how much of its own R&D Claude leads

- [ ] Interesting

**Underlying event date:** 2026-09-17

**What happened**

On September 17 Anthropic published an R&D Automation Index for its own work.
9 月 17 日，Anthropic 发布了针对自身工作的 R&D Automation Index。

The index puts Claude in the lead on 26% of the company's AI research and engineering work in August, up from under 1% in February.
该指数显示，8 月有 26% 的 AI 研发工作由 Claude 主导，而 2 月这一比例还不到 1%。

The same post reports about 30,000 agents at work at one time on the main internal platform.
同一篇文章还报告，其主要内部平台上同时约有 30000 个智能体在工作。

Monitors checked every agent action, blocked about 0.002% of decisions, and sent roughly 50 transcripts a week to human review.
监控覆盖每一次智能体动作，拦截约 0.002% 的决策，每周约有 50 份记录转交人工复核。

**Why it matters**

Few laboratories publish internal automation and oversight numbers, so this gives practitioners a rare baseline for supervising agents at scale.
很少有实验室公开内部自动化和监督数据，这为从业者提供了大规模监督智能体的稀有基线。

**Sources:** [Anthropic](https://www.anthropic.com/institute/measuring-pace-of-ai-development) · [Unite.AI](https://www.unite.ai/anthropic-says-claude-leads-26-of-its-ai-research-and-development/)

<a id="story-anthropic-accenture-embedded-evaluation"></a>

### Anthropic and Accenture put evaluators inside the laboratory

- [ ] Interesting

**Underlying event date:** 2026-09-18

**What happened**

On September 18 Anthropic and Accenture announced embedded evaluation of frontier models.
9 月 18 日，Anthropic 和 Accenture 宣布对前沿模型开展嵌入式评估。

Accenture's Faculty division will red-team models, run alignment assessments, and test safeguards with employee-level access.
Accenture 旗下的 Faculty 将以员工级权限对模型做红队测试、对齐评估和安全防护测试。

Both companies plan to invest at least $1 billion over five years in evaluation capacity, and the arrangement is not exclusive.
两家公司计划在五年内至少投入 10 亿美元建设评估能力，且该安排并非排他性的。

**Why it matters**

Independent evaluation has stayed small and thinly funded, so a paid embedded team sets a standard that peers will be asked to match.
独立评估一直规模小、资金少，付费的驻场团队立下了一个同行会被要求对标的标准。

**Sources:** [Anthropic](https://www.anthropic.com/news/accenture-embedded-evaluation)

<a id="story-cloudflare-disallow-ai-training"></a>

### Cloudflare splits search, training, and agent crawling

- [ ] Interesting

**Underlying event date:** 2026-09-15

**What happened**

On September 15 Cloudflare replaced its blunt Block AI setting with separate controls for search, training, and agent crawlers.
9 月 15 日，Cloudflare 用搜索、训练和智能体爬虫三项独立控制，取代了原先笼统的 Block AI 设置。

A new Disallow AI Training setting publishes the preference in robots.txt and still allows accountable mixed-use crawlers.
新的 Disallow AI Training 设置会把该偏好写入 robots.txt，同时仍然放行“可问责”的混合用途爬虫。

Cloudflare calls a crawler accountable when the operator offers an opt-out, reports content use at URL level, and does not punish search ranking.
Cloudflare 认为，运营方提供退出机制、按 URL 报告内容使用情况且不影响搜索排名的爬虫才算“可问责”。

**Why it matters**

Site owners had to choose between search traffic and a training refusal, and separate signals let a site keep both.
网站所有者此前必须在搜索流量和拒绝训练之间二选一，独立信号让网站可以两者兼得。

**Sources:** [The Cloudflare Blog](https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/)

## Follow-ups to Interesting Stories

No story carried an active mark into this window, so there is no follow-up.
本周期内没有仍在生效的标记故事，因此没有跟进内容。

## Tracked Interests

No interest mark is active. Tick `Interesting` under any story above to track it for one month.
当前没有生效的兴趣标记。在上面任意故事下勾选 `Interesting`，即可跟踪一个月。

## Watch Next Week

GitHub Copilot still has no Plugin4Shell fix, by AIR Security's account, so a patched release is the next signal.
按 AIR Security 的说法，GitHub Copilot 仍未修复 Plugin4Shell，下一个信号是修复版本的发布。

AWS gives the new AgentCore Runtime only when you set platformVersion to V2.
只有把 platformVersion 设为 V2，AWS 才提供新的 AgentCore Runtime。

Adoption therefore depends on that opt-in.
因此采用速度取决于这一主动切换。

Anthropic says it intends to keep publishing these measurements, so the next index shows whether 26% keeps climbing.
Anthropic 表示会继续发布这类度量，下一期指数将显示 26% 是否继续上升。

## Sources

- [EN] [WSO2](https://www.globenewswire.com/news-release/2026/09/15/3362114/0/en/wso2-agent-manager-brings-sovereign-ai-governance-to-enterprise-agent-sprawl.html)
- [EN] [InfoQ](https://www.infoq.com/news/2026/09/ws02-agent-manager/)
- [EN] [The Cloudflare Blog](https://blog.cloudflare.com/workers-granular-authorization/)
- [EN] [Claude by Anthropic](https://www.claude.com/blog/salesforce-in-claude)
- [EN] [GitLab Docs](https://docs.gitlab.com/releases/19/gitlab-19-4-released/)
- [EN] [Microsoft Agent Framework releases](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.22.0)
- [EN] [AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/09/new-agentcore-runtime-generally-available/)
- [中文] [华为](https://www.huawei.com/cn/news/2026/9/hc-agentic-thinkpro-pto-cann)
- [EN] [AIR Security](https://www.air.security/blog-posts/plugin4shell)
- [EN] [Help Net Security](https://www.helpnetsecurity.com/2026/09/18/plugin4shell-ai-coding-agents-vulnerability/)
- [EN] [Anthropic](https://www.anthropic.com/institute/measuring-pace-of-ai-development)
- [EN] [Unite.AI](https://www.unite.ai/anthropic-says-claude-leads-26-of-its-ai-research-and-development/)
- [EN] [Anthropic](https://www.anthropic.com/news/accenture-embedded-evaluation)
- [EN] [The Cloudflare Blog](https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/)
