# building-incident-response-playbook

## When this workflow applies

Use to design or revise an organization-specific incident-response playbook with triggers, severity, roles, evidence handling, containment choices, communications, recovery, metrics, and exercises. Align current NIST SP 800-61 Rev. 3 with CSF 2.0 where applicable. Do not invent organizational authority, contacts, approvals, or system capabilities.

## Web execution boundary

This Web edition provides analysis, planning, review, templates, and verification guidance. It does not imply that a scanner, cloud account, repository, endpoint, HSM, SIEM, SOAR, or other external system is connected. Begin read-only. Require explicit authorization, confirmed scope, available tools, and rollback conditions before any live action.

## When to Use

- Establishing or maturing an incident response program from scratch
- Documenting procedures for a new incident type after a novel attack
- Automating response workflows in a SOAR platform (Cortex XSOAR, Splunk SOAR)
- Preparing for compliance audits requiring documented IR procedures (SOC 2, PCI-DSS, HIPAA)
- Conducting a gap analysis of existing IR capabilities against specific threat scenarios
**Do not use** for one-time ad hoc investigations; playbooks are reusable procedure documents, not case-specific reports.

## Prerequisites

- Organizational risk assessment identifying top incident scenarios by likelihood and impact
- NIST SP 800-61r3 or SANS PICERL framework adopted as the organizational IR standard
- Asset inventory with business criticality ratings and data classification
- RACI chart defining roles: Incident Commander, SOC analysts, system administrators, legal, communications
- Existing detection capabilities inventory (SIEM rules, EDR detections, IDS signatures)
- SOAR platform access if building automated playbooks

## Step 1: Select and Scope the Incident Type

Define the specific scenario the playbook will address:
- Identify the top incident types based on organizational risk assessment and historical data
- Scope each playbook to a single incident type for clarity (do not combine unrelated scenarios)
- Define trigger conditions that activate the playbook
Common playbook types:

## Step 2: Define the Playbook Structure

Every playbook should follow a consistent structure:

## Step 3: Write Decision Trees and Escalation Criteria

Define clear decision points with binary outcomes:
Escalation triggers:
- Any P1 incident: Immediate escalation to IR lead and CISO
- Data exfiltration confirmed: Legal counsel and privacy officer notified
- Customer data involved: Customer notification process activated

## Step 4: Define Specific Technical Procedures

Write tool-specific instructions for each step (not generic guidance):

## Step 5: Integrate with SOAR Platform

Convert manual playbook steps into automated workflows:
- Map each playbook step to a SOAR action (API call, script, human decision point)
- Define automation boundaries (what runs automatically vs. what requires analyst approval)
- Build enrichment automations for the triage phase
- Create containment automations with approval gates for high-impact actions

## Step 6: Test and Maintain the Playbook

Validate the playbook through exercises and maintain currency:
- Conduct tabletop exercises with the IR team walking through the playbook
- Perform live-fire exercises simulating the incident type in a test environment
- Review and update after every real incident that uses the playbook
- Schedule quarterly reviews for accuracy of contact lists, tool procedures, and escalation paths

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: building-incident-response-playbook. Condensed from the validated Codex source for the ChatGPT Web edition; executable examples and local-only artifacts were intentionally omitted._