from scapy.all import IP, TCP, Raw, wrpcap

packets = []

# TCP SYN
packets.append(
    IP(src="192.168.1.10", dst="192.168.1.20") /
    TCP(sport=12345, dport=502, flags="S")
)

# TCP SYN-ACK
packets.append(
    IP(src="192.168.1.20", dst="192.168.1.10") /
    TCP(sport=502, dport=12345, flags="SA")
)

# TCP packet carrying sample Modbus/TCP-like data
packets.append(
    IP(src="192.168.1.10", dst="192.168.1.20") /
    TCP(sport=12345, dport=502, flags="PA") /
    Raw(load=b"\x00\x01\x00\x00\x00\x06\x01\x03\x00\x00\x00\x01")
)

wrpcap("modbus-sample.pcap", packets)

print("Created modbus-sample.pcap")
