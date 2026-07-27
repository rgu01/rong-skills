from pathlib import Path
import unittest


ROOT = Path(__file__).parents[1]
SKILL = ROOT / "skills/creating-ai-newsletters/SKILL.md"
TEMPLATE = (
    ROOT
    / "skills/creating-ai-newsletters/references/newsletter-template.md"
)


class NewsletterContentContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.skill = SKILL.read_text(encoding="utf-8")
        cls.template = TEMPLATE.read_text(encoding="utf-8")

    def test_skill_prioritizes_agent_lifecycle_tools(self) -> None:
        for phrase in (
            "agent orchestration",
            "deployment",
            "observability",
            "evaluation",
            "governance",
            "MCP",
        ):
            self.assertIn(phrase, self.skill)

    def test_skill_requires_independent_story_counts(self) -> None:
        self.assertIn("five to seven AI Tools", self.skill)
        self.assertIn("three to five Other AI Stories", self.skill)
        self.assertIn("counts are independent", self.skill)

    def test_template_uses_tools_first_section_order(self) -> None:
        headings = [
            "## Executive Brief",
            "## AI Tools",
            "## Other AI Stories",
            "## Follow-ups to Interesting Stories",
            "## Tracked Interests",
            "## Watch Next Week",
            "## Sources",
        ]
        positions = [self.template.index(heading) for heading in headings]
        self.assertEqual(positions, sorted(positions))
        self.assertNotIn("## New Stories", self.template)

    def test_contract_forbids_cross_section_duplicates(self) -> None:
        self.assertIn(
            "same event in both `AI Tools` and `Other AI Stories`",
            self.template,
        )


if __name__ == "__main__":
    unittest.main()
