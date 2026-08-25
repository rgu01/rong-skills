"""Behaviour tests for the publication gate in newsletter_state.py.

These assert what the validator *does* with a synthetic edition, never how
SKILL.md happens to be worded.
"""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/ai/creating-ai-newsletters/scripts/newsletter_state.py"
SPEC = importlib.util.spec_from_file_location("newsletter_state", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"cannot load {SCRIPT}")
newsletter_state = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = newsletter_state
SPEC.loader.exec_module(newsletter_state)


AI_AT_WORK = """## AI at Work

<a id="story-acme-allows-agents"></a>

### Acme allows agents for its support team

- [ ] Interesting

**Stance:** Encouraging — Acme

**Underlying event date:** 2026-08-17

**What happened**

Acme let its support team use approved agents on 17 August 2026.
2026 年 8 月 17 日，Acme 允许支持团队使用已批准的 agent。

**Sources:** [Acme](https://example.com/acme)

"""


def build(
    *,
    brief: str = (
        "Agent tooling this week focused on control.\n"
        "本周的 agent 工具聚焦控制。\n"
    ),
    headline: str = "Anthropic makes Agent Skills generally available",
    title: str = "Agent Plumbing Gets Its Governance Layer",
    ai_at_work: str = "",
    sources: str = "- [EN] [Anthropic](https://claude.com/blog/agent-skills)\n",
) -> str:
    return f"""# {title}

**Coverage:** 2026-08-15–2026-08-21 (Europe/Stockholm)

## Executive Brief

{brief}
## AI Tools

<a id="story-agent-skills-ga"></a>

### {headline}

- [ ] Interesting

**Underlying event date:** 2026-08-19

**What happened**

Anthropic released Agent Skills on the Claude API on 19 August 2026.
2026 年 8 月 19 日，Anthropic 在 Claude API 上发布了 Agent Skills。

**Sources:** [Anthropic](https://claude.com/blog/agent-skills)

## Other AI Stories

<a id="story-glm-post-training"></a>

### 智谱发布 GLM-5.3

- [ ] Interesting

**事件日期：** 2026-08-18

**发生了什么**

智谱在 8 月 18 日发布了 GLM-5.3，基座模型未改变。

**来源：** [智谱](https://example.org/glm)

{ai_at_work}## Follow-ups to Interesting Stories

No qualifying update this week.

## Tracked Interests

- No active interests.

## Watch Next Week

Expect more vendors to gate MCP servers behind policy.
预计更多厂商会用策略来管控 MCP server。

## Sources

{sources}"""


class ReadabilityGateTests(unittest.TestCase):
    def validate(self, text: str, name: str = "2026-08-21-ai-newsletter.md"):
        with tempfile.TemporaryDirectory() as raw:
            path = Path(raw) / name
            path.write_text(text, encoding="utf-8")
            return newsletter_state.validate_edition(path)

    def assertRejects(self, text: str, fragment: str) -> None:
        result = self.validate(text)
        self.assertFalse(result["valid"], result["errors"])
        self.assertTrue(
            any(fragment in error for error in result["errors"]),
            f"expected {fragment!r} in {result['errors']}",
        )

    def test_compliant_edition_validates(self) -> None:
        result = self.validate(build())
        self.assertTrue(result["valid"], result["errors"])
        self.assertEqual(result["contract"], "current")

    def test_english_sentence_over_forty_words_is_rejected(self) -> None:
        long_sentence = "The vendor " + "shipped one more agent feature " * 9
        self.assertRejects(
            build(brief=f"{long_sentence.strip()}.\n供应商发布了功能。\n"),
            "English sentence runs",
        )

    def test_english_average_above_target_is_rejected(self) -> None:
        # Every sentence stays under the 40-word cap, but the average does not.
        sentence = " ".join(["vendors"] * 39)
        brief = ""
        for _ in range(20):
            brief += f"{sentence}.\n供应商发布了功能。\n\n"
        result = self.validate(build(brief=brief))
        self.assertFalse(result["valid"])
        self.assertTrue(
            any("average" in error for error in result["errors"]),
            result["errors"],
        )
        self.assertFalse(
            any("sentence runs" in error for error in result["errors"]),
            "no single sentence should breach the hard cap",
        )

    def test_chinese_sentence_over_sixty_characters_is_rejected(self) -> None:
        self.assertRejects(
            build(brief="The vendor shipped a feature.\n" + "供应商发布了一个功能" * 8 + "。\n"),
            "Chinese sentence runs",
        )

    def test_paragraph_over_six_sentences_is_rejected(self) -> None:
        self.assertRejects(
            build(brief="One. Two. Three. Four. Five. Six. Seven.\n"),
            "paragraph holds",
        )

    def test_translation_sentence_mismatch_is_rejected(self) -> None:
        self.assertRejects(
            build(brief="The vendor shipped. The rival replied.\n供应商发布了功能。\n"),
            "English sentences paired with",
        )

    def test_story_headline_obeys_the_word_cap(self) -> None:
        self.assertRejects(
            build(headline="Anthropic " + "ships another agent feature " * 12),
            "headline English sentence runs",
        )

    def test_h1_title_is_exempt(self) -> None:
        result = self.validate(build(title="Agent " + "plumbing metaphor " * 25))
        self.assertTrue(result["valid"], result["errors"])

    def test_sources_section_is_exempt(self) -> None:
        long_source = "- [EN] [" + "A very long source name " * 12 + "](https://e.com)\n"
        result = self.validate(build(sources=long_source))
        self.assertTrue(result["valid"], result["errors"])


class OptionalAiAtWorkTests(unittest.TestCase):
    def parse(self, text: str):
        with tempfile.TemporaryDirectory() as raw:
            path = Path(raw) / "2026-08-21-ai-newsletter.md"
            path.write_text(text, encoding="utf-8")
            return newsletter_state.parse_edition(path, date(2026, 8, 21))

    def test_edition_without_ai_at_work_is_current(self) -> None:
        parsed = self.parse(build())
        self.assertEqual(parsed.errors, [])
        self.assertEqual(parsed.contract, "current")

    def test_edition_with_ai_at_work_is_current(self) -> None:
        parsed = self.parse(build(ai_at_work=AI_AT_WORK))
        self.assertEqual(parsed.errors, [])
        self.assertEqual(parsed.contract, "current")

    def test_ai_at_work_out_of_order_is_rejected(self) -> None:
        text = build(ai_at_work=AI_AT_WORK)
        moved = text.replace(AI_AT_WORK, "")
        moved = moved.replace("## AI Tools\n", f"{AI_AT_WORK}## AI Tools\n", 1)
        parsed = self.parse(moved)
        self.assertTrue(
            any("story section order" in error for error in parsed.errors),
            parsed.errors,
        )


class AbsoluteExpiryTests(unittest.TestCase):
    def scan(self, today: date):
        with tempfile.TemporaryDirectory() as raw:
            archive = Path(raw)
            marked = build().replace("- [ ] Interesting", "- [x] Interesting", 1)
            (archive / "2026-08-21-ai-newsletter.md").write_text(
                marked, encoding="utf-8"
            )
            return newsletter_state.scan_archive(archive, today)

    def test_mark_stays_active_inside_one_calendar_month(self) -> None:
        result = self.scan(date(2026, 9, 20))
        self.assertEqual(len(result["interests"]), 1)
        self.assertEqual(result["expired"], [])

    def test_mark_expires_one_calendar_month_after_its_edition(self) -> None:
        result = self.scan(date(2026, 9, 22))
        self.assertEqual(result["interests"], [])
        self.assertEqual(len(result["expired"]), 1)
        self.assertTrue(result["expired"][0]["expired"])

    def test_archive_maintenance_ignores_readability(self) -> None:
        # Editions written before the caps existed must stay readable, or
        # cleanup would refuse to trash any of them.
        with tempfile.TemporaryDirectory() as raw:
            archive = Path(raw)
            sprawling = build(
                brief="The vendor " + "shipped one more agent feature " * 9 + ".\n"
                "供应商发布了功能。\n"
            )
            (archive / "2026-08-21-ai-newsletter.md").write_text(
                sprawling, encoding="utf-8"
            )
            result = newsletter_state.scan_archive(archive, date(2026, 8, 21))
        self.assertEqual(result["errors"], [])


if __name__ == "__main__":
    unittest.main()
