# Lab 09 Notes: Basic ICS/SCADA System Exploration

## 1. Lab Purpose

The purpose of this laboratory is to understand the basic components of
an ICS/SCADA environment and explore PLC and Modbus concepts using a safe
local simulation.

The laboratory does not interact with real industrial equipment.

---

## 2. What is ICS?

ICS stands for Industrial Control System.

ICS environments are used to monitor and control industrial processes.

Examples include:

- Manufacturing
- Water treatment
- Electrical power
- Oil and gas
- Transportation
- Building automation

---

## 3. What is SCADA?

SCADA stands for:

Supervisory Control and Data Acquisition.

SCADA systems are used to:

- Monitor industrial processes
- Collect data
- Display information
- Generate alarms
- Provide supervisory control

A simplified architecture can be represented as:

    Sensors
       |
       v
      PLC
       |
       v
   SCADA Server
       |
       v
      HMI
       |
       v
    Operator

---

## 4. What is a PLC?

PLC stands for:

Programmable Logic Controller.

A PLC is an industrial computer designed to control physical processes.

A PLC can receive inputs from:

- Sensors
- Switches
- Measurement devices

A PLC can control outputs such as:

- Motors
- Pumps
- Valves
- Relays

Example:

    Temperature Sensor
            |
            v
           PLC
            |
            v
       Cooling Motor

The PLC continuously processes inputs and controls outputs according
to its programmed logic.

---

## 5. What is Modbus?

Modbus is an industrial communication protocol.

It allows devices to exchange information.

A simplified example is:

    SCADA / Master
          |
          | Modbus
          v
       PLC / Slave
          |
          v
       Registers

Modbus can be implemented over different communication technologies.

Common examples include:

- Modbus RTU
- Modbus TCP

---

## 6. Modbus Data Concepts

Modbus commonly uses several types of data objects.

### Coils

Coils generally represent binary output values.

Example:

    Motor = ON

### Discrete Inputs

Discrete inputs represent binary input states.

Example:

    Door Sensor = OPEN

### Input Registers

Input registers are commonly used for read-only numeric information.

Example:

    Temperature = 72

### Holding Registers

Holding registers store numeric values that can commonly be read and,
depending on the device configuration, written.

Example:

    Register 1 = 125
    Register 2 = 78
    Register 3 = 100
    Register 4 = 45

For this laboratory, these registers are simulated locally.

---

## 7. Laboratory Environment

The laboratory is running in an Ubuntu Linux AWS EC2 environment.

The environment is a cloud-hosted Linux system.

The practical simulation is intentionally local.

No real industrial equipment is connected.

---

## 8. Environment Verification

The laboratory environment should be checked before performing the
simulation.

Useful commands include:

```bash
uname -a
- This displays kernel and system information.

python3 --version

- This displays the installed Python version.

java -version

This checks whether Java is installed.

Java may be required by some older graphical ICS/Modbus simulators.
---

## 9. ModbusPal Consideration

The original laboratory instructions mention ModbusPal.

ModbusPal is an older Modbus simulator.

Because the current laboratory environment is an AWS EC2 Linux system,
a graphical Java application may not be practical.

Therefore, the laboratory uses a safe local Python simulation to
demonstrate the same basic concepts:

Simulated device
Holding registers
Read operation
Write operation
Verification

This approach avoids claiming that a graphical simulator was used when
it was not actually available.
---

## 10. Simulated PLC

The simulated PLC contains the following holding registers:

Register	Initial Value
1	        125
2	        78
3	        100
4	        45

These values represent simulated industrial process data.

They are not connected to real sensors or equipment.
--- 

 ## 11. Read Operation

The simulation reads Register 1.

Example:

Reading Register 1...
Register 1 Value: 125

Interpretation:

The simulated device successfully returned the value stored in the
holding register.

---
# 12. Write Operation

A simulated write operation changes a register value.

- Example:

Register 2
Before: 78
After: 150

This demonstrates the basic concept of writing a new value to a
simulated holding register.

No real industrial device is modified.
---

## 13. Read-After-Write Verification

After changing a register value, the simulation reads the register
again.

- Example:

Register 2 Before: 78
Writing Register 2 = 150
Register 2 After: 150

This verifies that the simulated write operation was successful.

---
## 14. Example Simulated Device

The simulated device can be represented as:

+----------------------------+
|      Simulated PLC         |
+----------------------------+
| Register 1 = 125           |
| Register 2 = 78            |
| Register 3 = 100           |
| Register 4 = 45            |
+----------------------------+
             |
             |
          Modbus
             |
             v
+----------------------------+
|    Simulated Master        |
|    Read / Write Data       |
+----------------------------+
15. Configuration Documentation

A simulated device configuration can contain:

Device Name : PLC-SIM-01
Protocol    : Modbus
Mode        : Local Simulation
Register 1  : 125
Register 2  : 78
Register 3  : 100
Register 4  : 45

These values are for educational simulation only.

---
## 16. Why Simulation is Important

- Industrial systems should not be experimented with directly.

A simulator allows learners to understand:

- Industrial protocols
- Device communication
- Registers
- Data points
- Read operations
- Write operations

without affecting a real production process.

---

## 17. Security Considerations

- Industrial environments require careful control of communication.

Important security principles include:

- Network segmentation
- Access control
- Authentication where supported
- Monitoring
- Change management
- Asset inventory
- Secure configuration
- Testing in isolated environments

A laboratory should always remain separated from production systems.

---

##18. ICS Communication Flow

A simplified communication flow is:

Sensor
  |
  v
PLC
  |
  | Industrial Protocol
  v
SCADA Server
  |
  v
HMI
  |
  v
Operator

- The PLC handles control logic while SCADA provides supervisory
monitoring and control.

---

## 19. Practical Findings

- The practical simulation demonstrates:

A PLC-style device can be represented in software.
Holding registers can store numeric process values.
A simulated master can read register values.
A simulated master can write a new value.
The new value can be verified.
The entire exercise can be performed without contacting real
industrial equipment.
---

## 20. Safety Findings

- The laboratory was intentionally performed using a local simulation.

Therefore:

No real PLC was contacted.
No real SCADA server was contacted.
No real HMI was contacted.
No production system was accessed.
No industrial process was changed.
No external network scanning was performed.
---

## 21. Skills Demonstrated

- This laboratory demonstrates beginner-level knowledge of:

ICS architecture
SCADA concepts
PLC concepts
Modbus concepts
Holding registers
Read/write operations
Simulation
Technical documentation
Safe laboratory practices
---

## 22. Portfolio Evidence

- The laboratory should preserve:

README.md
lab-notes.md
environment-check.py
modbus-simulation.py
environment-results.txt
modbus-results.txt

- These files provide evidence of both theoretical understanding and
practical work.
---

## 23. Key Terms
- ICS

- Industrial Control System.

- SCADA

- Supervisory Control and Data Acquisition.

- PLC

- Programmable Logic Controller.

- HMI

- Human-Machine Interface.

- Modbus

- Industrial communication protocol.

- Holding Register

- A numeric Modbus data location commonly used for readable and writable
values, depending on device configuration.

- Simulator

- Software that represents the behavior of a real system without using
the physical system.
---

## 24. Quick Revision

Remember:

PLC      = Controls industrial processes


HMI      = Operator interface


SCADA    = Supervisory monitoring and control


Modbus   = Industrial communication protocol


Register = Stores simulated process data


Simulator = Safe environment for learning
---

## 25. Lab Conclusion

- This laboratory introduced the basic concepts of ICS/SCADA system
exploration.

- A simulated PLC environment was used to demonstrate Modbus-style
holding registers and basic read/write operations.

The exercise provided practical experience while maintaining a strict
boundary between the laboratory and real industrial infrastructure.

The skills developed here provide a foundation for future laboratories
involving industrial protocols, monitoring, asset discovery, and
ICS security.
