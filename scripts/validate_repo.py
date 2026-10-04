#!/usr/bin/env python3
"""Check required repository files, local Markdown links, metadata, and CI shape."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "AGENTS.md",
    "README.md",
    "CHANGELOG.md",
    "VERSION",
    "docs/ai/INDEX.md",
    "docs/ai/CODE-MAP.md",
    "scripts/validate_repo.py",
    ".github/workflows/ci.yml",
)
HEADINGS = (
    "Purpose and navigation",
    "Repository map",
    "Change rules",
    "Verification",
    "Versioning and releases",
    "Completion",
)


def main() -> int:
    errors = [f"missing required file: {name}" for name in REQUIRED if not (ROOT / name).is_file()]
    if errors:
        return report(errors)

    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    for heading in HEADINGS:
        if f"## {heading}" not in agents:
            errors.append(f"AGENTS.md missing section: {heading}")

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
    if f"## {version}" not in changelog:
        errors.append(f"CHANGELOG.md has no section for VERSION {version}")

    workflow = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    for marker in ("name:", "on:", "pull_request:", "push:", "jobs:", "runs-on:", "python3 scripts/validate_repo.py"):
        if marker not in workflow:
            errors.append(f"CI workflow missing expected marker: {marker}")

    nested = [p for p in ROOT.rglob("AGENTS.md") if p != ROOT / "AGENTS.md" and ".git" not in p.parts]
    if nested:
        errors.append("unexpected nested AGENTS.md: " + ", ".join(str(p.relative_to(ROOT)) for p in nested))
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
