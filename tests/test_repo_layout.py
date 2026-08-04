"""Pin the topic-grouped layout of skills/ and knowledge/.

The grouping is organizational, but several things depend on the exact depth:
the newsletter skill resolves the repo root by walking up from its own
directory, the README documents these paths, and the install snippet globs
`skills/*/*/`. A stray skill at the wrong depth breaks all three silently.
"""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
TOPICS = {"formal-methods", "ai", "engineering"}

EXPECTED_SKILLS = {
    "formal-methods": {"formal-specs-lilo", "uppaal"},
    "ai": {"creating-ai-newsletters", "qna"},
    "engineering": set(),
}


def _subdirs(path: Path) -> set[str]:
    return {p.name for p in path.iterdir() if p.is_dir()}


class SkillLayoutTests(unittest.TestCase):
    def test_skills_root_holds_only_topic_directories(self) -> None:
        self.assertEqual(TOPICS, _subdirs(ROOT / "skills"))

    def test_no_skill_sits_directly_under_skills_root(self) -> None:
        stray = sorted(p.name for p in (ROOT / "skills").glob("*/SKILL.md"))
        self.assertEqual([], stray, "skills must live at skills/<topic>/<name>/SKILL.md")

    def test_each_topic_holds_its_expected_skills(self) -> None:
        for topic, expected in EXPECTED_SKILLS.items():
            with self.subTest(topic=topic):
                self.assertEqual(expected, _subdirs(ROOT / "skills" / topic))

    def test_every_skill_has_a_skill_md_with_frontmatter(self) -> None:
        for topic in TOPICS:
            for skill in sorted((ROOT / "skills" / topic).iterdir()):
                if not skill.is_dir():
                    continue
                with self.subTest(skill=f"{topic}/{skill.name}"):
                    manifest = skill / "SKILL.md"
                    self.assertTrue(manifest.is_file(), f"{manifest} missing")
                    text = manifest.read_text(encoding="utf-8")
                    self.assertTrue(text.startswith("---\n"), "missing frontmatter")
                    self.assertIn(f"name: {skill.name}", text)
                    self.assertIn("description:", text)

    def test_empty_topics_are_tracked_by_a_placeholder(self) -> None:
        for topic, expected in EXPECTED_SKILLS.items():
            if expected:
                continue
            with self.subTest(topic=topic):
                self.assertTrue((ROOT / "skills" / topic / ".gitkeep").is_file())


class KnowledgeLayoutTests(unittest.TestCase):
    def test_knowledge_root_holds_only_topic_directories(self) -> None:
        self.assertEqual(TOPICS, _subdirs(ROOT / "knowledge"))

    def test_no_note_sits_directly_under_knowledge_root(self) -> None:
        stray = sorted(p.name for p in (ROOT / "knowledge").glob("*.md"))
        self.assertEqual([], stray, "notes must live at knowledge/<topic>/")

    def test_notes_are_filed_under_their_topic(self) -> None:
        expected = {
            "formal-methods": {
                "fret-concepts-and-fretish.md",
                "fret-cli-and-setup.md",
                "specforge-learning-notes.md",
            },
            "ai": {"llm-tokens-and-attention.md"},
        }
        for topic, notes in expected.items():
            with self.subTest(topic=topic):
                present = {p.name for p in (ROOT / "knowledge" / topic).glob("*.md")}
                self.assertEqual(notes, present)

    def test_newsletter_archive_lives_under_the_ai_topic(self) -> None:
        archive = ROOT / "knowledge" / "ai" / "AI-newsletter"
        self.assertTrue(archive.is_dir())
        self.assertTrue(
            sorted(archive.glob("*-ai-newsletter.md")),
            "archive should hold at least one dated edition",
        )


class DocumentedPathTests(unittest.TestCase):
    """The README and the newsletter skill must agree with the tree."""

    def test_readme_links_resolve(self) -> None:
        import re

        text = (ROOT / "README.md").read_text(encoding="utf-8")
        targets = re.findall(r"\]\((?!https?://)([^)#]+)", text)
        self.assertTrue(targets, "expected relative links in the README")
        for target in targets:
            with self.subTest(target=target):
                self.assertTrue((ROOT / target).exists(), f"broken README link: {target}")

    def test_newsletter_skill_declares_the_grouped_paths(self) -> None:
        skill = ROOT / "skills/ai/creating-ai-newsletters/SKILL.md"
        text = skill.read_text(encoding="utf-8")
        self.assertIn("knowledge/ai/AI-newsletter", text)
        self.assertIn("knowledge/ai/.AI-newsletter-trash", text)
        self.assertIn("skills/ai/creating-ai-newsletters/scripts/newsletter_state.py", text)

    def test_newsletter_skill_has_no_pre_grouping_paths(self) -> None:
        text = (ROOT / "skills/ai/creating-ai-newsletters/SKILL.md").read_text(
            encoding="utf-8"
        )
        for stale in (
            "$REPO_ROOT/knowledge/AI-newsletter",
            "$REPO_ROOT/skills/creating-ai-newsletters",
        ):
            with self.subTest(stale=stale):
                self.assertNotIn(stale, text)

    def test_repo_root_walk_up_from_the_skill_reaches_this_repo(self) -> None:
        """The depth the skill documents must actually land on the repo root."""
        skill_dir = ROOT / "skills/ai/creating-ai-newsletters"
        self.assertEqual(ROOT, skill_dir.parents[2])
        self.assertTrue((skill_dir.parents[2] / "knowledge").is_dir())


if __name__ == "__main__":
    unittest.main()
