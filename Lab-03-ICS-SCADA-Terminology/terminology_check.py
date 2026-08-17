terms = {
    "PLC": "Programmable Logic Controller - performs real-time control",
    "RTU": "Remote Terminal Unit - collects remote field data",
    "HMI": "Human-Machine Interface - provides operator visualization",
    "DCS": "Distributed Control System - provides distributed process control",
    "SCADA": "Supervisory Control and Data Acquisition - provides supervisory monitoring"
}

print("ICS/SCADA Terminology Verification")
print("=" * 40)

for term, description in terms.items():
    print(f"{term}: {description}")
