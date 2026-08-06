# implementing-code-signing-for-artifacts

## When this workflow applies

Use to design, implement, or audit artifact code signing with platform, PKI, or keyless mechanisms: key protection, identity, signing, verification, timestamping, policy, CI integration, revocation, and evidence. Trigger for build or release integrity. Never embed private keys or claim provenance from a signature alone.

## Web execution boundary

This Web edition provides analysis, planning, review, templates, and verification guidance. It does not imply that a scanner, cloud account, repository, endpoint, HSM, SIEM, SOAR, or other external system is connected. Begin read-only. Require explicit authorization, confirmed scope, available tools, and rollback conditions before any live action.

## When to Use

- When establishing artifact integrity verification to prevent supply chain tampering
- When compliance requires cryptographic proof that build artifacts are authentic and unmodified
- When distributing software to customers who need to verify publisher identity
- When implementing zero-trust deployment pipelines that reject unsigned artifacts
- When meeting SLSA Level 2+ requirements for provenance and integrity

## Prerequisites

- GPG key pair for traditional signing or Sigstore account for keyless signing
- Code signing certificate from a Certificate Authority for public distribution
- CI/CD pipeline with access to signing keys or identity provider
- Verification infrastructure in deployment pipelines

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: implementing-code-signing-for-artifacts. Condensed from the validated Codex source for the ChatGPT Web edition; executable examples and local-only artifacts were intentionally omitted._