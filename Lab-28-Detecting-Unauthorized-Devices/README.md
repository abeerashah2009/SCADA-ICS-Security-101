# Lab 28: Detecting Unauthorized Devices

## 📌 Lab Overview

This lab demonstrates a practical network-security workflow for identifying unknown or potentially unauthorized devices using **Nmap**, network baselining, follow-up scanning, Linux neighbor-table inspection, and network-interface health checks.

The exercise was performed in an **AWS EC2 Ubuntu environment** representing a controlled network-security lab.

The lab focuses on the principle that an organization should maintain a known network baseline and continuously compare current network observations against that baseline to identify unexpected changes.

> **Environment Note:**  
> This exercise was performed in AWS EC2 rather than a physical ICS/SCADA facility. Therefore, physical inspection of switches, cables, ports, PLCs, HMIs, and industrial equipment was not possible. This limitation is explicitly documented in the assessment.

---

# 🎯 Objectives

By completing this lab, the following objectives were achieved:

- Verify availability of Nmap.
- Identify the actual network interface and subnet.
- Perform network host discovery.
- Establish a network baseline.
- Record discovered IP addresses, hostnames, and MAC addresses.
- Perform a follow-up network scan.
- Compare baseline and follow-up results.
- Identify newly appearing hosts.
- Inspect the Linux neighbor table.
- Check network-interface health.
- Document physical-inspection limitations.
- Preserve scan results as auditable evidence.
- Produce professional security documentation.

---

# 🧰 Tools and Technologies

| Tool / Technology | Purpose |
|---|---|
| Ubuntu Linux | Lab operating system |
| AWS EC2 | Lab environment |
| Nmap 7.94SVN | Network host discovery |
| Linux `ip` utility | Network configuration and inspection |
| `ip neigh` | Neighbor/MAC table inspection |
| `tee` | Evidence preservation |
| Git | Version control and audit trail |
| Markdown | Security documentation |

---

# 🌐 Lab Environment

| Parameter | Value |
|---|---|
| Environment | AWS EC2 Ubuntu |
| Network Interface | `ens5` |
| Scanner IP | `172.31.10.102` |
| Subnet | `172.31.10.0/24` |
| Gateway | `172.31.10.1` |
| Nmap Version | `7.94SVN` |
| Scan Type | Host Discovery |
| Nmap Option | `-sn` |

The original lab instructions used:

```text
192.168.1.0/24
```

The example subnet was replaced with the actual AWS subnet:

```text
172.31.10.0/24
```

because that was the network assigned to the lab environment.

---

# 🔎 Task 1: Network Scanning and Baseline

## Step 1 — Verify Nmap

Nmap was verified before performing the network scan.

Command:

```bash
nmap --version
```

### Result

```text
Nmap version 7.94SVN
Platform: x86_64-pc-linux-gnu
```

Nmap was successfully available and ready for network discovery.

---

## Step 2 — Identify the Network

The local network configuration was examined using:

```bash
ip -br addr
```

```bash
ip route
```

```bash
ip route get 8.8.8.8
```

### Network Findings

- Interface: `ens5`
- Scanner address: `172.31.10.102/24`
- Network: `172.31.10.0/24`
- Gateway: `172.31.10.1`

This confirmed the correct subnet to use for the baseline scan.

---

# 📡 Step 3 — Perform Baseline Scan

The initial network baseline was created using Nmap host discovery:

```bash
sudo nmap -sn 172.31.10.0/24 | tee scans/baseline-scan.txt
```

The scan examined:

```text
256 IP addresses
```

and identified:

```text
5 active hosts
```

### Baseline Scan Evidence

```text
scans/baseline-scan.txt
```

---

# 🖥️ Baseline Device Inventory

The discovered devices were documented in:

```text
scans/baseline-inventory.md
```

| IP Address | Hostname | MAC Address | Status |
|---|---|---|---|
| `172.31.10.1` | `ip-172-31-10-1.ec2.internal` | `0A:78:67:64:4C:BD` | To be verified |
| `172.31.10.31` | `ip-172-31-10-31.ec2.internal` | `0A:FF:C8:84:82:11` | To be verified |
| `172.31.10.151` | `ip-172-31-10-151.ec2.internal` | `0A:FF:F4:54:86:5F` | To be verified |
| `172.31.10.187` | `ip-172-31-10-187.ec2.internal` | `0A:FF:CC:EE:2A:A5` | To be verified |
| `172.31.10.102` | `ip-172-31-10-102.ec2.internal` | Local host | Authorized scanner |

> **Important:** "To be verified" does not mean unauthorized. Actual authorization should be confirmed against an approved asset inventory.

---

# 🕵️ Task 2: Detecting Unknown Hosts

## Step 1 — Perform Follow-Up Scan

A second scan was performed shortly after the baseline scan.

Command:

```bash
sudo nmap -sn 172.31.10.0/24 | tee scans/followup-scan.txt
```

### Evidence

```text
scans/followup-scan.txt
```

The follow-up scan again identified:

```text
5 active hosts
```

---

# 📊 Step 2 — Baseline Comparison

The baseline and follow-up results were compared.

Evidence:

```text
scans/baseline-comparison.md
```

### Comparison Results

| Metric | Result |
|---|---:|
| Baseline hosts | 5 |
| Follow-up hosts | 5 |
| New hosts | 0 |
| Removed hosts | 0 |

### Detection Result

```text
No new host detected.
```

The follow-up scan matched the baseline inventory.

This indicates that **no new device appeared during the scan window**.

However, this does not prove that all five devices are authorized. Authorization must be validated against the organization's approved asset inventory.

---

# 🧭 Task 3: Network-Level Inspection

## Step 1 — Neighbor Table Inspection

The Linux neighbor table was inspected using:

```bash
ip neigh show dev ens5
```

Evidence was saved to:

```text
scans/neighbor-table.txt
```

### Observed Neighbors

| IP Address | MAC Address | State |
|---|---|---|
| `172.31.10.1` | `0a:78:67:64:4c:bd` | REACHABLE |
| `172.31.10.151` | `0a:ff:f4:54:86:5f` | REACHABLE |

Both addresses were already present in the Nmap baseline.

No previously unseen network neighbor was identified.

---

# 🖧 Step 2 — Network Interface Health

The network interface was inspected using:

```bash
ip -br link show ens5
```

and:

```bash
ip -s link show ens5
```

Evidence:

```text
scans/interface-statistics.txt
```

### Interface Information

| Parameter | Result |
|---|---|
| Interface | `ens5` |
| State | UP |
| MAC | `0a:ff:d0:91:50:8b` |
| RX Errors | 0 |
| RX Dropped | 0 |
| TX Errors | 0 |
| TX Dropped | 0 |
| Carrier Errors | 0 |
| Collisions | 0 |

The interface was operational and showed zero recorded packet errors or drops during the inspection.

---

# 🧪 Step 3 — Packet Analysis Tool Check

TShark availability was checked using:

```bash
command -v tshark || echo "tshark not installed"
```

### Result

```text
tshark not installed
```

Therefore, packet capture and Wireshark/TShark traffic analysis were not performed during this lab.

This limitation was documented rather than claiming packet analysis that was not actually performed.

---

# 🏭 Physical Inspection Assessment

In a real ICS/SCADA environment, identifying an unknown network device should be followed by physical verification.

Typical checks would include:

- Switch-port inspection
- MAC-address-table correlation
- Cable tracing
- Asset-tag verification
- PLC/HMI inspection
- Network-access-control records
- DHCP records
- Approved asset inventory
- Change-management records
- Asset-owner confirmation

These physical checks could not be performed because the lab was hosted on AWS EC2.

The limitation was documented in:

```text
scans/task3-assessment.md
```

---

# 🛡️ Security Assessment

The lab demonstrated a basic unauthorized-device detection workflow:

```text
Network Identification
        ↓
Baseline Discovery
        ↓
Device Inventory
        ↓
Follow-Up Scan
        ↓
Baseline Comparison
        ↓
Unknown Host Detection
        ↓
Network-Level Investigation
        ↓
Physical Verification
        ↓
Authorization Decision
```

The baseline contained **5 active hosts**.

The follow-up scan also contained **5 active hosts**.

Therefore:

```text
New hosts detected: 0
```

No new device was detected during the testing window.

---

# ⚠️ Security Considerations

A network scan alone is not sufficient to determine whether a device is authorized.

A mature ICS/SCADA asset-monitoring process should correlate network observations with:

- Asset inventory
- CMDB records
- DHCP logs
- Switch MAC-address tables
- NAC systems
- Firewall logs
- Network segmentation records
- Physical inspections
- Change-management tickets
- System owners

This is particularly important in ICS/SCADA environments where unexpected devices can introduce operational and security risks.

---

# 📁 Evidence Directory

All evidence collected during the lab is stored under:

```text
scans/
```

### Evidence Files

```text
scans/
├── baseline-scan.txt
├── baseline-inventory.md
├── followup-scan.txt
├── baseline-comparison.md
├── neighbor-table.txt
├── interface-statistics.txt
└── task3-assessment.md
```

---

# 📋 Evidence Description

| Evidence File | Purpose |
|---|---|
| `baseline-scan.txt` | Original Nmap network-discovery results |
| `baseline-inventory.md` | Documented baseline device inventory |
| `followup-scan.txt` | Follow-up Nmap discovery results |
| `baseline-comparison.md` | Baseline vs follow-up analysis |
| `neighbor-table.txt` | Linux neighbor-table evidence |
| `interface-statistics.txt` | Network interface health evidence |
| `task3-assessment.md` | Task 3 inspection and environment limitations |

---

# 🔐 Evidence Integrity and Auditability

The lab evidence is stored as plain-text and Markdown files so that results can be reviewed, version-controlled, and included in a security portfolio.

Git can be used to maintain an audit trail:

```bash
git status
```

```bash
git add Lab-28-Detecting-Unauthorized-Devices/
```

```bash
git commit -m "Lab 28: Detect unauthorized devices"
```

If a remote repository is configured:

```bash
git push origin main
```

---

# 📈 Lessons Learned

This lab demonstrated several important security principles:

1. **Know your network.**  
   The correct subnet must be identified before scanning.

2. **Create a baseline.**  
   A known-good device inventory provides a reference for future comparisons.

3. **Monitor for changes.**  
   Follow-up scans can reveal newly appearing devices.

4. **Investigate unknown devices.**  
   A new IP or MAC address should be investigated rather than automatically classified as malicious.

5. **Correlate multiple sources.**  
   Nmap results should be compared with asset inventories and network-management records.

6. **Document limitations.**  
   Cloud-based labs cannot reproduce every physical ICS security control.

7. **Preserve evidence.**  
   Scan output and analysis should be retained for audit and troubleshooting.

---

# 🚀 Real-World ICS/SCADA Application

In a production ICS/SCADA environment, this workflow can support:

- Asset inventory management
- Rogue-device detection
- Network segmentation validation
- Continuous network monitoring
- Incident investigation
- Change-management verification
- OT security assessments

A production implementation would normally combine passive monitoring with approved active scanning procedures to avoid disrupting sensitive industrial equipment.

---

# ✅ Lab Completion Checklist

### Task 1 — Network Baseline

- [x] Nmap verified
- [x] Network interface identified
- [x] Correct subnet identified
- [x] Baseline Nmap scan performed
- [x] Five active hosts identified
- [x] Device inventory documented
- [x] Baseline evidence preserved

### Task 2 — Unknown Host Detection

- [x] Follow-up scan performed
- [x] Follow-up results preserved
- [x] Baseline compared with follow-up
- [x] New hosts identified
- [x] No new hosts detected during test window
- [x] Findings documented

### Task 3 — Physical and Network Inspection

- [x] Neighbor table inspected
- [x] Interface status checked
- [x] Interface statistics collected
- [x] Packet-analysis tool availability checked
- [x] Physical inspection limitation documented
- [x] Network-level assessment documented

### Documentation

- [x] Evidence files created
- [x] Evidence directory organized
- [x] README created
- [x] Lab results documented
- [x] Security assessment documented

---

# 🏁 Final Result

## LAB 28 — COMPLETE

**Baseline devices:** 5  
**Follow-up devices:** 5  
**New devices detected:** 0  
**Network interface:** `ens5`  
**Subnet:** `172.31.10.0/24`  
**Nmap:** `7.94SVN`

The lab successfully demonstrated a repeatable baseline-and-comparison approach for detecting unexpected network devices while clearly documenting the limitations of an AWS-based environment.

---

## 📂 Evidence Location

All supporting evidence is available in:

```text
Lab-28-Detecting-Unauthorized-Devices/scans/
```

