#!/usr/bin/env python3
"""Validate template placeholders and the all-in-one bundle.

The placeholder registry parser intentionally supports only the small YAML
subset used by placeholders.yml:

- top-level placeholder keys ending with ":"
- two-space-indented scalar properties
- four-space-indented list items

Keep placeholders.yml in that shape, or replace load_registry() with a real
YAML parser before using more complex YAML features.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "placeholders.yml"
README_PATH = ROOT / "README.md"
PACK_DATE = "2026-03-21"
BUNDLE_FILENAME = f"claude_project_bootstrap_templates_{PACK_DATE}-all.md"
BUNDLE_PATH = ROOT / BUNDLE_FILENAME

PLACEHOLDER_RE = re.compile(r"\{\{([A-Z0-9_-]+)\}\}")

BUNDLE_FILES = [
    "README.md",
    "00-bootstrap-guide.md",
    "CLAUDE.md.template.md",
    "FEATURE_BRIEF.template.md",
    "docs/PROJECT_BRIEF.template.md",
    "docs/SKILL_ROUTING.template.md",
    "docs/QUALITY_GATES.template.md",
    "docs/TEST_STRATEGY.template.md",
    "docs/DECISION_LOG.template.md",
    "docs/HIDDEN_CONTRACT_REGISTER.template.md",
    "docs/CROSS_MODULE_CONSISTENCY_MATRIX.template.md",
    "docs/PROJECT_KICKOFF_CHECKLIST.template.md",
    ".claude/rules/backend-api.md.template.md",
    ".claude/rules/db-and-migrations.md.template.md",
    ".claude/rules/testing-and-release.md.template.md",
    ".claude/commands/project-kickoff.md.template.md",
    "placeholders.yml",
]


def _parse_scalar(raw: str):
    value = raw.strip()
    if value == "true":
        return True
    if value == "false":
        return False
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return value[1:-1]
    return value


def load_registry() -> dict[str, dict[str, object]]:
    registry: dict[str, dict[str, object]] = {}
    current_key: str | None = None
    current_list: str | None = None

    for line_number, line in enumerate(REGISTRY_PATH.read_text().splitlines(), start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        top_level = re.match(r"^([A-Z0-9_-]+):\s*$", line)
        if top_level:
            current_key = top_level.group(1)
            current_list = None
            registry[current_key] = {}
            continue

        property_line = re.match(r"^  ([a-z_]+):\s*(.*)$", line)
        if property_line and current_key:
            prop, raw_value = property_line.groups()
            if raw_value:
                registry[current_key][prop] = _parse_scalar(raw_value)
                current_list = None
            else:
                registry[current_key][prop] = []
                current_list = prop
            continue

        list_item = re.match(r"^    -\s*(.*)$", line)
        if list_item and current_key and current_list:
            registry[current_key][current_list].append(_parse_scalar(list_item.group(1)))
            continue

        raise ValueError(f"Unsupported placeholders.yml syntax at line {line_number}: {line}")

    return registry


def scan_files() -> list[Path]:
    files: list[Path] = []
    for path in sorted(ROOT.rglob("*")):
        rel = path.relative_to(ROOT)
        if not path.is_file():
            continue
        if ".git" in rel.parts:
            continue
        if rel.parts and rel.parts[0] == "scripts":
            continue
        if rel.name in {".DS_Store", "placeholders.yml"}:
            continue
        if path.suffix == ".md" or ".template" in path.name:
            files.append(path)
    return files


def collect_placeholders() -> dict[str, set[str]]:
    found: dict[str, set[str]] = {}
    for path in scan_files():
        rel = path.relative_to(ROOT).as_posix()
        for name in PLACEHOLDER_RE.findall(path.read_text()):
            found.setdefault(name, set()).add(rel)
    return found


def readme_placeholder_list() -> set[str]:
    text = README_PATH.read_text()
    match = re.search(
        r"^## 置換対象プレースホルダ\s*(?P<body>.*?)(?=^## |\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if not match:
        raise ValueError("README.md is missing the '置換対象プレースホルダ' section")
    return set(PLACEHOLDER_RE.findall(match.group("body")))


def generate_bundle() -> str:
    parts = [f"---\ngenerated: {PACK_DATE}\n---"]
    for rel_path in BUNDLE_FILES:
        path = ROOT / rel_path
        if not path.exists():
            raise FileNotFoundError(f"Bundle source is missing: {rel_path}")
        content = "\n".join(line.rstrip() for line in path.read_text().splitlines())
        parts.append(f"# FILE: {rel_path}\n\n{content.rstrip()}")
    return "\n\n---\n\n".join(parts) + "\n"


def validate(write_bundle: bool) -> int:
    errors: list[str] = []
    registry = load_registry()
    registry_keys = set(registry)

    for key, data in registry.items():
        if data.get("required") is True and not str(data.get("example", "")).strip():
            errors.append(f"{key}: required placeholder must define a non-empty example")
        if not str(data.get("description", "")).strip():
            errors.append(f"{key}: placeholder must define a description")

    found = collect_placeholders()
    found_keys = set(found)
    for key in sorted(found_keys - registry_keys):
        locations = ", ".join(sorted(found[key]))
        errors.append(f"{key}: placeholder is used but not registered in placeholders.yml ({locations})")

    readme_keys = readme_placeholder_list()
    for key in sorted(registry_keys - readme_keys):
        errors.append(f"{key}: registered in placeholders.yml but missing from README placeholder list")
    for key in sorted(readme_keys - registry_keys):
        errors.append(f"{key}: listed in README but missing from placeholders.yml")

    expected_bundle = generate_bundle()
    if write_bundle:
        BUNDLE_PATH.write_text(expected_bundle)
    elif BUNDLE_PATH.read_text() != expected_bundle:
        errors.append(
            f"{BUNDLE_PATH.name}: bundle is out of date; run "
            "python3 scripts/validate_templates.py --write-bundle"
        )

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("Template validation passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write-bundle",
        action="store_true",
        help="Regenerate claude_project_bootstrap_templates_2026-03-21-all.md",
    )
    args = parser.parse_args()
    return validate(write_bundle=args.write_bundle)


if __name__ == "__main__":
    raise SystemExit(main())
