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
CURRENT_STORY_SECTIONS = ("AI Tools", "Other AI Stories")


@dataclass(frozen=True)
class Interest:
    edition_date: str
    headline: str
    anchor: str
    path: str
    relative_link: str
    story_text: str
    sources: list[str]
    overdue: bool


@dataclass(frozen=True)
class Edition:
    path: Path
    edition_date: date
    interests: list[Interest]
    errors: list[str]


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
) -> tuple[tuple[str, ...], list[str]]:
    legacy_present = all(f"## {name}" in lines for name in LEGACY_STORY_SECTIONS)
    current_present = [
        name for name in CURRENT_STORY_SECTIONS if f"## {name}" in lines
    ]

    if legacy_present and current_present:
        return (), [f"{path}: mixed story section contract"]
    if current_present and len(current_present) != len(CURRENT_STORY_SECTIONS):
        return (), [f"{path}: incomplete story section contract"]
    if legacy_present:
        return LEGACY_STORY_SECTIONS, []
    if len(current_present) == len(CURRENT_STORY_SECTIONS):
        positions = [lines.index(f"## {name}") for name in CURRENT_STORY_SECTIONS]
        if positions != sorted(positions):
            return (), [f"{path}: incorrect current story section order"]
        return CURRENT_STORY_SECTIONS, []
    return (), [f"{path}: missing story section contract"]


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
                overdue=edition_date < subtract_calendar_months(today, 6),
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
) -> tuple[list[Interest], list[str]]:
    section_names, errors = _story_section_contract(path, lines)
    if errors:
        return [], errors

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
    return interests, errors


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

    interests, story_errors = _parse_story_interests(
        path, edition_date, lines, today
    )
    return Edition(path, edition_date, interests, errors + story_errors)


def validate_edition(path: Path) -> dict[str, object]:
    parsed = parse_edition(Path(path), date.today())
    return {
        "path": str(parsed.path),
        "valid": not parsed.errors,
        "interests": [asdict(item) for item in parsed.interests],
        "errors": parsed.errors,
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
    errors: list[str] = []

    for path in sorted(archive.iterdir(), key=lambda item: item.name):
        if not _looks_like_newsletter(path):
            continue
        if not ACTIVE_NAME_RE.fullmatch(path.name):
            errors.append(f"{path}: malformed newsletter filename")
            continue
        parsed = parse_edition(path, today)
        interests.extend(asdict(item) for item in parsed.interests)
        errors.extend(parsed.errors)

    return {"interests": interests, "errors": errors}


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
    expiry_boundary = subtract_calendar_months(today, 6)
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
