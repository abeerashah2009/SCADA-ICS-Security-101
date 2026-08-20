# Lab 20 Lab Notes: Firmware Basics for ICS Devices

## Date

20 August 2026

## Environment

```text
OS: Ubuntu Linux
ICS Platform: OpenPLC Runtime v4
OpenPLC Runtime Version: v4.1.10
Management/API: HTTPS
Management/API Port: 9443
Service: openplc-runtime.service
```

---

# Task 1 — Identify Current Firmware Version

## Step 1.1 — Verify OpenPLC Runtime

Command:

```bash
sudo systemctl status openplc-runtime --no-pager
```

Result:

```text
Active: active (running)
```

The OpenPLC Runtime service is running successfully.

## Step 1.2 — Verify Management Interface

The original port `8443` was already being used by another service (`dcvserver`) in the lab environment.

OpenPLC was therefore configured to use HTTPS port `9443`.

Configuration verification:

```bash
grep -n "port=" webserver/app.py | tail
grep -n "API_PORT" webserver/discovery/network_discovery.py
```

Result:

```text
415:            port=9443,
35:API_PORT: int = 9443
```

Port verification:

```bash
sudo ss -lntp | grep ':9443'
```

Result confirmed that Python/OpenPLC was listening on:

```text
0.0.0.0:9443
```

API connectivity test:

```bash
curl -k https://localhost:9443/api/ping
```

Response:

```json
{"msg":"Missing Authorization Header"}
```

This confirms that the API endpoint is reachable and responding. Authentication is required for the endpoint.

## Step 1.3 — Identify Runtime/Firmware Version

Command:

```bash
cat VERSION
```

Result:

```text
v4.1.10
```

### Recorded Version

**OpenPLC Runtime/Firmware Version: v4.1.10**

Additional information:

```text
Minimum Editor Version: 4.1.0
Python Package Version: 0.1.0
```

The Python package version `0.1.0` is not used as the OpenPLC runtime/firmware version.

---

# Task 2 — Firmware Vulnerability Research

## Common Firmware Security Risks

### Outdated Firmware

Old firmware can contain known vulnerabilities that attackers may exploit.

### Buffer Overflows

Improper input handling can cause memory corruption and may result in crashes or unauthorized code execution.

### Weak Authentication

Default or weak credentials can expose PLC management interfaces to unauthorized users.

### Insecure Firmware Updates

An update mechanism without adequate authentication or integrity protection may allow unauthorized firmware to be installed.

### Unsupported Firmware

End-of-life devices may no longer receive security patches.

### Inadequate Testing

Untested firmware changes can affect PLC operation and industrial processes.

## Security Controls

Recommended controls include:

* Maintain a firmware inventory.
* Track vendor security advisories.
* Use supported firmware versions.
* Test updates before production deployment.
* Back up configurations.
* Restrict administrative access.
* Use secure update mechanisms.
* Maintain recovery procedures.
* Document all changes.

---

# Task 2.2 — Stuxnet Case Study

Stuxnet is a major historical ICS cybersecurity case.

According to the CISA Primary Stuxnet Advisory, Stuxnet used multiple zero-day exploits and could spread through infected USB devices, network shares, STEP 7 project files, and WinCC-related files.

## Lessons Learned

1. Industrial systems can be affected through connected IT systems.
2. Removable media can introduce malware into isolated environments.
3. Engineering workstations are important security boundaries.
4. ICS environments require defense-in-depth security.
5. Software and firmware changes should be controlled and validated.
6. Access to control-system components should be restricted.

---

# Task 3 — Firmware Update Procedure

The firmware update portion of this lab is theoretical.

## Procedure

### 1. Identify the PLC

Record the:

* Manufacturer
* Model
* Current firmware
* Hardware configuration

### 2. Verify Compatibility

Check the manufacturer's documentation and confirm compatibility between the new firmware and the PLC hardware/software environment.

### 3. Obtain Firmware

Download firmware from the official vendor support portal.

Verify integrity/authenticity where supported.

### 4. Back Up

Before updating:

* Back up the PLC program.
* Back up configuration.
* Record current settings.
* Record current firmware version.
* Verify recovery procedures.

### 5. Plan Maintenance

Schedule the update during an approved maintenance window.

### 6. Perform Update

Follow the vendor's approved firmware-update procedure.

### 7. Verify

After the update:

* Confirm firmware version.
* Verify communication.
* Verify PLC operation.
* Check diagnostics and alarms.
* Confirm application functionality.

### 8. Document

Record:

```text
Device:
Previous Firmware:
New Firmware:
Update Date:
Firmware Source:
Backup Completed:
Verification Result:
Issues:
```

---

# Lab Verification Summary

| Check                                | Result                           |
| ------------------------------------ | -------------------------------- |
| OpenPLC installed                    | PASS                             |
| Runtime service active               | PASS                             |
| HTTPS management interface           | PASS                             |
| Port 9443 listening                  | PASS                             |
| API reachable                        | PASS                             |
| Runtime version identified           | PASS                             |
| Runtime version                      | v4.1.10                          |
| Firmware vulnerabilities researched  | PASS                             |
| Stuxnet case study                   | PASS                             |
| Firmware update procedure documented | PASS                             |
| Actual firmware update               | NOT PERFORMED — theoretical task |

---

# Runtime Observation

The runtime logs contained:

```text
No libplc_*.so file found in ./build
PLC State: EMPTY
State transition to RUNNING failed
```

This indicates that a PLC application/library is not currently loaded into the runtime.

This was documented as an environment observation and was not treated as a failure of the firmware-management objectives because the supplied Lab 20 instructions do not require creation or deployment of a PLC control program.

---

# Key Learning

This lab demonstrated that firmware management is an important part of ICS security.

Firmware updates must be treated as controlled operational changes rather than ordinary software updates. ICS environments require compatibility checking, backups, testing, maintenance planning, verification, and documentation before changes are introduced into production.

## Skills Demonstrated

* OpenPLC administration
* Linux/systemd administration
* Firmware version identification
* HTTPS/API testing
* ICS firmware security
* Vulnerability research
* Stuxnet analysis
* Firmware update planning
* Change management
* OT/ICS security documentation
