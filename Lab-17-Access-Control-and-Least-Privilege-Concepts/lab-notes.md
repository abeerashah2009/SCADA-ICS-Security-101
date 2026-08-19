# Lab 17: Access Control and Least Privilege Concepts

## 1. Lab Objective

The objective of this laboratory was to understand access control
and the principle of least privilege in an ICS environment.

The laboratory simulated two roles:

- Operator
- Engineer

The operator was given limited access to monitoring data.
The engineer was given access to modify ICS configuration data.

---

## 2. User Roles

### Operator

Responsibilities:

- Monitor ICS information
- Read monitoring data
- No permission to modify configuration

### Engineer

Responsibilities:

- Monitor ICS information
- Modify ICS configuration
- Maintain system configuration

---

## 3. Groups Created

The following Linux groups were created:

- operators
- engineers

Commands used:

    sudo groupadd operators
    sudo groupadd engineers

Status:

[PASS] Operator group created
[PASS] Engineer group created

---

## 4. Users Created

Users created:

- operator1
- engineer1

Commands:

    sudo useradd -m -G operators operator1
    sudo useradd -m -G engineers engineer1

Verification:

    id operator1
    id engineer1

Status:

[PASS] operator1 assigned to operators
[PASS] engineer1 assigned to engineers

---

## 5. ICS Directories

The following directories were created:

    /var/ics/config
    /var/ics/monitor

Configuration data was stored in:

    /var/ics/config/config.txt

Monitoring data was stored in:

    /var/ics/monitor/status.txt

Status:

[PASS] ICS directories created
[PASS] Sample ICS files created

---

## 6. Access Permissions

Configuration directory:

    /var/ics/config

Owner:

    root

Group:

    engineers

Permissions:

    770

This allows engineers to access and modify configuration data.

Monitoring directory:

    /var/ics/monitor

Owner:

    root

Group:

    operators

Permissions:

    750

This allows operators to read monitoring information.

Status:

[PASS] Configuration permissions configured
[PASS] Monitoring permissions configured

---

## 7. Operator Access Test

Command:

    sudo -u operator1 cat /var/ics/monitor/status.txt

Result:

Monitoring data was successfully displayed.

Observation:

The operator can read monitoring information.

Status:

[PASS] Operator read access verified

---

## 8. Unauthorized Configuration Test

Command:

    sudo -u operator1 sh -c 'echo "Unauthorized Config Change" > /var/ics/config/config.txt'

Result:

Permission denied.

Observation:

The operator was prevented from modifying ICS configuration.

This demonstrates least privilege.

Status:

[PASS] Unauthorized configuration modification blocked

---

## 9. Engineer Access Test

Command:

    sudo -u engineer1 sh -c 'echo "Updated Config Value" > /var/ics/config/config.txt'

Result:

Configuration was successfully updated.

Verification:

    sudo cat /var/ics/config/config.txt

Result:

    Updated Config Value

Observation:

The engineer has the required permission to modify ICS
configuration data.

Status:

[PASS] Engineer configuration access verified

---

## 10. Least Privilege Verification

The laboratory demonstrated that each role received only the
permissions required for its responsibilities.

Operator:

- Read monitoring data: ALLOWED
- Modify configuration: DENIED

Engineer:

- Modify configuration: ALLOWED

This prevents users from performing actions outside their
responsibilities.

---

## 11. Security Analysis

Access control is important in ICS/SCADA environments because
unauthorized changes can affect industrial processes.

Least privilege reduces risk by limiting user permissions.

Examples:

- Operators should not modify critical configurations.
- Engineers may require configuration write access.
- Administrative privileges should be limited to authorized
  administrators.

Role-based permissions can reduce accidental and unauthorized
changes.

---

## 12. Final Results

[PASS] Access control concepts understood

[PASS] Operator role created

[PASS] Engineer role created

[PASS] Operator monitoring access verified

[PASS] Operator configuration modification blocked

[PASS] Engineer configuration modification allowed

[PASS] Least privilege demonstrated

---

## 13. Conclusion

This laboratory demonstrated access control and least privilege
using Linux users, groups, and file permissions.

The operator received limited monitoring access while the engineer
received configuration access.

The unauthorized operator configuration attempt was blocked,
demonstrating that least privilege can prevent users from
performing actions outside their assigned responsibilities.

---

# 19. Practical Access Control Testing

## 19.1 Operator Access Test

Command:

sudo -u operator1 cat /var/ics/monitor/status.txt

Result:

Water Plant Status: NORMAL

Status:

[PASS] Operator can read monitoring data.

---

## 19.2 Operator Configuration Access Test

Command:

sudo -u operator1 cat /var/ics/config/config.txt

Result:

Permission denied

Status:

[PASS] Operator cannot read ICS configuration.

---

## 19.3 Operator Unauthorized Modification Test

Command:

sudo -u operator1 sh -c 'echo "Unauthorized Config Change" > /var/ics/config/config.txt'

Result:

Permission denied

Status:

[PASS] Operator cannot modify ICS configuration.

---

## 19.4 Engineer Configuration Access Test

Command:

sudo -u engineer1 cat /var/ics/config/config.txt

Result:

Initial ICS Configuration

Status:

[PASS] Engineer can read ICS configuration.

---

## 19.5 Engineer Configuration Modification Test

Command:

sudo -u engineer1 sh -c 'echo "Updated Config Value" > /var/ics/config/config.txt'

Result:

Configuration updated successfully.

Verification:

sudo cat /var/ics/config/config.txt

Result:

Updated Config Value

Status:

[PASS] Engineer can modify ICS configuration.

---

## 19.6 Engineer Monitoring Access Test

Command:

sudo -u engineer1 cat /var/ics/monitor/status.txt

Result:

Permission denied

Status:

[PASS] Engineer cannot access operator monitoring data.

---

# 20. Access Control Results

| Role | Monitoring Data | Configuration Data |
|------|-----------------|--------------------|
| Operator | READ | DENIED |
| Engineer | DENIED | READ/WRITE |

The practical tests demonstrated that users received only the
permissions required for their assigned roles.

The operator could read monitoring information but could not access
or modify configuration data.

The engineer could read and modify configuration data but could not
access the operator monitoring directory.

---

# 21. Least Privilege Demonstration

The laboratory successfully demonstrated the principle of least
privilege using Linux groups and filesystem permissions.

Access was controlled using:

- Linux user accounts
- Linux groups
- Directory ownership
- File permissions
- Group-based authorization

Unauthorized operations returned "Permission denied", while
authorized operations succeeded.

---

# 22. Final Conclusion

This laboratory demonstrated role-based access control and the
principle of least privilege in a simulated ICS environment.

The operator was restricted to monitoring activities, while the
engineer was granted access to configuration data.

The permission tests confirmed that users could not perform actions
outside their assigned responsibilities.

Least privilege reduces the risk of unauthorized changes and helps
protect sensitive ICS/SCADA resources.
