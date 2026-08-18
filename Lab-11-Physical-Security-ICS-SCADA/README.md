# Lab 11: Physical Security in ICS/SCADA

## Lab Overview

This laboratory explores the importance of physical security in Industrial Control
Systems (ICS) and Supervisory Control and Data Acquisition (SCADA) environments.

Physical security is an important layer of defense because unauthorized physical
access can allow an attacker to reach control rooms, engineering workstations,
network equipment, PLCs, RTUs, servers, or other industrial assets.

This laboratory uses a hypothetical ICS facility and a local software-based
assessment. No real industrial facility or physical security system is accessed.

---

## Objectives

The objectives of this laboratory are to:

- Understand the importance of physical security in ICS/SCADA environments.
- Identify common physical security safeguards.
- Understand the purpose of locks, fences, and CCTV.
- Analyze risks associated with unauthorized physical access.
- Assess vulnerabilities in a hypothetical ICS site.
- Develop mitigation strategies.
- Explore the role of open-source physical security software.
- Document security observations as professional portfolio evidence.

---

## Prerequisites

- Basic understanding of ICS/SCADA systems.
- Basic understanding of cybersecurity concepts.
- Basic understanding of physical security.
- Linux command-line familiarity.

---

# Task 1: Understanding Common Physical Safeguards

## 1.1 Locks

Locks are used to restrict physical access to authorized personnel.

Examples include:

- Mechanical locks
- Key locks
- Keypad locks
- Electronic access-control systems
- Keycard systems
- Biometric authentication

### ICS Security Importance

Access controls can help prevent unauthorized personnel from entering:

- Control rooms
- Server rooms
- PLC cabinets
- Network communication rooms
- Engineering workstations
- Electrical and instrumentation areas

### Key Security Principle

Physical access should follow the principle of least privilege.

Personnel should receive only the physical access required for their responsibilities.

---

## 1.2 Fences

Perimeter fencing provides a physical boundary around an industrial facility.

Fencing can:

- Deter unauthorized entry.
- Define controlled areas.
- Delay intruders.
- Support security patrols.
- Protect critical infrastructure.

Important areas may require stronger physical protection than general facility areas.

---

## 1.3 CCTV

Closed-Circuit Television (CCTV) systems provide visual monitoring.

CCTV can help organizations:

- Monitor entrances.
- Monitor restricted areas.
- Detect suspicious activity.
- Investigate security incidents.
- Support security personnel.
- Provide evidence after an incident.

CCTV should be considered a detection and monitoring control rather than the
only physical security control.

---

# Task 1.2: Case Study

## Hypothetical ICS Facility Case Study

Consider a water treatment facility containing:

- PLC control panels
- SCADA servers
- Engineering workstations
- Network switches
- Operator workstations
- Instrumentation equipment

The facility implements:

1. Perimeter fencing.
2. Controlled entrance gates.
3. Electronic access cards.
4. CCTV monitoring.
5. Locked control rooms.
6. Restricted server rooms.
7. Visitor identification procedures.

### Security Outcome

These controls create multiple physical security layers.

If an unauthorized person attempts to enter the control area:

1. The perimeter acts as the first barrier.
2. Access control restricts entry.
3. CCTV provides monitoring.
4. Security personnel can respond.
5. Locked equipment rooms provide additional protection.

### Security Lesson

Defense-in-depth should be applied to physical security.

A single physical control should not be relied upon to protect critical ICS assets.

---

# Task 2: Risks of Unauthorized Physical Access

## 2.1 Risk Identification

Unauthorized physical access to ICS environments can create serious risks.

Potential consequences include:

- Equipment damage
- Unauthorized system access
- Theft of equipment
- Theft of removable media
- Malware introduction
- Unauthorized configuration changes
- Network disruption
- Control system shutdown
- Operational downtime
- Safety consequences
- Data exposure

---

## Physical Access Attack Path

A simplified attack path is:

```text
Unauthorized Person
        |
        v
Facility Entry
        |
        v
Restricted Area
        |
        v
Control Room
        |
        v
Engineering Workstation
        |
        v
ICS Network / Control Equipment
        |
        v
Potential Operational Impact
This demonstrates why physical security and cybersecurity are closely connected.

Task 2.2: Security Breach Scenario
Hypothetical Scenario

An unauthorized individual enters an ICS control room.

The individual reaches an operator workstation and attempts to shut down a
critical monitoring application.

Possible Impact
Loss of operator visibility
Loss of monitoring capability
Incorrect operator information
Operational disruption
Potential safety consequences
Existing Controls

Possible controls include:

Locked control-room doors
Access cards
CCTV
Security guards
Visitor management
Workstation authentication
Restricted privileges
Alarm systems
Recommended Response

The organization should:

Detect unauthorized access.
Alert security personnel.
Restrict the individual's access.
Preserve security evidence.
Assess affected systems.
Verify ICS system integrity.
Restore normal operations safely.
Document the incident.
Review physical security controls.
Task 3: Hypothetical ICS Site Plan Assessment
3.1 Hypothetical Site

The hypothetical facility contains:

+--------------------------------------------------+
|              ICS FACILITY PERIMETER              |
|                                                  |
|  [Gate]                         [CCTV]           |
|     |                                            |
|     v                                            |
|  Reception                                       |
|     |                                            |
|     v                                            |
|  +-------------------+                           |
|  | Control Room      |                           |
|  | SCADA / HMI       |                           |
|  +-------------------+                           |
|           |                                      |
|           v                                      |
|  +-------------------+                           |
|  | Network / Server  |                           |
|  | Room              |                           |
|  +-------------------+                           |
|           |                                      |
|           v                                      |
|  +-------------------+                           |
|  | PLC / Control     |                           |
|  | Equipment Area    |                           |
|  +-------------------+                           |
|                                                  |
+--------------------------------------------------+
Vulnerability 1: Uncontrolled Entrance
Observation

An unguarded entrance could allow unauthorized personnel to enter the facility.

Risk

Unauthorized access could lead to access to restricted ICS areas.

Mitigation

Implement:

Electronic access control
Visitor registration
Security personnel
Access logging
Vulnerability 2: Insufficient CCTV Coverage
Observation

Blind spots may exist around critical areas.

Risk

Unauthorized activity may not be detected or recorded.

Mitigation

Implement:

Additional CCTV cameras
Appropriate camera placement
Monitoring procedures
Camera health checks
Vulnerability 3: Unlocked Control Equipment
Observation

PLC cabinets or control equipment may be physically accessible.

Risk

An attacker could manipulate or damage equipment.

Mitigation

Use:

Locked cabinets
Restricted access
Access logging
Tamper detection where appropriate
Vulnerability 4: Poor Server Room Protection
Observation

ICS servers and network equipment require stronger physical protection.

Risk

Unauthorized access could expose critical infrastructure.

Mitigation

Use:

Dedicated server rooms
Electronic access control
CCTV
Visitor restrictions
Environmental monitoring
Vulnerability 5: Lack of Visitor Controls
Observation

Visitors may enter restricted areas without appropriate supervision.

Risk

Unauthorized observation access, or tampering.

Mitigation

Implement:

Visitor identification
Visitor badges
Escort requirements
Visitor logs
Restricted visitor zones
Task 3.2: Risk and Mitigation Table
Vulnerability	Risk	Recommended Mitigation
Uncontrolled entrance	Unauthorized entry	Electronic access control
CCTV blind spots	Poor detection   	Improve camera coverage
Unlocked PLC cabinets	Equipment tampering	Lock cabinets
Weak server-room securit	Unauthorized system access	Restricted server room
Poor visitor management	Unauthorized access	Visitor registration and escort
Lack of access logging	Difficult investigations	Maintain access records
Task 4: Physical Security Tools
Open-Source Security Software

Open-source software can support physical security operations.

One example is ZoneMinder, an open-source video surveillance platform.

A surveillance management platform can provide capabilities such as:

Camera management
Video monitoring
Recording
Event monitoring
Security investigation
Lab Environment Limitation

ZoneMinder is not installed in this laboratory environment because this AWS
training environment is intended for safe cybersecurity laboratory exercises.

The laboratory therefore documents the technology and its security role rather
than deploying a production-style surveillance system.

Security Control Layers

A strong ICS physical security architecture can use multiple layers:

Perimeter Fence
       |
       v
Controlled Gate
       |
       v
Reception / Visitor Control
       |
       v
Electronic Access Control
       |
       v
CCTV Monitoring
       |
       v
Restricted Control Room
       |
       v
Locked Equipment / Server Rooms
       |
       v
ICS Assets

This is an example of defense-in-depth.

Physical Security Principles

Important principles include:

1. Defense in Depth

Use multiple security controls rather than relying on a single control.

2. Least Privilege

Personnel should receive only the physical access required for their duties.

3. Monitoring

Critical areas should be monitored for unauthorized activity.

4. Access Control

Only authorized personnel should enter restricted areas.

5. Accountability

Access should be logged where appropriate so security events can be investigated.

6. Resilience

Physical security controls should continue functioning during operational
disruptions where possible.

Safety Statement

This laboratory uses a hypothetical ICS facility and local documentation.

No real industrial facility was accessed.

No real PLC, RTU, SCADA server, CCTV system, control room, or industrial process
was contacted or modified.

No unauthorized physical security testing was performed.

Evidence Produced

The following evidence files are created for this laboratory:

README.md
lab-notes.md
physical-security-assessment.py
physical-security-results.txt
site-plan-assessment.md

These files document the laboratory activities and findings.

Learning Outcomes

After completing this laboratory, the learner should be able to:

Explain the importance of physical security in ICS/SCADA.
Identify common physical safeguards.
Explain the role of locks, fences, and CCTV.
Identify risks caused by unauthorized physical access.
Analyze a hypothetical ICS facility.
Identify physical vulnerabilities.
Recommend appropriate mitigation strategies.
Explain defense-in-depth for physical security.
Document security assessments professionally.
Final Assessment

The laboratory demonstrates that physical security is an essential component of
ICS/SCADA cybersecurity.

A compromise of physical security can potentially provide an attacker with
direct access to systems that control or monitor industrial processes.

Therefore, ICS security should combine:

Physical security
Network security
Access control
Monitoring
Incident response
Change management
Backup and recovery
Lab Completion Checklist
 Physical safeguards identified
 Locks explained
 Fences explained
 CCTV explained
 Case study documented
 Unauthorized access risks identified
 Security breach scenario analyzed
 Hypothetical site plan created
 Physical vulnerabilities identified
 Mitigation strategies documented
 Open-source security software reviewed
 Safety considerations documented
 Evidence files generated
