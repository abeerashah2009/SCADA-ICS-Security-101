comparison = {
    "Real-Time Operations": {
        "ICS": "Critical for industrial processes",
        "Traditional IT": "Usually less time-critical"
    },
    "Primary Priority": {
        "ICS": "Safety and availability",
        "Traditional IT": "Confidentiality, integrity, and availability"
    },
    "Lifecycle": {
        "ICS": "Typically long",
        "Traditional IT": "Usually shorter"
    },
    "Environment": {
        "ICS": "Physical/industrial processes",
        "Traditional IT": "Information and business systems"
    },
    "Typical Devices": {
        "ICS": "PLCs, RTUs, sensors, actuators",
        "Traditional IT": "Servers, PCs, laptops"
    }
}

print("ICS vs Traditional IT Comparison")
print("=" * 40)

for category, values in comparison.items():
    print(f"\n{category}")
    print(f"  ICS: {values['ICS']}")
    print(f"  Traditional IT: {values['Traditional IT']}")
