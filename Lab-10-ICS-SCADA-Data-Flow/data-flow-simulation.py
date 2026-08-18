#!/usr/bin/env python3

"""
Lab 10 - ICS/SCADA Data Flow Simulation

This program simulates a simple industrial data flow:

Sensor -> PLC -> SCADA Server -> HMI

The simulation is completely local and does not communicate
with real industrial devices.
"""

from datetime import datetime


def header(title):
    print("=" * 60)
    print(title)
    print("=" * 60)


def main():
    header("Lab 10 - ICS/SCADA Data Flow Simulation")

    print("\n1. Simulation Environment")
    print("-" * 60)
    print("Mode        : Local software simulation")
    print("Real PLC    : No")
    print("Real SCADA  : No")
    print("Network     : No external communication")

    print("\n2. Sensor Layer")
    print("-" * 60)

    sensor_data = {
        "Temperature": 72.5,
        "Pressure": 4.8,
        "Flow": 125.0
    }

    for sensor, value in sensor_data.items():
        unit = {
            "Temperature": "C",
            "Pressure": "bar",
            "Flow": "L/min"
        }[sensor]

        print(f"{sensor:12}: {value} {unit}")

    print("\n3. PLC Layer")
    print("-" * 60)
    print("[PASS] Sensor data received by simulated PLC")
    print("[PASS] PLC processing simulated")
    print("[PASS] Process values prepared for SCADA")

    plc_data = sensor_data.copy()

    print("\nPLC Process Data:")
    for key, value in plc_data.items():
        print(f"  {key}: {value}")

    print("\n4. SCADA Layer")
    print("-" * 60)
    print("[PASS] PLC data received by simulated SCADA server")
    print("[PASS] Supervisory monitoring simulated")

    print("\nSCADA Data:")
    for key, value in plc_data.items():
        print(f"  {key}: {value}")

    print("\n5. HMI / Operator Layer")
    print("-" * 60)
    print("[PASS] SCADA information presented to simulated HMI")
    print("[PASS] Operator visibility simulated")

    print("\nHMI Display:")
    for key, value in plc_data.items():
        unit = {
            "Temperature": "C",
            "Pressure": "bar",
            "Flow": "L/min"
        }[key]

        print(f"  {key}: {value} {unit}")

    print("\n6. Data Flow Verification")
    print("-" * 60)

    flow = [
        "Sensor",
        "PLC",
        "SCADA Server",
        "HMI / Operator"
    ]

    print(" -> ".join(flow))

    print("\n[PASS] Sensor-to-PLC flow verified")
    print("[PASS] PLC-to-SCADA flow verified")
    print("[PASS] SCADA-to-HMI flow verified")

    print("\n7. Security Observation")
    print("-" * 60)
    print("[PASS] Simulation is local")
    print("[PASS] No real PLC contacted")
    print("[PASS] No real SCADA system contacted")
    print("[PASS] No external network communication")
    print("[PASS] No industrial process modified")

    print("\n8. Potential Weak Points")
    print("-" * 60)
    print("- Network latency")
    print("- Packet loss")
    print("- Limited bandwidth")
    print("- Weak authentication")
    print("- Unencrypted protocols")
    print("- Poor network segmentation")
    print("- Single points of failure")

    print("\n" + "=" * 60)
    print("Lab 10 simulation completed successfully")
    print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)


if __name__ == "__main__":
    main()
