# Lab 26: ICS/SCADA Backup and Recovery Fundamentals

## 1. Lab Information

**Lab:** Lab 26 - ICS/SCADA Backup and Recovery Fundamentals
**Topic:** Backup, Recovery, Resilience, and Business Continuity in ICS/SCADA
**Environment:** Authorized educational laboratory
**Platform:** Ubuntu Linux
**Tools:** `rsync`, `cron`, Bash, standard Linux utilities
**Lab Type:** Defensive ICS/SCADA Security Practical

---

# 2. Lab Objective

The objective of this laboratory exercise is to understand how backup and recovery mechanisms can be designed for Industrial Control System (ICS) and Supervisory Control and Data Acquisition (SCADA) environments.

The practical focuses on:

* Identifying critical ICS/SCADA configuration data.
* Understanding why HMI and PLC data should be backed up.
* Comparing offline and online backup strategies.
* Using `rsync` to perform backups.
* Creating a controlled laboratory backup environment.
* Verifying backup integrity.
* Performing a basic recovery operation.
* Understanding automated backup scheduling with `cron`.
* Documenting backup and recovery procedures.
* Understanding the importance of recovery testing in industrial environments.

---

# 3. Safety and Laboratory Scope

This laboratory is performed in an isolated educational environment.

No real industrial control system, production PLC, HMI, SCADA server, or operational infrastructure should be modified during this exercise.

The laboratory uses simulated ICS/SCADA files and directories.

The purpose is to demonstrate **defensive backup and recovery concepts** rather than interact with real industrial equipment.

---

# 4. ICS/SCADA Backup Fundamentals

Backup is an important part of ICS/SCADA resilience.

Industrial systems can contain critical information such as:

* HMI configuration files
* PLC programs
* PLC configuration
* SCADA project files
* Alarm configurations
* Historian configuration
* Network configuration
* Device configuration
* Engineering workstation files
* User and application configuration
* Security configuration
* System documentation

Loss of these files can make recovery from hardware failure, accidental deletion, malware, or ransomware significantly more difficult.

A properly designed backup strategy provides a recovery point that can be used to restore critical configuration and operational data.

---

# 5. Critical ICS/SCADA Components

## 5.1 Human-Machine Interface (HMI)

An HMI allows operators to interact with an industrial process.

HMI systems may contain:

* Screen configurations
* Alarm definitions
* User interface settings
* Tag databases
* Communication settings
* Operator configuration
* Application settings

Example laboratory path:

```text
/var/scada/hmi/
```

In this laboratory, a simulated directory will be used instead of modifying the real `/var/scada/` directory.

---

## 5.2 Programmable Logic Controllers (PLCs)

PLCs are responsible for monitoring and controlling industrial processes.

PLC-related information may include:

* PLC programs
* Logic files
* Device configuration
* Communication parameters
* Controller settings
* Project files

Example laboratory path:

```text
/var/scada/plc/
```

Backing up PLC project information is important because rebuilding a controller configuration manually can be time-consuming and error-prone.

---

## 5.3 SCADA Server Configuration

SCADA servers may contain:

* Project files
* Tag databases
* Alarm configuration
* Historian configuration
* Communication drivers
* User configuration
* Application settings

These files should be considered critical assets when designing a backup strategy.

---

# 6. Laboratory Directory Structure

For this exercise, a safe simulated environment will be created inside the Lab 26 directory.

Expected structure:

```text
Lab-26-ICS-SCADA-Backup-and-Recovery-Fundamentals/
│
├── README.md
├── lab-notes.md
├── scada-data/
│   ├── hmi/
│   │   └── config.ini
│   │
│   └── plc/
│       └── plc-program.st
│
├── backup/
│   └── scada/
│
└── scripts/
    └── backup-scada.sh
```

This structure keeps the practical isolated from the operating system.

---

# 7. Environment Verification

## 7.1 Verify Operating System

Command:

```bash
cat /etc/os-release
```

Expected result:

The command should display the Linux distribution and version.

Example:

```text
Ubuntu
```

---

## 7.2 Verify Current Directory

Command:

```bash
pwd
```

Expected result:

```text
/home/ubuntu/SCADA-ICS-Security-101/Lab-26-ICS-SCADA-Backup-and-Recovery-Fundamentals
```

---

## 7.3 Verify Linux User

Command:

```bash
whoami
```

Expected result:

```text
ubuntu
```

---

# 8. Task 1 - Create Simulated ICS/SCADA Data

The first practical task is to create simulated HMI and PLC configuration files.

## 8.1 Create the Directory Structure

Command:

```bash
mkdir -p scada-data/hmi
mkdir -p scada-data/plc
mkdir -p backup/scada
mkdir -p scripts
```

Verify:

```bash
find . -maxdepth 3 -type d
```

Expected structure should include:

```text
./scada-data
./scada-data/hmi
./scada-data/plc
./backup
./backup/scada
./scripts
```

---

# 9. Create Simulated HMI Configuration

Create the HMI configuration file:

```bash
nano scada-data/hmi/config.ini
```

Example laboratory content:

```ini
[HMI]
name=SCADA-Lab-HMI
mode=operator

[Communication]
protocol=Modbus-TCP
server=127.0.0.1
port=1502

[Alarm]
enabled=true
```

Save and exit.

Verify:

```bash
cat scada-data/hmi/config.ini
```

---

# 10. Create Simulated PLC Program

Create a simulated PLC program:

```bash
nano scada-data/plc/plc-program.st
```

Example:

```text
PROGRAM Main
VAR
    Motor_Start : BOOL;
    Motor_Stop  : BOOL;
    Motor_Run   : BOOL;
END_VAR

IF Motor_Start AND NOT Motor_Stop THEN
    Motor_Run := TRUE;
END_IF;

IF Motor_Stop THEN
    Motor_Run := FALSE;
END_IF;

END_PROGRAM
```

Verify:

```bash
cat scada-data/plc/plc-program.st
```

---

# 11. Identify Critical Files

List the simulated ICS/SCADA data:

```bash
find scada-data -type f -ls
```

Expected files:

```text
scada-data/hmi/config.ini
scada-data/plc/plc-program.st
```

These files represent critical configuration information that should be protected through backup.

---

# 12. Task 2 - Install and Verify rsync

`rsync` is a commonly used Linux utility for synchronizing files and directories.

It can preserve important file attributes and efficiently transfer changed files.

## 12.1 Check rsync

Command:

```bash
rsync --version
```

If it is not installed:

```bash
sudo apt update
sudo apt install -y rsync
```

Verify again:

```bash
rsync --version
```

Expected result:

```text
rsync version ...
```

---

# 13. Understanding rsync Options

A common backup command is:

```bash
rsync -avz SOURCE DESTINATION
```

Important options:

| Option | Meaning                       |
| ------ | ----------------------------- |
| `-a`   | Archive mode                  |
| `-v`   | Verbose output                |
| `-z`   | Compress data during transfer |

For a local backup, compression is not always necessary, but `-z` is useful when transferring data over a network.

---

# 14. Task 3 - Perform the Initial Backup

The simulated SCADA data will be backed up into the laboratory backup directory.

Command:

```bash
rsync -av scada-data/ backup/scada/
```

Expected output should show files being copied.

Example:

```text
sending incremental file list
./
hmi/
hmi/config.ini
plc/
plc/plc-program.st

sent ...
received ...
```

---

# 15. Verify the Backup

List the original files:

```bash
find scada-data -type f -ls
```

List the backup files:

```bash
find backup/scada -type f -ls
```

The backup should contain equivalent files.

Expected:

```text
backup/scada/hmi/config.ini
backup/scada/plc/plc-program.st
```

---

# 16. Compare Original and Backup

Use:

```bash
diff -r scada-data backup/scada
```

If there is no output, the directory contents match.

This is a useful basic integrity check.

Expected result:

```text
No differences found
```

---

# 17. Task 4 - Demonstrate Incremental Backup

One advantage of `rsync` is that it does not necessarily copy every file again when the destination already contains identical data.

Run:

```bash
rsync -av scada-data/ backup/scada/
```

Observe the output.

The command should identify that files are already synchronized.

---

# 18. Modify Simulated HMI Configuration

Modify the HMI configuration:

```bash
nano scada-data/hmi/config.ini
```

Add or modify a value such as:

```ini
[Backup]
version=2
```

Save the file.

Check the modification:

```bash
cat scada-data/hmi/config.ini
```

---

# 19. Run rsync Again

Execute:

```bash
rsync -av scada-data/ backup/scada/
```

The modified file should be synchronized to the backup.

Verify:

```bash
cat backup/scada/hmi/config.ini
```

The backup should now contain the updated configuration.

---

# 20. Task 5 - Backup Integrity Verification

A backup is only useful if the restored data is correct.

Use:

```bash
diff -r scada-data backup/scada
```

No output indicates that the directories currently match.

Another useful check:

```bash
find scada-data -type f -printf '%p %s bytes\n'
```

and:

```bash
find backup/scada -type f -printf '%p %s bytes\n'
```

Compare the file names and sizes.

---

# 21. Task 6 - Simulate File Loss

To demonstrate recovery, simulate accidental deletion of a configuration file.

First confirm the file exists:

```bash
ls -l scada-data/hmi/config.ini
```

Remove the simulated original:

```bash
rm scada-data/hmi/config.ini
```

Verify:

```bash
ls -l scada-data/hmi/
```

The configuration file should no longer exist.

This represents a simplified example of data loss.

---

# 22. Task 7 - Recover the Deleted File

Restore the deleted configuration from the backup:

```bash
rsync -av backup/scada/hmi/config.ini scada-data/hmi/
```

Verify:

```bash
ls -l scada-data/hmi/config.ini
```

Read the restored file:

```bash
cat scada-data/hmi/config.ini
```

Expected result:

The original HMI configuration should be restored from the backup.

---

# 23. Verify Recovery

Compare the recovered directory with the backup:

```bash
diff -r scada-data backup/scada
```

No output indicates that the restored data matches the backup.

This demonstrates a basic recovery workflow:

```text
Original Data
      |
      v
   rsync
      |
      v
Backup Storage
      |
      | Data Loss
      v
Recovery Operation
      |
      v
Restored Data
```

---

# 24. Task 8 - Create a Backup Script

To automate the backup process, create:

```bash
nano scripts/backup-scada.sh
```

Example script:

```bash
#!/bin/bash

SOURCE="$HOME/SCADA-ICS-Security-101/Lab-26-ICS-SCADA-Backup-and-Recovery-Fundamentals/scada-data/"
DEST="$HOME/SCADA-ICS-Security-101/Lab-26-ICS-SCADA-Backup-and-Recovery-Fundamentals/backup/scada/"

echo "========================================"
echo " ICS/SCADA Backup"
echo "========================================"

echo "[INFO] Starting backup..."

rsync -av "$SOURCE" "$DEST"

if [ $? -eq 0 ]; then
    echo "[PASS] Backup completed successfully"
else
    echo "[FAIL] Backup failed"
    exit 1
fi
```

Save and exit.

---

# 25. Make the Script Executable

Command:

```bash
chmod +x scripts/backup-scada.sh
```

Verify:

```bash
ls -l scripts/backup-scada.sh
```

The permissions should contain an executable bit.

---

# 26. Run the Backup Script

Execute:

```bash
./scripts/backup-scada.sh
```

Expected output should contain:

```text
[INFO] Starting backup...
[PASS] Backup completed successfully
```

---

# 27. Verify Script-Based Backup

Run:

```bash
diff -r scada-data backup/scada
```

If there are no differences, the backup is synchronized.

---

# 28. Task 9 - Understand Offline Backups

An offline backup is stored on media that is disconnected from the production network or system when not actively being used.

Examples include:

* External storage
* Offline hard drives
* Removable backup media
* Isolated backup systems

## Advantages

* Reduced network exposure
* Better protection against ransomware
* Difficult for network-based malware to access
* Useful for disaster recovery

## Disadvantages

* Manual handling may be required
* Recovery can take longer
* Physical media can be damaged or lost
* Requires proper storage procedures

---

# 29. Task 10 - Understand Online Backups

An online backup remains connected to a network or backup infrastructure.

Examples include:

* Network backup servers
* NAS systems
* Cloud storage
* Enterprise backup platforms

## Advantages

* Fast access
* Convenient automation
* Easier centralized management
* Frequent backups can be scheduled

## Disadvantages

* Network exposure
* Potential ransomware impact
* Requires access control
* Backup infrastructure itself must be secured

---

# 30. Offline vs Online Backup

| Feature               | Offline Backup     | Online Backup           |
| --------------------- | ------------------ | ----------------------- |
| Network exposure      | Low                | Higher                  |
| Accessibility         | Lower              | High                    |
| Automation            | Limited            | Easy                    |
| Ransomware resistance | Strong             | Depends on architecture |
| Recovery speed        | Potentially slower | Usually faster          |
| Physical handling     | Often required     | Usually minimal         |
| ICS use               | Disaster recovery  | Operational backup      |

A mature ICS/SCADA backup strategy can use multiple backup layers rather than depending on a single method.

---

# 31. Task 11 - Cron Backup Scheduling

Linux `cron` can be used to schedule recurring administrative tasks.

Edit the user's crontab:

```bash
crontab -e
```

A daily 2:00 AM schedule could be represented as:

```text
0 2 * * * /home/ubuntu/SCADA-ICS-Security-101/Lab-26-ICS-SCADA-Backup-and-Recovery-Fundamentals/scripts/backup-scada.sh
```

Cron format:

```text
minute hour day month weekday command
```

For:

```text
0 2 * * *
```

the meaning is:

* Minute = `0`
* Hour = `2`
* Day = every day
* Month = every month
* Weekday = every weekday

Therefore:

```text
0 2 * * *
```

means every day at 02:00.

---

# 32. Verify Cron Configuration

List the current user's cron jobs:

```bash
crontab -l
```

Expected:

```text
0 2 * * * /home/ubuntu/SCADA-ICS-Security-101/Lab-26-ICS-SCADA-Backup-and-Recovery-Fundamentals/scripts/backup-scada.sh
```

If the schedule has been configured, this confirms that the backup has been registered with cron.

---

# 33. Important Cron Considerations

When using cron for security-sensitive backups:

* Use absolute paths.
* Ensure the backup script is executable.
* Ensure the destination has appropriate permissions.
* Avoid exposing credentials in scripts.
* Log backup activity.
* Monitor backup failures.
* Test recovery regularly.
* Protect the backup destination.

A scheduled backup that silently fails is not a reliable backup strategy.

---

# 34. Backup Security Considerations

ICS/SCADA backups should themselves be protected.

Important controls include:

### Access Control

Only authorized administrators should be able to modify backups.

### Least Privilege

Backup processes should use only the permissions they require.

### Network Segmentation

Backup infrastructure should not automatically have unrestricted access to control networks.

### Encryption

Sensitive backup data may require encryption at rest and during transfer.

### Offline Copies

Maintain disconnected or otherwise isolated copies where appropriate.

### Integrity Verification

Regularly verify that backup files are complete and usable.

### Recovery Testing

A backup should periodically be restored in a controlled environment to verify that it actually works.

---

# 35. Backup Strategy for ICS/SCADA

A practical strategy should consider:

```text
Critical Assets
      |
      v
Identify Data
      |
      v
Classify Criticality
      |
      v
Select Backup Method
      |
      +------------------+
      |                  |
      v                  v
Online Backup       Offline Backup
      |                  |
      +--------+---------+
               |
               v
        Integrity Check
               |
               v
        Recovery Testing
               |
               v
       Document Results
```

---

# 36. Recovery Objectives

Two important concepts in backup planning are:

## Recovery Point Objective (RPO)

RPO represents how much recent data an organization can afford to lose.

For example:

```text
RPO = 24 hours
```

means the organization may accept losing up to approximately one day's worth of changes.

## Recovery Time Objective (RTO)

RTO represents how quickly a system should be restored after an outage.

For example:

```text
RTO = 4 hours
```

means the target is to restore the required service within four hours.

ICS environments should define recovery objectives according to operational requirements and safety considerations.

---

# 37. Task Results

## Task 1 - Critical Components

**Status:** Completed / To be verified

Identified:

```text
HMI configuration
PLC program
SCADA configuration
```

---

## Task 2 - Backup Strategy

**Status:** Completed / To be verified

Reviewed:

```text
Offline backup
Online backup
Security considerations
```

---

## Task 3 - rsync Backup

**Status:** Completed / To be verified

Backup operation:

```bash
rsync -av scada-data/ backup/scada/
```

---

## Task 4 - Backup Verification

**Status:** Completed / To be verified

Verification:

```bash
diff -r scada-data backup/scada
```

Expected:

```text
No differences
```

---

## Task 5 - Recovery

**Status:** Completed / To be verified

Recovery operation:

```bash
rsync -av backup/scada/hmi/config.ini scada-data/hmi/
```

---

## Task 6 - Automated Backup

**Status:** Completed / To be verified

Backup script:

```text
scripts/backup-scada.sh
```

Cron scheduling:

```text
0 2 * * *
```

---

# 38. Evidence to Collect

The following evidence should be retained for the lab:

### Environment

```bash
cat /etc/os-release
```

### Directory Structure

```bash
find . -maxdepth 3 -type f
```

### Critical Data

```bash
find scada-data -type f
```

### Backup

```bash
rsync -av scada-data/ backup/scada/
```

### Verification

```bash
diff -r scada-data backup/scada
```

### Recovery

```bash
rsync -av backup/scada/hmi/config.ini scada-data/hmi/
```

### Script

```bash
./scripts/backup-scada.sh
```

### Cron

```bash
crontab -l
```

---

# 39. Troubleshooting

## rsync: command not found

Install rsync:

```bash
sudo apt update
sudo apt install -y rsync
```

Verify:

```bash
rsync --version
```

---

## Permission Denied

Check directory ownership:

```bash
ls -ld scada-data backup
```

Check file permissions:

```bash
ls -la scada-data
```

Avoid changing permissions unnecessarily.

---

## Backup Directory Does Not Exist

Create it:

```bash
mkdir -p backup/scada
```

Then retry:

```bash
rsync -av scada-data/ backup/scada/
```

---

## Script Permission Denied

Make the script executable:

```bash
chmod +x scripts/backup-scada.sh
```

Then:

```bash
./scripts/backup-scada.sh
```

---

## Cron Job Not Visible

Check:

```bash
crontab -l
```

If no jobs are configured, edit:

```bash
crontab -e
```

---

# 40. Skills Practiced

This laboratory developed practical knowledge of:

* ICS/SCADA asset identification
* HMI configuration protection
* PLC program protection
* Backup architecture
* Offline backup concepts
* Online backup concepts
* Linux `rsync`
* File synchronization
* Backup verification
* File recovery
* Bash scripting
* Cron scheduling
* Recovery planning
* RPO and RTO
* Defensive ICS security
* Operational resilience

---

# 41. Key Takeaways

1. ICS/SCADA systems depend on critical configuration and control data.
2. HMI and PLC information should be treated as important backup assets.
3. `rsync` provides a simple method for synchronizing backup data.
4. Backup verification is essential.
5. A backup is not considered reliable until recovery has been tested.
6. Offline backups provide additional protection against network-based threats.
7. Online backups provide convenient and automated protection.
8. Backup systems themselves must be secured.
9. Cron can automate recurring backup operations.
10. Recovery objectives should be considered when designing an ICS/SCADA backup strategy.
11. Multiple backup layers provide better resilience than relying on a single backup copy.
12. Backup and recovery procedures should be documented and tested regularly.

---

# 42. Lab Completion Checklist

* [ ] Ubuntu environment verified
* [ ] Lab directory verified
* [ ] Simulated HMI configuration created
* [ ] Simulated PLC program created
* [ ] Critical ICS/SCADA files identified
* [ ] `rsync` installed and verified
* [ ] Initial backup created
* [ ] Backup contents verified
* [ ] Original and backup compared
* [ ] Incremental backup tested
* [ ] Simulated file deletion performed
* [ ] Deleted file successfully recovered
* [ ] Backup script created
* [ ] Backup script tested
* [ ] Offline backup strategy reviewed
* [ ] Online backup strategy reviewed
* [ ] Cron scheduling configured
* [ ] Cron configuration verified
* [ ] Backup security considerations documented
* [ ] Recovery process documented
* [ ] Evidence collected
* [ ] `lab-notes.md` updated
* [ ] Changes committed to Git
* [ ] Changes pushed to GitHub

---

# 43. Final Conclusion

This laboratory demonstrated the fundamentals of backup and recovery for ICS/SCADA environments.

A simulated HMI and PLC environment was used to identify critical configuration data. `rsync` was then used to create and synchronize a backup. Backup integrity was checked, and a deleted configuration file was restored from the backup to demonstrate a basic recovery process.

The laboratory also examined the differences between online and offline backups and demonstrated how `cron` can be used to automate recurring backup operations.

The most important lesson is that **backup alone is not enough**. A reliable ICS/SCADA resilience strategy must include secure storage, integrity verification, appropriate access control, documented procedures, and regular recovery testing.

A properly designed backup and recovery process helps reduce downtime, improve resilience, and support safe recovery following accidental deletion, hardware failure, malware, ransomware, or other disruptive events.

---

# 44. Final Lab Status

**Lab:** Lab 26 - ICS/SCADA Backup and Recovery Fundamentals

**Documentation:** `README.md` + `lab-notes.md`

**Practical:** Backup, verification, recovery, scripting, and scheduling

**Final Status:** Complete only after all practical checklist items have been executed and verified.
