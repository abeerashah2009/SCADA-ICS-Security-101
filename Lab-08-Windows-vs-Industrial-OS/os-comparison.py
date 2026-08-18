#!/usr/bin/env python3

"""
Lab 08: Windows vs Industrial OS Basics
Practical OS Comparison and Environment Discovery

This script performs safe local system checks.
It does not modify the operating system or contact
any industrial devices.
"""

import platform
import os
import shutil
from datetime import datetime


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def check_command(command):
    return shutil.which(command) is not None


section("Windows vs Industrial OS Basics")
print("Lab 08 - OS Environment Verification")

section("1. Current Environment")

print(f"Operating System : {platform.system()}")
print(f"OS Release       : {platform.release()}")
print(f"OS Version       : {platform.version()}")
print(f"Architecture     : {platform.machine()}")
print(f"Python Version   : {platform.python_version()}")
print(f"Hostname         : {platform.node()}")

section("2. Linux Environment Checks")

if platform.system() == "Linux":
    print("[PASS] Linux-based environment detected")
else:
    print("[INFO] Current environment is not Linux")

section("3. Common System Utilities")

commands = [
    "systemctl",
    "ip",
    "uname",
    "ps",
]

for command in commands:
    if check_command(command):
        print(f"[AVAILABLE] {command}")
    else:
        print(f"[NOT AVAILABLE] {command}")

section("4. Industrial OS Concepts")

print("ICS operating systems commonly prioritize:")
print("  - Reliability")
print("  - Availability")
print("  - Deterministic behavior")
print("  - Long system lifecycles")
print("  - Controlled change management")

print("\nStandard desktop operating systems commonly prioritize:")
print("  - General-purpose computing")
print("  - Frequent security updates")
print("  - Broad hardware/software compatibility")
print("  - User productivity")

section("5. Patch Management Considerations")

print("ICS patching considerations:")
print("  - Compatibility testing")
print("  - Planned maintenance windows")
print("  - Downtime requirements")
print("  - Vendor validation")
print("  - Backup and recovery planning")
print("  - Change management")

print("\nDesktop OS patching is generally more frequent and")
print("can often be performed with less operational impact.")

section("6. Security Observation")

print("[PASS] OS characteristics reviewed")
print("[PASS] ICS reliability requirements reviewed")
print("[PASS] Patch management challenges reviewed")
print("[PASS] Safe local-only assessment completed")

section("7. Lab Safety")

print("No real ICS/SCADA devices were contacted.")
print("No operating system configuration was modified.")
print("No network scanning was performed.")
print("This script is intended for educational use.")

section("Lab Completion")

print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("Lab 08 verification completed successfully.")
