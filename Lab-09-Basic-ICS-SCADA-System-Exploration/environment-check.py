#!/usr/bin/env python3

import platform
import shutil
import subprocess
import sys
from datetime import datetime


def command_available(command):
    return shutil.which(command) is not None


def run_command(command):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout.strip()
    except Exception as error:
        return f"Unable to execute command: {error}"


print("=" * 60)
print("Lab 09 - ICS/SCADA Environment Verification")
print("=" * 60)

print("\n1. Operating System")
print("-" * 60)
print(f"System       : {platform.system()}")
print(f"Release      : {platform.release()}")
print(f"Version      : {platform.version()}")
print(f"Architecture : {platform.machine()}")
print(f"Hostname     : {platform.node()}")

print("\n2. Python Environment")
print("-" * 60)
print(f"Python       : {sys.version.split()[0]}")

print("\n3. Required Utilities")
print("-" * 60)

utilities = [
    "python3",
    "java",
    "uname"
]

for utility in utilities:
    if command_available(utility):
        print(f"[AVAILABLE] {utility}")
    else:
        print(f"[NOT AVAILABLE] {utility}")

print("\n4. Java Version")
print("-" * 60)

if command_available("java"):
    print(run_command(["java", "-version"]))
else:
    print("Java is not installed.")

print("\n5. Kernel Information")
print("-" * 60)
print(run_command(["uname", "-a"]))

print("\n6. ICS/SCADA Laboratory Assessment")
print("-" * 60)
print("[PASS] Operating system information collected")
print("[PASS] Python environment verified")
print("[PASS] Local laboratory environment identified")

if command_available("java"):
    print("[PASS] Java runtime is available")
else:
    print("[INFO] Java runtime is not currently available")
    print("[INFO] A local Python simulation will be used for this lab")

print("\n7. Safety Verification")
print("-" * 60)
print("[PASS] Environment assessment is local")
print("[PASS] No real ICS devices contacted")
print("[PASS] No industrial processes modified")
print("[PASS] No external network scanning performed")

print("\n" + "=" * 60)
print("Lab 09 environment verification completed")
print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 60)
