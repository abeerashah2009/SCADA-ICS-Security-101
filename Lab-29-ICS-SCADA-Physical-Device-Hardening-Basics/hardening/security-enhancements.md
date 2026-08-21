# Task 1.2 — Physical Security Enhancement Plan

## Objective

Document practical physical security enhancements that should be applied to ICS/SCADA equipment to reduce the risk of unauthorized physical access and tampering.

Because this lab is performed in an AWS EC2 environment, physical locks, seals, biometric systems, and enclosure modifications cannot be physically installed. The controls are therefore documented as an implementation plan for a real ICS/SCADA environment.

---

## 1. Tamper-Evident Seals

### Purpose

Tamper-evident seals provide visible evidence that an enclosure or access panel may have been opened.

### Recommended Implementation

Use numbered or serialized security seals on:

- PLC control cabinets
- RTU enclosures
- HMI cabinets
- Network cabinets
- Remote communication equipment
- Critical control panels

### Inspection Procedure

During periodic inspections:

1. Verify the seal number against the asset record.
2. Check whether the seal is intact.
3. Look for evidence of removal or replacement.
4. Record the inspection date.
5. Report unexpected seal changes as a security event.

### AWS Lab Status

Not physically installed.

**Status:** Documentation only.

---

## 2. Physical Locks

### Purpose

Mechanical locks restrict unauthorized access to critical equipment.

### Recommended Implementation

Appropriate locking mechanisms should be installed on cabinets containing critical ICS/SCADA equipment.

Access should be limited to authorized personnel.

### Access Management

The organization should maintain:

- Authorized personnel list
- Key or access-card inventory
- Access approval process
- Periodic access review
- Lost-key/card reporting procedure

### AWS Lab Status

No physical cabinet was available.

**Status:** Recommended control; not physically implemented.

---

## 3. Electronic Access Control

### Purpose

Electronic access controls provide stronger accountability for physical access.

Possible technologies include:

- Access cards
- Badge readers
- PIN-based access
- Biometric authentication
- Security monitoring systems

### ICS/SCADA Considerations

Physical access controls should not introduce unacceptable operational or safety risks.

Emergency access procedures should be documented.

Access logs should be retained according to organizational requirements.

### AWS Lab Status

No physical access-control system was available.

**Status:** Documentation only.

---

## 4. Protected Cable Entry

Cable openings should be protected to prevent:

- Unauthorized cable connections
- Cable damage
- Dust ingress
- Moisture ingress
- Accidental disconnection
- Tampering

Recommended controls include:

- Cable glands
- Sealed entry points
- Appropriate conduit
- Strain relief
- Physical cable protection

---

## 5. Enclosure Security Requirements

| Security Control | Recommended Status | AWS Lab Status |
|---|---|---|
| Mechanical enclosure | Required | Not physically testable |
| Physical lock | Required where appropriate | Not installed |
| Tamper-evident seal | Recommended | Not installed |
| Protected cable entry | Required | Not physically testable |
| Access control | Required for critical areas | Not available |
| Access logging | Recommended | Not available |
| Periodic inspection | Required | Documentation only |
| Asset identification | Required | Documentation only |

---

## 6. Physical Inspection Checklist

A real ICS/SCADA facility should periodically verify:

- [ ] Enclosure is locked
- [ ] No unauthorized access is evident
- [ ] Tamper seals are intact
- [ ] Cabinet panels are secure
- [ ] Hinges and fasteners are intact
- [ ] Cable entries are protected
- [ ] No exposed wiring exists
- [ ] No unauthorized equipment is present
- [ ] Asset identification is visible
- [ ] Environmental protection is adequate
- [ ] Access records are maintained

---

## 7. Security Response to Tampering

If evidence of unauthorized physical access is discovered:

1. Do not immediately modify or disturb the evidence unless safety requires it.
2. Notify the appropriate security/operations personnel.
3. Record the affected asset.
4. Document the observed condition.
5. Review physical access records.
6. Determine whether equipment integrity may have been affected.
7. Follow the organization's incident-response procedure.
8. Restore the equipment to an approved secure state.

---

## Assessment Result

The AWS environment does not contain physical ICS/SCADA cabinets or industrial devices on which these controls can be installed.

The lab therefore documents the required physical security enhancements and their expected implementation in a real industrial environment.

No physical lock, tamper seal, biometric reader, or enclosure modification is claimed to have been installed during this exercise.

---

## Evidence

This document provides the implementation plan for:

- Tamper-evident seals
- Physical locks
- Electronic access control
- Protected cable entry
- Physical inspection
- Tamper response
