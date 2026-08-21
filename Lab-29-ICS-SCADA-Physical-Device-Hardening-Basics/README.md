# Lab 29: ICS/SCADA Physical Device Hardening Basics

## Overview

This lab covers basic physical security and environmental protection practices for ICS/SCADA environments.

The lab focuses on:

- Physical enclosure security
- Tamper protection
- Physical access control
- Environmental protection
- Environmental monitoring
- Security policies
- Physical security incident response

> **Environment Limitation:**  
> This lab was performed in AWS EC2. Physical PLCs, RTUs, HMIs, industrial cabinets, physical locks, tamper seals, and industrial environmental sensors were not available. Therefore, physical installation and direct hardware inspection were not performed. The exercise documents the assessment methodology and recommended controls for a real ICS/SCADA environment.

---

## Objectives

- Assess physical enclosure security.
- Identify physical security weaknesses.
- Document security enhancements.
- Analyze environmental risks.
- Define environmental mitigation controls.
- Develop a physical security policy.
- Develop an incident-response plan.
- Document AWS environment limitations.
- Preserve assessment evidence.

---

## Environment

| Item | Value |
|---|---|
| Environment | AWS EC2 |
| Operating System | Ubuntu 24.04.3 LTS |
| Kernel | 6.14.0-1018-aws |
| Architecture | x86_64 |
| Hostname | `ip-172-31-10-116` |
| Interface | `ens5` |
| IP Address | `172.31.10.116/24` |

---

# Task 1 — Enclosure Security

## Enclosure Assessment

The enclosure assessment reviewed:

- Enclosure construction
- Mechanical protection
- Existing damage
- Cable entry protection
- Dust and moisture protection
- Physical access restrictions
- Environmental resilience
- Single points of failure
- Equipment redundancy

A physical industrial enclosure was not available in the AWS environment, so the assessment was performed as a documented security review.

**Evidence:**

`hardening/enclosure-assessment.md`

## Security Enhancements

Recommended controls were documented for:

- Tamper-evident seals
- Mechanical locks
- Electronic access control
- Protected cable entries
- Asset identification
- Physical inspections
- Tamper response

**Evidence:**

`hardening/security-enhancements.md`

---

# Task 2 — Environmental Factors

The environmental assessment examined conditions that can affect ICS/SCADA equipment reliability.

| Factor | Potential Impact |
|---|---|
| Dust | Contamination and overheating |
| Heat | Component degradation |
| Vibration | Mechanical stress |
| Moisture | Corrosion and electrical faults |
| Water Leakage | Equipment damage |
| Poor Ventilation | Heat accumulation |

Recommended controls included:

- Suitable industrial enclosures
- Dust protection
- Temperature monitoring
- Humidity monitoring
- Cooling and thermal management
- Vibration dampening
- Water-leak detection
- Preventive maintenance
- Environmental alarms

**Evidence:**

`hardening/environmental-assessment.md`

---

# Task 3 — Security Documentation

## Physical Security Policy

A physical security policy was developed covering:

- Physical access control
- Asset protection
- Environmental protection
- Inspection and maintenance
- Tamper detection
- Environmental monitoring
- Change management
- Personnel responsibilities
- Audit requirements

**Evidence:**

`hardening/physical-security-policy.md`

## Incident Response Plan

An incident-response plan was developed for:

- Unauthorized physical access
- Broken locks or seals
- Open control cabinets
- Unknown equipment or cables
- Physical equipment damage
- Temperature problems
- Water leakage
- Cooling failures
- Excessive vibration

The response process covers:

1. Safety assessment
2. Incident identification
3. Initial response
4. Evidence preservation
5. Tampering response
6. Environmental failure response
7. Recovery
8. Post-incident review

**Evidence:**

`hardening/incident-response-plan.md`

---

# Security Controls Summary

| Area | Controls |
|---|---|
| Physical Access | Locks, restricted areas, access control |
| Tamper Protection | Tamper-evident seals, inspections |
| Enclosures | Secure cabinets, protected cable entries |
| Environment | Temperature, humidity, vibration monitoring |
| Maintenance | Periodic inspections |
| Monitoring | Environmental alarms and logging |
| Incident Response | Identification, preservation, recovery |
| Governance | Policies, audits, change management |

---

# AWS Laboratory Limitation

The AWS environment is a virtual cloud environment and does not represent a physical industrial control facility.

The following activities were therefore not physically performed:

- Installing cabinet locks
- Applying tamper seals
- Installing biometric systems
- Inspecting PLC cabinets
- Installing industrial environmental sensors
- Measuring industrial vibration
- Inspecting physical cabling
- Inspecting physical control rooms

The exercise demonstrates the assessment, planning, documentation, and policy aspects of physical ICS/SCADA hardening.

No physical security control is claimed to have been installed during this exercise.

---

# Evidence Structure

```text
Lab-29-ICS-SCADA-Physical-Device-Hardening-Basics/
├── README.md
└── hardening/
    ├── enclosure-assessment.md
    ├── environmental-assessment.md
    ├── incident-response-plan.md
    ├── physical-security-policy.md
    └── security-enhancements.md
```

# Assessment Result

Lab 29 successfully documented a basic physical hardening framework for ICS/SCADA environments.

The lab addressed:

- Physical enclosure security
- Physical access controls
- Tamper protection
- Environmental risks
- Environmental monitoring
- Security policy development
- Incident-response planning
- AWS environment limitations

No physical industrial equipment was modified or installed during this exercise.

---

# Lab Status

- [x] AWS environment identified
- [x] Enclosure assessment completed
- [x] Security enhancement plan completed
- [x] Environmental assessment completed
- [x] Physical security policy completed
- [x] Incident-response plan completed
- [x] AWS limitations documented
- [x] Evidence organized
- [x] README completed

**LAB 29 — COMPLETE**

---

# Evidence Directory

All supporting documentation is stored in:

`hardening/`

---

# Skills Demonstrated

- ICS/SCADA physical security assessment
- Physical asset protection
- Tamper detection planning
- Environmental risk assessment
- Environmental monitoring
- Security policy development
- Incident-response planning
- Security documentation
- Audit and evidence organization

---

# Conclusion

This lab demonstrated how physical security, environmental protection, documentation, and incident-response planning contribute to the security and reliability of ICS/SCADA environments.

Although the exercise was performed in AWS EC2 rather than a physical industrial facility, the documented controls and procedures provide a practical baseline for implementation in a real ICS/SCADA environment.
