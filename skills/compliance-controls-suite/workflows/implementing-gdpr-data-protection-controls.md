# implementing-gdpr-data-protection-controls

## When this workflow applies

Use to map and implement GDPR technical and organizational controls for a defined processing activity: lawful basis, minimization, rights, security, processors, transfers, retention, breach response, records, and DPIA linkage. Verify current official guidance and jurisdictional context. Do not claim legal compliance or choose a lawful basis without controller input and evidence.

## Web execution boundary

This Web edition provides analysis, planning, review, templates, and verification guidance. It does not imply that a scanner, cloud account, repository, endpoint, HSM, SIEM, SOAR, or other external system is connected. Begin read-only. Require explicit authorization, confirmed scope, available tools, and rollback conditions before any live action.

## Overview

The General Data Protection Regulation (EU) 2016/679 (GDPR) is the EU's comprehensive data protection law governing the collection, processing, storage, and transfer of personal data. This skill covers implementing the technical and organizational measures required by GDPR, including data protection by design and by default, Data Protection Impact Assessments (DPIAs), data subject rights management, breach notific...

## When to Use

- When deploying or configuring implementing gdpr data protection controls capabilities in your environment
- When establishing security controls aligned to compliance requirements
- When building or improving security architecture for this domain
- When conducting security assessments that require this implementation

## Prerequisites

- Understanding of EU data protection law and its territorial scope
- Knowledge of personal data processing activities within the organization
- Familiarity with data architecture, databases, and application systems
- Understanding of data flows including cross-border transfers

## Phase 1: Data Mapping and Assessment (Weeks 1-6)

1. Create comprehensive data inventory:
- What personal data is collected
- From whom (data subjects)
- Why (purposes and lawful bases)
- Where it's stored (systems, locations, countries)

## Phase 2: Gap Analysis and Risk Assessment (Weeks 7-10)

1. Assess current state against GDPR requirements
2. Perform DPIAs for high-risk processing activities
3. Identify security gaps in Article 32 compliance
4. Evaluate data retention compliance
5. Assess data subject rights request handling capabilities

## Phase 3: Technical Controls Implementation (Weeks 11-24)

1. **Encryption**:
- Data at rest: AES-256 for databases, file systems, backups
- Data in transit: TLS 1.2+ for all personal data transfers
- Key management: secure key storage and rotation procedures
2. **Pseudonymization**:

## Phase 4: Organizational Controls (Weeks 11-24)

1. Appoint Data Protection Officer (DPO) if required
2. Develop data protection policies and procedures
3. Create breach notification procedures (72-hour timeline)
4. Establish data subject request (DSR) handling procedures
5. Implement vendor management with Data Processing Agreements (DPAs)

## Phase 5: Documentation and Compliance Evidence (Weeks 25-30)

1. Finalize ROPA documentation
2. Document all DPIAs and outcomes
3. Create data protection policies
4. Document technical and organizational measures
5. Establish privacy notice and consent records

## Phase 6: Ongoing Compliance (Continuous)

1. Regular DPIA reviews for new processing activities
2. Annual data mapping refresh
3. Periodic security measure testing (Art. 32 requirement)
4. Data subject request tracking and SLA monitoring
5. Breach response readiness testing

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: implementing-gdpr-data-protection-controls. Condensed from the validated Codex source for the ChatGPT Web edition; executable examples and local-only artifacts were intentionally omitted._