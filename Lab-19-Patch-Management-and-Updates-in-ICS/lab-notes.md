# Lab 19: Patch Management and Updates in ICS

## Objective

Learn how to identify systems requiring patches, review vendor
advisories, and develop a safe patching strategy for ICS environments.

## Environment

- OS: Ubuntu 24.04.3 LTS
- Kernel: 6.14.0-1018-aws
- Nmap: 7.94SVN
- OpenSSH: 9.6p1 Ubuntu-3ubuntu13.14
- Containerd: 2.2.5
- Amazon CloudWatch Agent: 1.300062.0b1304-1
- NICE DCV: 2025.0.20103-1

## Task 1: System and Network Inventory

Nmap identified 6 active hosts in the 172.31.10.0/24 network.

The local system exposed:

- TCP/22 — SSH
- TCP/8443 — NICE DCV

The system had 476 upgradable packages.

Evidence:

`task1-evidence.txt`

## Task 2: Software and Vendor Advisory Review

Software versions were collected and recorded for:

- Ubuntu
- OpenSSH
- Nmap
- Containerd
- Amazon CloudWatch Agent
- NICE DCV

Evidence:

- `task2-inventory.txt`
- `task2-advisories.md`

## Task 3: Safe Patching Strategy

A patching plan was developed covering:

- Asset prioritization
- Pre-patching checks
- Maintenance windows
- Controlled deployment
- Rollback procedures
- Post-patching verification

Evidence:

`patching-plan.md`

## Key ICS Security Lesson

ICS environments should not be patched blindly.

Updates should be:

1. Identified
2. Reviewed
3. Tested
4. Approved
5. Scheduled
6. Deployed
7. Verified
8. Documented

A rollback procedure should be available before production patching.

## Conclusion

This lab demonstrated the importance of controlled patch management
in ICS environments. Nmap was used for asset discovery and system
inventory, while package information was used to identify available
updates. A structured patching strategy was developed to minimize
operational disruption while improving security.
