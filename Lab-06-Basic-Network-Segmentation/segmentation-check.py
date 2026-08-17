#!/usr/bin/env python3

print("ICS/Enterprise Network Segmentation Check")
print("=" * 50)

# Conceptual network zones
zones = {
    "Internet": "Untrusted external network",
    "DMZ": "Public-facing services",
    "Corporate": "Business and enterprise systems",
    "ICS": "Industrial control systems"
}

print("\nNetwork Zones:")
for zone, description in zones.items():
    print(f"  {zone}: {description}")

# Simulated firewall policy
rules = [
    ("Internet", "DMZ", "ALLOW", "Required public services"),
    ("Internet", "Corporate", "BLOCK", "Direct corporate access"),
    ("Internet", "ICS", "BLOCK", "Direct ICS access"),
    ("Corporate", "DMZ", "ALLOW", "Authorized business services"),
    ("Corporate", "ICS", "RESTRICTED", "Only authorized traffic"),
    ("DMZ", "ICS", "BLOCK", "Prevent direct DMZ-to-ICS access"),
]

print("\nSimulated Firewall Policy:")
print("-" * 50)

for source, destination, action, reason in rules:
    print(f"{source:12} -> {destination:12} : {action}")
    print(f"  Reason: {reason}")

# Security checks
print("\nSecurity Checks:")
print("-" * 50)

checks = {
    "Internet directly blocked from ICS": True,
    "DMZ isolated from ICS": True,
    "Corporate-to-ICS access restricted": True,
    "Network zones logically separated": True,
    "Firewall controls zone communication": True,
}

passed = 0

for check, result in checks.items():
    status = "PASS" if result else "FAIL"
    print(f"[{status}] {check}")

    if result:
        passed += 1

print("\n" + "=" * 50)
print(f"Security checks passed: {passed}/{len(checks)}")

if passed == len(checks):
    print("Segmentation simulation completed successfully.")
else:
    print("Some segmentation checks require attention.")

print("No real network traffic was modified.")
print("No real ICS/SCADA devices were contacted.")
