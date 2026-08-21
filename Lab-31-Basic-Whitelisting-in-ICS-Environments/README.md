# Lab 31: Basic Whitelisting in ICS Environments

## Overview

This lab demonstrates a basic application-control approach for an ICS/SCADA environment using AppArmor on Ubuntu Linux.

The lab covers:

- Identifying critical ICS software
- Creating a controlled SCADA test application
- Installing AppArmor
- Generating an AppArmor profile
- Enforcing the AppArmor profile
- Testing the protected SCADA application
- Examining an application without an AppArmor profile
- Collecting security evidence
- Documenting AWS laboratory limitations

> **Environment Limitation:**  
> This laboratory was performed in an AWS EC2 Ubuntu environment. No physical PLC, RTU, HMI, SCADA server, or industrial control system was available. A controlled test application was therefore used instead of real industrial software.

---

# Objectives

The objectives of this lab were to:

- Understand application whitelisting concepts in ICS environments.
- Identify critical software that requires application-control protection.
- Install and configure AppArmor.
- Create a controlled SCADA test application.
- Generate an AppArmor security profile.
- Place the profile into enforce mode.
- Verify that the protected application continues to operate.
- Examine an application without an AppArmor profile.
- Preserve evidence of the security configuration.
- Document the limitations of the AWS laboratory environment.

---

# Environment

| Item | Value |
|---|---|
| Environment | AWS EC2 |
| Operating System | Ubuntu 24.04 |
| Architecture | x86_64 |
| Security Tool | AppArmor |
| Application Control | AppArmor |
| Test Application | `scada-app-bin` |
| Unauthorized Test Application | `nano` |

---

# Task 1 — Identify Critical ICS Software

## Critical ICS Software

Critical ICS/SCADA software was identified according to its operational importance and the potential impact of unauthorized execution or modification.

The following software components were identified as important for application-control protection:

- SCADA Server Application
- HMI Application
- PLC Engineering Software
- Historian Application
- ICS Database
- Alarm Management Software
- Remote Access Client

The detailed assessment was documented in:

`whitelisting/critical-software.md`

---

# Task 2 — Implement AppArmor Application Control

## AppArmor Installation

AppArmor and its utilities were installed using the Ubuntu package manager.

The AppArmor service was enabled and started successfully.

AppArmor status was verified using:

```bash
sudo aa-status
```

The verification confirmed that the AppArmor kernel module was loaded and that security profiles were active.

---

# Controlled SCADA Test Application

Because the AWS laboratory did not contain a real industrial control application, a controlled test application was created.

Application path:

`test-app/scada-app-bin`

The application was made executable and tested before applying AppArmor enforcement.

The application produced the following output:

```text
SCADA Test Application
Application is running successfully.
ICS process simulation active.
```

This confirmed that the controlled application was functioning correctly before security enforcement.

---

# AppArmor Profile Generation

An AppArmor profile was generated for the controlled SCADA test application using:

```bash
sudo aa-genprof "$(readlink -f test-app/scada-app-bin)"
```

The generated profile was associated with:

`test-app/scada-app-bin`

The application was exercised during the profile-generation process so that AppArmor could observe the application's required behavior.

The profile was then completed and loaded into AppArmor.

---

# AppArmor Enforcement

The generated AppArmor profile was placed into enforce mode using:

```bash
sudo aa-enforce "$(readlink -f test-app/scada-app-bin)"
```

The profile status was then verified with:

```bash
sudo aa-status
```

The verification confirmed that the SCADA test application had an AppArmor profile operating in enforce mode.

The collected evidence showed:

- AppArmor profiles loaded
- AppArmor profiles in enforce mode
- `scada-app-bin` listed as an enforce-mode profile
- The SCADA test application associated with the AppArmor profile

Evidence was saved in:

`evidence/apparmor-status.txt`

and:

`evidence/scada-apparmor-profile.txt`

---

# Task 3 — Validate Application Control

## Authorized Application Test

After the AppArmor profile was placed into enforce mode, the protected SCADA test application was executed again.

Command used:

```bash
./test-app/scada-app-bin
```

The application successfully produced:

```text
SCADA Test Application
Application is running successfully.
ICS process simulation active.
```

This demonstrates that the authorized test application continued to operate while its AppArmor profile was enforced.

---

# Unauthorized Application Test

The laboratory used `nano` as an example of an application that did not have an AppArmor profile assigned to it.

The application was identified using:

```bash
command -v nano
```

The result showed:

```text
/usr/bin/nano
```

The installed version was:

```text
GNU nano, version 7.2
```

The AppArmor status was checked using:

```bash
sudo aa-status | grep -w nano
```

No AppArmor profile was found for `nano`.

The evidence was recorded in:

`evidence/unauthorized-application-test.txt`

---

# Important Security Observation

The absence of an AppArmor profile does **not** automatically mean that an application is blocked.

Therefore, this lab does **not** claim that `nano` was prevented from executing.

The test demonstrates that the current AppArmor configuration specifically confines the protected SCADA test application.

It does not implement a complete system-wide executable allowlist.

This distinction is important because AppArmor application confinement and enterprise-wide application whitelisting are not exactly the same security control.

A complete application-whitelisting architecture may require additional application-control technologies and policies.

---

# Security Findings

| Security Check | Result |
|---|---|
| AppArmor installed | PASS |
| AppArmor service enabled | PASS |
| AppArmor module loaded | PASS |
| Critical ICS software identified | PASS |
| SCADA test application created | PASS |
| SCADA test application tested | PASS |
| AppArmor profile generated | PASS |
| AppArmor profile loaded | PASS |
| AppArmor profile enforced | PASS |
| Authorized application tested | PASS |
| Unauthorized application identified | PASS |
| Unauthorized application automatically blocked | NOT CLAIMED |
| AppArmor evidence collected | PASS |
| AWS limitations documented | PASS |

---

# Evidence Collected

## 1. Critical Software Assessment

File:

`whitelisting/critical-software.md`

This document identifies software components that would normally require strong application-control protection in an ICS/SCADA environment.

---

## 2. AppArmor Status

File:

`evidence/apparmor-status.txt`

This file contains the AppArmor status information collected during the laboratory exercise.

It provides evidence that the SCADA application profile was loaded and operating in enforce mode.

---

## 3. SCADA AppArmor Profile

File:

`evidence/scada-apparmor-profile.txt`

This file contains the generated AppArmor profile for the controlled SCADA test application.

---

## 4. Unauthorized Application Test

File:

`evidence/unauthorized-application-test.txt`

This file documents the `nano` test and confirms that no AppArmor profile was assigned to `nano`.

---

# Evidence Structure

```text
Lab-31-Basic-Whitelisting-in-ICS-Environments/
├── README.md
├── whitelisting/
│   └── critical-software.md
├── test-app/
│   └── scada-app-bin
└── evidence/
    ├── apparmor-status.txt
    ├── scada-apparmor-profile.txt
    └── unauthorized-application-test.txt
```

---

# ICS Security Relevance

Application control is important in ICS environments because unauthorized software execution can introduce security and operational risks.

An attacker or unauthorized user may attempt to execute software that has not been approved for an industrial environment.

Application-control mechanisms can help organizations:

- Identify approved applications.
- Restrict application behavior.
- Reduce unauthorized software execution.
- Protect critical engineering systems.
- Protect operator workstations.
- Reduce the attack surface.
- Improve security monitoring.
- Support compliance and audit requirements.

However, application-control policies must be carefully tested in ICS environments.

Unexpected restrictions can interfere with:

- Safety functions
- Monitoring
- Engineering activities
- Maintenance
- Control operations
- Alarm systems
- Industrial availability

For this reason, application-control changes should normally follow formal ICS change-management procedures.

---

# Recommended Production Practices

A real ICS environment should consider the following practices:

1. Maintain an inventory of approved software.
2. Identify critical ICS applications.
3. Define application-control policies.
4. Test policies before enforcement.
5. Use formal change management.
6. Monitor application-control events.
7. Maintain backup and recovery procedures.
8. Protect engineering workstations.
9. Restrict unauthorized software installation.
10. Periodically review application-control policies.
11. Document approved exceptions.
12. Maintain emergency recovery procedures.

---

# AWS Laboratory Limitation

This exercise was performed in an AWS EC2 environment rather than a physical industrial control facility.

The laboratory did not contain:

- Physical PLCs
- Physical RTUs
- Industrial HMIs
- Physical SCADA servers
- Industrial engineering workstations
- Physical control cabinets
- Industrial network equipment
- Real industrial sensors
- Real industrial processes

The application:

`test-app/scada-app-bin`

was therefore used only as a controlled demonstration application.

No real PLC, RTU, HMI, SCADA system, or industrial process was modified or restricted.

---

# What Was Successfully Demonstrated

The laboratory successfully demonstrated:

- Critical ICS software identification.
- AppArmor installation.
- AppArmor service activation.
- AppArmor profile generation.
- AppArmor profile enforcement.
- Controlled SCADA application execution.
- Application-control evidence collection.
- Identification of an application without an AppArmor profile.
- Documentation of security findings.
- Documentation of laboratory limitations.

---

# Lab Status

- [x] Critical ICS software identified
- [x] AppArmor installed
- [x] AppArmor service enabled
- [x] AppArmor module verified
- [x] Test SCADA application created
- [x] Test SCADA application executed
- [x] AppArmor profile generated
- [x] AppArmor profile enforced
- [x] Authorized application tested
- [x] Unauthorized application examined
- [x] Evidence collected
- [x] Evidence organized
- [x] AWS limitations documented
- [x] README completed

**LAB 31 — COMPLETE**

---

# Skills Demonstrated

This laboratory demonstrated the following skills:

- ICS/SCADA security fundamentals
- Application-control concepts
- Linux security administration
- AppArmor configuration
- AppArmor profile generation
- AppArmor enforcement
- Security verification
- Evidence collection
- Security documentation
- ICS application protection
- Security policy awareness
- Change-management awareness
- Audit evidence organization

---

# Conclusion

This lab demonstrated a foundational application-control approach for ICS/SCADA environments using AppArmor on Ubuntu Linux.

A controlled SCADA test application was created and successfully executed under an AppArmor enforce-mode profile.

The AppArmor profile was successfully generated, loaded, and enforced.

The unauthorized application test using `nano` confirmed that `nano` did not have an AppArmor profile.

Importantly, the laboratory does not claim that `nano` was automatically blocked because the configured AppArmor policy was designed to confine the protected SCADA test application rather than create a complete system-wide executable allowlist.

The exercise therefore demonstrates the difference between application confinement and a broader enterprise application-whitelisting architecture.

In a real ICS environment, application-control policies should be carefully tested, documented, approved through change management, and deployed with consideration for safety, reliability, availability, and operational requirements.

---

# Final Assessment

**Lab 31 successfully demonstrated basic application-control and whitelisting concepts using AppArmor in a controlled AWS environment.**

The laboratory evidence confirms that the controlled SCADA test application was successfully protected using an AppArmor enforce-mode profile.

No real industrial control equipment was modified during this exercise.
