# Lab 03 - ICS/SCADA Terminology

## Objectives

- Understand key terminology used in ICS/SCADA systems.
- Differentiate ICS from traditional IT systems.
- Explore real-world examples of ICS usage.

---

# Task 1 - Compile a Glossary of Terms

## 1.1 Key ICS/SCADA Terms

### PLC - Programmable Logic Controller

A PLC is an industrial computer designed to control machines and automated processes.

**Main purpose:**
- Execute control logic
- Monitor inputs
- Control outputs
- Automate industrial processes

**Example:**

A PLC can control the sequence of machines in a chemical production process.

---

### RTU - Remote Terminal Unit

An RTU is a specialized industrial device used to collect data from remote field devices and communicate that information to a central supervisory system.

**Main purpose:**
- Collect sensor data
- Monitor remote equipment
- Send telemetry data
- Perform control functions

**Example:**

RTUs can monitor pressure, temperature, and flow in an oil pipeline.

---

### HMI - Human-Machine Interface

An HMI is a graphical interface that allows operators to monitor and interact with industrial processes.

**Main purpose:**
- Display real-time process information
- Show alarms and system status
- Allow operator control
- Provide visualization

**Example:**

An HMI touchscreen can display temperature, pressure, and machine status in a manufacturing plant.

---

### DCS - Distributed Control System

A DCS is a control system in which control functions are distributed across multiple controllers rather than being handled by one central controller.

**Main purpose:**
- Distributed process control
- Continuous monitoring
- Automation
- Process optimization

**Example:**

DCS technology is commonly used in power plants and chemical processing facilities.

---

### SCADA - Supervisory Control and Data Acquisition

SCADA is a system architecture used to monitor and supervise industrial processes and collect data from field devices.

**Main purpose:**
- Supervisory monitoring
- Data collection
- Alarm management
- Process visualization
- Remote control

**Example:**

SCADA systems are used in water treatment and water distribution plants.

---

## Glossary Comparison

| Term | Full Form | Main Purpose | Example |
|---|---|---|---|
| PLC | Programmable Logic Controller | Real-time machine/process control | Chemical production |
| RTU | Remote Terminal Unit | Remote data collection and control | Oil pipeline |
| HMI | Human-Machine Interface | Operator visualization and interaction | Manufacturing plant |
| DCS | Distributed Control System | Distributed process control | Power plant |
| SCADA | Supervisory Control and Data Acquisition | Supervisory monitoring and data acquisition | Water treatment |

---

# Task 2 - ICS vs Traditional IT Systems

## What is ICS?

Industrial Control Systems (ICS) are systems that combine control components such as electrical, mechanical, hydraulic, and pneumatic devices to perform specific functions within an industrial process.

Examples include:

- Power generation
- Water treatment
- Manufacturing
- Oil and gas
- Chemical processing
- Transportation

---

## ICS vs Traditional IT

| Area | ICS | Traditional IT |
|---|---|---|
| Primary purpose | Control physical processes | Manage information and computing resources |
| Operation | Often real-time | Usually less time-critical |
| Main priority | Safety and availability | Confidentiality, integrity and availability |
| System lifecycle | Often long | Usually shorter |
| Downtime | Can affect physical processes and safety | Usually affects business operations |
| Hardware | PLCs, RTUs, sensors, actuators | Servers, PCs, laptops |
| Environment | Industrial/physical environment | Office/data-center environment |
| Updates | Carefully planned and tested | More frequently updated |

---

## Important Differences

### 1. Real-Time Operations

ICS often needs to respond to physical events in real time.

For example, a PLC may need to immediately stop a motor when a dangerous condition is detected.

### 2. Safety Requirements

ICS environments must consider physical safety because failures can affect people, equipment, and the environment.

### 3. Long Lifecycle

ICS equipment can remain operational for many years or decades.

Replacing or upgrading industrial equipment can be expensive and may interrupt production.

### 4. Availability and Operational Continuity

ICS environments strongly emphasize availability and continuous operation.

An outage can stop production or affect critical infrastructure.

Traditional IT environments often place greater emphasis on confidentiality and data integrity.

---

# Task 3 - Real-World ICS Usage

## Case Study 1 - Smart Grid

A smart grid uses ICS/SCADA technologies to monitor and control electrical power networks.

### Components

- RTUs
- PLCs
- HMIs
- SCADA systems
- Sensors
- Control equipment

### How it works

1. Sensors collect electrical measurements.
2. RTUs and PLCs collect and process field information.
3. Data is transmitted to supervisory systems.
4. SCADA systems display information to operators.
5. Operators monitor and control electrical infrastructure.

### Benefits

- Real-time monitoring
- Faster fault detection
- Improved reliability
- Better power distribution management
- Operational visibility

---

## Case Study 2 - Water Treatment Plant

Water treatment facilities use ICS/SCADA systems to monitor and control water treatment processes.

### Components

- Sensors
- PLCs
- RTUs
- SCADA servers
- HMIs
- Pumps
- Valves
- Chemical control systems

### How it works

1. Sensors measure water conditions.
2. PLCs process sensor information.
3. PLCs control pumps and valves.
4. SCADA collects and displays operational information.
5. Operators monitor the process through HMIs.
6. DCS or distributed control technologies can manage complex continuous processes.

### Benefits

- Improved efficiency
- Continuous monitoring
- Reduced human error
- Better process control
- Improved reliability

---

# Lab Summary

This lab introduced important terminology used in ICS/SCADA environments.

The major components studied were:

- PLC
- RTU
- HMI
- DCS
- SCADA

The lab also compared ICS environments with traditional IT systems and examined real-world applications in:

- Smart grids
- Water treatment plants

## Key Learning

ICS is different from traditional IT because it interacts with physical processes. Therefore, safety, availability, reliability, and real-time operation are extremely important.

---

# Conclusion

The lab provided a foundational understanding of ICS/SCADA terminology and the differences between industrial control environments and traditional IT systems.

Understanding these concepts is important before studying more advanced ICS security topics.
