# executing-nist-rmf-authorization-to-operate

## When this workflow applies

Use to plan, execute, or audit a NIST RMF authorization-to-operate workflow under SP 800-37 Rev. 2, including categorization, control selection, implementation, assessment, authorization evidence, POA&M, and continuous monitoring. Trigger for federal or RMF-aligned systems. Do not invent authorizing-official decisions, control evidence, inheritance, or compliance status.

## Web execution boundary

This Web edition provides analysis, planning, review, templates, and verification guidance. It does not imply that a scanner, cloud account, repository, endpoint, HSM, SIEM, SOAR, or other external system is connected. Begin read-only. Require explicit authorization, confirmed scope, available tools, and rollback conditions before any live action.

## When to Use

- When a federal or federally-aligned system (or a FedRAMP cloud service) needs an **Authorization to Operate**, a re-authorization, or has fallen out of authorization.
- When you must produce or review the core authorization artifacts: **System Security Plan (SSP)**, **Security Assessment Report (SAR)**, and **Plan of Action & Milestones (POA&M)**.
- When categorizing a system's impact level (Low / Moderate / High) under **FIPS 199**.
- When selecting, tailoring, or implementing a **NIST SP 800-53 Rev 5** control baseline.
- When standing up **continuous monitoring (ConMon)** or pursuing **ongoing authorization / cATO** after an initial ATO.

## Prerequisites

- A defined **system** and **authorization boundary** (what's in, what's inherited, what's a leveraged service).
- An identified **Authorizing Official (AO)**, **System Owner**, and **ISSO**.
- The information types the system handles (use **SP 800-60** to map them to impact levels).
- For cloud: the provider's **Customer Responsibility Matrix (CRM)** and any inherited/leveraged ATO.
- Access to assessment evidence sources (config, scans, policies) for the Assess step.

## Workflow

NIST SP 800-37 Rev 2 defines **seven steps**. Prepare is the foundation; the rest run in order and then loop through Monitor.

## 3. Select (FIPS 200 + SP 800-53 Rev 5 + SP 800-53B)

Start from the SP 800-53B baseline matching the categorization (Low/Moderate/High). Then **tailor**: apply scoping guidance, select compensating controls where needed, and assign values to organization-defined parameters. Add overlays (e.g., privacy, FedRAMP). Record the tailored set and the rationale in the SSP. Identify which controls are **common (inherited)**, **system-specific**, or **hybrid**.

## Output Format

1. **System & boundary** — description, components, data flows, inherited services.
2. **Categorization** — FIPS 199 C/I/A and overall impact, with information-type rationale.
3. **Control baseline & tailoring** — baseline selected, tailoring decisions, common vs system-specific.
4. **Implementation status** — per-family implementation summary (from the SSP).
5. **Assessment results (SAR)** — findings by severity; what's satisfied vs other-than-satisfied.
6. **POA&M** — open weaknesses, risk, owner, milestone dates.
7. **Authorization decision** — ATO/cATO/DATO, term, conditions, residual-risk statement, AO.
8. **ConMon plan** — what's monitored, how often, reporting cadence, reassessment triggers.

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: executing-nist-rmf-authorization-to-operate. Condensed from the validated Codex source for the ChatGPT Web edition; executable examples and local-only artifacts were intentionally omitted._