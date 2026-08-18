# Plugins, Transcripts, and Watermarks: the Week Agents Got Governable

**Coverage:** 2026-08-08–2026-08-14 (Europe/Stockholm)

## Executive Brief

Agent tooling this week pushed hard on portability and oversight: GitHub made Agent Plugins 1.0 generally available across VS Code, the Copilot CLI, and the Copilot app on August 12, while Anthropic's Compliance API began returning transcripts of Cowork and Claude Code sessions running on employees' own machines on August 11.
本周的智能体工具集中发力于可移植性与可监管性：8 月 12 日，GitHub 让 Agent Plugins 1.0 在 VS Code、Copilot CLI 和 Copilot 应用中全面可用；8 月 11 日，Anthropic 的 Compliance API 开始返回运行在员工本机上的 Cowork 与 Claude Code 会话记录。

On the model side, Google shipped Gemini 3.7 Flash and OpenAI previewed a Cerebras-powered Ultrafast mode on August 13, and DeepSeek released both its V4 Pro final build and an MIT-licensed agent framework the same evening.
在模型侧，8 月 13 日 Google 发布了 Gemini 3.7 Flash，OpenAI 预览了由 Cerebras 提供算力的 Ultrafast 模式；同一晚，DeepSeek 同时放出了 V4 Pro 正式版和一个采用 MIT 协议的智能体框架。

## AI Tools

<a id="story-github-agent-plugins-1-0"></a>

### GitHub makes Agent Plugins 1.0 generally available across every Copilot surface

- [ ] Interesting

**Underlying event date:** 2026-08-12

**What happened**

On August 12, GitHub made Agent Plugins 1.0 generally available on all Copilot plans across VS Code, the Copilot CLI, the Copilot app, and the Copilot SDK, where a single plugin package bundles agent skills together with MCP server configuration — a deployment runbook shipped alongside the tool integration it needs.
8 月 12 日，GitHub 在所有 Copilot 套餐中让 Agent Plugins 1.0 于 VS Code、Copilot CLI、Copilot 应用和 Copilot SDK 上全面可用；单个插件包会将智能体技能与 MCP 服务器配置打包在一起——例如把部署操作手册与它所需的工具集成一并交付。

Copilot-specific capabilities such as custom agents, commands, rules, hooks, and extensions live in a namespaced `com.github.copilot/` directory that other clients simply ignore, and the underlying open standard was published on August 6 with backing from AWS, Anysphere, Microsoft, OpenAI, Vercel, and Google.
Copilot 专有能力（自定义智能体、命令、规则、hooks 和扩展）被放在带命名空间的 `com.github.copilot/` 目录中，其他客户端会直接忽略；其底层开放标准于 8 月 6 日发布，得到 AWS、Anysphere、Microsoft、OpenAI、Vercel 和 Google 的支持。

**Why it matters**

Publishing an agent extension across several platforms has meant maintaining a separate manifest and directory layout per client, and a portable package with an ignored vendor namespace removes that duplication without forcing anyone to give up client-specific features.
在多个平台发布智能体扩展此前意味着要为每个客户端维护独立的清单文件和目录结构，而一个带有"可被忽略的厂商命名空间"的可移植包消除了这种重复，同时不必放弃各客户端的专有功能。

**Sources:** [GitHub Changelog](https://github.blog/changelog/2026-08-12-agent-plugins-1-0-in-vs-code-copilot-cli-and-the-copilot-app)

<a id="story-anthropic-compliance-api-local-sessions"></a>

### Anthropic's Compliance API starts returning Cowork and Claude Code transcripts

- [ ] Interesting

**Underlying event date:** 2026-08-11

**What happened**

On August 11, Anthropic extended the Compliance API to sessions that run on users' own machines, adding `GET /v1/compliance/apps/sessions/local` to list an organization's sessions, a per-session metadata endpoint, and a third endpoint returning the full transcript — all reachable in beta for Claude Enterprise with an existing Compliance Access Key and the `read:compliance_user_data` scope.
8 月 11 日，Anthropic 将 Compliance API 扩展到运行于用户本机的会话，新增 `GET /v1/compliance/apps/sessions/local` 用于列出组织内的会话、一个按会话返回元数据的端点，以及第三个返回完整会话记录的端点——Claude Enterprise 组织可在测试版中使用现有的 Compliance Access Key 和 `read:compliance_user_data` 权限范围访问它们。

The endpoints cover prompts, responses, and both web and MCP tool activity for Cowork on desktop, web, and mobile and for Claude Code in the CLI and desktop app, while excluding Claude Code on the web, Claude Code via the Claude Platform, and sessions running on Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Foundry.
这些端点覆盖桌面端、网页端和移动端的 Cowork 以及 CLI 与桌面应用中的 Claude Code 的提示、回复，以及网页和 MCP 工具活动；但不包括网页版 Claude Code、通过 Claude Platform 使用的 Claude Code，以及运行在 Amazon Bedrock、Google Cloud Vertex AI 或 Microsoft Foundry 上的会话。

**Why it matters**

Agent sessions that execute on a laptop are the hardest ones for a security team to see, and pulling their transcripts through the same interface already used for Claude chats gives audit and eDiscovery a single path without standing up per-product logging.
在笔记本电脑上执行的智能体会话是安全团队最难看见的部分，而通过已用于 Claude 聊天的同一接口调取其会话记录，让审计与电子取证获得了统一路径，无需为每个产品分别搭建日志系统。

**Sources:** [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview) · [Claude blog](https://claude.com/blog/compliance-api-cowork-and-claude-code)

<a id="story-deepseek-harness-developer-preview"></a>

### DeepSeek 以 MIT 协议开源 Harness 智能体框架开发者预览版

- [ ] Interesting

**底层事件日期：** 2026-08-13

**发生了什么**

8 月 13 日晚，DeepSeek 面向全球开发者开放 DeepSeek Harness 开发者预览版（v0.1）测试，并同步以 MIT 协议开放源代码，项目托管在 github.com/deepseek-ai/deepseek-harness，可用 `npx @deepseek-ai/dsh web` 一条命令在本地跑起来。

该框架采用"一切皆插件"的设计理念，模型、工具、技能、会话、沙箱、存储、循环、调度与 UI 等全部智能体能力均由插件组合而成，可自由替换、灵活重组；官方同时承认作为早期预览版本，仍有许多细节有待打磨。

**为何重要**

把模型本身降级为"代理技术栈中一个可替换的部分"，意味着团队可以在不重写编排逻辑的前提下更换底层模型或工具后端，而 MIT 协议与插件边界也让这套框架比多数厂商自带的智能体运行时更容易被审计和裁剪。

**来源：** [新浪科技](https://finance.sina.com.cn/tech/roll/2026-08-13/doc-inineuqm9899462.shtml)

<a id="story-langsmith-byoc-aws-ga"></a>

### LangSmith BYOC reaches general availability on AWS

- [ ] Interesting

**Underlying event date:** 2026-08-12

**What happened**

On August 12, LangChain made LangSmith Bring Your Own Cloud generally available on AWS, splitting the deployment so that the control plane handling authentication, billing, and platform management stays in LangChain's cloud while the data plane — a private Kubernetes cluster, databases, and storage — runs inside the customer's own AWS account and VPC.
8 月 12 日，LangChain 让 LangSmith 的"自带云"（BYOC）方案在 AWS 上正式全面可用；部署被拆分为两部分：负责认证、计费和平台管理的控制平面留在 LangChain 云端，而数据平面——私有 Kubernetes 集群、数据库与存储——运行在客户自己的 AWS 账户和 VPC 内。

Traces, datasets, experiments, prompts, deployments, and sandbox data all stay in the customer's environment, which LangChain positions at enterprises in financial services, healthcare, cybersecurity, and other regulated settings that need data residency and network isolation.
追踪数据、数据集、实验、提示词、部署和沙箱数据全部留在客户环境中；LangChain 将该方案定位于金融服务、医疗、网络安全等需要数据驻留与网络隔离的受监管行业客户。

**Why it matters**

Agent observability is only adoptable where the traces are allowed to live, and a GA'd BYOC tier lets a regulated team keep evaluation and deployment tooling without taking on the operational burden of a fully self-hosted stack.
智能体可观测性能否落地，取决于追踪数据被允许存放在哪里；一个正式可用的 BYOC 层级让受监管团队既能保留评测与部署工具，又不必承担完全自托管的运维负担。

**Sources:** [LangChain blog](https://www.langchain.com/blog/langsmith-byoc-is-now-generally-available-on-aws)

<a id="story-copilot-memory-ollama-jetbrains"></a>

### GitHub Copilot gains cross-session memory and Ollama models in JetBrains IDEs

- [ ] Interesting

**Underlying event date:** 2026-08-11

**What happened**

On August 11, GitHub shipped Copilot memory for JetBrains IDEs, letting Copilot retain and recall useful information across agent chat sessions with a toggle in the Copilot Memory settings portal, and added Ollama as a bring-your-own-key provider with provider configuration and model selection throughout the JetBrains experience.
8 月 11 日，GitHub 为 JetBrains 系列 IDE 推出 Copilot memory，让 Copilot 能够在多次智能体对话之间保留并调用有用信息，并可在 Copilot Memory 设置页中开关；同时新增 Ollama 作为"自带密钥"的模型提供方，在整个 JetBrains 体验中支持提供方配置与模型选择。

**Why it matters**

Re-explaining a project's conventions at the start of every agent session is pure overhead, and pairing persistent memory with a local-model provider lets teams keep both that context and their inference inside their own boundary.
在每次智能体会话开始时重新说明项目约定纯属额外开销，而把持久化记忆与本地模型提供方结合起来，可让团队把上下文和推理都保留在自己的边界之内。

**Sources:** [GitHub Changelog](https://github.blog/changelog/2026-08-11-copilot-memory-and-ollama-in-github-copilot-for-jetbrains)

<a id="story-claude-tag-channel-context"></a>

### Claude Tag reads a whole Slack channel before deciding whether to speak

- [ ] Interesting

**Underlying event date:** 2026-08-13

**What happened**

On August 13, Anthropic changed how Claude Tag decides to participate in Slack, evaluating context from across a channel rather than judging messages one at a time, which it reports as roughly 30% better accuracy at knowing when a reply is wanted — for example recognising that two engineers are circling the same bug from different angles without either of them issuing an @-mention.
8 月 13 日，Anthropic 改变了 Claude Tag 在 Slack 中决定是否参与对话的方式：它会评估整个频道的上下文，而不是逐条判断消息；据其数据，判断"何时该回复"的准确率提升约 30%——例如在无人 @ 它的情况下，识别出两位工程师正从不同角度讨论同一个 bug。

The change is available to Claude Teams and Enterprise customers at no additional cost, the expanded context does not count toward spending limits on any plan, and teams can still steer the behaviour with plain-language instructions or switch automatic replies off entirely.
该变更向 Claude Teams 与 Enterprise 客户免费提供，扩大的上下文用量不计入任何套餐的支出上限，团队仍可用自然语言指令来调节其行为，或完全关闭自动回复。

**Why it matters**

An agent parked in a shared channel fails in two directions — interrupting constantly or missing the moment it was needed — so channel-level context plus an off switch is what makes an always-present agent tolerable to the humans around it.
常驻共享频道的智能体会朝两个方向失效：不停打断，或者错过真正该出手的时刻；因此"频道级上下文加一个开关"才是让一个始终在场的智能体被周围同事接受的前提。

**Sources:** [Claude blog](https://claude.com/blog/claude-tag-now-reads-even-more-of-the-room)

## Other AI Stories

<a id="story-gemini-3-7-flash"></a>

### Google launches Gemini 3.7 Flash three weeks after its predecessor

- [ ] Interesting

**Underlying event date:** 2026-08-13

**What happened**

On August 13, Google released Gemini 3.7 Flash as what it calls its most intelligent workhorse model yet for coding and agents, three weeks after Gemini 3.6 Flash, reporting 43.6% versus 34.4% on FrontierCode 1.1, 65.3% versus 49.0% on DeepSWE v1.1, and 30.4% versus 17.0% on AutomationBench.
8 月 13 日，Google 发布 Gemini 3.7 Flash，称其为迄今面向编程与智能体最智能的"主力"模型，距 Gemini 3.6 Flash 仅三周；官方给出的对比成绩为 FrontierCode 1.1 43.6% 对 34.4%、DeepSWE v1.1 65.3% 对 49.0%、AutomationBench 30.4% 对 17.0%。

It carries an introductory price of $0.75 per million input tokens and $3.75 per million output tokens through December 31, 2026, rising to $1.50 and $7.50 afterwards, and is available in Google AI Studio, Android Studio, Google Antigravity, the Gemini Enterprise Agent Platform, and Gemini Spark for AI Pro and Ultra subscribers in more than 160 countries.
其初始优惠价格为每百万输入 token 0.75 美元、每百万输出 token 3.75 美元，有效期至 2026 年 12 月 31 日，之后升至 1.50 美元和 7.50 美元；上线渠道包括 Google AI Studio、Android Studio、Google Antigravity、Gemini Enterprise Agent Platform，以及面向 160 多个国家 AI Pro 与 Ultra 订阅者的 Gemini Spark。

**Why it matters**

A three-week gap between workhorse releases with double-digit gains on agentic benchmarks, sold at half the previous entry price, keeps resetting the cost floor that anyone budgeting a multi-step agent has to plan around.
主力模型之间仅隔三周、智能体基准上取得两位数提升，并以此前一半的入门价格出售，这不断重置着所有为多步智能体做预算的人必须参照的成本底线。

**Sources:** [Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) · [Axios](https://www.axios.com/2026/08/13/google-gemini-37-flash)

<a id="story-openai-ultrafast-mode"></a>

### OpenAI previews a Cerebras-powered Ultrafast mode for GPT-5.6 Sol

- [ ] Interesting

**Underlying event date:** 2026-08-13

**What happened**

On August 13, OpenAI previewed Ultrafast, a service tier running GPT-5.6 Sol up to 14 times faster than standard processing at up to 750 output tokens per second on hardware from the chipmaker Cerebras, offered to a small group of customers with expansion promised as capacity grows.
8 月 13 日，OpenAI 预览了 Ultrafast 服务层级：它在芯片厂商 Cerebras 的硬件上运行 GPT-5.6 Sol，速度最高可达标准处理的 14 倍、每秒最多输出 750 个 token；目前仅向少量客户开放，官方承诺随算力扩容再扩大范围。

OpenAI named incident response, customer service and support, financial market analysis, and e-commerce as the target workloads, framing the tier around the fact that real-time speed has usually meant dropping to a smaller or more specialised model.
OpenAI 将事故响应、客户服务与支持、金融市场分析和电子商务列为目标场景，并强调此前要获得实时速度通常意味着退而使用更小或更专用的模型。

**Why it matters**

Latency is what decides whether an agent can sit inside a live incident channel or a checkout flow at all, and separating speed from model size turns that into a purchasing decision rather than a capability sacrifice.
延迟决定了一个智能体究竟能否嵌入实时事故频道或结账流程，而把速度与模型规模解耦，使之从"能力上的妥协"变成了一项采购决策。

**Sources:** [TechCrunch](https://techcrunch.com/2026/08/13/openai-introduces-ultrafast-a-new-mode-that-makes-gpt-5-6-sol-work-at-14x-the-speed/)

<a id="story-openai-gpt-5-6-cyber"></a>

### OpenAI ships GPT-5.6-Cyber to vetted defenders only

- [ ] Interesting

**Underlying event date:** 2026-08-10

**What happened**

On August 10, OpenAI released GPT-5.6-Cyber, a model built from GPT-5.6 Sol for specialised cybersecurity work, available exclusively through the higher Red tier of its expanded Daybreak programme and only to trusted customer partners reported to include Accenture, IBM, CrowdStrike, and Cloudflare.
8 月 10 日，OpenAI 发布 GPT-5.6-Cyber——一个基于 GPT-5.6 Sol、面向专业网络安全工作的模型，仅通过其扩展后的 Daybreak 计划中更高的 Red 层级提供，且只面向受信任的客户合作方，据报道包括 Accenture、IBM、CrowdStrike 和 Cloudflare。

The lower Blue tier does not include access to the model, and OpenAI positions the release as putting frontier capability with defenders ahead of attackers rather than as a general product launch.
较低的 Blue 层级不包含该模型的访问权限；OpenAI 将此次发布定位为"让防御方先于攻击方拿到前沿能力"，而非一次面向大众的产品发布。

**Why it matters**

Gating an offence-capable model behind a named-partner tier is a distribution control rather than a technical one, which makes the vetting list itself the security boundary that everyone downstream is trusting.
把具备攻击能力的模型限制在"指名合作方"层级之内是一种分发管控而非技术管控，这使得那份审核名单本身成为下游所有人所信赖的安全边界。

**Sources:** [TechCrunch](https://techcrunch.com/2026/08/10/as-ai-led-attacks-multiply-openai-launches-a-new-cyber-model/)

<a id="story-anthropic-text-watermarking"></a>

### Anthropic will watermark Claude's text and files across every product

- [ ] Interesting

**Underlying event date:** 2026-08-11

**What happened**

On August 11, Anthropic said it will embed an imperceptible, machine-readable watermark in text generated by all models released after August 2 and will extend support to older models, applying it across the Claude API, Claude, Claude Code, Claude Cowork, and Claude Tag, with the C2PA open standard used for files.
8 月 11 日，Anthropic 表示将在 8 月 2 日之后发布的所有模型生成的文本中嵌入不可感知、可被机器读取的水印，并会将支持范围扩展到更早的模型；该机制覆盖 Claude API、Claude、Claude Code、Claude Cowork 和 Claude Tag，文件则采用 C2PA 开放标准。

Because the mark operates at the model level it travels with copied text and may survive some editing, though heavy rewrites or translation can remove it, and the company notes a watermark only shows Claude had a hand in something rather than that Claude wrote all of it — a proofreading pass can leave the same trace.
由于水印作用于模型层面，它会随复制的文本一起传递，并可能在一定程度的编辑后仍然存在，但大幅改写或翻译可能将其去除；该公司同时指出，水印只表明 Claude 参与过某项内容，而非表明全部内容由 Claude 生成——一次校对也会留下同样的痕迹。

**Why it matters**

The EU AI Act's transparency requirements that took effect on August 2 drove the change, but shipping it everywhere Claude runs rather than in Europe alone makes provenance marking a default property of the output that downstream reviewers can start assuming.
推动这一变更的是 8 月 2 日生效的欧盟《人工智能法案》透明度要求，但把它部署到 Claude 运行的所有地方而不只是欧洲，使来源标记成为输出的默认属性，下游审阅者可以开始据此进行假定。

**Sources:** [TechCrunch](https://techcrunch.com/2026/08/11/anthropic-says-it-will-watermark-text-generated-by-its-ai-models/) · [Fortune](https://fortune.com/2026/08/11/anthropic-claude-watermark-ai-text-police-ai-slop/)

<a id="story-deepseek-v4-pro-official"></a>

### DeepSeek V4 Pro 正式版上线，智能体评测逼近顶级闭源模型

- [ ] Interesting

**底层事件日期：** 2026-08-13

**发生了什么**

8 月 13 日晚，DeepSeek 发布 V4 Pro 正式版，官方 API 文档将 deepseek-v4-pro 对应版本更新为 DeepSeek-V4-Pro-0813，价格为每百万 token 3 元，官方当前仍未上调 API 使用价格。

从官方给出的跑分图看，V4 Pro 在 Agent 相关评测上的表现已几乎可与 Claude Fable 5 等顶级模型比肩；此前因用户大量使用 V4 Flash，其官方 API 曾多次出现性能下降。

**为何重要**

一个在智能体评测上接近顶级闭源模型、而单价维持在每百万 token 3 元的正式版，会直接改变中文团队在"自托管开源模型"与"调用海外 API"之间的成本权衡。

**来源：** [新浪财经](https://finance.sina.com.cn/roll/2026-08-13/doc-ininavwz3327589.shtml)

## AI at Work

<a id="story-compass-per-engineer-ai-budgets"></a>

### Compass puts a named AI budget on every engineer

- [ ] Interesting

**Stance:** Discouraging — Compass

**Underlying event date:** 2026-08-12

**What happened**

Speaking publicly for the first time on August 12, Compass CTO Shay Artzi said the real-estate brokerage has set per-engineer AI budgets — "We also put budgets for every engineer, so they are aware of how they're spending" — enforced through financially bounded agreements with Anthropic and Google, and covering engineers alongside the real-estate professionals using its AI Assistant and general corporate staff.
8 月 12 日首次公开表态时，房地产经纪公司 Compass 的 CTO Shay Artzi 表示公司已为每位工程师设定 AI 预算——"我们还为每位工程师设定了预算，好让他们清楚自己花了多少"——并通过与 Anthropic 和 Google 之间有财务上限的协议来落实，覆盖范围包括工程师、使用其 AI Assistant 的房产经纪人以及一般行政员工。

The underlying decision date was not disclosed, and the measure is a per-person spending ceiling made visible to the engineer rather than a restriction on which tools or models may be used.
其内部决策日期未被披露，该措施是一个对工程师本人可见的人均支出上限，而不是对可使用哪些工具或模型的限制。

**Why it matters**

Making each engineer's own consumption legible to them is the cheapest form of restraint available to an employer, and it lands differently from a blanket model ban because it leaves the tool choice intact while transferring the cost question onto the individual.
让每位工程师看见自己的用量，是雇主能采取的成本最低的约束形式；它与"全面禁用某个模型"的效果不同，因为工具选择权仍在，但成本问题被转移到了个人身上。

**Sources:** [Fortune](https://fortune.com/2026/08/12/cios-and-ctos-spent-years-lauding-ai-now-with-costs-rising-theyre-putting-limits-on-how-its-used/)

<a id="story-yum-brands-cheaper-model-training"></a>

### Yum Brands trains staff onto cheaper models and asks leaders to budget AI like headcount

- [ ] Interesting

**Stance:** Discouraging — Yum Brands

**Underlying event date:** 2026-08-12

**What happened**

Also speaking publicly on August 12, Yum Brands chief digital and technology officer Jim Dausch said AI token usage at the KFC and Taco Bell operator is not yet "a material number, but the trajectory was one that we're watching," and that as much as 95% of the tasks staff give AI tools can be handled by more basic, less expensive models.
同样在 8 月 12 日公开表态时，KFC 与 Taco Bell 的母公司 Yum Brands 的首席数字与技术官 Jim Dausch 表示，公司的 AI token 用量目前还不是"一个重要的数字，但这个趋势是我们正在关注的"，并称员工交给 AI 工具的任务中多达 95% 可以由更基础、更便宜的模型完成。

That reading led Yum to promote more training on AI model usage and to advise business leaders to manage digital spending the same way they budget a department's headcount, which is guidance and training rather than an enforced cap.
基于这一判断，Yum 加强了 AI 模型使用方面的培训，并建议业务负责人像编制部门人头预算一样管理数字支出——这属于指导与培训，而非强制上限。

**Why it matters**

Routing work to the cheapest adequate model is a skill an employer has to teach rather than a setting it can flip, and treating AI spend as a departmental budget line quietly moves the decision from IT into every manager's plan.
把工作路由到"足够好且最便宜"的模型是一项需要雇主去教的技能，而不是一个可以直接切换的开关；把 AI 支出当作部门预算科目，则悄悄把决策权从 IT 转移到了每位管理者的计划之中。

**Sources:** [Fortune](https://fortune.com/2026/08/12/cios-and-ctos-spent-years-lauding-ai-now-with-costs-rising-theyre-putting-limits-on-how-its-used/)

## Follow-ups to Interesting Stories

### LongHorizon-Harness ships a computer-use plugin layer, Terminal-Bench evaluation, and a browser dashboard

**Original interest:** [LongHorizon-Harness gives computer-use agents a manager, executor, and auditor](2026-08-05-ai-newsletter.md#story-longhorizon-harness)

**Underlying event date:** 2026-08-11–2026-08-14

**What changed**

v0.1.4 landed on August 11 with unified computer-use plugin support, a final user-facing reply, execution in the launch directory, and Terminal-Bench evaluation integration, and v0.1.5 followed on August 14 with a more user-friendly dashboard plus npm and httpx test fixes.
8 月 11 日发布的 v0.1.4 带来了统一的 computer-use 插件支持、面向用户的最终回复、在启动目录中执行，以及 Terminal-Bench 评测集成；8 月 14 日的 v0.1.5 紧随其后，提供了更易用的仪表盘，并修复了 npm 与 httpx 测试错误。

**Why it matters**

The original harness was a three-role architecture described in a paper; two releases inside four days turning it into a plugin surface with a browser workbench and a bench-marked evaluation path is what moves it from an interesting design to something a team can actually run.
最初的 harness 是论文中描述的三角色架构；四天内的两次发布把它变成了带浏览器工作台和可跑基准评测路径的插件化系统，这才使它从一个有趣的设计变成团队真正可以运行的东西。

**Sources:** [GitHub releases](https://github.com/AMAP-ML/LongHorizon-Harness/releases)

## Tracked Interests

- **[NVIDIA releases Cosmos 3 Edge for local physical AI](2026-07-24-ai-newsletter.md#story-nvidia-cosmos-3-edge-siggraph)** — Marked 2026-07-24. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[OpenAI rolls out Health in ChatGPT to U.S. users](2026-07-27-ai-newsletter.md#story-chatgpt-health-rollout)** — Marked 2026-07-27. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[月之暗面正式开源 Kimi K3](2026-07-29-ai-newsletter.md#story-kimi-k3-open-source)** — Marked 2026-07-29. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[Reader spotlight: SpecForge pairs LLMs with formal specifications](2026-07-29-ai-newsletter.md#story-imiron-specforge-ai-formal-specs)** — Marked 2026-07-29. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[LangSmith LLM Gateway enters public beta as a runtime control plane](2026-07-31-ai-newsletter.md#story-langsmith-llm-gateway-public-beta)** — Marked 2026-07-31. No qualifying update found this week; the gateway remains in public beta and GA pricing is still unannounced. Uncheck `Interesting` in the original story to stop tracking it.
- **[Deep Agents v0.7 cuts base input tokens by 65%](2026-07-31-ai-newsletter.md#story-deep-agents-v07-token-diet)** — Marked 2026-07-31. No qualifying update found this week; the related Managed Deep Agents public beta fell on 2026-08-07, one day before this coverage window. Uncheck `Interesting` in the original story to stop tracking it.
- **[BrowserStack puts an agentic testing harness inside the IDE](2026-07-31-ai-newsletter.md#story-browserstack-test-companion-ide)** — Marked 2026-07-31. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[herdr 0.8.0 relicenses to Apache-2.0 and cuts multi-client CPU by 95%](2026-08-04-ai-newsletter.md#story-herdr-v080-agent-multiplexer)** — Marked 2026-08-04. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[OpenAI introduces Astra with ten Lean-certified mathematical results](2026-08-04-ai-newsletter.md#story-openai-astra-lean-certified-proofs)** — Marked 2026-08-04. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[LongHorizon-Harness gives computer-use agents a manager, executor, and auditor](2026-08-05-ai-newsletter.md#story-longhorizon-harness)** — Marked 2026-08-05. Qualifying follow-up included above. Uncheck `Interesting` in the original story to stop tracking it.
- **[Drata ships agent discovery, scoring, and blocking in limited availability](2026-08-06-ai-newsletter.md#story-drata-ai-agent-governance)** — Marked 2026-08-06. No qualifying update found this week; the product remains in limited availability. Uncheck `Interesting` in the original story to stop tracking it.
- **[WriteGuard puts risk tiers and attribution in front of MCP writes](2026-08-06-ai-newsletter.md#story-cloudflare-writeguard-mcp-controls)** — Marked 2026-08-06. No qualifying update found this week; the private beta has not moved. Uncheck `Interesting` in the original story to stop tracking it.
- **[Anthropic puts a customer-run checkpoint in front of every Claude Enterprise prompt](2026-08-11-ai-newsletter.md#story-anthropic-inference-hooks)** — Marked 2026-08-11. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[Insygna offers a free security scorecard for agents before they get system access](2026-08-11-ai-newsletter.md#story-insygna-agent-report-card)** — Marked 2026-08-11. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[A probing method infers which training run a frontier model came from](2026-08-11-ai-newsletter.md#story-model-knowledge-cutoff-probing)** — Marked 2026-08-11. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.

## Watch Next Week

GitHub's changelog names AWS, Anysphere, Microsoft, OpenAI, Vercel, and Google as backers of the Agent Plugins standard, so the test of portability is whether any of them ships the same package format on their own surfaces rather than a namespaced variant.
GitHub 的更新日志将 AWS、Anysphere、Microsoft、OpenAI、Vercel 和 Google 列为 Agent Plugins 标准的支持方，因此可移植性的检验标准在于它们中是否有谁在自己的产品上落地同一套包格式，而不是一个带命名空间的变体。

Anthropic said it will extend watermarking support to models released before August 2, which is the claim to watch, since a mark that covers only the newest models leaves most deployed Claude output unmarked.
Anthropic 表示会把水印支持扩展到 8 月 2 日之前发布的模型，这正是值得关注的承诺——若水印只覆盖最新模型，绝大多数已部署的 Claude 输出仍不带标记。

Both Compass and Yum Brands described their cost controls publicly for the first time on the same day and neither disclosed a decision date, so the thing to watch is whether peers publish the policy itself rather than an executive's characterisation of it.
Compass 与 Yum Brands 都在同一天首次公开描述其成本管控措施，且均未披露决策日期；因此值得关注的是同行是否会公布政策文本本身，而不只是高管对政策的描述。

## Sources

- [EN] [GitHub Changelog — Agent Plugins 1.0](https://github.blog/changelog/2026-08-12-agent-plugins-1-0-in-vs-code-copilot-cli-and-the-copilot-app)
- [EN] [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
- [EN] [Claude blog — Compliance API coverage for Cowork and Claude Code](https://claude.com/blog/compliance-api-cowork-and-claude-code)
- [EN] [LangChain blog — LangSmith BYOC generally available on AWS](https://www.langchain.com/blog/langsmith-byoc-is-now-generally-available-on-aws)
- [EN] [GitHub Changelog — Copilot memory and Ollama for JetBrains](https://github.blog/changelog/2026-08-11-copilot-memory-and-ollama-in-github-copilot-for-jetbrains)
- [EN] [Claude blog — Claude Tag now reads even more of the room](https://claude.com/blog/claude-tag-now-reads-even-more-of-the-room)
- [EN] [Google Blog — Introducing Gemini 3.7 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/)
- [EN] [Axios — Google's Gemini 3.7 Flash arrives before Gemini 3.5 Pro](https://www.axios.com/2026/08/13/google-gemini-37-flash)
- [EN] [TechCrunch — OpenAI introduces Ultrafast](https://techcrunch.com/2026/08/13/openai-introduces-ultrafast-a-new-mode-that-makes-gpt-5-6-sol-work-at-14x-the-speed/)
- [EN] [TechCrunch — OpenAI launches a new cyber model](https://techcrunch.com/2026/08/10/as-ai-led-attacks-multiply-openai-launches-a-new-cyber-model/)
- [EN] [TechCrunch — Anthropic says it will watermark text generated by its AI models](https://techcrunch.com/2026/08/11/anthropic-says-it-will-watermark-text-generated-by-its-ai-models/)
- [EN] [Fortune — Anthropic plans to add an invisible mark to AI text](https://fortune.com/2026/08/11/anthropic-claude-watermark-ai-text-police-ai-slop/)
- [EN] [Fortune — CIOs and CTOs are putting limits on how AI is used](https://fortune.com/2026/08/12/cios-and-ctos-spent-years-lauding-ai-now-with-costs-rising-theyre-putting-limits-on-how-its-used/)
- [EN] [GitHub — LongHorizon-Harness releases](https://github.com/AMAP-ML/LongHorizon-Harness/releases)
- [中文] [新浪科技 — DeepSeek Harness 预览版来了](https://finance.sina.com.cn/tech/roll/2026-08-13/doc-inineuqm9899462.shtml)
- [中文] [新浪财经 — DeepSeek V4 Pro 正式版发布](https://finance.sina.com.cn/roll/2026-08-13/doc-ininavwz3327589.shtml)
