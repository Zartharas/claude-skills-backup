# analyzing-sbom-for-supply-chain-vulnerabilities

## When this workflow applies

Use to analyze CycloneDX or SPDX SBOMs for vulnerabilities, unsupported components, licensing concerns, provenance gaps, and policy violations. Trigger for SBOM ingestion, component-risk prioritization, VEX-aware review, or supply-chain reporting. Preserve format/version compatibility, verify current vulnerability data, and do not treat a scanner match as proof of exploitability.

## Web execution boundary

This Web edition provides analysis, planning, review, templates, and verification guidance. It does not imply that a scanner, cloud account, repository, endpoint, HSM, SIEM, SOAR, or other external system is connected. Begin read-only. Require explicit authorization, confirmed scope, available tools, and rollback conditions before any live action.

## Operating boundaries

- Work only on systems, applications, data, and artifacts the user owns or is authorized to assess.
- Begin with read-only inspection. Treat network requests, execution of untrusted code, active scanning, exploitation, credential use, containment, and configuration changes as explicit actions requiring confirmed scope.
- Keep destructive, disruptive, or externally visible steps in plan-only form unless the user clearly authorizes execution.
- Review installed tools and local documentation before adding dependencies. Never execute an unreviewed remote-install pipeline; verify the source and pin versions when installation is authorized.
- Preserve evidence and record assumptions, commands, timestamps, limitations, and confidence. Redact secrets and sensitive data from outputs.
- Stop when safety, legal authority, production impact, or evidence integrity is uncertain.

## When to Use

- A new regulatory requirement (EO 14028, EU CRA) mandates SBOM analysis for software deliveries
- Security team needs to assess third-party risk by scanning vendor-provided SBOMs
- CI/CD pipeline requires automated vulnerability checks against generated SBOMs
- Incident response needs to determine if a newly disclosed CVE affects deployed software
- Procurement team requires supply chain risk assessment for a software acquisition

## Prerequisites

- SBOM file in CycloneDX JSON (current baseline 1.7; legacy 1.4+ accepted when the parser supports it) or SPDX JSON (current baseline 3.0.1; legacy 2.3 accepted when supported)
- NVD API key (free, from authoritative source for higher rate limits
- Network access to NVD API (authoritative source
- Optionally: syft for SBOM generation, grype for cross-validation

## Step 1: Generate SBOM (if not provided)

Use syft to create an SBOM from a container image or project directory:
Syft supports over 30 package ecosystems including npm, PyPI, Maven, Go modules, apt, apk, and RPM. The generated SBOM includes package names, versions, licenses, CPE identifiers, and PURL (Package URL) references.

## Step 2: Parse SBOM and Extract Components

Parse the SBOM to extract all software components with their identifiers:
**CycloneDX JSON Structure (legacy-compatible 1.5 example):**
**SPDX JSON Structure (legacy-compatible 2.3 example):**

## Step 3: Correlate Components with NVD CVE Database

Query the NVD 2.0 API to find known vulnerabilities for each component:
The NVD API supports searching by CPE name (most precise), keyword, CVE ID, and date ranges. Rate limits: 5 requests/30 seconds without API key, 50 requests/30 seconds with key.

## Step 4: Build Dependency Graph and Identify Transitive Risks

Construct a directed graph of dependencies to trace vulnerability propagation:
Transitive dependency analysis identifies components that are not directly included but are pulled in through dependency chains. A vulnerability in a deeply nested transitive dependency (e.g., 4 levels deep) still represents risk but may be harder to remediate.
Key graph metrics for risk assessment:
- **In-degree**: How many components depend on this one (high in-degree = high blast radius)
- **Shortest path to root**: Distance from application entry point (closer = more exploitable)

## Step 5: Calculate Risk Scores

Aggregate vulnerability data into component and overall risk scores:

## Step 6: Cross-Validate with Grype

Use grype to independently scan the SBOM and compare findings:
Grype pulls vulnerability data from NVD, GitHub Security Advisories, Alpine SecDB, Red Hat, Debian, Ubuntu, Amazon Linux, and Oracle security databases, providing broader coverage than NVD alone.

## Step 7: Generate Compliance Report

Produce a structured report suitable for regulatory compliance:

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: analyzing-sbom-for-supply-chain-vulnerabilities. Condensed from the validated Codex source for the ChatGPT Web edition; executable examples and local-only artifacts were intentionally omitted._