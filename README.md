# Decision Stress Test

An explicit-only agent skill for stress-testing consequential plans, decisions,
and ideas before implementation.

It maps unresolved decisions as a dependency tree, checks available evidence
before questioning the user, and asks only the current high-impact frontier. Each
question includes a recommended default, reasoning, confidence, and the downstream
choice it unlocks. The final output is a compact decision record.

## Why this version exists

This is an independent implementation inspired by Matt Pocock's
[grilling skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md).
It is not Ruben Hassid's privately distributed `grill-me` package.

This version deliberately:

- requires explicit invocation;
- avoids an arbitrary question count;
- investigates available facts before asking the user;
- focuses on consequential and hard-to-reverse choices;
- produces a decision record instead of silently starting implementation.

## Install

### Codex

Clone the repository into the user skill directory:

```powershell
git clone https://github.com/androsland/decision-stress-test.git "$HOME\.agents\skills\decision-stress-test"
```

Invoke it with `$decision-stress-test`.

### Claude Code

Place the skill in `~/.claude/skills/decision-stress-test`. To keep it manual-only,
either use Claude Code's `/skills` menu to hide it from Claude while keeping it
user-invocable (`user-invocable-only` in `skillOverrides`), or install
`platforms/claude/SKILL.claude.md` as the directory's `SKILL.md`.

Invoke it with `/decision-stress-test`.

## Intended coverage and limits

The workflow must serve unrelated consequential decisions such as selecting a
software architecture and deciding whether to launch or price a product. It must
not interrupt a routine, reversible task whose outcome and acceptance checks are
already clear.

It cannot observe stakeholder intent, private organizational constraints, or
external evidence that the user has not supplied and the agent cannot access.
Those remain explicit unknowns rather than guessed facts.

## License

MIT
