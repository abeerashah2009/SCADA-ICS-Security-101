# Lab 09: Basic ICS/SCADA System Exploration

## Lab Overview

This laboratory introduces the basic operation of an Industrial Control
System (ICS) and Supervisory Control and Data Acquisition (SCADA)
environment through a safe simulated environment.

The lab focuses on understanding PLC concepts, Modbus communication,
registers, simulated data points, and basic read/write operations.

No real industrial devices are contacted during this laboratory.

---

## Objectives

By completing this laboratory, the following objectives will be achieved:

1. Understand the basic components of an ICS/SCADA system.
2. Understand the role of a PLC in an industrial environment.
3. Explore Modbus communication concepts.
4. Understand simulated holding registers and data points.
5. Perform safe simulated read and write operations.
6. Document simulated device configuration.
7. Record laboratory results for portfolio documentation.

---

## ICS/SCADA Components

A basic ICS/SCADA environment may contain:

- PLC
- HMI
- SCADA Server
- RTU
- Sensors
- Actuators
- Industrial communication protocols

### PLC

PLC stands for Programmable Logic Controller.

A PLC is an industrial computer used to control physical processes.

Examples of equipment controlled by PLCs include:

- Motors
- Pumps
- Valves
- Conveyors
- Production machinery

### HMI

HMI stands for Human-Machine Interface.

An HMI allows operators to monitor and interact with industrial processes.

### SCADA

SCADA stands for Supervisory Control and Data Acquisition.

SCADA systems provide supervisory monitoring, data collection,
alarms, visualization, and control functions.

---

## Modbus

Modbus is an industrial communication protocol commonly used to exchange
data between industrial devices.

Common Modbus concepts include:

- Coils
- Discrete Inputs
- Input Registers
- Holding Registers

### Holding Registers

Holding registers are commonly used to store numeric values that can
be read and, depending on permissions and device configuration, written.

For this laboratory, holding registers are simulated locally.

---

## Laboratory Environment

The laboratory is performed in an Ubuntu Linux environment running in
an AWS EC2 instance.

The environment is used only for educational simulation.

No real PLC, HMI, SCADA server, RTU, or industrial process is contacted.

---

## Practical Tasks

### Task 1: Environment Verification

Identify:

- Operating system
- Kernel
- CPU architecture
- Python version
- Java availability

### Task 2: PLC/Modbus Simulation

Create a safe local simulation representing a PLC with Modbus-style
holding registers.

Example simulated registers:

| Register | Example Value |
|----------|---------------|
| 1        | 125           |
| 2        | 78            |
| 3        | 100           |
| 4        | 45            |

### Task 3: Read Operation

Read a simulated holding register and display its value.

### Task 4: Write Operation

Modify a simulated register value and verify the new value.

### Task 5: Documentation

Record:

- Initial register values
- Read operation
- Write operation
- Final register values
- Environment information
- Safety observations

---

## Safety

This laboratory is intentionally limited to a local simulation.

The laboratory:

- Does not scan external systems.
- Does not contact real PLCs.
- Does not modify industrial equipment.
- Does not interact with production systems.
- Does not perform unauthorized network activity.

---

## Expected Learning Outcome

After completing this laboratory, the learner should understand:

- What a PLC does.
- What Modbus is used for.
- What holding registers represent.
- How industrial data points can be simulated.
- How read/write operations work conceptually.
- Why testing should be performed in an isolated environment.

---

## Portfolio Evidence

The completed laboratory should contain:

- README.md
- lab-notes.md
- Environment verification script
- Simulation script
- Simulation results
- Git commit and GitHub repository history

---

## Conclusion

This laboratory provides a beginner-friendly introduction to ICS/SCADA
system exploration using a safe simulated environment.

The practical exercises demonstrate how PLC-style data points and Modbus
register operations can be represented without connecting to real
industrial infrastructure.
