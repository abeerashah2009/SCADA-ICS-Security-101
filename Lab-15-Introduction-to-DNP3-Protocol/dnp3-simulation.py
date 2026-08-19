import socket

HOST = "127.0.0.1"
PORT = 20000

payload = bytes.fromhex("05 64 0c c4 01 00 00 00")

print("=" * 50)
print("DNP3 Laboratory Traffic Simulation")
print("=" * 50)

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(payload)

    print("[PASS] Laboratory payload sent successfully")
    print(f"Destination : {HOST}:{PORT}")
    print(f"Payload     : {payload.hex()}")

except ConnectionRefusedError:
    print("[INFO] No persistent laboratory listener on TCP/20000")
    print("       Existing capture evidence can still be analyzed.")
