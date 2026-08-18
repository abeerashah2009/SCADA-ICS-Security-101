# Lab 14 - Modbus TCP Packet Analysis

print("Modbus TCP Packet Structure")
print("=" * 35)

print("\nMBAP Header:")
print("1. Transaction Identifier")
print("2. Protocol Identifier")
print("3. Length")
print("4. Unit Identifier")

print("\nModbus PDU:")
print("1. Function Code")
print("2. Function-specific Data")

print("\nCommon Function Codes:")
function_codes = {
    "0x01": "Read Coils",
    "0x02": "Read Discrete Inputs",
    "0x03": "Read Holding Registers",
    "0x04": "Read Input Registers",
    "0x05": "Write Single Coil",
    "0x06": "Write Single Register",
    "0x10": "Write Multiple Registers",
}

for code, operation in function_codes.items():
    print(f"{code} - {operation}")

print("\nModbus TCP:")
print("Transport : TCP/IP")
print("Default Port : 502")
print("Header : MBAP")
print("RTU CRC : Not present in Modbus TCP")

print("\n[PASS] Modbus TCP packet structure reviewed")
print("[PASS] Common function codes identified")
