# Lab 23: Basic ICS/SCADA Asset Inventory

## Objective

This lab demonstrates basic ICS/SCADA asset inventory techniques using
network discovery, asset classification, software inventory, network
interconnection documentation, and Modbus TCP assessment.

The lab emphasizes accurate documentation and avoids assuming that an
unknown network host is an ICS device without supporting evidence.

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

## Assessment Date

2026-08-20

## Task 1: Hardware and Network Inventory

Nmap host discovery was performed against the authorized lab subnet:

    nmap -sn 172.31.10.0/24 -oN network-discovery.txt

Eight hosts were discovered during the initial network discovery:

- 172.31.10.42
- 172.31.10.82
- 172.31.10.96
- 172.31.10.118
- 172.31.10.142
- 172.31.10.151
- 172.31.10.153
- 172.31.10.216

The discovered hosts were documented in:

    asset-inventory.csv

The assessment workstation was identified as:

- Hostname: ip-172-31-10-82
- IP Address: 172.31.10.82
- OS: Ubuntu 24.04.3 LTS

No PLC, RTU, HMI, or physical sensor was confirmed from host discovery
alone. These assets were documented as not detected rather than assuming
their identities.

## Modbus TCP Assessment

TCP port 502 was assessed on the discovered hosts:

    nmap -p 502 172.31.10.42 172.31.10.82 172.31.10.96 \
    172.31.10.118 172.31.10.142 172.31.10.151 \
    172.31.10.153 172.31.10.216 -oN modbus-scan.txt

Results from the responding hosts:

- 172.31.10.42: TCP/502 closed
- 172.31.10.82: TCP/502 closed
- 172.31.10.96: TCP/502 closed
- 172.31.10.118: TCP/502 closed
- 172.31.10.142: TCP/502 closed
- 172.31.10.151: TCP/502 filtered
- 172.31.10.153: TCP/502 closed

Follow-up assessment:

    nmap -p 502 172.31.10.216 -oN modbus-216-sv.txt

Result:

- 172.31.10.216: host appeared down during the follow-up assessment.

Because 172.31.10.216 did not respond during the follow-up assessment,
its TCP/502 state could not be determined.

Therefore:

- No active Modbus TCP PLC was confirmed.
- No host was classified as a PLC solely from the Nmap results.
- 172.31.10.151 requires further authorized investigation because its
  TCP/502 state was filtered.
- 172.31.10.216 was unavailable during the follow-up Modbus assessment.

## Task 2: Software Inventory

The following software was identified on the assessment workstation:

| Software | Version | Purpose |
|---|---|---|
| Ubuntu Linux | 24.04.3 LTS | Operating system |
| Nmap | 7.94SVN | Network discovery |
| Rsyslog | 8.2312.0 | Logging |
| Python | 3.12.3 | Automation and scripting |
| Git | 2.43.0 | Version control |

Details are recorded in:

    software-inventory.csv

## Task 3: Network Interconnections

The assessment workstation is connected to the:

    172.31.10.0/24

network through interface:

    ens5

Default gateway:

    172.31.10.1

The observed network interconnections are documented in:

- network-interconnections.txt
- network-topology.txt

The topology documentation includes the assessment workstation, discovered
network hosts, gateway, and Modbus TCP assessment.

## Network Topology

The simplified observed topology is:

    AWS / Lab Network
            |
       172.31.10.1
          Gateway
            |
       172.31.10.0/24
            |
       172.31.10.82
       Assessment Host
            |
       Other Discovered Hosts
       172.31.10.42
       172.31.10.96
       172.31.10.118
       172.31.10.142
       172.31.10.151
       172.31.10.153
       172.31.10.216

No confirmed PLC, RTU, HMI, or sensor interconnection was identified.

## Security Observations

- Network discovery identifies reachable hosts but does not prove their
  ICS roles.
- TCP/502 was not confirmed open on any responding host.
- 172.31.10.151 returned a filtered TCP/502 state.
- 172.31.10.216 was discovered initially but was unavailable during the
  follow-up Modbus assessment.
- PLC, RTU, HMI, and sensor roles were not assumed without evidence.
- Unknown assets should remain classified as unknown until sufficient
  evidence is available.
- Maintaining an accurate asset inventory supports vulnerability
  management, monitoring, incident response, and ICS security.

## Evidence Files

- `asset-inventory.csv` - hardware and network asset inventory
- `software-inventory.csv` - software inventory
- `network-discovery.txt` - Nmap host discovery results
- `modbus-scan.txt` - Modbus TCP assessment results
- `modbus-216-sv.txt` - follow-up assessment of 172.31.10.216
- `network-interconnections.txt` - network interconnection documentation
- `network-topology.txt` - text-based network topology

## Conclusion

The lab successfully demonstrated a basic ICS/SCADA asset inventory
process.

Network hosts were discovered and documented, software and system
information were recorded, Modbus TCP was assessed, and the observed
network topology and interconnections were documented.

The exercise also demonstrated an important security principle:

Unknown assets should remain classified as unknown until sufficient
evidence is available to identify them accurately.

The assessment did not confirm an active Modbus TCP PLC, and the available
evidence was documented without making unsupported device-role assumptions.
