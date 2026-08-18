#!/usr/bin/env python3

"""
Lab 11 - Physical Security in ICS/SCADA
Safe Hypothetical Physical Security Assessment

This script evaluates a hypothetical ICS facility.
It does not access real industrial equipment, facilities,
CCTV systems, PLCs, SCADA systems, or physical security devices.
"""

from datetime import datetime


def print_header(title):
    print("=" * 64)
    print(title)
    print("=" * 64)


def main():
    print_header("Lab 11 - Physical Security in ICS/SCADA")
    print("Safe Hypothetical Facility Assessment")
    print()

    # ------------------------------------------------------------
    # 1. Assessment Environment
    # ------------------------------------------------------------
    print("=" * 64)
    print("1. Assessment Environment")
    print("-" * 64)

    print("Assessment Type : Hypothetical ICS Facility")
    print("Environment     : Local Documentation Assessment")
    print("Real Facility   : No")
    print("Real PLC        : No")
    print("Real SCADA      : No")
    print("Real CCTV       : No")
    print("External Access : No")

    # ------------------------------------------------------------
    # 2. Physical Safeguards
    # ------------------------------------------------------------
    print()
    print("=" * 64)
    print("2. Physical Safeguards Assessment")
    print("-" * 64)

    safeguards = [
        ("Perimeter fencing", "DETERRENCE"),
        ("Controlled entrance", "ACCESS CONTROL"),
        ("Electronic access cards", "AUTHENTICATION"),
        ("CCTV monitoring", "DETECTION"),
        ("Locked control room", "RESTRICTION"),
        ("Locked PLC cabinets", "EQUIPMENT PROTECTION"),
        ("Restricted server room", "CRITICAL ASSET PROTECTION"),
        ("Visitor management", "ACCOUNTABILITY"),
    ]

    for control, purpose in safeguards:
        print(f"[REVIEWED] {control:<30} -> {purpose}")

    # ------------------------------------------------------------
    # 3. Risk Assessment
    # ------------------------------------------------------------
    print()
    print("=" * 64)
    print("3. Unauthorized Physical Access Risks")
    print("-" * 64)

    risks = [
        "Unauthorized entry",
        "Equipment tampering",
        "Equipment theft",
        "Unauthorized configuration changes",
        "Malware introduction",
        "Network disruption",
        "Control-system shutdown",
        "Operational downtime",
        "Loss of monitoring",
        "Potential safety impact",
    ]

    for risk in risks:
        print(f"[IDENTIFIED] {risk}")

    # ------------------------------------------------------------
    # 4. Hypothetical Site Assessment
    # ------------------------------------------------------------
    print()
    print("=" * 64)
    print("4. Hypothetical ICS Site Assessment")
    print("-" * 64)

    vulnerabilities = [
        (
            "Uncontrolled entrance",
            "Unauthorized facility access",
            "Electronic access control and visitor registration",
        ),
        (
            "CCTV blind spots",
            "Security events may not be detected",
            "Improve camera coverage and monitoring",
        ),
        (
            "Unlocked PLC cabinets",
            "Physical equipment tampering",
            "Lock cabinets and restrict access",
        ),
        (
            "Weak server-room protection",
            "Unauthorized access to critical systems",
            "Use restricted server room and access control",
        ),
        (
            "Poor visitor management",
            "Unauthorized access to restricted areas",
            "Visitor badges, logs, and escort procedures",
        ),
    ]

    for number, (vulnerability, risk, mitigation) in enumerate(
        vulnerabilities, start=1
    ):
        print()
        print(f"Finding {number}")
        print(f"  Vulnerability : {vulnerability}")
        print(f"  Risk          : {risk}")
        print(f"  Mitigation    : {mitigation}")

    # ------------------------------------------------------------
    # 5. Defense in Depth
    # ------------------------------------------------------------
    print()
    print("=" * 64)
    print("5. Defense-in-Depth Model")
    print("-" * 64)

    layers = [
        "Perimeter Fence",
        "Controlled Gate",
        "Visitor Management",
        "Electronic Access Control",
        "CCTV Monitoring",
        "Restricted Control Room",
        "Locked Equipment Rooms",
        "ICS Assets",
    ]

    for position, layer in enumerate(layers, start=1):
        print(f"{position}. {layer}")

    # ------------------------------------------------------------
    # 6. Open-Source Security Tool Review
    # ------------------------------------------------------------
    print()
    print("=" * 64)
    print("6. Open-Source Physical Security Tool Review")
    print("-" * 64)

    print("[REVIEWED] ZoneMinder")
    print("Purpose    : Open-source video surveillance management")
    print("Capabilities:")
    print("  - Camera management")
    print("  - Video monitoring")
    print("  - Recording")
    print("  - Event monitoring")
    print("  - Security investigation")

    print()
    print("[INFO] ZoneMinder was not installed.")
    print("[INFO] This laboratory uses a safe documentation-based assessment.")

    # ------------------------------------------------------------
    # 7. Security Principles
    # ------------------------------------------------------------
    print()
    print("=" * 64)
    print("7. Physical Security Principles")
    print("-" * 64)

    principles = [
        "Defense in depth",
        "Least privilege",
        "Physical access control",
        "Monitoring",
        "Accountability",
        "Resilience",
    ]

    for principle in principles:
        print(f"[REVIEWED] {principle}")

    # ------------------------------------------------------------
    # 8. Safety Verification
    # ------------------------------------------------------------
    print()
    print("=" * 64)
    print("8. Safety Verification")
    print("-" * 64)

    safety_checks = [
        "No real ICS facility accessed",
        "No real PLC contacted",
        "No real SCADA system contacted",
        "No CCTV system accessed",
        "No physical security controls bypassed",
        "No industrial process modified",
        "No external facility tested",
        "Assessment remained hypothetical and local",
    ]

    for check in safety_checks:
        print(f"[PASS] {check}")

    # ------------------------------------------------------------
    # 9. Final Assessment
    # ------------------------------------------------------------
    print()
    print("=" * 64)
    print("9. Final Assessment")
    print("-" * 64)

    print("[PASS] Physical safeguards reviewed")
    print("[PASS] Locks reviewed")
    print("[PASS] Fencing reviewed")
    print("[PASS] CCTV reviewed")
    print("[PASS] Case study documented")
    print("[PASS] Unauthorized access risks identified")
    print("[PASS] Security breach scenario analyzed")
    print("[PASS] Hypothetical site assessed")
    print("[PASS] Physical vulnerabilities identified")
    print("[PASS] Mitigation strategies documented")
    print("[PASS] Open-source security software reviewed")
    print("[PASS] Defense-in-depth principles reviewed")
    print("[PASS] Safety requirements verified")

    # ------------------------------------------------------------
    # 10. Completion
    # ------------------------------------------------------------
    print()
    print("=" * 64)
    print("Lab 11 Assessment Completed Successfully")
    print("=" * 64)

    print(f"Completed : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Status    : COMPLETE")
    print("Evidence  : Physical security assessment documented")


if __name__ == "__main__":
    main()
