# performing-privacy-impact-assessment

## When this workflow applies

Use to conduct or structure a privacy impact assessment for a defined system or processing change: data flows, purposes, people, legal/policy context, necessity, risks, controls, residual risk, consultation, and approvals. Verify the governing jurisdiction/template. Do not fabricate processing facts or treat a PIA as legal approval.

## Web execution boundary

This Web edition provides analysis, planning, review, templates, and verification guidance. It does not imply that a scanner, cloud account, repository, endpoint, HSM, SIEM, SOAR, or other external system is connected. Begin read-only. Require explicit authorization, confirmed scope, available tools, and rollback conditions before any live action.

## When to Use

- When launching a new system, product, or processing activity that handles personal data
- When conducting GDPR Article 35 Data Protection Impact Assessments (DPIAs)
- When evaluating CCPA/CPRA compliance for data processing operations
- When performing privacy risk assessments aligned to the NIST Privacy Framework
- When mapping data flows across organizational boundaries and third-party processors
- When building automated privacy governance and assessment pipelines
- When preparing for regulatory audits or demonstrating accountability obligations

## Prerequisites

- Familiarity with GDPR, CCPA/CPRA, and NIST Privacy Framework concepts
- Access to data processing inventories and system architecture documentation
- Appropriate authorization from the Data Protection Officer (DPO) or privacy team
- Knowledge of organizational data flows and third-party processor relationships

## Phase 1: Data Inventory and Processing Activity Catalog

Build a complete inventory of personal data processing activities. Each record of
processing activity (ROPA) entry must capture the data categories, legal basis,
retention periods, and data subjects involved.

## Phase 2: Data Flow Mapping

Map all data flows from collection to deletion, identifying every touchpoint,
transformation, and storage location. This reveals hidden privacy risks in data
movement across systems.

## Phase 3: Privacy Risk Assessment with Scoring Matrix

Apply a structured risk scoring methodology evaluating likelihood and impact
across multiple privacy risk dimensions. The matrix aligns with both the
NIST PRAM and ICO DPIA risk assessment approaches.
Risk categories evaluated include:
1. **Data Minimization** -- Excessive collection beyond stated purpose

## Phase 4: GDPR and CCPA/CPRA Alignment Checks

Review how to run automated compliance checks against specific regulatory requirements.
The engine maps each processing activity against article-level GDPR obligations
and CCPA/CPRA consumer rights requirements.

## Phase 5: Remediation Plan and Report Generation

Generate a prioritized remediation plan with specific action items, responsible
parties, deadlines, and generate the formal PIA/DPIA report document.

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: performing-privacy-impact-assessment. Condensed from the validated Codex source for the ChatGPT Web edition; executable examples and local-only artifacts were intentionally omitted._