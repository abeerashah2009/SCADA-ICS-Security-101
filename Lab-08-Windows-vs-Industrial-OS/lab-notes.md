# Lab 08 Notes: Windows vs. Industrial OS Basics

## 1. Lab Information

**Lab Number:** 08

**Lab Name:** Windows vs. Industrial OS Basics

**Category:** ICS/SCADA Security Fundamentals

**Environment:** Ubuntu Linux on AWS EC2

**Purpose:** Understand operating systems used in ICS environments and compare their security and maintenance requirements with standard desktop operating systems.

---

# 2. Lab Objectives

The objectives of this lab are to:

- Understand the differences between Windows and industrial operating systems.
- Identify operating systems commonly encountered in ICS environments.
- Understand the purpose of Real-Time Operating Systems (RTOS).
- Understand the role of Linux in industrial environments.
- Compare ICS operating-system security with standard desktop operating systems.
- Understand the challenges of patching industrial systems.
- Understand compatibility and downtime concerns.
- Understand redundancy and maintenance windows.
- Practice identifying the operating system of the current laboratory machine.

---

# 3. What is an Operating System?

An Operating System (OS) is system software that manages computer hardware and provides services for applications.

Examples include:

- Microsoft Windows
- Linux
- Unix
- Real-Time Operating Systems (RTOS)

An operating system manages resources such as:

- CPU
- Memory
- Storage
- Network interfaces
- Processes
- Users
- Hardware devices

In an ICS environment, an operating system may run on:

- SCADA servers
- HMIs
- Engineering workstations
- Industrial PCs
- Monitoring systems
- Industrial gateways
- Embedded systems

---

# 4. Why Operating Systems Matter in ICS

Operating systems are important security components because vulnerabilities in an OS can affect applications and services running on top of it.

For example:

```text
Operating System
       |
       +--- SCADA Software
       |
       +--- HMI Application
       |
       +--- Network Services
       |
       +--- Monitoring Tools
# 5. Windows in Industrial Environments

Windows has historically been widely used in industrial environments.

Common applications include:

- Human-Machine Interfaces (HMIs)
- SCADA servers
- Engineering workstations
- Industrial PCs
- Supervisory applications

Windows is often used because many industrial applications were designed specifically for Windows.

# 6. Windows XP Embedded

Windows XP Embedded was designed for embedded and specialized systems.

It may be encountered when studying legacy industrial environments.

Potential reasons for continued use of older systems include:

- Long equipment lifecycles
- Specialized applications
- Vendor dependencies
- Compatibility requirements
- Expensive replacement costs
- Limited maintenance windows
---
# 7. Security Concerns with Legacy Windows

Legacy operating systems can create security challenges.

Examples include:

- Unsupported software
- Missing security updates
- Old protocols
- Older authentication mechanisms
- Compatibility limitations
- Difficult replacement processes

A legacy system should not simply be disconnected or upgraded without considering the industrial process that depends on it.

Security teams may need compensating controls such as:

- Network segmentation
- Firewalls
- Access restrictions
- Application allowlisting
- Monitoring
- Controlled administrative access
---
# 8. Real-Time Operating System (RTOS)

RTOS stands for:

- Real-Time Operating System

An RTOS is designed to provide predictable responses to events.

Timing can be extremely important in systems that interact with physical processes.

Important characteristics include:

- Predictable response time
- Deterministic behavior
- Task scheduling
- Real-time processing
- Reliability
---
# 9. Deterministic Behavior

Deterministic behavior means that system responses can be predicted within defined timing requirements.

Example:

Sensor Event
     |
     v
Controller Receives Event
     |
     v
Process Decision
     |
     v
Actuator Response

In some industrial applications, predictable timing is critical.
----

# 10. Linux in Industrial Environments

Linux is also used in industrial and embedded environments.

Advantages include:

- Open-source ecosystem
- Flexibility
- Customization
- Strong networking capabilities
- Large software ecosystem
- Automation support

Linux may be used for:

- SCADA servers
- Industrial gateways
- Embedded systems
- Monitoring systems
- Network appliances
- Data collection systems
---
# 11. ICS Operating Systems vs Desktop Operating Systems

ICS environments and traditional desktop environments have different operational priorities.

ICS Environment

Common priorities include:

- Safety
- Availability
- Reliability
- Deterministic behavior
- Integrity
- Desktop Environment

Traditional desktop environments commonly prioritize:     

- Productivity
- Security
-Application compatibility
- User experience
- General-purpose computing

The exact priorities can vary depending on the system and organization.
---

# 12. Comparison Table
Feature 	   ICS Environment	                       Standard Desktop
Primary Focus 	  Safety, availability, reliability	Productivity and general computing
Lifecycle	  Often long	                        Usually shorter
Updates   	  Controlled and tested           	Frequent
Downtime	  Potentially very costly	         Usually easier to schedule
Applications	  Specialized	                        General purpose
Hardware 	  May be specialized             	General purpose
Patch Management  Carefully controlled	                Regularly performed
Testing	          Extensive before deployment	        Usually less restrictive
---
# 13. Patch Management

Patch management is the process of identifying, evaluating, testing, approving, and installing software updates.

Patches may fix:

Security vulnerabilities
Software bugs
Compatibility problems
Performance issues

Patch management is an important part of cybersecurity.
---
# 14. Why ICS Patching Is Different

In a normal desktop environment, installing a security update may be relatively straightforward.

In an ICS environment, the same update may affect:

- HMI software
- SCADA applications
- PLC communication
- Drivers
- Specialized hardware
- Industrial protocols

Therefore, patches should be evaluated before deployment.
---

# 15. Patch Management Challenge: Compatibility

Compatibility is an important concern.

An operating-system update may change:

- Drivers
- Libraries
- Network behavior
- Authentication
- Application dependencies

A patch that is safe for a normal desktop may not necessarily be safe for a specialized industrial system.
---

# 16. Patch Management Challenge: Downtime

Industrial processes may need to operate continuously.

Taking a system offline can potentially result in:

Production interruption
Loss of monitoring
Loss of control
Reduced availability
Operational impact

Therefore, patching may need to occur during an approved maintenance window.
---

# 17. Patch Management Challenge: Testing

Testing helps determine whether a patch works correctly before deployment.

A controlled process may use:

Production System
       |
       | Configuration Copy
       v
Test Environment
       |
       v
Install Patch
       |
       v
Verify Applications
       |
       v
Verify Communications
       |
       v
Approve Deployment

Testing can reduce the risk of unexpected problems.
---

# 18. Vendor Compatibility

Industrial systems often depend on vendor-specific applications and hardware.

Before applying an important update, organizations may need to verify:

Vendor support
Application compatibility
Driver compatibility
Protocol compatibility
Hardware support
Recovery procedures
---

# 19. Maintenance Windows

A maintenance window is an approved period during which maintenance activities can be performed.

A typical maintenance process may include:

Plan
  |
  v
Backup
  |
  v
Maintenance Window
  |
  v
Apply Update
  |
  v
Verify System
  |
  v
Monitor
---

# 20. Redundancy

Redundancy means having additional systems available to maintain operations if one system becomes unavailable.

Example:

SCADA Server A
     |
     | Active
     v
Industrial Process


SCADA Server B
     |
     | Standby
     v
Failover System

Redundancy can help organizations perform maintenance while maintaining availability.
---

# 21. Legacy Systems

A legacy system is an older system that remains in operation.

ICS environments may contain legacy systems because industrial equipment can remain operational for many years.

Legacy systems can be difficult to replace because of:

- Cost
- Compatibility
- Vendor dependencies
- Downtime requirements
- Specialized hardware
- Operational risk
---

# 22. Compensating Security Controls

When a legacy system cannot be patched immediately, organizations may use compensating controls.

Examples include:

Network Segmentation

Place the system in a restricted network zone.

Firewall Rules

Allow only required communication.

Access Control

Restrict administrative access.

Monitoring

Monitor network and system activity.

Application Allowlisting

Allow only approved applications to execute where appropriate.
---

# 23. Current Lab Environment

This laboratory is being performed on an AWS EC2 instance.

The machine is a normal Linux cloud system.

It is not a real industrial controller.

The purpose of this exercise is to understand operating-system and ICS security concepts in a controlled environment.
---

# 24. Practical Environment Identification

The first practical step is to identify the current operating system.

- Command:

uname -a

Purpose:

Display kernel and system information.

Example:

Linux hostname 6.x.x-xxxx-aws #... x86_64 GNU/Linux

The exact output depends on the laboratory environment.

---

# 25. Understanding uname

- The command:

uname

displays basic system information.

The option:

-a

means:

all available information

Therefore:

uname -a

provides a broader view of the current system.

---

# 26. Operating System Information

- Another useful command is:

cat /etc/os-release

Purpose:

Display Linux distribution information.

Typical information includes:

Distribution name
Version
Release information
Distribution identifier
---

# 27. Kernel Information

- Command:

uname -r

Purpose:

Display the Linux kernel release.

The kernel is the core component of the operating system.

---

# 28. Architecture Information

- Command:

uname -m

Purpose:

Display the machine hardware architecture.

Example:

x86_64

This indicates a 64-bit x86 architecture.
---

# 29. Hostname Identification

- Command:

hostname

Purpose:

Display the hostname of the current machine.

A hostname can help administrators identify systems within an environment.
---

# 30. System Information Summary

- The following commands can be used together:

uname -a
cat /etc/os-release
uname -r
uname -m
hostname

These commands provide useful information about the laboratory operating system.

---
# 31. Security Importance of OS Identification

Operating-system identification helps security teams understand:

What platform is running
Which software family is being used
What patching strategy may apply
What security controls are appropriate
Whether the system may be legacy
What compatibility issues may exist

Asset identification is an important part of security management.
---

# 32. Safe Lab Principle

This lab is performed only against the current laboratory machine.

No real industrial systems should be modified.

No production ICS environment should be patched or changed as part of this exercise.

All security testing should be authorized.
---

# 33. Important ICS Security Principle

ICS security is not simply:

Install Every Patch Immediately

Instead, the process is closer to:

Identify
   |
   v
Assess Risk
   |
   v
Test
   |
   v
Approve
   |
   v
Schedule
   |
   v
Deploy
   |
   v
Verify
   |
   v
Monitor

This balances security with operational requirements.
---

# 34. Practical Lab Tasks

The following tasks will be performed in this laboratory.

Task 1: Identify the Operating System

Command:

uname -a

Goal:

Identify the kernel and system architecture.

Task 2: Identify the Linux Distribution

Command:

cat /etc/os-release

Goal:

Identify the operating-system distribution and version.

Task 3: Identify Kernel Version

Command:

uname -r

Goal:

Identify the running Linux kernel version.

Task 4: Identify Architecture

Command:

uname -m

Goal:

Identify the machine architecture.

Task 5: Identify Hostname

Command:

hostname

Goal:

Identify the hostname of the laboratory system.
---

# 35. Evidence Collection

Important command output should be saved as evidence.

Example:

uname -a | tee os-identification-results.txt

Additional information can be collected using:

cat /etc/os-release | tee -a os-identification-results.txt
uname -r | tee -a os-identification-results.txt
uname -m | tee -a os-identification-results.txt
hostname | tee -a os-identification-results.txt

The -a option with tee appends output instead of replacing the existing file.

36. Why Evidence Matters

Saving results demonstrates that the lab was actually performed.

Instead of only documenting:

Linux is an operating system.

The portfolio can demonstrate:

Command
   |
   v
Actual System Output
   |
   v
Interpretation

---

# 37. Expected Lab Evidence

The final lab directory may contain:

README.md
lab-notes.md
os-check.sh
os-identification-results.txt

The exact files depend on the practical tasks performed.
---

# 38. Key Terms
Operating System

Software that manages computer hardware and provides services for applications.

ICS

Industrial Control System.

SCADA

Supervisory Control and Data Acquisition.

HMI

Human-Machine Interface.

RTOS

Real-Time Operating System.

Legacy System

An older system that remains in operation.

Patch

A software update that may fix bugs or security vulnerabilities.

Patch Management

The controlled process of evaluating, testing, approving, and installing patches.

Redundancy

Additional systems used to maintain availability.

Deterministic

Predictable system behavior, especially predictable timing.

Maintenance Window

An approved period for performing system maintenance.

Compensating Control

A security measure used to reduce risk when the preferred security control cannot be applied.
---

# 39. Interview Questions
Q1. What is an RTOS?

An RTOS is a Real-Time Operating System designed to provide predictable responses to events and tasks.

Q2. Why are legacy operating systems common in ICS?

ICS equipment often has long operational lifecycles and may depend on specialized applications and hardware.

Q3. Why can't ICS systems always be patched immediately?

Patching can cause compatibility problems or downtime and may affect critical industrial processes.

Q4. What is patch management?

Patch management is the controlled process of identifying, evaluating, testing, approving, and deploying software updates.

Q5. Why is testing important before patching an ICS?

Testing helps determine whether the update affects industrial applications, drivers, communication, or system stability.

Q6. What is redundancy?

Redundancy means having additional systems available to maintain operations if a primary system becomes unavailable.

Q7. What is a legacy system?

A legacy system is an older system that remains in operation.

Q8. What is the purpose of network segmentation for legacy systems?

Segmentation can restrict communication and reduce the potential impact of a compromised legacy system.

Q9. What does uname -a do?

It displays detailed kernel and system information.

Q10. What does cat /etc/os-release show?

It displays Linux distribution and release information.

---

# 40. Security Best Practices

When managing ICS operating systems:

Maintain an accurate asset inventory.
Identify operating-system versions.
Track software dependencies.
Review vendor guidance.
Test patches before deployment.
Use approved maintenance windows.
Maintain backups.
Maintain recovery procedures.
Restrict unnecessary network access.
Monitor important systems.
Use network segmentation.
Avoid unauthorized scanning or modification.
---

# 41. Key Takeaways

Remember:

Operating System

Manages hardware and provides services for applications.

Windows

Widely used historically for HMIs, SCADA servers, and engineering workstations.

Linux

Flexible operating system used in many industrial and embedded applications.

RTOS

Designed for predictable real-time behavior.

ICS

Often prioritizes safety, availability, reliability, and process stability.

Legacy System

An older system that remains operational.

Patch Management

A controlled process for applying software updates.

Redundancy

Additional systems used to maintain availability.

Maintenance Window

Approved period for maintenance activities.

Asset Identification

Knowing what operating systems and devices exist is essential for security management.

---

# 42. Lab Conclusion

This laboratory demonstrates the fundamental differences between standard desktop operating systems and operating systems used in industrial environments.

ICS environments often have long operational lifecycles, specialized applications, and strict availability requirements.

As a result, operating-system security cannot always be managed in exactly the same way as a normal desktop computer.

A secure ICS operating-system strategy should balance:

Safety
Availability
Reliability
Integrity
Security
Compatibility

The practical commands in this lab demonstrate how to identify the operating system and basic system characteristics of a controlled Linux laboratory environment.

The exercise does not interact with real industrial equipment.
