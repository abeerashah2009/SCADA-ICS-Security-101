# Lab 15: Introduction to DNP3 Protocol

**Lab:** Lab 15 - Introduction to DNP3 Protocol
**Topic:** DNP3 Protocol and ICS/SCADA Communication
**Environment:** Authorized educational laboratory
**Protocol:** DNP3
**Primary Tools:** Python, Scapy, Wireshark/TShark

---

# 1. Lab Objective

The objective of this laboratory is to understand the fundamentals of DNP3 communication and analyze simulated industrial protocol traffic.

The laboratory also examines security challenges associated with DNP3 deployments.

---

# 2. Environment Verification

## 2.1 Operating System

Command:

```bash
uname -a
```

Result:

```text
Record output here.
```

Status:

```text
[ ] PASS
```

---

## 2.2 Python Version

Command:

```bash
python3 --version
```

Result:

```text
Record output here.
```

Status:

```text
[ ] PASS
```

---

## 2.3 Scapy Verification

Command:

```bash
python3 -c "from scapy.all import IP, TCP, Raw; print('Scapy OK')"
```

Result:

```text
Record output here.
```

Status:

```text
[ ] PASS
```

---

## 2.4 Wireshark/TShark Verification

Commands:

```bash
which wireshark
```

```bash
which tshark
```

Result:

```text
Record output here.
```

Status:

```text
[ ] PASS
```

---

# 3. Task 1 — DNP3 Packet Structure

## 3.1 DNP3 Overview

DNP3 stands for:

Distributed Network Protocol.

It is commonly used in:

* Electrical utilities
* Water systems
* SCADA environments
* RTUs
* IEDs
* Remote monitoring systems

---

## 3.2 DNP3 Layers

The major concepts reviewed were:

```text
Data Link Layer
Transport Layer
Application Layer
```

Status:

```text
[ ] PASS
```

---

## 3.3 DNP3 Data-Link Layer

Important fields include:

* Start bytes
* Length
* Control
* Destination
* Source
* CRC

Typical start bytes:

```text
05 64
```

Status:

```text
[ ] PASS
```

---

## 3.4 DNP3 Application Layer

Important concepts include:

* Application control
* Function code
* Object group
* Object variation
* Qualifier
* Data

Status:

```text
[ ] PASS
```

---

# 4. Task 2 — Simulated DNP3 Traffic

## 4.1 Simulation Script

File:

```text
dnp3-simulation.py
```

Syntax check:

```bash
python3 -m py_compile dnp3-simulation.py
```

Result:

```text
Record result here.
```

Status:

```text
[ ] PASS
```

---

## 4.2 Traffic Capture

Capture interface:

```text
Record interface here.
```

Capture/display filter:

```text
tcp.port == 20000
```

DNP3 display filter:

```text
dnp3
```

Packet count:

```text
Record packet count here.
```

---

## 4.3 Packet Analysis

Record the following:

### Source IP

```text
Record here.
```

### Destination IP

```text
Record here.
```

### Source Port

```text
Record here.
```

### Destination Port

```text
Record here.
```

### Protocol

```text
Record here.
```

### Payload

```text
Record here.
```

---

# 5. DNP3 Protocol Observations

The following concepts were reviewed:

| Concept     | Understanding                     |
| ----------- | --------------------------------- |
| DNP3        | Industrial communication protocol |
| Data Link   | Framing and addressing            |
| Transport   | Fragmentation/reassembly          |
| Application | Industrial operations and data    |
| Control     | Frame control information         |
| Source      | Originating DNP3 device           |
| Destination | Target DNP3 device                |
| CRC         | Transmission-error detection      |
| Port 20000  | Common DNP3 TCP/UDP port          |

---

# 6. Important Protocol Observation

A key lesson from this laboratory is:

```text
TCP port 20000
        ≠
Automatically valid DNP3
```

A generic TCP payload is not necessarily a valid DNP3 message.

A valid DNP3 packet must contain a structure that can be correctly interpreted according to the protocol specification.

This distinction is important when performing packet analysis.

---

# 7. Task 3 — DNP3 Security Analysis

## 7.1 Security Challenge 1 — Unauthorized Access

Risk:

```text
Unauthorized systems may attempt communication
with exposed DNP3 devices.
```

Status:

```text
[ ] REVIEWED
```

---

## 7.2 Security Challenge 2 — Data Manipulation

Risk:

```text
Unauthorized modification of industrial data
or control communication.
```

Status:

```text
[ ] REVIEWED
```

---

## 7.3 Security Challenge 3 — Man-in-the-Middle

Risk:

```text
An attacker positioned between communicating
systems may attempt to interfere with traffic.
```

Status:

```text
[ ] REVIEWED
```

---

# 8. Defensive Controls

The following controls were reviewed:

* Network segmentation
* Firewalls
* ACLs
* Allow-listing
* Least privilege
* Secure remote access
* VPN
* MFA
* Monitoring
* Logging
* Incident response

Status:

```text
[ ] PASS
```

---

# 9. Defense-in-Depth

A layered ICS security architecture can include:

```text
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
```

Security should not depend on one control.

Status:

```text
[ ] PASS
```

---

# 10. Skills Practiced

```text
[ ] DNP3 fundamentals
[ ] ICS/SCADA communication
[ ] Packet analysis
[ ] Wireshark
[ ] Scapy
[ ] TCP/IP analysis
[ ] Industrial protocol identification
[ ] Security analysis
[ ] Network segmentation
[ ] Defensive documentation
```

---

# 11. Safety Verification

```text
[PASS] No production ICS accessed
[PASS] No production SCADA accessed
[PASS] No production RTU accessed
[PASS] No unauthorized scanning performed
[PASS] No unauthorized DNP3 communication performed
[PASS] No industrial process modified
[PASS] Testing limited to authorized laboratory environment
```

---

# 12. Evidence Files

Expected files:

```text
README.md
lab-notes.md
dnp3-simulation.py
dnp3-security-review.md
```

Additional packet-capture evidence should only be retained when necessary and appropriate.

---

# 13. Final Results

## Task 1

```text
[ ] DNP3 fundamentals understood
[ ] DNP3 packet structure reviewed
[ ] DNP3 layers identified
[ ] Control field reviewed
[ ] Addressing reviewed
[ ] CRC reviewed
```

## Task 2

```text
[ ] Scapy verified
[ ] Simulation created
[ ] Simulation executed
[ ] Traffic captured
[ ] Traffic analyzed
```

## Task 3

```text
[ ] Security challenges identified
[ ] Unauthorized access risk understood
[ ] Data manipulation risk understood
[ ] MITM risk understood
[ ] Defensive controls documented
```

---

# 14. Final Conclusion

This laboratory introduced DNP3 and its role in ICS/SCADA communication.

The practical work focused on protocol structure, simulated traffic generation, packet analysis, and defensive security considerations.

The laboratory also reinforced the importance of distinguishing between generic TCP traffic and genuine DNP3 protocol traffic.

All activities were limited to an authorized educational environment.
