#!/usr/bin/env python3

import socket
import time

TARGET = "127.0.0.1"

MODBUS_PORT = 1502
DNP3_PORT = 20000

def send_traffic(port, payload, label):
    try:
        with socket.create_connection((TARGET, port), timeout=1) as sock:
            sock.sendall(payload)
            print(f"{label}: sent {len(payload)} bytes")
    except (ConnectionRefusedError, TimeoutError, OSError):
        pass

modbus_request = bytes.fromhex(
    "000100000006010300000002"
)

dnp3_request = bytes.fromhex(
    "056405c401000000"
)

for i in range(20):
    send_traffic(
        MODBUS_PORT,
        modbus_request,
        "MODBUS"
    )

    time.sleep(0.2)

    send_traffic(
        DNP3_PORT,
        dnp3_request,
        "DNP3"
    )

    time.sleep(0.3)

print("ICS traffic generation complete.")

