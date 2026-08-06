# ponytail

## When this workflow applies

Use when the user explicitly requests Ponytail, YAGNI, the simplest working coding solution, a minimal dependency footprint, or the smallest safe diff. Prefer reuse, standard libraries, native features, deletion, and one focused validation. Do not activate for every coding task, and never simplify away security, correctness, accessibility, data protection, tests required by risk, or explicit requirements.

## Web execution boundary

This Web edition provides analysis, planning, review, templates, and verification guidance. It does not imply that a scanner, cloud account, repository, endpoint, HSM, SIEM, SOAR, or other external system is connected. Begin read-only. Require explicit authorization, confirmed scope, available tools, and rollback conditions before any live action.

## Core workflow

Find the smallest **safe, correct, testable** coding solution when the user explicitly asks for Ponytail, YAGNI, a minimal solution, standard-library-first implementation, fewer dependencies, or the smallest safe diff.

## Root-cause rule

For defects, trace relevant callers, data flow, and failure conditions before editing. A small patch in the wrong layer is not a minimal solution because it creates repeated fixes and regression risk.

## Validation

Leave the smallest meaningful check that would fail if the change regressed. Use the project's existing test system when present. Do not replace required tests with an ad hoc assertion merely to keep the diff small.

## Output

Deliver the implementation requested. Briefly state:
- What was reused or avoided
- The validation performed
- The condition that would justify a more complex design
Do not force terse prose; pair with Caveman only when the user requests both.

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: ponytail. Condensed from the validated Codex source for the ChatGPT Web edition; executable examples and local-only artifacts were intentionally omitted._