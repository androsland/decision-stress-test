#!/usr/bin/env python3
"""Validate the two platform packages remain behaviorally identical."""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


def split_skill(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", text, re.S)
    if not match:
        raise AssertionError(f"invalid frontmatter in {path}")
    return match.group(1), match.group(2)


class PackageTests(unittest.TestCase):
    def test_platform_bodies_match(self) -> None:
        _, codex_body = split_skill(ROOT / "SKILL.md")
        _, claude_body = split_skill(ROOT / "platforms" / "claude" / "SKILL.claude.md")
        self.assertEqual(codex_body, claude_body)

    def test_invocation_policies_are_explicit_only(self) -> None:
        codex_frontmatter, _ = split_skill(ROOT / "SKILL.md")
        claude_frontmatter, _ = split_skill(
            ROOT / "platforms" / "claude" / "SKILL.claude.md"
        )
        openai_config = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertNotIn("disable-model-invocation", codex_frontmatter)
        self.assertIn("disable-model-invocation: true", claude_frontmatter)
        self.assertIn("allow_implicit_invocation: false", openai_config)

    def test_no_unfinished_placeholders(self) -> None:
        for path in ROOT.rglob("*.md"):
            self.assertNotIn("[TODO", path.read_text(encoding="utf-8"), str(path))


if __name__ == "__main__":
    unittest.main()
