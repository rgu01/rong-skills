#!/usr/bin/env python3
"""Inspect and maintain Markdown editions created by creating-ai-newsletters."""

from __future__ import annotations

import argparse
import calendar
import json
import re
from dataclasses import asdict, dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Sequence


ACTIVE_NAME_RE = re.compile(r"^(?P<edition>\d{4}-\d{2}-\d{2})-ai-newsletter\.md$")
TRASH_NAME_RE = re.compile(
    r"^TRASHED-(?P<trash>\d{4}-\d{2}-\d{2})"
    r"--EDITION-(?P<edition>\d{4}-\d{2}-\d{2})-ai-newsletter\.md$"
)
ANCHOR_RE = re.compile(r'^<a id="(?P<anchor>[a-z0-9][a-z0-9-]*)"></a>$')
CHECKBOX_RE = re.compile(r"^- \[(?P<mark>[ xX])\] Interesting\s*$")
URL_RE = re.compile(r"\[[^\]]+\]\((https?://[^)\s]+)\)")
COMMON_REQUIRED_SECTIONS = (
    "Executive Brief",
    "Follow-ups to Interesting Stories",
    "Tracked Interests",
    "Watch Next Week",
    "Sources",
)
LEGACY_STORY_SECTIONS = ("New Stories",)
# `AI at Work` is optional: an edition omits the heading entirely when no
# organization changed its employee AI-use stance inside the window.
CURRENT_REQUIRED_STORY_SECTIONS = ("AI Tools", "Other AI Stories")
CURRENT_OPTIONAL_STORY_SECTIONS = ("AI at Work",)
CURRENT_STORY_SECTIONS = (
    *CURRENT_REQUIRED_STORY_SECTIONS,
    *CURRENT_OPTIONAL_STORY_SECTIONS,
)
KNOWN_STORY_SECTIONS = (*CURRENT_STORY_SECTIONS, *LEGACY_STORY_SECTIONS)

# A mark expires one calendar month after the edition that carried it,
# whatever the run frequency. Expiry is absolute: a qualifying follow-up
# reports the update but never restarts the clock.
INTEREST_EXPIRY_MONTHS = 1
# Unmarked editions move to recoverable trash after this many calendar months.
ARCHIVE_RETENTION_MONTHS = 6

# ASD-STE100 writing rules, with the sentence cap relaxed from the
# specification's ~25 descriptive words to 40.
MAX_ENGLISH_SENTENCE_WORDS = 40
MAX_ENGLISH_SENTENCE_AVERAGE = 25.0
MAX_CHINESE_SENTENCE_CHARS = 60
MAX_PARAGRAPH_SENTENCES = 6


@dataclass(frozen=True)
class Interest:
    edition_date: str
    headline: str
    anchor: str
    path: str
    relative_link: str
    story_text: str
    sources: list[str]
    expired: bool


@dataclass(frozen=True)
class Edition:
    path: Path
    edition_date: date
    interests: list[Interest]
    errors: list[str]
    contract: str = ""

    @property
    def active_interests(self) -> list[Interest]:
        return [item for item in self.interests if not item.expired]

    @property
    def expired_interests(self) -> list[Interest]:
        return [item for item in self.interests if item.expired]


def subtract_calendar_months(value: date, months: int) -> date:
    """Subtract calendar months, clamping the day to the destination month."""
    month_index = value.year * 12 + value.month - 1 - months
    year, zero_based_month = divmod(month_index, 12)
    month = zero_based_month + 1
    day = min(value.day, calendar.monthrange(year, month)[1])
    return date(year, month, day)


def _parse_active_name(path: Path) -> tuple[date | None, list[str]]:
    match = ACTIVE_NAME_RE.fullmatch(path.name)
    if not match:
        return None, [f"{path}: malformed newsletter filename"]
    try:
        return date.fromisoformat(match.group("edition")), []
    except ValueError:
        return None, [f"{path}: malformed newsletter filename"]


def _next_nonblank(lines: list[str], start: int) -> int | None:
    for index in range(start, len(lines)):
        if lines[index].strip():
            return index
    return None


def _previous_nonblank(lines: list[str], start: int) -> int | None:
    for index in range(start, -1, -1):
        if lines[index].strip():
            return index
    return None


def _section_bounds(
    lines: list[str], section_name: str
) -> tuple[int, int] | None:
    try:
        start = lines.index(f"## {section_name}") + 1
    except ValueError:
        return None
    end = len(lines)
    for index in range(start, len(lines)):
        if lines[index].startswith("## "):
            end = index
            break
    return start, end


def _story_section_contract(
    path: Path, lines: list[str]
) -> tuple[str, tuple[str, ...], list[str]]:
    present = {name for name in KNOWN_STORY_SECTIONS if f"## {name}" in lines}
    legacy_present = all(f"## {name}" in lines for name in LEGACY_STORY_SECTIONS)

    if legacy_present and present - set(LEGACY_STORY_SECTIONS):
        return "", (), [f"{path}: mixed story section contract"]
    if not present:
        return "", (), [f"{path}: missing story section contract"]
    if legacy_present:
        return "legacy", LEGACY_STORY_SECTIONS, []

    missing = [
        name for name in CURRENT_REQUIRED_STORY_SECTIONS if name not in present
    ]
    if missing:
        return (
            "",
            (),
            [f"{path}: missing required section: {name}" for name in missing],
        )

    sections = tuple(name for name in CURRENT_STORY_SECTIONS if name in present)
    positions = [lines.index(f"## {name}") for name in sections]
    if positions != sorted(positions):
        return "", (), [f"{path}: incorrect current story section order"]
    return "current", sections, []


def _parse_story_section(
    path: Path,
    edition_date: date,
    lines: list[str],
    today: date,
    section_name: str,
    anchors_seen: set[str],
) -> tuple[list[Interest], list[str]]:
    bounds = _section_bounds(lines, section_name)
    if bounds is None:
        return [], [f"{path}: missing required section: {section_name}"]

    start, end = bounds
    section = lines[start:end]
    headings = [
        index for index, line in enumerate(section) if line.startswith("### ")
    ]
    errors: list[str] = []
    interests: list[Interest] = []

    for heading_position, heading_index in enumerate(headings):
        headline = section[heading_index][4:].strip()
        anchor_index = _previous_nonblank(section, heading_index - 1)
        checkbox_index = _next_nonblank(section, heading_index + 1)
        anchor_match = (
            ANCHOR_RE.fullmatch(section[anchor_index])
            if anchor_index is not None
            else None
        )
        checkbox_match = (
            CHECKBOX_RE.fullmatch(section[checkbox_index])
            if checkbox_index is not None
            else None
        )

        if not headline or anchor_match is None or checkbox_match is None:
            errors.append(
                f"{path}: malformed checkbox/story association near "
                f"{headline or 'unnamed story'}"
            )
            continue

        anchor = anchor_match.group("anchor")
        if anchor in anchors_seen:
            errors.append(f"{path}: duplicate story anchor: {anchor}")
            continue
        anchors_seen.add(anchor)

        block_end = (
            headings[heading_position + 1]
            if heading_position + 1 < len(headings)
            else len(section)
        )
        block = "\n".join(section[heading_index:block_end])
        sources = list(dict.fromkeys(URL_RE.findall(block)))
        if checkbox_match.group("mark").lower() != "x":
            continue

        interests.append(
            Interest(
                edition_date=edition_date.isoformat(),
                headline=headline,
                anchor=anchor,
                path=str(path),
                relative_link=f"{path.name}#{anchor}",
                story_text=block,
                sources=sources,
                expired=edition_date
                < subtract_calendar_months(today, INTEREST_EXPIRY_MONTHS),
            )
        )

    orphan_checkboxes = [
        index
        for index, line in enumerate(section)
        if CHECKBOX_RE.fullmatch(line)
        and _previous_nonblank(section, index - 1) not in headings
    ]
    for _ in orphan_checkboxes:
        errors.append(f"{path}: malformed checkbox/story association")

    return interests, errors


def _parse_story_interests(
    path: Path,
    edition_date: date,
    lines: list[str],
    today: date,
) -> tuple[list[Interest], list[str], str]:
    contract, section_names, errors = _story_section_contract(path, lines)
    if errors:
        return [], errors, contract

    interests: list[Interest] = []
    anchors_seen: set[str] = set()
    for section_name in section_names:
        section_interests, section_errors = _parse_story_section(
            path,
            edition_date,
            lines,
            today,
            section_name,
            anchors_seen,
        )
        interests.extend(section_interests)
        errors.extend(section_errors)
    return interests, errors, contract


def parse_edition(path: Path, today: date) -> Edition:
    """Parse one active-edition file without following symlinks."""
    path = Path(path)
    edition_date, errors = _parse_active_name(path)
    if path.is_symlink():
        return Edition(
            path,
            edition_date or today,
            [],
            errors + [f"{path}: refusing newsletter symlink"],
        )
    if not path.is_file():
        return Edition(
            path,
            edition_date or today,
            [],
            errors + [f"{path}: newsletter is not a regular file"],
        )
    if edition_date is None:
        return Edition(path, today, [], errors)

    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        return Edition(path, edition_date, [], errors + [f"{path}: {exc}"])

    for section in COMMON_REQUIRED_SECTIONS:
        if f"## {section}" not in lines:
            errors.append(f"{path}: missing required section: {section}")

    interests, story_errors, contract = _parse_story_interests(
        path, edition_date, lines, today
    )
    return Edition(path, edition_date, interests, errors + story_errors, contract)


# --- Readability -----------------------------------------------------------
# These checks gate publication only. `parse_edition` stays free of them so
# archive maintenance keeps reading editions written before the rules existed.

CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
MD_LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
EMPHASIS_RE = re.compile(r"[*_]{1,3}")
LIST_MARKER_RE = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+")
ENGLISH_SENTENCE_RE = re.compile(r"(?<=[.!?])\s+(?=[\"'\u201c(\[]?[A-Z0-9])")
CHINESE_SENTENCE_RE = re.compile(r"(?<=[\u3002\uff01\uff1f])")
SKIPPED_PROSE_SECTIONS = ("Sources",)


def _is_chinese(text: str) -> bool:
    return bool(CJK_RE.search(text))


def _normalize_prose(line: str) -> str:
    text = MD_LINK_RE.sub(r"\1", line)
    text = INLINE_CODE_RE.sub(" ", text)
    text = LIST_MARKER_RE.sub("", text)
    text = EMPHASIS_RE.sub("", text)
    return text.strip()


def _split_sentences(text: str) -> list[str]:
    pattern = CHINESE_SENTENCE_RE if _is_chinese(text) else ENGLISH_SENTENCE_RE
    return [part.strip() for part in pattern.split(text) if part.strip()]


def _sentence_size(sentence: str) -> int:
    if _is_chinese(sentence):
        return len("".join(sentence.split()))
    return len(sentence.split())


def _excerpt(text: str, limit: int = 60) -> str:
    return text if len(text) <= limit else f"{text[:limit]}..."


def _measure(path: Path, label: str, text: str, english_words: list[int]) -> list[str]:
    """Check one prose line or headline, recording English sentence lengths."""
    errors: list[str] = []
    for sentence in _split_sentences(text):
        size = _sentence_size(sentence)
        if _is_chinese(sentence):
            if size > MAX_CHINESE_SENTENCE_CHARS:
                errors.append(
                    f"{path}: {label} Chinese sentence runs {size} characters "
                    f"(max {MAX_CHINESE_SENTENCE_CHARS}): {_excerpt(sentence)}"
                )
        else:
            english_words.append(size)
            if size > MAX_ENGLISH_SENTENCE_WORDS:
                errors.append(
                    f"{path}: {label} English sentence runs {size} words "
                    f"(max {MAX_ENGLISH_SENTENCE_WORDS}): {_excerpt(sentence)}"
                )
    return errors


def readability_errors(path: Path, lines: list[str]) -> list[str]:
    """Apply the sentence, paragraph, and translation-parity caps."""
    errors: list[str] = []
    english_words: list[int] = []
    paragraph: list[tuple[str, int]] = []
    section = ""
    fenced = False

    def flush() -> None:
        for language in dict.fromkeys(lang for lang, _ in paragraph):
            total = sum(n for lang, n in paragraph if lang == language)
            if total > MAX_PARAGRAPH_SENTENCES:
                errors.append(
                    f"{path}: paragraph holds {total} {language} sentences "
                    f"(max {MAX_PARAGRAPH_SENTENCES})"
                )
        for index in range(len(paragraph) - 1):
            language, count = paragraph[index]
            next_language, next_count = paragraph[index + 1]
            if language == "English" and next_language == "Chinese":
                if count != next_count:
                    errors.append(
                        f"{path}: {count} English sentences paired with "
                        f"{next_count} Chinese sentences"
                    )
        paragraph.clear()

    for raw in lines:
        line = raw.rstrip()
        if line.strip().startswith("```"):
            fenced = not fenced
            flush()
            continue
        if fenced:
            continue
        if line.startswith("## "):
            flush()
            section = line[3:].strip()
            continue
        if section in SKIPPED_PROSE_SECTIONS:
            continue
        if not line.strip():
            flush()
            continue
        if line.startswith("# "):
            continue
        if line.startswith("### "):
            flush()
            errors.extend(
                _measure(path, "headline", line[4:].strip(), english_words)
            )
            continue
        if (
            ANCHOR_RE.fullmatch(line)
            or CHECKBOX_RE.fullmatch(line)
            or line.lstrip().startswith(("|", ">", "<"))
        ):
            continue
        text = _normalize_prose(line)
        if not text:
            continue
        sentences = _split_sentences(text)
        errors.extend(_measure(path, "prose", text, english_words))
        paragraph.append(
            ("Chinese" if _is_chinese(text) else "English", len(sentences))
        )
    flush()

    if english_words:
        average = sum(english_words) / len(english_words)
        if average >= MAX_ENGLISH_SENTENCE_AVERAGE:
            errors.append(
                f"{path}: English sentences average {average:.1f} words "
                f"(target below {MAX_ENGLISH_SENTENCE_AVERAGE:.0f})"
            )
    return errors


def validate_edition(path: Path) -> dict[str, object]:
    path = Path(path)
    parsed = parse_edition(path, date.today())
    errors = list(parsed.errors)
    if path.is_file() and not path.is_symlink():
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeError):
            lines = []
        errors.extend(readability_errors(path, lines))
    return {
        "path": str(parsed.path),
        "valid": not errors,
        "contract": parsed.contract,
        "interests": [asdict(item) for item in parsed.active_interests],
        "expired": [asdict(item) for item in parsed.expired_interests],
        "errors": errors,
    }


def _looks_like_newsletter(path: Path) -> bool:
    return path.name.endswith(".md") and "newsletter" in path.name.lower()


def _prepare_directory(path: Path, label: str) -> list[str]:
    for component in (path, *path.parents):
        if component.is_symlink():
            return [
                f"{path}: refusing {label} directory symlink "
                f"component: {component}"
            ]
    if path.exists() and not path.is_dir():
        return [f"{path}: {label} path is not a directory"]
    try:
        path.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        return [f"{path}: cannot create {label} directory: {exc}"]
    for component in (path, *path.parents):
        if component.is_symlink():
            return [
                f"{path}: refusing {label} directory symlink "
                f"component: {component}"
            ]
    return []


def scan_archive(archive: Path, today: date) -> dict[str, object]:
    archive = Path(archive)
    directory_errors = _prepare_directory(archive, "archive")
    if directory_errors:
        return {"interests": [], "errors": directory_errors}
    interests: list[dict[str, object]] = []
    expired: list[dict[str, object]] = []
    errors: list[str] = []

    for path in sorted(archive.iterdir(), key=lambda item: item.name):
        if not _looks_like_newsletter(path):
            continue
        if not ACTIVE_NAME_RE.fullmatch(path.name):
            errors.append(f"{path}: malformed newsletter filename")
            continue
        parsed = parse_edition(path, today)
        interests.extend(asdict(item) for item in parsed.active_interests)
        expired.extend(asdict(item) for item in parsed.expired_interests)
        errors.extend(parsed.errors)

    return {"interests": interests, "expired": expired, "errors": errors}


def _unique(items: list[str]) -> list[str]:
    return list(dict.fromkeys(items))


def cleanup_archive(archive: Path, trash: Path, today: date) -> dict[str, object]:
    archive = Path(archive)
    trash = Path(trash)
    directory_errors = _prepare_directory(archive, "archive")
    directory_errors.extend(_prepare_directory(trash, "trash"))
    if directory_errors:
        return {
            "moved": [],
            "purged": [],
            "errors": _unique(directory_errors),
        }
    moved: list[str] = []
    purged: list[str] = []
    errors: list[str] = []
    expiry_boundary = subtract_calendar_months(today, ARCHIVE_RETENTION_MONTHS)
    purge_boundary = today - timedelta(days=30)

    for path in sorted(trash.iterdir(), key=lambda item: item.name):
        match = TRASH_NAME_RE.fullmatch(path.name)
        if match is None:
            if _looks_like_newsletter(path):
                errors.append(f"{path}: malformed newsletter trash filename")
            continue
        if path.is_symlink():
            errors.append(f"{path}: refusing newsletter trash symlink")
            continue
        if not path.is_file():
            errors.append(f"{path}: newsletter trash entry is not a regular file")
            continue
        try:
            trash_date = date.fromisoformat(match.group("trash"))
            date.fromisoformat(match.group("edition"))
        except ValueError:
            errors.append(f"{path}: malformed newsletter trash filename")
            continue
        if trash_date < purge_boundary:
            try:
                path.unlink()
            except OSError as exc:
                errors.append(f"{path}: cannot purge: {exc}")
            else:
                purged.append(str(path))

    for path in sorted(archive.iterdir(), key=lambda item: item.name):
        if not _looks_like_newsletter(path):
            continue
        if not ACTIVE_NAME_RE.fullmatch(path.name):
            errors.append(f"{path}: malformed newsletter filename")
            continue
        parsed = parse_edition(path, today)
        errors.extend(parsed.errors)
        # Expiry stops the research work, not the archiving: an edition that
        # carries any mark, active or expired, stays out of the trash.
        if parsed.errors or parsed.edition_date >= expiry_boundary or parsed.interests:
            continue
        destination = trash / (
            f"TRASHED-{today.isoformat()}--EDITION-"
            f"{parsed.edition_date.isoformat()}-ai-newsletter.md"
        )
        if destination.exists() or destination.is_symlink():
            errors.append(f"{destination}: trash destination already exists")
            continue
        try:
            path.replace(destination)
        except OSError as exc:
            errors.append(f"{path}: cannot move to trash: {exc}")
        else:
            moved.append(str(destination))

    return {"moved": moved, "purged": purged, "errors": _unique(errors)}


def prepare(archive: Path, trash: Path, today: date) -> dict[str, object]:
    cleanup = cleanup_archive(archive, trash, today)
    scan = scan_archive(archive, today)
    return {
        "moved": cleanup["moved"],
        "purged": cleanup["purged"],
        "interests": scan["interests"],
        "expired": scan["expired"],
        "errors": _unique(cleanup["errors"] + scan["errors"]),
    }


def _parse_date(value: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("date must use YYYY-MM-DD") from exc


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Inspect and maintain saved AI newsletter Markdown editions."
    )
    commands = parser.add_subparsers(dest="command", required=True)

    scan = commands.add_parser("scan", help="return active interests as JSON")
    scan.add_argument("--archive", type=Path, required=True)
    scan.add_argument("--today", type=_parse_date, default=date.today())

    cleanup = commands.add_parser("cleanup", help="apply safe retention rules")
    cleanup.add_argument("--archive", type=Path, required=True)
    cleanup.add_argument("--trash", type=Path, required=True)
    cleanup.add_argument("--today", type=_parse_date, default=date.today())

    prepare_parser = commands.add_parser(
        "prepare", help="clean up, then return active interests as JSON"
    )
    prepare_parser.add_argument("--archive", type=Path, required=True)
    prepare_parser.add_argument("--trash", type=Path, required=True)
    prepare_parser.add_argument("--today", type=_parse_date, default=date.today())

    validate = commands.add_parser(
        "validate", help="validate one saved newsletter edition"
    )
    validate.add_argument("file", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    if args.command == "scan":
        result = scan_archive(args.archive, args.today)
    elif args.command == "cleanup":
        result = cleanup_archive(args.archive, args.trash, args.today)
    elif args.command == "prepare":
        result = prepare(args.archive, args.trash, args.today)
    else:
        result = validate_edition(args.file)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
