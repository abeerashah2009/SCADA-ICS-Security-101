# Lab 08: Windows vs. Industrial OS Basics

## Lab Overview

This lab explores the differences between standard desktop operating systems and operating systems commonly encountered in Industrial Control System (ICS) environments.

The lab focuses on Windows-based systems, Linux-based systems, and Real-Time Operating Systems (RTOS), with particular attention to security, reliability, lifecycle, patch management, and operational availability.

---

## Objectives

By completing this lab, I will:

- Understand the differences between Windows and industrial operating systems.
- Identify operating systems commonly used in ICS environments.
- Understand the role of RTOS in industrial systems.
- Compare the security posture of ICS operating systems with standard desktop operating systems.
- Understand ICS patch-management challenges.
- Understand the importance of compatibility testing.
- Understand the role of redundancy and maintenance windows.
- Apply safe security practices in an industrial environment.

---

## Prerequisites

- Basic understanding of operating systems.
- Basic understanding of computer networking.
- Basic understanding of Industrial Control Systems (ICS).
- Basic Linux command-line knowledge.

---

# Task 1: Identify Operating Systems Used in ICS

## 1.1 Windows-Based Industrial Systems

Windows operating systems have historically been used in many industrial environments.

Common applications include:

- Human-Machine Interfaces (HMIs)
- SCADA servers
- Engineering workstations
- Industrial PCs
- Supervisory applications

Older Windows versions may still exist in some industrial environments because ICS equipment often has long operational lifecycles.

### Security Consideration

Unsupported operating systems may no longer receive normal security updates.

This can increase security risk and requires additional compensating controls.

---

## 1.2 Windows XP Embedded

Windows XP Embedded was designed for embedded and specialized systems.

It may be encountered when studying legacy industrial environments.

Important considerations include:

- Legacy software dependencies
- Compatibility requirements
- Limited patching options
- Long equipment lifecycles
- Increased security risk

---

## 1.3 Real-Time Operating Systems (RTOS)

RTOS stands for Real-Time Operating System.

An RTOS is designed to provide predictable responses to events.

RTOS environments are useful when timing and deterministic behavior are important.

Important characteristics include:

- Predictable response time
- Deterministic behavior
- Task scheduling
- Real-time processing
- Reliability

RTOS platforms may be used in embedded and safety-critical systems.

---

## 1.4 Linux-Based Industrial Systems

Linux is also widely used in industrial and embedded environments.

Advantages include:

- Open-source ecosystem
- Flexibility
- Customization
- Strong networking capabilities
- Large software ecosystem

Linux can be used for:

- SCADA servers
- Industrial gateways
- Embedded systems
- Monitoring systems
- Network appliances

---

# Task 2: Compare ICS and Standard Desktop Operating Systems

## ICS Operating Systems

ICS environments commonly prioritize:

1. Safety
2. Availability
3. Reliability
4. Deterministic behavior
5. Integrity

A failure in an industrial system may affect a physical process.

---

## Standard Desktop Operating Systems

Traditional desktop systems commonly prioritize:

- General productivity
- Application compatibility
- Security updates
- User experience
- General-purpose computing

---

## Comparison

| Feature | ICS Environment | Standard Desktop |
|---|---|---|
| Primary Focus | Safety, availability, reliability | Productivity and general computing |
| Lifecycle | Often long | Usually shorter |
| Updates | Controlled and tested | Frequent |
| Downtime | Potentially very costly | Usually easier to schedule |
| Applications | Specialized | General purpose |
| Hardware | May be specialized | General purpose |
| Patch Management | Carefully controlled | Regularly performed |

---

# Task 3: Patch Management in ICS

Patch management is the process of identifying, testing, approving, and installing software updates.

Updates may fix:

- Security vulnerabilities
- Software bugs
- Compatibility issues
- Performance problems

---

## Why ICS Patching Is Different

ICS systems cannot always be patched immediately.

Reasons include:

### 1. Compatibility

A patch may interfere with:

- HMI software
- SCADA applications
- Drivers
- PLC communication
- Specialized hardware

### 2. Downtime

Industrial processes may need to operate continuously.

Taking a system offline for maintenance may interrupt production.

### 3. Testing Requirements

Security updates should ideally be tested before deployment.

### 4. Vendor Dependencies

Industrial systems may depend on specific vendor-supported software versions.

---

# Task 4: Safe ICS Patch Management Process

A controlled patch-management process can follow these stages:

```text
Identify Patch
      |
      v
Risk Assessment
      |
      v
Compatibility Review
      |
      v
Test in Laboratory
      |
      v
Backup / Recovery Preparation
      |
      v
Maintenance Window
      |
      v
Deploy Patch
      |
      v
Verify System
      |
      v
Monitor
## Task 5: Redundancy

-Redundancy means having additional systems available to maintain operations if a primary system becomes unavailable.

-Example:

SCADA Server A
      |
      | Active
      v
Industrial Process


SCADA Server B
      |
      | Standby
      v
Available for Failover

Redundancy can help organizations perform maintenance while maintaining service availability.

## Task 6: ICS Security Challenges

Industrial environments may contain:

- Legacy operating systems
- Unsupported software
- Long equipment lifecycles
- Specialized applications
- Vendor dependencies
- Limited maintenance windows
- Safety requirements
- Availability requirements

- These characteristics make ICS security different from ordinary desktop security.

## Task 7: Practical Lab Environment

- This laboratory is performed on an Ubuntu Linux system running in an AWS EC2 environment.

- The system used for this exercise is a normal cloud Linux system.

- It is not a real industrial control system.

- Therefore, the practical exercises demonstrate operating-system concepts and security principles rather than modifying a real ICS environment.

## Task 8: Security Considerations

- Industrial systems must not be modified, scanned, patched, or tested without authorization.

Before making changes to a real ICS environment:

- Obtain authorization.
- Review the proposed change.
- Perform compatibility testing.
- Prepare backups.
- Prepare a recovery plan.
- Coordinate with system operators.
- Use an approved maintenance window.
- Verify system operation after the change.
Key Terms
- ICS

- Industrial Control System.

- RTOS

Real-Time Operating System.

- SCADA

- Supervisory Control and Data Acquisition.

- HMI

- Human-Machine Interface.

- Patch

- A software update that may fix bugs or security vulnerabilities.

- Legacy System

- An older system that remains operational.

- Redundancy

- Using additional systems to maintain availability if a primary system fails.

- Deterministic

- Predictable behavior, particularly predictable response timing.

Lab Safety

- This laboratory uses a controlled cloud environment.

- No real industrial devices or industrial processes should be contacted.

- All testing should be performed only on systems that are owned by the learner or for which explicit authorization has been provided.

Learning Outcomes

- After completing this lab, I should be able to:

- Explain the role of operating systems in ICS environments.
- Describe Windows-based industrial systems.
- Explain the purpose of RTOS.
- Describe the use of Linux in industrial environments.
- Compare ICS and desktop operating-system security.
- Explain why ICS patching requires additional planning.
- Describe the importance of testing and compatibility.
- Explain how redundancy supports availability.
- Apply safe security practices when working with ICS environments.
Conclusion

- This lab demonstrates that operating-system management in ICS environments differs significantly from ordinary desktop environments.

- ICS systems often have long lifecycles and specialized applications. As a result, security updates must be carefully evaluated, tested, and deployed.

Effective ICS security requires balancing:

- Safety
- Availability
- Reliability
- Integrity
- Security
- Compatibility

- A controlled and well-tested approach helps improve security while reducing the risk of disrupting industrial operations.
