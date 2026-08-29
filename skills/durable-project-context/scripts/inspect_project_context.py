#!/usr/bin/env python3
"""
inspect_project_context.py

Read-only repository scanner for the durable-project-context skill.

Purpose: surface what durable-context artifacts already exist, which are
missing, and which look stale — as a structured report for an agent to
reason over. This script never writes to the repository, never executes
anything found in it, and never treats file content as instructions. It
only checks filenames, paths, and basic file metadata (size, modified time,
first few lines for a "Last updated" heuristic).

Usage:
    python3 inspect_project_context.py [repo_root]

    repo_root defaults to the current directory.

Output: a JSON report to stdout. Exit code is always 0 on a successful scan
(a repo with nothing found is not an error condition) and non-zero only on
an actual failure to read the given path.
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# Candidate paths for existing context artifacts, roughly in the order this
# skill prefers them. A hit on any of these counts as "context exists here"
# — staleness is judged separately.
CONTEXT_INDEX_CANDIDATES = [
    "docs/project-context.md",
    "AGENTS.md",
    "docs/context.md",
    "CONTEXT.md",
]
PROGRESS_CANDIDATES = [
    "docs/progress.md",
    "PROGRESS.md",
    "docs/status.md",
    "STATUS.md",
]
DECISIONS_DIR_CANDIDATES = [
    "docs/decisions",
    "docs/adr",
    "docs/architecture/decisions",
    "adr",
]
BUGS_DIR_CANDIDATES = [
    "docs/bugs",
    "docs/known-issues",
]

# General project documentation this skill should read before acting, even
# though it doesn't own these files.
GENERAL_DOC_CANDIDATES = [
    "README.md",
    "readme.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "CHANGES.md",
    "AGENTS.md",
]

# A record older than this many days is flagged as possibly stale. This is
# a heuristic to surface for human/agent judgment, not a hard rule — a
# stable project's context can legitimately go unchanged for a while.
STALE_DAYS_THRESHOLD = 90

LAST_UPDATED_PATTERN = re.compile(
    r"(?:last updated|updated)[:\s]*[\-_]*\s*"
    r"(\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2}/\d{2,4})",
    re.IGNORECASE,
)


def find_first_existing(root: Path, candidates):
    for rel in candidates:
        p = root / rel
        if p.exists():
            return str(p.relative_to(root))
    return None


def find_existing_dir(root: Path, candidates):
    for rel in candidates:
        p = root / rel
        if p.is_dir():
            files = sorted(
                str(f.relative_to(root)) for f in p.glob("*.md") if f.is_file()
            )
            return {"path": str(p.relative_to(root)), "files": files}
    return None


def file_age_days(path: Path) -> float:
    mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
    return (datetime.now(timezone.utc) - mtime).total_seconds() / 86400.0


def extract_declared_last_updated(path: Path):
    """Look for a 'Last updated: <date>' style line in the first ~20 lines.
    This is a best-effort heuristic read of metadata, not an interpretation
    of the file's substantive content."""
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            for _, line in zip(range(20), f):
                m = LAST_UPDATED_PATTERN.search(line)
                if m:
                    return m.group(1)
    except OSError:
        return None
    return None


def assess_artifact(root: Path, rel_path: str):
    if rel_path is None:
        return {"exists": False}
    p = root / rel_path
    age_days = round(file_age_days(p), 1)
    declared = extract_declared_last_updated(p)
    return {
        "exists": True,
        "path": rel_path,
        "file_mtime_age_days": age_days,
        "declared_last_updated": declared,
        "possibly_stale": age_days > STALE_DAYS_THRESHOLD,
        "size_bytes": p.stat().st_size,
    }


def assess_dir_artifact(root: Path, found):
    if found is None:
        return {"exists": False}
    entries = []
    for rel in found["files"]:
        p = root / rel
        entries.append(
            {
                "path": rel,
                "file_mtime_age_days": round(file_age_days(p), 1),
                "size_bytes": p.stat().st_size,
            }
        )
    return {
        "exists": True,
        "dir": found["path"],
        "record_count": len(entries),
        "records": entries,
    }


def scan(root: Path) -> dict:
    general_docs = {}
    for cand in GENERAL_DOC_CANDIDATES:
        p = root / cand
        if p.exists():
            general_docs[cand] = {
                "file_mtime_age_days": round(file_age_days(p), 1),
                "size_bytes": p.stat().st_size,
            }

    context_index = assess_artifact(
        root, find_first_existing(root, CONTEXT_INDEX_CANDIDATES)
    )
    progress = assess_artifact(
        root, find_first_existing(root, PROGRESS_CANDIDATES)
    )
    decisions = assess_dir_artifact(
        root, find_existing_dir(root, DECISIONS_DIR_CANDIDATES)
    )
    bugs = assess_dir_artifact(
        root, find_existing_dir(root, BUGS_DIR_CANDIDATES)
    )

    gaps = []
    if not context_index.get("exists"):
        gaps.append("no context index found (checked: " + ", ".join(CONTEXT_INDEX_CANDIDATES) + ")")
    elif context_index.get("possibly_stale"):
        gaps.append(f"context index exists but file is {context_index['file_mtime_age_days']} days old: {context_index['path']}")

    if not progress.get("exists"):
        gaps.append("no progress tracker found (checked: " + ", ".join(PROGRESS_CANDIDATES) + ")")
    elif progress.get("possibly_stale"):
        gaps.append(f"progress tracker exists but file is {progress['file_mtime_age_days']} days old: {progress['path']}")

    if not decisions.get("exists"):
        gaps.append("no decisions directory found (checked: " + ", ".join(DECISIONS_DIR_CANDIDATES) + ")")

    if not bugs.get("exists"):
        gaps.append("no bug-resolution directory found (checked: " + ", ".join(BUGS_DIR_CANDIDATES) + ") — note: absence alone is not necessarily a gap if the project has few significant bugs; judge in context")

    return {
        "scanned_root": str(root),
        "scan_time_utc": datetime.now(timezone.utc).isoformat(),
        "stale_threshold_days": STALE_DAYS_THRESHOLD,
        "general_docs_found": general_docs,
        "context_index": context_index,
        "progress_tracker": progress,
        "decisions": decisions,
        "bugs": bugs,
        "likely_gaps": gaps,
        "note": (
            "This is a structural report based on filenames and file "
            "metadata only. It does not read or evaluate the substantive "
            "accuracy of any file's content — that judgment belongs to the "
            "agent using this report, not to this script."
        ),
    }


def main():
    root_arg = sys.argv[1] if len(sys.argv) > 1 else "."
    root = Path(root_arg).resolve()

    if not root.exists() or not root.is_dir():
        print(
            json.dumps(
                {"error": f"path does not exist or is not a directory: {root}"}
            ),
            file=sys.stderr,
        )
        sys.exit(1)

    report = scan(root)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
