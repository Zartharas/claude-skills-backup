# skill-pack-quality-auditor

## When this workflow applies

Use to inspect, improve, convert, or validate ChatGPT, Codex, or Agent Skills folders and archives. Trigger when actual SKILL.md files or packages are supplied and the user wants compatibility classification, trigger refinement, progressive disclosure, safety review, code scanning, regression tests, or installable packages. Do not recreate third-party skills from names alone or claim unavailable tools or installation.

## Web execution boundary

This Web edition provides analysis, planning, review, templates, and verification guidance. It does not imply that a scanner, cloud account, repository, endpoint, HSM, SIEM, SOAR, or other external system is connected. Begin read-only. Require explicit authorization, confirmed scope, available tools, and rollback conditions before any live action.

## Goal

Produce a source-preserving, standards-compliant improvement of supplied skills. Work from the actual files, not the public name alone.

## Trigger quality

Create realistic should-trigger, should-not-trigger, and boundary queries. Test:
- Formal and casual wording
- Misspellings
- Short and context-rich prompts
- Prompts that mention the domain without needing the workflow
- Adjacent skills with overlapping vocabulary
- Requests that violate the skill's non-goals
Aim for approximately 20 trigger queries for important skills. Split development and validation prompts to avoid overfitting.

## Workflow quality

Prefer:
- A clear input and output contract
- Evidence hierarchy
- Explicit assumptions and unknowns
- Progressive disclosure
- High control for fragile operations and more freedom for judgment tasks
- Defined completion gates
- Honest tool and capability routing
- Reversible steps and stop conditions for risky work

## Overlap and router design

When several skills belong to one family:
- Keep exact public names as entry points or aliases.
- Create a narrow router only when it reduces trigger collisions or duplicated core instructions.
- Put specialized procedures in child skills or references.
- Do not create a router that activates on every request.
- Define negative triggers so adjacent skills remain distinguishable.

## Validation

Perform:
1. Structural validation
2. Trigger tests
3. Positive workflow tests
4. Negative and boundary tests
5. Tool-availability tests
6. Safety and authorization tests
7. Regression tests against the original skill's useful behavior
8. Archive inspection to confirm the package contains only intended files

## Deliverables

For each skill, provide:
- Compatibility classification
- Key defects and risks
- Preserved source material
- Changes made
- Remaining dependencies or unsupported capabilities
- Positive, negative, and boundary test results
- Installable archive or patched folder
- Honest installation status

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: skill-pack-quality-auditor. Condensed from the validated Codex source for the ChatGPT Web edition; executable examples and local-only artifacts were intentionally omitted._