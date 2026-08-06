# implementing-sigstore-for-software-signing

## Web execution boundary

This Web edition provides analysis, planning, review, templates, and verification guidance. It does not imply that a scanner, cloud account, repository, endpoint, HSM, SIEM, SOAR, or other external system is connected. Begin read-only. Require explicit authorization, confirmed scope, available tools, and rollback conditions before any live action.

## When to Use

- Signing container images and software artifacts without managing long-lived cryptographic keys
- Establishing verifiable provenance for build outputs in CI/CD pipelines using OIDC identity binding
- Querying the Rekor transparency log to audit when and by whom an artifact was signed
- Verifying that container images pulled from registries were signed by authorized identities and issuers
- Integrating Sigstore verification into Kubernetes admission controllers to enforce signed-image policies
**Do not use** for signing artifacts that require air-gapped or offline signing workflows where OIDC authentication is unavailable, for environments that cannot reach the public Sigstore infrastructure (Fulcio, Rekor) and have no private instance deployed, or as a replacement for traditional PGP/GPG signing where regulatory compliance mandates specific key management procedures.

## Prerequisites

- Access to an OIDC identity provider supported by Fulcio (Google, GitHub, Microsoft, or a custom OIDC issuer)
- Container registry credentials (for signing container images) with push access to store signature objects
- Network access to fulcio.sigstore.dev, rekor.sigstore.dev, and tuf-repo-cdn.sigstore.dev (or private Sigstore instance URLs)

## Step 1: Install and Configure Cosign

Confirm installation requirements for Cosign and verify it can reach the Sigstore infrastructure:
- Verify the approved signing-client version and trust configuration before use.

## Step 2: Keyless Signing with Cosign and Fulcio

Perform identity-based signing where Fulcio issues a short-lived certificate bound to your OIDC identity:
- For image signing, bind the signature to the immutable image digest and an approved workload identity; retain certificate and transparency-log evidence.
- For file signing, create and retain a verification bundle containing the signature, certificate, timestamp, and transparency evidence.

## Step 3: Verify Signed Artifacts

Verify that artifacts were signed by expected identities from expected OIDC issuers:
- Verify the signature, certificate identity and issuer, transparency-log inclusion, and current artifact digest before promotion.
- Verify the file signature against the approved identity, issuer, bundle, timestamp, and transparency evidence.
- **Verification failure modes**: Cosign returns a non-zero exit code on failure. Common failures include certificate identity mismatch, expired certificates without a valid Rekor timestamp, missing Rekor entry, and image digest mismatch (image was modified after signing).

## Step 4: Query the Rekor Transparency Log

Search and verify entries in the Rekor transparency log to audit signing events:

## Step 5: Integrate into CI/CD Pipelines

Embed signing and verification into build and deployment pipelines:
- **Kubernetes admission enforcement**: Deploy Sigstore Policy Controller or Kyverno with Cosign verification policies to reject unsigned or incorrectly signed images at admission time
- Attach signed provenance, SBOM, and vulnerability attestations when required, and verify them before promotion.

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: implementing-sigstore-for-software-signing. Condensed from the validated Codex source for the ChatGPT Web edition; executable examples and local-only artifacts were intentionally omitted._