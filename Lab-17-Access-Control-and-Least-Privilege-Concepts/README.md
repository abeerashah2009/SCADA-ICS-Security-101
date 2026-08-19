# Lab 17: Access Control and Least Privilege Concepts

## Overview

This laboratory demonstrates access control and the principle of
least privilege in a simulated Industrial Control System (ICS)
environment.

Linux users and groups were used to represent different ICS roles.
Filesystem permissions were then configured to ensure that each role
could access only the resources required for its responsibilities.

## Lab Objectives

- Understand access control in an ICS environment
- Understand the principle of least privilege
- Create role-based Linux groups
- Create simulated ICS user accounts
- Assign filesystem permissions based on roles
- Test authorized and unauthorized actions
- Document access-control results

## Simulated ICS Roles

| Role | Responsibility |
|------|----------------|
| Operator | Monitor ICS process information |
| Engineer | Read and modify ICS configuration |

## Linux Groups

Two role-based groups were created:

```text
operators
engineers
Users:

operator1  → operators
engineer1  → engineers
ICS Resources

Two simulated ICS directories were created:

/var/ics/config
/var/ics/monitor
Configuration Directory
Owner: root
Group: engineers
Permissions: 770

Engineers were granted read/write access to configuration data.

Monitoring Directory
Owner: root
Group: operators
Permissions: 750

Operators were granted access to monitoring data.

Access Control Testing
Operator

The operator successfully accessed monitoring data:

Water Plant Status: NORMAL

The operator was denied access to configuration data:

Permission denied

The operator was also prevented from modifying configuration:

Permission denied
Engineer

The engineer successfully read the configuration:

Initial ICS Configuration

The engineer successfully modified the configuration:

Updated Config Value

The engineer was denied access to operator monitoring data:

Permission denied
Results
Role	Monitoring Data	Configuration Data
Operator	READ	DENIED
Engineer	DENIED	READ/WRITE
Security Concept Demonstrated

The laboratory demonstrates least privilege.

Each user received only the permissions necessary for their
assigned role.

This reduces the possibility of unauthorized changes to sensitive
ICS resources.

Technologies Used
Ubuntu Linux
Linux users and groups
Linux filesystem permissions
chmod
chown
useradd
groupadd
sudo
ICS/SCADA security concepts
Evidence

Detailed commands, outputs, permission tests, and observations are
documented in:

lab-notes.md
Safety

All testing was performed in an authorized educational laboratory
environment.

No production ICS or SCADA systems were accessed or modified.

Conclusion

This laboratory provided practical experience with role-based
access control and least privilege.

The permission tests demonstrated that operators could perform
monitoring activities without accessing configuration resources,
while engineers could manage configuration data without accessing
operator monitoring resources.

The lab demonstrates how Linux permissions can be used to model
basic access-control concepts applicable to ICS/SCADA environments.
