
---

# 23. Permission and Ownership Evidence

## Directory Permissions

Command:

sudo ls -ld /var/ics/config /var/ics/monitor

Expected configuration:

- `/var/ics/config` → owner: root, group: engineers, permissions: 770
- `/var/ics/monitor` → owner: root, group: operators, permissions: 750

## File Permissions

Command:

sudo ls -l /var/ics/config/config.txt /var/ics/monitor/status.txt

This evidence confirms that the ICS resources are owned and
controlled according to the assigned user roles.

Status:

[PASS] Ownership and permission configuration verified.

---

# 24. Lab Completion

The access-control implementation, authorization tests,
least-privilege validation, documentation, and permission evidence
were successfully completed.

Status:

[PASS] Lab 17 completed.
