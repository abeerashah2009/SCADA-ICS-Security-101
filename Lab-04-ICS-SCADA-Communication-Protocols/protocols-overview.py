#!/usr/bin/env python3

print("ICS/SCADA Communication Protocols Overview")
print("=" * 50)

protocols = {
    "Modbus RTU": {
        "type": "Serial",
        "transport": "RS-485 / RS-232",
        "common_use": "PLCs, sensors, meters"
    },
    "Modbus TCP": {
        "type": "Ethernet",
        "transport": "TCP/IP",
        "common_use": "Industrial Ethernet networks"
    },
    "DNP3": {
        "type": "Serial or Ethernet",
        "transport": "Serial / TCP/IP",
        "common_use": "Utilities and SCADA"
    },
    "OPC UA": {
        "type": "Ethernet",
        "transport": "TCP/IP",
        "common_use": "Industrial interoperability"
    }
}

for protocol, details in protocols.items():
    print(f"\nProtocol: {protocol}")
    print(f"  Communication Type: {details['type']}")
    print(f"  Transport: {details['transport']}")
    print(f"  Common Use: {details['common_use']}")

print("\n" + "=" * 50)
print("Simulation completed successfully.")
print("No real industrial devices were contacted.")
