# Lab 14: Introduction to Modbus Protocol

## Lab Overview

Modbus is one of the most widely recognized industrial communication protocols used in Industrial Control Systems (ICS) and SCADA environments.

This lab introduces the fundamental concepts of Modbus communication, with a primary focus on **Modbus TCP**. The lab covers Modbus architecture, packet structure, function codes, register addressing, read/write operations, and communication documentation.

The purpose of this lab is to build a foundational understanding of how industrial devices such as PLCs, RTUs, HMIs, SCADA servers, and other control-system components exchange data using Modbus.

All activities in this lab are designed for learning and documentation purposes. Any read/write operations should be performed only against a local simulator or explicitly authorized test environment.

---

# Objectives

By completing this lab, the learner will be able to:

1. Explain the purpose of the Modbus protocol.
2. Understand the difference between Modbus RTU and Modbus TCP.
3. Describe the basic structure of a Modbus TCP communication.
4. Identify common Modbus function codes.
5. Understand Modbus coils, inputs, and registers.
6. Explain Modbus register addressing.
7. Understand the role of the Unit Identifier in Modbus TCP.
8. Understand the MBAP header used by Modbus TCP.
9. Perform safe read operations against a test Modbus server.
10. Perform controlled write operations against a local simulator.
11. Document Modbus communication and responses.
12. Understand security considerations associated with Modbus.
13. Apply defensive security principles to Modbus-based ICS environments.

---

# Prerequisites

The following knowledge is recommended before starting this lab:

- Basic Linux command-line knowledge
- Basic networking concepts
- Understanding of IP addresses and TCP ports
- Basic knowledge of hexadecimal notation
- Basic understanding of ICS/SCADA architecture
- Familiarity with PLCs and industrial devices
- Basic cybersecurity concepts

---

# Lab Environment

## Operating Environment

This lab is performed in a Linux-based learning environment.

Example environment:

```text
Operating System : Ubuntu Linux
Shell            : Bash
Python           : Python 3
Protocol         : Modbus TCP
Default Port     : TCP/502
Test Environment : Local Modbus simulator/server
Safety Scope

This lab is strictly educational and defensive.

Only use Modbus communication against:

A local simulator
A deliberately created test server
A laboratory environment
Systems for which explicit authorization has been provided

Do not send Modbus write commands to real industrial equipment unless you are explicitly authorized and operating under an approved test procedure.

Safety Rules
Do not scan unauthorized industrial networks.
Do not connect to production PLCs.
Do not modify real industrial processes.
Do not send uncontrolled write commands.
Do not attempt to bypass authentication or security controls.
Do not interfere with safety systems.
Keep testing inside the authorized laboratory environment.
Modbus Fundamentals
What is Modbus?

Modbus is an industrial communication protocol originally developed by Modicon.

It is commonly used for communication between industrial devices such as:

PLCs
RTUs
SCADA systems
HMIs
Sensors
Industrial gateways
Monitoring systems

Modbus follows a simple request/response communication model.

A client sends a request and the server returns a response.

Example:

Modbus Client
     |
     | Request
     v
Modbus Server
     |
     | Response
     v
Modbus Client
Modbus Communication Models

Modbus exists in several forms.

Modbus RTU

Modbus RTU normally operates over serial communication technologies such as:

RS-232
RS-485

Typical characteristics:

Transport: Serial
Encoding : Binary
Integrity : CRC
Modbus TCP

Modbus TCP carries Modbus communication over TCP/IP networks.

Typical characteristics:

Transport : TCP/IP
Default Port : 502
Integrity Mechanism : TCP + protocol checks
Header : MBAP

The communication generally looks like:

Modbus Client
     |
     | TCP/IP
     |
     v
Network
     |
     v
Modbus TCP Server
Important Modbus TCP Concept

Modbus TCP is different from Modbus RTU.

A common beginner mistake is assuming that Modbus TCP packets contain the same CRC used by Modbus RTU.

They do not.

Modbus RTU
Address
Function Code
Data
CRC
Modbus TCP
MBAP Header
Modbus PDU

The MBAP header is used to identify and manage the TCP transaction.

Modbus TCP Packet Structure

A Modbus TCP message consists of:

+-------------------------+
| MBAP Header             |
+-------------------------+
| Modbus PDU              |
+-------------------------+

The MBAP header contains:

Transaction Identifier
Protocol Identifier
Length
Unit Identifier
MBAP Header
Transaction Identifier

Used to associate a response with the corresponding request.

Example:

Transaction ID: 0001
Protocol Identifier

For Modbus TCP this is normally:

Protocol ID: 0000
Length

Specifies the number of following bytes.

Unit Identifier

Identifies the target logical device.

This is especially useful in environments where a Modbus TCP gateway communicates with serial Modbus devices.

Modbus PDU

The Protocol Data Unit contains:

Function Code
Data

Example:

03
0000
0002

Where:

03       = Read Holding Registers
0000     = Starting address
0002     = Number of registers
Modbus Data Areas

Modbus commonly uses four logical data areas.

Data Area	Common Reference	Access
Coils	0xxxx	Read/Write
Discrete Inputs	1xxxx	Read
Input Registers	3xxxx	Read
Holding Registers	4xxxx	Read/Write

These reference numbers are commonly used in documentation.

Actual protocol addresses may be zero-based.

Register Addressing

A common notation is:

40001
40002
40003

These are commonly referred to as holding-register references.

However, the Modbus protocol request generally carries a zero-based address.

For example:

40001

may correspond to protocol address:

0

depending on the simulator or device documentation.

Therefore, always verify the addressing convention used by the particular Modbus implementation.

Common Function Codes
Function Code 01
0x01

Read Coils.

Used to read binary output states.

Function Code 02
0x02

Read Discrete Inputs.

Used to read binary input states.

Function Code 03
0x03

Read Holding Registers.

This is one of the most commonly used Modbus functions.

Function Code 04
0x04

Read Input Registers.

Function Code 05
0x05

Write Single Coil.

Function Code 06
0x06

Write Single Holding Register.

Function Code 10
0x10

Write Multiple Holding Registers.

Task 1: Study Modbus Packet Structure
Task Objective

Understand how a Modbus TCP message is constructed and identify the major fields.

Example Modbus TCP Request

Conceptually:

MBAP Header
    |
    +-- Transaction ID
    +-- Protocol ID
    +-- Length
    +-- Unit ID


PDU
    |
    +-- Function Code
    +-- Starting Address
    +-- Quantity

For a Read Holding Registers request:

Function Code: 0x03
Starting Address: 0x0000
Quantity: 0x0002

This means:

Read 2 holding registers
starting at protocol address 0.
Task 2: Modbus Simulator
Task Objective

Use a simulator or local Modbus server to understand basic Modbus TCP communication.

A simulator provides a safe environment for practicing industrial protocol communication without interacting with production equipment.

Simulator Configuration

Configure the Modbus client with values appropriate for the test environment.

Example local configuration:

IP Address : 127.0.0.1
Port       : 502
Protocol   : Modbus TCP
Unit ID    : 1

The exact Unit ID and port may vary depending on the simulator.

Task 2.1: Establish a Test Connection

Before performing any operation, verify that the test Modbus server is intentionally running.

Example:

Server:
127.0.0.1


Port:
502

Only connect to a server that belongs to the laboratory environment.

Task 2.2: Read Holding Registers

Function Code:

0x03

Operation:

Read Holding Registers

Example laboratory request:

Starting Address : 0
Number of Registers : 2

Conceptually:

Client
  |
  | FC 03
  | Address 0
  | Quantity 2
  v
Server
  |
  | Register Values
  v
Client
Example Response

A successful Modbus TCP response contains:

Function Code
Byte Count
Register Data

For two registers:

Function Code : 03
Byte Count    : 04
Data          : 4 bytes

Example conceptual response:

[03][04][12][34][56][78]

The two registers contain:

Register 1 = 0x1234
Register 2 = 0x5678

This is a conceptual example only.

Task 2.3: Write a Single Register

Function Code:

0x06

Operation:

Write Single Holding Register

Example laboratory operation:

Register Address : 0
Value            : 0x000A

Conceptually:

Client
  |
  | FC 06
  | Address
  | Value
  v
Server
  |
  | Echo Response
  v
Client

A successful response normally echoes the request information.

Important Safety Note About Write Operations

Write operations change device data.

Therefore:

READ  = Observe data
WRITE = Change data

Write operations should only be performed against a controlled simulator or explicitly authorized test device.

Never test arbitrary write commands against production PLCs or industrial controllers.

Task 3: Document Modbus Communication

For every test operation, record:

Timestamp
Server IP
TCP port
Unit ID
Function code
Starting address
Quantity
Data sent
Data received
Operation result
Safety scope

Example:

Timestamp : Laboratory test
Server    : 127.0.0.1
Port      : 502
Unit ID   : 1
Operation : Read Holding Registers
Function  : 0x03
Address   : 0
Quantity  : 2
Result    : Successful
Environment: Local simulator
Modbus Troubleshooting

If a Modbus request fails, check the following.

1. Server Status

Verify that the test server is running.

2. IP Address

Verify the configured IP address.

3. TCP Port

The traditional Modbus TCP port is:

502

The laboratory simulator may use another port.

4. Unit ID

Verify the Unit ID configured by the simulator.

5. Register Address

Check whether the simulator uses:

0-based addressing

or:

1-based/reference addressing
6. Function Code

Verify that the selected function code matches the intended data type.

Modbus Exception Responses

A Modbus server may return an exception response when a request cannot be processed.

Conceptually:

Exception Function Code
Exception Code

The function code may have its high bit set.

For example:

03

can become:

83

to indicate an exception associated with function code 03.

Common Exception Codes
Code	Meaning
01	Illegal Function
02	Illegal Data Address
03	Illegal Data Value
04	Server Device Failure

These responses can help troubleshoot communication problems.

Modbus Security Considerations

Modbus was designed primarily for industrial communication rather than modern cybersecurity.

Traditional Modbus TCP does not inherently provide strong:

Authentication
Authorization
Encryption
Integrity protection at the application layer

This creates security concerns when Modbus is exposed to untrusted networks.

Potential ICS Risks

Poorly protected Modbus communication can contribute to:

Unauthorized Reading

Attackers may attempt to read process information.

Unauthorized Writing

Attackers may attempt to modify registers or control values.

Process Manipulation

Unauthorized changes could potentially affect industrial processes.

Information Disclosure

Register values may reveal operational information.

Availability Impact

Excessive or malformed traffic may interfere with device communications.

Defensive Controls

Organizations can reduce Modbus-related risk using defense-in-depth.

Recommended controls include:

Network segmentation
Industrial firewalls
Access control
Secure remote access
Monitoring
Allow-listing
Protocol-aware security monitoring
Strong authentication around management systems
Least privilege
Asset inventory
Secure configuration
Change management
Incident response procedures
Modbus Network Segmentation

A basic defensive architecture may look like:

Corporate Network
       |
       | Firewall
       |
       v
   ICS DMZ
       |
       | Firewall
       |
       v
   SCADA Network
       |
       v
      PLCs
       |
       v
   Field Devices

Modbus traffic should not be unnecessarily exposed to corporate or public networks.

Defense-in-Depth

A strong ICS security architecture should use multiple layers.

             Defense-in-Depth
                    |
     +--------------+--------------+
     |              |              |
 Network        Access         Monitoring
 Security       Control        & Detection
     |              |              |
 Segmentation   Least Privilege   Logging
 Firewall       Authentication    Alerts
     |              |              |
     +--------------+--------------+
                    |
              ICS Protection

No single security control should be considered sufficient.

Task Results
Modbus Fundamentals

[PASS] Modbus protocol purpose understood

[PASS] Modbus RTU and Modbus TCP identified

[PASS] Modbus TCP default port identified

[PASS] MBAP header identified

[PASS] Modbus PDU structure understood

Function Codes

[PASS] Function Code 0x01 identified

[PASS] Function Code 0x02 identified

[PASS] Function Code 0x03 identified

[PASS] Function Code 0x04 identified

[PASS] Function Code 0x05 identified

[PASS] Function Code 0x06 identified

[PASS] Function Code 0x10 identified

Register Concepts

[PASS] Holding registers understood

[PASS] Input registers understood

[PASS] Coil concepts understood

[PASS] Discrete input concepts understood

[PASS] Register addressing considerations documented

Security

[PASS] Modbus security limitations identified

[PASS] Unauthorized write risk understood

[PASS] Network segmentation identified as a defensive control

[PASS] Defense-in-depth principles documented

[PASS] No production ICS system accessed

Evidence Files

The following files document the work completed during this laboratory:

README.md
lab-notes.md

Additional evidence files may be added if a local simulator is used.

Skills Practiced

This laboratory developed the following skills:

Industrial protocol fundamentals
Modbus TCP concepts
Protocol packet analysis
Function-code identification
Register addressing
Client/server communication
Industrial networking
ICS security awareness
Network segmentation
Defensive documentation
Technical troubleshooting
Key Takeaways
Modbus is widely used in industrial environments.
Modbus TCP operates over TCP/IP.
TCP port 502 is the traditional default Modbus TCP port.
Modbus TCP uses an MBAP header.
Modbus RTU uses CRC, while Modbus TCP does not use the RTU CRC field.
Function codes determine the requested operation.
Function Code 0x03 reads holding registers.
Function Code 0x06 writes a single holding register.
Register addressing can differ between documentation and protocol-level addresses.
Write operations should only be performed in authorized environments.
Modbus should be protected using network segmentation and defense-in-depth.
Understanding industrial protocols is important for ICS security professionals.
Conclusion

This lab introduced the Modbus industrial communication protocol with a focus on Modbus TCP.

The laboratory covered Modbus architecture, RTU versus TCP, MBAP headers, Modbus function codes, register addressing, read/write operations, exception responses, troubleshooting, and security considerations.

Understanding Modbus is important for ICS/SCADA security because defenders need to understand normal industrial communication before they can identify abnormal or potentially malicious activity.

The lab was performed within an authorized educational environment and did not involve unauthorized access to industrial systems.
Safety Statement

This laboratory is for educational and defensive cybersecurity training.

[PASS] No unauthorized ICS systems accessed
[PASS] No production PLCs accessed
[PASS] No production SCADA systems accessed
[PASS] No unauthorized scanning performed
[PASS] No uncontrolled write operations performed
[PASS] No industrial process modified
[PASS] Testing limited to authorized laboratory environments
Lab Completion Checklist
 Understand Modbus fundamentals
 Understand Modbus TCP
 Understand Modbus RTU
 Identify MBAP header fields
 Identify common function codes
 Understand register addressing
 Understand read operations
 Understand write operations
 Document communication
 Review Modbus security risks
 Review defensive controls
 Maintain laboratory safety
