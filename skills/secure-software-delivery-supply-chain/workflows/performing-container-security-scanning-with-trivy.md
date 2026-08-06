# performing-container-security-scanning-with-trivy

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

- When conducting security assessments that involve performing container security scanning with trivy
- When following incident response procedures for related security events
- When performing scheduled security testing or auditing activities
- When validating security controls through hands-on testing

## Prerequisites

- Container registry credentials for remote image scanning
- CI/CD platform (GitHub Actions, GitLab CI, Jenkins) for pipeline integration
- Kubernetes cluster for Trivy Operator deployment (optional)

## Step 1: Scan Container Images

Review how to run vulnerability and secret scanning against container images from local builds or remote registries. Configure severity thresholds and ignore unfixed vulnerabilities.

## Step 2: Generate SBOM

Produce CycloneDX or SPDX SBOM documents from scanned images for supply chain compliance and vulnerability tracking across the software lifecycle.

## Step 3: Scan IaC and Kubernetes Manifests

Detect misconfigurations in Dockerfiles, Kubernetes YAML, Terraform, and Helm charts using built-in policy checks aligned with CIS benchmarks.

## Step 4: Integrate into CI/CD

Add Trivy scanning as a pipeline gate that blocks builds with critical/high vulnerabilities, generates SARIF reports for GitHub Advanced Security, and produces JUnit XML for test dashboards.

## Expected Output

JSON/table report listing CVEs with severity, CVSS scores, fixed versions, affected packages, misconfiguration findings, and exposed secrets with file locations.

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: performing-container-security-scanning-with-trivy. Condensed from the validated Codex source for the ChatGPT Web edition; executable examples and local-only artifacts were intentionally omitted._