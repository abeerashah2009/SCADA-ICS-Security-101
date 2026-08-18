# ICS/SCADA Threat Comparison

## External vs Internal Threats

| Threat Type | Origin | Example | Potential Impact | Primary Controls |
|---|---|---|---|---|
| External | Outside organization | Cybercriminal | Data theft/disruption | Firewall, segmentation, MFA |
| Internal Malicious | Inside organization | Disgruntled employee | Unauthorized changes | Least privilege, monitoring |
| Internal Accidental | Inside organization | Phishing victim | Malware/credential compromise | Awareness training, email security |
| Contractor | Trusted third party | Compromised vendor account | Unauthorized access | Access control, monitoring |
| Nation-State | External | Strategic cyber operation | Espionage/sabotage | Defense-in-depth, segmentation |

## Key Observation

ICS environments must account for both technical and human threats.

External attackers may attempt to penetrate the organization, while internal
users may already have authorized access.

Security controls should therefore combine:

- Authentication
- Authorization
- Least privilege
- Network segmentation
- Monitoring
- Security awareness
- Incident response

## Defensive Principle

A strong ICS security architecture assumes that both external and internal
threats are possible and uses multiple layers of protection.

## Safety

This document contains defensive analysis only.

No real ICS/SCADA system was accessed, scanned, exploited, or modified.
