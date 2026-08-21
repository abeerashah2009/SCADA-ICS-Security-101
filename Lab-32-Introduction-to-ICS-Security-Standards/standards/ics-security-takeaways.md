# Major ICS Security Takeaways

## 1. Protect Physical Access

Critical ICS equipment should be physically protected.

Examples include:

- Locked control cabinets
- Restricted control rooms
- Visitor controls
- Security monitoring
- Protection of engineering workstations

Physical access can allow an attacker to bypass some logical security controls.

---

## 2. Segment Industrial Networks

ICS networks should be separated from enterprise networks where appropriate.

Recommended controls may include:

- Firewalls
- Industrial DMZs
- VLANs
- Access control lists
- Controlled communication paths

Segmentation reduces unnecessary exposure and limits lateral movement.

---

## 3. Control Remote Access

Remote access to ICS systems should be tightly controlled.

Security measures may include:

- Strong authentication
- Multi-factor authentication where supported
- Least privilege
- Approved remote-access gateways
- Session monitoring
- Time-limited access

---

## 4. Manage Patches Carefully

ICS patching requires planning.

Before applying a patch:

1. Identify the affected system.
2. Check vendor information.
3. Test the patch.
4. Verify compatibility.
5. Create a backup.
6. Schedule maintenance.
7. Apply the patch.
8. Verify system operation.

---

## 5. Maintain Backups

Critical ICS configurations should be backed up.

Examples:

- PLC programs
- HMI configurations
- SCADA configurations
- Network configurations
- Engineering workstation data

Backups should be protected and periodically tested.

---

## 6. Monitor ICS Activity

Organizations should monitor:

- Authentication
- Configuration changes
- Network traffic
- Security events
- Unauthorized access
- Industrial protocol activity

Monitoring can help identify abnormal activity.

---

## 7. Prepare for Incidents

ICS incident response plans should consider safety and operational availability.

Response procedures should be tested before an actual incident occurs.

---

## 8. Protect Legacy Systems

Legacy systems may have:

- Unsupported operating systems
- Old applications
- Limited security features
- Difficult patching requirements

Additional controls may therefore be required, such as:

- Network isolation
- Application control
- Access restrictions
- Monitoring
- Compensating controls

---

## 9. Apply Least Privilege

Users and systems should receive only the permissions required to perform their tasks.

This reduces the potential impact of compromised accounts.

---

## 10. Follow Change Management

Security changes to ICS systems should follow an approved change-management process.

Changes should be:

- Documented
- Reviewed
- Tested
- Approved
- Scheduled
- Verified
- Reversible where practical

---

# Summary

The major ICS security priorities identified during this lab are:

1. Physical security
2. Network segmentation
3. Access control
4. Remote-access security
5. Patch management
6. Backup and recovery
7. Monitoring and logging
8. Incident response
9. Legacy-system protection
10. Change management
ubuntu@ip-172-31-10-48:~/SCADA-ICS-Security-101$ cd ~/SCADA-ICS-Security-101/Lab-32-Introduction-to-ICS-Security-Standards

echo "===== README ====="
head -30 README.md

echo
echo "===== NIST REVIEW ====="
head -30 standards/nist-sp-800-82-review.md

echo
echo "===== ICS SECURITY TAKEAWAYS ====="
cat standards/ics-security-takeaways.md

echo
echo "===== ICS VS IT ====="
cat standards/ics-vs-it.md

echo
echo "===== VERIFICATION ====="
cat evidence/lab32-verification.txt
===== README =====
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

===== NIST REVIEW =====
# NIST SP 800-82 Review

## Document Reviewed

**Document:** NIST Special Publication 800-82 Revision 2
**Title:** Guide to Industrial Control Systems (ICS) Security
**Organization:** National Institute of Standards and Technology (NIST)

---

## 1. Purpose of NIST SP 800-82

NIST SP 800-82 provides guidance for improving the security of Industrial Control Systems (ICS).

The document addresses systems such as:

- Supervisory Control and Data Acquisition (SCADA)
- Distributed Control Systems (DCS)
- Programmable Logic Controllers (PLC)
- Industrial automation systems
- Other operational technology environments

The main purpose is to help organizations understand and manage cybersecurity risks while maintaining the safety, reliability, availability, and performance requirements of industrial systems.

---

## 2. Why ICS Security Is Different

ICS environments differ from traditional information technology environments.


===== ICS SECURITY TAKEAWAYS =====
# Major ICS Security Takeaways

## 1. Protect Physical Access

Critical ICS equipment should be physically protected.

Examples include:

- Locked control cabinets
- Restricted control rooms
- Visitor controls
- Security monitoring
- Protection of engineering workstations

Physical access can allow an attacker to bypass some logical security controls.

---

## 2. Segment Industrial Networks

ICS networks should be separated from enterprise networks where appropriate.

Recommended controls may include:

- Firewalls
- Industrial DMZs
- VLANs
- Access control lists
- Controlled communication paths

Segmentation reduces unnecessary exposure and limits lateral movement.

---

## 3. Control Remote Access

Remote access to ICS systems should be tightly controlled.

Security measures may include:

- Strong authentication
- Multi-factor authentication where supported
- Least privilege
- Approved remote-access gateways
- Session monitoring
- Time-limited access

---

## 4. Manage Patches Carefully

ICS patching requires planning.

Before applying a patch:

1. Identify the affected system.
2. Check vendor information.
3. Test the patch.
4. Verify compatibility.
5. Create a backup.
6. Schedule maintenance.
7. Apply the patch.
8. Verify system operation.

---

## 5. Maintain Backups

Critical ICS configurations should be backed up.

Examples:

- PLC programs
- HMI configurations
- SCADA configurations
- Network configurations
- Engineering workstation data

Backups should be protected and periodically tested.

---

## 6. Monitor ICS Activity

Organizations should monitor:

- Authentication
- Configuration changes
- Network traffic
- Security events
- Unauthorized access
- Industrial protocol activity

Monitoring can help identify abnormal activity.

---

## 7. Prepare for Incidents

ICS incident response plans should consider safety and operational availability.

Response procedures should be tested before an actual incident occurs.

---

## 8. Protect Legacy Systems

Legacy systems may have:

- Unsupported operating systems
- Old applications
- Limited security features
- Difficult patching requirements

Additional controls may therefore be required, such as:

- Network isolation
- Application control
- Access restrictions
- Monitoring
- Compensating controls

---

## 9. Apply Least Privilege

Users and systems should receive only the permissions required to perform their tasks.

This reduces the potential impact of compromised accounts.

---

## 10. Follow Change Management

Security changes to ICS systems should follow an approved change-management process.

Changes should be:

- Documented
- Reviewed
- Tested
- Approved
- Scheduled
- Verified
- Reversible where practical

---

# Summary

The major ICS security priorities identified during this lab are:

1. Physical security
2. Network segmentation
3. Access control
4. Remote-access security
5. Patch management
6. Backup and recovery
7. Monitoring and logging
8. Incident response
9. Legacy-system protection
10. Change management

===== ICS VS IT =====
# ICS Security vs IT Security

## Comparison

| Feature | ICS Security | IT Security |
|---|---|---|
| Primary Environment | Industrial and operational systems | Business and information systems |
| Main Examples | SCADA, PLC, HMI, RTU, DCS | Servers, laptops, databases, cloud systems |
| Availability | Extremely important | Very important |
| Safety | Often directly affected | Usually indirect |
| Real-Time Requirements | Often critical | Usually less time-sensitive |
| Legacy Systems | Common | Less dominant |
| Patch Management | Requires extensive testing | Generally more flexible |
| System Shutdown | May be unsafe or operationally unacceptable | Often more manageable |
| Physical Security | Highly important | Important |
| Network Segmentation | Strongly emphasized | Important |
| Remote Access | Requires strict control | Requires strict control |
| Change Management | Highly important | Important |
| Incident Response | Must consider safety and process stability | Primarily focuses on information and service protection |
| Security Priority | Safety, availability, reliability, integrity | Confidentiality, integrity, availability |
| Industrial Protocols | Common | Less common |
| Specialized Equipment | PLCs, RTUs, HMIs, sensors | Servers, workstations, network devices |
| Maintenance Windows | Often limited | Usually more flexible |
| Security Testing | Must avoid disrupting operations | Generally easier to perform |
| Recovery Requirements | Process and safety recovery | Data and service recovery |

---

# Key Differences

## 1. Safety

ICS environments can directly control physical processes.

A security failure may therefore cause:

- Equipment damage
- Production disruption
- Environmental impact
- Safety incidents

IT systems generally have less direct interaction with physical processes.

---

## 2. Availability

Industrial systems may need to operate continuously.

Taking an ICS component offline for security maintenance may not always be possible.

---

## 3. Real-Time Operation

Many ICS environments require predictable and timely communication.

Security controls must therefore be designed without introducing unacceptable delays or instability.

---

## 4. Legacy Systems

ICS environments frequently contain systems that were designed before modern cybersecurity requirements became common.

These systems may be difficult to:

- Patch
- Upgrade
- Replace
- Monitor

---

## 5. Patch Management

IT systems can often be patched more frequently.

ICS patching may require:

- Vendor approval
- Testing
- Maintenance windows
- Backups
- Change approval
- Operational validation

---

## 6. Physical Security

Physical security is particularly important for ICS because industrial equipment may be located in:

- Control rooms
- Plants
- Substations
- Pump stations
- Manufacturing facilities
- Remote field locations

---

## 7. Security Priorities

Traditional IT security often emphasizes:

1. Confidentiality
2. Integrity
3. Availability

ICS security must strongly consider:

1. Safety
2. Availability
3. Reliability
4. Integrity
5. Confidentiality

The exact priority depends on the industrial environment and risk assessment.

---

# Conclusion

ICS security and IT security share many security principles, including authentication, access control, monitoring, segmentation, incident response, and risk management.

However, ICS environments require additional consideration of safety, real-time operation, availability, reliability, physical processes, legacy systems, and specialized equipment.

Therefore, IT security controls should not simply be copied into an ICS environment without evaluating their operational impact.

===== VERIFICATION =====
LAB 32 — ICS SECURITY STANDARDS VERIFICATION

Environment:
AWS EC2 Ubuntu Linux

Security Standard Reviewed:
NIST SP 800-82 Revision 2

Topics Reviewed:
- ICS security fundamentals
- ICS-specific risks
- Network segmentation
- Access control
- Patch management
- Malware protection
- Monitoring and logging
- Incident response
- Backup and recovery
- Physical security
- Legacy systems
- Change management

Documents Created:

1. standards/nist-sp-800-82-review.md
   Purpose:
   Documents the NIST SP 800-82 review and major ICS security concepts.

2. standards/ics-security-takeaways.md
   Purpose:
   Documents the major security recommendations identified during the review.

3. standards/ics-vs-it.md
   Purpose:
   Compares ICS security requirements with traditional IT security.

Laboratory Limitation:

This was a documentation and standards-review exercise performed in an AWS environment.

No physical PLC, RTU, HMI, SCADA server, industrial network, or real industrial process was available.

No production ICS system was modified.

LAB 32 STATUS: COMPLETE
ubuntu@ip-172-31-10-48:~/SCADA-ICS-Security-101/Lab-32-Introduction-to-ICS-Security-Standards$
