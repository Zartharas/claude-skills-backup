# performing-soc2-type2-audit-preparation

## When this workflow applies

Use to prepare for a SOC 2 Type II examination: scope, Trust Services Criteria, system description, control design, operating evidence, exceptions, vendors, readiness testing, and remediation. Trigger for readiness, not attestation. Do not claim SOC 2 compliance or auditor conclusions, and preserve evidence periods and ownership.

## Web execution boundary

This Web edition provides analysis, planning, review, templates, and verification guidance. It does not imply that a scanner, cloud account, repository, endpoint, HSM, SIEM, SOAR, or other external system is connected. Begin read-only. Require explicit authorization, confirmed scope, available tools, and rollback conditions before any live action.

## When to Use

- When preparing for a SOC 2 Type II audit engagement with a CPA firm
- When conducting a gap assessment against AICPA Trust Services Criteria
- When automating evidence collection across cloud infrastructure and identity providers
- When validating that controls have operated effectively over the audit period (3-12 months)
- When building continuous compliance monitoring to maintain SOC 2 posture between audits
- When remediating control gaps identified during readiness assessment

## Prerequisites

- Familiarity with AICPA Trust Services Criteria (CC1-CC9)
- Access to cloud provider APIs (AWS, Azure, or GCP) with read-only permissions
- Access to identity provider (Okta, Azure AD, Google Workspace)
- Access to version control system (GitHub, GitLab)
- Access to ticketing system (Jira, Linear, ServiceNow)
- Appropriate authorization to collect compliance evidence

## 4. Automate Evidence Collection

Collect evidence continuously throughout the audit period from integrated systems:

## 7. Prepare Evidence Packages for Auditors

Organize collected evidence into structured packages per criteria:

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: performing-soc2-type2-audit-preparation. Condensed from the validated Codex source for the ChatGPT Web edition; executable examples and local-only artifacts were intentionally omitted._