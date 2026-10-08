# Local LLM Agent on an 8 GB Laptop GPU

A study note recorded on 2026-10-08. It records which open-weight models and
which agent harnesses run as a local coding agent on one laptop, how fast they
run, and how well they do four fixed agent tasks. All measurements come from
2026-10-07 and 2026-10-08 on the hardware below.

---

## Hardware and sandbox

| Item | Value |
|---|---|
| CPU | Intel Core Ultra 7 255H, 16 threads |
| GPU | NVIDIA RTX PRO 2000 Blackwell Laptop GPU, 8 GB VRAM (8151 MiB), driver 596.58 |
| RAM | 32 GB on Windows. WSL2 gets 26 GB plus 8 GB swap through `.wslconfig`. |
| OS | Windows with WSL2, kernel 6.18.33.2-microsoft-standard-WSL2. A separate WSL distro, `own-llm` (Ubuntu 24.04), holds the whole test. |

Windows keeps about 1.1 GB of VRAM for the desktop, so about 7 GB is free for a
model.

The separate distro keeps the main Linux distro and Windows unchanged. It
shares the WSL kernel and the GPU passthrough. One command removes it:

```
wsl --unregister own-llm
```

### A WSL problem with a second systemd distro

All WSL2 distros share one kernel, and so they share one binfmt_misc table.
This table tells the kernel how to start a file type. One entry, `WSLInterop`,
starts Windows programs such as `wsl.exe`.

WSL powers off a distro about 15 s after its last process ends. In the
sandbox distro, each power-off removed every binfmt_misc entry, also the
entries of the main distro. After that, Windows programs failed in all
distros with `Exec format error`. All systemd units had already stopped when
the entries disappeared. The likely cause is the last stage of the systemd
shutdown, which removes all binfmt_misc entries. The journal ends before that
stage, so this cause is not confirmed.

When the sandbox distro starts, its `systemd-binfmt.service` also clears the
whole table before it registers its own entries.

Measures that kept the test running:

- Mask `systemd-binfmt.service` in the sandbox distro. The distro then does not
  clear the table when it starts.
- Keep one idle process, `sleep infinity`, running in the sandbox distro, so
  that WSL does not power it off.
- Turn off unattended upgrades in the sandbox distro. An upgrade restarted
  `systemd-binfmt` at 06:19 on 2026-10-08.

After the sandbox distro stops, this command in the main distro restores its
entries without a WSL restart. Run it in a normal terminal, because sudo needs
a terminal for the password:

```
sudo systemctl restart systemd-binfmt
```

---

## Serving stack: Ollama 0.40.0

Ollama runs as a systemd service inside the sandbox distro. It serves an
OpenAI-compatible API at `http://localhost:11434/v1` and an Anthropic-compatible
API at `http://localhost:11434`.

Server settings used for every test:

```
OLLAMA_CONTEXT_LENGTH=65536
OLLAMA_FLASH_ATTENTION=1
OLLAMA_KV_CACHE_TYPE=q8_0
```

Both harnesses need a context of 64k tokens or more. The Ollama default is 4k
when the GPU has less than 24 GiB of VRAM
([Ollama context length](https://docs.ollama.com/context-length)).

### Three settings that decide the speed

Without tuning, every model ran at 0.5 to 2 tokens per second. Three causes
explain this. Each fix goes into a per-model tag (a Modelfile), so the server
configuration does not change.

1. **CPU threads.** Ollama uses all 16 threads by default. On this CPU, 8
   threads are much faster for the part of a model that runs on the CPU. The
   14B model on the CPU alone gave 0.26 tokens per second with 16 threads and
   4.2 with 8 threads. Even the 9B model, fully on the GPU, gained 20%. Fix:
   `PARAMETER num_thread 8`.
2. **Automatic layer fit.** Ollama keeps 1 to 2 GB of VRAM free and puts the
   remaining layers on the CPU. For qwen3.5:9b, a hybrid model with recurrent
   layers, this split caused 164 CPU-GPU hops per step and 0.65 tokens per
   second. Fix: remove the vision projector, which text tasks do not need, and
   force all layers onto the GPU with `PARAMETER num_gpu 99`.
3. **The VRAM limit.** Forcing too many layers onto the GPU makes the driver
   spill into shared system memory. qwen3:14b with all 41 layers on the GPU
   used 7852 of 8151 MiB and fell to 2.3 tokens per second, with 697 s to read
   a 17k-token prompt. Keep the VRAM use below about 7.6 GB.

Mixture-of-experts models need no layer setting. Ollama 0.40 puts the attention
and shared layers on the GPU and the expert weights in system RAM by itself.

Example Modelfile for the 9B tag `qwen35-tuned:9b`. The `FROM` line names the
text-only copy of the weights:

```
FROM qwen3.5-text:9b
PARAMETER num_gpu 99
PARAMETER num_thread 8
PARAMETER num_ctx 65536
PARAMETER temperature 1
PARAMETER top_k 20
PARAMETER top_p 0.95
PARAMETER presence_penalty 1.5
```

A tag built `FROM` a published tag keeps that tag's sampling parameters. A tag
built `FROM` a raw weight file does not. The four sampling lines above copy the
values of the published `qwen3.5:9b` tag. Check every tuned tag with
`ollama show --modelfile <tag>`.

---

## Model speed

Test: about 490 prompt tokens and 300 output tokens, three runs averaged,
thinking off, temperature 0.2. The long-prompt test sends one prompt of 15.4k to 16.9k tokens,
which is about the size of the Claude Code system prompt.

| Tuned tag | Base model | Context | CPU / GPU | Output tokens/s | Long prompt read time | Output tokens/s after long prompt | VRAM MiB |
|---|---|---|---|---|---|---|---|
| `qwen35-tuned:9b` | qwen3.5:9b, text-only copy | 65536 | 0 / 100 | 44.3 | 10.8 s | 41.1 | 6454 |
| `qwen3-tuned:14b` | qwen3:14b | 40960 | 37 / 63 | 8.2 | 70.9 s | 3.3 | 7846 |
| `gptoss-tuned:20b` | gpt-oss:20b | 65536 | 62 / 38 | 22.6 | 23.5 s | 21.2 | 6140 |
| `qwen36-tuned:35b` | qwen3.6:35b-a3b-coding | 65536 | 80 / 20 | 29.2 | 88.1 s | 30.8 | 6394 |

Speed without tuning, for comparison:

| Model | Output tokens/s |
|---|---|
| qwen3.5:9b, automatic fit | 0.65 |
| qwen3:14b, automatic fit | 0.48 |
| gpt-oss:20b, 16 threads | 1.82 |
| qwen3.6:35b-a3b-coding, 16 threads | 1.94 |

Facts about each model:

- **qwen3.5:9b** has a native context of 256k tokens and supports tools and
  thinking. No published tag is text-only, so the text-only copy is built from
  the same model file. The hybrid layers make Ollama read the full prompt again
  when a request does not extend the cached prefix.
- **qwen3:14b** has a trained context of 40,960 tokens. Ollama 0.40 does not
  apply YaRN (a method that stretches the context), so it limits the model to
  40,960 tokens even when 65,536 is requested.
- **gpt-oss:20b** has 20.9B parameters in total and a trained context of 131k
  tokens. Its expert weights take 10.4 GB of system RAM.
- **qwen3.6:35b-a3b-coding** has 35.5B parameters with 3B active for each
  token, and a native context of 262k tokens. Its expert weights take 20.3 GB,
  which leaves little of the 26 GB WSL memory for other work. It writes fast
  but reads slowly, because the experts process the prompt on the CPU.

---

## Harnesses

Two harnesses were tested with the same models: Claude Code 2.1.292 and
OpenCode 1.18.35. Both run inside the sandbox distro.

| Item | Claude Code | OpenCode |
|---|---|---|
| Connection | `ANTHROPIC_BASE_URL=http://localhost:11434`, `ANTHROPIC_AUTH_TOKEN=ollama`, `ANTHROPIC_API_KEY=""` | Provider `@ai-sdk/openai-compatible` with `baseURL` `http://localhost:11434/v1` in `opencode.json` |
| Start with a model | `claude --model <tag>` | `opencode --model ollama/<tag>` |
| Switch model in a session | `/model <tag>`, then confirm. It also saves the tag as the default for new sessions. | `/models`, then pick the tag. No confirmation. |
| Headless run | `claude -p "<prompt>" --output-format stream-json --verbose --allowedTools "..."` | `opencode run --model ollama/<tag> --format json --auto "<prompt>"` |
| Second turn, headless | `claude -p --continue "<prompt>"` | `opencode run --continue "<prompt>"` |
| Skills | Loads `SKILL.md` folders from `~/.claude/skills/` and `.claude/skills/` | Loads them through a `skill` tool from `.opencode/skills/`, `.claude/skills/` and `.agents/skills/` |
| Instructions file | CLAUDE.md | AGENTS.md, or CLAUDE.md when no AGENTS.md exists |
| System prompt size | about 19,000 tokens | about 8,100 tokens |

Sources, read on 2026-10-07:
[Ollama and Claude Code](https://docs.ollama.com/integrations/claude-code),
[Claude Code model configuration](https://code.claude.com/docs/en/model-config),
[Claude Code headless mode](https://code.claude.com/docs/en/headless),
[Ollama Anthropic compatibility](https://docs.ollama.com/api/anthropic-compatibility),
[OpenCode providers](https://opencode.ai/docs/providers/),
[OpenCode CLI](https://opencode.ai/docs/cli/),
[OpenCode skills](https://opencode.ai/docs/skills/),
[OpenCode agents](https://opencode.ai/docs/agents/).

Anthropic does not support non-Claude models behind a gateway
([LLM gateway](https://code.claude.com/docs/en/llm-gateway)). Claude Code on a
local model works, but without vendor support.

### Settings each harness needs with a local model

**Claude Code: the context window.** Claude Code does not know local model
tags, so it assumes a window of 200k tokens. It then compacts the history too
late for a 64k model. Set the real window:

```
CLAUDE_CODE_MAX_CONTEXT_TOKENS=65536
```

**Claude Code: the permission mode.** The default mode, `auto`, sends a
safety-classifier request for each tool call to the same local model. In one
run this gave one HTTP 404 and one request cut off at exactly 60 s. The task
runs used `--permission-mode dontAsk` with a fixed tool list instead. In that
mode Claude Code allows the listed tools and refuses all others, with no
classifier.

**OpenCode: network contacts.** A traced OpenCode process (`strace` on its
connect and DNS calls) showed these outside contacts:

| Config and cache | Outside hosts |
|---|---|
| Default config | `models.opencode.ai` (model catalogue) at every start. `api.github.com`, likely the update check, at TUI start. |
| Privacy keys, empty cache | `models.opencode.ai` (catalogue), then `github.com` and `release-assets.githubusercontent.com` to download a `ripgrep` binary for the search tools. |
| Privacy keys, catalogue file `models.json` copied into `~/.cache/opencode`, `rg` on the PATH | none, in headless mode and in the TUI |

The privacy keys in `opencode.json`:

```json
"enabled_providers": ["ollama"],
"share": "disabled",
"autoupdate": false
```

The trace shows host names and times, not the content sent.

**OpenCode: the title agent.** OpenCode sends one hidden request in each
session to generate a session title. With a thinking model this request
produced 5,800 to 9,700 tokens and took 73 to 88% of the wall time. Turn it off
in `opencode.json`:

```json
"agent": { "title": { "disable": true } }
```

---

## Task results

Each model ran four fixed tasks in each harness on a clone of this repository
(commit 79a6e49). Every task ran headless, with a limit of 900 s per turn and
thinking at the model default.

| Task | What the model must do | Pass rule |
|---|---|---|
| T1 | Answer a question whose answer is in one paper summary under `knowledge/papers/`. | Correct answer, and the right file named. |
| T2 | Explain `knowledge/ai/llm-tokens-and-attention.md` with the `answer-better` skill, then answer "continue". | Turn 1 opens with a map of the parts, gives part 1 only, and ends with a checkpoint. The first acronym is spelled out. Turn 2 gives part 2 only and ends with a checkpoint. The content agrees with the note. |
| T3 | Answer a question that needs facts from `tests/test_repo_layout.py` and `README.md`. | Correct answer that names both files. |
| T4 | Add one test method to `tests/test_repo_layout.py` and run it. | The new test passes, and no other file or test changes. |

One test in the repository already failed before the runs. The T4 grader
accepts that failure and fails a run that edits it.

Settings for the runs on 2026-10-08: Claude Code with
`--permission-mode dontAsk`, the tool list Read, Grep, Glob, Edit, Write, Bash
and Skill, and `CLAUDE_CODE_MAX_CONTEXT_TOKENS=65536`. OpenCode with the title
agent turned off. No run had an HTTP 404, 500 or 499 error.

### Results of the larger models, one run per cell

Wall time in seconds. T2 adds both turns.

| Model | Harness | T1 | T2 | T3 | T4 |
|---|---|---|---|---|---|
| `gptoss-tuned:20b` | Claude Code | pass, 191 | fail, 259 | pass, 285 | fail, 900 (timeout) |
| `gptoss-tuned:20b` | OpenCode | pass, 43 | fail, 196 | pass, 35 | pass, 79 |
| `qwen36-tuned:35b` | Claude Code | pass, 219 | fail, 154 | pass, 122 | pass, 119 |
| `qwen36-tuned:35b` | OpenCode | pass, 91 | fail, 81 | pass, 34 | pass, 44 |

`qwen3-tuned:14b` had no task runs, because its output speed after a long
prompt (3.3 tokens per second) is below the speed floor of 8 tokens per
second.

### Results of the 9B model, three runs per cell

`qwen35-tuned:9b` ran three times in each cell. Each run takes under a minute,
so repeats were cheap. The table gives the passes out of three and the median
wall time in seconds.

| Harness | T1 | T2 | T3 | T4 |
|---|---|---|---|---|
| Claude Code | 3 of 3, 30 | 0 of 3, 54 | 0 of 3, 22 | 3 of 3, 35 |
| OpenCode | 2 of 3, 18 | 0 of 3, 43 | 1 of 3, 17 | 3 of 3, 20 |

- **Claude Code failed T3 in all three runs.** The model read only the test
  file and never `README.md`. It took a file pattern from a comment in the
  test file instead of the README.
- **OpenCode gave an empty answer in five turns.** With a long system prompt,
  the model writes its final answer without first closing its thinking block.
  Ollama then sends the whole answer in the `reasoning` field and leaves
  `content` empty, and OpenCode shows only `content`. Direct API requests with
  a long prompt reproduced this in 10 of 10 cases.
- **T4 passed in all six runs.**

The fix is to turn thinking off for this model in `opencode.json`. Ollama maps
`reasoning_effort: "none"` to thinking off
([Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)).
OpenCode passes the per-model option to the request
([OpenCode models](https://opencode.ai/docs/models/)):

```json
"qwen35-tuned:9b": { "options": { "reasoningEffort": "none" } }
```

OpenCode with thinking off, three runs per cell:

| Thinking | T1 | T2 | T3 | T4 | Empty answers |
|---|---|---|---|---|---|
| on | 2 of 3, 18 s | 0 of 3, 43 s | 1 of 3, 17 s | 3 of 3, 20 s | 5 turns |
| off | 3 of 3, 14 s | 0 of 3, 25 s | 2 of 3, 17 s | 3 of 3, 20 s | none |

### What the failures show

- **T2 failed in every run of every model.** No model spelled out the first
  acronym, "LLM", "LLMs" or "BPE", as the skill requires. The pacing rules of
  the skill held in most runs: a map, one part per turn, and a checkpoint after
  each turn. They held in all Claude Code runs and in the OpenCode runs of the
  35B model. They failed in the OpenCode runs of the 9B model, which gave no
  first-turn text, and in the OpenCode run of gpt-oss. gpt-oss did not load the
  skill. It wrote "We can just read the file" and gave the full explanation in
  each turn, with no checkpoint.
- **gpt-oss in Claude Code failed T4.** It sent the new test method with
  literal `\n` characters in the edit, which made the test file invalid
  Python. It then read and edited the file again until the 900 s limit.
- **Skill loading differs between the harnesses.** The skill sets
  `disable-model-invocation: true`, so the Claude Code prompt called it with
  `/answer-better`, and Claude Code put the skill text into the prompt. OpenCode loads a
  skill only when the model calls its `skill` tool. The two Qwen models called it, and gpt-oss did not.

### Harness speed

OpenCode finished faster than Claude Code in every pair of the same model
and task. The likely main cause is the size of the system prompt: about 8,100
tokens in OpenCode against about 19,000 in Claude Code. The difference is largest for the models
that read prompts slowly on the CPU. For `qwen36-tuned:35b`, T1 took 91 s in
OpenCode and 219 s in Claude Code.

---

## Recommended setup

No tested model passes all four tasks. The table counts the passes on T1, T3
and T4, the tasks that read files, combine facts and edit code.

| Model | Claude Code | OpenCode |
|---|---|---|
| `qwen36-tuned:35b` | 3 of 3 runs | 3 of 3 runs |
| `gptoss-tuned:20b` | 2 of 3 runs | 3 of 3 runs |
| `qwen35-tuned:9b` | 6 of 9 runs, thinking on | 8 of 9 runs, thinking off |

The recommended setup on this laptop:

- **Harness: OpenCode.** It was faster in every pair. Its system prompt is
  less than half the size of the Claude Code prompt. It loads the same
  `SKILL.md` folders. Turn off its title agent, set the three privacy keys,
  and copy `models.json` into its cache before the first start.
- **Main model: `qwen36-tuned:35b`.** It passed every T1, T3 and T4 run. It
  writes about 30 tokens per second. It needs 34 to 91 s per task in
  OpenCode, mostly to read the prompt. Its expert weights take about 20 GB of
  the 26 GB WSL memory.
- **Fast model: `qwen35-tuned:9b`, with thinking off in OpenCode.** It runs
  fully on the GPU at about 44 tokens per second and finishes T1, T3 and T4 in
  14 to 35 s. It is reliable
  for single-file questions and small edits (T1 and T4). It is not reliable
  when an answer needs a second file (T3). Switch to it with `/models` for
  quick work, as you switch from a large to a small hosted model.
- **Alternative: `gptoss-tuned:20b`.** It is the middle choice in speed. It
  broke the edit format once in Claude Code, and it did not load the skill in
  OpenCode.
- **Do not use the 14B dense class.** After a long prompt it writes 3.3 tokens
  per second on this GPU.

Claude Code also works with these models. Use it when its hooks, memory or
other Claude Code features matter more than speed. Anthropic does not support
it with non-Claude models.

These results have one run per cell for the two larger models. The skill test
shows that no model follows every rule of a skill. Check the output of an
instruction-heavy skill before you rely on it.

---

## Open items

| Item | What would settle it |
|---|---|
| A lower llama.cpp fit target (`LLAMA_ARG_FIT_TARGET`, server-wide) may put more expert weights on the GPU. | One speed run of each mixture-of-experts model with a lower target. |
| The source of the 60 s cut-off on the Anthropic endpoint in auto permission mode is not known. | A request longer than 60 s in auto mode, and the Ollama log of it. |
| One interactive Claude Code prompt took 7 min 48 s on qwen3.5:9b (more than 6,000 thinking tokens), while the same kind of prompt took seconds in headless mode. | The same prompt in interactive mode with thinking off. |
| The step that removes all binfmt_misc entries when a systemd distro powers off is not confirmed. | A boot log of the last shutdown stage, or the systemd source for the shutdown stage. |
| The two larger models have one run per cell. | Three runs of each cell for `qwen36-tuned:35b` and `gptoss-tuned:20b`. |
| A copied `models.json` may lack models that appear later. It is not known when OpenCode needs a newer catalogue. | One OpenCode start with a model that the copied catalogue does not list. |
