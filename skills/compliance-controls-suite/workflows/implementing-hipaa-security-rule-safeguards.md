# implementing-hipaa-security-rule-safeguards

## When this workflow applies

Use to assess or implement HIPAA Security Rule administrative, physical, and technical safeguards for a defined covered entity or business associate. Distinguish the current rule from proposed changes and verify current HHS guidance. Do not make legal determinations, invent risk-analysis evidence, or claim compliance from a checklist.

## Web execution boundary

This Web edition provides analysis, planning, review, templates, and verification guidance. It does not imply that a scanner, cloud account, repository, endpoint, HSM, SIEM, SOAR, or other external system is connected. Begin read-only. Require explicit authorization, confirmed scope, available tools, and rollback conditions before any live action.

## When to Use

- When an organization is a **covered entity** (health plan, clearinghouse, or provider transmitting electronic transactions) or a **business associate** handling **ePHI** on their behalf.
- When standing up or maturing controls to protect **electronic protected health information**.
- When performing the mandatory **HIPAA Security Risk Analysis** (§164.308(a)(1)(ii)(A)) — the single most-cited gap in OCR enforcement.
- When preparing for an **OCR audit/investigation** or responding to a suspected **breach**.
- When drafting, reviewing, or remediating a **Business Associate Agreement (BAA)**.
- When mapping existing security controls to the HIPAA safeguard standards and implementation specifications.
> Scope note: this skill covers the **Security Rule** (ePHI). The **Privacy Rule** (uses/disclosures of all PHI) and the **Breach Notification Rule** are related but distinct; this skill touches breach readiness and BAAs where they intersect security.

## Prerequisites

- A clear determination of the organization's **role** (covered entity vs business associate) and where ePHI lives, flows, and is stored (an ePHI data map).
- An **asset inventory** of systems that create, receive, maintain, or transmit ePHI.
- Knowledge of the current rule's structure (45 CFR §§164.302–318) and the **required vs addressable** distinction.

## Output Format

1. **Role & ePHI scope** — covered entity vs BA; ePHI data map and systems.
2. **Risk analysis summary** — top risks to ePHI with likelihood/impact (feeds risk management).
3. **Safeguard status** — Administrative / Physical / Technical, each specification marked **Implemented / Partial / Gap** with required-vs-addressable noted.
4. **BAA inventory** — business associates and BAA status.
5. **Breach-notification readiness** — detection, four-factor assessment, notification workflow.
6. **2025 NPRM gap view** — readiness against the proposed mandates (clearly labeled proposed).
7. **Remediation plan** — prioritized, with owners and dates; required specs and risk-analysis gaps first.

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: implementing-hipaa-security-rule-safeguards. Condensed from the validated Codex source for the ChatGPT Web edition; executable examples and local-only artifacts were intentionally omitted._