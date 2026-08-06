# securing-github-actions-workflows

## When this workflow applies

Use to audit or harden GitHub Actions workflows against untrusted input, token abuse, unsafe triggers, dependency compromise, cache/artifact poisoning, self-hosted runner risk, and excessive permissions. A connected GitHub app or repository files are required for live changes. Pin third-party actions to verified full commit SHAs and preserve required functionality.

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

- When GitHub Actions is the CI/CD platform and workflows need hardening against supply chain attacks
- When workflows handle secrets, deploy to production, or have elevated permissions
- When preventing script injection via untrusted PR titles, branch names, or commit messages
- When requiring audit trails and approval gates for workflow modifications
- When third-party actions pose supply chain risk through mutable version tags

## Prerequisites

- GitHub repository with GitHub Actions enabled
- GitHub organization admin access for organization-level settings
- Understanding of GitHub Actions workflow syntax and events

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: securing-github-actions-workflows. Condensed from the validated Codex source for the ChatGPT Web edition; executable examples and local-only artifacts were intentionally omitted._