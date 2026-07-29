# QnA Explanatory Sketches Design

## Goal

Improve the `qna` skill so long explanations include a compact sketch when a visual representation would make the current idea easier to understand.

## Behavior

- Decide per answer chunk whether a sketch would clarify structure, flow, hierarchy, spatial arrangement, state changes, or relationships.
- Use a lightweight inline ASCII or Unicode sketch by default.
- Use Mermaid only when the response environment is known to render it.
- Keep simple facts, definitions, and linear explanations in prose.
- Introduce the sketch briefly and explain its meaning immediately afterward.
- Keep each sketch limited to the current paced chunk; do not reveal later chunks early.
- Treat sketches as an aid to explanation, not decoration.

## Skill Changes

Add a concise visual-decision section to `skills/qna/SKILL.md` and extend its example or common-mistakes guidance enough to demonstrate the expected answer shape.

## Validation

Add a focused contract test that verifies the skill:

1. identifies situations where sketches help;
2. provides a lightweight text-sketch default;
3. states when prose is preferable;
4. preserves paced disclosure; and
5. requires an explanation of the sketch.

Run the focused test and the repository test suite before completion.
