# Lab 04 Notes: ICS/SCADA Communication Protocols

## 1. What is an ICS/SCADA Protocol?

An ICS/SCADA communication protocol is a set of rules that allows industrial devices and systems to exchange information.

For example:

Sensor → PLC → SCADA Server → HMI

The protocol defines how these devices communicate and exchange data.

---

## 2. Modbus

Modbus is one of the most common industrial communication protocols.

### Modbus RTU

- Uses serial communication.
- Commonly uses RS-485.
- Can also use RS-232.
- Often used to communicate with PLCs, sensors, meters, and other devices.
- Uses a master/client and slave/server communication model depending on the implementation.

### Modbus TCP

- Uses Ethernet networks.
- Runs over TCP/IP.
- Allows Modbus communication across modern IP networks.
- Commonly uses TCP port 502.

### Easy Example

A PLC may contain a register representing water flow.

A SCADA system can request that register and display the value to an operator.

---

## 3. DNP3

DNP3 means Distributed Network Protocol version 3.

It is commonly used in SCADA and utility environments.

### Common Applications

- Electricity systems
- Water systems
- Remote monitoring
- Utility automation

### Why DNP3 is useful

DNP3 was designed for reliable communication between control centers and remote devices, especially where communication may occur over long distances.

---

## 4. OPC UA

OPC UA stands for Open Platform Communications Unified Architecture.

It is an industrial communication and interoperability standard.

### Main Purpose

OPC UA allows different industrial applications and devices to exchange information using standardized methods.

### Common Uses

- Industrial automation
- Data collection
- Monitoring
- Machine-to-machine communication
- Integration between different vendors

---

## 5. Serial vs Ethernet

### Serial Communication

Example:

Modbus RTU

Typical technologies:

- RS-232
- RS-485

Basic idea:

Industrial Device → Serial Cable → Controller

### Ethernet Communication

Examples:

- Modbus TCP
- DNP3 over IP
- OPC UA

Basic idea:

Industrial Device → Ethernet Network → Industrial System

---

## 6. Quick Comparison

| Protocol | Typical Communication | Common Use |
|---|---|---|
| Modbus RTU | Serial | PLCs, sensors, meters |
| Modbus TCP | Ethernet/TCP | Industrial networks |
| DNP3 | Serial or IP | Utilities and SCADA |
| OPC UA | Ethernet/IP | Industrial interoperability |

---

## 7. Water Treatment Plant Example

Imagine a water treatment plant.

### Modbus

Used to monitor:

- Flow rate
- Valve position
- Pump status
- Sensor values

### DNP3

Could be used for communication with remote equipment and stations.

### OPC UA

Could exchange information between the SCADA system and other industrial applications.

---

## 8. Important Security Concept

ICS communication protocols were often designed primarily for reliability and functionality rather than modern cybersecurity.

Security therefore requires additional controls such as:

- Network segmentation
- Access control
- Authentication where supported
- Monitoring
- Secure configuration
- Firewalls
- Industrial DMZs

Never test protocols against real industrial equipment unless you have explicit authorization.

---

## 9. Key Takeaways

Remember:

**Modbus RTU = Serial**

**Modbus TCP = Ethernet/TCP**

**DNP3 = SCADA/Utilities**

**OPC UA = Industrial Interoperability**

The main purpose of these protocols is to allow industrial devices and systems to exchange information reliably.
