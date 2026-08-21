# NIST SP 800-82 Review

## Document Reviewed

**Document:** NIST Special Publication 800-82 Revision 2  
**Title:** Guide to Industrial Control Systems (ICS) Security  
**Organization:** National Institute of Standards and Technology (NIST)

---

## 1. Purpose of NIST SP 800-82

NIST SP 800-82 provides guidance for improving the security of Industrial Control Systems (ICS).

The document addresses systems such as:

- Supervisory Control and Data Acquisition (SCADA)
- Distributed Control Systems (DCS)
- Programmable Logic Controllers (PLC)
- Industrial automation systems
- Other operational technology environments

The main purpose is to help organizations understand and manage cybersecurity risks while maintaining the safety, reliability, availability, and performance requirements of industrial systems.

---

## 2. Why ICS Security Is Different

ICS environments differ from traditional information technology environments.

Traditional IT security often prioritizes:

- Confidentiality
- Integrity
- Availability

ICS environments commonly place stronger emphasis on:

- Safety
- Availability
- Reliability
- Integrity
- Timely response

A cybersecurity control that is acceptable for an ordinary IT workstation may not be appropriate for a critical industrial controller.

For example, immediately rebooting an industrial system to install a security update may not be acceptable if the system is controlling an important industrial process.

---

## 3. Major ICS Security Risks

Important ICS security risks include:

### Cyber Attacks

Attackers may attempt to:

- Gain unauthorized access
- Modify control logic
- Manipulate industrial processes
- Disable monitoring
- Steal credentials
- Disrupt communications
- Install malicious software

### Physical Threats

ICS equipment may also be exposed to:

- Unauthorized physical access
- Equipment tampering
- Theft
- Environmental damage
- Damage to control cabinets
- Disconnection of communication equipment

### Legacy Technology

Many industrial environments contain older systems that may:

- Use outdated operating systems
- Have limited security capabilities
- Depend on specialized software
- Be difficult to patch
- Require long maintenance cycles

---

## 4. ICS Security Architecture

NIST recommends considering the architecture and communication paths of an ICS environment when designing security controls.

Important components may include:

- Enterprise network
- Industrial DMZ
- Control network
- Supervisory systems
- HMI systems
- PLCs
- RTUs
- Engineering workstations
- Field devices

Network segmentation can help limit the movement of attackers between enterprise IT systems and industrial control systems.

---

## 5. Network Segmentation

Network segmentation is an important ICS security practice.

Organizations should avoid unnecessarily exposing control systems directly to enterprise networks or the Internet.

Security architecture may use:

- Firewalls
- Industrial DMZs
- VLANs
- Access control lists
- Network monitoring
- Controlled remote access

The objective is to reduce unnecessary communication paths and limit the potential impact of a compromise.

---

## 6. Access Control

Access to ICS systems should be restricted to authorized personnel.

Important controls include:

- Strong authentication
- Role-based access
- Least privilege
- Account management
- Controlled administrative access
- Monitoring of privileged activity

Remote access should be carefully controlled because remote connectivity can increase the attack surface of an industrial environment.

---

## 7. Patch Management

ICS patch management requires additional planning compared with ordinary IT environments.

Before deploying patches, organizations should consider:

- Safety requirements
- Availability requirements
- Vendor support
- System compatibility
- Maintenance windows
- Testing requirements
- Backup and recovery procedures

Patches should be tested before deployment to critical ICS components whenever practical.

---

## 8. Malware Protection

ICS environments should use appropriate malware protection mechanisms.

However, security software must be tested carefully because aggressive security controls can potentially interfere with industrial applications.

Organizations should verify:

- Compatibility
- Performance impact
- Update procedures
- Detection capability
- Recovery procedures

---

## 9. Monitoring and Logging

ICS security requires effective monitoring.

Organizations should monitor:

- Authentication events
- Network traffic
- Configuration changes
- System events
- Security alerts
- Unauthorized activity
- Changes to industrial applications

Logs should be protected and retained according to organizational requirements.

---

## 10. Incident Response

ICS incident response must consider operational and safety consequences.

A response procedure should address:

- Detection
- Analysis
- Containment
- Eradication
- Recovery
- Lessons learned

However, immediately disconnecting or shutting down an ICS component may create safety or operational problems.

Incident response procedures should therefore be designed specifically for the industrial environment.

---

## 11. Backup and Recovery

Critical ICS configurations should be backed up.

Examples include:

- PLC programs
- HMI configurations
- SCADA configurations
- Network configurations
- Engineering workstation configurations
- Security device configurations

Backups should be protected from unauthorized modification and periodically tested for recovery.

---

## 12. Physical Security

Physical security is an important part of ICS security.

Controls may include:

- Restricted access to control rooms
- Locked control cabinets
- Visitor management
- Security monitoring
- Environmental protection
- Protection of engineering workstations

Cybersecurity controls alone cannot fully protect an industrial environment if unauthorized individuals can physically access critical equipment.

---

## 13. Key Takeaway

The most important lesson from NIST SP 800-82 is that ICS security must consider cybersecurity together with:

- Safety
- Reliability
- Availability
- Operational requirements
- Physical security
- Legacy technology
- Industrial processes

Security controls should be carefully selected and tested so that cybersecurity improvements do not unintentionally disrupt industrial operations.

---

## Conclusion

NIST SP 800-82 provides a useful foundation for understanding ICS cybersecurity.

The guidance emphasizes that industrial environments require security strategies that account for operational technology, safety, availability, reliability, physical access, legacy systems, and specialized industrial protocols.

For an effective ICS security program, organizations should combine technical controls with risk management, security policies, change management, monitoring, incident response, and recovery planning.
