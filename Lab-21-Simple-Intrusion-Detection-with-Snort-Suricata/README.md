# Lab 21: Simple Intrusion Detection with Snort/Suricata

## Overview

This lab demonstrates the basic use of an open-source Intrusion Detection System (IDS) to monitor network traffic and detect Modbus TCP communication. **Suricata** was used to configure and test a simple detection rule.

## Objectives

* Understand the basic installation and configuration of Suricata.
* Create a custom rule to detect Modbus TCP traffic.
* Validate the Suricata configuration.
* Generate network traffic toward TCP port **502**.
* Verify that the IDS generates an alert.
* Understand the role of IDS tools in securing ICS/SCADA environments.

## Environment

* **Operating System:** Ubuntu Linux
* **IDS:** Suricata
* **Protocol:** Modbus TCP
* **Modbus TCP Port:** 502
* **Rule SID:** 1000001

## Task 1: Install Suricata

Update the package repository and install Suricata:

```bash
sudo apt update
sudo apt install suricata
```

Verify the installation:

```bash
suricata --build-info
```

## Task 2: Configure the Detection Rule

A custom rule was created to detect TCP traffic directed toward Modbus TCP port 502.

Example rule:

```text
alert tcp any any -> any 502 (msg:"Modbus Traffic Detected"; sid:1000001; rev:1;)
```

### Rule Explanation

| Component     | Meaning                                 |
| ------------- | --------------------------------------- |
| `alert`       | Generate an alert when the rule matches |
| `tcp`         | Monitor TCP traffic                     |
| `any any`     | Any source IP and source port           |
| `->`          | Traffic direction                       |
| `any 502`     | Any destination IP using port 502       |
| `msg`         | Alert message                           |
| `sid:1000001` | Unique rule identifier                  |
| `rev:1`       | Rule revision number                    |

The rule is designed to identify traffic associated with the standard **Modbus TCP port**.

## Task 3: Validate the Suricata Configuration

The configuration was tested using:

```bash
sudo suricata -T -c /etc/suricata/suricata.yaml
```

A successful configuration test confirms that Suricata can load its configuration and rules without errors.

## Task 4: Generate Test Traffic

Nmap was installed as a traffic-generation tool:

```bash
sudo apt install nmap
```

Test traffic was generated toward TCP port 502:

```bash
nmap -p 502 <target-ip>
```

This scan generates TCP traffic to the Modbus service port and can trigger the custom Suricata rule.

## Task 5: Verify the Alert

Suricata alerts can be checked using:

```bash
sudo cat /var/log/suricata/fast.log
```

The JSON event log can also be examined:

```bash
sudo cat /var/log/suricata/eve.json
```

The expected alert message is:

```text
Modbus Traffic Detected
```

with SID:

```text
1000001
```

## Lab Result

The Suricata configuration was successfully validated, test network traffic was generated toward TCP port **502**, and the custom detection rule successfully identified the traffic.

This confirms that the IDS was able to detect the specified network pattern.

## Security Relevance to ICS/SCADA

Modbus TCP is commonly encountered in industrial control environments. Monitoring Modbus traffic can help security teams identify unexpected communication with PLCs, RTUs, HMIs, and other ICS components.

A simple port-based rule is useful for learning, but production IDS rules should inspect Modbus protocol fields and expected device behavior to reduce false positives and provide more meaningful detection.

## Conclusion

In this lab, Suricata was installed and configured as a basic Intrusion Detection System. A custom rule was created to detect TCP traffic directed to Modbus port **502**. The configuration was validated, test traffic was generated, and the resulting alert was verified in the Suricata logs.

This lab demonstrates the fundamentals of network intrusion detection and its application to **ICS/SCADA security**.

## Evidence for Submission

Recommended screenshots/evidence:

1. Suricata installation completed successfully.
2. Custom `local.rules` containing the Modbus detection rule.
3. Successful output of the Suricata configuration test.
4. Nmap command generating traffic to port 502.
5. `fast.log` showing the **Modbus Traffic Detected** alert.
6. `eve.json` showing the corresponding Suricata event.

## Key Commands

```bash
sudo apt update
sudo apt install suricata nmap

sudo suricata -T -c /etc/suricata/suricata.yaml

nmap -p 502 <target-ip>

sudo cat /var/log/suricata/fast.log
sudo cat /var/log/suricata/eve.json
```
