# Lab 26: ICS/SCADA Backup and Recovery Fundamentals

## 1. Lab Overview

Backup and recovery are critical security and operational requirements in **Industrial Control Systems (ICS)** and **Supervisory Control and Data Acquisition (SCADA)** environments.

ICS/SCADA systems control and monitor physical processes such as:

* Electrical power generation and distribution
* Water treatment and distribution
* Manufacturing
* Oil and gas operations
* Building automation
* Transportation infrastructure

A failure, corruption, accidental deletion, ransomware incident, hardware failure, or unauthorized modification can affect both **IT systems and physical operations**.

A well-designed backup strategy allows an organization to restore critical configurations and operational data after an incident.

This laboratory demonstrates:

1. Identification of critical ICS/SCADA components.
2. Classification of data that should be backed up.
3. Comparison of offline and online backups.
4. Creation of a simple backup structure.
5. Use of `rsync` for backup operations.
6. Automation using `cron`.
7. Verification of backup integrity.
8. Basic recovery testing.
9. Security considerations for ICS/SCADA backups.

---

# 2. Lab Objectives

By completing this laboratory, you should be able to:

* Understand the importance of backup and recovery in ICS/SCADA environments.
* Identify critical ICS/SCADA system components.
* Identify configuration files and PLC-related data that require protection.
* Explain the difference between online and offline backups.
* Use `rsync` to perform file-based backups.
* Create a backup directory structure.
* Automate backup tasks with `cron`.
* Verify that backup files were successfully copied.
* Perform a basic recovery test.
* Apply security principles to ICS/SCADA backup systems.
* Document backup and recovery evidence professionally.

---

# 3. Prerequisites

Before starting the lab, ensure you have:

* Linux-based laboratory environment.
* Basic Linux command-line knowledge.
* Basic understanding of ICS/SCADA architecture.
* Basic networking knowledge.
* Basic cybersecurity knowledge.
* `rsync` installed or permission to install it.
* `cron`/`crontab` available.
* Sufficient disk space for the laboratory backup.
* An authorized educational environment.

---

# 4. Safety and Authorization

This laboratory is designed for an **authorized educational environment**.

The backup operations performed in this lab should use **laboratory files and directories only**.

Do not modify production PLCs, HMIs, SCADA servers, historians, or industrial controllers without explicit authorization.

For this lab, directories such as:

```text
/var/scada/
```

are treated as **laboratory examples**.

If the directory does not exist, we can create a controlled laboratory equivalent under the user's home directory.

---

# 5. ICS/SCADA Backup Fundamentals

## 5.1 Why Backups Matter

ICS/SCADA environments depend heavily on configuration data.

For example, an HMI may contain:

* Screen configurations
* Alarm settings
* Operator settings
* Communication parameters
* Device addresses
* User configuration
* Application configuration

A PLC environment may contain:

* PLC programs
* Logic files
* Configuration files
* Device parameters
* Firmware information
* Project files

If this information is lost, recovering the system manually may take significant time.

A backup provides a known copy that can be used during recovery.

---

# 6. Critical ICS/SCADA Components

The following components should be considered during a backup assessment.

## 6.1 Human-Machine Interface (HMI)

An **HMI** allows operators to monitor and interact with industrial processes.

Examples of HMI data include:

```text
HMI configuration
Alarm configuration
Display screens
Communication settings
Operator settings
Application configuration
```

Example laboratory location:

```text
/var/scada/hmi/
```

Example configuration file:

```text
/var/scada/hmi/config.ini
```

---

## 6.2 Programmable Logic Controllers (PLCs)

A **PLC** controls physical industrial processes.

PLC-related backup data may include:

```text
PLC programs
PLC project files
Controller configuration
I/O configuration
Network configuration
Device parameters
```

Example laboratory location:

```text
/var/scada/plc/
```

---

## 6.3 SCADA Server Configuration

SCADA servers may contain:

```text
Application configuration
Communication configuration
Alarm configuration
Tag databases
User configuration
Service configuration
```

These files can be critical for restoring the SCADA environment.

---

## 6.4 Historian Data

Industrial systems may store historical information such as:

* Sensor values
* Process measurements
* Alarm events
* Operator actions
* Production information

Historian data may require a different backup strategy because of its size and continuous growth.

---

# 7. Backup Priority

Not every file has the same recovery priority.

A simple classification can be used:

| Priority | Example                      | Recovery Importance |
| -------- | ---------------------------- | ------------------- |
| Critical | PLC programs                 | Very High           |
| Critical | HMI configuration            | Very High           |
| High     | SCADA configuration          | High                |
| High     | Network/device configuration | High                |
| Medium   | Alarm history                | Medium              |
| Medium   | Historian data               | Medium/High         |
| Low      | Temporary files              | Low                 |

The exact classification should depend on the organization's recovery requirements.

---

# 8. Task 1 — Identify Critical System Components

## Objective

Identify important ICS/SCADA files and directories that should be included in a backup.

---

## Step 1.1 — Check the SCADA Directory

Run:

```bash
ls -lah /var/scada/
```

If this is a laboratory environment and the directory does not exist, create a controlled test environment instead of modifying real industrial data.

For example:

```bash
mkdir -p ~/scada-lab/hmi
mkdir -p ~/scada-lab/plc
mkdir -p ~/scada-lab/config
```

---

## Step 1.2 — Create Laboratory HMI Data

Create an example configuration:

```bash
cat > ~/scada-lab/hmi/config.ini <<'EOF'
[HMI]
name=Lab-HMI
mode=operator
refresh_interval=1000
EOF
```

Verify:

```bash
cat ~/scada-lab/hmi/config.ini
```

Expected output:

```text
[HMI]
name=Lab-HMI
mode=operator
refresh_interval=1000
```

---

## Step 1.3 — Create Laboratory PLC Data

Create an example PLC project:

```bash
cat > ~/scada-lab/plc/plc-program.st <<'EOF'
PROGRAM Main
VAR
    MotorStart : BOOL;
    MotorRunning : BOOL;
END_VAR

MotorRunning := MotorStart;
EOF
```

Verify:

```bash
cat ~/scada-lab/plc/plc-program.st
```

---

## Step 1.4 — Create Example SCADA Configuration

```bash
cat > ~/scada-lab/config/scada.conf <<'EOF'
[SCADA]
name=ICS-SCADA-LAB
environment=educational
protocol=Modbus-TCP
EOF
```

Verify:

```bash
cat ~/scada-lab/config/scada.conf
```

---

## Step 1.5 — Review the Laboratory Structure

Run:

```bash
find ~/scada-lab -type f -ls
```

Expected structure:

```text
scada-lab/
├── config/
│   └── scada.conf
├── hmi/
│   └── config.ini
└── plc/
    └── plc-program.st
```

### Task 1 Result

The laboratory has identified three important categories:

```text
HMI configuration
PLC program
SCADA configuration
```

These represent examples of data that should be considered for backup.

---

# 9. Task 2 — Offline and Online Backup Strategies

## 9.1 Offline Backup

An **offline backup** is stored on media that is disconnected from the production/network environment when not being used.

Examples include:

* External storage
* Offline backup server
* Removable media
* Offline archival storage

### Advantages

* Reduced network exposure
* Better protection against ransomware
* Difficult for attackers to modify when disconnected
* Useful for disaster recovery

### Disadvantages

* Requires manual handling
* May take longer to access
* Storage media can be lost or damaged

---

# 10. Online Backup

An **online backup** remains connected to a network or backup infrastructure.

Examples include:

* Backup server
* NAS
* Cloud storage
* Enterprise backup platform

### Advantages

* Faster access
* Easier automation
* Convenient centralized management
* Can support frequent backups

### Disadvantages

* Network exposure
* Potential ransomware impact
* Requires strong authentication and access controls
* Compromise of the backup server can affect stored backups

---

# 11. Offline vs Online Backup

| Feature               | Offline Backup              | Online Backup             |
| --------------------- | --------------------------- | ------------------------- |
| Network connected     | No                          | Usually yes               |
| Automation            | Limited                     | High                      |
| Accessibility         | Lower                       | High                      |
| Ransomware resistance | Stronger                    | Lower if poorly protected |
| Recovery speed        | Moderate                    | Usually faster            |
| Security              | High when properly isolated | Depends on controls       |
| Best use              | Disaster recovery           | Operational recovery      |

A strong ICS backup strategy should normally use **multiple backup layers**, rather than relying on only one type.

---

# 12. The 3-2-1 Backup Principle

A useful backup concept is the **3-2-1 strategy**:

```text
3 copies of important data
2 different types of storage
1 copy stored offline/offsite
```

Example:

```text
Production system
       |
       +---- Local backup
       |
       +---- Backup server
       |
       +---- Offline/offsite backup
```

This provides additional resilience if one backup becomes unavailable.

---

# 13. Task 3 — Install and Verify rsync

`rsync` is a commonly used Linux utility for synchronizing files and directories.

Check whether it is installed:

```bash
rsync --version
```

If necessary:

```bash
sudo apt update
sudo apt install -y rsync
```

Verify:

```bash
rsync --version
```

Expected output will contain an `rsync` version.

---

# 14. Understanding rsync

Basic syntax:

```bash
rsync [options] SOURCE DESTINATION
```

Example:

```bash
rsync -av ~/scada-lab/ ~/scada-backup/
```

Important options:

### `-a`

Archive mode.

Preserves important file attributes such as:

* Permissions
* Timestamps
* Symbolic links
* Directory structure

### `-v`

Verbose output.

Displays files being processed.

### `-z`

Compression.

Useful primarily when transferring data across a network.

For a local filesystem backup, compression is generally unnecessary.

---

# 15. Task 4 — Create the Backup Directory

Create the backup location:

```bash
mkdir -p ~/scada-backup
```

Verify:

```bash
ls -ld ~/scada-backup
```

---

# 16. Perform the First Backup

Run:

```bash
rsync -av ~/scada-lab/ ~/scada-backup/
```

Expected output should show the files being copied.

Example:

```text
sending incremental file list
./
config/
config/scada.conf
hmi/
hmi/config.ini
plc/
plc/plc-program.st

sent ... bytes
received ... bytes
```

---

# 17. Verify the Backup

Check the backup:

```bash
find ~/scada-backup -type f -ls
```

You should see:

```text
~/scada-backup/config/scada.conf
~/scada-backup/hmi/config.ini
~/scada-backup/plc/plc-program.st
```

---

# 18. Compare Source and Backup

Use:

```bash
diff -r ~/scada-lab ~/scada-backup
```

If there is no output, the files are identical.

This is an important verification step.

A successful `rsync` command alone does not prove that your recovery data is usable.

---

# 19. Task 5 — Test Incremental Backup

Modify the HMI configuration:

```bash
echo "alarm_logging=enabled" >> ~/scada-lab/hmi/config.ini
```

Check:

```bash
cat ~/scada-lab/hmi/config.ini
```

Run the backup again:

```bash
rsync -av ~/scada-lab/ ~/scada-backup/
```

`rsync` should detect the changed file and update the backup.

---

# 20. Verify the Incremental Backup

Run:

```bash
diff -r ~/scada-lab ~/scada-backup
```

No output indicates that the source and backup currently match.

---

# 21. Task 6 — Create a Backup Script

Instead of manually typing the command every time, create a script.

Create:

```bash
nano backup-scada.sh
```

Add:

```bash
#!/bin/bash

SOURCE="$HOME/scada-lab/"
DESTINATION="$HOME/scada-backup/"

echo "======================================"
echo " ICS/SCADA Backup"
echo "======================================"
echo "Source      : $SOURCE"
echo "Destination : $DESTINATION"
echo "Start Time  : $(date)"
echo "--------------------------------------"

rsync -av "$SOURCE" "$DESTINATION"

RESULT=$?

echo "--------------------------------------"

if [ "$RESULT" -eq 0 ]; then
    echo "[PASS] Backup completed successfully"
else
    echo "[FAIL] Backup failed"
fi

echo "End Time    : $(date)"
echo "======================================"

exit "$RESULT"
```

Save the file.

---

# 22. Make the Script Executable

Run:

```bash
chmod +x backup-scada.sh
```

Verify:

```bash
ls -l backup-scada.sh
```

The permissions should include executable permission.

---

# 23. Run the Backup Script

Execute:

```bash
./backup-scada.sh
```

Expected result:

```text
[PASS] Backup completed successfully
```

---

# 24. Task 7 — Automate Backup Using Cron

`cron` is a Linux scheduling service that can execute commands automatically.

Check cron:

```bash
systemctl status cron
```

If required:

```bash
sudo systemctl enable --now cron
```

---

# 25. Understand Cron Syntax

A cron entry contains five scheduling fields:

```text
MINUTE HOUR DAY MONTH WEEKDAY COMMAND
```

Example:

```text
0 2 * * * command
```

Meaning:

```text
Minute   = 0
Hour     = 2
Day      = every day
Month    = every month
Weekday  = every weekday
```

Therefore:

```text
0 2 * * *
```

means:

**Every day at 02:00 AM.**

---

# 26. Configure the Cron Job

Open the user's crontab:

```bash
crontab -e
```

Add:

```cron
0 2 * * * /home/ubuntu/SCADA-ICS-Security-101/Lab-26-ICS-SCADA-Backup-and-Recovery/backup-scada.sh >> /home/ubuntu/scada-backup.log 2>&1
```

> Adjust the path if your Lab 26 directory has a different name.

Save and exit.

---

# 27. Verify the Cron Job

Run:

```bash
crontab -l
```

You should see the scheduled backup entry.

Example:

```text
0 2 * * * /home/ubuntu/.../backup-scada.sh >> /home/ubuntu/scada-backup.log 2>&1
```

---

# 28. Test the Cron Command Manually

Before waiting for 2 AM, always test the exact command manually:

```bash
/home/ubuntu/SCADA-ICS-Security-101/Lab-26-ICS-SCADA-Backup-and-Recovery/backup-scada.sh
```

Then check:

```bash
tail -20 ~/scada-backup.log
```

This helps detect problems before relying on the scheduled job.

---

# 29. Task 8 — Basic Recovery Test

A backup is only useful if it can actually be restored.

Create a recovery directory:

```bash
mkdir -p ~/scada-recovery
```

Restore the backup:

```bash
rsync -av ~/scada-backup/ ~/scada-recovery/
```

---

# 30. Verify Recovery

Run:

```bash
find ~/scada-recovery -type f -ls
```

Then compare:

```bash
diff -r ~/scada-lab ~/scada-recovery
```

No output indicates that the recovered files match the original laboratory data.

---

# 31. Simulate Data Loss

For a controlled laboratory test, create a temporary copy and remove a file from the copy.

For example:

```bash
cp -r ~/scada-lab ~/scada-failure-test
```

Remove a file:

```bash
rm ~/scada-failure-test/hmi/config.ini
```

Verify:

```bash
ls ~/scada-failure-test/hmi/
```

The configuration file should no longer be present.

---

# 32. Recover the Missing File

Restore it from the backup:

```bash
rsync -av ~/scada-backup/hmi/ ~/scada-failure-test/hmi/
```

Verify:

```bash
cat ~/scada-failure-test/hmi/config.ini
```

The configuration should be restored.

---

# 33. Backup Integrity Verification

Backup integrity should be checked regularly.

A simple checksum can be generated with:

```bash
sha256sum ~/scada-lab/hmi/config.ini
```

Generate the backup checksum:

```bash
sha256sum ~/scada-backup/hmi/config.ini
```

If both checksums are identical, the files have identical contents.

Example:

```text
SOURCE:
abc123...  config.ini

BACKUP:
abc123...  config.ini
```

Matching hashes provide strong evidence that the file contents are identical.

---

# 34. ICS/SCADA Backup Security Considerations

Backup systems themselves must be protected.

Important controls include:

### Access Control

Only authorized administrators should be able to:

* Create backups
* Delete backups
* Modify backup repositories
* Restore systems

---

### Network Segmentation

Backup infrastructure should not unnecessarily share unrestricted connectivity with control networks.

A common architecture is:

```text
ICS Network
     |
     | Controlled connection
     |
Backup System
     |
     +---- Offline Backup
```

---

### Encryption

Sensitive backup data may require encryption:

```text
Production Data
      ↓
Encrypted Backup
      ↓
Protected Storage
```

---

### Offline Copies

Maintain offline or otherwise isolated backup copies to reduce the impact of ransomware or destructive attacks.

---

### Backup Retention

Do not keep only the latest backup.

A retention policy may maintain:

```text
Daily backups
Weekly backups
Monthly backups
Long-term archives
```

The exact retention period depends on operational and regulatory requirements.

---

# 35. Recovery Time Objective (RTO)

**RTO** describes how quickly a system needs to be restored after a disruption.

Example:

```text
RTO = 4 hours
```

This means the organization targets restoration within four hours.

---

# 36. Recovery Point Objective (RPO)

**RPO** describes the maximum acceptable amount of data loss measured in time.

Example:

```text
RPO = 1 hour
```

This means the organization aims to recover data from no more than approximately one hour before the incident.

---

# 37. RTO vs RPO

| Concept | Meaning                                 |
| ------- | --------------------------------------- |
| RTO     | How quickly the system must be restored |
| RPO     | How much recent data can be lost        |

Example:

```text
Incident
   |
   +---- RPO → maximum acceptable data loss
   |
   +---- RTO → maximum acceptable recovery time
```

These values help determine backup frequency and recovery design.

---

# 38. Troubleshooting

## Problem 1 — rsync command not found

Check:

```bash
which rsync
```

Install:

```bash
sudo apt update
sudo apt install -y rsync
```

---

## Problem 2 — Permission denied

Check directory permissions:

```bash
ls -ld ~/scada-lab
ls -ld ~/scada-backup
```

Avoid using `sudo` unnecessarily when working with your own laboratory directories.

---

## Problem 3 — Cron job does not execute

Check:

```bash
crontab -l
```

Check cron service:

```bash
systemctl status cron
```

Use absolute paths in cron jobs.

---

## Problem 4 — Backup appears empty

Check:

```bash
find ~/scada-lab -type f
```

Then:

```bash
find ~/scada-backup -type f
```

Confirm that the source actually contains files.

---

## Problem 5 — Source and backup differ

Run:

```bash
diff -r ~/scada-lab ~/scada-backup
```

Then run:

```bash
rsync -av ~/scada-lab/ ~/scada-backup/
```

Run the comparison again.

---

# 39. Evidence to Collect

For a professional lab submission, collect evidence such as:

### System Information

```bash
hostname
uname -a
```

### rsync Verification

```bash
rsync --version
```

### Source Data

```bash
find ~/scada-lab -type f -ls
```

### Backup Data

```bash
find ~/scada-backup -type f -ls
```

### Backup Execution

```bash
./backup-scada.sh
```

### Backup Comparison

```bash
diff -r ~/scada-lab ~/scada-backup
```

### Cron Configuration

```bash
crontab -l
```

### Recovery

```bash
find ~/scada-recovery -type f -ls
```

### Integrity

```bash
sha256sum ~/scada-lab/hmi/config.ini
sha256sum ~/scada-backup/hmi/config.ini
```

---

# 40. Suggested Evidence Files

A clean Lab 26 directory could contain:

```text
Lab-26-ICS-SCADA-Backup-and-Recovery/
│
├── README.md
├── lab-notes.md
├── backup-scada.sh
└── evidence/
    ├── backup-output.txt
    ├── source-files.txt
    ├── backup-files.txt
    └── recovery-verification.txt
```

Do **not** commit unnecessary virtual environments, caches, secrets, credentials, or huge backup datasets to GitHub.

---

# 41. Lab Results

## Task 1 — Critical Components

Identified:

* HMI configuration
* PLC program
* SCADA configuration

**Result:** PASS

---

## Task 2 — Backup Strategies

Reviewed:

* Offline backups
* Online backups
* 3-2-1 backup strategy
* Backup security considerations

**Result:** PASS

---

## Task 3 — rsync Backup

Performed:

```bash
rsync -av ~/scada-lab/ ~/scada-backup/
```

**Result:** PASS

---

## Task 4 — Backup Verification

Performed:

```bash
diff -r ~/scada-lab ~/scada-backup
```

**Result:** PASS when no differences are reported.

---

## Task 5 — Automated Backup

Configured a `cron` schedule for automated execution.

**Result:** PASS after verifying the crontab entry and testing the script.

---

## Task 6 — Recovery Test

Restored laboratory data from the backup and verified the recovered files.

**Result:** PASS

---

# 42. Skills Practiced

During this laboratory, the following skills were practiced:

* ICS/SCADA asset identification
* Backup planning
* Linux file management
* `rsync`
* Bash scripting
* `cron`
* File integrity verification
* SHA-256 checksums
* Recovery testing
* RTO/RPO concepts
* Backup security
* Disaster recovery concepts
* Documentation
* Evidence collection

---

# 43. Key Takeaways

1. **Backups are essential for ICS/SCADA resilience.**

2. **PLC programs and HMI/SCADA configurations are highly important recovery assets.**

3. **Online backups provide convenience and automation but can remain exposed to network threats.**

4. **Offline backups provide an additional layer of protection against ransomware and destructive attacks.**

5. **`rsync` provides a simple and efficient method for file-based backups.**

6. **Automation using `cron` reduces dependence on manual backup operations.**

7. **A backup should always be tested through restoration.**

8. **RTO defines the desired recovery time.**

9. **RPO defines the acceptable amount of data loss.**

10. **Backup infrastructure must itself be secured.**

11. **A 3-2-1 strategy provides stronger resilience than maintaining only one backup copy.**

---

# 44. Final Lab Checklist

* [ ] Understand ICS/SCADA backup requirements
* [ ] Identify critical HMI data
* [ ] Identify critical PLC data
* [ ] Identify SCADA configuration data
* [ ] Create laboratory SCADA data
* [ ] Install/verify `rsync`
* [ ] Create backup directory
* [ ] Perform initial backup
* [ ] Verify backup contents
* [ ] Test incremental backup
* [ ] Create backup script
* [ ] Configure `cron`
* [ ] Verify scheduled backup
* [ ] Perform recovery test
* [ ] Verify recovered files
* [ ] Perform checksum verification
* [ ] Document RTO/RPO concepts
* [ ] Document security considerations
* [ ] Collect evidence
* [ ] Update `lab-notes.md`
* [ ] Review README
* [ ] Commit laboratory work to Git
* [ ] Push the completed lab to GitHub

---

# 45. Conclusion

This laboratory demonstrated the fundamentals of **ICS/SCADA backup and recovery** using Linux-based open-source tools.

The practical workflow covered the complete backup lifecycle:

```text
Identify Critical Data
        ↓
Plan Backup Strategy
        ↓
Create Backup
        ↓
Verify Backup
        ↓
Automate Backup
        ↓
Protect Backup
        ↓
Test Recovery
        ↓
Document Results
```

The laboratory emphasized that backup is not simply the act of copying files. A reliable ICS/SCADA backup strategy must consider:

* What data is critical
* How frequently it should be backed up
* Where backups should be stored
* Who can access them
* How backups are protected
* How long backups are retained
* How quickly systems must be restored
* How much data loss is acceptable
* Whether restoration has actually been tested

A properly designed backup and recovery process improves **availability, resilience, operational continuity, and disaster recovery capability** in ICS/SCADA environments.

**Lab 26 Focus:**
`Backup → Verify → Protect → Automate → Recover → Test`
