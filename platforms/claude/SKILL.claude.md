---
name: decision-stress-test
description: Stress-test a consequential plan, decision, or idea through explicit, evidence-led questioning before implementation. Use only when the user invokes this skill directly; do not use for ordinary planning, brainstorming, architecture review, or specification work.
disable-model-invocation: true
argument-hint: "[plan, decision, or idea]"
---

# Decision Stress Test

Expose the decisions, assumptions, and failure modes that could materially change the outcome. This is an explicit deliberation workflow, not a generic planning step.

## Boundaries

- The user's instructions and chosen scope take precedence.
- Do not implement, edit files, send messages, or make external changes during the stress test unless the user separately requests that work.
- Do not force a fixed question count. Stop when the consequential frontier is resolved or the user says to stop.
- Do not ask for facts available from the repository, tools, or supplied material. Check those first and state what was actually verified.
- Distinguish factual unknowns from preferences and decisions that only the user can make.
- Skip trivial, easily reversible choices unless they affect a downstream irreversible decision.

## Workflow

1. Restate the decision in one sentence and name the success criterion.
2. Inspect available evidence before questioning. Record material facts, constraints, and non-goals without treating examples as universal requirements.
3. Map the decision tree internally:
   - desired outcome and affected users;
   - irreversible or expensive choices;
   - viable alternatives and trade-offs;
   - dependencies and assumptions;
   - failure modes, detection, rollback, and exit conditions.
4. Identify the current frontier: high-impact questions whose prerequisites are already settled. Defer questions that depend on unresolved answers.
5. Ask one focused question at a time unless several questions are genuinely independent and easier to answer together. For each question provide:
   - why it matters;
   - the options or decision boundary;
   - a recommended default with reasoning and confidence;
   - what downstream choice the answer unlocks.
6. After each answer, update the tree. Challenge contradictions and test the recommendation against every remaining option rather than carrying an eliminated option's rationale forward.
7. End when the high-impact frontier is empty. Present the decision record and ask whether the user wants to proceed, revise a decision, or leave it unresolved.

## Decision record

Return a compact record containing:

- chosen direction and success measure;
- alternatives considered and evidence-based rejection reasons;
- verified facts versus assumptions;
- major risks, mitigations, detection, and rollback;
- unresolved items and their owners;
- acceptance checks;
- a clear go, conditional-go, or no-go recommendation.

Do not manufacture certainty. If evidence is insufficient, scope the conclusion and name what would settle it.
