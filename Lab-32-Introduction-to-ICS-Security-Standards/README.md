# Lab 32: Introduction to ICS Security Standards

## Overview

This laboratory introduces important cybersecurity standards and security practices used in Industrial Control Systems (ICS) environments.

The primary focus of this lab is **NIST Special Publication 800-82 (NIST SP 800-82), Guide to Operational Technology (OT) Security**.

The laboratory focuses on understanding how cybersecurity principles must be adapted for industrial environments where security, safety, reliability, availability, and real-time operation are important.

The lab covers:

- NIST SP 800-82
- ICS cybersecurity risks
- Physical security
- Network segmentation
- Access control
- Patch management
- Legacy ICS systems
- Monitoring and logging
- Incident response
- Backup and recovery
- Change management
- ICS security architecture
- Differences between ICS and traditional IT security

> **Environment Limitation**
>
> This laboratory was performed as a standards-review and documentation exercise in an AWS EC2 Ubuntu environment.
>
> No physical PLC, RTU, HMI, SCADA server, industrial network, or real industrial process was available.
>
> No production ICS system was modified during this exercise.

---

# Objectives

The objectives of this laboratory were to:

- Understand the basic principles of ICS security.
- Review the major concepts presented in NIST SP 800-82.
- Identify cybersecurity risks specific to ICS environments.
- Identify major security controls relevant to ICS.
- Understand the importance of physical security.
- Understand network segmentation.
- Understand ICS patch-management challenges.
- Understand the security challenges of legacy ICS systems.
- Compare ICS security requirements with traditional IT security.
- Document major ICS security takeaways.
- Create evidence files for the laboratory.
- Build professional ICS security documentation.

---

# Environment

| Item | Value |
|---|---|
| Environment | AWS EC2 |
| Operating System | Ubuntu Linux |
| Architecture | x86_64 |
| Lab Type | Standards Review and Documentation |
| Primary Reference | NIST SP 800-82 |
| Physical PLC | Not Available |
| Physical RTU | Not Available |
| Physical HMI | Not Available |
| Physical SCADA System | Not Available |
| Production ICS Modified | No |

---

# Task 1 — Review NIST SP 800-82

## 1.1 What Is NIST SP 800-82?

NIST SP 800-82 provides cybersecurity guidance for Industrial Control Systems and operational technology environments.

ICS environments include technologies such as:

- Supervisory Control and Data Acquisition (SCADA)
- Distributed Control Systems (DCS)
- Programmable Logic Controllers (PLC)
- Remote Terminal Units (RTU)
- Human-Machine Interfaces (HMI)
- Industrial automation systems
- Safety systems
- Industrial network infrastructure

The guidance helps organizations identify cybersecurity risks and select appropriate security protections while considering the operational requirements of industrial systems.

---

# 1.2 Why ICS Security Is Different

ICS environments are different from traditional IT environments because they directly or indirectly interact with physical processes.

A cybersecurity incident affecting an ICS can potentially result in:

- Production disruption
- Equipment damage
- Loss of process visibility
- Loss of control
- Safety consequences
- Environmental impact
- Financial losses
- Service interruption

For this reason, security decisions in an ICS environment must consider more than confidentiality and data protection.

Security controls must also consider:

- Safety
- Availability
- Reliability
- Operational continuity
- Deterministic behavior
- Real-time requirements
- Physical consequences

---

# 1.3 ICS Security Priorities

Traditional IT security commonly uses the CIA triad:

- Confidentiality
- Integrity
- Availability

ICS environments may place stronger emphasis on:

1. Safety
2. Availability
3. Reliability
4. Integrity
5. Timely and predictable operation

The exact priority depends on the industrial environment, system architecture, business requirements, and risk assessment.

A security control that is acceptable in an IT environment may not always be appropriate for an ICS environment.

For example, immediately rebooting a critical ICS server to install a security update may be acceptable in some IT environments but could cause an unexpected industrial process interruption.

---

# 1.4 ICS Security Risks

ICS environments face both cyber and physical threats.

## Cybersecurity Threats

Attackers may attempt to:

- Obtain unauthorized access.
- Steal user credentials.
- Exploit vulnerable services.
- Modify PLC logic.
- Manipulate industrial processes.
- Disable alarms.
- Disable monitoring.
- Disrupt communications.
- Install malware.
- Modify configuration files.
- Compromise engineering workstations.
- Move from IT networks into OT networks.

---

## Physical Threats

Physical security is particularly important in industrial environments.

Physical threats may include:

- Unauthorized access to control rooms.
- Tampering with control cabinets.
- Theft of equipment.
- Damage to network equipment.
- Unauthorized connection of devices.
- Disconnection of cables.
- Damage to PLCs or RTUs.
- Environmental hazards.

Physical security controls can include:

- Restricted facility access.
- Locked control cabinets.
- Visitor management.
- Security cameras.
- Badge access.
- Security guards.
- Environmental monitoring.
- Physical asset inventory.

---

# 1.5 Legacy ICS Systems

Many ICS environments contain legacy systems that may remain operational for many years.

Legacy systems may have:

- Older operating systems.
- Unsupported software.
- Limited security features.
- Specialized hardware.
- Vendor-specific applications.
- Difficult patching requirements.
- Long replacement cycles.

Replacing a legacy ICS component may require significant planning because the component may be connected to safety-critical or production-critical processes.

Therefore, compensating security controls may sometimes be necessary.

Examples include:

- Network segmentation.
- Firewalls.
- Access restrictions.
- Application control.
- Monitoring.
- Jump servers.
- Strict administrative access.
- Physical security.

---

# 1.6 ICS Architecture

A simplified ICS architecture may look like this:

```text
                Enterprise Network
                       |
                       |
                Industrial DMZ
                       |
                 Firewall / ACL
                       |
                 Control Network
                       |
              +--------+--------+
              |                 |
             HMI              SCADA
              |                 |
              +--------+--------+
                       |
                      PLC
                       |
                Field Devices
                       |
              Sensors / Actuators
```

This architecture demonstrates the importance of separating enterprise IT systems from industrial control systems.

A real ICS architecture may contain additional zones, security boundaries, safety systems, historians, engineering workstations, remote access infrastructure, and other industrial components.

---

# 1.7 Network Segmentation

Network segmentation is an important ICS security practice.

Segmentation helps limit communication between systems that do not need direct access to each other.

A simplified segmentation model can include:

```text
Internet
   |
Enterprise IT Network
   |
Firewall
   |
Industrial DMZ
   |
Firewall
   |
ICS Control Network
   |
PLC / HMI / SCADA
   |
Field Devices
```

Benefits of segmentation include:

- Reduced attack surface.
- Limited lateral movement.
- Controlled communication.
- Better monitoring.
- Separation of IT and OT traffic.
- Improved incident containment.

Segmentation should be designed according to actual operational requirements.

---

# Task 2 — Major ICS Security Takeaways

## 2.1 Physical Security

Physical access to ICS equipment should be restricted.

Recommended controls include:

- Locked server rooms.
- Locked control cabinets.
- Restricted access to engineering workstations.
- Badge-based access.
- Visitor controls.
- CCTV monitoring.
- Physical asset inventories.

Physical security is important because an attacker with direct physical access may be able to bypass some logical security controls.

---

# 2.2 Network Segmentation

ICS networks should not normally be directly exposed to untrusted networks.

Recommended practices include:

- Separating IT and OT networks.
- Using firewalls between security zones.
- Creating an industrial DMZ.
- Restricting unnecessary protocols.
- Limiting administrative access.
- Monitoring traffic between zones.

Example:

```text
Corporate Network
       |
    Firewall
       |
Industrial DMZ
       |
    Firewall
       |
Control Network
       |
 PLC / HMI / SCADA
```

---

# 2.3 Patch Management

Patching ICS systems requires additional planning compared with ordinary IT systems.

Before applying patches, organizations should consider:

- System criticality.
- Vendor support.
- Production schedules.
- Safety requirements.
- Testing requirements.
- Backup availability.
- Recovery procedures.
- Maintenance windows.

A patch should ideally be tested in a controlled environment before deployment to a production ICS.

---

# 2.4 Access Control

Only authorized personnel should have access to ICS systems.

Important practices include:

- Unique user accounts.
- Strong authentication.
- Least privilege.
- Role-based access.
- Restricted administrator access.
- Controlled remote access.
- Account monitoring.
- Removal of unused accounts.

Administrative access should be carefully controlled because compromised administrator credentials can have significant impact on ICS systems.

---

# 2.5 Application Control

Application control can help restrict unauthorized software.

Approved applications should be identified and documented.

Examples of applications that may require strict control include:

- SCADA applications.
- HMI software.
- PLC engineering software.
- Historian applications.
- Industrial databases.
- Alarm management software.
- Remote engineering tools.

Application-control policies should be tested carefully before enforcement.

---

# 2.6 Monitoring and Logging

ICS security monitoring can help identify suspicious activity.

Organizations may monitor:

- Authentication events.
- Network connections.
- Firewall events.
- Configuration changes.
- Application execution.
- PLC changes.
- Engineering workstation activity.
- Security alerts.

Logging should be designed so that monitoring does not negatively affect critical industrial operations.

---

# 2.7 Backup and Recovery

ICS environments should maintain reliable backups of important systems and configurations.

Potential backup targets include:

- PLC programs.
- HMI configurations.
- SCADA configurations.
- Engineering workstation configurations.
- Network device configurations.
- Historian databases.
- Security configurations.

Backups should be:

- Protected.
- Tested.
- Documented.
- Available during recovery.
- Stored according to organizational requirements.

Recovery procedures should be tested before an actual incident occurs.

---

# 2.8 Incident Response

ICS incident response requires consideration of operational safety.

A response process may include:

1. Identify the incident.
2. Validate the event.
3. Assess operational impact.
4. Protect personnel and safety.
5. Contain the incident where appropriate.
6. Preserve evidence.
7. Recover systems.
8. Verify normal operation.
9. Document lessons learned.

Incident-response decisions should be coordinated between cybersecurity, engineering, operations, and safety teams.

---

# 2.9 Change Management

Changes to ICS systems should be carefully controlled.

Examples include:

- Firmware updates.
- PLC logic changes.
- Firewall rule changes.
- HMI configuration changes.
- SCADA software updates.
- Network configuration changes.
- Security-policy changes.

A controlled change process should include:

- Change request.
- Risk assessment.
- Testing.
- Approval.
- Maintenance window.
- Implementation.
- Verification.
- Documentation.
- Rollback plan.

---

# 2.10 Remote Access

Remote access can introduce significant risk to ICS environments.

Remote access should therefore be:

- Authorized.
- Restricted.
- Monitored.
- Time-limited where appropriate.
- Protected with strong authentication.
- Routed through controlled access points.

Organizations should avoid unnecessary direct exposure of ICS systems to the Internet.

---

# Task 3 — ICS Security Example Scenario

## Utility Company SCADA Network

Consider a utility company operating a SCADA environment.

The company has:

- Corporate IT network.
- Engineering workstations.
- SCADA servers.
- HMIs.
- PLCs.
- Remote access systems.

A basic security architecture could be:

```text
                    Internet
                       |
                 Corporate IT
                       |
                    Firewall
                       |
              Industrial DMZ
                       |
                    Firewall
                       |
                SCADA Network
                 /           \
               HMI           SCADA
                \             /
                 \           /
                     PLC
                      |
               Field Devices
```

The industrial DMZ provides an additional security boundary between corporate systems and industrial systems.

Firewall rules should allow only required communications.

---

# Task 4 — Document ICS Security Takeaways

The major security takeaways identified during this laboratory are:

```text
1. Protect physical access to ICS equipment.

2. Separate enterprise IT networks from ICS/OT networks.

3. Use firewalls and controlled communication paths.

4. Maintain an inventory of critical ICS assets.

5. Carefully manage patches and firmware updates.

6. Test security changes before production deployment.

7. Use least privilege and controlled administrative access.

8. Protect remote access to industrial systems.

9. Maintain reliable backups of critical configurations.

10. Monitor security and operational events.

11. Maintain tested incident-response procedures.

12. Use formal change management for ICS modifications.

13. Protect legacy systems with compensating controls when necessary.

14. Consider safety and availability when implementing security controls.

15. Document security policies and procedures.
```

The detailed takeaways were also documented in:

`standards/ics-security-takeaways.md`

---

# Task 5 — Compare ICS Security and IT Security

ICS and IT environments share many cybersecurity principles, but their operational requirements can be significantly different.

---

## 5.1 ICS vs IT Comparison

| Feature | ICS Security | Traditional IT Security |
|---|---|---|
| Primary concern | Safety, availability, reliability and integrity | Confidentiality, integrity and availability |
| Real-time requirements | Often critical | Usually less operationally deterministic |
| Physical consequences | Potentially significant | Usually less direct |
| Legacy systems | Common | Also present but generally easier to replace |
| Patch management | Requires extensive testing and scheduling | Often faster and more flexible |
| System downtime | May affect physical processes | Usually affects business services |
| Change management | Highly controlled | Controlled but often more flexible |
| Network architecture | Strong segmentation is important | Segmentation is also important |
| Equipment lifetime | Often long | Usually shorter |
| Safety requirements | Often directly relevant | Usually less directly connected |
| Application control | Important for critical systems | Important for endpoints and servers |
| Remote access | Requires strict control | Also requires strong control |
| Monitoring | Must avoid affecting operations | Generally easier to deploy |
| Recovery | Must consider process safety | Primarily focuses on service recovery |

---

# 5.2 Real-Time Processing

ICS environments may require predictable and timely communication.

For example:

```text
Sensor
   |
PLC
   |
Control Logic
   |
Actuator
```

A delay or interruption may affect an industrial process.

Therefore, security controls should be evaluated for their potential operational impact.

---

# 5.3 Legacy Systems

ICS environments frequently contain older systems because industrial equipment may remain operational for many years.

Traditional IT environments often have shorter hardware and software replacement cycles.

This means ICS security teams may need to use compensating controls when direct patching or replacement is not immediately possible.

---

# 5.4 Physical Security

Physical security can be especially important in ICS environments because industrial equipment may directly control physical processes.

Examples include:

- Pumps.
- Motors.
- Valves.
- Electrical equipment.
- Industrial machinery.

Unauthorized physical access can therefore create both cybersecurity and operational risks.

---

# 5.5 Availability

Availability is extremely important in many ICS environments.

Unexpected downtime may result in:

- Production loss.
- Service interruption.
- Equipment problems.
- Safety concerns.
- Financial losses.

Security controls should therefore be tested to ensure that they do not unintentionally disrupt critical operations.

---

# Task 6 — Standards Documentation

The laboratory produced three standards-review documents.

## NIST SP 800-82 Review

File:

`standards/nist-sp-800-82-review.md`

Purpose:

- Summarize NIST SP 800-82.
- Identify ICS security concepts.
- Document ICS-specific risks.
- Explain major security principles.

---

## ICS Security Takeaways

File:

`standards/ics-security-takeaways.md`

Purpose:

- Document practical ICS security recommendations.
- Identify important security controls.
- Summarize operational considerations.

---

## ICS vs IT Comparison

File:

`standards/ics-vs-it.md`

Purpose:

- Compare ICS security requirements with traditional IT security.
- Document differences in availability, safety, legacy systems, patching, and physical security.

---

# Evidence

The laboratory verification information was saved in:

`evidence/lab32-verification.txt`

The evidence directory contains documentation supporting the laboratory activities.

---

# Evidence Structure

```text
Lab-32-Introduction-to-ICS-Security-Standards/
|
├── README.md
|
├── standards/
│   ├── nist-sp-800-82-review.md
│   ├── ics-security-takeaways.md
│   └── ics-vs-it.md
|
└── evidence/
    └── lab32-verification.txt
```

---

# Verification

The laboratory files were verified using Linux commands.

Example:

```bash
pwd
```

The laboratory directory was confirmed as:

```text
/home/ubuntu/SCADA-ICS-Security-101/Lab-32-Introduction-to-ICS-Security-Standards
```

The directory structure was verified using:

```bash
find . -maxdepth 2 -type d -print | sort
```

Expected structure:

```text
.
./evidence
./standards
```

---

# Documentation Verification

The Markdown files were created using:

```bash
nano standards/nist-sp-800-82-review.md
nano standards/ics-security-takeaways.md
nano standards/ics-vs-it.md
```

The verification evidence was created using:

```bash
nano evidence/lab32-verification.txt
```

The main laboratory documentation was created using:

```bash
nano README.md
```

---

# ICS Security Findings

| Security Area | Result |
|---|---|
| NIST SP 800-82 reviewed | PASS |
| ICS security risks identified | PASS |
| Physical security documented | PASS |
| Network segmentation documented | PASS |
| Patch management documented | PASS |
| Access control documented | PASS |
| Application control documented | PASS |
| Monitoring documented | PASS |
| Backup and recovery documented | PASS |
| Incident response documented | PASS |
| Change management documented | PASS |
| Legacy ICS risks documented | PASS |
| ICS vs IT comparison completed | PASS |
| Evidence collected | PASS |
| AWS limitations documented | PASS |

---

# Key Lessons Learned

The most important lessons from this laboratory are:

### Lesson 1 — ICS Security Is Different

ICS security must consider safety, availability, reliability, and operational continuity in addition to traditional cybersecurity goals.

### Lesson 2 — Segmentation Is Important

Industrial networks should be separated from enterprise networks using appropriate security boundaries.

### Lesson 3 — Patching Requires Planning

ICS systems should not necessarily be patched in the same way as ordinary IT systems.

Testing, vendor requirements, maintenance windows, and recovery procedures must be considered.

### Lesson 4 — Physical Security Matters

Cybersecurity protections can be weakened if unauthorized personnel have physical access to industrial equipment.

### Lesson 5 — Legacy Systems Create Challenges

Older ICS systems may not support modern security technologies and may require compensating controls.

### Lesson 6 — Change Management Is Critical

Security changes should be documented, tested, approved, implemented, and verified.

### Lesson 7 — Safety Must Be Considered

Cybersecurity actions must not unintentionally create unsafe industrial conditions.

---

# AWS Laboratory Limitation

This laboratory was completed in an AWS EC2 Ubuntu environment.

The AWS environment did not provide a real industrial control system.

The following were not available:

- Physical PLCs.
- Physical RTUs.
- Industrial HMIs.
- Physical SCADA servers.
- Industrial sensors.
- Industrial actuators.
- Control cabinets.
- Industrial switches.
- Real industrial processes.
- Production safety systems.

Therefore, this laboratory focused on:

- Standards review.
- Security documentation.
- Architecture understanding.
- Risk identification.
- ICS vs IT comparison.

No real industrial control process was modified.

---

# Professional ICS Security Relevance

The concepts reviewed in this laboratory are relevant to cybersecurity roles involving:

- ICS security.
- SCADA security.
- OT security.
- Industrial network security.
- Critical infrastructure security.
- Security engineering.
- Risk assessment.
- Security architecture.
- Incident response.
- Vulnerability management.

Understanding standards such as NIST SP 800-82 helps security professionals design protections that are appropriate for operational technology environments.

---

# Lab Completion Checklist

- [x] Lab directory created.
- [x] Evidence directory created.
- [x] Standards directory created.
- [x] NIST SP 800-82 review completed.
- [x] ICS security risks documented.
- [x] Physical security documented.
- [x] Network segmentation documented.
- [x] Patch management documented.
- [x] Access control documented.
- [x] Application control documented.
- [x] Monitoring and logging documented.
- [x] Backup and recovery documented.
- [x] Incident response documented.
- [x] Change management documented.
- [x] Legacy system risks documented.
- [x] ICS vs IT comparison completed.
- [x] Evidence collected.
- [x] AWS limitations documented.
- [x] README completed.

---

# Final Assessment

**LAB 32 — COMPLETE**

This laboratory successfully introduced the fundamentals of ICS security standards and reviewed major concepts from NIST SP 800-82.

The exercise demonstrated that ICS cybersecurity requires a security approach that considers both cyber risks and physical/operational consequences.

The laboratory also demonstrated important differences between ICS and traditional IT security, particularly regarding:

- Safety.
- Availability.
- Reliability.
- Real-time operation.
- Legacy systems.
- Patch management.
- Physical security.
- Change management.

The documentation created during this exercise provides a foundation for understanding how cybersecurity standards can be applied to industrial environments.

---

# Conclusion

ICS security requires more than simply applying traditional IT security controls to industrial systems.

Industrial environments have unique operational requirements and may contain legacy technologies, specialized protocols, long-lived equipment, and systems that directly interact with physical processes.

NIST SP 800-82 provides useful guidance for understanding these challenges and developing appropriate security strategies.

The major security principles identified in this laboratory include:

- Protect critical ICS assets.
- Control physical access.
- Segment IT and OT networks.
- Restrict unnecessary communication.
- Control administrative access.
- Carefully manage patches.
- Protect legacy systems.
- Monitor security events.
- Maintain reliable backups.
- Prepare for incidents.
- Follow formal change management.
- Consider safety and availability when implementing security controls.

This laboratory therefore provides a foundational understanding of ICS security standards and their importance in protecting industrial and critical-infrastructure environments.

**LAB 32 — SUCCESSFULLY COMPLETED**
