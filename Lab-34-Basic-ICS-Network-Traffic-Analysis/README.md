# Lab 34: Basic ICS Network Traffic Analysis

## Overview

This laboratory demonstrates the fundamentals of network traffic analysis in an Industrial Control Systems (ICS) environment.

The exercise used a controlled ICS traffic simulation on an AWS EC2 Ubuntu Linux system. Simulated Modbus-style and DNP3-style TCP traffic was generated over the loopback interface and captured using `tcpdump`. The resulting packet capture was analyzed using TShark to identify protocol activity, packet characteristics, payload sizes, and baseline bandwidth behavior.

> **Environment Limitation**
>
> This laboratory used simulated ICS traffic in a controlled AWS EC2 environment.
>
> No physical PLC, RTU, HMI, SCADA server, industrial switch, or production ICS network was involved.
>
> The traffic observed on TCP ports 1502 and 20000 represents a laboratory simulation of Modbus and DNP3 communication patterns.

---

# Objectives

The objectives of this laboratory were to:

* Capture simulated ICS network traffic.
* Identify Modbus-style and DNP3-style communication.
* Analyze TCP communication patterns.
* Examine application payload characteristics.
* Establish a basic network traffic baseline.
* Measure packet rate and bandwidth.
* Preserve packet-capture evidence.
* Generate SHA-256 integrity evidence.
* Document findings in a portfolio-quality format.

---

# Environment

| Component             | Value                        |
| --------------------- | ---------------------------- |
| Platform              | AWS EC2                      |
| Operating System      | Ubuntu 24.04.3 LTS           |
| Architecture          | x86_64                       |
| Capture Interface     | `lo`                         |
| Packet Capture Tool   | tcpdump 4.99.4               |
| Analysis Tool         | TShark 4.2.2                 |
| Capture Format        | PCAP                         |
| Simulated Modbus Port | TCP/1502                     |
| Simulated DNP3 Port   | TCP/20000                    |
| Traffic Source        | Python ICS traffic generator |

---

# Lab Architecture

The laboratory used a simple controlled simulation:

```text
+------------------------------------------------+
|              AWS EC2 Ubuntu Host               |
|                                                |
|              Loopback Interface (lo)          |
|                         |                      |
|             +-----------+-----------+          |
|             |                       |          |
|       TCP/1502                 TCP/20000       |
|     Modbus-style              DNP3-style       |
|       Traffic                   Traffic        |
|             |                       |          |
|             +-----------+-----------+          |
|                         |                      |
|                  tcpdump Capture              |
|                         |                      |
|              ics-baseline.pcap                |
|                         |                      |
|                      TShark                   |
|                         |                      |
|              Protocol Analysis                |
+------------------------------------------------+
```

---

# Task 1 — Capture Normal ICS Traffic

## 1.1 Network Interface Identification

The available network interfaces were checked before starting the capture.

The laboratory used the loopback interface:

```text
lo       UNKNOWN   127.0.0.1/8
ens5     UP        172.31.10.109/24
docker0  DOWN      172.17.0.1/16
```

The loopback interface was selected because the simulated ICS services were running locally on the same host.

---

## 1.2 ICS Traffic Generator

A Python-based traffic generator was created:

```text
scripts/ics-traffic-generator.py
```

The generator produced two controlled traffic patterns:

* Modbus-style TCP messages on port `1502`
* DNP3-style TCP messages on port `20000`

Example generator output:

```text
MODBUS: sent 12 bytes
DNP3: sent 8 bytes
MODBUS: sent 12 bytes
DNP3: sent 8 bytes
...
ICS traffic generation complete.
```

---

## 1.3 Simulated ICS Listeners

Two local TCP listeners were created for the laboratory:

```text
127.0.0.1:1502
127.0.0.1:20000
```

These listeners allowed the traffic generator to establish TCP connections and transmit simulated industrial protocol payloads.

---

## 1.4 Packet Capture

Traffic was captured using:

```bash
sudo tcpdump -i lo -nn -s 0 \
-w capture/ics-baseline.pcap \
'tcp port 1502 or tcp port 20000'
```

The final capture successfully recorded:

```text
329 packets captured
658 packets received by filter
0 packets dropped by kernel
```

The resulting PCAP was:

```text
capture/ics-baseline.pcap
```

---

# Task 2 — Identify Protocol Types

## 2.1 Packet Counts

TShark was used to identify traffic associated with the simulated ICS ports.

Results:

| Traffic Type | TCP Port | Packets |
| ------------ | -------: | ------: |
| Modbus-style |     1502 |     166 |
| DNP3-style   |    20000 |     163 |
| Total        |        — |     329 |

The two simulated protocol streams accounted for the complete capture.

---

## 2.2 Modbus-Style Traffic

The simulated Modbus traffic used TCP port `1502`.

Example payload:

```text
000100000006010300000002
```

The payload length was:

```text
12 bytes
```

The traffic repeatedly followed a predictable pattern:

```text
TCP connection
     |
     v
Modbus-style payload
     |
     v
TCP connection termination
```

The repeated communication pattern is useful for establishing a basic ICS network baseline.

---

## 2.3 DNP3-Style Traffic

The simulated DNP3 traffic used TCP port `20000`.

The generator transmitted:

```text
8-byte payload
```

The capture showed repeated connections to TCP port `20000`.

The traffic therefore provided a controlled representation of DNP3-style communication behavior.

> **Important:** The traffic generated in this laboratory is simulated protocol traffic. It should not be interpreted as a full implementation of the Modbus or DNP3 protocol stack.

---

## 2.4 Protocol Analysis Evidence

Detailed packet information was exported to:

```text
analysis/protocol-analysis.txt
```

The analysis includes:

* Frame number
* Relative timestamp
* Source address
* Destination address
* Source port
* Destination port
* TCP payload length
* Payload data where available

---

# Task 3 — Establish a Network Traffic Baseline

## 3.1 Capture Statistics

The final PCAP was analyzed using `capinfos`.

The following baseline measurements were recorded:

| Metric              |           Result |
| ------------------- | ---------------: |
| Packets             |              329 |
| Capture duration    | 9.722155 seconds |
| Data size           |            22 kB |
| Data byte rate      |   2340 bytes/sec |
| Data bit rate       |          18 kbps |
| Average packet size |      69.16 bytes |
| Average packet rate |   33 packets/sec |
| Packet drops        |                0 |

---

## 3.2 Baseline Interpretation

The laboratory traffic demonstrated a low-bandwidth and highly repetitive communication pattern.

The simulated ICS traffic consisted primarily of:

* Short TCP connections
* Small application payloads
* Repeated Modbus-style messages
* Repeated DNP3-style messages
* Predictable connection behavior

This provides a basic baseline that could be compared against future captures.

---

## 3.3 Potential Anomalies

In a real ICS environment, changes from an established baseline could require investigation.

Examples include:

* Unexpected increases in bandwidth
* Sudden increases in packet frequency
* New source or destination addresses
* Unexpected industrial protocols
* Unusual TCP ports
* Unexpected connection attempts
* Abnormally large payloads
* Repeated failed connections
* Communication outside approved network paths

A baseline does not automatically identify an attack. It provides a reference point that helps analysts identify traffic requiring further investigation.

---

# Evidence and Integrity

The following evidence was preserved:

```text
capture/ics-baseline.pcap
analysis/protocol-analysis.txt
analysis/bandwidth-baseline.txt
evidence/capture-summary.txt
evidence/protocol-counts.txt
evidence/capture-integrity.txt
```

The SHA-256 hash of the final packet capture was recorded as:

```text
26359265f400c2e5b96821531a3c247eefc0794fab90465e9b96dc3118e21a06
```

The hash provides a way to verify that the PCAP has not been modified after evidence collection.

Integrity verification can be performed with:

```bash
sha256sum capture/ics-baseline.pcap
```

The resulting SHA-256 value should match the value recorded in:

```text
evidence/capture-integrity.txt
```

---

# Repository Structure

```text
Lab-34-Basic-ICS-Network-Traffic-Analysis/
│
├── README.md
│
├── capture/
│   └── ics-baseline.pcap
│
├── analysis/
│   ├── bandwidth-baseline.txt
│   └── protocol-analysis.txt
│
├── evidence/
│   ├── capture-integrity.txt
│   ├── capture-summary.txt
│   └── protocol-counts.txt
│
└── scripts/
    └── ics-traffic-generator.py
```

---

# Key Findings

The laboratory successfully demonstrated:

1. Successful packet capture using `tcpdump`.
2. Successful analysis using TShark.
3. Identification of simulated Modbus-style traffic.
4. Identification of simulated DNP3-style traffic.
5. 329 packets captured during the final test.
6. Zero packets dropped by the capture process.
7. A repeatable low-bandwidth traffic pattern.
8. A baseline of approximately 18 kbps.
9. An average packet rate of approximately 33 packets/sec.
10. Preservation of PCAP integrity using SHA-256.

---

# Security Relevance

Network traffic baselining is an important part of ICS security monitoring.

Industrial environments often contain predictable communication patterns between:

```text
HMI
 |
SCADA
 |
PLC
 |
Field Devices
```

Unexpected changes in these communication patterns may provide useful indicators for security monitoring.

For example, an analyst could compare a known-good baseline with a later capture and investigate:

```text
Normal:
PLC <--> SCADA
        |
   predictable traffic

Potential anomaly:
Unknown Host --> PLC
        |
 unexpected protocol
        |
 unexpected connection
```

This approach supports network monitoring, incident investigation, and detection engineering.

---

# Limitations

This laboratory has several limitations.

### Simulated Environment

The capture was generated locally rather than from a production ICS network.

### Short Capture Duration

The final capture lasted approximately:

```text
9.72 seconds
```

A production baseline would normally require longer observation periods covering different operational states.

### Simulated Protocol Traffic

The traffic generator produced Modbus-style and DNP3-style traffic patterns rather than complete industrial protocol implementations.

### Loopback Capture

Traffic was captured on:

```text
lo
```

rather than a physical industrial Ethernet interface.

### No Production Impact

No physical PLC, SCADA system, RTU, HMI, industrial controller, or production process was modified.

---

# Recommended Improvements for a Real ICS Environment

For a production ICS network, a more comprehensive monitoring approach would include:

* Longer baseline collection periods
* Multiple operational states
* Passive network monitoring
* Industrial protocol-aware IDS
* Asset inventory
* Approved communication matrices
* Network segmentation
* SPAN/TAP-based monitoring
* Continuous packet analysis
* Alerting for unauthorized communications
* Centralized security logging
* Historical traffic comparison

The monitoring system should remain passive where possible to avoid disrupting industrial operations.

---

# Conclusion

This laboratory provided practical experience with basic ICS network traffic analysis.

A controlled ICS simulation was created using Modbus-style and DNP3-style TCP traffic. The traffic was captured with `tcpdump` and analyzed using TShark.

The final capture contained **329 packets**, with **166 packets associated with the simulated Modbus port** and **163 packets associated with the simulated DNP3 port**. The measured baseline was approximately **18 kbps** with an average packet rate of approximately **33 packets per second**.

The exercise demonstrated how network traffic characteristics can be documented and used as a baseline for future anomaly detection.

The resulting PCAP, analysis files, evidence, and integrity hash provide a reproducible laboratory record suitable for an ICS cybersecurity portfolio.

---

# Lab Status

**LAB 34 — BASIC ICS NETWORK TRAFFIC ANALYSIS**

**Status: COMPLETE**

Core outcomes achieved:

* [x] ICS traffic simulation
* [x] Network interface identification
* [x] Packet capture
* [x] Modbus-style traffic analysis
* [x] DNP3-style traffic analysis
* [x] Packet counting
* [x] Payload analysis
* [x] Bandwidth baseline
* [x] Capture summary
* [x] Evidence preservation
* [x] SHA-256 integrity documentation
* [x] Portfolio documentation
