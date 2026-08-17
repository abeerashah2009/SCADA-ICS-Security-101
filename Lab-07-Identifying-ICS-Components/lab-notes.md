# Lab 07 Notes: Identifying ICS Components in a Network

## 1. What is Network Discovery?

Network discovery is the process of identifying systems that are reachable on a network.

Security professionals use network discovery to understand:

- Which hosts are active
- Which systems are communicating
- What services are available
- What devices may require security controls

In an ICS environment, network discovery can help build an asset inventory.

---

## 2. What is Nmap?

Nmap stands for Network Mapper.

It is an open-source tool used for:

- Network discovery
- Host discovery
- Port scanning
- Service detection
- Version identification
- Security auditing

Nmap is widely used by network and security professionals.

---

## 3. Installing Nmap

Nmap was installed using Ubuntu's APT package manager.

Command:

```bash
sudo apt update
sudo apt install -y nmap
## 4. Host Discovery

The following command was used:

nmap -sn 127.0.0.1

The -sn option performs host discovery without performing a normal port scan.

Result
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00013s latency).
Nmap done: 1 IP address (1 host up) scanned
Interpretation

The local host responded successfully.

Therefore:

127.0.0.1 = Host is UP
## 5. Service Detection

The following command was used:

nmap -sV 127.0.0.1

The -sV option attempts to identify services and their versions on open ports.

Result

The scan completed without listing any open ports or services.

Interpretation

No open TCP services were detected by this scan on the local host.

This is a valid result and does not indicate a problem with Nmap.

## 6. Understanding ICS Components

Industrial Control Systems can contain many different types of devices.

PLC

PLC stands for Programmable Logic Controller.

PLCs control industrial processes such as:

Motors
Pumps
Valves
Production machinery
HMI

HMI stands for Human-Machine Interface.

An HMI allows operators to:

View process information
Monitor alarms
Control industrial processes
Interact with PLC systems
SCADA Server

A SCADA server provides supervisory monitoring and control functions.

It may collect information from:

PLCs
RTUs
Sensors
Remote equipment
RTU

RTU stands for Remote Terminal Unit.

RTUs are commonly used in geographically distributed industrial environments.

They collect field information and communicate with supervisory systems.

## 7. How ICS Components May Be Identified

During an authorized network assessment, analysts may use several sources of information.

Examples:

IP Address

An IP address identifies a network interface.

Hostname

A hostname may provide clues about the purpose of a system.

Example:

PLC-01
HMI-01
SCADA-SERVER
RTU-05

These names are only examples and should not be assumed to prove a device type.

Open Ports

Open ports can provide clues about running services.

Service Banners

Service information may reveal software or protocol details.

Vendor Information

Vendor information can sometimes help identify industrial equipment.

Asset Documentation

Existing network diagrams and asset inventories are often extremely valuable when identifying ICS components.

## 8. Lab Environment Findings

This lab was performed on an AWS EC2 Ubuntu system.

The target was:

127.0.0.1

This represents the local machine.

Findings
IP Address	Hostname	Status	Open Services	ICS Device
127.0.0.1	localhost	UP	None detected	None identified
## 9. Important Observation

The EC2 machine used for this laboratory is a normal Linux cloud instance.

It is not a real industrial control system.

Therefore, the scan did not identify:

PLC
HMI
SCADA server
RTU
Industrial controller

This is expected.

The purpose of the exercise is to learn the network discovery and inventory process, not to claim that a normal Linux server is an ICS device.

## 10. Why ICS Scanning Requires Caution

Industrial systems can be sensitive to network activity.

Some older or fragile devices may not handle aggressive scanning well.

Potential concerns include:

Service disruption
Increased network traffic
Unexpected device behavior
Process interruption

For this reason, ICS scanning should always be:

Authorized
Planned
Limited in scope
Appropriate for the environment
Coordinated with system operators
## 11. Safe Scanning Principle

For this lab, scanning was restricted to:

127.0.0.1

No external systems were scanned.

No real industrial devices were contacted.

No industrial processes were modified.

## 12. Nmap Commands Learned
Host Discovery
nmap -sn 127.0.0.1

Purpose:

Discover whether the host is reachable.

Service Detection
nmap -sV 127.0.0.1

Purpose:

Attempt to identify services and versions on open ports.

## 13. Network Inventory

A network inventory records information about systems and devices.

Example:

IP Address	Hostname	Device Type	OS	Services	Notes
127.0.0.1	localhost	Linux Host	Ubuntu	None detected	Lab system

A real ICS inventory may contain:

PLC
HMI
SCADA Server
RTU
Engineering Workstation
Network Switch
Industrial Firewall
Sensors
## 14. Security Benefits of Asset Inventory

Knowing what devices exist helps security teams:

Identify unknown systems
Track critical assets
Understand network architecture
Detect unexpected services
Prioritize security controls
Support incident response

You cannot effectively protect systems that you do not know exist.

## 15. Key Takeaways

Remember:

Nmap = Network discovery and security auditing tool.

-sn = Host discovery without normal port scanning.

-sV = Service and version detection.

PLC = Controls industrial processes.

HMI = Allows operators to interact with industrial systems.

SCADA = Supervisory monitoring and control.

RTU = Collects and communicates remote field data.

Asset inventory = Record of systems and devices in an environment.

## 16. Lab Conclusion

This lab demonstrated the basic process of network discovery using Nmap.

The local host was successfully identified as active, while no open services were detected during service discovery.

Although no real ICS components were present, the exercise demonstrated the methodology used when creating an authorized ICS network inventory.

Future ICS assessments can build on these skills by using a dedicated and authorized industrial simulation environment containing PLC, HMI, SCADA, and RTU simulators.
