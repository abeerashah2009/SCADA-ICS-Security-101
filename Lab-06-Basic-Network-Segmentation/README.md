# Lab 06: Basic Network Segmentation Concepts

## Objectives

- Understand network segmentation and why it is important in cybersecurity.
- Understand the purpose of a DMZ.
- Learn how corporate and ICS networks can be separated.
- Understand the role of firewalls, VLANs, and air-gapping.
- Design a simple segmented ICS/enterprise network.
- Understand basic security considerations for segmented networks.

## Key Concepts

### Network Segmentation

Network segmentation divides a larger network into separate security zones.

This can reduce the ability of an attacker to move from one network area to another.

### DMZ

A DMZ is a separate network zone used for systems that need controlled communication with external or less-trusted networks.

Example:

Internet → Firewall → DMZ → Firewall → Internal Network

### Corporate Network

A corporate network may contain:

- Employee workstations
- File servers
- Business applications
- Printers

### ICS Network

An ICS network may contain:

- PLCs
- HMIs
- SCADA servers
- Sensors
- Actuators

ICS networks have special requirements because they interact with physical processes.

## Segmentation Methods

### Firewalls

Firewalls control traffic between different network zones.

### VLANs

VLANs logically separate network traffic on shared network infrastructure.

### Air-Gapping

An air-gapped network is physically or logically isolated from another network.

## Example Architecture

```text
                    Internet
                       |
                       v
                  [ Firewall ]
                       |
              +--------+--------+
              |                 |
             DMZ          Corporate Network
              |                 |
         Web Server       PCs / File Server
              |
              |
         [ ICS Firewall ]
              |
              v
          ICS Network
              |
       +------+------+
       |             |
      HMI       PLC / SCADA
