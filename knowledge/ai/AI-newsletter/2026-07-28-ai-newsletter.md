# Agent Infrastructure Goes Stateless

**Coverage:** 2026-07-22–2026-07-28 (Europe/Stockholm)

## Executive Brief

Agent infrastructure moved toward stateless MCP deployments, stronger human approval, unified telemetry, and hardened sandboxes during the coverage window.
在本期报道窗口内，智能体基础设施朝着无状态 MCP 部署、更强的人工审批、统一遥测和强化沙箱方向发展。

Beyond tooling, the week brought a lower-cost frontier model, new rack-scale compute, context-aware AI eyewear, and a multibillion-dollar infrastructure partnership.
在工具之外，本周还出现了成本更低的前沿模型、新的机架级算力、具备情境感知能力的 AI 眼镜，以及一项数十亿美元规模的基础设施合作。

## AI Tools

<a id="story-cloudflare-agents-sdk-stateless-mcp"></a>

### Cloudflare Agents SDK adds stateless MCP support

- [ ] Interesting

**Underlying event date:** 2026-07-27

**What happened**

On July 27, Cloudflare released Agents SDK v0.20.0 with client and server support for the MCP 2026-07-28 release candidate, including stateless handlers, legacy fallback, multi-round-trip elicitation, and issuer-bound OAuth validation.
7 月 27 日，Cloudflare 发布 Agents SDK v0.20.0，加入对 MCP 2026-07-28 候选版本的客户端和服务器支持，包括无状态处理器、旧版回退、多轮往返信息征询，以及与签发方绑定的 OAuth 验证。

**Why it matters**

The release lets practitioners scale MCP servers without session storage while keeping one route compatible with newer and legacy clients.
该版本让实践者无需会话存储即可扩展 MCP 服务器，同时让同一路由兼容新版和旧版客户端。

**Sources:** [Cloudflare Changelog](https://developers.cloudflare.com/changelog/post/2026-07-27-agents-sdk-v0.20.0-mcp-sdk-v2/)

<a id="story-microsoft-project-perception"></a>

### Microsoft introduces Project Perception for agentic security

- [ ] Interesting

**Underlying event date:** 2026-07-27

**What happened**

On July 27, Microsoft introduced Project Perception, a multi-model security system that coordinates red-, blue-, and green-team agents and announced a public preview for August 3.
7 月 27 日，Microsoft 推出 Project Perception，这是一个协调红队、蓝队和绿队智能体的多模型安全系统，并宣布将于 8 月 3 日开启公开预览。

**Why it matters**

The system addresses continuous threat detection, investigation, and remediation while retaining human control over machine-speed defensive actions.
该系统面向持续威胁检测、调查与修复，同时让人类继续掌控以机器速度执行的防御操作。

**Sources:** [Official Microsoft Blog](https://blogs.microsoft.com/blog/2026/07/27/rethinking-security-for-the-age-of-ai/)

<a id="story-github-mcp-stateless-support"></a>

### GitHub MCP Server adopts the next stateless specification

- [ ] Interesting

**Underlying event date:** 2026-07-23

**What happened**

On July 23, GitHub updated its MCP Server ahead of the 2026-07-28 specification, removing Redis-backed protocol sessions, using required headers instead of payload inspection, and supporting multi-round-trip elicitation.
7 月 23 日，GitHub 在 2026-07-28 规范发布前更新了其 MCP Server，移除由 Redis 支撑的协议会话，改用必需请求头而非检查载荷，并支持多轮往返信息征询。

**Why it matters**

Stateless requests reduce deployment overhead and make remote MCP servers easier to scale, route, inspect, and verify.
无状态请求降低了部署开销，也让远程 MCP 服务器更易扩展、路由、检查和验证。

**Sources:** [GitHub Changelog](https://github.blog/changelog/2026-07-23-github-mcp-server-supports-the-next-mcp-specification/)

<a id="story-github-issues-agent-approvals"></a>

### GitHub Issues adds review controls for agent automation

- [ ] Interesting

**Underlying event date:** 2026-07-23

**What happened**

On July 23, GitHub placed rationale, confidence ratings, and optional approval queues for agent-driven issue changes into public preview.
7 月 23 日，GitHub 将智能体驱动的问题变更理由、置信度评级和可选审批队列推入公开预览。

**Why it matters**

Teams can automate triage and metadata changes while reviewing uncertain actions and retaining an audit trail, although GitHub cautions that approvals are not a server-side security boundary.
团队可以自动执行分类和元数据变更，同时审查不确定操作并保留审计轨迹，不过 GitHub 提醒审批并非服务器端安全边界。

**Sources:** [GitHub Changelog](https://github.blog/changelog/2026-07-23-agent-automation-controls-in-github-issues-in-public-preview/)

<a id="story-agentcore-unified-observability"></a>

### AWS unifies AgentCore traces and logs per agent

- [ ] Interesting

**Underlying event date:** 2026-07-23

**What happened**

On July 23, AWS announced that Amazon Bedrock AgentCore now sends an agent's traces, prompts, structured logs, and standard output to one per-agent CloudWatch log group.
7 月 23 日，AWS 宣布 Amazon Bedrock AgentCore 现可将智能体的追踪、提示词、结构化日志和标准输出发送到单个智能体专属的 CloudWatch 日志组。

**Why it matters**

Operators can correlate a complete execution history in one place and apply agent-specific IAM policies and customer-managed encryption keys.
运维人员可以在一个位置关联完整执行历史，并应用智能体专属的 IAM 策略和客户管理的加密密钥。

**Sources:** [AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-bedrock-agentcore-unified-observability-single-log-group/)

<a id="story-nvidia-nemoclaw-0092"></a>

### NVIDIA hardens NemoClaw sandboxes and headless deployment

- [ ] Interesting

**Underlying event date:** 2026-07-22

**What happened**

On July 22, NVIDIA released NemoClaw v0.0.92 with patched and integrity-pinned sandbox dependencies, a provider-neutral headless Linux workflow, and more diagnostic live end-to-end tests.
7 月 22 日，NVIDIA 发布 NemoClaw v0.0.92，带来已修补且锁定完整性校验的沙箱依赖、供应商中立的无头 Linux 工作流，以及诊断信息更丰富的实时端到端测试。

**Why it matters**

The update reduces supply-chain and deployment risk for operators running coding agents remotely while making stalls and failures easier to localize.
该更新降低了远程运行编码智能体时的供应链与部署风险，同时让卡顿和故障更容易定位。

**Sources:** [NVIDIA NemoClaw Release Notes](https://docs.nvidia.com/nemoclaw/user-guide/deepagents/release-notes/2026/7/22)

## Other AI Stories

<a id="story-anthropic-claude-opus-5"></a>

### Anthropic releases Claude Opus 5

- [ ] Interesting

**Underlying event date:** 2026-07-24

**What happened**

On July 24, Anthropic released Claude Opus 5 with adjustable effort, stronger coding and knowledge-work results, and the same price as Opus 4.8.
7 月 24 日，Anthropic 发布 Claude Opus 5，提供可调节推理投入、更强的编码与知识工作表现，并保持与 Opus 4.8 相同的价格。

**Why it matters**

Adjustable effort gives production teams a practical lever for balancing capability, latency, token use, and cost across long-running workloads.
可调节推理投入为生产团队在长时间运行的工作负载中平衡能力、延迟、词元用量和成本提供了实用杠杆。

**Sources:** [Anthropic](https://www.anthropic.com/news/claude-opus-5)

<a id="story-amd-helios-mi455x"></a>

### AMD launches Helios and its MI400 infrastructure portfolio

- [ ] Interesting

**Underlying event date:** 2026-07-23

**What happened**

On July 23, AMD launched its Helios rack-scale systems, MI400-series accelerators, sixth-generation EPYC processors, and new physical-AI platforms at Advancing AI 2026.
7 月 23 日，AMD 在 Advancing AI 2026 上推出 Helios 机架级系统、MI400 系列加速器、第六代 EPYC 处理器和新的物理 AI 平台。

**Why it matters**

The portfolio gives model builders and infrastructure buyers another open full-stack option spanning training, inference, enterprise systems, and robotics.
该产品组合为模型开发者和基础设施买家提供了另一种开放全栈选择，覆盖训练、推理、企业系统和机器人领域。

**Sources:** [AMD Investor Relations](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era)

<a id="story-samsung-intelligent-eyewear"></a>

### Samsung brings Gemini into everyday intelligent eyewear

- [ ] Interesting

**Underlying event date:** 2026-07-22

**What happened**

On July 22, Samsung introduced Android XR intelligent eyewear developed with Google, Gentle Monster, and Warby Parker, combining a camera, Gemini assistance, and context-aware hands-free interactions.
7 月 22 日，Samsung 推出与 Google、Gentle Monster 和 Warby Parker 联合开发的 Android XR 智能眼镜，结合摄像头、Gemini 助手和情境感知的免手操作交互。

**Why it matters**

The product moves multimodal assistance into an always-available wearable form, raising the practical importance of permissions, recording indicators, consent, and contextual privacy.
该产品将多模态辅助带入随时可用的可穿戴形态，使权限、录制指示、同意机制和情境隐私的实际重要性进一步上升。

**Sources:** [Samsung Newsroom U.K.](https://news.samsung.com/uk/samsung-brings-galaxy-ecosystem-into-everyday-eyewear)

<a id="story-amd-anthropic-partnership"></a>

### AMD commits up to $5 billion as Anthropic plans two gigawatts of Instinct GPUs

- [ ] Interesting

**Underlying event date:** 2026-07-22

**What happened**

On July 22, AMD and Anthropic announced a strategic partnership under which Anthropic plans to deploy up to two gigawatts of MI450-series GPUs and AMD committed up to $5 billion in strategic equity investment.
7 月 22 日，AMD 与 Anthropic 宣布战略合作：Anthropic 计划部署最高 2 吉瓦的 MI450 系列 GPU，AMD 则承诺进行最高 50 亿美元的战略股权投资。

**Why it matters**

The agreement couples a major frontier-lab compute commitment with joint ROCm optimization and gives AMD a larger role in supplying and financing the AI infrastructure market.
该协议将前沿实验室的大规模算力承诺与联合 ROCm 优化相结合，并让 AMD 在 AI 基础设施供应与融资市场中扮演更重要的角色。

**Sources:** [AMD 中国](https://www.amd.com/zh-cn/newsroom/press-releases/amd-anthropic-strategic-partnership.html)

## Follow-ups to Interesting Stories

No tracked story had a meaningful new event wholly inside the coverage window.
没有任何已追踪故事在本期报道窗口内发生完全符合条件的重大新事件。

## Tracked Interests

- **[NVIDIA releases Cosmos 3 Edge for local physical AI](2026-07-24-ai-newsletter.md#story-nvidia-cosmos-3-edge-siggraph)** — Marked 2026-07-24. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.
- **[OpenAI rolls out Health in ChatGPT to U.S. users](2026-07-27-ai-newsletter.md#story-chatgpt-health-rollout)** — Marked 2026-07-27. No qualifying update found this week. Uncheck `Interesting` in the original story to stop tracking it.

## Watch Next Week

Watch the August 3 public preview of Project Perception for evidence that its coordinated security agents preserve useful human control in operational workflows.
关注 Project Perception 于 8 月 3 日开启的公开预览，观察其协同安全智能体能否在实际工作流中保留有效的人类控制。

Watch how quickly operators adopt stateless MCP deployments as Cloudflare and GitHub expose migration paths that retain compatibility with legacy clients.
关注随着 Cloudflare 和 GitHub 提供兼容旧版客户端的迁移路径，运维人员采用无状态 MCP 部署的速度。

## Sources

- [EN] [Cloudflare Changelog](https://developers.cloudflare.com/changelog/post/2026-07-27-agents-sdk-v0.20.0-mcp-sdk-v2/)
- [EN] [Official Microsoft Blog](https://blogs.microsoft.com/blog/2026/07/27/rethinking-security-for-the-age-of-ai/)
- [EN] [GitHub Changelog — MCP Server](https://github.blog/changelog/2026-07-23-github-mcp-server-supports-the-next-mcp-specification/)
- [EN] [GitHub Changelog — Issues automation](https://github.blog/changelog/2026-07-23-agent-automation-controls-in-github-issues-in-public-preview/)
- [EN] [AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-bedrock-agentcore-unified-observability-single-log-group/)
- [EN] [NVIDIA NemoClaw Release Notes](https://docs.nvidia.com/nemoclaw/user-guide/deepagents/release-notes/2026/7/22)
- [EN] [Anthropic](https://www.anthropic.com/news/claude-opus-5)
- [EN] [AMD Investor Relations](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era)
- [EN] [Samsung Newsroom U.K.](https://news.samsung.com/uk/samsung-brings-galaxy-ecosystem-into-everyday-eyewear)
- [中文] [AMD 中国](https://www.amd.com/zh-cn/newsroom/press-releases/amd-anthropic-strategic-partnership.html)
