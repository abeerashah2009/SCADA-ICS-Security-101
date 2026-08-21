# Lab 33: ICS/SCADA Logging with Syslog

## Overview

This laboratory demonstrates the fundamentals of centralized logging for Industrial Control Systems (ICS) and Supervisory Control and Data Acquisition (SCADA) environments using **rsyslog** on Ubuntu Linux.

The lab establishes a Syslog logging service, configures rsyslog to receive Syslog messages over UDP and TCP port 514, generates controlled ICS/SCADA log events, verifies that the events are stored successfully, and preserves evidence of the logging configuration and received messages.

The laboratory also validates the integrity of the collected log evidence using a SHA-256 hash.

> **Environment Limitation:**
>
> This laboratory was performed in an AWS EC2 Ubuntu environment.
>
> No physical PLC, RTU, HMI, SCADA server, or industrial control system was available.
>
> Therefore, a controlled ICS/SCADA log generator was used to simulate industrial events.
>
> No production ICS system or real industrial process was modified during this exercise.

---

# Objectives

The objectives of this laboratory were to:

* Understand Syslog fundamentals in ICS/SCADA environments.
* Install and configure the rsyslog service.
* Configure rsyslog to receive remote Syslog messages.
* Enable UDP Syslog reception on port 514.
* Enable TCP Syslog reception on port 514.
* Create a controlled ICS/SCADA log generator.
* Generate simulated PLC, HMI, and SCADA events.
* Store ICS/SCADA events in a dedicated log file.
* Validate Syslog message reception.
* Verify the rsyslog service status.
* Validate the rsyslog configuration.
* Preserve logging evidence.
* Generate a SHA-256 integrity hash for the collected log evidence.
* Document the security relevance of centralized ICS logging.

---

# Environment

| Item                | Value                    |
| ------------------- | ------------------------ |
| Environment         | AWS EC2                  |
| Operating System    | Ubuntu Linux             |
| Architecture        | x86_64                   |
| Logging Service     | rsyslog                  |
| Syslog Protocol     | Syslog                   |
| UDP Port            | 514                      |
| TCP Port            | 514                      |
| ICS Log File        | `/var/log/ics-scada.log` |
| Log Generator       | `ics-log-generator.sh`   |
| Evidence Format     | TXT                      |
| Integrity Algorithm | SHA-256                  |

---

# Lab Architecture

The laboratory implemented the following simplified logging architecture:

```text
+---------------------------+
|   ICS/SCADA Log Generator |
|                           |
|   PLC-01                  |
|   HMI-01                  |
|   SCADA-01                |
+-------------+-------------+
              |
              | Syslog
              | UDP/TCP 514
              v
+---------------------------+
|        rsyslog             |
|     Syslog Server          |
|                           |
| Ubuntu EC2 Instance       |
+-------------+-------------+
              |
              v
+---------------------------+
| /var/log/ics-scada.log    |
|                           |
| Centralized ICS Events    |
+-------------+-------------+
              |
              v
+---------------------------+
| Evidence Collection       |
|                           |
| syslog-reception.txt      |
| log-integrity.txt         |
+---------------------------+
```

---

# Task 1 — Install and Configure Syslog Server

## 1.1 Install rsyslog

The rsyslog package was installed on the Ubuntu system.

The logging service provides the central Syslog functionality required for this laboratory.

The service was verified after configuration.

---

## 1.2 Configure Remote Syslog Reception

A dedicated rsyslog configuration file was created:

```text
logging/rsyslog-config.conf
```

The configuration was installed as:

```text
/etc/rsyslog.d/30-ics-scada.conf
```

The configuration enables Syslog reception over both UDP and TCP.

The relevant configuration includes:

```text
module(load="imudp")
input(type="imudp" port="514")

module(load="imtcp")
input(type="imtcp" port="514")
```

The configuration also directs ICS/SCADA test events to:

```text
/var/log/ics-scada.log
```

---

## 1.3 Validate rsyslog Configuration

The rsyslog configuration was tested using:

```bash
sudo rsyslogd -N1
```

The validation completed successfully:

```text
rsyslogd: End of config validation run. Bye.
```

This confirmed that the rsyslog configuration was syntactically valid.

---

## 1.4 Restart rsyslog

The service was restarted to apply the configuration:

```bash
sudo systemctl restart rsyslog
```

The service was subsequently verified as active and running.

---

# Task 2 — Verify Syslog Network Listening

The system was checked to confirm that rsyslog was listening on port 514.

Command used:

```bash
sudo ss -lntup | grep ':514'
```

The verification showed listeners for:

```text
UDP 0.0.0.0:514
UDP [::]:514
TCP 0.0.0.0:514
TCP [::]:514
```

This confirms that the Syslog server was configured to accept both UDP and TCP messages on the standard Syslog port.

---

# Task 3 — Create ICS/SCADA Log Generator

Because the AWS environment did not contain physical ICS equipment, a controlled log generator was used to simulate industrial events.

The generator was created at:

```text
logging/ics-log-generator.sh
```

The script was made executable using:

```bash
chmod +x logging/ics-log-generator.sh
```

The generator was executed using:

```bash
./logging/ics-log-generator.sh
```

The script successfully reported:

```text
ICS/SCADA test events generated.
```

---

# Simulated ICS/SCADA Events

The controlled generator produced events representing different industrial components.

Examples included:

```text
PLC-01: Process started
PLC-01: Temperature=72C
PLC-01: Pressure=4.2bar
HMI-01: Operator login successful
SCADA-01: Communication with PLC-01 established
PLC-01: Digital input changed
SCADA-01: Process monitoring active
```

These messages represent typical categories of events that may be relevant when monitoring an ICS environment.

---

# Task 4 — Store ICS/SCADA Logs

The generated events were successfully stored in:

```text
/var/log/ics-scada.log
```

The log file was inspected using:

```bash
sudo tail -20 /var/log/ics-scada.log
```

Example received events included:

```text
2026-08-21T04:17:02.685406+00:00 ip-172-31-10-161 ics-simulator: PLC-01: Process started
2026-08-21T04:17:02.690506+00:00 ip-172-31-10-161 ics-simulator: PLC-01: Temperature=72C
2026-08-21T04:17:02.695197+00:00 ip-172-31-10-161 ics-simulator: PLC-01: Pressure=4.2bar
2026-08-21T04:17:02.698968+00:00 ip-172-31-10-161 ics-simulator: HMI-01: Operator login successful
2026-08-21T04:17:02.702981+00:00 ip-172-31-10-161 ics-simulator: SCADA-01: Communication with PLC-01 established
2026-08-21T04:17:02.706823+00:00 ip-172-31-10-161 ics-simulator: PLC-01: Digital input changed
2026-08-21T04:17:02.710330+00:00 ip-172-31-10-161 ics-simulator: SCADA-01: Process monitoring active
```

This confirmed successful collection of the simulated ICS/SCADA events.

---

# Task 5 — Validate Remote Syslog Reception

A remote-style Syslog message was generated using the Linux `logger` utility.

The test command was:

```bash
logger --server 127.0.0.1 --port 514 --udp -t ics-remote-test "PLC-02: Remote Syslog test message"
```

After allowing the logging service time to process the message, the log file was checked.

The following message was successfully received:

```text
2026-08-21T04:19:30.974560+00:00 ip-172-31-10-161 ics-remote-test PLC-02: Remote Syslog test message
```

This is an important verification because it demonstrates that a Syslog message sent to UDP port 514 was processed by rsyslog and written to the dedicated ICS/SCADA log file.

Therefore, the laboratory successfully demonstrated the following flow:

```text
Syslog Message
      |
      v
UDP Port 514
      |
      v
rsyslog
      |
      v
/var/log/ics-scada.log
```

---

# Task 6 — Verify rsyslog Service

The rsyslog service status was collected using:

```bash
sudo systemctl status rsyslog --no-pager
```

The service was confirmed to be:

```text
Active: active (running)
```

The service was running successfully during the laboratory verification.

Evidence was saved to:

```text
evidence/rsyslog-status.txt
```

---

# Task 7 — Preserve Syslog Evidence

The received ICS/SCADA log entries were copied into an evidence file:

```bash
sudo tail -20 /var/log/ics-scada.log > evidence/syslog-reception.txt
```

The resulting evidence file contains the simulated ICS events and the verified remote Syslog test message.

Evidence file:

```text
evidence/syslog-reception.txt
```

---

# Task 8 — Verify Log Integrity

A SHA-256 hash was generated for the collected Syslog evidence:

```bash
sha256sum evidence/syslog-reception.txt > evidence/log-integrity.txt
```

The recorded SHA-256 value was:

```text
b5d9e8e120e82634796c8be472ee050d8470e26bdaeb9b9c8fe27e1396e9511d
```

The hash provides a way to detect later modification of the evidence file.

If the file is modified, calculating its SHA-256 hash again will produce a different value.

---

# Evidence Collected

## 1. rsyslog Status

File:

```text
evidence/rsyslog-status.txt
```

Purpose:

Records the rsyslog service status and demonstrates that the logging service was active and running.

---

## 2. Syslog Reception Evidence

File:

```text
evidence/syslog-reception.txt
```

Purpose:

Contains the collected ICS/SCADA Syslog messages received and stored by rsyslog.

---

## 3. Log Integrity Evidence

File:

```text
evidence/log-integrity.txt
```

Purpose:

Contains the SHA-256 hash of the collected Syslog evidence.

This provides basic evidence-integrity verification.

---

# Laboratory Files

The completed laboratory contains:

```text
Lab-33-ICS-SCADA-Logging-with-Syslog/
├── README.md
├── evidence/
│   ├── log-integrity.txt
│   ├── rsyslog-status.txt
│   └── syslog-reception.txt
└── logging/
    ├── ics-log-generator.sh
    └── rsyslog-config.conf
```

---

# Security Findings

| Security Check                       | Result |
| ------------------------------------ | ------ |
| rsyslog installed                    | PASS   |
| rsyslog configuration created        | PASS   |
| rsyslog configuration validated      | PASS   |
| rsyslog service restarted            | PASS   |
| UDP 514 listening                    | PASS   |
| TCP 514 listening                    | PASS   |
| ICS/SCADA log generator created      | PASS   |
| ICS/SCADA events generated           | PASS   |
| ICS/SCADA logs stored                | PASS   |
| Remote Syslog message generated      | PASS   |
| Remote Syslog message received       | PASS   |
| Syslog evidence collected            | PASS   |
| SHA-256 integrity hash created       | PASS   |
| AWS laboratory limitation documented | PASS   |

---

# ICS/SCADA Security Relevance

Logging is an important security capability in ICS/SCADA environments.

Industrial systems can generate security-relevant events such as:

* Operator authentication
* Configuration changes
* PLC communication events
* Process alarms
* Network communication failures
* Unauthorized access attempts
* System errors
* Engineering workstation activity
* Remote-access activity
* Changes to industrial devices

Centralized logging can help security and operations teams identify unusual behavior and investigate incidents.

---

# Importance of Centralized Logging

Without centralized logging, important security events may remain distributed across multiple devices.

Centralized logging can provide:

* Improved visibility
* Easier investigation
* Security-event correlation
* Better incident response
* Longer-term event retention
* Audit support
* Troubleshooting capabilities
* Detection of abnormal activity

For ICS environments, centralized logging should be designed carefully so that monitoring does not negatively affect industrial operations.

---

# Logging Considerations for ICS

ICS logging requires additional considerations compared with ordinary IT environments.

## Availability

Logging infrastructure should not become a single point of failure for critical operations.

---

## Performance

Logging should not introduce unacceptable resource consumption or network delays.

---

## Network Segmentation

ICS logging traffic should be appropriately controlled between network zones.

For example:

```text
Enterprise Network
        |
    Firewall
        |
Industrial DMZ
        |
    Firewall
        |
Control Network
        |
    ICS Devices
        |
        v
Central Logging System
```

---

## Time Synchronization

Accurate timestamps are important for investigating incidents.

ICS systems should use appropriate time-synchronization mechanisms so that events from multiple systems can be correlated reliably.

---

## Log Protection

Security logs should be protected from:

* Unauthorized modification
* Unauthorized deletion
* Unauthorized access
* Accidental loss

Where appropriate, logs should be forwarded to a centralized and protected logging infrastructure.

---

# Incident Response Relevance

Syslog data can provide useful evidence during an ICS security investigation.

For example, investigators may examine:

```text
Authentication events
        |
        v
Configuration changes
        |
        v
Network communication
        |
        v
Process anomalies
        |
        v
Security alerts
```

Correlating these events can help establish a timeline of suspicious activity.

---

# Example Security Investigation

A hypothetical investigation could identify the following sequence:

```text
09:10  Remote user authenticated
09:12  Engineering workstation accessed
09:15  PLC configuration changed
09:16  SCADA communication interrupted
09:18  Process alarm generated
09:20  Remote session terminated
```

Centralized logs can help investigators correlate these events and determine whether the activity was authorized.

---

# Production ICS Recommendations

A production ICS environment should consider the following logging practices:

1. Identify critical systems that require logging.
2. Define security-relevant events.
3. Centralize logs where appropriate.
4. Protect the logging infrastructure.
5. Synchronize system clocks.
6. Restrict access to logs.
7. Monitor authentication events.
8. Monitor configuration changes.
9. Monitor remote-access activity.
10. Monitor industrial network events.
11. Establish appropriate log-retention periods.
12. Protect logs from unauthorized modification.
13. Test log collection regularly.
14. Integrate important events with security monitoring systems.
15. Include logging requirements in incident-response procedures.

---

# AWS Laboratory Limitation

This laboratory was performed in an AWS EC2 environment rather than a physical industrial control environment.

The laboratory did not contain:

* Physical PLCs
* Physical RTUs
* Industrial HMIs
* Physical SCADA servers
* Industrial control cabinets
* Industrial sensors
* Industrial actuators
* Real industrial network equipment
* Real industrial processes

Therefore, the following components were simulated:

```text
PLC events
HMI events
SCADA events
Industrial process events
```

The laboratory demonstrates the **logging architecture and security concepts**, not production-grade industrial hardware integration.

No real industrial process was controlled or modified.

---

# What Was Successfully Demonstrated

This laboratory successfully demonstrated:

* Syslog fundamentals
* rsyslog installation
* rsyslog configuration
* UDP Syslog reception
* TCP Syslog reception
* Syslog port verification
* ICS/SCADA event generation
* Centralized ICS/SCADA log storage
* Remote-style Syslog transmission
* Remote Syslog reception
* Logging evidence collection
* SHA-256 evidence integrity verification
* Basic ICS security monitoring concepts
* Incident-response logging concepts
* Security documentation
* Evidence organization

---

# Lab Status

* [x] rsyslog installed
* [x] rsyslog configured
* [x] rsyslog configuration validated
* [x] rsyslog service restarted
* [x] UDP port 514 verified
* [x] TCP port 514 verified
* [x] ICS/SCADA log generator created
* [x] ICS/SCADA events generated
* [x] ICS/SCADA events stored
* [x] Remote Syslog message generated
* [x] Remote Syslog message received
* [x] Syslog evidence collected
* [x] SHA-256 integrity hash created
* [x] Evidence organized
* [x] AWS limitations documented
* [x] README completed

**LAB 33 — COMPLETE**

---

# Skills Demonstrated

This laboratory demonstrated practical skills in:

* ICS/SCADA cybersecurity
* Linux system administration
* Syslog
* rsyslog
* Linux logging
* Network-based logging
* UDP/TCP services
* Port verification
* Security monitoring
* Log collection
* Log analysis
* Evidence preservation
* SHA-256 integrity verification
* Incident-response preparation
* ICS security documentation
* Security operations fundamentals

---

# Conclusion

This laboratory demonstrated a basic centralized logging architecture for an ICS/SCADA environment using rsyslog on Ubuntu Linux.

The rsyslog service was successfully configured to receive Syslog messages over UDP and TCP port 514.

A controlled ICS/SCADA log generator produced simulated PLC, HMI, and SCADA events, which were successfully stored in:

```text
/var/log/ics-scada.log
```

A remote-style Syslog message was also successfully transmitted using UDP port 514 and received by rsyslog.

The received logging evidence was preserved in:

```text
evidence/syslog-reception.txt
```

A SHA-256 hash was generated to provide basic integrity verification of the collected evidence.

The laboratory therefore successfully demonstrated the fundamental workflow of:

```text
ICS/SCADA Events
       |
       v
    Syslog
       |
       v
    rsyslog
       |
       v
Centralized Log Storage
       |
       v
Security Evidence
       |
       v
Integrity Verification
```

In a production ICS environment, centralized logging should be combined with appropriate network segmentation, secure time synchronization, access control, log protection, monitoring, incident response, and change-management procedures.

No real industrial control equipment or production ICS process was modified during this laboratory.

---

# Final Assessment

**Lab 33 successfully demonstrated ICS/SCADA logging using Syslog and rsyslog in a controlled AWS Ubuntu environment.**

The laboratory successfully verified Syslog configuration, network reception, ICS/SCADA event collection, evidence preservation, and SHA-256 integrity verification.

**LAB 33 — SUCCESSFULLY COMPLETED**
