# performing-user-behavior-analytics

## When this workflow applies

Use to design, review, or implement UEBA for authorized identity and activity data: baselines, features, peer groups, scoring, privacy, tuning, investigations, and validation. Live analytics require a connected SIEM/UEBA platform or supplied data. Do not label a person malicious from anomaly scores alone.

## Web execution boundary

This Web edition provides analysis, planning, review, templates, and verification guidance. It does not imply that a scanner, cloud account, repository, endpoint, HSM, SIEM, SOAR, or other external system is connected. Begin read-only. Require explicit authorization, confirmed scope, available tools, and rollback conditions before any live action.

## When to Use

Use this skill when:
- SOC teams need to detect compromised accounts through abnormal authentication patterns
- Insider threat programs require behavioral monitoring beyond rule-based detection
- Impossible travel or geographic anomalies indicate credential compromise
- Privileged account monitoring requires baseline deviation detection
**Do not use** as the sole basis for disciplinary action — UEBA findings are indicators requiring investigation, not proof of malicious intent.

## Prerequisites

- SIEM with 30+ days of authentication and access log history for baseline creation
- VPN, O365, and Active Directory authentication logs normalized to CIM
- GeoIP database (MaxMind GeoLite2) for location-based anomaly detection
- Identity enrichment data (department, role, manager, typical work hours)
- Splunk Enterprise Security with UBA module or equivalent UEBA capability

## Step 1: Build User Authentication Baselines

Create behavioral baselines from historical data:

## Step 2: Detect Impossible Travel

Identify logins from geographically distant locations within impossible timeframes:

## Step 3: Detect Anomalous Login Timing

Identify logins outside a user's normal working hours:

## Step 4: Detect Unusual Data Access Patterns

Monitor for abnormal file or database access volumes:

## Step 5: Detect Privilege Abuse Patterns

Monitor privileged account usage anomalies:

## Step 6: Generate Risk Score and Prioritize Investigation

Aggregate all UEBA signals into a composite risk score:

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: performing-user-behavior-analytics. Condensed from the validated Codex source for the ChatGPT Web edition; executable examples and local-only artifacts were intentionally omitted._