# ISA/IEC 62443 vs NERC CIP

## Purpose

ISA/IEC 62443 and NERC CIP both address cybersecurity for critical industrial environments, but they have different scopes and purposes.

ISA/IEC 62443 is a family of standards focused on cybersecurity for industrial automation and control systems.

NERC CIP is a set of mandatory cybersecurity requirements for qualifying organizations and systems associated with the North American Bulk Electric System.

## Comparison

| Area | ISA/IEC 62443 | NERC CIP |
|---|---|---|
| Primary focus | Industrial automation and control systems | North American Bulk Electric System |
| Main sectors | Manufacturing, process control, energy, and other IACS environments | Bulk electric power sector |
| Approach | Risk-based standards and security lifecycle | Regulatory compliance requirements |
| Security architecture | Zones and conduits | Electronic Security Perimeters and access controls |
| Security levels | Uses Security Levels (SL) | Uses BES Cyber System categorization |
| Asset focus | Industrial automation and control components and systems | Qualifying BES Cyber Systems and associated assets |
| Personnel security | Addressed within relevant security lifecycle requirements | Explicit personnel and training requirements |
| Incident response | Supports lifecycle security and incident management | CIP-008 focuses on incident reporting and response planning |
| Recovery | Supports lifecycle maintenance and recovery practices | CIP-009 focuses on recovery plans |
| Applicability | Broad industrial environments | Qualifying North American BES environments |
| Laboratory status | Used as an educational reference | Used as an educational reference |

## Key Differences

### ISA/IEC 62443

ISA/IEC 62443 provides a structured approach to securing industrial automation and control systems.

Important concepts include:

- Security lifecycle management.
- Risk assessment.
- Security Levels.
- Zones and conduits.
- System and component security.
- Secure development and maintenance.

### NERC CIP

NERC CIP focuses specifically on cybersecurity requirements associated with the North American Bulk Electric System.

Important concepts include:

- BES Cyber System categorization.
- Security management controls.
- Personnel and training.
- Electronic access controls.
- Physical security.
- System security management.
- Incident response.
- Recovery planning.

## Relationship Between the Frameworks

The frameworks can complement each other in organizations where industrial control systems are part of the electric power sector.

For example:

- ISA/IEC 62443 can help structure the technical security architecture of industrial systems.
- NERC CIP can provide applicable regulatory requirements for qualifying power-sector cyber systems.
- Both emphasize risk management, access control, monitoring, incident response, and maintaining secure operations.

They should not be treated as identical frameworks.

## Laboratory Mapping

The simulated Lab 39 PLC and HMI configurations can be used to demonstrate several general compliance concepts.

### PLC

Example controls:

- Configuration management.
- Version control.
- Change tracking.
- Hash verification.
- Security configuration review.

### HMI

Example controls:

- Configuration management.
- Controlled communication with the PLC.
- Remote-access restrictions.
- Change documentation.

### Monitoring

The Lab 39 configuration-review script demonstrates a basic control verification process.

The script compares current configuration SHA-256 hashes against an approved baseline stored in the CMDB.

## Important Limitation

The laboratory does not demonstrate formal certification or regulatory compliance.

The Ubuntu environment and simulated PLC/HMI configurations are educational examples only.

Actual compliance requires:

- Applicable scope determination.
- Formal risk assessment.
- Organization-specific policies.
- Required technical and administrative controls.
- Documented evidence.
- Periodic assessments.
- Applicable regulatory or certification processes.

## Key Takeaway

ISA/IEC 62443 and NERC CIP address different but related cybersecurity needs.

ISA/IEC 62443 is useful for designing and managing cybersecurity in industrial automation and control environments.

NERC CIP establishes cybersecurity requirements for qualifying entities and cyber systems associated with the North American Bulk Electric System.

Understanding the difference allows security teams to select and apply the appropriate requirements to their operational environment.
