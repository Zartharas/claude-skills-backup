# implementing-aws-nitro-enclave-security

## Web execution boundary

This Web edition provides analysis, planning, review, templates, and verification guidance. It does not imply that a scanner, cloud account, repository, endpoint, HSM, SIEM, SOAR, or other external system is connected. Begin read-only. Require explicit authorization, confirmed scope, available tools, and rollback conditions before any live action.

## When to Use

- Processing sensitive data (PII, PHI, financial records, cryptographic secrets) that must be isolated from EC2 instance operators and administrators
- Building confidential computing pipelines where even root-level access on the parent instance cannot read enclave memory or state
- Implementing cryptographic attestation workflows that tie KMS decryption rights to a specific, verified enclave image hash
- Deploying multi-party computation environments where two or more enclaves authenticate each other via attestation before exchanging data
- Hardening existing workloads that currently decrypt secrets on the parent instance by migrating decryption into an enclave boundary
**Do not use** when the workload does not handle sensitive data that requires hardware-level isolation, when the instance type does not support Nitro Enclaves (requires Nitro-based instances with at least 4 vCPUs), or when latency constraints make the vsock communication overhead unacceptable.

## Prerequisites

- An AWS account with permissions to launch Nitro-capable EC2 instances (m5.xlarge or larger, C5, R5, M6i families)
- An AWS KMS symmetric key with key policy permissions for the enclave's IAM role
- The aws-nitro-enclaves-sdk-c or Python aws-encryption-sdk for enclave-side KMS operations
- An approved Nitro Enclaves allocator configuration with sufficient memory and vCPU reservations.

## Step 1: Configure the Nitro Enclaves Environment

Set up the parent EC2 instance to support enclave launches:
- **Install the Nitro Enclaves CLI**: On Amazon Linux 2, install the tools and allocator:
- Plan dedicated memory and vCPU reservations for the enclave and validate the impact on parent-instance capacity.
- Verify that the Nitro Enclaves runtime can communicate with the hypervisor before launching workloads.

## Step 2: Build the Enclave Image File (EIF)

Package the sensitive workload into a signed enclave image:
- **Create the application Dockerfile**: The enclave runs a minimal Linux environment. The application communicates exclusively through vsock:
The output contains three critical PCR values:
- **PCR0**: SHA-384 hash of the enclave image file (the full image digest)

## Step 3: Configure KMS Attestation-Based Key Policies

Create a KMS key policy that restricts decryption to a verified enclave:
- **Policy using PCR0 (image hash)**: This locks the key to a specific enclave build. Any code change produces a new PCR0, requiring a policy update:
- **Policy using PCR8 (signing certificate)**: Trusts any enclave signed with a specific certificate, enabling image rotation without policy changes:
- **Multi-PCR policy for defense in depth**: Combine PCR0 (image) and PCR1 (kernel) to ensure both the application and the boot environment match expected values:
- **IAM role policy**: The parent instance's IAM role must have kms:Decrypt permission, but the KMS key policy condition ensures the actual decryption only succeeds when the request originates from a valid enclave with the correct attestation document attached.

## Step 4: Implement Secure Vsock Communication

Establish the parent-to-enclave communication channel:
- **Vsock architecture**: The only way an enclave communicates with the outside world is through a vsock (virtual socket). Vsock uses a CID (Context Identifier) and port number. The parent instance CID is always 3, and the enclave CID is assigned at launch.
- **Parent-side proxy server**: The parent runs a proxy that forwards KMS API calls from the enclave through the vsock to the AWS KMS endpoint:
- **Enclave-side client**: The enclave application requests an attestation document from the Nitro Security Module (NSM) device at /dev/nsm, attaches it to KMS decrypt requests, and receives data encrypted to the enclave's ephemeral public key:

## Step 5: Validate Attestation Documents

Verify attestation documents from enclaves to establish trust:
- **Attestation document structure**: The document is CBOR-encoded and COSE-signed (COSE_Sign1). It contains:
- module_id: Identifier for the NSM module
- digest: Hashing algorithm (SHA-384)
- timestamp: Unix epoch milliseconds when the document was created

## Step 6: Launch and Monitor the Enclave

Review how to run the enclave and implement operational monitoring:
- **Launch the enclave**:
- **Verify enclave status**:
Expected output includes "State": "RUNNING", the assigned EnclaveCID, memory, CPU count, and enclave flags.

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: implementing-aws-nitro-enclave-security. Condensed from the validated Codex source for the ChatGPT Web edition; executable examples and local-only artifacts were intentionally omitted._