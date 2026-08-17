# SCADA and Industrial Control Systems (ICS) Security

## 1. Introduction

SCADA and Industrial Control Systems (ICS) are technologies used to monitor, control, and automate physical industrial processes.

They are commonly used in critical industries such as:

* Energy
* Power generation
* Water treatment
* Wastewater treatment
* Manufacturing
* Oil and gas
* Chemical processing
* Transportation
* Building automation
* Critical infrastructure

In simple words:

> **SCADA helps people monitor and supervise industrial processes, while ICS is the broader group of systems used to control industrial processes.**

A simple industrial environment can be understood as:

```text
Physical Process
       |
       v
    Sensors
       |
       v
      PLC
       |
       v
Industrial Network
       |
       v
     SCADA
       |
       v
    Operator
```

---

# 2. What is SCADA?

SCADA stands for:

**Supervisory Control and Data Acquisition**

SCADA is a system used to monitor industrial processes, collect real-time information, display that information to operators, and provide supervisory control capabilities.

The word SCADA can be understood in two important parts:

### Supervisory Control

This means monitoring and supervising an industrial process from a higher level.

For example, an operator can see whether:

* A pump is running
* A tank is full
* A valve is open
* Temperature is too high
* Pressure is normal

### Data Acquisition

This means collecting information from industrial devices and sensors.

For example:

```text
Temperature = 28°C
Water Level = 75%
Pressure = 4.2 bar
Pump Status = ON
```

SCADA collects this information and makes it available to operators.

---

# 3. Simple SCADA Example

Imagine a water treatment plant.

The plant contains:

* Water tanks
* Pumps
* Valves
* Water-level sensors
* Temperature sensors
* Pressure sensors

The sensors measure what is happening in the plant.

The control system receives this information.

SCADA displays the information to the operator.

```text
Water Tank
    |
    v
Water-Level Sensor
    |
    v
PLC / RTU
    |
    v
Industrial Network
    |
    v
SCADA
    |
    v
Operator
```

The operator might see:

```text
================================
       WATER TREATMENT SCADA
================================

Water Level : 75%
Temperature : 28°C
Pressure    : 4.2 bar
Pump        : ON
Valve       : OPEN
System      : NORMAL
```

This allows the operator to understand the current condition of the industrial process.

---

# 4. Main Functions of SCADA

SCADA systems commonly perform several important functions.

## 4.1 Real-Time Data Acquisition

SCADA collects information from sensors and industrial devices.

For example:

```text
Temperature Sensor
        |
        v
      28°C
        |
        v
      SCADA
```

The operator can see the current temperature.

---

## 4.2 Monitoring

SCADA provides a visual representation of the industrial process.

An operator may be able to see:

* Equipment status
* Sensor values
* Alarms
* Process conditions
* Trends
* System health

---

## 4.3 Supervisory Control

SCADA can provide operators with supervisory control capabilities.

Depending on the system, an operator may be able to:

* Start a pump
* Stop a pump
* Open a valve
* Close a valve
* Change a setpoint
* Acknowledge an alarm

These actions are controlled by the system's configuration and authorization mechanisms.

---

## 4.4 Data Logging and Storage

SCADA systems can store historical process information.

For example:

```text
Time       Temperature    Water Level
08:00      27°C           60%
08:10      28°C           65%
08:20      28°C           70%
08:30      29°C           75%
```

Historical data can help engineers and operators:

* Find problems
* Analyze trends
* Troubleshoot equipment
* Investigate incidents
* Generate reports

---

# 5. What is ICS?

ICS stands for:

**Industrial Control Systems**

ICS is a broad term used for systems that monitor and control industrial processes.

ICS is not just one single technology.

It is a larger category that can include:

* SCADA
* PLC
* DCS
* RTU
* HMI
* Industrial control networks

Think of ICS as a large umbrella:

```text
                    ICS
                     |
       +-------------+-------------+
       |             |             |
     SCADA          PLC           DCS
       |             |             |
      HMI           RTU       Control Systems
```

The exact architecture depends on the industrial environment.

---

# 6. SCADA vs ICS

SCADA and ICS are related, but they are not exactly the same thing.

### SCADA

SCADA is focused on:

* Supervisory monitoring
* Data acquisition
* Visualization
* Supervisory control
* Historical data

### ICS

ICS is the broader category that includes technologies used to monitor and control industrial processes.

A simple way to remember:

```text
ICS
 |
 +-- SCADA
 |
 +-- PLC
 |
 +-- DCS
 |
 +-- RTU
 |
 +-- HMI
```

Therefore:

> **SCADA is part of the broader ICS environment.**

---

# 7. What is OT?

OT stands for:

**Operational Technology**

OT refers to technology used to monitor and control physical equipment, processes, and events.

Examples include:

* PLCs
* SCADA
* DCS
* Sensors
* Actuators
* Industrial networks
* Industrial machines

A simple comparison is:

```text
IT
 |
 +-- Computers
 +-- Servers
 +-- Applications
 +-- Databases
 +-- Business Data


OT
 |
 +-- Sensors
 +-- PLCs
 +-- Pumps
 +-- Motors
 +-- Valves
 +-- Physical Processes
```

### Easy Difference

**IT manages information.**

**OT manages or interacts with physical processes.**

---

# 8. PLC - Programmable Logic Controller

PLC stands for:

**Programmable Logic Controller**

A PLC is an industrial computer designed to control machines and industrial processes.

PLCs receive inputs, execute programmed logic, and produce outputs.

```text
Sensor
   |
   v
PLC Input
   |
   v
PLC Logic
   |
   v
PLC Output
   |
   v
Equipment
```

---

# 9. PLC Example

Imagine a water tank.

A sensor measures the water level.

The sensor sends information to the PLC.

The PLC processes the information according to its programmed logic.

The PLC can then control a pump.

```text
Water Tank
    |
    v
Level Sensor
    |
    v
   PLC
    |
    v
   Pump
```

A simplified example of control logic could be:

```text
IF water level requires pumping
    operate the pump
```

Real industrial PLC logic is much more detailed and depends on the process requirements.

---

# 10. PLC Inputs and Outputs

## Inputs

Inputs provide information to the PLC.

Examples:

* Temperature sensor
* Pressure sensor
* Water-level sensor
* Switch
* Emergency-stop signal

```text
Sensor
  |
  v
PLC Input
```

## Outputs

Outputs allow the PLC to control equipment.

Examples:

* Pump
* Motor
* Valve
* Alarm
* Relay

```text
PLC Output
     |
     v
Equipment
```

A simple way to remember:

> **Input = information coming into the PLC.**

> **Output = action coming from the PLC.**

---

# 11. DCS - Distributed Control System

DCS stands for:

**Distributed Control System**

A DCS is an industrial control system designed to control complex processes using distributed control components.

DCS is commonly associated with industries such as:

* Chemical processing
* Power generation
* Oil and gas
* Large manufacturing facilities

Instead of depending on one central controller for every function, control functions can be distributed across different parts of the industrial environment.

---

# 12. HMI - Human-Machine Interface

HMI stands for:

**Human-Machine Interface**

An HMI is the interface through which an operator can view and interact with an industrial process.

For example:

```text
================================
          INDUSTRIAL HMI
================================

Pump 1       : ON
Pump 2       : OFF
Water Level  : 72%
Temperature  : 29°C
Pressure     : NORMAL
Alarm        : NONE
```

The HMI makes industrial information easier for humans to understand.

---

# 13. RTU - Remote Terminal Unit

RTU stands for:

**Remote Terminal Unit**

An RTU is a device commonly used to collect data from remote locations and communicate that information to a control center.

RTUs can be useful when industrial equipment is spread across large geographical areas.

Examples include:

* Remote water pumps
* Electrical substations
* Pipeline infrastructure
* Remote monitoring stations

A simplified example:

```text
Remote Sensor
      |
      v
     RTU
      |
      v
Communication Network
      |
      v
SCADA Control Center
```

---

# 14. Sensors

Sensors collect information from the physical environment.

Examples include:

* Temperature sensors
* Pressure sensors
* Water-level sensors
* Flow sensors
* Voltage sensors
* Current sensors
* Speed sensors

Example:

```text
Water Tank
    |
    v
Level Sensor
    |
    v
   PLC
```

The sensor does not normally make the final control decision.

It provides information about the physical process.

---

# 15. Actuators

Actuators perform physical actions.

Examples include:

* Pumps
* Motors
* Valves
* Relays

For example:

```text
PLC
 |
 v
Control Signal
 |
 v
Pump
 |
 v
Water Movement
```

Easy way to remember:

> **Sensor = tells the system what is happening.**

> **Actuator = does something to the physical process.**

---

# 16. Complete Industrial Control Loop

A basic industrial control loop looks like this:

```text
          Physical Process
                 |
                 v
              Sensor
                 |
                 v
             Controller
                 |
                 v
              Actuator
                 |
                 v
          Physical Process
```

The process continuously produces information.

Sensors measure it.

The controller processes it.

Actuators perform actions.

This creates a control loop.

---

# 17. Complete SCADA/ICS Architecture

A simplified industrial environment can look like this:

```text
                 PHYSICAL PROCESS
                        |
             +----------+----------+
             |                     |
          Sensors              Actuators
             |                     ^
             v                     |
            PLC <------------------+
             |
             |
      Industrial Network
             |
       +-----+------+
       |            |
      HMI         SCADA
       |            |
       +-----+------+
             |
             v
          Operator
```

The basic flow is:

```text
Physical Process
       |
       v
    Sensors
       |
       v
   PLC / RTU
       |
       v
Industrial Network
       |
       v
SCADA / HMI
       |
       v
Operator
```

---

# 18. Industrial Sectors Using SCADA/ICS

SCADA and ICS are used in many industries.

## 18.1 Energy

Used in:

* Power plants
* Electricity transmission
* Electricity distribution
* Electrical substations

SCADA can monitor:

* Voltage
* Current
* Power
* Equipment status
* Network conditions

---

## 18.2 Water and Wastewater

Used in:

* Water treatment plants
* Wastewater plants
* Pump stations
* Water distribution

SCADA can monitor:

* Water levels
* Flow rates
* Pump status
* Pressure
* Process conditions

---

## 18.3 Manufacturing

ICS can control:

* Production lines
* Motors
* Conveyors
* Industrial robots
* Machines
* Automated processes

---

## 18.4 Oil and Gas

ICS can be used for:

* Pipelines
* Pumping stations
* Storage facilities
* Processing facilities

---

## 18.5 Chemical Industry

Control systems can monitor and control:

* Temperature
* Pressure
* Flow
* Chemical processes
* Industrial equipment

---

## 18.6 Transportation

Industrial control technologies may be used in:

* Rail infrastructure
* Traffic systems
* Transportation facilities

---

# 19. Water Treatment Case Study

Consider a water treatment plant.

The plant contains:

* Water tanks
* Pumps
* Valves
* Sensors
* PLCs
* SCADA
* Operator workstations

A simplified architecture is:

```text
Water Tank
    |
    v
Sensors
    |
    v
PLC
    |
    v
Industrial Network
    |
    v
SCADA
    |
    v
Operator
```

Suppose the water-level sensor reports:

```text
Water Level = 90%
```

The PLC receives the information.

The PLC processes it using its configured control logic.

SCADA receives the relevant information and displays it to the operator.

The operator may see:

```text
================================
       WATER TREATMENT
================================

Water Level : 90%
Pump        : ON
Status      : HIGH
Alarm       : ACTIVE
```

This demonstrates how information moves between the physical process, control system, SCADA, and human operator.

---

# 20. Industrial Networks

Industrial devices need to communicate with each other.

A simplified industrial network looks like:

```text
                SCADA
                  |
                  |
        +---------+---------+
        |                   |
       PLC                 RTU
        |                   |
     Sensors             Sensors
        |
     Equipment
```

Industrial networks may contain multiple zones depending on the system architecture.

Network design is extremely important for ICS security.

---

# 21. Industrial Protocols

Industrial environments use specialized communication protocols.

Examples include:

* Modbus
* DNP3
* OPC UA
* EtherNet/IP
* PROFINET
* BACnet
* IEC 60870-5-104
* IEC 61850

Different protocols are used for different industrial applications.

For example:

```text
SCADA
  |
  | Industrial Protocol
  v
PLC / RTU
  |
  v
Industrial Equipment
```

---

# 22. Modbus

Modbus is a widely used industrial communication protocol.

It can be used for communication between industrial devices such as:

* PLCs
* SCADA systems
* Sensors
* Controllers

Common forms include:

* Modbus RTU
* Modbus TCP

A simple conceptual example:

```text
SCADA
  |
  | Modbus
  v
PLC
  |
  v
Industrial Device
```

Modbus should only be tested in an authorized laboratory environment.

---

# 23. Why ICS Security Is Important

ICS environments control physical processes.

This makes them different from ordinary computer systems.

A successful attack against an ICS environment could potentially cause:

* Production shutdown
* Loss of monitoring
* Equipment damage
* Environmental impact
* Service disruption
* Safety risks

For example:

```text
Cyber Attack
     |
     v
ICS System
     |
     v
Control Change
     |
     v
Physical Process
     |
     v
Potential Physical Impact
```

This is why ICS cybersecurity is critical.

---

# 24. IT Security vs ICS Security

Traditional IT security often focuses heavily on:

* Confidentiality
* Integrity
* Availability

ICS security must consider these as well as:

* Safety
* Reliability
* Availability
* Process stability
* Physical consequences

For example, shutting down an ordinary server may be inconvenient.

Unexpectedly shutting down an industrial control system could potentially stop production or affect safety.

Therefore, ICS security requires careful planning.

---

# 25. CIA Triad in ICS

CIA stands for:

**Confidentiality**

**Integrity**

**Availability**

## Confidentiality

Only authorized people should access sensitive information.

## Integrity

Industrial data and control commands should not be changed improperly.

## Availability

Industrial systems should remain available when required.

In many industrial environments, availability and safety are especially important.

---

# 26. Common ICS Security Risks

Common risks include:

* Weak passwords
* Unauthorized access
* Poor network segmentation
* Unpatched systems
* Unsupported software
* Insecure remote access
* Malware
* Misconfiguration
* Insider threats
* Compromised IT systems reaching OT networks

A major concern is that an attacker may move from an IT environment toward an OT/ICS environment if proper security boundaries are not in place.

---

# 27. Network Segmentation

Network segmentation means separating different parts of a network.

A simplified example is:

```text
                Internet
                   |
                   v
             Corporate IT
                   |
                Firewall
                   |
                   v
              OT / ICS
                   |
          +--------+--------+
          |                 |
        SCADA              PLC
          |                 |
          +--------+--------+
                   |
            Physical Process
```

The purpose is to reduce unnecessary communication between network zones and limit the potential spread of threats.

---

# 28. Defense in Depth

Defense in depth means using multiple layers of security.

For example:

```text
Layer 1  -> Physical Security
Layer 2  -> Network Segmentation
Layer 3  -> Firewalls
Layer 4  -> Authentication
Layer 5  -> Access Control
Layer 6  -> Monitoring
Layer 7  -> Backups
Layer 8  -> Incident Response
```

The goal is:

> Do not depend on a single security control.

If one control fails, other controls can still provide protection.

---

# 29. Access Control

Only authorized users should be allowed to access critical industrial systems.

Important practices include:

* Strong authentication
* Least privilege
* Role-based access
* Account management
* Removing unused accounts
* Controlled remote access
* Multi-factor authentication where supported and appropriate

---

# 30. Patch Management

Industrial systems should be maintained and patched appropriately.

However, patching ICS systems requires careful planning.

A simplified process is:

```text
Security Update
      |
      v
Testing
      |
      v
Compatibility Check
      |
      v
Maintenance Window
      |
      v
Deployment
      |
      v
Verification
```

Why?

Because an industrial system may depend on specific software, drivers, firmware, or vendor configurations.

A patch should therefore be tested before being deployed into a critical production environment whenever possible.

---

# 31. Monitoring and Logging

Industrial environments should be monitored for unusual activity.

Examples include:

* Unexpected logins
* Unusual network connections
* Unexpected configuration changes
* Unexpected commands
* Communication anomalies
* Changes to industrial devices

Logs help security teams with:

* Detection
* Troubleshooting
* Investigation
* Incident response

---

# 32. Backup and Recovery

Backups are important for recovering from failures or security incidents.

Potential backup targets include:

* SCADA configurations
* Server configurations
* PLC programs where appropriate
* HMI configurations
* Network device configurations
* Important documentation

A backup is only useful if it can be successfully restored.

Therefore:

```text
Backup
  |
  v
Restore Test
  |
  v
Verify Recovery
```

---

# 33. Remote Access Security

Remote access can increase the attack surface of an ICS environment.

Remote access should be carefully controlled.

Possible security measures include:

* VPN
* Multi-factor authentication
* Strong authentication
* Least privilege
* Jump hosts
* Session monitoring
* Time-limited access

Remote access should only be enabled when necessary.

---

# 34. Asset Inventory

Security teams should know what devices exist in their industrial environment.

A simple inventory might look like:

```text
Asset       Type       Purpose
------------------------------------------------
PLC-01      PLC        Pump control
RTU-01      RTU        Remote monitoring
SCADA-01    Server     Supervisory monitoring
HMI-01      HMI       Operator interface
SENSOR-01   Sensor     Water-level measurement
```

Asset inventory helps security teams understand:

* What needs protection
* What systems are connected
* Which devices may be vulnerable
* Which systems are critical

---

# 35. Purdue Model

The Purdue Model is commonly used as a conceptual way to organize industrial environments into different levels.

A simplified view is:

```text
Level 5
Enterprise Network
        |
        v
Level 4
Business / IT Systems
        |
        v
Level 3
Site Operations
        |
        v
Level 2
Supervisory Control
        |
        v
Level 1
Basic Control
        |
        v
Level 0
Physical Process
```

The exact implementation varies between organizations.

The model helps explain the relationship between enterprise IT systems and industrial control environments.

---

# 36. IT and OT Convergence

Modern organizations increasingly connect IT and OT environments.

This can provide benefits such as:

* Centralized monitoring
* Data analytics
* Predictive maintenance
* Remote management
* Cloud integration

However, greater connectivity can also increase cybersecurity risk.

```text
IT
 |
 v
Connected Environment
 |
 v
OT / ICS
 |
 v
Physical Process
```

Therefore, security architecture is important when connecting IT and OT.

---

# 37. Common ICS Security Controls

Important security controls include:

* Network segmentation
* Firewalls
* Access control
* Authentication
* Multi-factor authentication where appropriate
* Monitoring
* Logging
* Secure remote access
* Patch management
* Backup and recovery
* Asset inventory
* Vulnerability management
* Incident response
* Security policies
* Security awareness

---

# 38. Incident Response

A simplified ICS incident response process is:

```text
Prepare
   |
   v
Detect
   |
   v
Analyze
   |
   v
Contain
   |
   v
Recover
   |
   v
Learn
```

ICS incident response must consider:

* Safety
* Operational continuity
* System availability
* Physical processes
* Business impact

A security team should avoid taking actions that could unintentionally create a dangerous operational condition.

---

# 39. Stuxnet

Stuxnet is one of the most well-known examples of malware associated with industrial control environments.

It targeted industrial control environments associated with Iran's nuclear program.

The incident demonstrated that cyberattacks can potentially go beyond stealing information and affect physical industrial processes.

The important lesson is:

```text
Cyber Attack
      |
      v
Industrial Control System
      |
      v
Control Manipulation
      |
      v
Physical Process
      |
      v
Potential Physical Impact
```

Stuxnet is therefore an important case study in ICS cybersecurity.

---

# 40. Safety and ICS Security

Safety is an important part of industrial cybersecurity.

In an ordinary IT environment, a cyber incident might result in:

* Data loss
* Application downtime
* Service disruption

In an ICS environment, a cyber incident could potentially affect:

* Machines
* Pumps
* Motors
* Valves
* Chemical processes
* Electrical systems
* Physical safety

Therefore:

> **ICS cybersecurity is not only about protecting computers. It is also about protecting physical processes and people.**

---

# 41. Basic ICS Security Architecture

A simplified secure architecture could look like:

```text
                    Internet
                       |
                       v
                Corporate Network
                       |
                    Firewall
                       |
                       v
                 OT DMZ / Zone
                       |
                    Firewall
                       |
                       v
                  ICS Network
                       |
             +---------+---------+
             |                   |
           SCADA                PLC
             |                   |
             +---------+---------+
                       |
                Physical Process
```

The purpose of separating zones is to reduce unnecessary exposure and control communication paths.

---

# 42. Beginner Mental Model

The easiest way to understand SCADA and ICS is:

```text
SENSORS
   |
   | Collect information
   v
PLC / RTU
   |
   | Process and control
   v
EQUIPMENT
   |
   | Physical action
   v
INDUSTRIAL PROCESS
   |
   | Information
   v
SCADA / HMI
   |
   | Display information
   v
OPERATOR
```

Remember:

**Sensor = collects information**

**PLC = controls equipment**

**Actuator = performs an action**

**SCADA = supervises and displays**

**HMI = interface for humans**

**Operator = monitors and makes decisions**

**ICS = broader industrial control environment**

**OT = technology used to operate and control the physical world**

---

# 43. Key Terms

| Term                 | Meaning                                              |
| -------------------- | ---------------------------------------------------- |
| SCADA                | Supervisory Control and Data Acquisition             |
| ICS                  | Industrial Control Systems                           |
| OT                   | Operational Technology                               |
| PLC                  | Programmable Logic Controller                        |
| DCS                  | Distributed Control System                           |
| HMI                  | Human-Machine Interface                              |
| RTU                  | Remote Terminal Unit                                 |
| Sensor               | Measures a physical condition                        |
| Actuator             | Performs a physical action                           |
| SCADA Server         | Provides supervisory functions                       |
| Industrial Network   | Connects industrial devices                          |
| Modbus               | Industrial communication protocol                    |
| DNP3                 | Industrial communication protocol                    |
| OPC UA               | Industrial communication/interoperability technology |
| Network Segmentation | Separating network zones                             |
| Defense in Depth     | Multiple layers of security                          |

---

# 44. Key Takeaways

The most important concepts from this introduction are:

1. **SCADA** means Supervisory Control and Data Acquisition.
2. **ICS** means Industrial Control Systems.
3. SCADA is part of the broader ICS environment.
4. **OT** means Operational Technology.
5. **PLC** means Programmable Logic Controller.
6. **DCS** means Distributed Control System.
7. **HMI** means Human-Machine Interface.
8. **RTU** means Remote Terminal Unit.
9. Sensors collect information from physical processes.
10. Actuators perform physical actions.
11. PLCs execute control logic.
12. SCADA provides supervisory monitoring and control.
13. ICS is used in energy, water, manufacturing, oil and gas, and other critical industries.
14. Industrial systems communicate through industrial networks and protocols.
15. ICS security is important because cyber incidents can affect physical processes.
16. Network segmentation helps separate critical industrial systems from other networks.
17. Defense in depth uses multiple security controls.
18. Access control limits unauthorized access.
19. Monitoring and logging help detect suspicious activity.
20. Backups support recovery.
21. Remote access should be carefully controlled.
22. Asset inventory helps identify systems that need protection.
23. Stuxnet demonstrated the potential physical impact of cyberattacks against ICS.
24. ICS security must consider safety and operational continuity.

---

# 45. Lab Objectives

This lab focuses on:

* Understanding SCADA fundamentals
* Understanding ICS fundamentals
* Understanding OT fundamentals
* Understanding PLCs
* Understanding DCS
* Understanding HMI
* Understanding RTUs
* Understanding sensors and actuators
* Understanding SCADA architecture
* Identifying industrial sectors
* Understanding industrial networks
* Understanding industrial protocols
* Understanding ICS cybersecurity
* Understanding network segmentation
* Understanding access control
* Understanding patch management
* Understanding monitoring and logging
* Understanding backup and recovery
* Understanding incident response
* Understanding the Stuxnet case study

---

# 46. Practical Security Reminder

SCADA and ICS systems can control real physical equipment.

Never scan, attack, modify, or attempt unauthorized access to real industrial systems.

Security testing should only be performed in:

* Personal laboratory environments
* Authorized training environments
* CTF environments
* Explicitly authorized security assessments

This project focuses on educational and defensive cybersecurity concepts.

---

# 47. Conclusion

SCADA and ICS are important technologies used to monitor and control industrial processes.

The easiest way to remember the relationship is:

```text
                ICS
                 |
       +---------+---------+
       |         |         |
     SCADA      PLC       DCS
       |
      HMI
```

A basic industrial process can be understood as:

```text
Sensors
   |
   v
PLC / RTU
   |
   v
Industrial Network
   |
   v
SCADA / HMI
   |
   v
Operator
```

SCADA provides supervisory monitoring, data acquisition, visualization, and control capabilities.

ICS is the broader category of industrial control technologies.

OT represents the operational technology environment that interacts with physical processes.

Because industrial systems can affect the physical world, cybersecurity is extremely important.

Important defensive concepts include:

* Network segmentation
* Access control
* Secure remote access
* Monitoring
* Logging
* Patch management
* Backups
* Defense in depth
* Incident response
* Asset inventory

Understanding these fundamentals provides the foundation for more advanced OT and ICS cybersecurity labs.

---

# 48. Project Status

**Status:** Foundational SCADA/ICS Security Lab

**Focus:** SCADA, ICS, OT, PLCs, DCS, HMI, RTUs, industrial networks, protocols, architecture, and cybersecurity fundamentals

**Environment:** Authorized Linux laboratory environment

**Safety:** No real-world industrial control systems were accessed, scanned, attacked, or modified.
