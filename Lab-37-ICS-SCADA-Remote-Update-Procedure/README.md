# Lab 37: ICS/SCADA Remote Update Procedure

## Overview

This lab demonstrates a structured and secure procedure for performing remote updates in an ICS/SCADA environment.

The lab focuses on:

* Remote update planning
* System and network baseline collection
* Secure remote access using OpenVPN
* Firewall security requirements
* Backup and recovery
* Simulated update and rollback verification
* Evidence collection and documentation

The activities were performed in an Ubuntu-based AWS laboratory environment.

---

## Objectives

The main objectives of this lab were to:

1. Understand the process of performing controlled remote updates for ICS/SCADA systems.
2. Create a structured remote update plan.
3. Collect the current system and network security baseline.
4. Evaluate secure remote-access requirements.
5. Document OpenVPN availability and firewall requirements.
6. Create a backup of an ICS configuration.
7. Simulate an update to the configuration.
8. Restore the original configuration using the backup.
9. Verify that the rollback was successful.
10. Maintain evidence for audit and troubleshooting purposes.

---

## Lab Environment

| Item             | Details                                    |
| ---------------- | ------------------------------------------ |
| Platform         | AWS EC2                                    |
| Operating System | Ubuntu Linux                               |
| Remote Access    | SSH                                        |
| VPN Software     | OpenVPN 2.6.14                             |
| Firewall         | UFW / iptables baseline checked            |
| Repository       | `SCADA-ICS-Security-101`                   |
| Lab Directory    | `Lab-37-ICS-SCADA-Remote-Update-Procedure` |

---

# Task 1 — System Baseline

Before designing a remote update procedure, the current workstation configuration was documented.

The following information was collected:

* Date and time
* Hostname
* Operating system
* Kernel version
* IP addresses
* Routing table
* Listening network ports
* Running system services

### Evidence

```text
evidence/system-baseline.txt
```

The baseline provides a reference point for comparing the system before and after future maintenance activities.

---

# Task 2 — Remote Update Planning

A detailed remote update plan was created in:

```text
planning/remote-update-plan.txt
```

The plan includes:

* Pre-update assessment
* Maintenance window
* Component prioritization
* Update sequence
* Secure remote-access requirements
* Backup requirements
* Post-update validation
* Rollback conditions
* Rollback priorities
* Final approval requirements

## Update Priority

| Component                    | Priority | Validation                   |
| ---------------------------- | -------- | ---------------------------- |
| Backup and verification      | Critical | Confirm backup integrity     |
| PLC / control components     | High     | Verify PLC communication     |
| SCADA monitoring             | Medium   | Verify monitoring and alarms |
| Historian / data services    | Medium   | Verify data collection       |
| Gateway / network components | Low      | Verify network connectivity  |

Updates should be performed during an approved maintenance window to reduce operational impact.

---

# Task 3 — Secure Remote Access

The remote-access environment was examined before designing the secure update process.

The following items were checked:

* OpenVPN availability
* OpenVPN version
* SSH service status
* Listening ports
* UFW status
* iptables INPUT policy

### OpenVPN

The installed OpenVPN version was:

```text
OpenVPN 2.6.14
```

Evidence:

```text
vpn/remote-access-baseline.txt
```

---

## Secure VPN Design

A secure remote-access design was documented in:

```text
vpn/secure-remote-access-design.txt
```

The design recommends:

* Approved VPN access
* Strong certificate/key authentication
* Protection of private keys
* Authorized maintenance personnel only
* Restricted access to required ICS/SCADA systems
* Remote-session monitoring
* Administrative activity logging
* Avoiding direct Internet exposure of ICS/SCADA management interfaces

### Remote Update Flow

```text
Authorized Administrator
        |
        v
     VPN Tunnel
        |
        v
   Secure Gateway
        |
        v
 ICS/SCADA Management Network
        |
        +---- PLC
        +---- HMI
        +---- SCADA Server
        +---- Historian
        +---- Engineering Workstation
```

---

# Firewall Baseline

The current laboratory firewall state was recorded.

```text
UFW:
Inactive

iptables INPUT policy:
ACCEPT
```

This configuration was documented rather than changed because the laboratory is hosted in AWS and changing the firewall without confirming the management path could accidentally interrupt SSH access.

For a production ICS environment, firewall rules should be designed to:

1. Permit VPN traffic from approved sources.
2. Restrict SSH to authorized management networks.
3. Allow only required ICS/SCADA management traffic.
4. Permit established and related connections.
5. Deny unnecessary inbound traffic.
6. Log relevant blocked traffic.

AWS Security Groups should also be considered when the ICS laboratory is hosted in AWS.

---

# Task 4 — Backup and Recovery

A simulated ICS configuration was created for demonstrating backup and rollback.

The test configuration was:

```text
rollback/demo-system/etc/ics-application.conf
```

The original configuration contained:

```text
system_name=ICS-LAB
scada_mode=normal
poll_interval=5
alarm_enabled=true
remote_update=enabled
```

---

## Backup Creation

The configuration was backed up using `rsync`:

```bash
sudo rsync -a rollback/demo-system/etc/ rollback/backup/etc-backup/
```

The backup was stored under:

```text
rollback/backup/etc-backup/
```

The backup contents were then verified.

---

# Task 5 — Simulated Update

The configuration was intentionally changed to simulate an update:

```text
scada_mode=maintenance
poll_interval=10
alarm_enabled=false
```

This represents a controlled laboratory simulation of a configuration change.

The original production ICS/SCADA system was **not modified**.

---

# Task 6 — Rollback Procedure

The original configuration was restored from the backup:

```bash
rsync -a rollback/backup/etc-backup/ rollback/restored/
```

The restored configuration was then compared with the backup using:

```bash
cmp -s \
rollback/backup/etc-backup/ics-application.conf \
rollback/restored/ics-application.conf
```

The result was:

```text
ROLLBACK VERIFIED: configuration restored successfully
```

This confirms that the simulated rollback successfully restored the backed-up configuration.

---

# Rollback Strategy

If a real ICS/SCADA update fails, the following sequence should be followed:

1. Stop further update activity.
2. Preserve logs and evidence.
3. Restore the backed-up configuration.
4. Restore the previous software or firmware where applicable.
5. Restart affected services in a controlled order.
6. Validate ICS/SCADA communications.
7. Confirm stable operation.
8. Document the incident and rollback.

Rollback should be initiated if:

* Control communication is lost.
* SCADA services fail.
* Unexpected process behavior occurs.
* Critical alarms appear.
* Data collection fails.
* System stability decreases.
* The update cannot be successfully validated.

---

# Evidence Structure

The completed laboratory artifacts are organized as follows:

```text
Lab-37-ICS-SCADA-Remote-Update-Procedure/
├── evidence/
│   └── system-baseline.txt
│
├── planning/
│   └── remote-update-plan.txt
│
├── vpn/
│   ├── remote-access-baseline.txt
│   └── secure-remote-access-design.txt
│
├── rollback/
│   ├── backup/
│   │   └── etc-backup/
│   │       └── ics-application.conf
│   ├── demo-system/
│   │   └── etc/
│   │       └── ics-application.conf
│   └── restored/
│       └── ics-application.conf
│
└── scripts/
```

---

# Verification Summary

| Area                        | Result     |
| --------------------------- | ---------- |
| System baseline             | Completed  |
| Remote update plan          | Completed  |
| OpenVPN verification        | Completed  |
| Secure remote-access design | Completed  |
| Firewall baseline           | Documented |
| Backup creation             | Completed  |
| Simulated update            | Completed  |
| Configuration restoration   | Completed  |
| Rollback verification       | Successful |
| Evidence organization       | Completed  |

---

# Security Considerations

Remote updates are particularly sensitive in ICS/SCADA environments because incorrect changes can affect availability, safety, and industrial processes.

A secure remote-update procedure should therefore use:

* Authorized personnel
* Approved maintenance windows
* Secure VPN connectivity
* Strong authentication
* Restricted firewall rules
* Verified backups
* Controlled update sequencing
* Continuous monitoring
* Post-update validation
* Documented rollback procedures

The laboratory intentionally used a **simulated configuration** for the update and rollback demonstration instead of modifying a real industrial control system.

---

# Key Learning Outcomes

After completing this lab, the following concepts were demonstrated:

* Remote ICS/SCADA updates require careful planning.
* Critical control components should receive higher update priority.
* VPNs provide a secure channel for authorized remote maintenance.
* Firewall rules should restrict unnecessary remote access.
* Backups are essential before performing updates.
* Rollback procedures should be prepared before an update begins.
* Configuration restoration can be verified using file comparison.
* Evidence and baseline information improve troubleshooting and auditability.

---

# Conclusion

Lab 37 demonstrated a controlled approach to remote ICS/SCADA updates.

A complete update plan was created, the laboratory system was baselined, OpenVPN availability was verified, secure remote-access requirements were documented, and firewall conditions were recorded.

A simulated ICS configuration was then backed up, intentionally modified, and successfully restored. The rollback was verified using `cmp`, producing:

```text
ROLLBACK VERIFIED: configuration restored successfully
```

This lab demonstrates an important ICS security principle: **remote updates should never be performed without authorization, secure access, verified backups, validation procedures, and a tested rollback strategy.**

---

## Evidence Files

* `evidence/system-baseline.txt`
* `planning/remote-update-plan.txt`
* `vpn/remote-access-baseline.txt`
* `vpn/secure-remote-access-design.txt`
* `rollback/backup/etc-backup/ics-application.conf`
* `rollback/demo-system/etc/ics-application.conf`
* `rollback/restored/ics-application.conf`

---

## Final Status

**Lab 37 — ICS/SCADA Remote Update Procedure: COMPLETED**

The laboratory objectives were demonstrated through documented planning, secure remote-access analysis, backup creation, simulated updating, and verified rollback.
