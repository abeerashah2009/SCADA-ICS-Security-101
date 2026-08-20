# Lab 25: Incident Response Basics for ICS/SCADA

## Professional Portfolio Project

This lab demonstrates the fundamentals of **incident response in Industrial Control Systems (ICS) and Supervisory Control and Data Acquisition (SCADA) environments**.

The project focuses on developing an ICS-specific incident response approach, defining response-team responsibilities, creating an incident response plan, identifying containment strategies, and understanding how network segmentation and intrusion detection can support incident handling.

Unlike traditional IT environments, ICS environments require security decisions to consider **safety, availability, reliability, process integrity, and operational continuity**.

---

## Objectives

- Understand the incident response lifecycle in ICS/SCADA environments.
- Identify key roles and responsibilities within an ICS incident response team.
- Develop an ICS-specific incident response plan.
- Identify appropriate containment and isolation strategies.
- Understand the importance of network segmentation.
- Understand the role of IDS and network monitoring.
- Develop recovery and post-incident procedures.
- Document incident response activities professionally.
- Apply cybersecurity concepts to operational technology (OT) environments.

---

## ICS/SCADA Security Context

ICS/SCADA systems are used to monitor and control physical processes across critical infrastructure and industrial environments.

Examples include:

- Manufacturing
- Power generation and distribution
- Water and wastewater treatment
- Oil and gas
- Transportation
- Building automation
- Industrial production

A cybersecurity incident affecting an ICS environment can potentially result in:

- Process disruption
- Equipment damage
- Loss of operator visibility
- Unauthorized control
- Production downtime
- Safety incidents
- Financial losses

Therefore, ICS incident response must balance **cybersecurity, safety, and operational continuity**.

---

## Lab Environment

| Component | Details |
|---|---|
| Platform | Linux / Ubuntu |
| Environment | Fresh lab environment |
| Lab Type | ICS/SCADA Incident Response |
| Network | Simulated ICS/SCADA environment |
| Primary Focus | Incident Response and Containment |

> **Note:** Each lab in this training project uses a new/fresh environment. Results such as IP addresses, installed packages, running services, and network interfaces may therefore differ between labs.

---

# Task 1: ICS Incident Response Roles

An effective ICS incident response process requires clearly defined responsibilities.

## 1. Incident Response Leader

### Responsibilities

- Coordinate incident response activities.
- Establish incident priorities.
- Communicate with management and stakeholders.
- Coordinate technical and operational teams.
- Ensure safety requirements are considered.
- Maintain incident documentation.

### Primary Goal

Maintain overall control of the incident response process while ensuring that cybersecurity actions do not create unsafe operational conditions.

---

## 2. SCADA/ICS Engineer

### Responsibilities

- Understand the affected industrial process.
- Analyze SCADA and control-system behavior.
- Identify abnormal system activity.
- Assess the operational impact of an incident.
- Recommend safe isolation procedures.
- Coordinate system shutdown or recovery when required.

### Primary Goal

Protect the industrial process and maintain safe and reliable operations.

---

## 3. IT Security Analyst

### Responsibilities

- Investigate suspicious activity.
- Analyze logs and network traffic.
- Perform security analysis.
- Identify potential attack vectors.
- Support containment activities.
- Perform root-cause analysis.
- Recommend security controls.

### Primary Goal

Identify, contain, and mitigate the cybersecurity threat.

---

## 4. Communications Officer

### Responsibilities

- Maintain clear communication during the incident.
- Provide status updates to authorized stakeholders.
- Coordinate internal communications.
- Manage external communication when authorized.
- Maintain communication records.

### Primary Goal

Ensure accurate and controlled communication throughout the incident.

---

# Task 2: ICS/SCADA Incident Response Plan

## 1. Preparation

Preparation activities should include:

- Establishing incident response procedures.
- Identifying critical ICS assets.
- Maintaining network diagrams.
- Maintaining asset inventories.
- Defining response-team responsibilities.
- Establishing communication procedures.
- Preparing system backups.
- Establishing monitoring and logging capabilities.

---

## 2. Incident Detection

Potential indicators of an ICS security incident include:

- Unexpected network traffic
- Unauthorized login attempts
- Unexpected configuration changes
- Abnormal PLC activity
- Unexpected SCADA commands
- Loss of communication with field devices
- Unusual system performance
- Unexpected changes in process values
- Suspicious authentication events

Monitoring sources may include:

- Network monitoring
- IDS/IPS
- Firewall logs
- Authentication logs
- SCADA logs
- Windows/Linux system logs
- SIEM platforms

---

## 3. Incident Notification

When suspicious activity is detected:

1. Record the initial observation.
2. Identify the affected asset.
3. Determine the potential operational impact.
4. Notify the appropriate response team.
5. Escalate according to the incident severity.
6. Maintain an incident timeline.

---

## 4. Containment

Containment should be performed carefully because aggressive actions can disrupt industrial processes.

Possible containment techniques include:

- Isolating compromised hosts.
- Restricting suspicious network connections.
- Blocking unauthorized traffic.
- Separating affected network segments.
- Disabling compromised accounts.
- Restricting remote access.
- Increasing network monitoring.
- Preventing lateral movement.

> **ICS Safety Principle:** Do not disconnect or shut down critical control equipment without understanding the operational and safety consequences.

---

## 5. Eradication

After containment, the response team can investigate and remove the underlying threat.

Activities may include:

- Identifying the root cause.
- Removing malicious software.
- Removing unauthorized accounts.
- Correcting insecure configurations.
- Applying approved security updates.
- Resetting compromised credentials.
- Removing unauthorized access mechanisms.
- Validating system integrity.

---

## 6. Recovery

Recovery should be performed in a controlled manner.

Typical recovery activities include:

1. Restore systems from trusted backups.
2. Validate system configurations.
3. Verify security controls.
4. Test communication between systems.
5. Confirm normal SCADA operation.
6. Monitor systems for recurring suspicious activity.
7. Gradually return systems to normal operation.

---

## 7. Lessons Learned

After the incident:

- Conduct a post-incident review.
- Document what happened.
- Identify the root cause.
- Evaluate the effectiveness of the response.
- Identify security gaps.
- Update incident response procedures.
- Improve monitoring capabilities.
- Update network segmentation where required.
- Provide security awareness training.
- Record recommendations for future incidents.

---

# Task 3: ICS Containment Strategies

## Strategy 1: Host Isolation

A potentially compromised system may be isolated from the network to prevent further spread.

Possible approaches include:

- Removing network connectivity.
- Restricting firewall access.
- Moving systems into an isolated VLAN.
- Blocking communication with suspicious hosts.

Isolation should always consider the operational impact on the industrial process.

---

## Strategy 2: Network Segmentation

Network segmentation separates critical and non-critical systems.

Example logical architecture:

```text
                    Enterprise IT
                         |
                    Firewall
                         |
                    DMZ Network
                         |
                    ICS Firewall
                         |
              -----------------------
              |                     |
        SCADA Network          Engineering
              |                 Workstations
              |
        ----------------
        |              |
       PLCs           RTUs
        |              |
     Sensors        Field Devices
