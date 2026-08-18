# Lab 11 - Hypothetical ICS Site Pla`n Assessment

## Purpose

This document provides a hypothetical physical security assessment of an ICS
facility.

No real facility was assessed.

---

# 1. Hypothetical Site Layout

```text
+------------------------------------------------------+
|                  FACILITY PERIMETER                  |
|                                                      |
|   [SECURITY GATE]                 [CCTV]             |
|          |                                           |
|          v                                           |
|     [RECEPTION]                                      |
|          |                                           |
|          v                                           |
|   +----------------------+                           |
|   |     CONTROL ROOM    |                           |
|   |      SCADA / HMI    |                           |
|   +----------------------+                           |
|             |                                        |
|             v                                        |
|   +----------------------+                           |
|   |   SERVER / NETWORK   |                           |
|   |        ROOM          |                           |
|   +----------------------+                           |
|             |                                        |
|             v                                        |
|   +----------------------+                           |
|   |   PLC / CONTROL      |                           |
|   |      EQUIPMENT       |                           |
|   +----------------------+                           |
|                                                      |
+------------------------------------------------------+
2. Security Zones
Zone 1 - Facility Perimeter

Purpose:

Deter unauthorized entry.
Define the facility boundary.
Provide the first physical security layer.

Recommended controls:

Perimeter fencing
Controlled gates
CCTV
Security patrols
Zone 2 - Reception

Purpose:

Control visitor access.
Verify identities.
Maintain visitor records.

Recommended controls:

Reception personnel
Visitor badges
Visitor logs
Escort procedures
Zone 3 - Control Room

Critical area containing SCADA/HMI systems.

Recommended controls:

Electronic access control
CCTV
Restricted personnel
Access logging
Zone 4 - Server/Network Room

Contains critical IT/OT infrastructure.

Recommended controls:

Locked room
Electronic access control
CCTV
Restricted access
Environmental monitoring
Zone 5 - PLC/Control Equipment

Contains industrial control equipment.

Recommended controls:

Locked PLC cabinets
Restricted access
Tamper detection
Access logging
3. Vulnerability Assessment
ID	Vulnerability	Risk	Severity	Mitigation
V01	Uncontrolled entrance	Unauthorized entry	High	Electronic access control
V02	CCTV blind spot	Poor detection	Medium	Improve camera coverage
V03	Unlocked PLC cabinet	Equipment tampering	High	Lock cabinets
V04	Weak server-room protection	Unauthorized system access	High	Restricted server room
V05	Poor visitor control	Unauthorized access	Medium	Visitor registration
V06	Missing access logs	Poor accountability	Medium	Maintain access records
4. Recommended Defense-in-Depth
Perimeter Fence
       |
       v
Controlled Gate
       |
       v
Visitor Management
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
Locked Equipment Rooms
       |
       v
Critical ICS Assets
5. Security Improvements

Priority improvements:

Implement electronic access control.
Improve CCTV coverage.
Lock PLC and control cabinets.
Restrict server-room access.
Introduce visitor management.
Maintain physical access logs.
Review physical security periodically.
Integrate physical security monitoring with incident response procedures.
6. Assessment Conclusion

The hypothetical facility requires multiple layers of physical security.

No individual control should be considered sufficient by itself.

Defense-in-depth provides stronger protection by requiring an attacker to bypass
multiple controls before reaching critical ICS assets.

This assessment demonstrates how physical security contributes directly to the
overall ICS/SCADA cybersecurity posture.

Safety Statement

This site plan is hypothetical.

No real industrial facility was inspected.

No physical security system was accessed.

No security control was bypassed.

No real ICS equipment was contacted.
