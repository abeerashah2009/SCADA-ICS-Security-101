#!/usr/bin/env python3

print("Modbus Communication Simulation")
print("=" * 40)

# Simulated Modbus registers
registers = {
    1: 125,
    2: 78,
    3: 100,
    4: 45
}

print("\nSimulated Holding Registers:")

for register, value in registers.items():
    print(f"  Register {register}: {value}")

# Simulate reading a register
requested_register = 1

print(f"\nReading Register {requested_register}...")

if requested_register in registers:
    value = registers[requested_register]
    print(f"Register {requested_register} Value: {value}")
else:
    print("Register not found")

print("\nSimulation completed successfully.")
print("No real Modbus device was contacted.")
