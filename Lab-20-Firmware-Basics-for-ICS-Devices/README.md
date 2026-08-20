# Lab 20: Firmware Basics for ICS Devices

## Overview

This lab explores the role of firmware in Industrial Control Systems (ICS), with a focus on Programmable Logic Controllers (PLCs) and OpenPLC Runtime.

The lab demonstrates how to identify the runtime version of a simulated PLC, understand common firmware-related security risks, study the Stuxnet case, and document a secure firmware update procedure.

## Objectives

* Understand the role of firmware in ICS and PLC environments.
* Identify firmware/runtime version information.
* Understand common firmware security vulnerabilities.
* Study Stuxnet as an ICS cybersecurity case study.
* Understand the risks associated with outdated and vulnerable firmware.
* Document a controlled firmware update procedure.
* Apply security and change-management concepts to ICS environments.

## Lab Environment

| Component                    | Configuration             |
| ---------------------------- | ------------------------- |
| Platform                     | Ubuntu Linux              |
| ICS Simulator                | OpenPLC Runtime v4        |
| OpenPLC Runtime Version      | **v4.1.10**               |
| OpenPLC Management Interface | HTTPS                     |
| Management/API Port          | **9443**                  |
| Discovery API Port           | **9443**                  |
| Python Package Version       | 0.1.0                     |
| Service                      | `openplc-runtime.service` |
| Service Status               | Active (running)          |

> **Note:** `v4.1.10` is the OpenPLC Runtime version identified from the repository `VERSION` file. `0.1.0` is the Python package version and is not treated as the PLC runtime/firmware version.

## Task 1: Identify Current Firmware Version

### 1.1 Simulated PLC Environment

OpenPLC Runtime was configured as the simulated PLC environment.

The runtime service was verified with:

```bash
sudo systemctl status openplc-runtime --no-pager
```

The service reported:

```text
Active: active (running)
```

### 1.2 PLC Management Interface

The OpenPLC management/API interface was configured to use HTTPS on port `9443`.

The default port `8443` was already occupied by another service in the lab environment, so OpenPLC was configured to use `9443`.

Verification:

```bash
sudo ss -lntp | grep ':9443'
```

Expected result:

```text
LISTEN ... 0.0.0.0:9443 ... python3
```

The API endpoint was also reachable:

```bash
curl -k https://localhost:9443/api/ping
```

The server responded with:

```json
{"msg":"Missing Authorization Header"}
```

This confirmed that the OpenPLC HTTPS API was reachable and responding. The response indicates that authentication is required for the endpoint.

### 1.3 Runtime/Firmware Version

The runtime version was identified from the repository `VERSION` file:

```bash
cat VERSION
```

Result:

```text
v4.1.10
```

**Recorded OpenPLC Runtime/Firmware Version: `v4.1.10`**

The OpenPLC runtime source also documents that the `VERSION` file is used as a version source for local installations.

## Task 2: Firmware Vulnerability Research

Firmware and software in ICS environments can introduce security risks when vulnerabilities remain unpatched or when changes are deployed without appropriate testing.

Common firmware-related security risks include:

### 1. Outdated Firmware

Older firmware may contain publicly known vulnerabilities that can be exploited by attackers.

### 2. Buffer Overflow Vulnerabilities

Improper handling of input can cause memory corruption, crashes, or potentially unauthorized code execution.

### 3. Weak Authentication

Default, weak, or hard-coded credentials can allow unauthorized users to access PLC management functions.

### 4. Insecure Firmware Updates

Firmware update mechanisms should prevent unauthorized modification and should verify that firmware is legitimate and appropriate for the device.

### 5. Unsupported Firmware

Older devices may no longer receive security updates from the manufacturer, increasing long-term security risk.

### 6. Insufficient Change Testing

Firmware changes can affect control processes and device behavior. ICS changes therefore require testing and validation before deployment.

NIST guidance emphasizes that ICS/OT environments have unique performance, reliability, and safety requirements. Firmware and software changes should therefore be managed carefully and tested before being introduced into operational environments.

## Task 2.2: Stuxnet Case Study

Stuxnet is an important historical example of malware targeting industrial control environments.

The CISA Primary Stuxnet Advisory documents that Stuxnet used multiple zero-day vulnerabilities and could propagate through mechanisms including infected USB devices, network shares, STEP 7 project files, and WinCC-related files.

The major ICS security lesson is that industrial environments require defense-in-depth protection. An attacker does not necessarily need to attack a PLC directly; compromise of connected engineering workstations, removable media, software, or control-system components can provide a path toward the industrial process.

### Security Lessons from Stuxnet

* Keep systems patched where operationally safe and supported.
* Control removable media such as USB devices.
* Restrict unnecessary network connectivity.
* Apply strong authentication and access controls.
* Monitor engineering workstations and control-system components.
* Validate software and firmware changes.
* Maintain backups and recovery procedures.
* Use defense-in-depth security controls.

## Task 3: Firmware Update Procedure

The firmware update procedure in this lab is theoretical. No physical PLC firmware was flashed or replaced.

### Step 1 — Identify the Device

Record:

* PLC manufacturer
* PLC model
* Current firmware version
* Current configuration
* Installed communication modules

### Step 2 — Verify Compatibility

Check the manufacturer's official documentation and confirm that the proposed firmware version is compatible with:

* PLC hardware
* CPU/model
* Installed modules
* Engineering software
* Existing control application
* Communication protocols

### Step 3 — Obtain Firmware

Download firmware only from the manufacturer's official support portal or another approved source.

Verify the firmware file's integrity and authenticity where the manufacturer provides appropriate verification mechanisms.

### Step 4 — Back Up Configuration

Before updating:

* Back up the PLC configuration.
* Back up the control program.
* Record existing settings.
* Document the current firmware version.
* Confirm that recovery procedures are available.

### Step 5 — Plan the Maintenance Window

Firmware updates should be performed during an approved maintenance window.

ICS updates may require additional testing, validation, and planned outages because changes can affect operational processes.

### Step 6 — Perform the Update

Using the manufacturer's approved procedure:

1. Connect to the PLC management interface.
2. Upload the compatible firmware.
3. Verify the selected firmware.
4. Start the update.
5. Wait for the update to complete.
6. Restart the PLC if required.

### Step 7 — Verify

After the update:

* Confirm the new firmware version.
* Verify PLC communication.
* Verify control application functionality.
* Check alarms and diagnostics.
* Confirm that required services are operating correctly.

### Step 8 — Document

Record:

* Previous firmware version
* New firmware version
* Date of update
* Device/model
* Firmware source
* Backup status
* Verification results
* Any problems encountered

## Lab Findings

The OpenPLC Runtime environment was successfully configured and verified.

Key findings:

```text
OpenPLC Runtime Version: v4.1.10
Management/API Protocol: HTTPS
Management/API Port: 9443
OpenPLC Service: Active (running)
API Connectivity: Confirmed
Authentication: Required
```

The OpenPLC runtime logs also showed that no PLC application library was currently loaded:

```text
No libplc_*.so file found in ./build
PLC State: EMPTY
```

This was treated as a runtime/application-state observation rather than a failure of the firmware-management objectives of this lab, because the provided lab tasks focus on firmware identification, vulnerability research, and theoretical firmware-update procedures.

## Security Best Practices

For production ICS/OT environments:

* Use vendor-supported firmware versions.
* Maintain an accurate firmware inventory.
* Apply security patches through controlled change management.
* Test firmware updates before production deployment.
* Schedule updates during approved maintenance windows.
* Maintain tested backups and recovery procedures.
* Restrict administrative access.
* Protect engineering workstations.
* Monitor changes to PLCs and other control devices.
* Use defense-in-depth network segmentation.
* Document all firmware changes for auditability.

## Conclusion

This lab provided practical exposure to firmware management concepts in an ICS environment using OpenPLC.

The simulated PLC runtime was configured and its runtime version was identified as **v4.1.10**. The lab also examined common firmware security risks, the Stuxnet ICS case study, and a controlled theoretical firmware-update process.

The exercise demonstrated that firmware management is not simply about installing the newest version. In ICS environments, firmware changes must be carefully planned, tested, validated, documented, and performed with consideration for system availability, reliability, safety, and security.

## Skills Demonstrated

* ICS/SCADA security fundamentals
* PLC/OpenPLC runtime administration
* Firmware version identification
* Linux system administration
* Systemd service management
* HTTPS/API verification
* ICS vulnerability analysis
* Stuxnet case-study analysis
* Firmware security concepts
* Change-management concepts
* OT/ICS security best practices
* Technical documentation

## References

* NIST SP 800-82 Rev. 3 — Guide to Operational Technology (OT) Security
* CISA ICS Advisory ICSA-10-272-01 — Primary Stuxnet Advisory
* OpenPLC Runtime project documentation
