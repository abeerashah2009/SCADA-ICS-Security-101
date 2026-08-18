from pymodbus.server import StartTcpServer
from pymodbus.simulator import DataType, SimData, SimDevice


# Define holding registers
holding_registers = SimData(
    address=0,
    values=[100, 200, 300, 400, 500],
    datatype=DataType.REGISTERS,
)

# Define Modbus device with Unit ID 1
device = SimDevice(
    id=1,
    simdata=[holding_registers],
)

print("====================================")
print(" Local Modbus TCP Test Server")
print("====================================")
print("Address : 127.0.0.1")
print("Port    : 1502")
print("Unit ID : 1")
print("Registers:")
print("  0 = 100")
print("  1 = 200")
print("  2 = 300")
print("  3 = 400")
print("  4 = 500")
print("------------------------------------")
print("Server running...")
print("Press Ctrl+C to stop.")
print("------------------------------------")

StartTcpServer(
    context=device,
    address=("127.0.0.1", 1502),
)
