# Lab 11 - Physical Security in ICS/SCADA
## Laboratory Execution Notes

---

## 1. Environment

Laboratory type:
Safe local documentation and assessment exercise

Environment:
Ubuntu Linux AWS laboratory environment

Assessment target:
Hypothetical ICS/SCADA facility

Real industrial equipment:
None

---

# Task 1 - Physical Safeguards

## 1.1 Locks

Locks were reviewed as a physical access-control mechanism.

Examples considered:

- Mechanical locks
- Keypad locks
- Keycard systems
- Electronic access-control systems
- Biometric controls

ICS areas that may require controlled access include:

- Control rooms
- Server rooms
- PLC cabinets
- Network rooms
- Engineering workstations

### Finding

Physical access should be limited to authorized personnel according to job
responsibilities.

---

## 1.2 Fences

Perimeter fencing was reviewed as a first-layer physical security control.

Fencing can:

- Define the facility boundary.
- Deter unauthorized entry.
- Delay unauthorized access.
- Support security monitoring.

### Finding

Critical industrial facilities should use appropriate perimeter protection.

---

## 1.3 CCTV

CCTV was reviewed as a monitoring and detection mechanism.

Potential monitoring locations include:

- Facility entrances
- Security gates
- Control-room entrances
- Server rooms
- Restricted equipment areas

### Finding

CCTV can improve detection and provide evidence during investigations, but
should not be treated as the only physical security control.

---

# Task 1.2 - Case Study

A hypothetical water-treatment ICS facility was analyzed.

The facility contains:

- PLC control panels
- SCADA servers
- Operator workstations
- Network equipment
- Instrumentation equipment

The facility uses multiple physical controls:

1. Perimeter fencing
2. Controlled entrance
3. Electronic access cards
4. CCTV
5. Locked control rooms
6. Restricted server rooms
7. Visitor procedures

### Assessment

The controls provide defense in depth.

An unauthorized person would need to bypass multiple security layers before
reaching critical ICS equipment.

### Lesson Learned

Physical security should use multiple independent controls.

---

# Task 2 - Unauthorized Physical Access Risks

Potential risks identified:

1. Equipment damage
2. Unauthorized system access
3. Theft
4. Malware introduction
5. Unauthorized configuration changes
6. Network disruption
7. Control-system shutdown
8. Operational downtime
9. Safety impact
10. Data exposure

---

# Task 2.2 - Security Breach Scenario

## Scenario

An unauthorized individual enters an ICS control room and attempts to shut
down a monitoring application.

## Potential Impact

- Loss of operator visibility
- Loss of monitoring capability
- Operational disruption
- Potential safety consequences

## Recommended Controls

- Locked control-room doors
- Electronic access cards
- CCTV
- Security personnel
- Visitor management
- Workstation authentication
- Restricted user privileges

## Recommended Response

1. Detect unauthorized access.
2. Alert security personnel.
3. Restrict further access.
4. Preserve evidence.
5. Assess affected systems.
6. Verify ICS integrity.
7. Restore normal operations safely.
8. Document the incident.
9. Improve security controls.

---

# Task 3 - Hypothetical ICS Site Assessment

## Site Components

The hypothetical facility contains:

- Security gate
- Reception
- Control room
- SCADA/HMI systems
- Server/network room
- PLC/control equipment area
- CCTV coverage

---

# Vulnerability Assessment

## Vulnerability 1 - Uncontrolled Entrance

### Risk

Unauthorized personnel could enter the facility.

### Mitigation

- Electronic access control
- Visitor registration
- Security personnel
- Access logging

---

## Vulnerability 2 - CCTV Blind Spots

### Risk

Unauthorized activity may not be detected.

### Mitigation

- Improve camera placement
- Increase coverage
- Monitor security events
- Perform camera health checks

---

## Vulnerability 3 - Unlocked PLC Cabinets

### Risk

Unauthorized individuals could tamper with control equipment.

### Mitigation

- Lock PLC cabinets
- Restrict access
- Maintain access records
- Use tamper detection where appropriate

---

## Vulnerability 4 - Weak Server Room Protection

### Risk

Unauthorized access could expose critical ICS infrastructure.

### Mitigation

- Dedicated server room
- Electronic access control
- CCTV
- Visitor restrictions
- Environmental monitoring

---

## Vulnerability 5 - Poor Visitor Management

### Risk

Visitors could enter restricted areas without authorization.

### Mitigation

- Visitor identification
- Visitor badges
- Escort requirements
- Visitor logs
- Restricted visitor zones

---

# Task 4 - Open-Source Physical Security Software

ZoneMinder was reviewed as an example of open-source video surveillance
management software.

Potential capabilities include:

- Camera management
- Video monitoring
- Recording
- Event monitoring
- Security investigation

## Deployment Decision

ZoneMinder was not installed in this AWS training environment.

Reason:

The purpose of this laboratory is to understand and document physical security
concepts safely. A production-style CCTV deployment is unnecessary for
demonstrating the required learning objectives.

---

# Defense-in-Depth Model

The assessed facility can use the following layered model:

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
ICS Assets

---

# Security Findings

| Area | Finding | Risk | Recommendation |
|---|---|---|---|
| Perimeter | Must be controlled | Unauthorized entry | Fence and controlled gates |
| Entrance | Access must be restricted | Unauthorized access | Electronic access control |
| CCTV | Coverage must be sufficient | Detection gaps | Improve camera coverage |
| Control room | Critical area | System manipulation | Restricted access |
| PLC cabinets | Physical access risk | Equipment tampering | Lock cabinets |
| Server room | Critical infrastructure | Unauthorized access | Restricted room |
| Visitors | May require supervision | Unauthorized access | Visitor management |

---

# Safety Verification

The assessment was performed against a hypothetical ICS facility.

No real industrial facility was accessed.

No real PLC was contacted.

No SCADA system was contacted.

No CCTV system was accessed.

No physical security controls were bypassed.

No industrial process was modified.

No unauthorized testing was performed.

---

# Final Learning Assessment

The laboratory demonstrated that physical security is an important part of
ICS cybersecurity.

The assessment showed that:

- Unauthorized physical access can lead to cybersecurity consequences.
- Physical security should use defense in depth.
- Access controls reduce unauthorized entry.
- CCTV improves detection and investigation.
- Critical ICS equipment should have restricted physical access.
- Visitor management improves accountability.
- Physical and cybersecurity controls should work together.

---

# Completion Status

Task 1: Physical safeguards reviewed - COMPLETE

Task 2: Unauthorized access risks analyzed - COMPLETE

Task 3: Hypothetical ICS site assessed - COMPLETE

Task 4: Open-source security software reviewed - COMPLETE

Safety assessment - COMPLETE

Documentation - COMPLETE
