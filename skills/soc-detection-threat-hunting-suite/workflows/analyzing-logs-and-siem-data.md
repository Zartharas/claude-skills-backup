# analyzing-logs-and-siem-data

## When this workflow applies

Use to investigate authorized security events from supplied logs, SIEM exports, or a genuinely connected SIEM: normalize fields, reconstruct timelines, correlate activity, write or review defensive queries, and distinguish observed evidence from inference. Do not claim live access, execute searches, or widen scope unless the current host exposes the system and the user authorizes it.

## Web execution boundary

This Web edition provides analysis, planning, review, templates, and verification guidance. It does not imply that a scanner, cloud account, repository, endpoint, HSM, SIEM, SOAR, or other external system is connected. Begin read-only. Require explicit authorization, confirmed scope, available tools, and rollback conditions before any live action.

## Operating boundaries

- Work only on systems, applications, data, and artifacts the user owns or is authorized to assess.
- Begin with read-only inspection. Treat network requests, execution of untrusted code, active scanning, exploitation, credential use, containment, and configuration changes as explicit actions requiring confirmed scope.
- Keep destructive, disruptive, or externally visible steps in plan-only form unless the user clearly authorizes execution.
- Review installed tools and local documentation before adding dependencies. Never execute an unreviewed remote-install pipeline; verify the source and pin versions when installation is authorized.
- Preserve evidence and record assumptions, commands, timestamps, limitations, and confidence. Redact secrets and sensitive data from outputs.
- Stop when safety, legal authority, production impact, or evidence integrity is uncertain.

## Purpose

Support security log analysis across all major platforms. The assistant analyzes supplied log samples, drafts SIEM and Sigma logic, proposes correlation rules, and identifies anomalous patterns without claiming platform execution.

## Activation Triggers

This skill activates when the user asks about:
- Parsing Windows Event Logs, Linux syslog, or application logs
- Building Splunk SPL, Elastic KQL/EQL, QRadar AQL, or Sentinel KQL queries
- Creating Sigma rules for platform-agnostic detection
- Detecting anomalies or attack patterns in log data
- Building SIEM correlation rules for complex attack scenarios
- Converting queries between SIEM platforms
- Log source health monitoring and gap analysis
- Detecting lateral movement, privilege escalation, or persistence in logs

## Prerequisites

**Platform tools:**
- Splunk — Splunk Web, SPL, and SOAR
- Elastic Stack — Kibana, KQL, EQL
- Microsoft Sentinel — KQL, Workbooks
- IBM QRadar — AQL, Rules
- Sigma — Platform-agnostic rule format
- python-evtx — Parse Windows .evtx files without Windows

## 4. Sigma Rule Development

**When the user asks to create Sigma rules:**
**Sigma rule conversion to SIEM platforms:**

## 5. Correlation Rule Development

**When the user asks to create correlation rules for multi-event detection:**
Step 1: Bucket failed logins by source IP in 5-minute windows
Step 2: If count > 20 → mark IP as "brute force source"
Step 3: Watch for successful login from same IP within 10 minutes
Step 4: If successful login → escalate to HIGH severity
Step 5: Watch for lateral movement from the successfully logged-in host
Step 6: Declare incident if all 3 events observed
spl
index=windows EventCode=4625

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: analyzing-logs-and-siem-data. Condensed from the validated Codex source for the ChatGPT Web edition; executable examples and local-only artifacts were intentionally omitted._