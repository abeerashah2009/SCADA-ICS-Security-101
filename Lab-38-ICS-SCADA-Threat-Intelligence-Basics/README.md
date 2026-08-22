# Lab 38: ICS/SCADA Threat Intelligence Basics

## Overview

This lab demonstrates the fundamentals of collecting, analyzing, and applying threat intelligence to an ICS/SCADA environment.

The exercise focuses on:

* Identifying trusted ICS threat-intelligence sources.
* Reviewing vendor and government security advisories.
* Comparing published vulnerabilities against the actual laboratory environment.
* Performing threat impact analysis.
* Integrating threat intelligence into an incident-response procedure.
* Documenting defensive actions and security improvements.

The laboratory uses an Ubuntu 24.04-based system for ICS/SCADA security training.

---

## Objectives

The objectives of this lab are to:

1. Understand ICS/SCADA threat intelligence.
2. Identify reliable ICS security advisory sources.
3. Analyze current ICS vulnerabilities and threats.
4. Compare threats against the laboratory asset inventory.
5. Determine vulnerability applicability.
6. Identify appropriate security controls.
7. Integrate threat intelligence into incident response.
8. Document detection, containment, eradication, and recovery procedures.

---

## Laboratory Environment

The laboratory was evaluated before performing the threat-intelligence analysis.

The baseline captured:

* Host information
* Operating system
* Kernel version
* Network interfaces
* Listening services
* Running services
* Installed software
* Security-relevant packages

### Security-Relevant Software

The environment contains security-related components including:

* AppArmor
* OpenVPN
* OpenSSH
* UFW
* rsyslog

A complete software inventory was also captured for future vulnerability-to-asset comparison.

---

## Directory Structure

```text
Lab-38-ICS-SCADA-Threat-Intelligence-Basics/
│
├── README.md
│
├── evidence/
│   ├── lab-environment-baseline.txt
│   ├── software-inventory.txt
│   └── software-inventory-summary.txt
│
├── threat-intelligence/
│   └── siemens-advisory-analysis.txt
│
├── analysis/
│   └── threat-to-lab-mapping.txt
│
├── incident-response/
│   └── threat-intelligence-response-procedure.txt
│
└── scripts/
```

---

# Task 1: Identify Sources of ICS Threat Intelligence

## 1.1 Siemens ProductCERT

A Siemens ProductCERT advisory was selected for analysis:

**Advisory:** SSA-688146

**Title:** Multiple Cross-Site Scripting Vulnerabilities in SIMATIC S7 PLCs Web Server

The advisory was analyzed to identify:

* Affected technology
* Vulnerability type
* CVE identifiers
* Severity
* Potential security impact
* Vendor remediation recommendations

The selected advisory includes the following CVEs:

```text
CVE-2026-25786
CVE-2026-25787
CVE-2026-25789
```

The analysis highlighted the importance of:

* Restricting industrial management interfaces.
* Protecting firmware-update privileges.
* Limiting administrative access.
* Applying vendor-recommended security updates.
* Following industrial security guidance.

---

## 1.2 CISA ICS Advisory

A CISA ICS advisory was also reviewed:

**Advisory:** ICSA-25-021-02

**Technology:** Siemens SIMATIC S7-1200 CPUs

**Vulnerability:** Cross-Site Request Forgery (CSRF)

The advisory demonstrates how an attacker could potentially abuse authenticated user interaction to affect the operating state of an industrial controller.

The analysis emphasized:

* Keeping affected products updated.
* Protecting industrial devices from unnecessary network exposure.
* Using appropriate ICS network-security controls.
* Restricting administrative privileges.

---

## Threat-Intelligence Sources

The laboratory analysis used trusted sources including:

* CISA ICS Advisories
* Siemens ProductCERT Security Advisories
* Siemens Industrial Security guidance

These sources provide information that can be used to monitor emerging ICS vulnerabilities and determine whether they apply to an organization's assets.

---

# Task 2: Compare Threats Against the Lab Environment

## Lab Asset Assessment

The current laboratory is an Ubuntu 24.04-based security-training environment.

Observed components include:

* Ubuntu operating system
* OpenSSH
* OpenVPN
* UFW
* AppArmor
* rsyslog
* Network services
* Administrative remote-access services

The laboratory **does not contain a physical Siemens SIMATIC S7 PLC or S7-1200 CPU**.

Therefore, the selected Siemens vulnerabilities are treated as threat-intelligence research and are **not confirmed vulnerabilities on the current Ubuntu host**.

---

## Threat Applicability

The following threats were mapped against the laboratory:

| Threat         | Affected Technology               | Lab Component   | Applicability           |
| -------------- | --------------------------------- | --------------- | ----------------------- |
| SSA-688146 XSS | Siemens SIMATIC S7 PLC web server | No Siemens PLC  | Not directly applicable |
| CVE-2026-25786 | Siemens SIMATIC S7 web server     | No affected PLC | Not directly applicable |
| CVE-2026-25787 | Siemens SIMATIC S7 web server     | No affected PLC | Not directly applicable |
| CVE-2026-25789 | Siemens SIMATIC S7 web server     | No affected PLC | Not directly applicable |
| ICSA-25-021-02 | Siemens S7-1200 CPU               | No S7-1200      | Not directly applicable |

---

## Applicability Assessment Method

A published vulnerability should not automatically be considered applicable.

The following questions should be answered:

1. Is the affected product present?
2. Is the affected version present?
3. Is the vulnerable service enabled?
4. Is the device reachable through the relevant attack path?
5. Are compensating security controls available?
6. What remediation does the vendor recommend?

This approach prevents false vulnerability assumptions and improves the accuracy of threat assessments.

---

# Impact Analysis

If a comparable vulnerability existed on an actual ICS PLC web interface, exploitation could potentially affect the integrity of the control environment.

Possible consequences could include:

* Unauthorized configuration changes.
* Unauthorized administrative actions.
* Changes to device operating state.
* Loss of confidence in system integrity.
* Disruption of monitoring or control operations.
* Potential operational or safety consequences.

### Current Laboratory Impact

**Assessment: LOW / NOT DIRECTLY APPLICABLE**

The selected Siemens products are not present in the current laboratory.

The findings are therefore treated as threat intelligence rather than evidence of an active vulnerability.

---

# Security Control Mapping

The threat intelligence was converted into practical security controls.

## 1. Network Segmentation

* Separate ICS management networks from untrusted networks.
* Avoid unnecessary Internet exposure.
* Restrict access to industrial management interfaces.

## 2. Access Control

* Restrict administrative access.
* Apply least privilege.
* Protect privileged credentials.
* Limit firmware and configuration permissions.

## 3. Patch Management

* Monitor vendor advisories.
* Maintain accurate software and firmware inventories.
* Verify affected versions.
* Apply vendor-approved updates during maintenance windows.

## 4. Remote Access Security

* Use secure remote-access mechanisms.
* Restrict management interfaces.
* Monitor administrative sessions.
* Control remote maintenance activities.

## 5. Change Control

* Require authorization before configuration or firmware changes.
* Maintain backups before updates.
* Maintain documented rollback procedures.
* Record administrative activity.

## 6. Monitoring

* Monitor system and security logs.
* Detect unexpected configuration changes.
* Investigate suspicious administrative activity.
* Preserve evidence for incident response.

---

# Task 3: Integrate Threat Intelligence Into Incident Response

A dedicated incident-response procedure was created based on the selected Siemens threat intelligence.

The procedure covers the complete incident-response lifecycle.

## Preparation

Maintain current information about:

* PLCs
* HMIs
* SCADA servers
* Historians
* Engineering workstations
* Network devices
* Remote-access systems
* Software and firmware versions

Supporting documentation should include:

* Network diagrams
* Configuration backups
* Incident-response contacts
* Vendor advisory subscriptions
* Maintenance procedures
* Recovery procedures

---

## Detection and Analysis

Monitor for:

* Unexpected PLC configuration changes.
* Unexpected firmware-update activity.
* Unauthorized administrative access.
* Suspicious web-interface activity.
* Unexpected CPU operating-mode changes.
* Authentication anomalies.
* Unexpected network connections.
* Suspicious user interaction involving management interfaces.

When suspicious activity occurs:

1. Record the date and time.
2. Identify the affected asset.
3. Record product and firmware information.
4. Compare the asset against vendor advisories.
5. Preserve relevant logs.
6. Determine whether the vulnerability is applicable.

---

## Containment

If an affected industrial device is confirmed:

* Restrict unnecessary network access.
* Isolate the affected management interface where operationally safe.
* Restrict administrative accounts.
* Stop unauthorized update activity.
* Maintain required control-system availability.
* Preserve logs and evidence.

Containment actions must not create unsafe industrial-process conditions.

---

## Eradication

Follow the affected vendor's official remediation guidance.

Possible actions include:

* Applying vendor-recommended firmware updates.
* Applying software patches.
* Removing unauthorized configuration changes.
* Disabling unnecessary services.
* Restricting management interfaces.
* Resetting compromised credentials where appropriate.
* Restoring an approved system configuration.

All updates should follow an approved change-control process.

---

## Recovery

After remediation:

1. Restore approved configurations where required.
2. Restart affected services in a controlled sequence.
3. Verify PLC communications.
4. Verify SCADA monitoring.
5. Verify alarms.
6. Verify historian/data collection.
7. Verify network connectivity.
8. Review system logs.
9. Monitor for abnormal behavior.
10. Obtain operational approval before returning to normal service.

---

## Post-Incident Review

Document:

* Threat-intelligence source.
* Affected asset.
* Vulnerability and CVE information.
* Detection method.
* Containment actions.
* Remediation performed.
* Recovery results.
* Evidence collected.
* Lessons learned.

Security controls and incident-response procedures should be updated based on the findings.

---

# Threat Intelligence Integration Workflow

```text
Threat Intelligence
        |
        v
Asset Identification
        |
        v
Applicability Assessment
        |
        v
Detection / Monitoring
        |
        v
Incident Analysis
        |
        v
Containment
        |
        v
Remediation
        |
        v
Recovery
        |
        v
Lessons Learned
        |
        +------> Updated Threat Intelligence Monitoring
```

---

# Evidence Collected

The following evidence was created during the laboratory:

### Environment Evidence

```text
evidence/lab-environment-baseline.txt
```

Contains:

* Host information
* OS information
* Kernel information
* Network configuration
* Listening services
* Running services

### Software Inventory

```text
evidence/software-inventory.txt
```

Contains the installed package inventory.

```text
evidence/software-inventory-summary.txt
```

Contains:

* Package count
* Security-relevant packages
* Installed versions

The captured package inventory contained **1732 packages**.

---

# Threat Intelligence Evidence

```text
threat-intelligence/siemens-advisory-analysis.txt
```

Contains:

* Siemens ProductCERT advisory analysis
* CISA advisory analysis
* CVE information
* Risk assessment
* Vendor remediation guidance
* Threat-intelligence sources
* Lab relevance assessment

---

# Threat Mapping Evidence

```text
analysis/threat-to-lab-mapping.txt
```

Contains:

* Lab component identification
* Threat-to-asset mapping
* Applicability assessment
* Security-control mapping
* Impact analysis
* Recommended defensive controls

---

# Incident Response Evidence

```text
incident-response/threat-intelligence-response-procedure.txt
```

Contains the simulated response procedure covering:

* Preparation
* Detection and analysis
* Containment
* Eradication
* Recovery
* Post-incident review
* Threat-intelligence integration
* Incident-response improvements

---

# Validation Commands

The following commands can be used to verify the laboratory evidence:

```bash
# Check environment evidence
wc -l evidence/lab-environment-baseline.txt

# Check software inventory
wc -l evidence/software-inventory.txt
cat evidence/software-inventory-summary.txt

# Verify Siemens advisory identifiers
grep -Ei "SSA-688146|CVE-2026-25786|CVE-2026-25787|CVE-2026-25789|ICSA-25-021-02" \
threat-intelligence/siemens-advisory-analysis.txt

# Verify threat mapping
grep -Ei "NOT DIRECTLY APPLICABLE|IMPACT ANALYSIS|NETWORK SEGMENTATION|PATCH MANAGEMENT|CONCLUSION" \
analysis/threat-to-lab-mapping.txt

# Verify incident-response phases
grep -Ei "PREPARATION|DETECTION|CONTAINMENT|ERADICATION|RECOVERY|POST-INCIDENT|FINAL ASSESSMENT" \
incident-response/threat-intelligence-response-procedure.txt

# Review all lab files
find . -maxdepth 3 -type f -print | sort
```

---

# Key Lessons Learned

This lab demonstrates that threat intelligence is most useful when it is connected to real assets and operational procedures.

Key lessons include:

* Use trusted ICS security sources.
* Maintain an accurate asset inventory.
* Compare vulnerabilities against actual products and versions.
* Do not assume every published vulnerability affects the environment.
* Apply least privilege.
* Restrict industrial management interfaces.
* Monitor configuration and administrative activity.
* Maintain tested backups and recovery procedures.
* Integrate threat intelligence into incident response.
* Follow vendor remediation guidance.
* Document security decisions for future audits.

---

# Final Assessment

**Lab Status: Completed**

The laboratory successfully demonstrated:

* ICS/SCADA environment baseline collection.
* Software inventory collection.
* Threat-intelligence source identification.
* Siemens vulnerability analysis.
* CISA advisory analysis.
* Threat-to-lab mapping.
* Vulnerability applicability assessment.
* Impact analysis.
* Security-control mapping.
* Incident-response integration.
* Detection, containment, eradication, and recovery planning.

The selected Siemens vulnerabilities were correctly identified as **not directly applicable** to the current Ubuntu laboratory because the affected Siemens PLC products are not present.

The exercise therefore demonstrates the correct professional approach: **collect intelligence → identify affected assets → determine applicability → define controls → integrate the findings into incident response.**

---

## Conclusion

ICS/SCADA threat intelligence provides security teams with information about emerging vulnerabilities, attack techniques, and vendor-recommended mitigations.

The most important step is not simply finding a vulnerability, but determining whether that vulnerability applies to the actual environment.

By combining threat intelligence with asset inventory, vulnerability assessment, security controls, monitoring, and incident response, ICS/SCADA teams can improve their ability to detect and respond to emerging threats while maintaining operational safety and system availability.
