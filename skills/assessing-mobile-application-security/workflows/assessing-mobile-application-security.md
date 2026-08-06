# assessing-mobile-application-security

## When this workflow applies

Use for authorized Android or iOS security assessment planning, evidence review, and lab testing across storage, transport, authentication, platform controls, reverse engineering, and abuse cases. Align to current OWASP MASVS/MASTG profiles. Require explicit scope and test devices; do not target third-party apps or production users without authorization.

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

Support authorized assessment of Android and iOS application security against the **OWASP MASVS** (Mobile Application Security Verification Standard) and execute tests from the **OWASP MASTG** (Mobile Application Security Testing Guide). The assistant performs static analysis on APK/IPA artifacts, guides dynamic instrumentation (Frida/objection), reviews secure storage, transport, and platform-interaction controls...
> **Authorization Required**: Only test applications you own or are explicitly authorized to assess. Decompiling and modifying third-party apps may violate licenses and law. Confirm written scope before proceeding.

## Activation Triggers

This skill activates when the user asks about:
- Android (APK/AAB) or iOS (IPA) application security testing
- OWASP MASVS / MASTG verification or a mobile pentest checklist
- Decompiling, reversing, or static analysis of a mobile app
- Insecure data storage, hardcoded secrets, or keystore/keychain review
- Certificate pinning, SSL bypass, or mobile TLS/transport security
- Frida / objection dynamic instrumentation or runtime hooking
- AndroidManifest.xml, exported components, deep links, or Info.plist review
- Mobile malware analysis or suspicious APK triage

## Prerequisites

**Optional enhanced capabilities:**
- apktool — APK decode/rebuild
- jadx — Dalvik → Java decompiler
- apkid — packer/obfuscator/compiler fingerprinting
- frida / objection — dynamic instrumentation
- mobsf (MobSF) — automated static+dynamic analysis platform
- Android SDK platform-tools (adb), unzip, openssl

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: assessing-mobile-application-security. Condensed from the validated Codex source for the ChatGPT Web edition; executable examples and local-only artifacts were intentionally omitted._