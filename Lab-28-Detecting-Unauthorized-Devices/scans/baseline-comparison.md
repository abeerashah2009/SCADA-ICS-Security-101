# Baseline vs Follow-up Scan

## Scan Information

- Network: 172.31.10.0/24
- Baseline scan: 2026-08-21 01:35 UTC
- Follow-up scan: 2026-08-21 01:36 UTC
- Tool: Nmap 7.94SVN
- Scan type: Host discovery (`-sn`)

## Results

| IP Address | Baseline | Follow-up | MAC Address | Finding |
|---|---|---|---|---|
| 172.31.10.1 | Present | Present | 0A:78:67:64:4C:BD | No change |
| 172.31.10.31 | Present | Present | 0A:FF:C8:84:82:11 | No change |
| 172.31.10.102 | Present | Present | Local host | No change |
| 172.31.10.151 | Present | Present | 0A:FF:F4:54:86:5F | No change |
| 172.31.10.187 | Present | Present | 0A:FF:CC:EE:2A:A5 | No change |

## Detection Result

- Baseline hosts: 5
- Follow-up hosts: 5
- New hosts detected: 0
- Removed hosts detected: 0

## Assessment

The follow-up scan matched the baseline inventory. No new host was detected during this scan window.

This result does not prove that all devices are authorized. Authorization should be verified against the organization's approved asset inventory or network management records.

## Evidence

- `baseline-scan.txt`
- `followup-scan.txt`
- `baseline-inventory.md`
