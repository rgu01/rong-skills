from pathlib import Path
import unittest


ROOT = Path(__file__).parents[1]
SKILL = ROOT / "skills/ai/creating-ai-newsletters/SKILL.md"
TEMPLATE = (
    ROOT
    / "skills/ai/creating-ai-newsletters/references/newsletter-template.md"
)
EMPLOYER_WATCH = (
    ROOT / "skills/ai/creating-ai-newsletters/references/employer-watch.md"
)
WATCH_DIR = "knowledge/ai/.employer-watch"


class NewsletterContentContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.skill = SKILL.read_text(encoding="utf-8")
        cls.template = TEMPLATE.read_text(encoding="utf-8")

    def test_skill_prioritizes_coding_and_pipeline_tools(self) -> None:
        flat = " ".join(self.skill.split())
        for phrase in (
            "coding agents",
            "CI/CD",
            "code review",
            "test generation",
            "sandboxes",
            "supply-chain",
            "General agent infrastructure without a direct coding or "
            "pipeline use does not qualify",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, flat)
        self.assertNotIn("blog.cloudflare.com", self.skill)

    def test_skill_requires_independent_story_counts(self) -> None:
        self.assertIn("five to seven AI Tools", self.skill)
        self.assertIn("three to five Other AI Stories", self.skill)
        self.assertIn("counts are independent", self.skill)

    def test_template_uses_tools_first_section_order(self) -> None:
        headings = [
            "## Executive Brief",
            "## AI Tools",
            "## Correctness and Formal Methods",
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
        self.assertIn("same event in more than one of", self.template)

    def test_employer_watch_is_documented_as_local_only(self) -> None:
        self.assertTrue(EMPLOYER_WATCH.is_file(), f"{EMPLOYER_WATCH} missing")
        self.assertIn(WATCH_DIR, self.skill)
        self.assertIn("references/employer-watch.md", self.skill)
        self.assertIn("never reaches the committed edition", self.skill)

    def test_employer_watch_directory_is_gitignored(self) -> None:
        """AGENTS.md forbids employer information in this repository, so the
        watchlist and its editions must never become committable."""
        ignored = (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()
        self.assertIn(f"{WATCH_DIR}/", [line.strip() for line in ignored])

    def test_employer_watch_never_enters_a_published_section(self) -> None:
        watch = EMPLOYER_WATCH.read_text(encoding="utf-8")
        self.assertIn("not a standing topic", watch)
        self.assertIn("Leakage guard", watch)
        for section in (
            "## AI Tools",
            "## Correctness and Formal Methods",
            "## Other AI Stories",
            "## AI at Work",
        ):
            with self.subTest(section=section):
                self.assertNotIn(section, watch)


if __name__ == "__main__":
    unittest.main()
