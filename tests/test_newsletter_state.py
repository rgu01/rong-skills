from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/creating-ai-newsletters/scripts/newsletter_state.py"
SPEC = importlib.util.spec_from_file_location("newsletter_state", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"cannot load {SCRIPT}")
newsletter_state = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = newsletter_state
SPEC.loader.exec_module(newsletter_state)


def edition(
    stories: list[tuple[str, str, bool, str]] | None = None,
    *,
    extra: str = "",
) -> str:
    stories = stories or [
        (
            "story-example-model-ships",
            "Example model ships",
            False,
            "https://example.com/release",
        )
    ]
    blocks = []
    for anchor, headline, checked, url in stories:
        mark = "x" if checked else " "
        blocks.append(
            f"""<a id="{anchor}"></a>

### {headline}

- [{mark}] Interesting

**Underlying event date:** 2026-07-23

**What happened**

The model shipped on 2026-07-23.
该模型于 2026-07-23 发布。

**Sources:** [Release]({url})
"""
        )
    return f"""# Weekly AI News

**Coverage:** 2026-07-18–2026-07-24 (Europe/Stockholm)

## Executive Brief

One concise sentence.
一句简短的话。

## New Stories

{"".join(blocks)}
{extra}
## Follow-ups to Interesting Stories

No qualifying follow-ups.

## Tracked Interests

No active interests.

## Watch Next Week

Watch releases.
关注发布。

## Sources

- [EN] [Release](https://example.com/release)
"""


class NewsletterStateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.archive = self.root / "knowledge/AI-newsletter"
        self.trash = self.root / "knowledge/.AI-newsletter-trash"
        self.archive.mkdir(parents=True)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def write_edition(
        self,
        edition_date: str,
        content: str,
    ) -> Path:
        path = self.archive / f"{edition_date}-ai-newsletter.md"
        path.write_text(content, encoding="utf-8")
        return path

    def test_scan_finds_checked_story_and_builds_relative_link(self) -> None:
        path = self.write_edition(
            "2025-12-01",
            edition(
                [
                    (
                        "story-example-model-ships",
                        "Example model ships",
                        True,
                        "https://example.com/release",
                    )
                ]
            ),
        )

        result = newsletter_state.scan_archive(self.archive, date(2026, 7, 24))

        self.assertEqual(result["errors"], [])
        self.assertEqual(result["interests"][0]["headline"], "Example model ships")
        self.assertEqual(
            result["interests"][0]["anchor"], "story-example-model-ships"
        )
        self.assertEqual(
            result["interests"][0]["sources"],
            ["https://example.com/release"],
        )
        self.assertIn(
            "The model shipped on 2026-07-23.",
            result["interests"][0]["story_text"],
        )
        self.assertEqual(
            result["interests"][0]["relative_link"],
            f"{path.name}#story-example-model-ships",
        )
        self.assertTrue(result["interests"][0]["overdue"])

    def test_scan_ignores_unchecked_and_accepts_uppercase_mark(self) -> None:
        self.write_edition(
            "2026-07-24",
            edition(
                [
                    ("story-one", "One", False, "https://example.com/one"),
                    ("story-two", "Two", True, "https://example.com/two"),
                ]
            ).replace("- [x] Interesting", "- [X] Interesting"),
        )

        result = newsletter_state.scan_archive(self.archive, date(2026, 7, 24))

        self.assertEqual([item["headline"] for item in result["interests"]], ["Two"])
        self.assertFalse(result["interests"][0]["overdue"])

    def test_checkbox_outside_new_stories_is_not_an_interest(self) -> None:
        content = edition().replace(
            "No qualifying follow-ups.",
            "### Old follow-up\n\n- [x] Interesting\n",
        )
        self.write_edition("2026-07-24", content)

        result = newsletter_state.scan_archive(self.archive, date(2026, 7, 24))

        self.assertEqual(result["interests"], [])

    def test_validate_reports_malformed_story_association(self) -> None:
        path = self.write_edition(
            "2026-07-24",
            edition().replace('<a id="story-example-model-ships"></a>\n\n', ""),
        )

        result = newsletter_state.validate_edition(path)

        self.assertTrue(
            any("malformed checkbox/story association" in item for item in result["errors"])
        )

    def test_scan_reports_malformed_filename_and_symlink(self) -> None:
        malformed = self.archive / "weekly-ai-newsletter.md"
        malformed.write_text(edition(), encoding="utf-8")
        target = self.root / "target.md"
        target.write_text(edition(), encoding="utf-8")
        link = self.archive / "2026-07-23-ai-newsletter.md"
        link.symlink_to(target)

        result = newsletter_state.scan_archive(self.archive, date(2026, 7, 24))

        self.assertEqual(len(result["errors"]), 2)
        self.assertTrue(any("malformed newsletter filename" in e for e in result["errors"]))
        self.assertTrue(any("symlink" in e for e in result["errors"]))

    def test_subtract_calendar_months_clamps_end_of_month(self) -> None:
        self.assertEqual(
            newsletter_state.subtract_calendar_months(date(2026, 8, 31), 6),
            date(2026, 2, 28),
        )

    def test_cleanup_moves_only_expired_unmarked_edition(self) -> None:
        old = self.write_edition("2026-01-23", edition())
        boundary = self.write_edition("2026-01-24", edition())
        recent = self.write_edition("2026-07-23", edition())

        result = newsletter_state.cleanup_archive(
            self.archive, self.trash, date(2026, 7, 24)
        )

        expected = (
            self.trash
            / "TRASHED-2026-07-24--EDITION-2026-01-23-ai-newsletter.md"
        )
        self.assertEqual(result["moved"], [str(expected)])
        self.assertFalse(old.exists())
        self.assertTrue(expected.exists())
        self.assertTrue(boundary.exists())
        self.assertTrue(recent.exists())

    def test_cleanup_preserves_expired_marked_edition(self) -> None:
        marked = self.write_edition(
            "2025-12-01",
            edition(
                [
                    (
                        "story-marked",
                        "Marked",
                        True,
                        "https://example.com/marked",
                    )
                ]
            ),
        )

        result = newsletter_state.cleanup_archive(
            self.archive, self.trash, date(2026, 7, 24)
        )

        self.assertEqual(result["moved"], [])
        self.assertTrue(marked.exists())

    def test_cleanup_purges_strictly_older_than_thirty_days(self) -> None:
        self.trash.mkdir()
        boundary = self.trash / (
            "TRASHED-2026-06-24--EDITION-2025-01-01-ai-newsletter.md"
        )
        expired = self.trash / (
            "TRASHED-2026-06-23--EDITION-2025-01-02-ai-newsletter.md"
        )
        boundary.write_text(edition(), encoding="utf-8")
        expired.write_text(edition(), encoding="utf-8")

        result = newsletter_state.cleanup_archive(
            self.archive, self.trash, date(2026, 7, 24)
        )

        self.assertEqual(result["purged"], [str(expired)])
        self.assertTrue(boundary.exists())
        self.assertFalse(expired.exists())

    def test_cleanup_preserves_unrelated_malformed_and_symlink_files(self) -> None:
        unrelated = self.archive / "notes.md"
        unrelated.write_text("keep", encoding="utf-8")
        malformed = self.archive / "newsletter.md"
        malformed.write_text(edition(), encoding="utf-8")
        target = self.root / "target.md"
        target.write_text(edition(), encoding="utf-8")
        link = self.archive / "2025-01-01-ai-newsletter.md"
        link.symlink_to(target)

        result = newsletter_state.cleanup_archive(
            self.archive, self.trash, date(2026, 7, 24)
        )

        self.assertTrue(unrelated.exists())
        self.assertTrue(malformed.exists())
        self.assertTrue(link.is_symlink())
        self.assertTrue(result["errors"])

    def test_cleanup_refuses_destination_collision(self) -> None:
        old = self.write_edition("2025-01-01", edition())
        self.trash.mkdir()
        destination = self.trash / (
            "TRASHED-2026-07-24--EDITION-2025-01-01-ai-newsletter.md"
        )
        destination.write_text("existing", encoding="utf-8")

        result = newsletter_state.cleanup_archive(
            self.archive, self.trash, date(2026, 7, 24)
        )

        self.assertTrue(old.exists())
        self.assertEqual(destination.read_text(encoding="utf-8"), "existing")
        self.assertTrue(any("already exists" in e for e in result["errors"]))

    def test_cleanup_refuses_symlinked_archive_root(self) -> None:
        external = self.root / "external-archive"
        external.mkdir()
        old = external / "2025-01-01-ai-newsletter.md"
        old.write_text(edition(), encoding="utf-8")
        archive_link = self.root / "archive-link"
        archive_link.symlink_to(external, target_is_directory=True)

        result = newsletter_state.cleanup_archive(
            archive_link, self.trash, date(2026, 7, 24)
        )

        self.assertTrue(old.exists())
        self.assertEqual(result["moved"], [])
        self.assertTrue(any("archive directory symlink" in e for e in result["errors"]))

    def test_cleanup_refuses_symlinked_trash_root(self) -> None:
        external = self.root / "external-trash"
        external.mkdir()
        old_trash = external / (
            "TRASHED-2026-01-01--EDITION-2025-01-01-ai-newsletter.md"
        )
        old_trash.write_text(edition(), encoding="utf-8")
        trash_link = self.root / "trash-link"
        trash_link.symlink_to(external, target_is_directory=True)

        result = newsletter_state.cleanup_archive(
            self.archive, trash_link, date(2026, 7, 24)
        )

        self.assertTrue(old_trash.exists())
        self.assertEqual(result["purged"], [])
        self.assertTrue(any("trash directory symlink" in e for e in result["errors"]))

    def test_prepare_creates_directories_and_returns_post_cleanup_interests(self) -> None:
        archive = self.root / "new/archive"
        trash = self.root / "new/trash"

        result = newsletter_state.prepare(archive, trash, date(2026, 7, 24))

        self.assertTrue(archive.is_dir())
        self.assertTrue(trash.is_dir())
        self.assertEqual(
            result,
            {"moved": [], "purged": [], "interests": [], "errors": []},
        )

    def test_cli_scan_prints_json(self) -> None:
        self.write_edition("2026-07-24", edition())

        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "scan",
                "--archive",
                str(self.archive),
                "--today",
                "2026-07-24",
            ],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(completed.returncode, 0)
        self.assertEqual(json.loads(completed.stdout)["interests"], [])

    def test_cli_prepare_returns_nonzero_for_malformed_archive(self) -> None:
        (self.archive / "bad-ai-newsletter.md").write_text(
            edition(), encoding="utf-8"
        )

        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "prepare",
                "--archive",
                str(self.archive),
                "--trash",
                str(self.trash),
                "--today",
                "2026-07-24",
            ],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertNotEqual(completed.returncode, 0)
        self.assertTrue(json.loads(completed.stdout)["errors"])

    @unittest.skipUnless(hasattr(os, "symlink"), "symlinks unsupported")
    def test_validate_rejects_symlink(self) -> None:
        target = self.root / "target.md"
        target.write_text(edition(), encoding="utf-8")
        link = self.archive / "2026-07-24-ai-newsletter.md"
        link.symlink_to(target)

        result = newsletter_state.validate_edition(link)

        self.assertTrue(any("symlink" in e for e in result["errors"]))


if __name__ == "__main__":
    unittest.main()
