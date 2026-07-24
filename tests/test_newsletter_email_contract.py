from pathlib import Path
import unittest


SKILL = Path(__file__).parents[1] / "skills/creating-ai-newsletters/SKILL.md"


class NewsletterEmailContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = SKILL.read_text(encoding="utf-8")

    def test_default_recipient_and_subject_are_defined(self) -> None:
        self.assertIn("ronggufly@gmail.com", self.text)
        self.assertIn("AI Newsletter", self.text)

    def test_email_requires_validated_saved_markdown(self) -> None:
        email_section = self.text.split("## Email delivery", 1)[1]
        self.assertIn("validate", email_section)
        self.assertIn("complete saved Markdown", email_section)
        self.assertIn("after", email_section)

    def test_missing_connector_or_send_failure_is_reported_without_claiming_delivery(self) -> None:
        email_section = self.text.split("## Email delivery", 1)[1]
        self.assertIn("email connector", email_section)
        self.assertIn("not sent", email_section)
        self.assertIn("do not claim", email_section)


if __name__ == "__main__":
    unittest.main()
