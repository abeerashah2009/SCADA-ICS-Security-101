# Lab 23: Basic ICS/SCADA Asset Inventory

## Objective

This lab demonstrates basic ICS/SCADA asset inventory techniques using
network discovery, asset classification, software inventory, and Modbus
TCP port assessment.

## Environment

- OS: Ubuntu 24.04.3 LTS
- Kernel: 6.14.0-1018-aws
- Network: 172.31.10.0/24
- Assessment Host: 172.31.10.82
- Interface: ens5
- Gateway: 172.31.10.1
- Nmap: 7.94SVN
- Rsyslog: 8.2312.0
- Python: 3.12.3
- Git: 2.43.0

## Task 1: Hardware and Network Inventory

Nmap host discovery was performed against the authorized lab subnet:

    nmap -sn 172.31.10.0/24 -oN network-discovery.txt

Eight hosts were discovered:

- 172.31.10.42
- 172.31.10.82
- 172.31.10.96
- 172.31.10.118
- 172.31.10.142
- 172.31.10.151
- 172.31.10.153
- 172.31.10.216

The discovered hosts were documented in `asset-inventory.csv`.

No PLC, RTU, HMI, or physical sensor was confirmed from host discovery
alone. These assets were documented as not detected rather than assuming
their identities.

## Modbus TCP Assessment

TCP port 502 was checked on the discovered hosts:

    nmap -p 502 172.31.10.42 172.31.10.82 172.31.10.96 \
    172.31.10.118 172.31.10.142 172.31.10.151 \
    172.31.10.153 172.31.10.216 -oN modbus-scan.txt

Results:

- 172.31.10.42: closed
- 172.31.10.82: closed
- 172.31.10.96: closed
- 172.31.10.118: closed
- 172.31.10.142: closed
- 172.31.10.151: filtered
- 172.31.10.153: closed

No active Modbus TCP PLC was confirmed.

## Task 2: Software Inventory

The following software was identified on the assessment workstation:

| Software | Version | Purpose |
|---|---|---|
| Ubuntu Linux | 24.04.3 LTS | Operating system |
| Nmap | 7.94SVN | Network discovery |
| Rsyslog | 8.2312.0 | Logging |
| Python | 3.12.3 | Automation/scripting |
| Git | 2.43.0 | Version control |

Details are recorded in `software-inventory.csv`.

## Task 3: Network Interconnections

The assessment workstation is connected to the `172.31.10.0/24`
network through interface `ens5`.

Network gateway:

    172.31.10.1

The observed network interconnections and security observations are
documented in:

- `network-interconnections.txt`
- `network-topology.txt`

The topology documents the assessment host, discovered network hosts,
gateway, and Modbus TCP assessment.

## Security Observations

- Network discovery identifies reachable hosts but does not prove their
  ICS roles.
- TCP/502 was not confirmed open on any scanned host.
- Host `172.31.10.151` returned a filtered TCP/502 state and would require
  further authorized investigation.
- PLC, RTU, HMI, and sensor roles were not assumed without evidence.
- Maintaining an accurate asset inventory is important for ICS security,
  vulnerability management, monitoring, and incident response.

## Evidence Files

- `asset-inventory.csv` - hardware and network asset inventory
- `software-inventory.csv` - installed software inventory
- `network-discovery.txt` - Nmap host discovery results
- `modbus-scan.txt` - TCP/502 Modbus assessment
- `network-interconnections.txt` - network interconnection documentation
- `network-topology.txt` - text-based network topology

## Conclusion

The lab successfully demonstrated a basic ICS/SCADA asset inventory
process. Network hosts were discovered and documented, software and
system information were recorded, Modbus TCP was assessed, and the
observed network topology and interconnections were documented.

The exercise also demonstrated an important security principle:
unknown assets should remain classified as unknown until sufficient
evidence is available to identify them accurately.
