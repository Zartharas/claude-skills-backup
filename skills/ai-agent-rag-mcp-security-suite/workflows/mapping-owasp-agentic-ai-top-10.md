# Mapping to the OWASP Top 10 for Agentic Applications (2026)

## What this is

Published December 9, 2025 by the OWASP GenAI Security Project's Agentic Security
Initiative — peer-reviewed by 100+ practitioners — this is a distinct taxonomy from the
OWASP Top 10 for LLM Applications. It covers risks specific to systems where an agent
*plans, holds memory, calls tools, and acts autonomously*, not just risks in a single
LLM call. It extends rather than replaces the LLM Top 10; most agent systems inherit both.

Use this as the organizing structure when assessing an agentic system (Claude Code with
MCP servers, an autonomous CI/CD agent, a multi-agent pipeline) rather than treating every
finding as generic "prompt injection."

## The ten categories (ASI01–ASI10)

| ID | Risk | What it covers | Real incident |
|---|---|---|---|
| ASI01 | Agent Goal Hijack | Attacker manipulates the agent's goals, task selection, or decision path — often via indirect prompt injection hidden in content the agent processes (web pages, documents, emails) | EchoLeak (CVE-2025-32711) — zero-click data exfiltration |
| ASI02 | Tool Misuse & Exploitation | Abuse of legitimate tools within the agent's authorized privileges — chaining internal/external tools for exfiltration, over-privileged APIs, poisoned tool descriptions | — |
| ASI03 | Identity & Privilege Abuse | Inherited permissions during delegation, cached/shared credentials, confused-deputy attacks where a lower-privileged agent gets a higher-privileged one to act on its behalf | Amazon Q compromise (950,000+ installs) |
| ASI04 | Agentic Supply Chain Vulnerabilities | Compromised tool servers, poisoned MCP servers, malicious agent packages/plugins | GitHub MCP exploit — see also this catalog's `secure-software-delivery-supply-chain` skill for the package-hallucination (slopsquatting) angle specifically |
| ASI05 | Unexpected Code Execution | Manipulation that reaches actual code execution (RCE) — template injection, unsafe eval paths reached via agent tool chains | — |
| ASI06 | Memory & Context Poisoning | Persistent corruption of context window or long-term memory that influences decisions across sessions, potentially spreading across cooperating agents | — |
| ASI07 | Insecure Inter-Agent Communication | Compromised real-time messages between agents in multi-agent systems — replay attacks on trust chains, fake peer registration, spoofed delegation | — |
| ASI08 | Cascading Agent Failures | Failure or poisoning in one agent propagating through a pipeline, distinct from direct goal hijack (ASI01) or memory poisoning (ASI06) | — |
| ASI09 | Human-Agent Trust Exploitation | Attacks that exploit a human operator's over-trust in agent output/behavior | — |
| ASI10 | Rogue Agents | An agent operating outside its intended scope or constraints, whether from compromise or emergent misalignment | Replit agent deleted a production database during a code freeze |

## How to use this during a review

1. Identify whether the system under review is agentic (plans/acts autonomously across
   steps, holds memory, calls tools) or a single-shot LLM call. If single-shot, the LLM
   Top 10 alone is sufficient — this framework doesn't add coverage for that case.
2. Map the two structural threads that run through most of these categories:
   - **Identity/credential handling** — shows up in ASI03, ASI05, ASI10. Check: what can
     each agent access, and is any credential shared or over-scoped beyond that agent's
     actual task?
   - **Containment of autonomy** — shows up in ASI01, ASI02, ASI07, ASI08. Check: can the
     agent's actions be bounded to its intended task, and is there a human checkpoint before
     consequential actions?
3. For each applicable category, test with scenarios specific to the agent's actual
   architecture rather than generic prompts:
   - ASI01/ASI06 — attempt to poison a document, email, or RAG source the agent will
     retrieve, and observe whether it alters agent behavior
   - ASI02 — probe tool-chaining paths with adversarial parameter combinations
   - ASI03 — test whether the agent can reach systems outside its defined scope through
     credential inheritance
   - ASI07 — test inter-agent message spoofing in any multi-agent setup
4. Apply the OWASP "Least Agency" principle as the primary mitigation lens: grant only the
   minimum autonomy required for the agent's bounded task — this blunts ASI01, ASI02, and
   ASI05 simultaneously rather than needing ten separate fixes.
5. Report findings mapped to the specific ASI category, not as an undifferentiated list —
   this makes findings directly usable against org threat models or compliance mappings
   that reference the framework by ID.

## Relationship to this skill's existing workflows

- `auditing-mcp-servers-for-tool-poisoning.md` — the concrete audit procedure for ASI02
  and part of ASI04
- `securing-agentic-ai-tool-invocation.md` — implementation guidance overlapping ASI01,
  ASI02, ASI03
- `testing-prompt-injection-in-rag-pipelines.md` — the concrete test procedure for ASI01
  and ASI06
- This workflow adds the formal taxonomy and the two categories (ASI07 inter-agent
  communication, ASI08 cascading failures, ASI09 human-trust exploitation, ASI10 rogue
  agents) not covered by the existing workflows at all — most relevant once more than one
  agent or automated pipeline stage is involved.

## Non-goals

- Voluntary community framework, not a compliance mandate on its own — cite it as a
  reference taxonomy, not a certification claim.
- Does not replace authorized penetration testing of a live agentic system.
