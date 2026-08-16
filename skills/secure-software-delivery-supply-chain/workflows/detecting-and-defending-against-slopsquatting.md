# Detecting and defending against slopsquatting

## What this is

AI coding assistants hallucinate package names that don't exist — roughly 19.7% of
AI-recommended packages across a 576,000-sample academic study (USENIX Security 2025,
Spracklen et al.). Attackers register those exact hallucinated names on PyPI/npm and
attach malicious payloads. Traditional typosquatting defenses (name-similarity/collision
detection against existing packages) don't catch this: hallucinated names are brand-new
strings with nothing to collide against.

This is a distinct, escalating threat class from generic "check your dependencies" supply
chain review — it specifically targets the gap between what an AI agent recommends and
what a human (or the agent itself, autonomously) installs without independent verification.

## Why it's more exploitable than it sounds

- **Hallucinations are predictable, not random.** When the same prompt is re-run ten times,
  43% of hallucinated package names repeat on every single run. An attacker needs only a
  few dozen queries against a popular model to identify and pre-register the names most
  likely to be recommended to real users later.
- **Cross-registry confusion compounds it.** ~8.7% of Python packages hallucinated by models
  actually exist as real packages in the npm registry — a developer working in Python could
  unknowingly be steered toward installing a JavaScript-ecosystem package, or an attacker
  could register the name on PyPI specifically to catch this confusion.
- **Confirmed, not theoretical.** The `unused-imports` npm package (hallucinated instead of
  the real `eslint-plugin-unused-imports`) was still live with ~233 weekly downloads as of
  February 2026, despite being security-flagged. `huggingface-cli` on PyPI (hallucinated
  instead of the correct `pip install huggingface_hub[cli]`) accumulated 30,000+ downloads
  in three months after being copied into a public Alibaba repo's README without verification
  — illustrating how a single unverified copy-paste from AI output can propagate through
  trusted documentation to a wide audience.

## The CI/CD-specific escalation: when the agent installs autonomously

The risk compounds significantly when an AI coding agent is wired into CI/CD with enough
permission to resolve and install dependencies without a human in the loop. The Clinejection
incident (disclosed February 2026) is the concrete pattern to check for: an AI-powered issue
triage workflow was configured with `allowed_non_write_users: "*"` (any GitHub user could
trigger it) and an overly broad `--allowedTools "Bash,Read,Write,Edit,..."` flag — together
giving an untrusted external trigger a path to arbitrary code execution on the CI runner.

**Check for this pattern specifically:**
- Any GitHub Actions workflow using an AI coding action (e.g. `claude-code-action` or
  equivalent) — inspect `allowed_non_write_users` / equivalent triggering-permission fields;
  it should never be a wildcard for workflows with write or execution capability
  Related: `workflows/securing-github-actions-workflows.md` in this skill.
- The `--allowedTools` (or equivalent tool-scoping flag) granted to any autonomous agent in
  CI — scope it to the minimum required, not a broad `Bash,Write,Edit` grant
- Whether the agent can install packages *and* execute code in the same job without a
  human-reviewed gate in between

## Verification workflow

1. **Never install a package name recommended by an AI assistant without checking it exists
   and matches the intended package.** Search the registry directly (pypi.org, npmjs.com);
   don't trust the name as given.
2. **Enforce lockfile pinning and package hash verification in CI/CD** — this is the primary
   structural defense. A pinned lockfile with hash verification means a newly-registered
   malicious package under a hallucinated name can't silently substitute for what was
   actually reviewed and approved.
3. **Audit existing dependency manifests for suspiciously plausible but unfamiliar package
   names** — particularly ones that read like a conflation of two real packages (38% of
   hallucinations in the USENIX study were this pattern, e.g. mashing two real package names
   together) or a name that's suspiciously exact for what the code needed.
4. **If an autonomous agent resolves and installs dependencies in CI**, require the
   installation step to run in a separate, permission-scoped job from any step with write
   access to the repo or secrets — don't let dependency resolution and deployment share
   a blast radius.
5. **Report findings** as: package name, where it's referenced, whether it was verified to
   exist and match the intended package, and — if not verifiable — flag as
   `probable slopsquat` rather than asserting malicious intent without registry confirmation.

## Non-goals

- This does not replace SBOM/VEX analysis (`workflows/analyzing-sbom-for-supply-chain-vulnerabilities.md`)
  or container scanning (`workflows/performing-container-security-scanning-with-trivy.md`) —
  those catch known-vulnerable *real* packages; this catches *fabricated* ones.
- Does not perform live registry lookups or execute installs; verification steps above are
  guidance for the user or an authorized, explicitly-approved tool call — never install a
  package as part of this review without explicit authorization.
