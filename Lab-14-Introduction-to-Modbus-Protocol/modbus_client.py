from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient("127.0.0.1", port=1502)

print("====================================")
print(" Modbus TCP Read / Write Test")
print("====================================")

if client.connect():
    print("[PASS] Connected to Modbus server")

    # Task 2.2 - Read Holding Registers
    read_result = client.read_holding_registers(
        address=0,
        count=2,
        device_id=1
    )

    if read_result.isError():
        print("[FAIL] Initial read failed")
        print(read_result)
    else:
        print("[PASS] Initial read successful")
        print("Function Code : 0x03")
        print("Starting Address : 0")
        print("Quantity : 2")
        print("Register Values :", read_result.registers)

    # Task 2.3 - Write Single Register
    write_result = client.write_register(
        address=0,
        value=999,
        device_id=1
    )

    if write_result.isError():
        print("[FAIL] Write failed")
        print(write_result)
    else:
        print("[PASS] Write successful")
        print("Function Code : 0x06")
        print("Register Address : 0")
        print("Value Written : 999")

    # Verify the write
    verify_result = client.read_holding_registers(
        address=0,
        count=1,
        device_id=1
    )

    if verify_result.isError():
        print("[FAIL] Write verification failed")
        print(verify_result)
    else:
        print("[PASS] Write verification successful")
        print("Register 0 =", verify_result.registers[0])

    client.close()
    print("[PASS] Connection closed")

else:
    print("[FAIL] Could not connect to Modbus server")
