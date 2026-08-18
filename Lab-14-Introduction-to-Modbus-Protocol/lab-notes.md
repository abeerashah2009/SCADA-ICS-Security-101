# Lab 14: Modbus Protocol - Lab Notes

## 1. Lab Information

**Lab:** Lab 14 - Introduction to Modbus Protocol
**Topic:** Modbus TCP and ICS/SCADA Communication
**Environment:** Authorized educational laboratory
**Protocol:** Modbus TCP
**Default TCP Port:** 502

---

## 2. Objectives Completed

- Studied Modbus protocol fundamentals.
- Compared Modbus RTU and Modbus TCP.
- Studied Modbus TCP packet structure.
- Identified the MBAP header.
- Identified common Modbus function codes.
- Studied coils, discrete inputs, input registers, and holding registers.
- Reviewed register addressing.
- Studied read and write operations.
- Reviewed Modbus exception responses.
- Reviewed Modbus security risks.
- Studied defensive controls for Modbus-based ICS environments.

---

## 3. Modbus Fundamentals

Modbus is an industrial communication protocol commonly used in ICS/SCADA environments.

It follows a request/response communication model.

```text
Modbus Client
      |
      | Request
      v
Modbus Server
      |
      | Response
      v
Modbus Client
## 4. Modbus RTU vs Modbus TCP
Feature	Modbus RTU	Modbus TCP
Transport	Serial	TCP/IP
Common Technology	RS-485	Ethernet
Default TCP Port	N/A	502
Header	RTU frame	MBAP header
CRC field	Yes	No RTU CRC
Typical Use	Serial industrial networks	Ethernet/IP networks
Important Observation

Modbus TCP does not use the CRC field found in a Modbus RTU frame.

Modbus TCP uses the MBAP header together with the Modbus PDU.
----
##5.ModbusTCP Packet Structure

A Modbus TCP message consists of:

+----------------------+
| MBAP Header          |
+----------------------+
| Modbus PDU           |
+----------------------+
MBAP Header Fields
Transaction Identifier
Protocol Identifier
Length
Unit Identifier
Modbus PDU

The PDU contains:

Function Code
Function-specific Data
6. Important Function Codes
Function Code	Hex	Operation
01	0x01	Read Coils
02	0x02	Read Discrete Inputs
03	0x03	Read Holding Registers
04	0x04	Read Input Registers
05	0x05	Write Single Coil
06	0x06	Write Single Register
16	0x10	Write Multiple Registers
--
7. Modbus Data Areas
Data Area	Common Reference	Access
Coils	0xxxx	Read/Write
Discrete Inputs	1xxxx	Read
Input Registers	3xxxx	Read
Holding Registers	4xxxx	Read/Write
Addressing Note

Documentation may use references such as:

40001
40002
40003

However, the protocol request may use zero-based addresses.

For example:

40001 -> Protocol Address 0

The exact addressing convention depends on the device or simulator.

8. Read Holding Registers

Function Code:

0x03

Example:

Starting Address : 0
Quantity         : 2

Conceptually:

Client
  |
  | Function Code 03
  | Address 0
  | Quantity 2
  v
Server
  |
  | Register Data
  v
Client

Example conceptual response:

[03][04][12][34][56][78]

This represents two registers:

Register 1 = 0x1234
Register 2 = 0x5678
9. Write Single Register

Function Code:

0x06

Example laboratory operation:

Register Address : 0
Value            : 0x000A

A successful response normally echoes the request.

Safety

Write operations modify data.

Therefore:

READ  = Observe data
WRITE = Change data

Write operations should only be performed against an authorized simulator or controlled laboratory device.

10. Modbus Exception Responses

A Modbus server can return an exception response when a request cannot be processed.

Common exception codes include:

Code	Meaning
01	Illegal Function
02	Illegal Data Address
03	Illegal Data Value
04	Server Device Failure

An exception response can indicate that the requested operation could not be completed.

11. Modbus Security Observations

Traditional Modbus TCP does not inherently provide strong:

Authentication
Authorization
Encryption
Application-layer integrity protection

Potential risks include:

Unauthorized reading
Unauthorized writing
Process manipulation
Information disclosure
Communication disruption
12. Defensive Controls

Recommended defensive controls include:

Network segmentation
Industrial firewalls
Access control
Least privilege
Secure remote access
Monitoring
Protocol-aware monitoring
Asset inventory
Secure configuration
Change management
Incident response
Defense-in-Depth
Network Segmentation
        |
        v
   Access Control
        |
        v
    Monitoring
        |
        v
    Detection
        |
        v
   ICS Protection
13. Troubleshooting Notes

If a Modbus connection fails, check:

1. Server

Verify that the authorized test server is running.

2. IP Address

Verify the configured server IP.

Example:

127.0.0.1
3. TCP Port

Traditional Modbus TCP uses:

502

The simulator may use another port.

4. Unit ID

Verify that the Unit ID matches the test server configuration.

5. Register Address

Check whether the simulator uses zero-based or reference-style addressing.

6. Function Code

Verify that the selected function code matches the intended operation.

14. Laboratory Evidence

Current laboratory documentation:

README.md
lab-notes.md

No production ICS/SCADA equipment was accessed.

15. Safety Verification
[PASS] No unauthorized ICS systems accessed
[PASS] No production PLC accessed
[PASS] No production SCADA system accessed
[PASS] No unauthorized scanning performed
[PASS] No uncontrolled write operations performed
[PASS] No industrial process modified
[PASS] Testing limited to authorized laboratory environments
16. Key Takeaways
Modbus is widely used in industrial environments.
Modbus TCP operates over TCP/IP.
TCP port 502 is the traditional Modbus TCP port.
Modbus TCP uses an MBAP header.
Modbus RTU uses a CRC field.
Modbus TCP does not use the Modbus RTU CRC field.
Function codes define Modbus operations.
Function Code 0x03 reads holding registers.
Function Code 0x06 writes a single holding register.
Register addressing may differ between documentation and protocol-level addressing.
Modbus should not be unnecessarily exposed to untrusted networks.
Network segmentation and defense-in-depth are important ICS security controls.
Write operations must only be performed in authorized environments.
17. Lab Conclusion

This laboratory provided a foundational understanding of Modbus communication with a focus on Modbus TCP.

The lab covered Modbus architecture, packet structure, MBAP headers, function codes, registers, addressing, read/write operations, exception responses, troubleshooting, and security considerations.

Understanding Modbus communication is important for ICS/SCADA security because defenders need to understand normal industrial traffic before they can identify abnormal or potentially malicious activity.

All activities were limited to an authorized educational environment.
