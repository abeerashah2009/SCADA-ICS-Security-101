# Lab 15: Introduction to DNP3 Protocol

## Lab Overview

DNP3 (Distributed Network Protocol) is an industrial communication protocol widely used in Industrial Control Systems (ICS) and Supervisory Control and Data Acquisition (SCADA) environments.

DNP3 is particularly common in utility environments such as:

* Electrical power systems
* Water and wastewater systems
* Remote terminal units (RTUs)
* SCADA systems
* Substations
* Distribution automation

This laboratory introduces the fundamental concepts of DNP3 communication, packet structure, traffic analysis, simulated communication, and DNP3 security considerations.

The practical exercises are performed inside an authorized educational environment. No production ICS/SCADA system should be contacted.

---

# Objectives

By completing this laboratory, the learner will be able to:

1. Explain what DNP3 is.
2. Explain where DNP3 is commonly used.
3. Identify the major layers of DNP3 communication.
4. Understand the DNP3 data-link layer.
5. Understand the DNP3 transport layer.
6. Understand the DNP3 application layer.
7. Identify important DNP3 packet fields.
8. Understand DNP3 control fields.
9. Understand DNP3 function codes at a basic level.
10. Capture simulated DNP3-related traffic.
11. Analyze traffic using Wireshark.
12. Use Scapy to create a controlled laboratory simulation.
13. Understand the difference between simulated DNP3 payloads and valid protocol frames.
14. Identify major DNP3 security challenges.
15. Understand defensive controls for DNP3-based ICS environments.

---

# Prerequisites

Recommended knowledge:

* Basic Linux command-line usage
* Basic networking concepts
* TCP/IP fundamentals
* Basic understanding of ICS/SCADA
* Familiarity with Wireshark
* Basic Python knowledge
* Basic Scapy knowledge

---

# Lab Environment

## Operating System

Example:

```text
Operating System : Ubuntu Linux
Shell            : Bash
Python           : Python 3
Packet Tool      : Wireshark / TShark
Python Library   : Scapy
Protocol         : DNP3
```

---

# Safety Scope

This laboratory is strictly educational and defensive.

Only use:

* Localhost
* Local test servers
* Simulated traffic
* Authorized laboratory systems

Do not:

* Scan public DNP3 devices.
* Connect to production SCADA systems.
* Send packets to real substations.
* Modify real RTU values.
* Attempt unauthorized DNP3 communication.
* Perform denial-of-service testing.
* Attempt to bypass ICS security controls.

All practical traffic in this lab should remain inside the authorized laboratory environment.

---

# DNP3 Fundamentals

## What is DNP3?

DNP3 stands for:

**Distributed Network Protocol**

It was designed for reliable communication between control-system devices.

DNP3 is commonly associated with:

```text
SCADA Master
     |
     |
     v
   DNP3
     |
     v
   RTU
     |
     v
Field Devices
```

A typical DNP3 environment may contain:

* SCADA master stations
* RTUs
* Intelligent Electronic Devices (IEDs)
* PLCs
* Sensors
* Control equipment

---

# Where DNP3 is Used

DNP3 is commonly encountered in:

### Electrical Utilities

Examples:

* Substations
* Distribution systems
* Power generation
* Remote monitoring

### Water Utilities

Examples:

* Pump stations
* Water treatment
* Reservoir monitoring

### Other Industrial Environments

DNP3 can also be used in remote monitoring and control environments where reliable communication is important.

---

# DNP3 Communication Model

A simplified architecture is:

```text
+----------------------+
| SCADA Master Station |
+----------------------+
           |
           |
       DNP3 Network
           |
           |
+----------------------+
| RTU / IED            |
+----------------------+
           |
           |
+----------------------+
| Field Devices        |
+----------------------+
```

The master generally communicates with outstations such as RTUs or IEDs.

---

# DNP3 Protocol Layers

DNP3 can be understood through several important layers.

## 1. Data Link Layer

The data-link layer provides communication framing and addressing.

Important concepts include:

* Source address
* Destination address
* Control field
* Frame length
* CRC

The beginning of a DNP3 data-link frame commonly contains the DNP3 start bytes:

```text
05 64
```

These bytes are useful when identifying DNP3 frames.

---

## 2. Transport Layer

The DNP3 transport layer provides fragmentation and reassembly of larger application messages.

Important concepts include:

* First fragment
* Final fragment
* Sequence information
* Fragmentation

---

## 3. Application Layer

The application layer contains the actual DNP3 operations and data.

Important concepts include:

* Application control
* Function codes
* Object groups
* Object variations
* Qualifiers
* Data objects

---

# DNP3 Packet Structure

A simplified DNP3 message can be represented as:

```text
+----------------------+
| Data Link Layer      |
+----------------------+
| Transport Layer      |
+----------------------+
| Application Layer   |
+----------------------+
```

The data-link layer includes information such as:

```text
Start
Length
Control
Destination
Source
CRC
```

The application layer can contain:

```text
Application Control
Function Code
Object Headers
Object Data
```

---

# Important DNP3 Fields

## Start Bytes

Typical DNP3 data-link frames begin with:

```text
05 64
```

These bytes identify the beginning of a DNP3 frame.

---

## Length

The length field indicates the size of the DNP3 link-layer data.

---

## Control Field

The control field provides information about how the frame should be handled.

It can contain information related to:

* Direction
* Primary/secondary role
* Frame count
* Frame count validity
* Function-related control information

---

## Destination Address

Identifies the intended DNP3 destination.

---

## Source Address

Identifies the DNP3 source.

---

## CRC

DNP3 uses CRC values at the data-link layer to help detect transmission errors.

CRC is primarily an integrity mechanism for transmission errors.

It should not be confused with modern cryptographic authentication.

---

# DNP3 Application Layer

The application layer carries higher-level DNP3 operations.

Examples of operations include:

* Reading data
* Writing data
* Controlling outputs
* Reporting events
* Confirming operations

DNP3 uses object groups and variations to represent different types of information.

---

# DNP3 Function Codes

DNP3 application-layer function codes identify requested operations.

Examples include:

```text
READ
WRITE
SELECT
OPERATE
DIRECT OPERATE
DIRECT OPERATE NO ACKNOWLEDGE
```

The exact interpretation depends on the DNP3 application-layer message.

---

# Task 1: Review DNP3 Packet Breakdown

## Task Objective

Understand the basic structure of DNP3 packets and identify important protocol fields.

---

## Step 1.1: Verify Python

Run:

```bash
python3 --version
```

Expected:

```text
Python 3.x.x
```

Record the result in `lab-notes.md`.

---

## Step 1.2: Verify Scapy

Run:

```bash
python3 -c "import scapy; print(scapy.__version__)"
```

If Scapy is not installed, install it using the laboratory-approved package method.

For a user-local installation:

```bash
python3 -m pip install --user scapy
```

Verify again:

```bash
python3 -c "from scapy.all import IP, TCP, Raw; print('Scapy OK')"
```

Expected:

```text
Scapy OK
```

---

## Step 1.3: Check Wireshark/TShark

Run:

```bash
which wireshark
```

and:

```bash
which tshark
```

If available, verify:

```bash
tshark --version
```

Record the installed version in `lab-notes.md`.

---

# Step 1.4: Understand the DNP3 Filter

If Wireshark has DNP3 protocol dissection available, the protocol display filter can be:

```text
dnp3
```

A useful fallback filter for controlled DNP3-port traffic is:

```text
tcp.port == 20000
```

DNP3 commonly uses TCP/UDP port:

```text
20000
```

Important:

A packet sent to TCP port 20000 is not automatically a valid DNP3 packet.

Wireshark must be able to recognize and dissect the payload as DNP3.

---

# Step 1.5: Identify DNP3 Layers

When a valid DNP3 packet is available in Wireshark, identify:

```text
Ethernet
   |
IP
   |
TCP/UDP
   |
DNP3
   |
Data Link
   |
Transport
   |
Application
```

Record the fields visible in the packet details.

---

# Expected Result — Task 1

The learner should be able to identify:

```text
[PASS] DNP3 purpose understood
[PASS] DNP3 use in ICS/SCADA understood
[PASS] Data Link Layer identified
[PASS] Transport Layer identified
[PASS] Application Layer identified
[PASS] Control field concept understood
[PASS] Source/Destination address concepts understood
[PASS] CRC concept understood
```

---

# Task 2: Capture DNP3 Traffic in a Simulated Environment

## Task Objective

Generate controlled laboratory traffic and inspect it using packet-analysis tools.

---

# Important Practical Note

The basic Scapy example commonly used in introductory DNP3 exercises is:

```python
Ether() / IP() / TCP() / Raw()
```

This creates Ethernet/IP/TCP traffic containing arbitrary application data.

It does **not automatically create a standards-compliant DNP3 frame**.

Therefore this lab distinguishes between:

### DNP3 Traffic Simulation

A controlled TCP payload that represents DNP3-related laboratory data.

### Valid DNP3 Traffic

A standards-compliant DNP3 frame that Wireshark can dissect as DNP3.

This distinction is important for accurate protocol analysis.

---

# Step 2.1: Create the Simulation Script

Create:

```bash
nano dnp3-simulation.py
```

The script should generate traffic only toward localhost or another explicitly authorized laboratory endpoint.

The supplied simulation script will be used to demonstrate:

* Ethernet framing
* IP communication
* TCP transport
* Application payload
* DNP3-related test data

---

# Step 2.2: Review the Script

Run:

```bash
cat dnp3-simulation.py
```

Then perform a syntax check:

```bash
python3 -m py_compile dnp3-simulation.py
```

No output indicates successful compilation.

---

# Step 2.3: Start Packet Capture

If using Wireshark:

```bash
wireshark
```

Select the appropriate local interface.

For localhost traffic, this is commonly:

```text
lo
```

Apply:

```text
tcp.port == 20000
```

If valid DNP3 traffic is being captured and dissected, try:

```text
dnp3
```

---

# Step 2.4: Generate Laboratory Traffic

Run:

```bash
python3 dnp3-simulation.py
```

The script should send traffic only to the authorized laboratory destination.

Do not change the destination to an unknown or public ICS system.

---

# Step 2.5: Analyze the Captured Traffic

In Wireshark, examine:

```text
Ethernet
IP
TCP
Data
```

Look for:

* Source IP
* Destination IP
* Source port
* Destination port
* TCP flags
* TCP payload
* Payload length

If Wireshark recognizes the payload as DNP3, additionally inspect:

* DNP3 link layer
* DNP3 control field
* Source address
* Destination address
* Transport information
* Application layer
* Function code
* Object information

---

# Expected Result — Task 2

Record:

```text
[PASS] Simulation script executed
[PASS] Traffic generated in authorized environment
[PASS] Packet capture performed
[PASS] Source/destination information identified
[PASS] TCP port identified
[PASS] Payload inspected
[PASS] DNP3-related fields reviewed where available
```

---

# Task 3: Identify DNP3 Security Challenges

## Task Objective

Understand why DNP3 communication requires additional security controls.

---

# Step 3.1: Lack of Traditional Encryption

Traditional DNP3 was designed primarily for reliable industrial communication rather than modern Internet security.

Depending on the deployment and security configuration, DNP3 traffic may not provide modern confidentiality by itself.

Potential concern:

```text
Sensitive industrial information
          |
          v
Unprotected communication
          |
          v
Potential information disclosure
```

---

# Step 3.2: Unauthorized Access

If an attacker gains network access to a DNP3 environment, they may attempt unauthorized communication with exposed devices.

Potential consequences include:

* Unauthorized data collection
* Unauthorized control requests
* Process disruption
* Information disclosure

---

# Step 3.3: Data Manipulation

Unauthorized modification of industrial communication can potentially affect:

* Measurements
* Status information
* Control commands
* Operational decisions

---

# Step 3.4: Man-in-the-Middle Risks

An attacker positioned between communicating systems could potentially attempt to interfere with communication.

Defensive measures are therefore important.

---

# Step 3.5: Attack Surface

Common attack-surface concerns include:

```text
Remote access
     |
     v
Network connectivity
     |
     v
DNP3 devices
     |
     v
Control functions
```

Poor network segmentation can increase exposure.

---

# Step 3.6: Mitigation Strategies

Recommended defensive controls include:

### Network Segmentation

Separate:

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
      RTUs/IEDs
```

---

### Access Control

Restrict communication to authorized systems.

Use:

* ACLs
* Firewall rules
* Allow-listing
* Least privilege

---

### Secure Remote Access

Remote access should use approved secure mechanisms.

Examples:

* VPN
* MFA
* Jump servers
* Privileged access management

---

### Monitoring

Monitor:

* DNP3 communication
* Unexpected source addresses
* Unexpected destinations
* Unusual function codes
* Unexpected control operations
* Configuration changes

---

### Defense-in-Depth

No single security control should be considered sufficient.

A layered approach should include:

```text
                ICS Security
                     |
        +------------+------------+
        |            |            |
     Network       Access      Monitoring
     Security      Control     & Detection
        |            |            |
    Firewall      Least        Logging
    Segmentation  Privilege    Alerts
        |            |            |
        +------------+------------+
                     |
               ICS Protection
```

---

# Task 3 Expected Result

```text
[PASS] DNP3 security limitations identified
[PASS] Unauthorized access risk understood
[PASS] Data manipulation risk understood
[PASS] MITM risk understood
[PASS] Network segmentation identified
[PASS] ACLs identified
[PASS] Secure remote access identified
[PASS] Monitoring identified
[PASS] Defense-in-depth understood
```

---

# Task 4: DNP3 Security Review

Create:

```bash
nano dnp3-security-review.md
```

Document:

1. Three DNP3 security concerns.
2. Three possible defensive controls.
3. Why network segmentation is important.
4. Why monitoring is important.
5. Why unauthorized DNP3 access should be prevented.

---

# Troubleshooting

## Scapy Import Error

If you receive:

```text
ModuleNotFoundError: No module named 'scapy'
```

Install Scapy in the authorized laboratory environment:

```bash
python3 -m pip install --user scapy
```

Then verify:

```bash
python3 -c "from scapy.all import IP, TCP, Raw; print('Scapy OK')"
```

---

## Wireshark Not Found

Check:

```bash
which wireshark
```

and:

```bash
which tshark
```

If neither exists, record the limitation in `lab-notes.md` before installing packages.

---

## No Packets Captured

Check:

```bash
ip addr
```

For localhost traffic, make sure the capture includes:

```text
lo
```

For normal network traffic, identify the active interface using:

```bash
ip route
```

---

## `dnp3` Filter Shows Nothing

This can happen if the generated traffic is only a generic TCP payload.

Try:

```text
tcp.port == 20000
```

Then inspect the TCP payload manually.

Remember:

```text
TCP port 20000
        ≠
Automatically valid DNP3
```

A valid DNP3 frame must contain a structure that the protocol dissector recognizes.

---

# Evidence to Collect

The following evidence should be maintained:

```text
README.md
lab-notes.md
dnp3-simulation.py
dnp3-security-review.md
```

If Wireshark capture files are created, do not commit unnecessarily large captures.

If a small authorized capture is required for evidence, document:

```text
Capture Interface
Capture Filter
Display Filter
Packet Count
Protocol
Source
Destination
```

---

# Task Results

## Task 1

```text
[PASS] DNP3 fundamentals reviewed
[PASS] DNP3 layers reviewed
[PASS] Packet structure reviewed
[PASS] Control field concept reviewed
[PASS] Addressing reviewed
[PASS] CRC concept reviewed
```

## Task 2

```text
[PASS] Scapy environment verified
[PASS] Simulation script created
[PASS] Simulation script syntax verified
[PASS] Authorized traffic generated
[PASS] Packet capture performed
[PASS] Traffic analyzed
```

## Task 3

```text
[PASS] Security challenges identified
[PASS] Unauthorized access risk documented
[PASS] Data manipulation risk documented
[PASS] MITM risk documented
[PASS] Defensive controls documented
```

---

# Skills Practiced

This laboratory develops skills in:

* DNP3 protocol fundamentals
* ICS/SCADA networking
* Packet analysis
* Wireshark
* Scapy
* TCP/IP analysis
* Industrial protocol identification
* DNP3 security awareness
* Network segmentation
* Access control
* Defensive monitoring
* Technical documentation

---

# Key Takeaways

1. DNP3 is an important industrial communication protocol.
2. It is widely used in utility and SCADA environments.
3. DNP3 communication can be understood through data-link, transport, and application concepts.
4. DNP3 data-link frames contain important addressing and control information.
5. DNP3 uses CRC mechanisms for transmission-error detection.
6. Application-layer operations include functions such as read, write, select, and operate.
7. TCP port 20000 is commonly associated with DNP3.
8. A TCP packet on port 20000 is not automatically a valid DNP3 packet.
9. Wireshark can help analyze DNP3 communication when the traffic is correctly recognized.
10. Scapy can be used for controlled packet-generation exercises.
11. Traditional DNP3 deployments may require additional security controls.
12. Network segmentation is important for reducing DNP3 exposure.
13. Access control and monitoring are important defensive mechanisms.
14. Secure remote access should be implemented for authorized management.
15. ICS security should use defense-in-depth.

---

# Safety Verification

```text
[PASS] No public ICS systems accessed
[PASS] No production SCADA systems accessed
[PASS] No production RTUs accessed
[PASS] No unauthorized scanning performed
[PASS] No unauthorized DNP3 communication performed
[PASS] No industrial process modified
[PASS] Testing limited to authorized laboratory environment
```

---

# Lab Completion Checklist

* [ ] Understand DNP3 fundamentals
* [ ] Understand DNP3 use in ICS/SCADA
* [ ] Understand DNP3 protocol layers
* [ ] Identify DNP3 packet fields
* [ ] Understand control field
* [ ] Understand source and destination addressing
* [ ] Understand CRC
* [ ] Verify Python
* [ ] Verify Scapy
* [ ] Verify Wireshark/TShark
* [ ] Create DNP3 simulation
* [ ] Capture laboratory traffic
* [ ] Analyze captured packets
* [ ] Review DNP3 security challenges
* [ ] Document mitigation strategies
* [ ] Complete `lab-notes.md`
* [ ] Complete `dnp3-security-review.md`
* [ ] Run `git diff --check`
* [ ] Commit laboratory files
* [ ] Push laboratory files to GitHub
* [ ] Verify clean Git working tree

---

# Conclusion

This laboratory introduced the DNP3 protocol and its role in ICS/SCADA environments.

The exercises covered DNP3 architecture, protocol layers, packet structure, traffic analysis, Scapy-based simulation, Wireshark analysis, and security considerations.

The laboratory also demonstrated an important protocol-analysis principle: generating traffic toward a DNP3-associated TCP port does not automatically make that traffic valid DNP3. Accurate analysis requires understanding the actual protocol structure.

Understanding DNP3 is valuable for ICS security professionals because defenders must recognize legitimate industrial communication before they can identify suspicious or abnormal activity.

All practical work in this laboratory should remain within an authorized educational environment.
