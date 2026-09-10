# Repository instructions

- Keep the skill explicit-only on both Codex and Claude Code.
- Keep the instruction body in `SKILL.md` and `platforms/claude/SKILL.claude.md` identical; only supported platform frontmatter may differ.
- Do not add a fixed question count or make the skill trigger during ordinary planning.
- Preserve evidence-first questioning and the final decision record.
- Run `python tests/test_package.py` before proposing a change.
- Do not add AI attribution to commits, issues, pull requests, or releases.
