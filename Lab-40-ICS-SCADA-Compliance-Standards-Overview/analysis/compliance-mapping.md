# Lab 40 Compliance Mapping

## Purpose

This document maps selected Lab 40 activities to general concepts from ISA/IEC 62443 and NERC CIP.

This is an educational mapping and is not a formal compliance assessment.

| Lab Activity | ISA/IEC 62443 Concept | NERC CIP Concept | Evidence |
|---|---|---|---|
| PLC configuration baseline | Configuration/security lifecycle | System security management | PLC configuration + hash |
| HMI configuration baseline | Configuration/security lifecycle | System security management | HMI configuration + hash |
| Git version control | Lifecycle and change management | Configuration/security evidence | Git history |
| CMDB | Asset/configuration management | Documentation and evidence | SQLite database |
| Configuration review | Security verification | Security monitoring/management | config-review.sh |
| Change detection | Risk management and monitoring | System security management | Periodic review |
| Configuration restoration | Lifecycle maintenance | Recovery planning | Baseline configuration |
| Network segmentation concept | Zones and conduits | Electronic access controls | Framework comparison |
| Incident management policy | Security lifecycle | CIP-008 concepts | Security policy |
| Recovery policy | Lifecycle security | CIP-009 concepts | Security policy |

## Control Objectives

### Configuration Management

Maintain known-good configurations and record authorized changes.

### Access Control

Restrict access to ICS systems and approved communication paths.

### Network Security

Separate systems according to their security requirements and control communication between zones.

### Monitoring

Detect unexpected configuration changes and investigate abnormal activity.

### Incident Response

Maintain procedures for identifying, responding to, and documenting cybersecurity incidents.

### Recovery

Maintain known-good configurations and procedures for restoring critical systems.

## Important Limitation

This mapping does not establish certification, compliance, or regulatory applicability.

A real assessment would require:

- Scope determination.
- Detailed control requirements.
- Formal risk assessment.
- Organization-specific procedures.
- Technical validation.
- Evidence review.
- Periodic assessment.

## Key Takeaway

Compliance frameworks can be translated into practical security activities such as configuration management, access control, monitoring, incident response, recovery, and evidence collection.
