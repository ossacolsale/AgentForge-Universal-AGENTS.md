#!/usr/bin/env python3
"""Check required template files, local Markdown links, metadata, and CI wiring."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "AGENTS.md",
    "README.md",
    "CHANGELOG.md",
    "VERSION",
    "LICENSE",
    "docs/ai/INDEX.md",
    "docs/ai/CODE-MAP.md",
    "docs/ai/SESSION-STATE.md",
    "scripts/validate_repo.py",
    ".github/workflows/ci.yml",
)


def main() -> int:
    errors = [f"missing required file: {name}" for name in REQUIRED if not (ROOT / name).is_file()]
    if errors:
        return report(errors)

    # Check relative Markdown links, ignoring external URLs and anchor-only links.
    for markdown in ROOT.rglob("*.md"):
        if ".git" in markdown.parts:
            continue
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", markdown.read_text(encoding="utf-8")):
            target = target.split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            if not (markdown.parent / target).resolve().exists():
                errors.append(f"broken link in {markdown.relative_to(ROOT)}: {target}")

    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errors.append("VERSION must contain a semantic version (major.minor.patch)")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    if "## Unreleased" not in changelog:
        errors.append("CHANGELOG.md must include an Unreleased section")
    if f"## {version}" not in changelog:
        errors.append(f"CHANGELOG.md has no section for VERSION {version}")

    workflow = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    for trigger in ("push", "pull_request"):
        if not re.search(rf"(?m)^\s*{trigger}:\s*(?:#.*)?$", workflow):
            errors.append(f"CI workflow must run on {trigger}")
    if "python3 scripts/validate_repo.py" not in workflow:
        errors.append("CI workflow must run scripts/validate_repo.py")

    return report(errors)


def report(errors: list[str]) -> int:
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
