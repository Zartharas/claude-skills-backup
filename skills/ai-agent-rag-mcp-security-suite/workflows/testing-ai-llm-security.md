# testing-ai-llm-security

## When this workflow applies

Use for authorized security assessment of AI, LLM, RAG, and agent systems: prompt injection, data leakage, unsafe tool use, output handling, model abuse, supply chain, and monitoring. Define scope, harm limits, test data, and stop conditions. Do not attack public systems, exfiltrate real data, or present a checklist as complete assurance.

## Web execution boundary

This Web edition provides analysis, planning, review, templates, and verification guidance. It does not imply that a scanner, cloud account, repository, endpoint, HSM, SIEM, SOAR, or other external system is connected. Begin read-only. Require explicit authorization, confirmed scope, available tools, and rollback conditions before any live action.

## Operating boundaries

- Work only on systems, applications, data, and artifacts the user owns or is authorized to assess.
- Begin with read-only inspection. Treat network requests, execution of untrusted code, active scanning, exploitation, credential use, containment, and configuration changes as explicit actions requiring confirmed scope.
- Keep destructive, disruptive, or externally visible steps in plan-only form unless the user clearly authorizes execution.
- Review installed tools and local documentation before adding dependencies. Never execute an unreviewed remote-install pipeline; verify the source and pin versions when installation is authorized.
- Preserve evidence and record assumptions, commands, timestamps, limitations, and confidence. Redact secrets and sensitive data from outputs.
- Stop when safety, legal authority, production impact, or evidence integrity is uncertain.

## Purpose

Support authorized assessment of the security of AI/LLM-powered applications — chatbots, RAG pipelines, autonomous agents, and tool-using systems. The assistant maps findings to the **OWASP Top 10 for LLM Applications (2025)** and the **MITRE ATLAS** adversarial-ML knowledge base, builds reproducible attack cases, and recommends concrete mitigations (input/output guardrails, least-privilege tool scopes, content pr...
> **Authorization Required**: Only test AI systems you own or are explicitly authorized to assess. Prompt-injection and data-exfiltration testing against third-party AI services may violate their terms of service and local law. Confirm written scope before proceeding.

## Activation Triggers

This skill activates when the user asks about:
- Prompt injection (direct or indirect), jailbreaks, or system-prompt extraction
- OWASP LLM Top 10, MITRE ATLAS, or AI/ML threat modeling
- Securing a RAG pipeline, vector database, or retrieval layer
- LLM agent / tool-use / function-calling security and confused-deputy risks
- Guardrail, content-filter, or model output validation design
- Sensitive-information disclosure or training-data leakage from a model
- Model / ML supply chain security (model files, pickle, model registries)
- AI red teaming, jailbreak corpora, or automated adversarial prompt generation

## Prerequisites

**Optional enhanced capabilities:**
- garak — LLM vulnerability scanner (NVIDIA)
- promptfoo — prompt/red-team evaluation harness
- API key for the target LLM endpoint (test environment only)
- modelscan / picklescan — ML model file safety scanning

## 6. Output Handling & Guardrails

- **Never** pass raw LLM output into eval, SQL, shell, or innerHTML. Encode/parameterize at the sink (LLM05).
- Layered guardrails: input filter → policy in system prompt → output classifier → sink-specific sanitization. Defense in depth, since any single layer is bypassable.
- Validate structured output against a strict schema; reject on parse failure.
- Apply egress controls so an injected agent cannot reach attacker URLs.

## Output Standards

Produce a structured AI security assessment:

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: testing-ai-llm-security. Condensed from the validated Codex source for the ChatGPT Web edition; executable examples and local-only artifacts were intentionally omitted._