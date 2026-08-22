# Lab 36: Endpoint Security for ICS Workstations

## Overview

This lab demonstrates basic endpoint security controls for an ICS workstation using open-source Linux security tools.

The exercise focuses on three important endpoint-security areas:

1. **Antivirus / malware protection** using ClamAV.
2. **USB storage restriction** using Linux `modprobe` configuration.
3. **Software inventory** using `dpkg-query`.

The laboratory environment is an Ubuntu 24.04.3 LTS AWS EC2 system. The environment is a controlled simulation and does not represent a production ICS workstation.

---

## Objectives

* Understand basic endpoint security requirements for ICS workstations.
* Install and configure ClamAV antivirus protection.
* Update and verify the ClamAV malware database.
* Perform a malware scan and document the results.
* Restrict USB storage access using Linux kernel module configuration.
* Preserve the original USB configuration before making changes.
* Update the initramfs after applying the USB restriction.
* Create a software inventory of installed packages.
* Collect security evidence for auditing and future investigation.
* Understand limitations when applying endpoint controls to operational ICS systems.

---

## Environment

| Component        | Details               |
| ---------------- | --------------------- |
| Platform         | AWS EC2               |
| Operating System | Ubuntu 24.04.3 LTS    |
| Architecture     | amd64                 |
| Kernel           | Linux 6.14.0-1018-aws |
| Antivirus        | ClamAV 1.5.3          |
| Package Manager  | APT / dpkg            |
| USB Control      | modprobe blacklist    |
| Inventory Tool   | dpkg-query            |

---

# Task 1: Enable Basic Antivirus / Endpoint Protection

## 1.1 ClamAV Installation

ClamAV was installed as the open-source antivirus engine for the laboratory workstation.

The installed components include:

* `clamav`
* `clamav-base`
* `clamav-daemon`
* `clamav-freshclam`
* `libclamav12`

The installed ClamAV version was verified with:

```bash
clamscan --version
```

Result:

```text
ClamAV 1.5.3/28099/Fri Aug 21 06:26:38 2026
```

---

## 1.2 ClamAV Database

The ClamAV malware database was verified under:

```text
/var/lib/clamav/
```

The database contained:

* `main.cvd`
* `daily.cvd`
* `bytecode.cvd`
* database signature files
* `freshclam.dat`

The database was successfully available on the workstation.

During manual execution of `freshclam`, a lock error was initially observed because the `freshclam` daemon was already running:

```text
ERROR: Failed to lock the log file /var/log/clamav/freshclam.log
```

The running process was subsequently verified:

```text
/usr/bin/freshclam -d --foreground=true
```

Therefore, the database was already being managed by the FreshClam background process.

---

## 1.3 ClamAV Service

The ClamAV daemon was initially inactive because the required virus database condition had not yet been satisfied.

After the database became available, the daemon was started:

```bash
sudo systemctl start clamav-daemon
```

The service was then verified as:

```text
active
```

The service was also configured as enabled.

Final status was recorded in:

```text
security/clamav-final-status.txt
```

---

## 1.4 ClamAV Malware Scan

A controlled scan of the Lab 36 directory was performed using:

```bash
clamscan -r -i . | tee evidence/clamav-lab-scan.txt
```

### Scan Results

```text
Known viruses: 3628022
Engine version: 1.5.3
Scanned directories: 5
Scanned files: 3
Infected files: 0
Data scanned: 4.44 KiB
```

### Result

**No infected files were detected.**

The scan output was preserved as:

```text
evidence/clamav-lab-scan.txt
```

A concise scan report was also created:

```text
evidence/clamav-scan-summary.txt
```

---

# Task 2: Restrict USB Storage Access

## 2.1 USB Security Baseline

Before changing the USB configuration, the existing workstation state was documented.

The baseline showed:

```text
usb-storage module is not currently loaded
```

The USB utility was available at:

```text
/usr/bin/lsusb
```

No existing `usb-storage` restriction was configured before the change.

The baseline was preserved in:

```text
security/usb-baseline.txt
```

---

## 2.2 Configuration Backup

Before modifying the USB configuration, the existing modprobe blacklist file was backed up:

```bash
sudo cp /etc/modprobe.d/blacklist.conf \
/etc/modprobe.d/blacklist.conf.backup
```

The backup was verified.

This follows an important security and change-management principle:

> Always preserve the original configuration before applying endpoint-security changes.

---

## 2.3 USB Storage Blacklisting

A dedicated configuration file was created:

```text
/etc/modprobe.d/ics-usb-storage.conf
```

The configuration contains:

```text
blacklist usb-storage
```

This prevents the Linux `usb-storage` kernel module from being automatically loaded.

The configuration was verified using:

```bash
grep -Rni "usb-storage" /etc/modprobe.d/
```

Result:

```text
/etc/modprobe.d/ics-usb-storage.conf:1:blacklist usb-storage
```

---

## 2.4 Initramfs Update

The initramfs was updated so that the configuration is incorporated into the boot environment:

```bash
sudo update-initramfs -u
```

The command completed successfully and generated:

```text
/boot/initrd.img-6.14.0-1018-aws
```

---

## 2.5 USB Restriction Verification

The USB storage module was checked after configuration:

```bash
lsmod | grep '^usb_storage'
```

Result:

```text
usb-storage module is not currently loaded
```

The final USB restriction evidence was stored in:

```text
security/usb-restriction-status.txt
```

### Security Observation

USB storage devices can represent a significant security concern in ICS environments because removable media may introduce:

* Malware
* Unauthorized software
* Configuration files
* Unapproved firmware
* Data exfiltration
* Uncontrolled file transfers

Restricting USB storage can therefore reduce the attack surface of an ICS workstation.

---

# Task 3: Document Software Inventory

## 3.1 Package Inventory

The installed software inventory was generated using:

```bash
dpkg-query -W -f='${binary:Package}\t${Version}\t${Architecture}\n' \
> inventory/software-inventory.txt
```

The inventory contains package names, versions, and architectures.

---

## 3.2 Inventory Results

Total installed packages documented:

```text
1738
```

Inventory file:

```text
inventory/software-inventory.txt
```

File size:

```text
68K
```

---

## 3.3 ClamAV Software Inventory

The inventory confirmed the presence of the following ClamAV components:

```text
clamav
clamav-base
clamav-daemon
clamav-freshclam
libclamav12:amd64
```

All package versions were documented in the inventory.

A summary was created at:

```text
inventory/inventory-summary.txt
```

---

# Evidence Collection

The lab preserves evidence and verification information in separate directories.

## Evidence Directory

```text
evidence/
├── clamav-lab-scan.txt
└── clamav-scan-summary.txt
```

### `clamav-lab-scan.txt`

Contains the complete ClamAV scan output.

### `clamav-scan-summary.txt`

Contains the important scan results, including:

* ClamAV version
* Number of known viruses
* Number of scanned directories
* Number of scanned files
* Number of infected files
* Scan start time
* Scan end time

---

# Security Evidence

```text
security/
├── clamav-database.txt
├── clamav-final-status.txt
├── clamav-status.txt
├── usb-baseline.txt
└── usb-restriction-status.txt
```

## `clamav-database.txt`

Documents the ClamAV database files and their sizes.

## `clamav-status.txt`

Records the initial ClamAV service state.

## `clamav-final-status.txt`

Records the final ClamAV installation, database, enabled state, and active state.

## `usb-baseline.txt`

Documents the USB security state before configuration.

## `usb-restriction-status.txt`

Documents the final USB storage restriction configuration and module state.

---

# Software Inventory Evidence

```text
inventory/
├── inventory-summary.txt
└── software-inventory.txt
```

The complete inventory provides a snapshot of installed software and can support:

* Software auditing
* Vulnerability management
* Change management
* Unauthorized software detection
* Incident response
* Configuration management

---

# Important ICS Security Considerations

Endpoint security in an ICS environment differs from normal enterprise IT environments.

ICS workstations may support:

* HMI applications
* SCADA software
* Engineering software
* PLC programming tools
* Historian clients
* Industrial communication software

Security controls must therefore be introduced carefully.

An antivirus scan, software update, reboot, kernel change, or USB restriction could potentially affect an operational system.

Before deploying similar controls to production ICS systems, organizations should consider:

1. Vendor compatibility.
2. Maintenance windows.
3. Application allowlisting.
4. Change-management procedures.
5. Backup and recovery procedures.
6. Testing in a representative environment.
7. Operational technology availability requirements.
8. Safety requirements.
9. Incident-response procedures.

---

# ClamAV Security Observation

ClamAV successfully performed a controlled scan of the laboratory files.

The final result was:

```text
Infected files: 0
```

This confirms that no malware was detected in the files scanned during this laboratory exercise.

However, a clean scan does **not** prove that an entire production ICS environment is malware-free.

It only represents the result of the specific scan performed against the selected laboratory files.

---

# USB Security Observation

The USB storage kernel module was successfully blacklisted using:

```text
blacklist usb-storage
```

The initramfs was regenerated and the module was confirmed as not currently loaded.

This demonstrates a basic Linux endpoint-control technique.

In production ICS environments, USB restrictions should be combined with additional controls such as:

* Device authorization
* Application allowlisting
* Malware scanning
* Endpoint monitoring
* Physical security
* Security policies
* Controlled removable-media procedures

---

# Software Inventory Observation

The workstation contained:

```text
1738
```

installed packages at the time of collection.

Maintaining an accurate inventory helps security teams determine:

* What software is installed.
* Which versions are deployed.
* Whether unauthorized software exists.
* Which packages require updates.
* Which applications may introduce security risk.

Software inventory should be maintained regularly because the workstation state can change over time.

---

# Lab Limitations

This exercise was performed on an:

```text
AWS EC2 Ubuntu 24.04.3 LTS
```

laboratory workstation.

It is **not a production PLC, HMI, SCADA server, engineering workstation, or physical industrial control system**.

The USB restriction was tested at the Linux kernel-module configuration level. A physical USB storage device was not inserted or tested in this AWS environment.

The ClamAV scan covered the Lab 36 working directory rather than the entire operating system.

Therefore, the results demonstrate the security techniques and evidence-collection process rather than production ICS security validation.

---

# Recommended Production Improvements

For a real ICS workstation, endpoint protection should be expanded with:

* Application allowlisting.
* Host-based intrusion detection.
* Centralized logging.
* File-integrity monitoring.
* Secure configuration baselines.
* Vulnerability management.
* Controlled removable media.
* Network segmentation.
* Privileged-access management.
* Offline backups.
* Security monitoring.
* Formal change management.
* Vendor-approved security tools.
* Regular incident-response exercises.

Security controls should always be tested before deployment to operational ICS systems.

---

# Final Lab Results

| Security Control                           | Result |
| ------------------------------------------ | ------ |
| ClamAV installed                           | PASS   |
| ClamAV version verified                    | PASS   |
| Malware database available                 | PASS   |
| ClamAV daemon enabled                      | PASS   |
| ClamAV daemon active                       | PASS   |
| Malware scan completed                     | PASS   |
| Infected files detected                    | 0      |
| USB baseline documented                    | PASS   |
| Original blacklist configuration backed up | PASS   |
| USB storage blacklisted                    | PASS   |
| Initramfs updated                          | PASS   |
| USB storage module not loaded              | PASS   |
| Software inventory created                 | PASS   |
| Package count documented                   | 1738   |
| Evidence documented                        | PASS   |

---

# Final File Structure

```text
Lab-36-Endpoint-Security-for-ICS-Workstations/
│
├── README.md
│
├── evidence/
│   ├── clamav-lab-scan.txt
│   └── clamav-scan-summary.txt
│
├── inventory/
│   ├── inventory-summary.txt
│   └── software-inventory.txt
│
└── security/
    ├── clamav-database.txt
    ├── clamav-final-status.txt
    ├── clamav-status.txt
    ├── usb-baseline.txt
    └── usb-restriction-status.txt
```

---

# Conclusion

Lab 36 demonstrated three fundamental endpoint-security controls for an ICS workstation.

**ClamAV** was installed and configured as the laboratory antivirus solution. The malware database was available, the ClamAV daemon was activated, and a controlled scan completed with **0 infected files**.

**USB storage access** was restricted by blacklisting the `usb-storage` kernel module. The original configuration was backed up, the new security configuration was created, and the initramfs was successfully updated.

**Software inventory** was documented using `dpkg-query`, producing an inventory of **1,738 installed packages**.

The laboratory demonstrates how endpoint-security controls can be implemented, verified, and documented using open-source Linux tools. In a production ICS environment, these controls must be carefully tested and introduced through appropriate change-management, vendor-compatibility, safety, and operational procedures.

**Lab 36 Status: COMPLETED**
