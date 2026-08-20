# Lab 24: ICS/SCADA Risk Assessment 101

## Overview

This lab demonstrates a basic risk assessment process for a simulated ICS/SCADA environment. The assessment covers network discovery, service identification, network traffic capture, threat identification, risk evaluation, and security mitigation recommendations.

## Objectives

- Understand ICS/SCADA security risks.
- Identify potential network assets and attack surfaces.
- Perform network discovery using Nmap.
- Identify exposed and filtered services.
- Capture network traffic using tcpdump and Wireshark.
- Identify potential threats.
- Evaluate risks based on likelihood and impact.
- Recommend appropriate security mitigations.
- Document assessment findings professionally.

## Environment

| Component | Details |
|---|---|
| Operating System | Ubuntu 24.04.3 LTS |
| Assessment Host | 172.31.10.201 |
| Assessment Network | 172.31.10.0/24 |
| Nmap | 7.94SVN |
| Wireshark | 4.2.2 |
| Packet Capture | tcpdump |
| Capture Interface | any |

## Task 1: ICS/SCADA Risk Concepts

ICS/SCADA environments differ from traditional IT environments because availability, reliability, integrity, and safety are critical.

Potential consequences of an ICS security incident include:

- Operational downtime
- Loss of process control
- Equipment damage
- Safety hazards
- Production disruption
- Financial losses

## Task 2: Threat Identification

The following threats were considered:

1. Unauthorized access
2. Malware infection
3. Unnecessary network exposure
4. Weak network segmentation
5. Loss of system availability
6. Unauthorized access to management services
7. Exposure of web-based services

## Task 3: Network Discovery

Network discovery was performed against the simulated assessment network using Nmap.

Command used:

```bash
nmap -sn 172.31.10.0/24 -oN network-discovery.txt

