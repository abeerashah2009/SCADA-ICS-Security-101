# Lab 02 - ICS/SCADA Architecture Basics

## 📌 Lab Overview

This lab introduces the fundamental architecture of Industrial Control Systems (ICS) and Supervisory Control and Data Acquisition (SCADA) systems.

The lab focuses on understanding the four major ICS/SCADA layers:

- Field Layer
- Control Layer
- Supervisory Layer
- Enterprise Layer

It also covers important ICS components including:

- PLCs
- RTUs
- HMIs
- SCADA Servers
- Sensors
- Actuators

---

## 🎯 Objectives

By completing this lab, I learned how to:

- Understand the four main layers of an ICS/SCADA architecture.
- Identify the roles of PLCs, RTUs, and HMIs.
- Understand how industrial field devices communicate with control systems.
- Understand the relationship between the control, supervisory, and enterprise layers.
- Create and test a basic PLC Structured Text program.
- Simulate PLC logic using Python.
- Understand data and control flow within a water treatment plant example.

---

# Task 1 - Review Typical ICS/SCADA Layers

## 1.1 Field Layer

The Field Layer directly interacts with the physical industrial process.

### Main Components

- Sensors
- Actuators

### Examples

Sensors can measure:

- Temperature
- Pressure
- Flow
- Water level

Actuators can perform physical actions such as:

- Opening valves
- Starting pumps
- Controlling motors

---

## 1.2 Control Layer

The Control Layer processes information from field devices and performs real-time control.

### Main Components

- PLCs
- RTUs

### PLC

A Programmable Logic Controller (PLC) executes programmed control logic and performs real-time automation tasks.

### RTU

A Remote Terminal Unit (RTU) collects data from remote field devices and communicates the information to supervisory systems.

---

## 1.3 Supervisory Layer

The Supervisory Layer provides monitoring and operational control of the industrial process.

### Main Components

- SCADA Server
- HMI

### SCADA Server

A SCADA server collects and manages industrial process data and provides supervisory control capabilities.

### HMI

A Human-Machine Interface (HMI) provides a graphical interface through which operators monitor and interact with industrial processes.

---

## 1.4 Enterprise Layer

The Enterprise Layer connects operational technology (OT) environments with business and IT systems.

### Examples

- Business applications
- Data analytics
- Reporting
- Production management systems

---

# Task 1.2 - Key Component Identification

| Component | Full Name | Main Purpose | Example |
|---|---|---|---|
| RTU | Remote Terminal Unit | Collects and transmits remote field data | Oil pipeline monitoring |
| PLC | Programmable Logic Controller | Executes real-time control logic | Industrial automation |
| HMI | Human-Machine Interface | Provides operator visualization and control | Power generation |
| SCADA | Supervisory Control and Data Acquisition | Supervises and monitors industrial processes | Water treatment plant |

---

# Water Treatment Plant Case Study

A water treatment plant can use the four ICS/SCADA layers as follows:

### Field Layer

- Water Level Sensors
- Flow Sensors
- Pressure Sensors
- Pumps
- Valves

### Control Layer

- PLC
- RTU

### Supervisory Layer

- SCADA Server
- HMI

### Enterprise Layer

- Business Network
- Data Analytics
- Reporting

---

# Task 2 - Identifying RTUs, PLCs, and HMIs

## RTU

RTUs are commonly used in remote industrial environments.

### Example

An RTU can monitor pressure, temperature, and flow sensors along an oil pipeline and transmit the information to a supervisory system.

---

## PLC

PLCs are designed for automation tasks that require reliable and precise control logic.

### Example

A PLC can control robotic equipment in an automobile manufacturing plant.

---

## HMI

HMIs provide operators with a graphical interface for monitoring and interacting with industrial processes.

### Example

An HMI at a power generation facility can display:

- Turbine speed
- Temperature
- Pressure
- Performance information

---

# Component Comparison

| Component | Primary Role | Example |
|---|---|---|
| RTU | Remote data collection and communication | Oil pipeline |
| PLC | Real-time control | Manufacturing automation |
| HMI | Operator monitoring and interaction | Power generation |
| SCADA Server | Supervisory monitoring and control | Water treatment |

---

# Task 2.2 - Hands-On PLC Simulation

## PLC Structured Text Program

The following PLC program was created using IEC 61131-3 Structured Text syntax:

```iecst
PROGRAM PLC_PRG
VAR
    LED : BOOL;
END_VAR

LED := NOT LED;

END_PROGRAM
