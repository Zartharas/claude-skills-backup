# network-security-analysis

## When this workflow applies

Use to assess authorized network architecture, packet captures, flow/log data, protocols, segmentation, exposure, firewall policy, and defensive controls. Trigger for evidence-based network investigation or design review. Require scope before scanning or active tests, preserve captures as evidence, and do not infer compromise from one indicator.

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

Support network security operations including traffic analysis from PCAP files, IDS/IPS rule authoring for Snort and Suricata, firewall rule auditing, network anomaly detection, and network architecture security reviews.

## Activation Triggers

This skill activates when the user asks about:
- Analyzing PCAP or PCAPNG files for suspicious activity
- Creating Snort or Suricata detection rules
- Writing Zeek (Bro) scripts for network analysis
- Reviewing firewall rules (iptables, nftables, pf, cloud security groups)
- Detecting C2 beaconing, DNS tunneling, or data exfiltration in network traffic
- Network architecture security review
- IDS/IPS signature development
- Network segmentation and east-west traffic analysis

## Prerequisites

**Recommended tools:**
- Wireshark / tshark — Packet capture and GUI analysis
- Suricata — Modern IDS/IPS engine
- Snort 3 — Classic IDS/IPS engine
- Zeek (Bro) — Network analysis and scripting framework
- tcpdump — Command-line packet capture
- NetworkMiner — PCAP artifact extraction
- nmap — Network scanning and discovery

## 2. Suricata Rule Creation

**When the user asks to create Suricata IDS rules:**
**Suricata Rule Syntax Reference:**
**Suricata Testing:**

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: network-security-analysis. Condensed from the validated Codex source for the ChatGPT Web edition; executable examples and local-only artifacts were intentionally omitted._