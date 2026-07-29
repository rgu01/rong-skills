from pathlib import Path
import unittest


ROOT = Path(__file__).parents[1]
SKILL = ROOT / "skills/qna/SKILL.md"


class QnaSkillContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.skill = SKILL.read_text(encoding="utf-8")

    def test_skill_names_when_a_sketch_helps(self) -> None:
        for concept in (
            "structure",
            "flow",
            "hierarchy",
            "spatial arrangement",
            "state changes",
            "relationships",
        ):
            self.assertIn(concept, self.skill)

    def test_skill_defaults_to_lightweight_text_sketches(self) -> None:
        self.assertIn("ASCII or Unicode", self.skill)
        self.assertIn("Mermaid", self.skill)
        self.assertIn("known to render it", self.skill)

    def test_skill_keeps_plain_explanations_in_prose(self) -> None:
        self.assertIn(
            "facts, definitions, and linear explanations",
            self.skill,
        )

    def test_skill_preserves_pacing_and_explains_the_sketch(self) -> None:
        self.assertIn("current chunk", self.skill)
        self.assertIn("Explain the sketch immediately", self.skill)


if __name__ == "__main__":
    unittest.main()
