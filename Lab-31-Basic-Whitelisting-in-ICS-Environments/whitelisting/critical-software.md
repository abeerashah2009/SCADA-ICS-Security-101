# Critical ICS Software for Whitelisting

## Purpose

This document identifies software that would normally be considered critical in an ICS/SCADA environment and should be explicitly approved before execution.

## Critical Software

| Software Component | ICS Role | Whitelisting Priority |
|---|---|---|
| SCADA Server Application | Supervisory monitoring and control | Critical |
| HMI Application | Operator interface | Critical |
| PLC Engineering Software | PLC programming and configuration | Critical |
| Historian Application | Industrial data collection and storage | High |
| ICS Database | Process and operational data | Critical |
| Alarm Management Software | Alarm monitoring and notification | High |
| Remote Access Client | Controlled maintenance access | High |

## AWS Laboratory Limitation

The AWS EC2 laboratory environment does not contain a real PLC, HMI, SCADA server, or industrial control application.

Therefore, this lab uses a controlled test application to demonstrate AppArmor policy enforcement.

No real industrial control software is modified or restricted during this exercise.
