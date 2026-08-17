# Lab 05 Notes: Virtual ICS/SCADA Lab Environment

## 1. What is Virtualization?

Virtualization allows one physical computer to run multiple isolated virtual computers called Virtual Machines (VMs).

Example:

Physical Computer
       |
       +--- VM 1
       |
       +--- VM 2
       |
       +--- VM 3

Each VM can have its own:

- Operating system
- CPU allocation
- Memory
- Storage
- Network interface

---

## 2. What is a Hypervisor?

A hypervisor is software or technology that manages Virtual Machines.

Two common types are:

### Type 1 Hypervisor

Runs directly on physical hardware.

Examples:

- VMware ESXi
- Microsoft Hyper-V
- KVM-based virtualization

### Type 2 Hypervisor

Runs on top of an operating system.

Examples:

- VirtualBox
- VMware Workstation

---

## 3. Why Virtualization is Useful for ICS/SCADA

ICS/SCADA environments contain many different systems.

A virtual laboratory can simulate:

- SCADA servers
- HMIs
- PLC environments
- Engineering workstations
- Network monitoring systems
- Security testing machines

Instead of buying physical industrial equipment, students can use virtual machines for learning and experimentation.

---

## 4. Current Lab Environment

This lab is running inside an AWS EC2 instance.

The environment discovery showed:

- Operating System: Ubuntu 24.04
- Environment: Amazon EC2
- Hypervisor: KVM
- Virtualization type: Full virtualization
- `/dev/kvm`: Not available

This means the current machine is already a virtual machine.

---

## 5. What is Nested Virtualization?

Nested virtualization means running a virtual machine inside another virtual machine.

Example:

Physical Server
      |
      +--- VM / EC2
             |
             +--- VirtualBox
                    |
                    +--- ICS VM

Nested virtualization requires the underlying environment to expose the required virtualization capabilities.

---

## 6. Why VirtualBox Was Not Installed

The original lab instructions recommend installing VirtualBox and creating another VM.

However, the current EC2 environment does not expose `/dev/kvm`.

Therefore, installing and running VirtualBox inside this EC2 instance is not an appropriate approach for this lab.

The environment discovery itself is an important practical result.

---

## 7. Recommended ICS/SCADA Lab Architecture

A complete ICS/SCADA learning environment could contain:

### ICS Network

- PLC simulator
- HMI
- SCADA server
- Industrial protocols

### IT/Security Network

- Linux security machine
- Monitoring tools
- Log collection
- Network analysis

### Network Design

The networks should be isolated.

Example:

IT Network
     |
     |
 Firewall
     |
     |
ICS/SCADA Network
     |
     +--- SCADA Server
     |
     +--- HMI
     |
     +--- PLC Simulator

---

## 8. Network Isolation

Network isolation is very important when working with ICS/SCADA.

A laboratory should preferably use:

- Host-only networks
- Private virtual networks
- Isolated VLANs
- Firewalls
- Controlled communication paths

Real industrial systems should never be connected to a testing environment without authorization.

---

## 9. Key Terms

### Virtual Machine (VM)

A software-based computer running inside another computer.

### Hypervisor

Technology that creates and manages virtual machines.

### Nested Virtualization

Running virtual machines inside another virtual machine.

### KVM

Kernel-based Virtual Machine technology used for Linux virtualization.

### `/dev/kvm`

A Linux device interface used for KVM virtualization acceleration when available.

---

## 10. Key Takeaways

Remember:

Virtualization = Running virtual computers.

Hypervisor = Manages virtual machines.

KVM = Linux virtualization technology.

Nested virtualization = VM inside a VM.

ICS virtualization = Useful for safely creating training and testing environments.

The current EC2 environment is already virtualized, but `/dev/kvm` is unavailable, so additional VM creation through VirtualBox is not suitable here.
