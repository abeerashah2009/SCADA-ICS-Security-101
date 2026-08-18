# Lab 10: ICS/SCADA Data Flow

## Lab Overview

This laboratory demonstrates the basic flow of industrial data through an
ICS/SCADA environment.

The simulated data path is:

Sensor → PLC → SCADA Server → Operator

The laboratory focuses on understanding how process data moves between
industrial components, identifying potential bottlenecks and security
weak points, and documenting the architecture.

## Objectives

- Understand the basic data flow in ICS/SCADA environments.
- Trace simulated sensor data to a PLC.
- Trace PLC data to a SCADA system.
- Identify potential bottlenecks and weak points.
- Understand common industrial communication protocols.
- Create a simple ICS/SCADA data-flow diagram.
- Document findings for a professional cybersecurity portfolio.

## ICS/SCADA Data Flow

A simplified industrial data flow can be represented as:

```text
Physical Process
      |
      v
   Sensors
      |
      | Process Data
      v
     PLC
      |
      | Industrial Protocol
      | Example: Modbus
      v
 SCADA Server
      |
      | Supervisory Data
      v
   HMI / Operator
Component Roles
Sensor

Sensors collect information from the physical environment.

Examples include:

Temperature
Pressure
Flow
Level
Vibration
PLC

PLC stands for Programmable Logic Controller.

The PLC receives field information, executes control logic, and may send
commands to industrial equipment.

SCADA Server

SCADA stands for Supervisory Control and Data Acquisition.

The SCADA server collects information from industrial controllers and
provides supervisory monitoring and control capabilities.

HMI

HMI stands for Human-Machine Interface.

It allows an operator to view process information, alarms, and system status.

Common Industrial Protocols

Examples of protocols that may be encountered in ICS/SCADA environments
include:

Modbus
DNP3
BACnet
OPC-based communication

The protocol used in this laboratory is a simulated representation and does
not communicate with a real industrial device.
## Laboratory Tasks
# Task 1: Trace Sensor-to-PLC Data Flow

- The laboratory simulation generates sensor values such as:

- Temperature
- Pressure
- Flow

The simulated values are passed to a PLC representation.

The process demonstrates how field data can move from sensors to a controller.
---
# Task 2: Trace PLC-to-SCADA Data Flow

- The simulated PLC processes the sensor values and forwards the information
to a simulated SCADA server.

The SCADA layer records the values for supervisory monitoring.
---
# Task 3: Identify Bottlenecks and Weak Points

- Potential weak points considered in this laboratory include:

Network latency
Packet loss
Limited bandwidth
Unnecessary network exposure
Lack of network segmentation
Lack of authentication
Unencrypted industrial protocols
Single points of failure

These observations are theoretical unless supported by measured laboratory
data.

# Task 4: Create a Data-Flow Diagram

- The laboratory includes a text-based network/data-flow diagram documenting
the movement of information.

The diagram represents:

Sensor
  |
  | Temperature / Pressure / Flow
  v
PLC
  |
  | Modbus-like simulated communication
  v
SCADA Server
  |
  | Supervisory Information
  v
HMI / Operator
Security Considerations

ICS environments have different priorities from normal IT environments.

- Important security considerations include:

Availability
Reliability
Safety
Network segmentation
Controlled access
Monitoring
Change management
Backup and recovery

Industrial protocols may also have limited built-in security features.

Therefore, additional controls such as firewalls, segmentation, monitoring,
and controlled access can be important.

Safety

This laboratory uses a local simulation.

No real PLCs, SCADA servers, industrial controllers, or physical processes
were contacted.

No real industrial network traffic was modified.

No production systems were scanned.

Evidence

- The laboratory evidence includes:

README.md
lab-notes.md
data-flow-simulation.py
simulation-results.txt
data-flow-diagram.md
Learning Outcome

After completing this laboratory, the learner should be able to explain the
basic movement of industrial data from sensors to PLCs and from PLCs to
SCADA systems.

The learner should also understand common data-flow weaknesses and the
importance of protecting communication paths in ICS/SCADA environments.
