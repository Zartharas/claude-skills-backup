# performing-ssl-certificate-lifecycle-management

## When this workflow applies

Use to manage or audit TLS/X.509 certificate discovery, issuance, deployment, monitoring, rotation, revocation, renewal, inventory, and incident response. Verify current platform, CA, protocol, and client requirements. Do not replace production certificates or private keys without authorization, staged validation, and rollback.

## Web execution boundary

This Web edition provides analysis, planning, review, templates, and verification guidance. It does not imply that a scanner, cloud account, repository, endpoint, HSM, SIEM, SOAR, or other external system is connected. Begin read-only. Require explicit authorization, confirmed scope, available tools, and rollback conditions before any live action.

## Overview

SSL/TLS certificate lifecycle management encompasses the full process of requesting, issuing, deploying, monitoring, renewing, and revoking X.509 certificates. Poor certificate management is a leading cause of outages and security incidents. This skill covers automating the entire certificate lifecycle using Python and ACME protocol tools.

## When to Use

- When conducting security assessments that involve performing ssl certificate lifecycle management
- When following incident response procedures for related security events
- When performing scheduled security testing or auditing activities
- When validating security controls through hands-on testing

## Prerequisites

- Familiarity with cryptography concepts and tools
- Access to a test or lab environment for safe execution
- Appropriate authorization for any testing activities

## Security Considerations

- Set up automated monitoring for all certificates
- Use ECDSA (P-256) certificates for better performance over RSA
- Enable OCSP stapling on all servers
- Implement Certificate Transparency log monitoring
- Maintain inventory of all certificates and their locations
- Plan for CA compromise scenarios (key pinning, backup CAs)

## Validation Criteria

- [ ] CSR generation produces valid PKCS#10 request
- [ ] Certificate parsing extracts all relevant fields
- [ ] Expiration monitoring detects certificates within threshold
- [ ] Certificate chain validation verifies trust path
- [ ] OCSP checking detects revoked certificates
- [ ] Certificate inventory tracks all deployed certificates

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: performing-ssl-certificate-lifecycle-management. Condensed from the validated Codex source for the ChatGPT Web edition; executable examples and local-only artifacts were intentionally omitted._