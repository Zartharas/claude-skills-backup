# conducting-cyber-risk-assessment-with-nist-800-30

## When this workflow applies

Use to conduct or structure a defensible cyber-risk assessment using NIST SP 800-30 Rev. 1 concepts: scope, threat sources/events, vulnerabilities, likelihood, impact, uncertainty, risk determination, and treatment. Trigger when evidence and organizational context are available. Do not fabricate ratings, asset values, threat frequencies, or management acceptance.

## Web execution boundary

This Web edition provides analysis, planning, review, templates, and verification guidance. It does not imply that a scanner, cloud account, repository, endpoint, HSM, SIEM, SOAR, or other external system is connected. Begin read-only. Require explicit authorization, confirmed scope, available tools, and rollback conditions before any live action.

## When to Use

- When the organization needs a real risk *assessment* — an analysis of specific threats, likelihoods, and impacts — rather than a maturity score against a framework. (Maturity tells you how mature your practices are; a risk assessment tells you what could hurt you and how badly.)
- When another framework requires a documented risk analysis as a mandatory input: NIST CSF (ID.RA), ISO 27001 (Clause 6.1.2), NIST RMF / 800-37 (the Prepare and Select steps), SOC 2 (CC3), PCI DSS, or HIPAA (§164.308(a)(1)(ii)(A)).
- When standing up or significantly changing a system and you must understand its risk before authorization or go-live.
- When leadership asks for the organization's top risks, ranked, with a rationale they can defend to a board or regulator.
- When building or refreshing an enterprise risk register.

## Prerequisites

- An inventory of in-scope assets, systems, and the information types they handle (system boundary defined).
- Access to threat intelligence (internal incident history, sector ISAC feeds, MITRE ATT&CK) to ground threat-event likelihood in observed behavior.
- Vulnerability data (scan results, pen-test findings, configuration/architecture review) for the in-scope systems.
- Business context: which missions/processes the systems support, and what impact to confidentiality, integrity, or availability would mean in business terms.
- Familiarity with the three-tier risk-management context from NIST SP 800-39 (organization, mission/business process, information system).

## Workflow

NIST SP 800-30 Rev 1 defines four steps. Steps 1 and 4 bookend the assessment; Step 2 is the analytic core.

## Output Format

1. **Purpose, scope, and tier** — what was assessed and why.
2. **Assumptions, constraints, and risk model** — the factors and scales used (so results are reproducible).
3. **Threat sources** — by type, with adversarial characterization.
4. **Threat events** — each with affected assets and ATT&CK mapping where adversarial.
5. **Vulnerabilities and predisposing conditions** — tied to threat events.
6. **Risk register** — table: ID, threat event, asset, likelihood, impact, **risk level**, contributing vulnerabilities, recommended treatment, owner, residual risk.
7. **Top risks summary** — ranked, in business terms, for leadership.
8. **Maintenance plan** — refresh cadence and re-assessment triggers.

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: conducting-cyber-risk-assessment-with-nist-800-30. Condensed from the validated Codex source for the ChatGPT Web edition; executable examples and local-only artifacts were intentionally omitted._