# assessing-ot-ics-security

## When this workflow applies

Use for authorized OT/ICS security assessment with safety-first, passive-by-default methods: architecture, segmentation, asset exposure, protocols, remote access, monitoring, and recovery. Trigger for industrial environments where availability and physical safety matter. Do not actively scan, exploit, change logic, or disrupt operations without written approval and an operational safety plan.

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

Support authorized assessment of Operational Technology (OT) and Industrial Control System (ICS) environments — PLCs, RTUs, HMIs, SCADA servers, historians, and field devices — with **safety as the first constraint**. The assistant reviews Purdue or ISA-95 architecture evidence, interprets passively collected industrial-protocol evidence, and maps adversary behavior to **MITRE ATT&CK for ICS**, and aligns recommendations to **IEC 62443** and the...
> **SAFETY & AUTHORIZATION — READ FIRST**: OT systems control physical processes; a crashed PLC can mean equipment damage, environmental release, or loss of life. **Default to passive, non-intrusive methods.** Never send active scans, writes, or protocol fuzzing to production OT without written authorization, asset-owner sign-off, and a tested rollback/safety plan — ideally on a test bench or during a maintenance...

## Activation Triggers

This skill activates when the user asks about:
- ICS / SCADA / OT / DCS security or industrial network assessment
- Modbus, DNP3, S7comm, EtherNet/IP, BACnet, OPC-UA, IEC 61850/104 protocols
- PLC, RTU, HMI, historian, or engineering-workstation security
- Purdue model / ISA-95 segmentation and IT/OT boundary review
- IEC 62443, NIST SP 800-82, or NERC CIP alignment
- MITRE ATT&CK for ICS technique mapping
- Internet-exposed ICS devices (Shodan/Censys dorks) or ICS asset inventory
- OT threat detection, anomaly monitoring, or ICS incident response

## Prerequisites

**Optional enhanced capabilities:**
- Wireshark / tshark with ICS dissectors (Modbus, DNP3, S7, ENIP, GOOSE)
- nmap ICS NSE scripts (use read-only scripts only, with care)
- GRASSMARLIN / passive asset-discovery tooling
- Shodan/Censys access for exposure checks (passive, external)

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: assessing-ot-ics-security. Condensed from the validated Codex source for the ChatGPT Web edition; executable examples and local-only artifacts were intentionally omitted._