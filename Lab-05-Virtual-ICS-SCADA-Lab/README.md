# Lab 05: Setting Up a Virtual ICS/SCADA Lab Environment

## Objectives

- Understand virtualization in an ICS/SCADA laboratory.
- Identify the virtualization technology available in the current environment.
- Determine whether nested virtualization is available.
- Understand the requirements for running additional virtual machines.
- Document a safe approach for building a virtual ICS/SCADA lab.

## Lab Environment

This lab is being performed inside an AWS EC2 instance running Ubuntu 24.04.

The EC2 instance is already a virtual machine running under the KVM hypervisor.

## Environment Discovery

The following commands were used:

```bash
uname -a
systemd-detect-virt
lscpu | grep -E 'Virtualization|Hypervisor'
ls -l /dev/kvm
