# Lab 16: Basic Network Monitoring with Wireshark

**Lab:** Lab 16 - Basic Network Monitoring with Wireshark
**Topic:** Network Monitoring and ICS/SCADA Traffic Analysis
**Environment:** Authorized educational laboratory
**Primary Tool:** TShark/Wireshark
**Protocols Reviewed:** TCP, HTTP, Modbus, DNP3

---

# 1. Lab Objective

The objective of this laboratory was to understand basic network
monitoring and packet analysis using Wireshark/TShark.

The laboratory focused on:

- Capturing network traffic
- Reading packet information
- Using capture filters
- Using display filters
- Reviewing HTTP and TCP traffic
- Testing Modbus and DNP3 protocol filters
- Understanding ICS/SCADA network monitoring

All practical testing was limited to the authorized educational
laboratory environment.

---

# 2. Environment Verification

## 2.1 Python Version

Command:

python3 --version

Result:

Python 3.12.3

Status:

[PASS] Python verified

---

## 2.2 TShark Installation

Command:

which tshark

Result:

/usr/bin/tshark

Status:

[PASS] TShark installed

---

## 2.3 TShark Version

Command:

tshark --version

Result:

TShark (Wireshark) 4.2.2

Status:

[PASS] TShark version verified

---

## 2.4 Network Interfaces

Command:

ip -br link

Observed interfaces:

- lo
- ens5
- docker0

The loopback interface `lo` was selected for the laboratory
traffic capture.

Status:

[PASS] Network interface identified

---

## 2.5 TShark Capture Interface

Command:

sudo tshark -D

Result:

1. ens5
2. any
3. lo (Loopback)
4. docker0

Status:

[PASS] Capture interfaces identified

---

# 3. Task 1 — Wireshark/TShark Setup

Wireshark is a network protocol analyzer used to capture and
inspect network traffic.

Because this laboratory environment is a command-line Ubuntu
environment, TShark was used instead of the graphical Wireshark
interface.

TShark provides packet capture and packet analysis functionality
from the command line.

Status:

[PASS] Wireshark/TShark functionality verified

---

# 4. Task 2 — Capture Live Network Traffic

## 4.1 Capture Interface

Interface:

lo

The loopback interface was selected because the laboratory traffic
was generated locally on the system.

---

## 4.2 Initial Capture

Command:

sudo tshark -i lo -c 5

Observed traffic included:

- DNS traffic
- TCP traffic
- Localhost communication

Status:

[PASS] Live traffic captured

---

## 4.3 Local HTTP Traffic Generation

A local HTTP service was already available on TCP port 8080.

Command:

curl http://127.0.0.1:8080

Result:

HTTP directory listing returned successfully.

Status:

[PASS] Local HTTP traffic generated

---

# 5. Task 3 — Capture HTTP Traffic

## 5.1 Capture Command

Command:

sudo tshark -i lo -f "tcp port 8080" -c 10

Result:

10 packets captured.

Observed traffic included:

- TCP SYN
- TCP SYN/ACK
- TCP ACK
- HTTP GET request
- HTTP 200 OK response
- TCP FIN/ACK

Status:

[PASS] TCP/HTTP traffic captured

---

# 6. Packet Analysis

Capture file:

/tmp/lab16.pcapng

Command:

sudo tshark -r /tmp/lab16.pcapng

Observed:

- Source IP: 127.0.0.1
- Destination IP: 127.0.0.1
- Destination Port: 8080
- Protocols: TCP and HTTP

The packet capture demonstrated a complete local TCP connection
including connection establishment, HTTP communication, and
connection termination.

Status:

[PASS] Packet capture analyzed

---

# 7. HTTP Display Filter

Command:

sudo tshark -r /tmp/lab16.pcapng -Y "http"

Result:

HTTP GET / HTTP/1.1

HTTP/1.0 200 OK

Observation:

The HTTP display filter successfully identified HTTP packets
inside the packet capture.

Status:

[PASS] HTTP display filter tested

---

# 8. Modbus Filter Test

Command:

sudo tshark -r /tmp/lab16.pcapng -Y "modbus"

Result:

No packets matched the Modbus display filter.

Observation:

The capture did not contain valid Modbus protocol packets.

The laboratory therefore did not claim the HTTP traffic as
Modbus traffic.

Status:

[PASS] Modbus filter tested and result documented

---

# 9. DNP3 Filter Test

Command:

sudo tshark -r /tmp/lab16.pcapng -Y "dnp3"

Result:

No packets matched the DNP3 display filter.

Observation:

The capture did not contain valid DNP3 protocol packets.

The laboratory therefore did not claim the HTTP traffic as
DNP3 traffic.

Status:

[PASS] DNP3 filter tested and result documented

---

# 10. ICS Traffic Simulation

A Python-based ICS traffic simulation script was created.

File:

ics-traffic-simulation.py

Syntax verification command:

python3 -m py_compile ics-traffic-simulation.py

Result:

No syntax errors reported.

Status:

[PASS] Simulation script syntax verified

---

## 10.1 Simulation Execution

Command:

python3 ics-traffic-simulation.py

Result:

==================================================
ICS Traffic Simulation
==================================================
[INFO] Sending Modbus traffic to TCP/502
[INFO] No listener on TCP/502
[INFO] Modbus filter can still be tested against packet data.
[INFO] Sending DNP3 traffic to TCP/20000
[INFO] No listener on TCP/20000
[INFO] DNP3 filter can still be tested against packet data.
==================================================
Simulation complete
==================================================

Observation:

The simulation completed successfully.

No persistent Modbus listener was available on TCP/502 and no
persistent DNP3 listener was available on TCP/20000.

Therefore, the simulation results were documented without
claiming that valid Modbus or DNP3 packets were captured.

Status:

[PASS] ICS traffic simulation executed

---

# 11. Protocol Filters Reviewed

## Modbus

Display filter:

modbus

Common Modbus TCP port:

502

Purpose:

Used to identify Modbus protocol traffic in packet captures.

---

## DNP3

Display filter:

dnp3

Common DNP3 TCP/UDP port:

20000

Purpose:

Used to identify DNP3 protocol traffic in packet captures.

---

# 12. Important Observation

A very important lesson from this laboratory is that a TCP port
number alone does not prove that a packet contains a specific
industrial protocol.

For example:

TCP/502 is commonly associated with Modbus TCP.

TCP/20000 is commonly associated with DNP3.

However, protocol identification should be confirmed by examining
the actual packet contents and protocol dissection.

---

# 13. ICS/SCADA Security Analysis

Network monitoring can help identify suspicious activity in
industrial environments.

Important observations include:

- Unexpected connections
- Unknown source addresses
- Unexpected destination ports
- Repeated connection attempts
- Unusual protocol traffic
- Unexpected Modbus commands
- Unexpected DNP3 communication

Network monitoring should be combined with other security controls
such as firewalls, segmentation, access control, logging, and
incident response.

Status:

[PASS] ICS/SCADA monitoring concepts reviewed

---

# 14. Safety Verification

[PASS] Testing performed in authorized laboratory environment

[PASS] No production ICS accessed

[PASS] No production SCADA accessed

[PASS] No industrial process modified

[PASS] No unauthorized scanning performed

[PASS] Traffic analysis limited to laboratory systems

---

# 15. Evidence Files

The laboratory contains:

README.md
lab-notes.md
ics-traffic-simulation.py

Packet capture:

/tmp/lab16.pcapng

---

# 16. Final Results

## Task 1

[PASS] TShark installed

[PASS] TShark version verified

[PASS] Network interfaces identified

---

## Task 2

[PASS] Loopback interface selected

[PASS] Live traffic captured

[PASS] HTTP traffic generated

[PASS] TCP traffic observed

---

## Task 3

[PASS] Packet capture analyzed

[PASS] HTTP filter tested

[PASS] Modbus filter tested

[PASS] DNP3 filter tested

[PASS] Protocol identification results documented

---

## Task 4

[PASS] ICS traffic simulation script created

[PASS] Python syntax verified

[PASS] Simulation executed

[PASS] Modbus listener limitation documented

[PASS] DNP3 listener limitation documented

---

# 17. Skills Practiced

[PASS] Network monitoring

[PASS] Packet capture

[PASS] TShark

[PASS] TCP analysis

[PASS] HTTP analysis

[PASS] Display filters

[PASS] Capture filters

[PASS] Modbus protocol filtering

[PASS] DNP3 protocol filtering

[PASS] ICS/SCADA traffic analysis

[PASS] Security observation

[PASS] Technical documentation

---

# 18. Final Conclusion

This laboratory provided practical experience with basic network
monitoring using TShark.

Live traffic was captured on the loopback interface and analyzed
using packet and protocol filters.

HTTP and TCP traffic were successfully identified in the capture.

Modbus and DNP3 filters were also tested. No valid Modbus or DNP3
packets were present in the captured traffic, and this limitation
was documented instead of incorrectly identifying generic TCP
traffic as industrial protocol traffic.

The laboratory demonstrated the importance of packet analysis and
protocol validation when monitoring ICS/SCADA environments.

All activities were performed within the authorized educational
laboratory environment.
