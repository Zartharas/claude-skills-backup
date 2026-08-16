---
name: vibe-coding-security-review
description: >
  Audits AI-generated ("vibe-coded") application code for the security vulnerability
  patterns AI coding assistants routinely introduce: IDOR/BOLA, disabled Supabase/Firebase/Convex
  row-level security, hardcoded secrets, client-trusted payment prices, unsigned webhooks,
  insecure mobile token storage, SSRF via webhooks/image optimizers/link previews, file-upload
  path traversal and SVG XSS, XSS/DOM/prototype pollution, weak cryptography, SQL/Prisma
  injection, missing rate limiting, cross-tenant data leakage, and MCP tool-poisoning /
  prompt-injection patterns specific to AI coding agents. Use when the user asks to audit,
  review, or check code for security issues, runs /vibe-coding-security-review, or is writing
  or reviewing code that handles authentication, payments, database access, API keys, file
  uploads, or user data. Loads only the reference file(s) matching the technology actually
  detected in the project (Supabase, Stripe, React Native, etc.) rather than every category,
  to keep context use proportional to relevance.
---

# Vibe Coding Security Review

Structured security audit for AI-generated code, organized as reference files loaded by
detected stack rather than a single flat checklist.

## Workflow

1. Identify what's actually in scope: which files changed, which stack/services the project
   uses (Supabase? Stripe? React Native? WebSockets? MCP tools?).
2. Load only the reference file(s) matching that stack — see the category table below.
   Don't load categories with no applicable technology present.
3. For each applicable category, check the concrete patterns listed in that reference file
   against the actual code — not a generic restatement of the category name.
4. Classify each finding: confirmed (you read the vulnerable line), probable (pattern present,
   couldn't fully verify reachability), or informational (best practice gap, not itself
   exploitable).
5. Report file:line for every confirmed/probable finding, with a concrete fix, not just the
   category name.
6. Note explicitly what you did NOT check (e.g., no dynamic/runtime testing was performed;
   this is static review).

## Categories (load only what's relevant)

| Reference | Covers |
|---|---|
| `references/secrets-and-env.md` | Hardcoded API keys, exposed `.env`, `NEXT_PUBLIC_`/`VITE_` leaks, MCP config leaks |
| `references/database-security.md` | Supabase RLS, Firebase rules, Convex auth gaps |
| `references/authentication.md` | IDOR/BOLA, JWT algorithm confusion, OAuth misconfig, `jwt.decode()` without verify |
| `references/multitenancy.md` | Cross-tenant data leakage, unscoped queries |
| `references/rate-limiting.md` | Unprotected auth/AI endpoints, missing CAPTCHA, client-tamperable counters |
| `references/payments.md` | Client-submitted prices, unsigned webhooks, stale subscription checks |
| `references/mobile.md` | Insecure token storage (localStorage/AsyncStorage), API keys in JS bundle |
| `references/ai-integration.md` | AI API key exposure, prompt injection, cache poisoning |
| `references/deployment.md` | Missing security headers, wildcard CORS, exposed `.git`, debug mode in prod |
| `references/ssrf.md` | SSRF via webhooks, image optimizer, link previews, cloud metadata endpoints |
| `references/file-uploads.md` | Path traversal, SVG XSS, MIME spoofing, missing size limits |
| `references/xss-injection.md` | Unsanitized HTML, `javascript:` URIs, prototype pollution, `eval()` |
| `references/cryptography.md` | Weak hashing for passwords, AES-CBC, nonce reuse |
| `references/data-access.md` | SQL injection, Prisma operator injection, insecure deserialization, ReDoS |
| `references/error-handling-logging.md` | Stack traces in API responses, secrets in logs, happy-path-only error handling |
| `references/data-privacy.md` | GDPR/CCPA/APP compliance gaps |
| `references/mcp-and-agents.md` | MCP tool poisoning, hidden instructions in fetched content, agent prompt injection |
| `references/supply-chain.md` | Slopsquatted/hallucinated packages, unpinned dependencies, malicious npm packages |
| `references/websockets.md` | Missing origin checks, unauthenticated socket connections |

## Non-goals

- Not a replacement for a professional penetration test or manual business-logic review —
  automated/structured review catches known patterns, not novel logic flaws.
- Does not perform dynamic testing, exploitation, or any action beyond static code review
  unless the user explicitly asks for and authorizes a specific verification step (e.g., a
  read-only curl check against an endpoint the user owns).
- Overlaps with `secure-software-delivery-supply-chain` (deeper CI/CD and slopsquatting
  coverage) and `ai-agent-rag-mcp-security-suite` (deeper agent/MCP operational-security
  coverage) — this skill covers the application-code-level version of those categories;
  route deeper supply-chain or agent-security questions to those skills instead.

## Provenance

Built from two sources, merged for full category coverage:
- Structure, base categories, and stack-conditional loading: raroque/vibe-security-skill (MIT)
- Gap-fill categories (multitenancy, SSRF, file uploads, XSS, cryptography, error handling,
  data privacy, MCP/agents, supply chain, websockets): ironsightscyber/vibe-security
  (**GPL-3.0** per its actual LICENSE file, despite an MIT badge in its README — noted here
  for accurate provenance if this skill is ever modified or redistributed beyond personal use)
