# Lab 24: ICS/SCADA Risk Assessment 101

## Environment

- OS: Ubuntu 24.04.3 LTS
- Assessment Host: 172.31.10.201
- Network: 172.31.10.0/24
- Nmap: 7.94SVN
- Wireshark: 4.2.2

## Network Discovery

Nmap host discovery identified 9 hosts initially:

- 172.31.10.13
- 172.31.10.53
- 172.31.10.96
- 172.31.10.118
- 172.31.10.121
- 172.31.10.142
- 172.31.10.151
- 172.31.10.158
- 172.31.10.201

A subsequent service scan identified 13 responding hosts.

## Observed Services

Several hosts exposed SSH on TCP/22.

Host 172.31.10.151 exposed:
- TCP/80 HTTP
- TCP/443 HTTPS

Most other tested ports were closed or filtered.

## Threat Identification

### 1. Unauthorized Access
SSH and web services represent potential access points that should be protected with authentication, network segmentation, and firewall controls.

### 2. Malware Infection
Malware could affect system availability, integrity, or operational processes if it reaches an ICS environment.

### 3. Network Exposure
Hosts with accessible services should be reviewed to determine whether each service is necessary.

## Risk Assessment

| Risk | Likelihood | Impact | Rank |
|---|---|---|---|
| Unauthorized access through exposed services | High | High | 1 |
| Malware infection | Medium | High | 2 |
| Unnecessary network services | Medium | Medium | 3 |
| Weak network segmentation | Medium | High | 4 |
| Loss of system availability | Medium | High | 5 |

## Recommended Mitigations

- Restrict access to management services such as SSH.
- Use firewall rules and network segmentation.
- Disable unnecessary services.
- Apply secure authentication and key-based SSH access.
- Monitor network traffic.
- Maintain an accurate asset inventory.
- Keep systems and security software updated according to ICS maintenance procedures.
- Establish backups and recovery procedures.
- Monitor critical ICS/SCADA communications.

## Conclusion

The assessment identified multiple hosts and several exposed services in the simulated environment. The results demonstrate why asset discovery, service identification, network monitoring, and risk ranking are important components of ICS/SCADA security.
