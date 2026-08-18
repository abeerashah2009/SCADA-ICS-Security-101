# Lab 13 - Task 1: Understanding ICS/SCADA Threats

## Objective

Understand the difference between external and internal threats affecting
Industrial Control Systems (ICS) and Supervisory Control and Data Acquisition
(SCADA) environments.

---

# 1. External Threats

External threats originate outside an organization.

## Common External Threat Actors

- Cybercriminals
- Nation-state actors
- Hacktivists
- Competitors
- Organized threat groups
- External attackers

## Common External Attack Methods

- Phishing
- Spear-phishing
- Malware
- Exploitation of vulnerable services
- Credential theft
- Remote-access abuse
- Supply-chain compromise

## Potential Objectives

External attackers may attempt to:

- Steal sensitive information
- Obtain credentials
- Disrupt industrial operations
- Conduct espionage
- Extort organizations
- Sabotage critical infrastructure
- Achieve political or strategic objectives

---

# 2. Internal Threats

Internal threats originate from people or activities within an organization.

## Potential Internal Sources

- Employees
- Contractors
- Vendors
- Administrators
- Maintenance personnel
- Authorized users

Internal threats can be either malicious or accidental.

---

# 3. Malicious Insider

A malicious insider intentionally abuses legitimate access.

### Example

An employee with authorized access to an industrial environment deliberately
changes a configuration without authorization.

### Potential Impact

- Unauthorized configuration changes
- Data theft
- Process disruption
- Security-policy violations
- Operational downtime

---

# 4. Accidental Insider

An accidental insider does not intentionally cause harm.

### Example

An employee receives a convincing phishing email and opens a malicious
attachment.

The employee may unknowingly introduce malware into the organization's
environment.

### Potential Impact

- Malware infection
- Credential compromise
- Unauthorized access
- Network compromise
- Potential IT-to-OT security impact

---

# 5. External vs Internal Threat Comparison

| Characteristic | External Threat | Internal Threat |
|---|---|---|
| Origin | Outside organization | Inside organization |
| Example | Cybercriminal | Employee |
| Access | Usually must obtain access | May already have authorized access |
| Common Vector | Phishing, exploitation | Misuse, negligence |
| Motivation | Financial, political, espionage | Financial, personal, malicious or accidental |
| Detection | Network/security monitoring | User/activity monitoring |
| Potential Impact | Data theft or disruption | Data exposure or operational disruption |

---

# 6. Key Security Concept: Trusted Access

Authorized access does not automatically mean authorized activity.

An internal user may have legitimate access but could:

- Make unauthorized changes
- Accidentally expose information
- Introduce malware
- Misconfigure systems
- Violate security procedures

Therefore, ICS environments should use multiple security controls.

---

# 7. Recommended Defensive Controls

## Least Privilege

Users should receive only the permissions required to perform their jobs.

## Strong Authentication

Sensitive systems should use strong authentication and, where appropriate,
multi-factor authentication.

## Network Segmentation

IT and OT networks should be separated using appropriate architecture,
firewalls, and access controls.

## Monitoring

Organizations should monitor:

- Authentication activity
- Administrative actions
- Network connections
- Configuration changes
- Critical system events

## Security Awareness

Personnel should receive training on:

- Phishing
- Social engineering
- Password security
- Removable media risks
- Reporting suspicious activity

---

# 8. Threat Analysis

A simple ICS threat-analysis model is:

```text
WHO?
 |
 +-- External attacker
 |
 +-- Employee
 |
 +-- Contractor
 |
 +-- Nation-state
 |
 +-- Cybercriminal

HOW?
 |
 +-- Phishing
 +-- Malware
 +-- Exploitation
 +-- Credential compromise
 +-- Insider misuse

WHY?
 |
 +-- Financial gain
 +-- Espionage
 +-- Sabotage
 +-- Political objectives
 +-- Strategic advantage
Understanding who, how, and why helps defenders prioritize
appropriate security controls.

9. ICS-Specific Considerations

ICS environments require special attention because cyber incidents can affect
physical processes.

Potential consequences include:

Loss of visibility
Loss of control
Production interruption
Equipment damage
Safety risks
Service disruption

Therefore, ICS cybersecurity must protect both digital systems and the
physical processes they control.

10. Task 1 Findings
Finding 1

External attackers generally need to obtain access to the organization's
environment.

Finding 2

Internal users may already possess legitimate access, making access
management particularly important.

Finding 3

Internal threats are not always malicious. Human error can also introduce
significant security risks.

Finding 4

Defense-in-depth is necessary because no single control can completely
eliminate either external or internal threats.

11. Safety

This task involved only conceptual threat analysis.

[PASS] No real ICS system scanned
[PASS] No PLC accessed
[PASS] No SCADA system accessed
[PASS] No credentials attacked
[PASS] No malware deployed
[PASS] No production system tested
[PASS] Defensive analysis only
Task 1 Conclusion

External and internal threats can both seriously affect ICS/SCADA environments.

External threats may originate from cybercriminals, nation-state actors,
hacktivists, or other external groups.

Internal threats may originate from employees, contractors, administrators,
or accidental user actions.

Effective ICS security therefore requires:

Strong authentication
Least privilege
Network segmentation
Monitoring
Security awareness
Access control
Defense-in-depth
