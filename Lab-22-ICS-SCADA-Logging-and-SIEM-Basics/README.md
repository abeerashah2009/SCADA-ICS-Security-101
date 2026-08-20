# Lab 22: ICS/SCADA Logging and SIEM Basics

## Overview

This lab demonstrates the fundamentals of logging and security monitoring in Industrial Control Systems (ICS) and Supervisory Control and Data Acquisition (SCADA) environments.

The lab uses **rsyslog** to demonstrate centralized log collection and Linux command-line tools such as `grep` to identify suspicious activity in simulated PLC and HMI logs.

## Objectives

* Understand important log sources in ICS/SCADA environments.
* Identify PLC and HMI logging information.
* Configure rsyslog for centralized log collection.
* Generate and collect ICS security events.
* Analyze logs for suspicious behavior.
* Understand the basic role of SIEM systems in ICS security monitoring.

## Environment

* **Operating System:** Ubuntu Linux
* **Logging Service:** rsyslog
* **Simulated ICS Devices:** PLC01 and HMI01
* **Central Log:** `/var/log/ics-central.log`

## Task 1: Identify Key ICS/SCADA Log Sources

### PLC Logs

PLC logs can contain:

* Operating status
* Input/output state changes
* Runtime errors
* Communication errors
* User access events
* Configuration changes

Example:

```text
2026-08-20 15:00:01 [PLC01] Status: RUN
2026-08-20 15:03:10 [PLC01] Error: Communication timeout
2026-08-20 15:04:30 [PLC01] User: Admin Access: Granted SourceIP: 192.168.1.10
```

### HMI Logs

HMI logs can contain:

* Operator logins
* Failed login attempts
* Alarm acknowledgements
* System status changes
* User interactions
* Configuration events

Example:

```text
2026-08-20 15:10:01 [HMI01] User: Operator Login: Success SourceIP: 192.168.1.60
2026-08-20 15:11:20 [HMI01] Alarm: High Temperature Acknowledged
2026-08-20 15:14:33 [HMI01] User: Unknown Login: Failed SourceIP: 10.10.10.55
```

## Task 2: Install and Verify rsyslog

The rsyslog package was installed using:

```bash
sudo apt update
sudo apt install -y rsyslog
```

The service was verified successfully:

```bash
sudo systemctl status rsyslog --no-pager
```

The service status showed:

```text
Active: active (running)
```

The rsyslog service was therefore operating correctly.

## Task 3: Configure Centralized ICS Logging

A dedicated rsyslog configuration was created:

```text
if ($programname == "ics-lab") then {
    action(type="omfile" file="/var/log/ics-central.log")
    stop
}
```

Configuration validation was performed using:

```bash
sudo rsyslogd -N1
```

The configuration validation completed successfully.

The rsyslog service was restarted:

```bash
sudo systemctl restart rsyslog
```

## Task 4: Generate and Collect ICS Events

A test ICS event was generated using:

```bash
logger -t ics-lab "LAB-22 CENTRAL TEST: PLC01 Access Denied SourceIP=10.10.10.55"
```

The centralized log was then checked:

```bash
sudo cat /var/log/ics-central.log
```

The event was successfully recorded:

```text
2026-08-20T11:10:37.773800+00:00 ip-172-31-10-253 ics-lab: LAB-22 CENTRAL TEST: PLC01 Access Denied SourceIP=10.10.10.55
```

This confirms that rsyslog successfully collected the ICS test event into the centralized log.

## Task 5: Analyze Suspicious Activity

### PLC Analysis

The following command was used:

```bash
grep "Access: Denied" plc_logs.txt
```

Three denied access attempts were identified:

```text
2026-08-20 15:05:42 [PLC01] User: Unknown Access: Denied SourceIP: 10.10.10.55
2026-08-20 15:05:44 [PLC01] User: Unknown Access: Denied SourceIP: 10.10.10.55
2026-08-20 15:05:46 [PLC01] User: Unknown Access: Denied SourceIP: 10.10.10.55
```

### HMI Analysis

The following command was used:

```bash
grep "Login: Failed" hmi_logs.txt
```

Two failed HMI login attempts were identified:

```text
2026-08-20 15:14:33 [HMI01] User: Unknown Login: Failed SourceIP: 10.10.10.55
2026-08-20 15:14:35 [HMI01] User: Unknown Login: Failed SourceIP: 10.10.10.55
```

### Security Finding

The same source IP, `10.10.10.55`, appeared in both PLC denied-access events and HMI failed-login events.

Repeated authentication failures from the same unknown source may indicate unauthorized access attempts or password-guessing activity and should be investigated in a real ICS environment.

## SIEM Concept

A SIEM can collect logs from multiple sources, including:

* PLCs
* HMIs
* Servers
* Firewalls
* Network devices
* Security tools

The SIEM can then centralize, correlate, search, and analyze these events to generate security alerts.

Examples of open-source security monitoring platforms include OSSEC and the ELK Stack.

In this lab, rsyslog and command-line analysis were used to demonstrate the basic concepts without deploying a complete SIEM platform.

## Files Included

| File                      | Purpose                           |
| ------------------------- | --------------------------------- |
| `log-sources.txt`         | Documents PLC and HMI log sources |
| `plc_logs.txt`            | Simulated PLC log entries         |
| `hmi_logs.txt`            | Simulated HMI log entries         |
| `suspicious-activity.txt` | Analysis of suspicious events     |
| `ics-central.log`         | Centralized rsyslog evidence      |
| `README.md`               | Lab documentation                 |

## Key Commands

```bash
sudo apt update
sudo apt install -y rsyslog

sudo systemctl status rsyslog --no-pager

sudo rsyslogd -N1

sudo systemctl restart rsyslog

grep "Access: Denied" plc_logs.txt

grep "Login: Failed" hmi_logs.txt

logger -t ics-lab "LAB-22 CENTRAL TEST: PLC01 Access Denied SourceIP=10.10.10.55"

sudo cat /var/log/ics-central.log
```

## Results

The lab successfully demonstrated:

1. Identification of PLC and HMI log sources.
2. Creation and analysis of simulated ICS logs.
3. Detection of repeated denied access and failed login attempts.
4. Installation and verification of rsyslog.
5. Configuration of a centralized ICS logging destination.
6. Successful forwarding of an ICS security event.
7. Basic log analysis using Linux command-line tools.

## Conclusion

This lab demonstrated the importance of centralized logging and log analysis in ICS/SCADA environments. PLC and HMI logs can provide valuable information about system status, user activity, errors, and potential security incidents.

Rsyslog was successfully configured to collect ICS events into a centralized log file. Suspicious activity was identified using `grep`, demonstrating the basic principles used by SIEM systems for security monitoring and incident detection.

In a production ICS environment, centralized logging and SIEM integration can improve visibility, event correlation, detection, and incident response.
