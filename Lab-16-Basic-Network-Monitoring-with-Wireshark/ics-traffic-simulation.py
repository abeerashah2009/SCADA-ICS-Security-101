import socket
import time

HOST = "127.0.0.1"

# Modbus/TCP uses port 502
# DNP3 commonly uses port 20000

def send_traffic(port, payload, name):
    print(f"[INFO] Sending {name} traffic to TCP/{port}")

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            s.connect((HOST, port))
            s.sendall(payload)
            print(f"[PASS] {name} payload sent")
    except ConnectionRefusedError:
        print(f"[INFO] No listener on TCP/{port}")
        print(f"[INFO] {name} filter can still be tested against packet data.")
    except Exception as e:
        print(f"[INFO] {name} test: {e}")


# Simple Modbus/TCP-like laboratory payload
modbus_payload = bytes.fromhex(
    "000100000006010300000002"
)

# DNP3-like laboratory payload
dnp3_payload = bytes.fromhex(
    "05640cc401000000"
)

print("=" * 50)
print("ICS Traffic Simulation")
print("=" * 50)

send_traffic(502, modbus_payload, "Modbus")
time.sleep(1)

send_traffic(20000, dnp3_payload, "DNP3")

print("=" * 50)
print("Simulation complete")
print("=" * 50)
