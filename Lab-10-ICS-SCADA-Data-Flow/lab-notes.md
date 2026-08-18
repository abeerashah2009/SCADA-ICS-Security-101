# Lab 10 - ICS/SCADA Data Flow
## Detailed Laboratory Notes

---

## 1. Lab Information

**Lab Number:** 10

**Lab Name:** ICS/SCADA Data Flow

**Repository:** SCADA-ICS-Security-101

**Environment:** Ubuntu Linux on AWS EC2

**Lab Type:** Local ICS/SCADA simulation

---

## 2. Objective

The objective of this laboratory is to understand how process information
moves through a simplified Industrial Control System (ICS) and Supervisory
Control and Data Acquisition (SCADA) environment.

The simulated data path is:

```text
Sensor
   |
   v
PLC
   |
   v
SCADA Server
   |
   v
HMI / Operator
- The laboratory focuses on:

Sensor data generation
PLC processing
SCADA data collection
HMI/operator visibility
Data-flow analysis
Potential bottlenecks
Security weak points
Documentation of industrial data movement
---

## 3. ICS/SCADA Components
- 3.1 Sensor
 A sensor measures a physical property of an industrial process.

= Examples include:

Temperature
Pressure
Flow
Level
Vibration

In this laboratory, sensor values are simulated using software.

- 3.2 PLC

PLC stands for:

- Programmable Logic Controller

A PLC is an industrial controller used to monitor inputs and control
industrial equipment.

- Typical PLC responsibilities include:

Receiving sensor information
Executing control logic
Controlling actuators
Sending process information to supervisory systems

In this laboratory, the PLC is represented by a software simulation.

- 3.3 SCADA Server

SCADA stands for:

- Supervisory Control and Data Acquisition

A SCADA server collects information from industrial controllers and provides
supervisory monitoring and control functions.

- Typical SCADA responsibilities include:

Collecting PLC data
Recording process information
Generating alarms
Providing operator visibility
Supporting supervisory control

In this laboratory, the SCADA server is simulated using Python.

- 3.4 HMI

- HMI stands for:

Human-Machine Interface

An HMI provides operators with a way to view industrial process information.

- An HMI may display:

Temperature
Pressure
Flow
Alarms
Equipment status
Trends

The HMI is represented conceptually in this laboratory.
---

## 4. Simulated Data Flow

- The laboratory follows this path:

Physical Process
       |
       v
    Sensors
       |
       | Temperature
       | Pressure
       | Flow
       v
      PLC
       |
       | Process Data
       | Modbus-like Simulation
       v
  SCADA Server
       |
       | Supervisory Information
       v
 HMI / Operator

The simulation does not communicate with real industrial equipment.
---

## 5. Task 1 - Sensor to PLC

- The first stage of the laboratory represents sensors generating process data.

Example sensor values:

Temperature = 72.5 C
Pressure    = 4.8 bar
Flow        = 125.0 L/min

The simulated PLC receives these values.

The PLC representation demonstrates the role of a controller between field
devices and supervisory systems.

- Observation

The sensor is the source of process information.

The PLC acts as the control layer receiving and processing that information.

--- 
## 6. Task 2 - PLC to SCADA

- The simulated PLC forwards process information to the SCADA layer.

Example:

Sensor
  |
  v
PLC
  |
  | Temperature = 72.5 C
  | Pressure = 4.8 bar
  | Flow = 125.0 L/min
  v
SCADA Server

The SCADA server receives the process information for supervisory monitoring.

- Observation

The PLC performs control-related processing while the SCADA layer provides
supervisory visibility.
---

## 7. Task 3 - SCADA to HMI

- The SCADA server provides information to the HMI/operator.

Example:

SCADA Server
     |
     v
HMI
     |
     v
Operator

The operator may use the HMI to monitor:

Process values
Equipment status
Alarms
Trends

The HMI is therefore an important interface between the industrial process
and human operators.

---
## 8. Common Industrial Protocols

Industrial environments may use protocols such as:

Modbus

Modbus is a widely known industrial communication protocol.

It can be used to exchange process data between controllers and supervisory
systems.

DNP3

DNP3 is commonly associated with industrial and utility environments.

BACnet

BACnet is widely associated with building automation and control systems.

OPC

OPC-based technologies are commonly used for industrial data exchange and
integration.

The protocol behavior in this laboratory is simulated and does not represent
communication with a real industrial device.
---

## 9. Task 4 - Potential Bottlenecks

Several conditions can affect industrial data flow.

Network Latency

High latency can delay communication between devices.

Packet Loss

Lost packets may result in incomplete or delayed information.

Limited Bandwidth

Insufficient network capacity can affect communication performance.

Single Point of Failure

A single critical device or network path can become a major availability
risk.

Excessive Network Exposure

Industrial devices should not unnecessarily be exposed to untrusted networks.

---

## 10. Security Weak Points

- Potential security weaknesses include:

Poor network segmentation
Excessive access permissions
Weak authentication
Unencrypted legacy protocols
Inadequate monitoring
Unsupported operating systems
Poor change management
Lack of backups
Single points of failure

These are theoretical observations for this laboratory unless supported by
measured simulation results.
---

## 11. Data-Flow Security

- A secure ICS architecture should consider:

Enterprise Network
        |
      Firewall
        |
       DMZ
        |
      Firewall
        |
   Control Network
        |
       PLC
        |
     Sensors

Network segmentation can help limit unnecessary communication between
different security zones.

---

## 12. Availability and Reliability

- ICS environments often prioritize:

Safety
Availability
Reliability
Deterministic operation
Controlled change

This means security changes must be carefully tested before deployment.

A security control that unexpectedly stops an industrial process can itself
create operational risk.

---

## 13. Monitoring Considerations

Monitoring can help identify:

Unexpected communication
Abnormal traffic
New devices
Configuration changes
Communication failures
Unusual process values

Monitoring should be designed carefully so that it does not negatively affect
industrial operations.

--- 

## 14. Laboratory Safety

- This laboratory is intentionally designed as a local simulation.

- The following safety conditions apply:

No real PLC was contacted.
No real SCADA server was contacted.
No physical industrial equipment was contacted.
No production network was scanned.
No industrial process was modified.
No real Modbus traffic was required.
No external ICS device was targeted.

---

## 15. Evidence Collected

- The following evidence files are created for the laboratory:

README.md
lab-notes.md
data-flow-simulation.py
simulation-results.txt
data-flow-diagram.md

- These files provide documentation and reproducible evidence for the
laboratory portfolio.

---

## 16. Expected Simulation Results

The simulation should demonstrate:

Sensor data generated
        |
        v
PLC receives data
        |
        v
PLC processes data
        |
        v
SCADA receives data
        |
        v
HMI displays information

The simulation should also confirm that the operation is local and does not
contact real industrial devices.

---

## 17. Professional Security Observation

- A major lesson from this laboratory is that understanding data flow is
essential for ICS security.

Security teams need to understand:

What produces the data?
        |
        v
Who processes the data?
        |
        v
Who receives the data?
        |
        v
Who can modify the data?
        |
        v
What happens if communication fails?

This information helps identify critical assets and communication paths.

---

## 18. Key Takeaways

Remember:

Sensor = Collects physical process information

PLC = Performs industrial control

SCADA = Provides supervisory monitoring and control

HMI = Provides operator interaction

Data Flow = Movement of information between system components

Network Segmentation = Separates systems into security zones

Monitoring = Helps identify abnormal communication and activity

Availability = Critical requirement in industrial environments

---

## 19. Final Laboratory Conclusion

- This laboratory demonstrated the basic movement of information through a
simplified ICS/SCADA architecture.

- The simulated data flow was:

Sensor → PLC → SCADA Server → HMI / Operator

The laboratory also demonstrated how security teams can analyze communication
paths and identify potential weaknesses such as latency, packet loss,
unnecessary network exposure, weak authentication, and single points of
failure.

The entire exercise was performed using a local software simulation.

No real industrial devices or production systems were contacted.

---

## 20. Portfolio Learning Outcome

After completing this laboratory, the learner should be able to:

Explain basic ICS/SCADA data flow.
Identify the roles of sensors and PLCs.
Explain the purpose of a SCADA server.
Explain the purpose of an HMI.
Understand common industrial communication protocols.
Identify potential data-flow bottlenecks.
Identify common ICS security weaknesses.
Document an industrial data-flow architecture.
Perform safe local ICS/SCADA simulations.
