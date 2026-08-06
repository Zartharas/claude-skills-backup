# performing-post-quantum-cryptography-migration

## When this workflow applies

Use to inventory cryptographic dependencies and plan a risk-based post-quantum migration using current NIST standards and transition guidance. Trigger for crypto agility, harvest-now-decrypt-later exposure, hybrid testing, vendor readiness, and roadmaps. Distinguish final standards from drafts/selections and do not claim product support without testing.

## Web execution boundary

This Web edition provides analysis, planning, review, templates, and verification guidance. It does not imply that a scanner, cloud account, repository, endpoint, HSM, SIEM, SOAR, or other external system is connected. Begin read-only. Require explicit authorization, confirmed scope, available tools, and rollback conditions before any live action.

## When to Use

- When assessing organizational readiness for the NIST post-quantum cryptography transition
- When building a cryptographic inventory to identify quantum-vulnerable algorithms across infrastructure
- When evaluating hybrid TLS 1.3 configurations using X25519MLKEM768 key exchange
- When testing CRYSTALS-Kyber (ML-KEM) and CRYSTALS-Dilithium (ML-DSA) algorithm support
- When implementing crypto-agility to support both classical and post-quantum algorithms
- When preparing migration roadmaps informed by the draft NIST IR 8547 transition proposal
- When configuring oqs-provider with OpenSSL 3.x for post-quantum algorithm support

## Prerequisites

- oqs-provider for OpenSSL (for hybrid TLS testing with older OpenSSL)
- Network access to target servers for TLS assessment
- Administrative access for infrastructure scanning
- Familiarity with PKI, TLS, and cryptographic protocols

## Phase 1: Cryptographic Inventory Scanning

The first step in PQC migration is discovering all cryptographic algorithm usage
across the enterprise. This includes TLS configurations, certificates, code libraries,
key stores, and protocol configurations.
The scanner identifies:
- TLS protocol versions in use

## Phase 2: Crypto-Agility Assessment

Evaluate the organization's ability to swap cryptographic algorithms without
major infrastructure changes:
Key assessment areas:
1. **Protocol flexibility**: Can TLS configurations be updated without downtime?
2. **Library versions**: Do deployed crypto libraries support PQC algorithms?

## Phase 3: Hybrid TLS Readiness Testing

Test whether infrastructure supports hybrid key exchange with X25519MLKEM768:
**OpenSSL 3.5+ (native ML-KEM support):**
**OpenSSL 3.0-3.4 with oqs-provider:**
**Web Server Configuration for Hybrid TLS:**
Apache httpd:

## Phase 4: ML-KEM Key Encapsulation Validation

Validate that ML-KEM (CRYSTALS-Kyber) key encapsulation works correctly in your
environment:
ML-KEM parameter comparison:

## Phase 5: ML-DSA Digital Signature Validation

Validate ML-DSA (CRYSTALS-Dilithium) signature operations:
ML-DSA parameter comparison:

## Phase 6: Migration Roadmap Generation

Generate a prioritized migration roadmap based on inventory and assessment results:
The roadmap prioritizes systems by:
1. **Data sensitivity**: Systems handling long-lived secrets migrate first
2. **Exposure level**: Internet-facing services before internal
3. **Crypto-agility**: Systems that can easily swap algorithms first

## Validation Checklist

- [ ] Cryptographic inventory covers all TLS endpoints, certificates, and key stores
- [ ] All quantum-vulnerable algorithms (RSA, ECDH, ECDSA, DH, DSA) are identified
- [ ] Crypto-agility assessment documents library versions and upgrade paths
- [ ] Hybrid TLS (X25519MLKEM768) tested on representative server configurations
- [ ] ML-KEM key encapsulation validated at target security level (768 recommended)
- [ ] ML-DSA signature verification validated for certificate chain use
- [ ] SLH-DSA (FIPS 205) evaluated as backup signature algorithm
- [ ] Migration roadmap prioritizes by data sensitivity and compliance timeline
- [ ] OpenSSL version and oqs-provider compatibility confirmed

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: performing-post-quantum-cryptography-migration. Condensed from the validated Codex source for the ChatGPT Web edition; executable examples and local-only artifacts were intentionally omitted._