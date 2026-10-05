# AI Newsletter — Agents Get Search, Routing, and a Review API

**Coverage:** 2026-09-29–2026-10-05 (Europe/Stockholm)

## Executive Brief

Cloudflare added search and model routing for agents, while GitHub opened Copilot code review to API requests.
Cloudflare 为智能体增加搜索和模型路由，GitHub 则开放 Copilot 代码审查 API。

Cloudflare also released post-trained decision models, but none of these releases verifies that generated firmware meets its requirements.
Cloudflare 还发布了后训练决策模型，但这些发布均未验证生成的固件符合需求。

## AI Tools

<a id="story-cloudflare-web-search-api"></a>

### Cloudflare adds web search through AI Gateway

- [ ] Interesting

**Event date:** 2026-10-02

**What happened**

On October 2, Cloudflare introduced web search through AI Gateway, REST calls, and Workers bindings.
10月2日，Cloudflare 通过 AI Gateway、REST 调用和 Workers 绑定推出网页搜索。

**Why it matters**

Agents can retrieve current source links instead of guessing URLs, but developers must check the retrieved content.
智能体可以检索最新来源链接，不必猜测网址，但开发者仍须核对检索内容。

**Embedded-code lens**

A firmware agent could retrieve a current SDK manual; engineers must check its revision and test the resulting code on hardware.
固件智能体可检索最新 SDK 手册；工程师仍须核对版本，并在硬件上测试生成代码。

**Sources:** [Cloudflare announcement](https://blog.cloudflare.com/introducing-web-search-api/)

<a id="story-cloudflare-auto-router"></a>

### Cloudflare puts an automatic model router in AI Gateway

- [ ] Interesting

**Event date:** 2026-09-30

**What happened**

On September 30, Cloudflare released Auto Router in public beta to select models based on task signals and estimated cost.
9月30日，Cloudflare 公测 Auto Router，按任务特征和预计成本选择模型。

**Why it matters**

The router addresses agent spending, but Cloudflare's internal task results do not prove quality on other workloads.
该路由器帮助控制智能体开支，但 Cloudflare 的内部任务结果不证明其他工作负载的质量。

**Embedded-code lens**

A team could route simple test drafts to cheaper models; it must still check generated tests against requirements and run them.
团队可将简单测试草稿交给低价模型；仍须按需求核对并运行测试。

**Sources:** [Cloudflare announcement](https://blog.cloudflare.com/auto-router/)

<a id="story-copilot-review-api"></a>

### GitHub opens Copilot code review to API requests

- [ ] Interesting

**Event date:** 2026-10-02

**What happened**

On October 2, GitHub enabled Copilot code review requests through supported REST and GraphQL APIs.
10月2日，GitHub 开放通过受支持的 REST 和 GraphQL API 请求 Copilot 代码审查。

**Why it matters**

Teams can start agent reviews inside existing workflows instead of relying on a manual request.
团队可在现有工作流中启动智能体审查，不必依赖手动请求。

**Embedded-code lens**

Firmware teams could add review to pull request checks; they still need compiler diagnostics, static analysis, and hardware tests.
固件团队可将审查加入拉取请求检查；仍须运行编译器诊断、静态分析和硬件测试。

**Sources:** [GitHub changelog](https://github.blog/changelog/2026-10-02-copilot-code-review-api-support-and-new-default-effort-level/)

<a id="story-cloudflare-ai-search-ga"></a>

### Cloudflare makes AI Search generally available

- [ ] Interesting

**Event date:** 2026-10-01

**What happened**

On October 1, Cloudflare made AI Search generally available with native image retrieval, scanned-PDF OCR, and larger files.
10月1日，Cloudflare 正式推出 AI Search，支持原生图像检索、扫描 PDF 文字识别和更大文件。

**Why it matters**

Agents can search mixed document collections, but retrieval does not establish that a cited document is authoritative.
智能体可搜索混合文档集合，但检索结果不能证明所引文档具有权威性。

**Embedded-code lens**

Teams could index scanned component manuals; engineers must compare extracted register details with approved datasheets.
团队可索引扫描的元件手册；工程师仍须用获批数据手册核对寄存器信息。

**Sources:** [Cloudflare announcement](https://blog.cloudflare.com/ai-search-ga/)

<a id="story-cloudflare-os-git"></a>

### Cloudflare OS adds work on existing Git repositories

- [ ] Interesting

**Event date:** 2026-10-01

**What happened**

On October 1, Cloudflare announced that Cloudflare OS agents can connect to existing GitHub repositories and open pull requests.
10月1日，Cloudflare 宣布 Cloudflare OS 智能体可连接现有 GitHub 仓库并创建拉取请求。

**Why it matters**

This adds a coding workflow to an existing agent workspace; fully managed deployments remain on a waitlist.
这为现有智能体工作区加入编程流程；全托管部署仍须等待候补资格。

**Embedded-code lens**

An agent could draft a driver change; maintainers must verify pin mappings, timing, and behavior on the target board.
智能体可草拟驱动更改；维护者仍须在目标板上验证引脚映射、时序和行为。

**Sources:** [Cloudflare announcement](https://blog.cloudflare.com/managed-cloudflare-os/)

<a id="story-cloudflare-monetization-gateway"></a>

### Cloudflare opens a payment gateway beta for agent tools

- [ ] Interesting

**Event date:** 2026-09-30

**What happened**

On September 30, Cloudflare opened a closed beta that lets eligible sellers charge agents for API and MCP calls.
9月30日，Cloudflare 开放封闭测试，让符合条件的卖家对智能体 API 和 MCP 调用收费。

**Why it matters**

HTTP 402 enables payment per request, but access is limited and agent operators still need spending controls.
HTTP 402 支持按请求付费，但接入受限，智能体运营者仍须控制支出。

**Sources:** [Cloudflare announcement](https://blog.cloudflare.com/monetization-gateway-beta/)

## Other AI Stories

<a id="story-cloudflare-clef-models"></a>

### Cloudflare releases Clef decision models and previews RL tuning

- [ ] Interesting

**Event date:** 2026-10-01

**What happened**

On October 1, Cloudflare released Clef and Clef-flash decision models, which use frozen Qwen bases and post-trained adapters.
10月1日，Cloudflare 发布 Clef 和 Clef-flash 决策模型，使用冻结的 Qwen 基座和后训练适配器。

**Why it matters**

The models return bounded choices for routing tasks; Cloudflare's benchmark results are not proof of safety-critical decisions.
这些模型为任务路由返回有界选项；Cloudflare 的基准测试结果不能证明安全关键决策可靠。

**Embedded-code lens**

A team could classify review findings for triage; engineers must independently inspect every safety-critical finding.
团队可将审查结果分类分流；工程师仍须独立检查每项安全关键结果。

**Sources:** [Cloudflare announcement](https://blog.cloudflare.com/clef-decision-models/)

<a id="story-openai-gpt-6-1-sol"></a>

### OpenAI updates Sol for coding at unchanged standard API rates

- [ ] Interesting

**Event date:** 2026-09-29

**What happened**

On September 29, OpenAI introduced GPT-6.1 Sol at $2 per million input tokens and $10 per million output tokens.
9月29日，OpenAI 推出 GPT-6.1 Sol，百万输入 token 价格为 2 美元，百万输出 token 为 10 美元。

**Why it matters**

Those standard rates match GPT-6 Sol, while the cached-input rate falls from $0.20 to $0.10 per million tokens.
其标准价格与 GPT-6 Sol 相同，但百万缓存输入 token 价格从 0.20 美元降至 0.10 美元。

**Embedded-code lens**

Teams could compare both models on driver tasks; neither price nor a general coding result verifies interrupt timing.
团队可在驱动任务中比较两款模型；价格或通用编程结果均不能验证中断时序。

**Sources:** [DevDay reporting](https://www.explainx.ai/blog/openai-dev-day-2026)

<a id="story-cloudflare-pay-per-use"></a>

### Cloudflare starts a paid-use beta for AI publishers

- [ ] Interesting

**Event date:** 2026-09-30

**What happened**

On September 30, Cloudflare opened Pay Per Use in beta for publisher-approved, buyer-reported uses of content.
9月30日，Cloudflare 公测 Pay Per Use，让出版者批准内容使用，并由买方报告用量。

**Why it matters**

The scheme ties payments to reported use rather than page access, but buyers report their own usage.
该方案按报告的使用量而非页面访问量付费，但使用量由买方自行报告。

**Sources:** [Cloudflare announcement](https://blog.cloudflare.com/pay-per-use/)

## Follow-ups to Interesting Stories

No qualifying follow-ups: there are no active interests.
没有符合条件的后续报道：目前没有有效关注标记。

## Tracked Interests

There are no active interests.
目前没有有效关注标记。

## Watch Next Week

Cloudflare plans to start AI Search billing on November 1; teams can test retrieval quality and estimate costs before then.
Cloudflare 计划于11月1日开始对 AI Search 收费；团队可提前测试检索质量并估算成本。

## Sources

- [EN] [Cloudflare: Web Search API](https://blog.cloudflare.com/introducing-web-search-api/)
- [EN] [Cloudflare: Auto Router](https://blog.cloudflare.com/auto-router/)
- [EN] [GitHub: Copilot code review API](https://github.blog/changelog/2026-10-02-copilot-code-review-api-support-and-new-default-effort-level/)
- [EN] [Cloudflare: AI Search GA](https://blog.cloudflare.com/ai-search-ga/)
- [EN] [Cloudflare: Cloudflare OS](https://blog.cloudflare.com/managed-cloudflare-os/)
- [EN] [Cloudflare: Monetization Gateway](https://blog.cloudflare.com/monetization-gateway-beta/)
- [EN] [Cloudflare: Clef](https://blog.cloudflare.com/clef-decision-models/)
- [EN] [Explainx: DevDay reporting](https://www.explainx.ai/blog/openai-dev-day-2026)
- [EN] [Cloudflare: Pay Per Use](https://blog.cloudflare.com/pay-per-use/)
