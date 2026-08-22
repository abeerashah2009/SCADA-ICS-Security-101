# Lab 35: Introduction to ICS Forensics

## Overview

This laboratory introduces the fundamentals of **forensic investigation in Industrial Control System (ICS) environments**.

Unlike traditional IT systems, ICS environments operate critical physical processes where investigation activities must be carefully controlled to avoid disrupting PLCs, HMIs, SCADA servers, engineering workstations, historians, and industrial network communications.

In this lab, a controlled AWS EC2 Ubuntu environment was used to practice the collection, preservation, hashing, and documentation of forensic evidence.

The laboratory focuses on:

* ICS forensic imaging concepts
* Identification of important forensic data
* System and network evidence collection
* Log and configuration evidence
* Volatile system-state information
* Evidence integrity using SHA-256
* Chain-of-custody documentation
* Preservation of forensic artifacts
* ICS-specific operational considerations

---

## Objectives

The objectives of this laboratory are to:

1. Understand how forensic investigations differ in ICS environments.
2. Identify important system, network, and operational evidence.
3. Collect system-level forensic information using Linux tools.
4. Preserve collected evidence for further investigation.
5. Generate SHA-256 hashes to verify evidence integrity.
6. Document chain-of-custody requirements.
7. Understand the importance of minimizing operational impact during ICS investigations.
8. Build a repeatable forensic evidence collection workflow.

---

## Environment

| Component          | Details                          |
| ------------------ | -------------------------------- |
| Platform           | AWS EC2                          |
| Operating System   | Ubuntu 24.04.3 LTS               |
| Architecture       | x86_64                           |
| Kernel             | 6.14.0-1018-aws                  |
| Root Disk          | `/dev/nvme0n1p1`                 |
| Network Interface  | `ens5`                           |
| Loopback Interface | `lo`                             |
| Logging            | rsyslog / systemd journal        |
| Evidence Integrity | SHA-256                          |
| Collection Method  | Linux shell commands and scripts |

---

# Task 1 — Understanding ICS Forensic Imaging

## 1.1 ICS Forensic Imaging

Forensic imaging is the process of creating a reliable copy of digital information for investigation while preserving the original evidence.

ICS forensic imaging differs from traditional IT forensics because ICS systems are often:

* Operational 24/7
* Safety-critical
* Time-sensitive
* Connected to physical processes
* Dependent on legacy systems
* Sensitive to system changes
* Difficult to shut down for investigation

An investigator must therefore balance **evidence preservation** with **operational safety**.

A traditional IT system may be taken offline for imaging. In an ICS environment, shutting down a PLC, HMI, SCADA server, or engineering workstation could interrupt an industrial process.

Therefore, forensic acquisition should be as **non-intrusive as possible**.

---

## 1.2 Types of ICS Data

Important forensic information may include:

### Real-Time Process Data

Process information can help investigators determine what the industrial system was doing during an incident.

Examples include:

* Sensor readings
* Actuator states
* Process values
* Alarm conditions
* PLC states
* Control commands
* Historian records

### System Configuration

Configuration information can reveal how the ICS environment was operating.

Examples include:

* PLC configurations
* SCADA configurations
* HMI settings
* Network configurations
* Firewall rules
* Engineering workstation configurations
* User accounts
* Application settings

### Network Data

Network information can reveal communication between:

* PLCs
* HMIs
* SCADA servers
* Engineering workstations
* Historians
* Remote-access systems
* Security devices

---

# Task 2 — Identifying Important Forensic Data

## 2.1 System Information

The laboratory collected system information using:

```bash
./scripts/collect-forensic-evidence.sh
```

The collection script generated:

```text
evidence/system-info.txt
```

The collected information included:

* Date and time
* Hostname
* Operating system
* Kernel version
* System uptime
* Network interfaces
* Disk information
* Mounted filesystems
* Running services

This information establishes a baseline of the system at the time of evidence collection.

---

## 2.2 Network Evidence

Network information is important during ICS investigations because abnormal communication may indicate:

* Unauthorized access
* Malware activity
* Remote access
* Network scanning
* Unexpected services
* Suspicious connections
* Changes in network configuration

The laboratory collected:

```bash
ss -tulpen
```

and:

```bash
ip route
```

The evidence was stored in:

```text
evidence/forensic-system-state.txt
```

---

## 2.3 Process Evidence

Running processes were collected using:

```bash
ps aux --sort=-%cpu | head -30
```

Process information can help investigators identify:

* Unexpected applications
* Suspicious processes
* Resource-intensive programs
* Unauthorized software
* Abnormal system activity

---

## 2.4 User and Login Evidence

The laboratory collected current users using:

```bash
who
```

Login history was collected using:

```bash
last -n 10
```

This information can help investigators determine:

* Who was logged into the system
* Recent login activity
* Possible unauthorized access
* Unexpected sessions

---

## 2.5 Logging Evidence

System logging is an important source of forensic evidence.

The laboratory checked the rsyslog service using:

```bash
systemctl status rsyslog --no-pager
```

Recent system events were collected using:

```bash
journalctl -n 50 --no-pager
```

These logs may provide information about:

* Service activity
* Authentication events
* System changes
* Errors
* Network activity
* Unexpected events

---

# Task 3 — Automated Forensic Collection

## Collection Script

The laboratory created:

```text
scripts/collect-forensic-evidence.sh
```

The script automates the collection of basic system information.

It generated:

```text
evidence/system-info.txt
```

This provides a repeatable approach to collecting baseline information during an investigation.

### Example Execution

```bash
chmod +x scripts/collect-forensic-evidence.sh

./scripts/collect-forensic-evidence.sh
```

Expected result:

```text
Forensic system information collected: evidence/system-info.txt
```

---

# Task 4 — Forensic System State Collection

A broader forensic snapshot was collected using Linux system interrogation commands.

The following categories were captured:

```text
System Identity
Current Users
Login History
Network Connections
Routing Table
DNS Configuration
Running Processes
Systemd Services
rsyslog Status
Recent Journal Events
```

The resulting evidence file was:

```text
evidence/forensic-system-state.txt
```

This provides a snapshot of the system's state at the time of collection.

---

# Task 5 — Chain of Custody

## 5.1 Chain-of-Custody Principles

Chain of custody is the documentation of how evidence is:

1. Collected
2. Identified
3. Preserved
4. Transferred
5. Accessed
6. Analyzed
7. Stored

The purpose is to demonstrate that evidence was not improperly altered or replaced.

For an ICS investigation, documentation is particularly important because investigators may need to explain why specific systems were accessed or why certain collection techniques were used.

---

## 5.2 Chain-of-Custody Record

The laboratory created:

```text
evidence/chain-of-custody.txt
```

Case identifier:

```text
LAB35-ICS-FORENSICS-001
```

Evidence source:

```text
AWS EC2 Ubuntu 24.04.3 LTS laboratory system
```

The record documents:

* Collection date
* Collection host
* Collector
* Evidence items
* Collection method
* Integrity method
* Evidence handling requirements
* Operational considerations

---

# Task 6 — Evidence Integrity

Cryptographic hashing was used to verify evidence integrity.

SHA-256 hashes were generated using:

```bash
sha256sum \
evidence/system-info.txt \
evidence/forensic-system-state.txt \
evidence/chain-of-custody.txt \
> evidence/evidence-sha256.txt
```

The resulting hash file was:

```text
evidence/evidence-sha256.txt
```

---

## Integrity Verification

The evidence was verified using:

```bash
sha256sum -c evidence/evidence-sha256.txt
```

The verification produced:

```text
evidence/system-info.txt: OK
evidence/forensic-system-state.txt: OK
evidence/chain-of-custody.txt: OK
```

This confirms that the files matched their recorded SHA-256 hashes at verification time.

---

# Task 7 — Evidence Summary

A consolidated evidence summary was created:

```text
forensics/evidence-summary.txt
```

The summary identifies the major artifacts collected during the exercise.

### Primary Evidence

```text
System identification
Hostname and operating system information
Kernel information
System uptime
Network interfaces
Disk and filesystem information
Mounted filesystems
Running services
Current users
Login history
Network sockets
Routing table
DNS configuration
Running processes
rsyslog status
Recent journal events
```

---

# ICS Forensic Evidence Sources

In a real ICS environment, investigators may need to examine evidence from multiple components.

### PLCs

Potential evidence:

* PLC configuration
* Program logic
* Firmware information
* Diagnostic information
* Event logs
* Operational state

### HMI Systems

Potential evidence:

* Operator activity
* Alarm history
* Application logs
* User activity
* Configuration files

### SCADA Servers

Potential evidence:

* SCADA application logs
* User authentication
* Database activity
* Alarm records
* Configuration files
* Service activity

### Engineering Workstations

Potential evidence:

* Project files
* PLC programming software
* User activity
* Command history
* Malware indicators
* Configuration changes

### Historians

Potential evidence:

* Historical process data
* Alarm records
* Process trends
* Time-series information

### Network Infrastructure

Potential evidence:

* Firewall logs
* IDS/IPS alerts
* Switch logs
* Router logs
* Network captures
* Authentication records

---

# Operational Safety Considerations

Forensic investigation in an ICS environment must prioritize operational safety.

Investigators should avoid unnecessary:

```text
System shutdowns
PLC reboots
Configuration changes
Network changes
Service restarts
Firmware changes
Application installations
Heavy disk activity
```

Before collecting evidence, investigators should understand the potential impact of their actions.

A production PLC or SCADA server should not be treated exactly like a normal desktop computer.

---

# Evidence Preservation Strategy

A basic preservation workflow is:

```text
Identify
   ↓
Document
   ↓
Collect
   ↓
Hash
   ↓
Preserve
   ↓
Analyze a Copy
   ↓
Document Findings
```

The original evidence should remain unchanged whenever possible.

Analysis should preferably be performed on a working copy.

---

# Lab Evidence Structure

The final laboratory directory contains:

```text
Lab-35-Introduction-to-ICS-Forensics/
│
├── README.md
│
├── evidence/
│   ├── chain-of-custody.txt
│   ├── evidence-sha256.txt
│   ├── forensic-system-state.txt
│   └── system-info.txt
│
├── forensics/
│   └── evidence-summary.txt
│
└── scripts/
    └── collect-forensic-evidence.sh
```

---

# Evidence Description

| File                           | Purpose                              |
| ------------------------------ | ------------------------------------ |
| `README.md`                    | Complete laboratory documentation    |
| `system-info.txt`              | Basic forensic system information    |
| `forensic-system-state.txt`    | Detailed system-state snapshot       |
| `chain-of-custody.txt`         | Evidence handling documentation      |
| `evidence-sha256.txt`          | SHA-256 integrity verification       |
| `evidence-summary.txt`         | Consolidated forensic findings       |
| `collect-forensic-evidence.sh` | Automated evidence collection script |

---

# Key Commands Used

### System Information

```bash
hostnamectl
uname -a
lsb_release -ds
uptime
```

### Network Information

```bash
ip -br addr
ip route
ss -tulpen
```

### User Information

```bash
who
last -n 10
```

### Process Information

```bash
ps aux --sort=-%cpu | head -30
```

### Services

```bash
systemctl list-units --type=service --state=running --no-pager
```

### Logging

```bash
systemctl status rsyslog --no-pager
journalctl -n 50 --no-pager
```

### Evidence Hashing

```bash
sha256sum evidence/system-info.txt
```

### Hash Verification

```bash
sha256sum -c evidence/evidence-sha256.txt
```

---

# Results

The laboratory successfully demonstrated a basic ICS forensic evidence collection workflow.

The following results were achieved:

* System information successfully collected.
* Network configuration successfully recorded.
* Disk and filesystem information captured.
* Running services documented.
* Current users and login history collected.
* Network sockets and routing information captured.
* Running processes documented.
* rsyslog status examined.
* Recent journal events collected.
* Chain-of-custody documentation created.
* SHA-256 hashes generated.
* Evidence integrity successfully verified.
* Evidence summary created.

---

# Forensic Integrity Result

The SHA-256 verification completed successfully:

```text
evidence/system-info.txt: OK
evidence/forensic-system-state.txt: OK
evidence/chain-of-custody.txt: OK
```

This demonstrates that the collected evidence files matched their recorded cryptographic hashes at the time of verification.

---

# ICS-Specific Lessons Learned

This laboratory demonstrates several important differences between IT and ICS forensics.

### 1. Availability Matters

ICS systems may control physical processes, so taking a system offline can create operational or safety risks.

### 2. Evidence Is Distributed

Important evidence may exist across PLCs, HMIs, SCADA servers, historians, engineering workstations, and network devices.

### 3. Minimal Impact Is Important

Investigators should use the least disruptive collection method possible.

### 4. Integrity Must Be Demonstrated

Hashing provides a mechanism for detecting changes to collected evidence.

### 5. Documentation Is Critical

Every evidence-handling activity should be documented to maintain a reliable chain of custody.

---

# Limitations

This laboratory was performed in a controlled **AWS EC2 Ubuntu environment**.

It does not represent a production ICS network.

The laboratory did not perform:

* Physical PLC imaging
* Live PLC memory acquisition
* SCADA database imaging
* HMI disk imaging
* Industrial switch acquisition
* Physical removable-media acquisition
* Production process interruption

The collected artifacts therefore represent a **Linux-based forensic exercise** demonstrating concepts applicable to ICS investigations.

---

# Conclusion

Lab 35 introduced the fundamentals of forensic investigation in Industrial Control Systems.

The laboratory demonstrated how investigators can collect system information, network information, process information, service information, user activity, and system logs while maintaining evidence integrity.

A chain-of-custody record was created to document the evidence collection process, and SHA-256 hashes were used to verify that collected artifacts remained unchanged.

The exercise also highlighted an important principle of ICS security:

> **Forensic investigation must preserve evidence without unnecessarily disrupting the industrial process.**

The practical workflow developed in this laboratory provides a foundation for more advanced ICS forensic activities involving PLCs, SCADA systems, network traffic, industrial protocols, historians, and security monitoring systems.

---

# Skills Demonstrated

* ICS Forensics Fundamentals
* Digital Evidence Collection
* Linux Forensic Investigation
* System-State Analysis
* Network Evidence Collection
* Process Analysis
* Service Analysis
* Log Analysis
* Chain of Custody
* SHA-256 Integrity Verification
* Evidence Preservation
* Bash Automation
* Incident Investigation
* ICS Operational Safety Awareness

---

## Lab Status

**Status:** Completed

**Evidence Collection:** Successful

**Integrity Verification:** Successful

**Chain of Custody:** Documented

**Environment:** AWS EC2 Ubuntu 24.04.3 LTS

**Lab:** Lab 35 — Introduction to ICS Forensics
