# Coding models get cheaper, but firmware still needs proof

**Coverage:** 2026-09-22–2026-09-28 (Europe/Stockholm)

## Executive Brief

OpenAI and Anthropic released lower-cost coding models, while GitHub, Anthropic, and AWS expanded the tools around agent work.
OpenAI 和 Anthropic 发布成本更低的编码模型，GitHub、Anthropic 和 AWS 扩展了智能体工具。

MLPerf's new post-training benchmark checks software repairs, but it does not show that generated firmware satisfies a written requirement.
MLPerf 的新后训练基准测试检查软件修复，但不证明生成的固件符合书面需求。

## AI Tools

<a id="story-github-copilot-jetbrains-assisted-approvals"></a>

### GitHub Copilot adds assisted approvals and persistent MCP controls in JetBrains

- [ ] Interesting

**Underlying event date:** 2026-09-22

**What happened**

On September 22 GitHub released its JetBrains plugin 1.18.0 with assisted approvals, shared skills, plan mode, and persistent MCP tool controls.
9 月 22 日，GitHub 发布 JetBrains 插件 1.18.0，加入辅助审批、共享技能、计划模式和 MCP 工具控制。

Low-risk tool calls can receive automatic approval, while higher-risk actions still require a user decision.
低风险工具调用可以自动获批，高风险操作仍需用户决定。

**Why it matters**

The release reduces routine approval prompts without removing human control from actions that can change code or systems.
该版本减少常规审批提示，同时保留人类对代码或系统变更操作的控制。

**Embedded-code lens**

A firmware team could use approval rules before an agent edits a driver, then still compile and test the result on its target.
固件团队可在智能体修改驱动前设置审批规则，但仍须在目标设备上编译和测试结果。

**Sources:** [GitHub Changelog](https://github.blog/changelog/2026-09-22-new-features-and-improvements-in-copilot-for-jetbrains/)

<a id="story-claude-code-cloud-sessions-ga"></a>

### Claude Code cloud sessions reach general availability

- [ ] Interesting

**Underlying event date:** 2026-09-23

**What happened**

On September 23 Anthropic made Claude Code cloud sessions generally available on eligible paid plans.
9 月 23 日，Anthropic 向符合条件的付费版用户正式开放 Claude Code 云端会话。

Each task runs in an isolated environment, and users can run parallel sessions across connected GitHub repositories.
每项任务都在隔离环境中运行，用户可在已连接的 GitHub 仓库间并行启动会话。

**Why it matters**

Cloud sessions let teams delegate bounded coding work without keeping a developer terminal or local machine active.
云端会话让团队无需持续开启开发者终端或本地机器，也能委派边界明确的编码工作。

**Embedded-code lens**

Cloud coding could draft firmware tests, but a cloud sandbox alone cannot show that timing and interrupts behave correctly on the target board.
云端编码可起草固件测试，但仅靠云端沙箱无法证明目标板上的时序和中断行为正确。

**Sources:** [Claude by Anthropic](https://claude.com/blog/claude-code-on-the-web)

<a id="story-microsoft-copilot-managed-runtime-preview"></a>

### Microsoft previews a managed runtime for Copilot-built applications

- [ ] Interesting

**Underlying event date:** 2026-09-25

**What happened**

On September 25 Microsoft previewed Copilot Managed Runtime for hosting applications inside Microsoft 365.
9 月 25 日，Microsoft 预览 Copilot Managed Runtime，可在 Microsoft 365 中托管应用。

It supports apps built with Copilot Studio, and Microsoft plans to open it to third-party and professional developers.
它支持用 Copilot Studio 构建的应用，Microsoft 计划向第三方和专业开发者开放。

**Why it matters**

The preview offers a governed place to run agent-built business applications, rather than leaving each team to host its own.
该测试版为智能体构建的业务应用提供受治理的运行环境，团队无需各自托管。

**Embedded-code lens**

This is not a firmware runtime; use it for related internal workflows, not as evidence that generated C passes hardware tests.
这不是固件运行时；它可处理相关内部流程，但不能证明生成的 C 代码通过硬件测试。

**Sources:** [Microsoft](https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/)

<a id="story-cloudwatch-omni-agent-observability"></a>

### CloudWatch Omni unifies agent tracing, evaluation, and experiments

- [ ] Interesting

**Underlying event date:** 2026-09-22

**What happened**

On September 22 AWS launched CloudWatch Omni for agent observability, evaluation, experimentation, and prompt management.
9 月 22 日，AWS 发布 CloudWatch Omni，用于智能体可观测性、评估、实验和提示词管理。

It includes 17 evaluators, trace comparison, production datasets, and IDE support for VS Code and Kiro.
它包含 17 个评估器、链路对比、生产数据集，以及对 VS Code 和 Kiro 的 IDE 支持。

**Why it matters**

Teams can now test prompt and model changes against the same traces that operators inspect after deployment.
团队现在可以用运维人员部署后检查的同一批链路，测试提示词和模型变更。

**Embedded-code lens**

Agent traces can identify a bad tool choice during code generation, but they do not replace requirement-derived tests or static analysis.
智能体链路可找出生成代码时的错误工具选择，但不能替代需求驱动的测试或静态分析。

**Sources:** [AWS News Blog](https://aws.amazon.com/blogs/aws/introducing-amazon-cloudwatch-omni-ai-powered-observability-for-generative-ai-and-agentic-workloads/)

<a id="story-comet-opik-nebius-observability"></a>

### Comet brings Opik agent evaluation to Nebius AI Cloud

- [ ] Interesting

**Underlying event date:** 2026-09-24

**What happened**

On September 24 Comet listed a Nebius-optimized Opik build in Nebius AI Cloud Applications.
9 月 24 日，Comet 把针对 Nebius 优化的 Opik 上架到 Nebius AI Cloud Applications。

Opik records agent traces and intermediate steps, and it runs automated evaluation beside training and inference workloads.
Opik 记录智能体链路和中间步骤，并在训练与推理工作负载旁运行自动评估。

**Why it matters**

Opik helps teams compare agent versions and catch regressions before deployment, although this integration targets cloud workloads.
Opik 帮助团队比较智能体版本并在部署前发现回归，但该集成面向云工作负载。

**Embedded-code lens**

A firmware team could score coding-agent runs here, but it must still run its own compiler, property checks, and board tests.
固件团队可在这里评估编码智能体，但仍须运行自身的编译器、属性检查和板级测试。

**Sources:** [Comet](https://www.comet.com/site/blog/opik-nebius-partnership/)

## Other AI Stories

<a id="story-openai-gpt-6-sol-luna"></a>

### OpenAI introduces GPT-6 Sol and Luna

- [ ] Interesting

**Underlying event date:** 2026-09-22

**What happened**

On September 22 OpenAI released GPT-6 Sol for complex coding and GPT-6 Luna for high-volume, defined tasks.
9 月 22 日，OpenAI 发布面向复杂编码的 GPT-6 Sol，以及面向大量明确任务的 GPT-6 Luna。

OpenAI says both cost half as much through its API as their GPT-5.6 predecessors, and reports fewer coding errors for Sol.
OpenAI 称两款模型的 API 价格均为 GPT-5.6 前代的一半，并报告 Sol 的编码错误更少。

**Why it matters**

For engineering teams, cost per verified change matters more than the price of one model call.
对工程团队来说，每项通过验证的变更成本，比单次模型调用的价格更重要。

**Embedded-code lens**

Sol could draft C changes, but its reported coding gains do not establish that those changes meet timing, memory, or functional requirements.
Sol 可起草 C 代码变更，但其报告的编码进步不证明这些变更符合时序、内存或功能需求。

**Sources:** [TechCrunch](https://techcrunch.com/2026/09/22/openai-launches-gpt-6-sol-and-luna/)

<a id="story-anthropic-claude-opus-5-5"></a>

### Anthropic launches Claude Opus 5.5 for long coding tasks

- [ ] Interesting

**Underlying event date:** 2026-09-22

**What happened**

On September 22 Anthropic released Claude Opus 5.5 and said typical token-billed workloads cost about 40% less than Opus 5.
9 月 22 日，Anthropic 发布 Claude Opus 5.5，并称常见按 token 计费任务的成本较 Opus 5 低约 40%。

Anthropic reports stronger results on long coding tasks and a 60% lower price for cached reads.
Anthropic 报告了更好的长任务编码结果，并将缓存读取价格降低 60%。

**Why it matters**

Lower cached-context costs can matter when an agent repeatedly reads source files and requirements during a long code change.
智能体在长时间修改代码时会反复读取源码和需求，更低的缓存上下文成本可能更有价值。

**Embedded-code lens**

The reported tests cover general coding, not firmware conformance; compare models on a private, requirement-linked driver task with target tests.
报告测试的是通用编码而非固件符合性；应在有需求链接和目标测试的驱动任务上比较模型。

**Sources:** [Anthropic](https://www.anthropic.com/claude-opus-5-5) · [TechCrunch](https://techcrunch.com/2026/09/22/anthropic-releases-opus-5-5-with-lower-prices-and-fable-level-performance/)

<a id="story-mlperf-post-training-benchmark"></a>

### MLPerf adds its first LLM post-training benchmark

- [ ] Interesting

**Underlying event date:** 2026-09-24

**What happened**

On September 24 MLCommons announced an MLPerf benchmark for post-training coding agents with RLVR and GRPO.
9 月 24 日，MLCommons 宣布了一项 MLPerf 基准测试，用 RLVR 和 GRPO 后训练编码智能体。

The workload uses Qwen 3.5 397B, OpenHands, 700 training problems, and 251 separate validation problems.
该工作负载使用 Qwen 3.5 397B、OpenHands、700 个训练问题和 251 个独立验证问题。

**Why it matters**

A shared pass@4 target compares complete post-training systems, including the agent harness, instead of measuring throughput alone.
共享的 pass@4 目标比较包含智能体执行框架的完整后训练系统，而非只测吞吐量。

**Embedded-code lens**

Hidden repair tests resist reward hacking, but firmware needs properties traced back to requirements and tests on the target hardware.
隐藏的修复测试可抵御奖励投机，但固件还需要可追溯至需求的属性和目标硬件测试。

An August 6 study tested LLM translation of 15 written requirements into LTL; its 450 candidate formulas needed semantic evaluation.
一项 8 月 6 日的研究将 15 条书面需求转成 LTL；其生成的 450 条候选公式仍需语义评估。

A proposed firmware workflow would review each generated property against its requirement, check a system model, and test compiled code on hardware.
一种固件工作流是先核对生成的属性与需求，再检查系统模型，并在硬件上测试编译后的代码。

This study is background outside the coverage window, not a new release this week.
该研究是覆盖期外的背景资料，不是本周的新发布。

**Sources:** [MLCommons](https://mlcommons.org/2026/09/mlperf-training-llm-post-training/) · [arXiv background, 2026-08-06](https://arxiv.org/abs/2608.06287v1)

<a id="story-self-supervised-confidence-stopping"></a>

### Confidence training cuts reasoning tokens without a stopping rule

- [ ] Interesting

**Underlying event date:** 2026-09-25

**What happened**

On September 25 researchers submitted a study that trained models to predict intermediate answer confidence without a stopping objective.
9 月 25 日，研究人员提交研究，训练模型预测中途答案的置信度，但不设置停止目标。

They report up to 25% fewer generated tokens at matched accuracy on math, science, and coding tasks.
他们报告称，在数学、科学和编码任务中，相同准确率下生成的 token 最多减少 25%。

**Why it matters**

This points to another route to lower reasoning cost, though the paper does not test embedded software projects.
这提供了另一条降低推理成本的路径，但论文未测试嵌入式软件项目。

**Sources:** [arXiv](https://arxiv.org/abs/2609.31619)

## Follow-ups to Interesting Stories

No story carried an active mark into this window, so there is no follow-up.
本周期内没有仍在生效的标记故事，因此没有跟进内容。

## Tracked Interests

No interest mark is active. Tick `Interesting` under any story above to track it for one month.
当前没有生效的兴趣标记。在上面任意故事下勾选 `Interesting`，即可跟踪一个月。

## Watch Next Week

MLCommons plans its first submissions in October; compare their repair scores with requirement-linked tests before adopting a coding model for firmware.
MLCommons 计划在 10 月首次接收提交；为固件选编码模型前，还应对照需求驱动的测试。

## Sources

- [EN] [GitHub Changelog](https://github.blog/changelog/2026-09-22-new-features-and-improvements-in-copilot-for-jetbrains/)
- [EN] [Claude by Anthropic](https://claude.com/blog/claude-code-on-the-web)
- [EN] [Microsoft](https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/)
- [EN] [AWS News Blog](https://aws.amazon.com/blogs/aws/introducing-amazon-cloudwatch-omni-ai-powered-observability-for-generative-ai-and-agentic-workloads/)
- [EN] [Comet](https://www.comet.com/site/blog/opik-nebius-partnership/)
- [EN] [TechCrunch](https://techcrunch.com/2026/09/22/openai-launches-gpt-6-sol-and-luna/)
- [EN] [Anthropic](https://www.anthropic.com/claude-opus-5-5)
- [EN] [TechCrunch](https://techcrunch.com/2026/09/22/anthropic-releases-opus-5-5-with-lower-prices-and-fable-level-performance/)
- [EN] [MLCommons](https://mlcommons.org/2026/09/mlperf-training-llm-post-training/)
- [EN] [arXiv background, 2026-08-06](https://arxiv.org/abs/2608.06287v1)
- [EN] [arXiv](https://arxiv.org/abs/2609.31619)
