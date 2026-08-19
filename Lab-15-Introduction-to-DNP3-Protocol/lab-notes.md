# Lab 15: Introduction to DNP3 Protocol

**Lab:** Lab 15 - Introduction to DNP3 Protocol  
**Topic:** DNP3 Protocol and ICS/SCADA Communication  
**Environment:** Authorized educational laboratory  
**Protocol:** DNP3  
**Primary Tools:** Python, Scapy, TShark

---

# 1. Lab Objective

The objective of this laboratory was to understand the fundamentals of DNP3 communication and analyze simulated industrial protocol traffic.

The laboratory also examined common security challenges associated with DNP3 deployments.

All practical testing was limited to the authorized educational laboratory environment.

---

# 2. Environment Verification

## 2.1 Operating System
Command:

uname -a

Result:

Linux ip-172-31-10-221 6.14.0-1018-aws #18~24.04.1-Ubuntu SMP Mon Nov 24 19:46:27 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux

Status:

[PASS]
---

## 2.2 Python Version

Command:

python3 --version

Result:

Python 3.12.3

Status:

[PASS]

---

## 2.3 Scapy Verification

Command:

python3 -c "from scapy.all import IP, TCP, Raw; print('Scapy OK')"

Result:

Scapy OK

Status:

[PASS]

---

## 2.4 Wireshark/TShark Verification

Commands:

which wireshark
which tshark

Result:

Wireshark GUI: Not installed
TShark: /usr/bin/tshark

Status:

[PASS] TShark available
[INFO] Wireshark GUI not installed
---

# 3. Task 1 — DNP3 Packet Structure

## 3.1 DNP3 Overview

DNP3 stands for:

Distributed Network Protocol 3

DNP3 is an industrial communication protocol commonly used in:

- Electrical utilities
- Water systems
- SCADA environments
- RTUs
- IEDs
- Remote monitoring systems

Status:

[PASS] DNP3 fundamentals reviewed

---

## 3.2 DNP3 Layers

The major concepts reviewed were:

Data Link Layer
Transport Layer
Application Layer

Status:

[PASS] DNP3 layers reviewed

---

## 3.3 DNP3 Data-Link Layer

Important fields include:

- Start bytes
- Length
- Control
- Destination
- Source
- CRC

Typical DNP3 start bytes:

05 64

Status:

[PASS] Data-link fields reviewed

---

## 3.4 DNP3 Application Layer

Important concepts include:

- Application control
- Function code
- Object group
- Object variation
- Qualifier
- Data

Status:

[PASS] Application-layer concepts reviewed
---

# 4. Task 2 — Simulated DNP3 Traffic

## 4.1 Simulation Script

File:

dnp3-simulation.py

Syntax check:

python3 -m py_compile dnp3-simulation.py

Result:

No syntax errors reported.

Status:

[PASS] Simulation script created and syntax verified

---

## 4.2 Simulation Execution

Command:

python3 dnp3-simulation.py

Result:

DNP3 Laboratory Traffic Simulation

[INFO] No persistent laboratory listener on TCP/20000
Existing capture evidence can still be analyzed.

Observation:

The laboratory environment did not have a persistent DNP3
listener on TCP/20000 at the time of execution.

Existing packet-capture evidence can still be analyzed.

Status:

[PASS] Simulation executed

---

## 4.3 Traffic Capture

Capture interface:

lo

Capture filter:

tcp port 20000

Display filter:

tcp.port == 20000

DNP3 display filter:

dnp3

Capture file:

/tmp/dnp3.pcapng

Packet count:

8

Status:

[PASS] Traffic capture evidence analyzed

---

## 4.4 Packet Analysis

Source IP:

127.0.0.1

Destination IP:

127.0.0.1

Source Port:

39148

Destination Port:

20000

Protocol:

TCP

TCP Payload Length:

8 bytes

Payload:

05 64 0C C4 01 00 00 00

---

## 4.5 TShark Payload Analysis

Command:

sudo tshark -r /tmp/dnp3.pcapng -Y "tcp.payload" -T fields -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e tcp.len -e tcp.payload

Result:

127.0.0.1  127.0.0.1  39148  20000  8  05640cc401000000

Status:

[PASS] Packet payload identified

---

## 4.6 DNP3 Dissection Test

Command:

sudo tshark -r /tmp/dnp3.pcapng -Y "dnp3"

Result:

No packets matched the DNP3 display filter.

Observation:

The captured TCP payload contains the DNP3-like start bytes
05 64, but TShark did not identify the packet using its
DNP3 protocol dissector.

Therefore, the captured payload is documented as a
DNP3-like laboratory payload rather than a fully validated
DNP3 frame.

Status:

[PASS] Protocol-identification limitation documented
---

# 5. DNP3 Protocol Observations

The following concepts were reviewed:

| Concept | Understanding |
|---|---|
| DNP3 | Industrial communication protocol |
| Data Link | Framing and addressing |
| Transport | Fragmentation and reassembly |
| Application | Industrial operations and data |
| Control | Frame control information |
| Source | Originating DNP3 device |
| Destination | Target DNP3 device |
| CRC | Transmission-error detection |
| Port 20000 | Common DNP3 TCP/UDP port |

---

# 6. Important Protocol Observation

A key lesson from this laboratory is:

TCP port 20000
        is not automatically valid DNP3

A generic TCP payload is not necessarily a valid DNP3 message.

The laboratory payload contained the DNP3 start bytes:

05 64

However, TShark did not identify the payload as DNP3.

Therefore, protocol identification should not be based only on
the TCP port number or a small portion of the payload.

A valid DNP3 packet must contain a structure that can be correctly
interpreted according to the protocol specification.

Status:

[PASS] Protocol identification concept understood

---

# 7. Task 3 — DNP3 Security Analysis

## 7.1 Security Challenge 1 — Unauthorized Access

Risk:

Unauthorized systems may attempt communication with exposed
DNP3 devices.

Potential impact:

- Unauthorized access
- Information exposure
- Unwanted communication with industrial devices

Status:

[REVIEWED] Unauthorized access risk

---

## 7.2 Security Challenge 2 — Data Manipulation

Risk:

Unauthorized modification of industrial data or control
communication may affect the integrity of ICS/SCADA operations.

Potential impact:

- Incorrect data
- Loss of process integrity
- Unsafe or unexpected operations

Status:

[REVIEWED] Data manipulation risk

---

## 7.3 Security Challenge 3 — Man-in-the-Middle

Risk:

An attacker positioned between communicating systems may attempt
to observe or interfere with network traffic.

Potential impact:

- Traffic interception
- Data manipulation
- Communication disruption

Status:

[REVIEWED] MITM risk

---

# 8. Defensive Controls

The following defensive controls were reviewed:

- Network segmentation
- Firewalls
- Access Control Lists (ACLs)
- Allow-listing
- Least privilege
- Secure remote access
- VPN
- Multi-Factor Authentication (MFA)
- Network monitoring
- Logging
- Incident response

Status:

[PASS] Defensive controls reviewed

---

# 9. Defense-in-Depth

A layered ICS security architecture can include:

Corporate Network
       |
    Firewall
       |
    ICS DMZ
       |
    Firewall
       |
  SCADA Network
       |
    RTU / IED

Security should not depend on a single control.

Multiple security layers should work together to reduce risk.

Status:

[PASS] Defense-in-depth concept reviewed

---

# 10. Skills Practiced

[PASS] DNP3 fundamentals
[PASS] ICS/SCADA communication
[PASS] Packet analysis
[PASS] TShark
[PASS] Scapy
[PASS] TCP/IP analysis
[PASS] Industrial protocol identification
[PASS] Security analysis
[PASS] Network segmentation
[PASS] Defensive documentation

---

# 11. Safety Verification

[PASS] No production ICS accessed
[PASS] No production SCADA accessed
[PASS] No production RTU accessed
[PASS] No unauthorized scanning performed
[PASS] No industrial process modified
[PASS] Testing limited to authorized laboratory environment

---

# 12. Evidence Files

The laboratory contains:

README.md
lab-notes.md
dnp3-simulation.py
dnp3_packet_analysis.py

Packet-capture evidence:

/tmp/dnp3.pcapng

The packet capture was generated from the authorized
laboratory loopback interface.

---

# 13. Final Results

## Task 1

[PASS] DNP3 fundamentals reviewed
[PASS] DNP3 packet structure reviewed
[PASS] DNP3 layers identified
[PASS] Control field reviewed
[PASS] Addressing reviewed
[PASS] CRC concept reviewed

## Task 2

[PASS] Scapy verified
[PASS] Simulation script created
[PASS] Simulation script syntax verified
[PASS] Simulation executed
[PASS] Traffic captured
[PASS] Traffic analyzed
[PASS] Payload identified
[PASS] DNP3 identification limitation documented

## Task 3

[PASS] Security challenges identified
[PASS] Unauthorized access risk reviewed
[PASS] Data manipulation risk reviewed
[PASS] MITM risk reviewed
[PASS] Defensive controls documented
[PASS] Defense-in-depth reviewed

---

# 14. Final Conclusion

This laboratory introduced DNP3 and its role in ICS/SCADA
communication.

The practical work focused on protocol structure, simulated
traffic generation, packet capture, packet analysis, and
defensive security considerations.

The laboratory also reinforced the importance of distinguishing
between generic TCP traffic and genuine DNP3 protocol traffic.

The captured laboratory payload used the DNP3 start bytes 05 64,
but TShark did not decode it as DNP3. This demonstrates why
protocol identification should be validated using packet
structure and protocol dissection rather than relying only on
the TCP port.

All activities were limited to the authorized educational
laboratory environment.
