#!/bin/bash

OUTPUT="evidence/system-info.txt"

{
    echo "========================================"
    echo "LAB 35 - ICS FORENSIC SYSTEM INFORMATION"
    echo "========================================"
    echo

    echo "===== DATE ====="
    date -u

    echo
    echo "===== HOSTNAME ====="
    hostname

    echo
    echo "===== OPERATING SYSTEM ====="
    lsb_release -ds 2>/dev/null || cat /etc/os-release

    echo
    echo "===== KERNEL ====="
    uname -a

    echo
    echo "===== SYSTEM UPTIME ====="
    uptime

    echo
    echo "===== NETWORK INTERFACES ====="
    ip -br addr

    echo
    echo "===== DISK INFORMATION ====="
    lsblk

    echo
    echo "===== MOUNTED FILESYSTEMS ====="
    findmnt

    echo
    echo "===== RUNNING SERVICES ====="
    systemctl --type=service --state=running --no-pager

} > "$OUTPUT"

echo "Forensic system information collected: $OUTPUT"
