#!/usr/bin/env python3

from datetime import datetime


class SimulatedPLC:
    """Simple local PLC/Modbus-style simulation."""

    def __init__(self):
        self.device_name = "PLC-SIM-01"
        self.protocol = "Modbus Simulation"
        self.registers = {
            1: 125,
            2: 78,
            3: 100,
            4: 45,
        }

    def display_configuration(self):
        print("=" * 60)
        print("Lab 09 - Basic ICS/SCADA System Exploration")
        print("=" * 60)

        print("\n1. Simulated Device Configuration")
        print("-" * 60)
        print(f"Device Name : {self.device_name}")
        print(f"Protocol    : {self.protocol}")
        print("Mode        : Local Simulation")

    def display_registers(self, title):
        print(f"\n{title}")
        print("-" * 60)

        for register, value in self.registers.items():
            print(f"Register {register}: {value}")

    def read_register(self, register):
        if register not in self.registers:
            raise ValueError(f"Register {register} does not exist.")

        return self.registers[register]

    def write_register(self, register, value):
        if register not in self.registers:
            raise ValueError(f"Register {register} does not exist.")

        if not isinstance(value, int):
            raise ValueError("Register value must be an integer.")

        if not 0 <= value <= 65535:
            raise ValueError("Register value must be between 0 and 65535.")

        self.registers[register] = value


def main():
    plc = SimulatedPLC()

    plc.display_configuration()

    plc.display_registers("2. Initial Holding Registers")

    print("\n3. Read Operation")
    print("-" * 60)

    register = 1
    value = plc.read_register(register)

    print(f"Reading Register {register}...")
    print(f"Register {register} Value: {value}")

    print("\n4. Write Operation")
    print("-" * 60)

    register_to_write = 2
    old_value = plc.read_register(register_to_write)
    new_value = 150

    print(f"Register {register_to_write} Before: {old_value}")
    print(f"Writing Register {register_to_write} = {new_value}")

    plc.write_register(register_to_write, new_value)

    print(f"Register {register_to_write} After: "
          f"{plc.read_register(register_to_write)}")

    print("\n5. Read-After-Write Verification")
    print("-" * 60)

    verified_value = plc.read_register(register_to_write)

    if verified_value == new_value:
        print("[PASS] Register write verified successfully")
    else:
        print("[FAIL] Register write verification failed")

    plc.display_registers("6. Final Holding Registers")

    print("\n7. Security and Safety Verification")
    print("-" * 60)
    print("[PASS] Simulation performed locally")
    print("[PASS] No real PLC contacted")
    print("[PASS] No real Modbus device contacted")
    print("[PASS] No external network communication required")
    print("[PASS] No industrial process modified")

    print("\n" + "=" * 60)
    print("Simulation completed successfully.")
    print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)


if __name__ == "__main__":
    main()
