# multi-expert-analysis

## When this workflow applies

Use for complex, consequential, cross-domain decisions that need several relevant expert lenses, evidence reconciliation, adversarial challenge, and an actionable recommendation. Trigger for cybersecurity, architecture, incident response, GRC, research design, legal-risk, or operational decisions with competing constraints. Do not activate for simple questions or simulate a theatrical panel.

## Web execution boundary

This Web edition provides analysis, planning, review, templates, and verification guidance. It does not imply that a scanner, cloud account, repository, endpoint, HSM, SIEM, SOAR, or other external system is connected. Begin read-only. Require explicit authorization, confirmed scope, available tools, and rollback conditions before any live action.

## Purpose

Increase decision quality through disciplined decomposition, evidence checks, and adversarial review. Do not simulate a theatrical panel of dozens of experts. Select the smallest set of genuinely relevant lenses.
This skill improves the reasoning process and the quality of the visible rationale. It cannot change the host model's native reasoning setting or guarantee correctness.

## Activation threshold

Use this workflow when at least two are true:
- The decision spans multiple domains.
- Error could create legal, security, safety, financial, academic, operational, or reputational harm.
- Evidence is incomplete, conflicting, or time-sensitive.
- The user needs a recommendation rather than a summary.
- There are meaningful tradeoffs, dependencies, or second-order effects.
- An implementation plan must survive review by different stakeholders.
Do not use it merely because a task sounds important.

## Select expert lenses

Choose three to six relevant lenses. Examples:
- Domain specialist
- Security or abuse-case reviewer
- Legal, privacy, or compliance reviewer
- Operations and reliability reviewer
- Architecture or implementation reviewer
- Data, measurement, or research-method reviewer
- Financial or resource reviewer
- Human factors and stakeholder reviewer

## Evidence discipline

Separate:
- **Established facts**
- **Source-derived claims**
- **Reasonable inferences**
- **Assumptions**
- **Unknowns**
- **Time-sensitive claims requiring current verification**
Use authoritative or primary sources for high-stakes claims when external research is available. Never fabricate citations, quotations, legal conclusions, test results, or stakeholder positions.

## Required safety gates

For security testing, offensive work, external actions, or intrusive diagnostics:
- Confirm authorization and scope.
- Prefer non-destructive, reversible methods.
- Protect evidence and privacy.
- Define stop conditions.
- Do not expand scope silently.
- Separate observed evidence from inferred impact.
For academic research:
- Do not fabricate sources, citations, methods, experiments, participants, approvals, or results.

## Output structure

Use only sections that add value:
1. **Conclusion**
2. **Assumptions and evidence**
3. **Cross-expert findings**
4. **Devil's-advocate challenge**
5. **Risk and control table**
6. **Recommendation and conditions**
7. **Unknowns that could change the decision**
Keep the visible rationale concise enough to audit. Do not expose private chain-of-thought or fill the response with fictional dialogue.

## Completion gate

Before finalizing:
- The recommendation follows from evidence and constraints.
- Material counterarguments were addressed.
- Facts, inferences, and unknowns are distinguishable.
- Current claims were verified where necessary.
- Authorization, privacy, and safety boundaries are explicit.
- The next action is feasible and owned.

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: multi-expert-analysis. Condensed from the validated Codex source for the ChatGPT Web edition; executable examples and local-only artifacts were intentionally omitted._