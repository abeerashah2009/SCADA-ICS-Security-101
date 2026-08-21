# Task 2 — ICS/SCADA Environmental Factors Impact Assessment

## Assessment Objective

Evaluate environmental factors that can affect the security, reliability, and operational integrity of ICS/SCADA equipment.

The assessment focuses on:

- Dust and debris
- Temperature and heat
- Vibration
- Moisture
- Environmental monitoring
- Mitigation controls

---

## Lab Environment

This assessment was performed in an AWS EC2 Ubuntu environment.

The AWS environment does not contain a physical PLC cabinet, RTU enclosure, HMI cabinet, industrial control panel, or physical industrial sensors.

Therefore, direct measurement of industrial environmental conditions was not possible.

The assessment documents the environmental risks and appropriate mitigation controls for a real ICS/SCADA deployment.

---

# 1. Dust and Debris

## Risk

Dust and debris can accumulate inside equipment enclosures and ventilation systems.

Potential effects include:

- Reduced airflow
- Overheating
- Fan blockage
- Contamination of electrical components
- Reduced equipment lifespan
- Increased maintenance requirements

## Recommended Controls

A real industrial deployment should consider:

- Dust-resistant enclosures
- Appropriate enclosure ingress protection
- Sealed cable entry points
- Dust-proof gaskets
- Preventive cleaning schedules
- Filter maintenance
- Environmental inspections

## Assessment

No physical industrial enclosure was available for inspection.

**AWS Lab Status:** Not physically testable.

---

# 2. Heat and Temperature

## Risk

Excessive temperature can affect electronic equipment and reduce operational reliability.

Potential effects include:

- Component degradation
- Thermal shutdown
- Reduced equipment lifespan
- Communication failures
- Unexpected controller resets

## Recommended Controls

Possible mitigation measures include:

- Adequate ventilation
- Heat sinks
- Cooling fans
- Air conditioning where required
- Temperature monitoring
- Thermal alarms
- Equipment rated for the expected operating temperature

## Temperature Monitoring

Critical industrial environments should establish acceptable operating ranges for each device.

Environmental monitoring systems should generate alerts when temperatures approach defined thresholds.

## Assessment

No physical industrial temperature sensor was available in the AWS environment.

**AWS Lab Status:** Documentation only.

---

# 3. Vibration

## Risk

Industrial machinery can generate mechanical vibration that may affect electronic and electrical equipment.

Potential effects include:

- Loose connections
- Connector degradation
- Mechanical fatigue
- Circuit-board stress
- Sensor instability
- Equipment failure

## Recommended Controls

Where vibration is significant, facilities should consider:

- Vibration-dampening mounts
- Proper equipment mounting
- Secure cable management
- Periodic mechanical inspections
- Vibration monitoring
- Equipment rated for the operating environment

## Assessment

No industrial machinery or physical control cabinet was available for vibration testing.

**AWS Lab Status:** Not physically testable.

---

# 4. Moisture and Water Exposure

## Risk

Moisture can cause:

- Corrosion
- Electrical shorts
- Insulation degradation
- Component damage
- Equipment failure

## Recommended Controls

A real facility should consider:

- Appropriate enclosure protection
- Sealed cable entries
- Moisture monitoring
- Drainage
- Environmental alarms
- Proper equipment placement
- Corrosion-resistant materials

## Assessment

No physical enclosure was available for moisture testing.

**AWS Lab Status:** Documentation only.

---

# 5. Environmental Monitoring

Environmental monitoring should be considered for critical ICS/SCADA areas.

Potential monitoring parameters include:

| Parameter | Purpose |
|---|---|
| Temperature | Detect overheating |
| Humidity | Detect moisture risk |
| Dust | Detect contamination |
| Vibration | Detect mechanical stress |
| Water leakage | Detect flooding or leaks |
| Power quality | Detect electrical abnormalities |

Monitoring systems should provide alerts to appropriate operations or maintenance personnel.

---

# 6. Environmental Risk Assessment

| Environmental Factor | Potential Impact | Recommended Mitigation | AWS Lab Status |
|---|---|---|---|
| Dust | Overheating / contamination | Sealed enclosure, filters, cleaning | Not physically testable |
| Heat | Component degradation | Cooling and monitoring | Documentation only |
| Vibration | Loose connections / mechanical stress | Dampening and monitoring | Not physically testable |
| Moisture | Corrosion / electrical faults | Sealing and monitoring | Not physically testable |
| Water leakage | Equipment damage | Leak detection and drainage | Not physically testable |
| Poor ventilation | Heat accumulation | Thermal management | Documentation only |

---

# 7. Environmental Inspection Checklist

A real ICS/SCADA facility should periodically verify:

- [ ] Enclosure is free from excessive dust
- [ ] Ventilation openings are unobstructed
- [ ] Cooling equipment is operational
- [ ] Temperature is within the approved range
- [ ] Humidity is within the approved range
- [ ] No water leakage is present
- [ ] No corrosion is visible
- [ ] Equipment mounting is secure
- [ ] Excessive vibration is not present
- [ ] Environmental sensors are operational
- [ ] Environmental alarms are functional
- [ ] Maintenance records are current

---

# 8. Mitigation Strategy

Environmental protection should follow a layered approach.

### Layer 1 — Prevention

- Use suitable industrial enclosures.
- Protect cable entry points.
- Control temperature and humidity.
- Keep equipment areas clean.
- Install equipment according to manufacturer requirements.

### Layer 2 — Monitoring

- Monitor temperature.
- Monitor humidity.
- Monitor vibration where required.
- Monitor water leakage.
- Generate environmental alerts.

### Layer 3 — Response

When an environmental threshold is exceeded:

1. Generate an alert.
2. Notify appropriate personnel.
3. Determine whether equipment operation is affected.
4. Follow the approved operational response procedure.
5. Record the event.
6. Inspect affected equipment.
7. Correct the environmental condition.
8. Document the corrective action.

---

# 9. ICS/SCADA Operational Considerations

Environmental controls must not negatively affect the industrial process.

Any installation or modification involving:

- Cooling systems
- Sensors
- Cabinets
- Power supplies
- Monitoring equipment
- Network-connected environmental devices

should follow the organization's change-management and maintenance procedures.

Safety requirements should take priority when environmental conditions threaten personnel or process safety.

---

# Assessment Result

The AWS environment does not provide physical ICS/SCADA equipment or an industrial operating environment in which dust, heat, vibration, or moisture can be directly measured.

The lab therefore provides a documented environmental risk assessment and mitigation strategy suitable for planning a real ICS/SCADA physical hardening program.

No physical environmental sensor, cooling system, vibration mount, or enclosure modification is claimed to have been installed during this exercise.

---

# Evidence

This document records:

- Environmental risks
- Environmental impact analysis
- Recommended mitigation controls
- Environmental monitoring requirements
- Inspection checklist
- Response strategy
- AWS laboratory limitations
