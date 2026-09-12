# Collision Boundaries

This skill owns enterprise security **platform/system engineering**.

## Neighboring skills and boundaries

### Application security review
Owner: `vibe-coding-security-review`

Use that skill when the primary question is whether source code contains exploitable vulnerabilities or insecure implementation patterns.

This skill may consume the resulting findings to assess SIEM visibility, architecture, telemetry, response, or enterprise deployment implications.

### Software delivery / supply chain
Owner: `secure-software-delivery-supply-chain`

Use that skill for CI/CD, SBOM/VEX, dependency risk, build provenance, signing, GitHub Actions hardening, container/IaC supply-chain analysis, and policy-as-code.

This skill owns how those controls integrate with enterprise security operations or platform architecture.

### AI / RAG / agent / MCP security
Owner: `ai-agent-rag-mcp-security-suite`

Use that skill for prompt injection, agent authority, tool abuse, RAG poisoning, MCP security, and AI-native threat modeling.

This skill owns enterprise deployment/integration concerns around AI security products and telemetry.

### Cloud security architecture
Owner: existing Cloud Security Architecture specialist

Use the cloud specialist when the primary task is cloud-native security architecture, landing zones, cloud IAM, cloud control design, or provider-native cloud security posture.

Use this skill when cloud is one component of a broader enterprise security platform/integration problem.

### Cryptography / PKI / Zero Trust
Owner: existing Cryptography, PKI, and Zero Trust specialist

Use that skill for cryptographic design, certificate chains, PKI lifecycle, protocol security, key management, or deep Zero Trust design.

This skill may reason about operational certificate/SAML/platform effects but should not redesign cryptographic primitives.

### OT / ICS
Owner: existing OT and ICS Security specialist

Use that skill for control-system protocols, safety, Purdue/industrial architecture, PLC/SCADA-specific analysis, and OT threat models.

This skill may cover SIEM/SOAR integration of OT telemetry.

### Mobile application security
Owner: existing Mobile Application Security specialist

Use that skill for mobile binary/app review, platform permissions, mobile-specific attack surface, and secure mobile development.

### Architecture rendering
Owner: `archify-web`

This skill produces engineering analysis and architecture facts.
Archify Web turns those facts into diagrams/artifacts.

### AI watermark / provenance
Owner: AI watermark/provenance hygiene skill.

No overlap except that this skill may recommend provenance controls as one enterprise capability.

## Routing rule

If the task can be solved entirely within a specialist domain, use the specialist.

If the problem crosses products, teams, telemetry paths, integration boundaries, or enterprise architecture, this skill is the preferred owner.
