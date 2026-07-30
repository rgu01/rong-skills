from pathlib import Path
import unittest


ROOT = Path(__file__).parents[1]
README = ROOT / "README.md"


class FormalSpecsLiloReadmeTests(unittest.TestCase):
    def test_readme_lists_formal_specs_lilo_skill(self) -> None:
        text = README.read_text(encoding="utf-8")
        self.assertIn(
            "[`formal-specs-lilo`](skills/formal-specs-lilo/SKILL.md)",
            text,
        )
        self.assertIn("natural-language requirements", text)
        self.assertIn("Lilo", text)


if __name__ == "__main__":
    unittest.main()
