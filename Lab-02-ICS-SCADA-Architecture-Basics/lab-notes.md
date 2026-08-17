# Lab 02 - ICS/SCADA Architecture Basics

## Task 1 - Review Typical Layers in ICS/SCADA Systems

### 1.1 ICS/SCADA Layers

#### Field Layer
The Field Layer directly interacts with the physical industrial process.

Main components:
- Sensors
- Actuators

Sensors collect information such as temperature, pressure, flow, and level.

Actuators perform physical actions such as opening valves, starting motors, or controlling pumps.

#### Control Layer
The Control Layer processes information from field devices and makes real-time control decisions.

Main components:
- PLCs
- RTUs

PLCs execute programmed control logic.

RTUs collect and transmit field data and can also perform control functions.

#### Supervisory Layer
The Supervisory Layer provides monitoring and operational control of the industrial process.

Main components:
- SCADA servers
- HMIs

HMIs allow operators to view process information and interact with the control system.

#### Enterprise Layer
The Enterprise Layer connects operational technology with business and IT systems.

Examples:
- Business applications
- Data analytics
- Production management systems
- Reporting systems

### 1.2 Key Components

#### RTU - Remote Terminal Unit
RTUs collect data from remote field devices and communicate the information to supervisory or control systems.

Example:
An RTU can monitor pressure and flow sensors along an oil pipeline.

#### PLC - Programmable Logic Controller
A PLC executes programmed control logic and performs real-time automation tasks.

Example:
A PLC can control motors and robotic equipment in an automobile manufacturing plant.

#### HMI - Human-Machine Interface
An HMI provides a graphical interface that allows operators to monitor and interact with industrial processes.

Example:
An HMI can display turbine temperature, speed, and performance at a power generation facility.

### Water Treatment Plant Example

A basic water treatment architecture can contain:

Field Layer:
- Water level sensors
- Flow sensors
- Pressure sensors
- Pumps
- Valves

Control Layer:
- PLCs
- RTUs

Supervisory Layer:
- SCADA server
- HMI

Enterprise Layer:
- Business network
- Reporting
- Data analytics
## Task 2 - Identifying RTUs, PLCs, and HMIs

### 2.1 Analysis of Components

#### RTU - Remote Terminal Unit

RTUs are commonly used in remote industrial environments where PLC deployment may be difficult.

Example:
An RTU can be used in an oil pipeline monitoring system to collect information from pressure, temperature, and flow sensors and transmit the data to the supervisory system.

#### PLC - Programmable Logic Controller

PLCs are designed for automation tasks that require precise and reliable control logic.

Example:
A PLC can control robotic assembly equipment in an automobile manufacturing plant.

#### HMI - Human-Machine Interface

HMIs provide operators with a graphical interface for monitoring and interacting with industrial processes.

Example:
An HMI at a power generation facility can display turbine speed, temperature, pressure, and performance information.

### Component Comparison

| Component | Main Purpose | Example |
|---|---|---|
| RTU | Collect and transmit remote field data | Oil pipeline monitoring |
| PLC | Execute real-time control logic | Automobile robotic assembly |
| HMI | Provide operator visualization and control | Power generation facility |
## 2.2 Hands-On PLC Simulation

### PLC Program

The following Structured Text program was created according to the lab instructions:

```iecst
PROGRAM PLC_PRG
VAR
    LED : BOOL;
END_VAR

LED := NOT LED;

END_PROGRAM
