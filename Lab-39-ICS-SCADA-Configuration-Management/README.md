````bash
cd ~/SCADA-ICS-Security-101/Lab-39-ICS-SCADA-Configuration-Management

cat > README.md <<'EOF'
# Lab 39: ICS/SCADA Configuration Management

## Overview

This lab demonstrates a practical configuration management process for ICS/SCADA environments.

The exercise uses:

- Git for configuration version control
- SHA-256 hashes for configuration integrity verification
- SQLite as a lightweight Configuration Management Database (CMDB)
- Bash automation for periodic configuration reviews
- Simulated PLC and HMI configuration files
- Evidence files to document configuration changes and verification results

The lab demonstrates how configuration baselines can be established, changes can be detected, changes can be recorded in a CMDB, and configurations can be restored and verified against an approved baseline.

---

## Objectives

- Understand the importance of configuration management in ICS/SCADA environments.
- Establish version control for PLC and HMI configurations.
- Create configuration baselines using Git and SHA-256 hashes.
- Record configuration changes in a SQLite CMDB.
- Detect configuration drift using automated hash comparison.
- Document simulated configuration changes.
- Restore a configuration to its approved baseline.
- Perform periodic configuration reviews.
- Maintain an auditable configuration-management process.

---

## Lab Environment

| Component | Details |
|---|---|
| Operating System | Ubuntu Linux |
| Architecture | x86_64 |
| Version Control | Git 2.43.0 |
| Database | SQLite 3.45.1 |
| Shell | Bash |
| Repository | SCADA-ICS-Security-101 |
| Lab | Lab 39 |
| PLC | Simulated PLC |
| HMI | Simulated HMI |
| Protocol | Modbus-TCP |

> The PLC and HMI configurations used in this lab are simulated configuration files. No physical industrial controller or production ICS system was modified.

---

## Tools Used

### Git

Git provides version control for configuration files and allows configuration changes to be associated with commits.

Verified version:

```text
git version 2.43.0
````

### SQLite

SQLite is used as a lightweight CMDB to record configuration information, change descriptions, Git references, and SHA-256 hashes.

Verified version:

```text
3.45.1
```

### SHA-256

SHA-256 hashes are used to verify that configuration files have not changed unexpectedly.

### Bash

Bash scripts automate configuration integrity checks and periodic reviews.

---

# Directory Structure

```text
Lab-39-ICS-SCADA-Configuration-Management/
├── README.md
├── evidence/
│   ├── cmdb-verification.txt
│   └── periodic-review.txt
├── configurations/
│   ├── plc/
│   │   ├── plc_config.txt
│   │   └── plc_config.baseline.txt
│   └── hmi/
│       └── hmi_config.xml
├── cmdb/
│   └── config_management.db
├── scripts/
│   └── config-review.sh
└── change-records/
```

---

# Task 1: Establish Version Control for PLC and HMI Configurations

## 1.1 Verify Git

Git was already available on the Ubuntu system.

```bash
git --version
```

Result:

```text
git version 2.43.0
```

The Lab 39 directory is located inside the existing Git repository:

```text
/home/ubuntu/SCADA-ICS-Security-101
```

---

## 1.2 Create Simulated PLC Configuration

The PLC configuration represents a simplified industrial controller configuration.

File:

```text
configurations/plc/plc_config.txt
```

Configuration:

```text
# LAB 39 - SIMULATED PLC CONFIGURATION

PLC_NAME=PLC-LAB-01
PLC_MODEL=SIMULATED-PLC
FIRMWARE_VERSION=1.0
IP_ADDRESS=192.168.10.10
PROTOCOL=Modbus-TCP
PORT=502
SCAN_INTERVAL=1000
SAFETY_INTERLOCK=enabled
REMOTE_CONFIGURATION=disabled
```

Important configuration parameters include:

* PLC name
* PLC model
* Firmware version
* IP address
* Industrial communication protocol
* Modbus TCP port
* Scan interval
* Safety interlock state
* Remote configuration state

---

## 1.3 Create Simulated HMI Configuration

File:

```text
configurations/hmi/hmi_config.xml
```

Configuration:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- LAB 39 - SIMULATED HMI CONFIGURATION -->
<hmi>
    <name>HMI-LAB-01</name>
    <version>1.0</version>
    <plc_target>PLC-LAB-01</plc_target>
    <protocol>Modbus-TCP</protocol>
    <poll_interval>1000</poll_interval>
    <alarm_monitoring>enabled</alarm_monitoring>
    <remote_access>disabled</remote_access>
</hmi>
```

The HMI configuration contains:

* HMI name
* Version
* PLC target
* Communication protocol
* Polling interval
* Alarm monitoring status
* Remote access status

---

## 1.4 Generate Initial SHA-256 Hashes

The original configuration hashes were recorded as the baseline.

### PLC baseline

```text
845e9428bbfbadd04c50f7c167d2f71d35c17ffcf59f1b80f67e39b740dd831c
```

### HMI baseline

```text
74a1001826592ae7af7bce544e1685fd7ce6952d6bb79b25b0fe41946323dedf
```

These hashes provide an integrity reference for future configuration reviews.

---

## 1.5 Commit the Baseline Configurations

The initial PLC and HMI configurations were added to Git:

```bash
git add configurations/plc/plc_config.txt configurations/hmi/hmi_config.xml
```

Commit:

```bash
git commit -m "Lab 39: add baseline PLC and HMI configurations"
```

Recorded commit:

```text
0948aee
```

This establishes the initial Git configuration baseline.

---

# Task 2: Record Configuration Changes in a CMDB

## 2.1 Install SQLite

SQLite was not initially installed.

The package was installed using:

```bash
sudo apt update
sudo apt install -y sqlite3
```

SQLite was then verified:

```bash
sqlite3 --version
```

Result:

```text
3.45.1
```

---

## 2.2 Create the CMDB

The SQLite database was created at:

```text
cmdb/config_management.db
```

The database contains a table named:

```text
ConfigChanges
```

---

## 2.3 CMDB Table Structure

The table contains:

```sql
CREATE TABLE IF NOT EXISTS ConfigChanges (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    FileName TEXT NOT NULL,
    DateModified TEXT NOT NULL,
    ChangeDescription TEXT NOT NULL,
    GitCommit TEXT,
    SHA256 TEXT
);
```

The database records:

* Record ID
* Configuration file
* Modification date
* Description of the change
* Git commit
* SHA-256 hash

This provides a basic configuration-management audit trail.

---

## 2.4 Record Initial Baselines

The initial PLC configuration was recorded with:

```text
File:
configurations/plc/plc_config.txt

Git Commit:
0948aee

SHA-256:
845e9428bbfbadd04c50f7c167d2f71d35c17ffcf59f1b80f67e39b740dd831c
```

The initial HMI configuration was recorded with:

```text
File:
configurations/hmi/hmi_config.xml

Git Commit:
0948aee

SHA-256:
74a1001826592ae7af7bce544e1685fd7ce6952d6bb79b25b0fe41946323dedf
```

---

## 2.5 Verify CMDB Records

The database was queried using:

```bash
sqlite3 -header -column cmdb/config_management.db \
"SELECT * FROM ConfigChanges;"
```

The final baseline records include:

```text
ID  FileName                           DateModified  ChangeDescription
1   configurations/plc/plc_config.txt  2026-08-22    Initial baseline PLC configuration
2   configurations/hmi/hmi_config.xml  2026-08-22    Initial baseline HMI configuration
```

The CMDB therefore contains records for both PLC and HMI configurations.

---

## 2.6 Verify Database Integrity

The SQLite database was checked using:

```bash
sqlite3 cmdb/config_management.db \
"PRAGMA integrity_check;"
```

Result:

```text
ok
```

This confirms that the SQLite database passed the integrity check.

Evidence was saved to:

```text
evidence/cmdb-verification.txt
```

---

# Task 3: Automated Configuration Review

## 3.1 Create Configuration Review Script

The automated review script is:

```text
scripts/config-review.sh
```

The script:

1. Calculates the current PLC SHA-256 hash.
2. Calculates the current HMI SHA-256 hash.
3. Retrieves the approved baseline hashes from the CMDB.
4. Compares current hashes against approved hashes.
5. Reports MATCH or MISMATCH.
6. Produces an overall review result.

---

## 3.2 Run the Configuration Review

The script was executed with:

```bash
./scripts/config-review.sh
```

The initial review produced:

```text
PLC configuration: MATCH
HMI configuration: MATCH

REVIEW RESULT: CONFIGURATIONS MATCH APPROVED BASELINE
```

This confirms that the configurations initially matched the approved CMDB baseline.

---

# Task 4: Simulate Configuration Drift

To demonstrate configuration monitoring, the PLC scan interval was intentionally changed.

Original value:

```text
SCAN_INTERVAL=1000
```

Modified value:

```text
SCAN_INTERVAL=2000
```

The modified configuration generated a new SHA-256 hash:

```text
e1f5f2a9348b44ef080050285c25c74c31890eddf2793a4285ef8ecd9f53b913
```

The original approved hash was:

```text
845e9428bbfbadd04c50f7c167d2f71d35c17ffcf59f1b80f67e39b740dd831c
```

Because the hashes were different, the configuration review detected the change.

---

## 4.1 Configuration Drift Detection

The review script reported:

```text
PLC configuration: MISMATCH
HMI configuration: MATCH

REVIEW RESULT: DISCREPANCY DETECTED
```

This demonstrates how hash comparison can identify unexpected configuration changes.

---

# Task 5: Record the Configuration Change in the CMDB

The simulated change was recorded in the CMDB.

Change description:

```text
Simulated configuration change:
SCAN_INTERVAL changed from 1000 to 2000
```

The change was associated with:

```text
GitCommit: PENDING
```

New configuration hash:

```text
e1f5f2a9348b44ef080050285c25c74c31890eddf2793a4285ef8ecd9f53b913
```

The database integrity check continued to return:

```text
ok
```

This demonstrates that configuration drift can be documented in the CMDB rather than simply detected and ignored.

---

# Task 6: Restore the Approved Configuration

The simulated PLC configuration was restored using the saved baseline:

```bash
cp configurations/plc/plc_config.baseline.txt \
   configurations/plc/plc_config.txt
```

The restored value was verified:

```bash
grep SCAN_INTERVAL configurations/plc/plc_config.txt
```

Result:

```text
SCAN_INTERVAL=1000
```

The restored SHA-256 hash was:

```text
845e9428bbfbadd04c50f7c167d2f71d35c17ffcf59f1b80f67e39b740dd831c
```

---

# Task 7: Correct Baseline Comparison Logic

During testing, the review script initially compared against the most recent CMDB record.

Because the simulated change had been recorded in the CMDB, this caused the restored original configuration to appear as a mismatch.

The script was therefore updated to compare against the original approved baseline:

```sql
ORDER BY ID ASC LIMIT 1
```

This ensures that the review process compares the active configuration against the approved baseline rather than the latest change record.

The corrected review produced:

```text
PLC approved baseline:
845e9428bbfbadd04c50f7c167d2f71d35c17ffcf59f1b80f67e39b740dd831c

HMI approved baseline:
74a1001826592ae7af7bce544e1685fd7ce6952d6bb79b25b0fe41946323dedf
```

Final result:

```text
PLC configuration: MATCH
HMI configuration: MATCH

REVIEW RESULT: CONFIGURATIONS MATCH APPROVED BASELINE
```

---

# Task 8: Final Periodic Configuration Review

A complete review was saved to:

```text
evidence/periodic-review.txt
```

The final review verified:

### PLC

```text
SCAN_INTERVAL=1000
```

Final PLC hash:

```text
845e9428bbfbadd04c50f7c167d2f71d35c17ffcf59f1b80f67e39b740dd831c
```

### HMI

Final HMI hash:

```text
74a1001826592ae7af7bce544e1685fd7ce6952d6bb79b25b0fe41946323dedf
```

### Database

```text
PRAGMA integrity_check;
```

Result:

```text
ok
```

### Final configuration review

```text
REVIEW RESULT: CONFIGURATIONS MATCH APPROVED BASELINE
```

---

# Evidence

The lab contains the following evidence:

## CMDB Verification

```text
evidence/cmdb-verification.txt
```

Contains:

* Database timestamp
* Database table information
* Configuration records
* Git commit
* SHA-256 hashes
* Database integrity result

## Periodic Review

```text
evidence/periodic-review.txt
```

Contains:

* Review timestamp
* Current configuration hashes
* Approved baseline hashes
* Configuration review results
* Configuration change history
* Database integrity check
* Final PLC configuration
* Final PLC hash

---

# Configuration Baselines

| Configuration | Approved SHA-256                                                   | Status |
| ------------- | ------------------------------------------------------------------ | ------ |
| PLC           | `845e9428bbfbadd04c50f7c167d2f71d35c17ffcf59f1b80f67e39b740dd831c` | MATCH  |
| HMI           | `74a1001826592ae7af7bce544e1685fd7ce6952d6bb79b25b0fe41946323dedf` | MATCH  |

---

# Configuration Change Demonstration

The lab intentionally introduced the following change:

```text
SCAN_INTERVAL=1000
```

Changed to:

```text
SCAN_INTERVAL=2000
```

The new hash became:

```text
e1f5f2a9348b44ef080050285c25c74c31890eddf2793a4285ef8ecd9f53b913
```

The automated review detected:

```text
PLC configuration: MISMATCH
```

The change was then recorded in the CMDB and the configuration was restored to the approved baseline.

This demonstrates a complete configuration-drift lifecycle:

```text
Approved Baseline
       |
       v
Configuration Change
       |
       v
SHA-256 Hash Changes
       |
       v
Automated Detection
       |
       v
CMDB Change Record
       |
       v
Configuration Restoration
       |
       v
Final Verification
       |
       v
Approved Baseline Restored
```

---

# ICS/SCADA Security Relevance

Configuration management is particularly important in ICS/SCADA environments because unauthorized or undocumented configuration changes can affect:

* PLC operation
* HMI functionality
* Industrial communication
* Alarm behavior
* Safety-related settings
* Network connectivity
* Process monitoring
* System availability

A configuration-management process provides visibility into what configuration is approved, what changed, when it changed, and whether the current system matches the approved baseline.

---

# Security Benefits

This lab demonstrates several important security controls:

### Configuration Integrity

SHA-256 hashes provide a mechanism for detecting unexpected file modifications.

### Version Control

Git provides historical tracking of configuration files and associates changes with commits.

### Change Accountability

The CMDB records configuration changes and provides a structured audit trail.

### Configuration Drift Detection

Automated comparison detects differences between the active configuration and the approved baseline.

### Recovery

A known-good baseline can be used to restore a configuration after an unauthorized or incorrect change.

### Auditability

Evidence files preserve the results of configuration reviews and database integrity checks.

---

# Important ICS Considerations

In a real ICS/SCADA environment, configuration changes should not be performed directly on production PLCs or HMIs without appropriate authorization.

A controlled process should include:

1. Change request
2. Risk assessment
3. Approval
4. Backup
5. Maintenance window
6. Configuration change
7. Validation
8. Documentation
9. Rollback plan
10. Post-change monitoring

Safety and operational availability must always take priority when performing configuration management on industrial control systems.

---

# Key Commands

## Check Git

```bash
git --version
```

## Check SQLite

```bash
sqlite3 --version
```

## Generate Configuration Hash

```bash
sha256sum configurations/plc/plc_config.txt
sha256sum configurations/hmi/hmi_config.xml
```

## Query CMDB

```bash
sqlite3 -header -column cmdb/config_management.db \
"SELECT * FROM ConfigChanges;"
```

## Check Database Integrity

```bash
sqlite3 cmdb/config_management.db \
"PRAGMA integrity_check;"
```

## Run Configuration Review

```bash
./scripts/config-review.sh
```

## Check Final PLC Parameter

```bash
grep SCAN_INTERVAL configurations/plc/plc_config.txt
```

## Check Git Status

```bash
git status
```

---

# Final Assessment

Lab 39 successfully demonstrates a basic ICS/SCADA configuration-management workflow.

The lab established simulated PLC and HMI configuration baselines, stored their SHA-256 hashes, committed the baseline configurations to Git, and recorded the configuration information in a SQLite CMDB.

A simulated PLC configuration change was introduced by changing:

```text
SCAN_INTERVAL=1000
```

to:

```text
SCAN_INTERVAL=2000
```

The automated configuration review successfully detected the resulting hash mismatch.

The change was recorded in the CMDB, and the PLC configuration was subsequently restored to the approved baseline.

The final review confirmed:

```text
PLC configuration: MATCH
HMI configuration: MATCH

REVIEW RESULT: CONFIGURATIONS MATCH APPROVED BASELINE
```

The SQLite database also passed its integrity check:

```text
ok
```

Therefore, the Lab 39 exercise demonstrates the complete configuration-management lifecycle:

```text
Baseline
   |
   v
Version Control
   |
   v
CMDB Recording
   |
   v
Configuration Monitoring
   |
   v
Change Detection
   |
   v
Change Documentation
   |
   v
Restoration
   |
   v
Final Verification
```

The exercise demonstrates how Git, SQLite, SHA-256 hashing, and Bash automation can be combined to create a simple but auditable configuration-management process for ICS/SCADA environments.

---

# Lab Status

```text
[+] Git configuration management
[+] PLC configuration baseline
[+] HMI configuration baseline
[+] SHA-256 integrity verification
[+] SQLite CMDB
[+] Configuration change recording
[+] Automated configuration review
[+] Configuration drift detection
[+] Configuration restoration
[+] Periodic review evidence
[+] Database integrity verification
[+] Final baseline verification

LAB 39 STATUS: COMPLETE
```

EOF

```
```
