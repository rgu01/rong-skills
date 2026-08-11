# Agents Get a Control Plane: Registries, Allowlists, and Prompt Checkpoints

**Coverage:** 2026-08-05–2026-08-11 (Europe/Stockholm, CEST)

## Executive Brief

This week's agent tooling was almost entirely about control rather than capability: Anthropic put a customer-run allow-or-deny checkpoint in front of every Claude Enterprise prompt, GitHub let enterprises allowlist which MCP servers Copilot may run, and AWS shipped both a governed agent catalog and 14-day persistent agent compute.
本周的智能体工具几乎全部关于控制而非能力：Anthropic 在每一次 Claude Enterprise 提示词之前加入了由客户自建服务器执行的允许/拒绝检查点，GitHub 让企业可以为 Copilot 允许运行的 MCP 服务器设置白名单，AWS 则同时推出了受治理的智能体目录与可持续 14 天的智能体算力。

Away from tooling, Meta returned to permissive open weights with a 30B agent model that runs on one consumer GPU, and Cloudflare reported that suspicious behavior on its network now shifts between human and agentic mid-session, which is why it is moving from point-in-time risk scores to continuous trust evaluation.
在工具之外，Meta 以一款可在单张消费级 GPU 上运行的 300 亿参数智能体模型回归宽松开放权重，而 Cloudflare 报告称其网络上的可疑行为如今会在同一会话中在人类与智能体之间来回切换，这正是它从时点风险评分转向持续信任评估的原因。

## AI Tools

<a id="story-anthropic-inference-hooks"></a>

### Anthropic puts a customer-run checkpoint in front of every Claude Enterprise prompt

- [X] Interesting

**Underlying event date:** 2026-08-05

**What happened**

On August 5, Anthropic launched inference hooks in beta for Claude Enterprise, routing each prompt and tool-call response over a signed WebSocket connection to a security server the customer runs, which returns an allow or deny verdict before the model generates.
8 月 5 日，Anthropic 面向 Claude Enterprise 推出 inference hooks 测试版：每一条提示词与工具调用返回值都会通过签名的 WebSocket 连接发送到客户自建的安全服务器，由其返回允许或拒绝的裁决，模型才会开始生成。

A single organization-level setting covers Claude Enterprise chat, Claude Code, Claude Cowork, and tool calls made through MCP connectors, skills, and plugins, and the rollout includes an allow-by-default shadow mode, role-based exclusions, percentage rollouts, and direct integration with Netskope, Palo Alto Networks, Proofpoint, and Zscaler.
一个组织级开关即可覆盖 Claude Enterprise 聊天、Claude Code、Claude Cowork，以及通过 MCP 连接器、skills 与插件发起的工具调用；上线方案包含默认放行的影子模式、按角色排除、按比例灰度，并可直接对接 Netskope、Palo Alto Networks、Proofpoint 与 Zscaler。

**Why it matters**

Data-loss prevention has been the standard reason security teams refuse to approve an agent that touches real systems, and moving the decision to a customer-operated server before inference means the veto lives with the compliance team instead of inside the vendor's policy engine.
数据防泄漏一直是安全团队拒绝批准接触真实系统的智能体的标准理由；把决策前移到客户自建服务器、并置于推理之前，意味着否决权归属合规团队，而不再由供应商的策略引擎掌握。

**Sources:** [Claude by Anthropic](https://claude.com/blog/claude-enterprise-inference-hooks) · [Claude Platform Docs](https://platform.claude.com/docs/en/manage-claude/inference-hooks)

<a id="story-agentcore-runtime-instances"></a>

### AgentCore runtime instances give agents 14-day sessions on managed EC2

- [ ] Interesting

**Underlying event date:** 2026-08-06

**What happened**

On August 6, AWS made Amazon Bedrock AgentCore runtime instances generally available in nine Regions, running agents on AWS-managed EC2 infrastructure in the customer's own account with sessions that persist up to 14 days, GPU-accelerated and memory- or compute-optimized instance families, multiple agents collaborating on one host, session stop and restart to avoid paying for idle time, and AWS handling provisioning, patching, scaling, and teardown.
8 月 6 日，AWS 在九个区域正式推出 Amazon Bedrock AgentCore runtime instances：在客户自有账号内、由 AWS 托管的 EC2 基础设施上运行智能体，会话最长可持续 14 天，支持 GPU 加速与内存或计算优化实例族，多个智能体可在同一主机上协作，会话可停止与重启以避免为空闲付费，预置、补丁、扩缩与销毁均由 AWS 负责。

The new compute type complements the existing microVM option, which starts faster but caps sessions at eight hours.
这一新计算类型与既有的 microVM 选项互补——后者启动更快，但会话上限为 8 小时。

**Why it matters**

Long-running research, migration, and build agents die on serverless timeouts and lose their working state, so a managed host that keeps a session and its collaborators alive for two weeks removes the checkpoint-and-resume scaffolding teams currently write by hand.
长时间运行的研究、迁移与构建类智能体会因无服务器超时而中断并丢失工作状态；一个能让会话及其协作者存活两周的托管主机，可以省掉团队目前手写的检查点与恢复脚手架。

**Sources:** [AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-bedrock-agentcore-runtime-instances-generally-available/) · [AWS News Blog](https://aws.amazon.com/blogs/aws/runtime-instances-persistent-compute-for-production-ai-agents-on-amazon-bedrock-agentcore/)

<a id="story-aws-agent-registry-namespace"></a>

### AWS Agent Registry leaves preview with its own namespace and a hard migration deadline

- [ ] Interesting

**Underlying event date:** 2026-08-06

**What happened**

On August 6, AWS Agent Registry launched under its own `agent-registry` namespace, offering a private governed catalog of agents, MCP servers, skills, and custom resources with an approval workflow, hybrid semantic-plus-keyword search, new `ListDiscoverableRegistryRecords` and `BatchGetDiscoverableRegistryRecord` browsing APIs, a required `recordType` field, and a native MCP endpoint that MCP-compatible clients can query directly.
8 月 6 日，AWS Agent Registry 在独立的 `agent-registry` 命名空间下上线：提供面向智能体、MCP 服务器、skills 与自定义资源的私有受治理目录，含审批流程、语义与关键词混合检索、新增的 `ListDiscoverableRegistryRecords` 与 `BatchGetDiscoverableRegistryRecord` 浏览 API、必填的 `recordType` 字段，以及可供 MCP 兼容客户端直接查询的原生 MCP 端点。

The move breaks backward compatibility across endpoints, IAM actions, ARNs, SDK clients, CLI commands, and the record schema, customers without existing registries lose access to the old `bedrock-agentcore` namespace immediately, and the old namespace shuts down on September 17, 2026.
此次变更在端点、IAM 动作、ARN、SDK 客户端、CLI 命令与记录结构上均不向后兼容；没有既有注册表的客户即刻失去旧 `bedrock-agentcore` 命名空间的访问权限，而旧命名空间将于 2026 年 9 月 17 日关闭。

**Why it matters**

Teams rebuild agents and MCP servers that already exist because nothing makes them discoverable, and a catalog that validates records against MCP and A2A schemas and exposes itself over MCP lets the agents themselves find approved capabilities instead of relying on a wiki page.
团队之所以重复造已经存在的智能体与 MCP 服务器，是因为没有任何东西让它们可被发现；一个按 MCP 与 A2A 规范校验记录、并通过 MCP 暴露自身的目录，让智能体自己就能找到已批准的能力，而不必依赖一个 wiki 页面。

**Sources:** [AWS Agent Registry migration guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-faq.html) · [AWS Agent Registry overview](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html)

<a id="story-github-mcp-allowlists"></a>

### GitHub lets enterprises allowlist the MCP servers Copilot may run

- [ ] Interesting

**Underlying event date:** 2026-08-06

**What happened**

On August 6, GitHub made MCP allowlists generally available in enterprise managed settings, adding `allowedMcpServers` and `deniedMcpServers` keys to `copilot/managed-settings.json` in the source organization's `.github-private` repository, with matchers on remote server URL including wildcards, exact local stdio command and arguments, or user-assigned server name.
8 月 6 日，GitHub 在企业托管设置中正式推出 MCP 白名单：在来源组织的 `.github-private` 仓库中的 `copilot/managed-settings.json` 内新增 `allowedMcpServers` 与 `deniedMcpServers` 两个键，匹配方式支持远程服务器 URL（可用通配符）、本地 stdio 命令与参数的精确匹配，或用户自定义的服务器名称。

GitHub notes that name matching is a convenience rather than a security control because users can rename servers, and enforcement currently covers the GitHub Copilot app, Copilot CLI, and VS Code.
GitHub 指出，按名称匹配只是便利手段而非安全控制，因为用户可以重命名服务器；目前的强制执行范围覆盖 GitHub Copilot 应用、Copilot CLI 与 VS Code。

**Why it matters**

MCP server sprawl is how untrusted tool code reaches a developer's credentials, and central approval expressed as configuration in a repository is the first version of this control that a platform team can review, diff, and roll back like any other policy file.
MCP 服务器泛滥正是不可信工具代码接触开发者凭据的途径；把集中审批表达为仓库中的配置文件，是平台团队第一次可以像审阅其他策略文件那样对这项控制做评审、比对差异与回滚。

**Sources:** [GitHub Changelog](https://github.blog/changelog/2026-08-06-mcp-allowlists-in-enterprise-managed-settings/)

<a id="story-insygna-agent-report-card"></a>

### Insygna offers a free security scorecard for agents before they get system access

- [X] Interesting

**Underlying event date:** 2026-08-10

**What happened**

On August 10, Insygna launched the Agent Report Card, a free service where a company connects an agent repository and receives a 0-to-100 score across secret exposure, dependency vulnerabilities, code security, container hardening, LLM security measured against the OWASP LLM Top 10, and image security, plus findings with affected files and line numbers, version tracking, and a shareable Insygna Verified badge.
8 月 10 日，Insygna 推出 Agent Report Card：这是一项免费服务，企业接入智能体代码仓库后，可获得涵盖密钥暴露、依赖漏洞、代码安全、容器加固、按 OWASP LLM Top 10 衡量的 LLM 安全与镜像安全六个维度的 0 至 100 分评分，并附带指明受影响文件与行号的问题清单、版本跟踪，以及可对外展示的 Insygna Verified 徽章。

Insygna reports that the median tested agent scores below 50, with roughly 60% of tested agents in that range, and frames the check with its CEO's argument that an agent gets employee-level system access with none of the verification.
Insygna 称受测智能体的中位分数低于 50，约 60% 的受测智能体落在该区间，并以其 CEO 的说法为这项检查定调：智能体获得了与员工同级的系统访问权限，却完全没有经过相应的背景核查。

**Why it matters**

Nothing stops a team from granting an agent repository production credentials today, and a free pre-deployment scan against named dimensions gives reviewers a concrete artifact to demand, even though the score and the badge come from the vendor and are not an independent audit.
今天没有任何机制阻止团队把生产凭据交给一个智能体仓库；一次面向明确维度的免费部署前扫描，为评审者提供了可以索要的具体材料——尽管评分与徽章均出自供应商，并不构成独立审计。

**Sources:** [AIThority](https://aithority.com/security/insygna-launches-free-public-service-to-help-companies-stop-rogue-ai-agents/)

## Other AI Stories

<a id="story-meta-muse-glimmer"></a>

### Meta open-sources a 30B agent model that runs on one consumer GPU

- [ ] Interesting

**Underlying event date:** 2026-08-10

**What happened**

On August 10, Meta released Muse Glimmer, a 30-billion-parameter model under Apache 2.0 built for always-on local agents, distilled from a larger Muse system into a 2B vision encoder feeding a 28B text decoder, with weights on Hugging Face and optimized integrations for llama.cpp, MLX, and ExecuTorch promised in the following days.
8 月 10 日，Meta 发布 Muse Glimmer：一款采用 Apache 2.0 许可、面向常驻本地智能体的 300 亿参数模型，由更大的 Muse 系统蒸馏而来，结构为 20 亿参数视觉编码器接 280 亿参数文本解码器；权重已上传 Hugging Face，面向 llama.cpp、MLX 与 ExecuTorch 的优化集成承诺在随后几天推出。

Meta targets reliable tool calling, persistent state across restarts, local coding, long tool-use sessions, and LLM-as-a-judge evaluation, and reports category-best scores of 75.5 on MCP Atlas, 51.2 on SWE-Bench Pro, 94.7 on AIME 2026, and 78.8 on Charxiv Reasoning.
Meta 的目标场景包括可靠的工具调用、跨重启的持久状态、本地编码、长时间工具使用会话与 LLM-as-a-judge 评估，并报告了同类最佳成绩：MCP Atlas 75.5、SWE-Bench Pro 51.2、AIME 2026 94.7、Charxiv Reasoning 78.8。

**Why it matters**

An agent that keeps running on a laptop changes which workloads can touch sensitive data at all, and permissive weights at a size that fits one consumer GPU put that decision inside the team rather than inside a vendor contract.
一个能在笔记本上持续运行的智能体，改变了哪些工作负载可以接触敏感数据的边界；而在单张消费级 GPU 可承载的规模上给出宽松许可的权重，把这一决策交回团队内部，而不再取决于供应商合同。

**Sources:** [Meta for Developers](https://developer.meta.com/ai/models/muse-glimmer/) · [VentureBeat](https://venturebeat.com/technology/meta-returns-to-open-source-with-muse-glimmer-an-apache-2-0-licensed-30b-parameter-ai-model-optimized-for-agents-available-now)

<a id="story-cloudflare-precursor-agent-behavior"></a>

### Cloudflare says sessions now switch between human and agent mid-flight

- [ ] Interesting

**Underlying event date:** 2026-08-07

**What happened**

On August 7, Cloudflare described its shift from point-in-time risk assessment to continuous trust evaluation, reporting 206 million Precursor client-side behavior evaluation events across 73,438 zones in a single 24-hour period and finding that suspicious behavior often appears mid-session and that traffic shifts between human and agentic within one session.
8 月 7 日，Cloudflare 阐述了其从时点风险评估转向持续信任评估的变化，称在单个 24 小时周期内于 73,438 个 zone 上产生了 2.06 亿次 Precursor 客户端行为评估事件，并发现可疑行为往往出现在会话中段，且同一会话内的流量会在人类与智能体之间来回切换。

The company also previewed Adaptive Intelligence, a detection engine it says will keep learning and self-adjusting instead of requiring manual version updates, alongside mitigations including AI Labyrinth and queuing for legitimate bots.
该公司还预告了 Adaptive Intelligence 检测引擎，称其将持续学习并自我调整，而不再依赖人工版本更新，同时配合 AI Labyrinth 与对正当机器人排队等缓解手段。

**Why it matters**

Bot-or-human is the assumption under most access control, and a session that legitimately hands off from a person to a shopping or checkout agent breaks both the block-all-bots policy and the trust-the-logged-in-user policy at the same time.
"机器人还是人"是多数访问控制的隐含前提；而一个由人正当交接给购物或结账智能体的会话，会同时打破"全面封禁机器人"与"信任已登录用户"这两种策略。

**Sources:** [Cloudflare Blog](https://blog.cloudflare.com/good-and-bad-agentic-behaviors/)

<a id="story-corma-defensive-security-seed"></a>

### Corma raises $60 million to build a defensive-only security model

- [ ] Interesting

**Underlying event date:** 2026-08-10

**What happened**

On August 10, Corma announced a $60 million seed round led by Sequoia Capital with Khosla Ventures and Coatue, to build a foundation model purpose-built for defensive cybersecurity from offices in Tel Aviv and San Francisco.
8 月 10 日，Corma 宣布完成由 Sequoia Capital 领投、Khosla Ventures 与 Coatue 参投的 6000 万美元种子轮融资，将在特拉维夫与旧金山两地打造专为防御性网络安全构建的基础模型。

Founded in 2025 by AI researchers including Google and DeepMind alumni alongside Unit 8200 veterans, the company says early Fortune 100 and Fortune 500 deployments cut threat response times by more than 94% and that in its internal simulations AI attackers succeeded 88% of the time while AI defenders detected only 12% of threats.
公司成立于 2025 年，创始团队包括来自 Google 与 DeepMind 的 AI 研究者以及 8200 部队老兵；公司称其在《财富》100 强与 500 强企业的早期部署将威胁响应时间缩短超过 94%，并称在内部模拟中 AI 攻击方成功率为 88%，而 AI 防守方仅检测出 12% 的威胁。

**Why it matters**

The asymmetry these numbers describe is the same one behind this year's agent-driven intrusions, and a seed round of this size for a defense-only lab is a bet that the counterweight has to be a model rather than more human analysts.
这些数字所描述的不对称，正是本年度智能体驱动入侵背后的同一种不对称；为一家只做防御的实验室投入这一规模的种子轮，是在押注制衡手段必须是一个模型，而不是更多人力分析师。

**Sources:** [Fortune](https://fortune.com/2026/08/10/exclusive-corma-raises-60-million-from-sequoia-for-ai-trained-to-defend-against-cyberattacks/) · [SiliconANGLE](https://siliconangle.com/2026/08/10/corma-launches-60m-funding-defensive-cybersecurity-ai/)

<a id="story-model-knowledge-cutoff-probing"></a>

### A probing method infers which training run a frontier model came from

- [X] Interesting

**Underlying event date:** 2026-08-10

**What happened**

On August 10, independent researcher Shrivu Shankar published a method that infers training-run identity from three signals — eight-way multiple-choice quizzes built from daily Wikipedia events, the model's own answer to what today's date is, and 50 repeated "what model are you?" queries.
8 月 10 日，独立研究者 Shrivu Shankar 发布了一种方法，通过三类信号推断模型属于哪一次训练运行：由维基百科每日事件构建的八选一测验、模型自己对"今天是几号"的回答，以及重复 50 次的"你是哪个模型"提问。

He concludes that Anthropic's Opus 4.7 and later models come from one training run cutting off around late December 2025, that the GPT-5.6 family sits on a separate checkpoint finishing around late February 2026, that Opus 5's factual knowledge looks closer to January 2026 than its published May 2026 cutoff, and that models sometimes claim prior-generation identities, which he reads as training on earlier model outputs.
他的结论是：Anthropic 的 Opus 4.7 及之后的模型来自同一次截止于 2025 年 12 月底左右的训练运行；GPT-5.6 家族则处在另一个约完成于 2026 年 2 月底的检查点上；Opus 5 的事实性知识看起来更接近 2026 年 1 月，而非其公布的 2026 年 5 月截止时间；模型有时会自称上一代身份，他认为这表明训练数据中包含了早期模型的输出。

**Why it matters**

Published cutoff dates are what teams use to decide whether a model can be trusted on recent APIs, prices, or vulnerabilities, and a cheap probe that contradicts the datasheet is more useful than the datasheet.
公布的知识截止日期，是团队判断某个模型能否在近期 API、价格或漏洞问题上被信任的依据；一个成本低廉却与官方说明相矛盾的探测方法，比官方说明更有用。

**Sources:** [Shrivu Shankar](https://blog.sshh.io/p/exploring-claudegpt-knowledge-cutoffs)

## AI at Work

No qualifying story this week. Searches in English and Simplified Chinese for employers changing how their own employees may use AI surfaced only out-of-window events — Microsoft's 2025 "no longer optional" memo, Meta's 2026 review criteria, Accenture's promotion requirement, Uber's June 2026 per-employee spending cap, the DNC's April 2026 tool restrictions, Samsung's earlier ban, and AXA's July 21, 2026 Copilot rollout — plus aggregate employer surveys and sector-wide regulation, none of which meet this section's requirement of one named organization changing its stance inside the coverage window.
本期没有符合标准的报道。围绕"雇主如何改变自身员工使用 AI 的规则"进行的英文与简体中文检索，只找到窗口期之外的事件——微软 2025 年"不再可选"的内部备忘录、Meta 2026 年的考核标准、埃森哲把晋升与 AI 使用挂钩、Uber 2026 年 6 月的人均支出上限、美国民主党全国委员会 2026 年 4 月的工具限制、三星更早的禁令，以及 AXA 于 2026 年 7 月 21 日宣布的 Copilot 推广——此外只有面向雇主整体的调查与行业级监管，均不满足本栏目"一家具名机构在覆盖窗口内改变立场"的要求。

## Follow-ups to Interesting Stories

No marked interest had a qualifying in-window update this week. Every tracked item is listed below with its status.
本周没有任何已标记的关注项获得符合标准的窗口期内更新。所有跟踪项及其状态列于下方。

## Tracked Interests

- **[NVIDIA releases Cosmos 3 Edge for local physical AI](2026-07-24-ai-newsletter.md#story-nvidia-cosmos-3-edge-siggraph)** — Marked 2026-07-24. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[OpenAI rolls out Health in ChatGPT to U.S. users](2026-07-27-ai-newsletter.md#story-chatgpt-health-rollout)** — Marked 2026-07-27. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[月之暗面正式开源 Kimi K3](2026-07-29-ai-newsletter.md#story-kimi-k3-open-source)** — Marked 2026-07-29. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[Reader spotlight: SpecForge pairs LLMs with formal specifications](2026-07-29-ai-newsletter.md#story-imiron-specforge-ai-formal-specs)** — Marked 2026-07-29. No qualifying update found this week; Imiron's newest posts remain its June 10, 2026 accelerator announcement and June 1, 2026 funding round. Uncheck `Interesting` in the original story to stop tracking it.
- **[LangSmith LLM Gateway enters public beta as a runtime control plane](2026-07-31-ai-newsletter.md#story-langsmith-llm-gateway-public-beta)** — Marked 2026-07-31. No qualifying update found this week; the gateway remains in public beta. Uncheck `Interesting` in the original story to stop tracking it.
- **[Deep Agents v0.7 cuts base input tokens by 65%](2026-07-31-ai-newsletter.md#story-deep-agents-v07-token-diet)** — Marked 2026-07-31. No qualifying update found this week; only patch releases landed in the window. Uncheck `Interesting` in the original story to stop tracking it.
- **[BrowserStack puts an agentic testing harness inside the IDE](2026-07-31-ai-newsletter.md#story-browserstack-test-companion-ide)** — Marked 2026-07-31. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[herdr 0.8.0 relicenses to Apache-2.0 and cuts multi-client CPU by 95%](2026-08-04-ai-newsletter.md#story-herdr-v080-agent-multiplexer)** — Marked 2026-08-04. No qualifying update found this week; the latest published build predates the window. Uncheck `Interesting` in the original story to stop tracking it.
- **[OpenAI introduces Astra with ten Lean-certified mathematical results](2026-08-04-ai-newsletter.md#story-openai-astra-lean-certified-proofs)** — Marked 2026-08-04. No qualifying update found this week; the Astra pause was already published in the 2026-08-10 edition. Uncheck `Interesting` in the original story to stop tracking it.
- **[LongHorizon-Harness gives computer-use agents a manager, executor, and auditor](2026-08-05-ai-newsletter.md#story-longhorizon-harness)** — Marked 2026-08-05. No qualifying update found this week beyond the tagged releases already published in the 2026-08-10 edition. Uncheck `Interesting` in the original story to stop tracking it.
- **[Drata ships agent discovery, scoring, and blocking in limited availability](2026-08-06-ai-newsletter.md#story-drata-ai-agent-governance)** — Marked 2026-08-06. No qualifying update found this week; the product remains in limited availability. Uncheck `Interesting` in the original story to stop tracking it.
- **[WriteGuard puts risk tiers and attribution in front of MCP writes](2026-08-06-ai-newsletter.md#story-cloudflare-writeguard-mcp-controls)** — Marked 2026-08-06. No qualifying update found this week; WriteGuard remains in private beta. Uncheck `Interesting` in the original story to stop tracking it.

## Watch Next Week

The AWS Agent Registry migration window closes on September 17, 2026, so teams that ran the preview namespace have to finish endpoint, IAM, and schema migration or lose the data left behind in it.
AWS Agent Registry 的迁移窗口将于 2026 年 9 月 17 日关闭，因此使用过预览命名空间的团队必须完成端点、IAM 与数据结构迁移，否则将丢失留在旧命名空间中的数据。

Meta promised llama.cpp, MLX, and ExecuTorch integrations for Muse Glimmer within days of the August 10 release, and Cloudflare's Adaptive Intelligence engine is still described as coming soon, so both claims should be checkable against shipped artifacts shortly.
Meta 承诺在 8 月 10 日发布后数日内推出 Muse Glimmer 面向 llama.cpp、MLX 与 ExecuTorch 的集成，而 Cloudflare 的 Adaptive Intelligence 引擎目前仍标注为即将推出，因此这两项说法很快都能对照实际交付物加以核验。

## Sources

- [EN] [Claude by Anthropic](https://claude.com/blog/claude-enterprise-inference-hooks)
- [EN] [Claude Platform Docs](https://platform.claude.com/docs/en/manage-claude/inference-hooks)
- [EN] [AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-bedrock-agentcore-runtime-instances-generally-available/)
- [EN] [AWS News Blog](https://aws.amazon.com/blogs/aws/runtime-instances-persistent-compute-for-production-ai-agents-on-amazon-bedrock-agentcore/)
- [EN] [AWS Agent Registry migration guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-faq.html)
- [EN] [AWS Agent Registry overview](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html)
- [EN] [GitHub Changelog](https://github.blog/changelog/2026-08-06-mcp-allowlists-in-enterprise-managed-settings/)
- [EN] [AIThority](https://aithority.com/security/insygna-launches-free-public-service-to-help-companies-stop-rogue-ai-agents/)
- [EN] [Meta for Developers](https://developer.meta.com/ai/models/muse-glimmer/)
- [EN] [VentureBeat](https://venturebeat.com/technology/meta-returns-to-open-source-with-muse-glimmer-an-apache-2-0-licensed-30b-parameter-ai-model-optimized-for-agents-available-now)
- [EN] [Cloudflare Blog](https://blog.cloudflare.com/good-and-bad-agentic-behaviors/)
- [EN] [Fortune](https://fortune.com/2026/08/10/exclusive-corma-raises-60-million-from-sequoia-for-ai-trained-to-defend-against-cyberattacks/)
- [EN] [SiliconANGLE](https://siliconangle.com/2026/08/10/corma-launches-60m-funding-defensive-cybersecurity-ai/)
- [EN] [Shrivu Shankar](https://blog.sshh.io/p/exploring-claudegpt-knowledge-cutoffs)
