# Lab 04: ICS/SCADA Communication Protocols Overview

## Objectives

- Understand common communication protocols used in ICS and SCADA systems.
- Distinguish between serial-based and Ethernet-based protocols.
- Understand practical industrial applications of Modbus, DNP3, and OPC UA.
- Understand the role of communication protocols in industrial environments.

## Protocols Covered

### Modbus

Modbus is a widely used industrial communication protocol.

Common variants:

- Modbus RTU - commonly used over serial communication such as RS-485.
- Modbus TCP - Modbus communication over TCP/IP networks.

### DNP3

DNP3 stands for Distributed Network Protocol version 3.

It is commonly used in:

- Electric utilities
- Water systems
- Remote monitoring
- SCADA systems

DNP3 is designed for reliable communication between control centers and remote devices.

### OPC UA

OPC UA is an industrial interoperability standard.

It allows different industrial systems and vendors to exchange data in a standardized way.

It is commonly used for:

- Industrial automation
- Data exchange
- Monitoring
- Integration between different systems

## Serial vs Ethernet

| Type | Example | Communication |
|---|---|---|
| Serial | Modbus RTU | RS-485 / RS-232 |
| Ethernet | Modbus TCP | TCP/IP |
| Ethernet | DNP3 | IP networks |
| Ethernet | OPC UA | TCP/IP |

## Plant Example

A water treatment plant may use multiple protocols.

- Modbus can monitor flow rates and valve positions.
- DNP3 can communicate with remote equipment.
- OPC UA can exchange information between different industrial systems.

## Safety Note

This lab uses simulations and does not connect to real industrial control equipment.

## Learning Outcomes

After completing this lab, I understand:

- Basic ICS/SCADA communication protocols.
- The difference between serial and Ethernet-based communication.
- Basic uses of Modbus, DNP3, and OPC UA.
- How communication protocols support industrial monitoring and control.
