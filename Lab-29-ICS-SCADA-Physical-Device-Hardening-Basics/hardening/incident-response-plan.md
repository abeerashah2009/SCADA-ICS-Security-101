# Task 3.2 — ICS/SCADA Physical Security Incident Response Plan

## 1. Purpose

This incident response plan defines the basic response process for physical security breaches and environmental failures affecting ICS/SCADA equipment.

The objective is to protect personnel safety, maintain operational integrity, preserve evidence, and restore affected equipment to an approved secure state.

---

## 2. Scope

This procedure applies to incidents involving:

- Unauthorized physical access
- Broken cabinet locks
- Damaged tamper-evident seals
- Open control cabinets
- Unauthorized cables or equipment
- Missing ICS/SCADA equipment
- Physical equipment damage
- Excessive temperature
- Excessive humidity
- Water leakage
- Excessive vibration
- Cooling-system failure
- Other environmental conditions that may affect control equipment

---

## 3. Safety First

Personnel safety and process safety take priority over security investigation activities.

If the condition creates an immediate safety risk:

1. Follow the site's emergency procedures.
2. Notify responsible operations personnel.
3. Do not interfere with safety systems.
4. Follow approved shutdown or emergency procedures where required.
5. Do not perform unauthorized equipment changes.

Security investigation should only continue when it is safe to do so.

---

## 4. Incident Identification

Potential indicators include:

- Broken tamper seals
- Damaged locks
- Open cabinets
- Unknown devices
- Unknown cables
- Missing equipment
- Unexpected hardware modifications
- Evidence of forced entry
- Excessive temperature
- Water leakage
- Environmental alarm
- Unusual vibration
- Cooling-system failure

The observation should be recorded as soon as practical.

---

## 5. Initial Response

When a physical security incident is identified:

1. Record the date and time.
2. Identify the affected asset or location.
3. Notify appropriate operations and security personnel.
4. Determine whether personnel safety is affected.
5. Determine whether the industrial process is affected.
6. Avoid unnecessary changes to the affected equipment.
7. Preserve relevant physical and electronic evidence.
8. Follow the organization's incident-response procedure.

---

## 6. Evidence Preservation

Evidence may include:

- Photographs of damaged equipment
- Tamper-seal numbers
- Access-control records
- CCTV records
- Maintenance records
- Asset inventory records
- Environmental monitoring records
- Network logs
- System alerts
- Change-management records

Evidence should be protected from unauthorized modification.

Investigators should document who collected the evidence and when it was collected.

---

## 7. Physical Tampering Response

If physical tampering is suspected:

1. Restrict unnecessary access to the affected area.
2. Record the condition of the equipment.
3. Verify the asset identity.
4. Check access records.
5. Compare the current condition with approved documentation.
6. Determine whether unauthorized hardware or cabling was introduced.
7. Notify security and operations personnel.
8. Assess whether equipment integrity may have been affected.
9. Follow approved recovery procedures.
10. Document the final disposition.

No equipment should be removed, modified, or reset solely for convenience unless authorized or required for safety.

---

## 8. Environmental Failure Response

Environmental failures may include:

- High temperature
- High humidity
- Water leakage
- Cooling failure
- Excessive vibration
- Dust contamination

Response should include:

1. Confirm the environmental alarm or observation.
2. Notify responsible personnel.
3. Determine whether equipment operation is affected.
4. Correct the environmental condition using approved procedures.
5. Inspect affected equipment.
6. Record the incident.
7. Determine whether maintenance is required.
8. Verify that environmental conditions have returned to an acceptable range.

---

## 9. Recovery

Recovery activities should follow approved operational and maintenance procedures.

Possible actions include:

- Repairing damaged enclosures
- Replacing damaged locks
- Replacing tamper seals
- Removing unauthorized equipment
- Correcting environmental conditions
- Restoring cooling
- Inspecting affected equipment
- Verifying equipment configuration
- Performing approved functional checks

Recovery should not introduce unapproved changes into the ICS/SCADA environment.

---

## 10. Post-Incident Review

After the incident:

- Determine the root cause.
- Review physical access records.
- Review maintenance records.
- Review environmental logs.
- Identify security-control failures.
- Identify required corrective actions.
- Update the asset inventory if necessary.
- Update procedures where appropriate.
- Record lessons learned.

Corrective actions should be tracked to completion.

---

## 11. Roles and Responsibilities

| Role | Responsibility |
|---|---|
| Operations | Maintain process safety and operational continuity |
| Security | Investigate physical security events |
| Maintenance | Inspect and repair physical equipment |
| Engineering | Assess technical impact |
| Management | Approve major corrective actions |
| Incident Response Team | Coordinate investigation and recovery |

Responsibilities should be adapted to the organization's structure.

---

## 12. Incident Documentation Template

| Field | Information |
|---|---|
| Incident ID | To be assigned |
| Date/Time | To be recorded |
| Location | To be recorded |
| Asset | To be identified |
| Incident Type | Physical / Environmental |
| Initial Observation | To be documented |
| Safety Impact | To be assessed |
| Operational Impact | To be assessed |
| Evidence Collected | To be recorded |
| Personnel Notified | To be recorded |
| Corrective Action | To be documented |
| Recovery Status | To be documented |
| Final Review | To be completed |

---

## 13. AWS Lab Limitation

This exercise was performed in an AWS EC2 environment.

The environment does not contain physical PLC cabinets, industrial control rooms, physical access-control systems, or industrial environmental monitoring equipment.

Therefore, no physical breach or environmental failure was actually simulated or physically remediated.

This document represents an incident-response planning exercise for a real ICS/SCADA environment.

---

## Assessment Result

A documented response process was developed for physical security breaches and environmental failures.

The procedure addresses:

- Incident identification
- Safety considerations
- Initial response
- Evidence preservation
- Physical tampering
- Environmental failures
- Recovery
- Post-incident review
- Roles and responsibilities
- Incident documentation

No claim is made that a real physical security incident occurred during this AWS-based laboratory exercise.

---

## Evidence

This document provides the incident-response component of Lab 29 and complements:

- `enclosure-assessment.md`
- `security-enhancements.md`
- `environmental-assessment.md`
- `physical-security-policy.md`
