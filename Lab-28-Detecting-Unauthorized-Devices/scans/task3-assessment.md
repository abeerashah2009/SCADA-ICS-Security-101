# Task 3 - Physical and Network-Level Inspection

## Environment Limitation

This lab was performed on an AWS EC2 instance. Direct physical inspection of network equipment, switch ports, cables, and connected industrial devices was therefore not possible from the lab environment.

The limitation is documented rather than treating the cloud environment as a physical ICS network.

## Neighbor Table Check

The network neighbor table on `ens5` showed:

| IP Address | MAC Address | State |
|---|---|---|
| 172.31.10.1 | 0a:78:67:64:4c:bd | REACHABLE |
| 172.31.10.151 | 0a:ff:f4:54:86:5f | REACHABLE |

Both addresses were already present in the Nmap baseline. No previously unseen neighbor was identified during this check.

## Interface Health Check

Interface: `ens5`

- State: UP
- MAC Address: `0a:ff:d0:91:50:8b`
- RX errors: 0
- RX dropped: 0
- TX errors: 0
- TX dropped: 0
- Carrier errors: 0
- Collisions: 0

The interface was operational and showed zero recorded packet errors or drops at the time of inspection.

## Packet Analysis Tool

TShark was checked using `command -v tshark`.

Result:

`tshark not installed`

Therefore, packet capture or Wireshark/TShark traffic analysis was not performed during this lab run.

## Assessment

No new network neighbor was identified during the available network-level inspection. Physical inspection remains a required follow-up action in a real ICS/SCADA environment when an unknown device cannot be attributed to an approved asset.

Authorization decisions should be based on the organization's approved asset inventory and physical/network records.
