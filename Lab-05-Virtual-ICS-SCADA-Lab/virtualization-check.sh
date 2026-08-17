#!/bin/bash

echo "Virtual ICS/SCADA Lab Environment Check"
echo "======================================="
echo

echo "Operating System:"
uname -a
echo

echo "Virtualization Environment:"
systemd-detect-virt
echo

echo "Hypervisor Information:"
lscpu | grep -E 'Virtualization|Hypervisor' || echo "No hypervisor information found"
echo

echo "KVM Device:"
if [ -e /dev/kvm ]; then
    ls -l /dev/kvm
    echo "KVM device is available."
else
    echo "/dev/kvm is not available."
    echo "Nested KVM acceleration is not exposed to this environment."
fi

echo
echo "CPU Information:"
nproc
echo

echo "Memory Information:"
free -h

echo
echo "======================================="
echo "Virtualization check completed."
