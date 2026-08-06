# testing-prompt-injection-in-rag-pipelines

## When this workflow applies

Use for authorized testing of RAG pipelines for direct/indirect prompt injection, retrieval poisoning, instruction-data confusion, unsafe rendering, data exfiltration, and downstream tool abuse. Use synthetic or approved corpora, preserve evidence, and define stop conditions. Do not poison third-party knowledge bases or expose real secrets.

## Web execution boundary

This Web edition provides analysis, planning, review, templates, and verification guidance. It does not imply that a scanner, cloud account, repository, endpoint, HSM, SIEM, SOAR, or other external system is connected. Begin read-only. Require explicit authorization, confirmed scope, available tools, and rollback conditions before any live action.

## Operating boundaries

- Work only on systems, applications, data, and artifacts the user owns or is authorized to assess.
- Begin with read-only inspection. Treat network requests, execution of untrusted code, active scanning, exploitation, credential use, containment, and configuration changes as explicit actions requiring confirmed scope.
- Keep destructive, disruptive, or externally visible steps in plan-only form unless the user clearly authorizes execution.
- Review installed tools and local documentation before adding dependencies. Never execute an unreviewed remote-install pipeline; verify the source and pin versions when installation is authorized.
- Preserve evidence and record assumptions, commands, timestamps, limitations, and confidence. Redact secrets and sensitive data from outputs.
- Stop when safety, legal authority, production impact, or evidence integrity is uncertain.
> **Authorized-use-only notice:** This skill describes offensive testing techniques against Retrieval-Augmented Generation (RAG) systems. Run these probes only against applications you own or have explicit written authorization to test. Adversarial inputs that exfiltrate documents or hijack a model can cause real harm to production systems and downstream users. Always test in a non-production environment first and...

## Overview

Retrieval-Augmented Generation (RAG) pipelines combine a large language model (LLM) with a retrieval layer (a vector store such as FAISS, Chroma, Pinecone, Milvus, or pgvector) so the model can answer questions over private documents. The retrieval layer is an *injection surface*: any text that the retriever returns is concatenated into the model's context window and is treated by the model as authoritative. An at...
Beyond text-level injection, RAG pipelines are vulnerable at the *embedding* layer. An attacker who understands the embedding model can craft text that lands near high-value queries in vector space ("embedding manipulation" / retrieval poisoning), guaranteeing that the malicious chunk is retrieved for a target query even when it is not semantically relevant to a human. This skill walks through systematically probi...

## When to Use

- When security-testing a RAG chatbot, internal knowledge assistant, or document-Q&A product before or after release.
- When validating that retrieval guardrails (input/output filtering, context sandboxing) actually block injected instructions.
- During an AI red-team engagement scoped to test the LLM application layer (OWASP LLM Top 10 coverage).
- When you ingest user-controllable or third-party content into a vector store and need to prove the blast radius of a poisoned document.
- As a regression gate in CI/CD: re-run the probe suite on every prompt-template or retriever change.

## Prerequisites

- Network access to the target RAG application (HTTP API, or a local harness you control).
- Authorization / signed RoE for the target.
- Install the tooling:

## Validation Criteria

- [ ] Retrieval surface and ingestion entry points enumerated and documented
- [ ] garak promptinject/latentinjection/leakreplay probes run with a saved report
- [ ] Promptfoo indirect-prompt-injection and rag-document-exfiltration plugins executed
- [ ] PyRIT multi-turn campaign run against the target with scored transcripts
- [ ] Embedding-poisoning PoC shows high cosine similarity and retrieval of the planted chunk
- [ ] At least one successful injection demonstrated end-to-end (or absence verified) with evidence
- [ ] Guardrail behavior recorded for each probe (fired / bypassed)
- [ ] Findings mapped to OWASP LLM01:2025 and MITRE ATLAS AML.T0051
- [ ] Remediation recommendations provided (context isolation, output filtering, corpus provenance)

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: testing-prompt-injection-in-rag-pipelines. Condensed from the validated Codex source for the ChatGPT Web edition; executable examples and local-only artifacts were intentionally omitted._