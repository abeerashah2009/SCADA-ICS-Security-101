# Lab 07: Identifying ICS Components in a Network

## Objectives

- Understand how ICS components can be identified in a network.
- Learn the basic use of Nmap for network discovery.
- Understand how PLCs, HMIs, SCADA servers, and other ICS components may appear during network assessment.
- Practice documenting network inventory information.
- Understand the importance of authorization before scanning industrial networks.

## Prerequisites

- Basic understanding of ICS/SCADA architecture.
- Basic networking knowledge.
- Familiarity with Linux command-line tools.
- Basic understanding of Nmap.

## Lab Environment

This exercise is performed in an AWS EC2 Linux environment.

Because this is a cloud-hosted environment, the lab does not contain real PLCs, HMIs, or industrial controllers.

For safety, the practical scan in this lab is limited to the local system.

Target:

    127.0.0.1

No external or unauthorized network is scanned.

## Task 1: Network Discovery with Nmap

Nmap is an open-source network discovery and security auditing tool.

A ping scan can be used to determine whether a host is reachable without performing a full port scan.

Example:

```bash
nmap -sn 127.0.0.1
