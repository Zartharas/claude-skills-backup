# performing-cloud-incident-containment-procedures

## Web execution boundary

This Web edition provides analysis, planning, review, templates, and verification guidance. It does not imply that a scanner, cloud account, repository, endpoint, HSM, SIEM, SOAR, or other external system is connected. Begin read-only. Require explicit authorization, confirmed scope, available tools, and rollback conditions before any live action.

## Overview

Cloud incident containment requires cloud-native approaches that differ significantly from traditional on-premises response. Containment procedures must leverage platform-specific controls including security groups, IAM policies, network ACLs, and service-level isolation to restrict compromised resources while preserving forensic evidence. According to the 2025 Unit 42 Global Incident Response Report, responding t...

## When to Use

- When conducting security assessments that involve performing cloud incident containment procedures
- When following incident response procedures for related security events
- When performing scheduled security testing or auditing activities
- When validating security controls through hands-on testing

## Prerequisites

- Familiarity with incident response concepts and tools
- Access to a test or lab environment for safe execution
- Appropriate authorization for any testing activities

## Evidence Preservation Best Practices

1. **Always snapshot before containment** - Create disk/volume snapshots before network isolation
2. **Preserve CloudTrail/Activity Logs** - Copy logs to write-protected storage
3. **Document all actions** - Timestamp every containment step taken
4. **Use break-glass procedures** - Pre-establish emergency access for IR team
5. **Maintain forensic chain of custody** - Hash all evidence artifacts

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: performing-cloud-incident-containment-procedures. Condensed from the validated Codex source for the ChatGPT Web edition; executable examples and local-only artifacts were intentionally omitted._