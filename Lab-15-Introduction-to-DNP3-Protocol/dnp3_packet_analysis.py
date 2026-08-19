from scapy.all import Ether, IP, TCP, Raw

print("=" * 50)
print("DNP3 Packet Structure Analysis")
print("=" * 50)

# DNP3 commonly uses TCP port 20000.
# This is a laboratory representation for analysis.
packet = (
    Ether()
    / IP(src="127.0.0.1", dst="127.0.0.1")
    / TCP(sport=40000, dport=20000)
    / Raw(load=b"\x05\x64\x0c\xc4\x01\x00\x00\x00")
)

print("\n[PASS] Packet constructed successfully")

print("\nProtocol Layers:")
packet.show()

print("\nDNP3 Laboratory Fields:")
print("Start Bytes       : 05 64")
print("Length            : 0C")
print("Control Field     : C4")
print("Destination       : 01 00")
print("Source            : 00 00")
print("DNP3 Port         : TCP/20000")

print("\n[PASS] DNP3 packet structure documented")

