# Lab 18: Secure Remote Access Basics

**Lab:** Lab 18 - Secure Remote Access Basics  
**Environment:** Authorized educational Linux laboratory  
**Primary System:** Ubuntu Linux  
**Topics:** SSH, VPN, RDP, Telnet

---

# 1. Lab Objectives

The objectives of this laboratory are to:

- Understand secure remote access using SSH.
- Compare SSH, VPN, RDP, and Telnet.
- Understand the security risks of plaintext remote access protocols.
- Review basic VPN concepts for secure ICS/SCADA remote access.
- Apply secure remote-access principles in an authorized laboratory environment.

---

# 2. Task 1 — SSH Verification

## 2.1 OpenSSH Version

Command:

```bash
ssh -V
---

# 4. Task 3 — OpenVPN Basic Key Generation

## 4.1 OpenVPN Verification

OpenVPN was used to demonstrate basic VPN cryptographic
configuration in the authorized laboratory environment.

Command:

sudo openvpn --genkey secret lab-static.key

Result:

OpenVPN static key generated successfully.

---

## 4.2 Key File Permissions

Command:

ls -l lab-static.key

Result:

-rw------- 1 root root 636 lab-static.key

Verification command:

sudo stat -c '%A %U:%G %n' lab-static.key

Result:

-rw------- root:root lab-static.key

Status:

[PASS] OpenVPN static key generated.

[PASS] Key is owned by root.

[PASS] Key permissions restrict access to the root user.

Security Note:

The contents of the cryptographic key were not displayed or
shared because the key is sensitive authentication material.

---

# 5. VPN Security Concepts

A VPN creates an authenticated and encrypted tunnel between
authorized systems.

For an ICS/SCADA environment, a VPN can provide a controlled
remote-access path instead of exposing industrial services
directly to an untrusted network.

Important VPN security principles include:

- Strong authentication
- Encryption
- Restricted network access
- Firewall controls
- Least privilege
- Logging and monitoring
- Separation between IT and ICS networks

---

# 6. Remote Access Protocol Comparison

| Protocol | Purpose | Security |
|---|---|---|
| SSH | Secure remote command-line access | Encrypted |
| VPN | Secure network tunnel | Encrypted/authenticated |
| RDP | Remote graphical desktop | Encrypted session |
| Telnet | Remote command-line access | Plaintext/insecure |

SSH and VPN are generally preferred for secure remote access.
RDP can provide secure remote graphical access when properly
configured.

Telnet should not be used for sensitive remote administration
because its communication is transmitted without modern
encryption.

---

# 7. Telnet Security Risks

Telnet transmits session information in plaintext.

Potential risks include:

- Credential interception
- Session monitoring
- Command disclosure
- Traffic sniffing
- Unauthorized access

For ICS environments, plaintext remote administration creates
additional risk because credentials or operational information
could potentially be exposed.

SSH provides a secure alternative to Telnet.

---

# 8. ICS Remote Access Security Design

A secure ICS remote-access design should use:

1. VPN for controlled remote network access.
2. SSH for secure Linux administration.
3. Strong authentication.
4. Firewall restrictions.
5. Network segmentation.
6. Least-privilege accounts.
7. Monitoring and logging.

Remote users should not receive unrestricted access to the
industrial control network.

---

# 9. Important Lab Limitation

This laboratory generated and protected an OpenVPN static key
as a practical demonstration of VPN cryptographic material.

A complete production VPN requires additional server and client
configuration, certificates or authentication, routing,
firewall rules, and access-control policies.

Therefore, this laboratory does not claim that a complete
production VPN server was deployed.

---

# 10. Final Conclusion

This laboratory demonstrated secure remote-access concepts using
SSH and OpenVPN.

SSH was verified as an active secure remote-access service.
An OpenVPN static key was generated and protected with
root-only permissions.

SSH, VPN, RDP, and Telnet were compared, and the security risks
of plaintext Telnet communication were reviewed.

The laboratory demonstrated why encrypted, authenticated, and
least-privilege remote access is important when protecting
ICS/SCADA environments.

Status:

[PASS] Lab objectives completed.

---

# SSH Remote Access Demonstration

## SSH Version

Command:

ssh -V

Result:

OpenSSH_9.6p1 Ubuntu-3ubuntu13.14, OpenSSL 3.0.13

## SSH Server Status

The SSH service was verified as active and running.

SSH was listening on TCP port 22.

## SSH Key Authentication

An ED25519 key pair was generated:

~/.ssh/lab18_key
~/.ssh/lab18_key.pub

The public key was added to:

~/.ssh/authorized_keys

Permissions were configured securely:

~/.ssh = 700
~/.ssh/authorized_keys = 600

## SSH Connection Test

Command:

ssh -i ~/.ssh/lab18_key -o StrictHostKeyChecking=no ubuntu@localhost

Result:

SSH connection successfully established to localhost using
public-key authentication.

Status:

[PASS] Secure SSH remote access demonstrated.


---

# Telnet Security Risk Analysis

## Telnet Overview

Telnet is a remote access protocol that does not provide encryption
for the session by default.

Unlike SSH, Telnet can transmit authentication credentials and
session data in plaintext.

## Security Risks

The main risks of Telnet include:

- Usernames and passwords may be exposed.
- Session data can potentially be captured by network monitoring tools.
- Attackers on the network may intercept sensitive information.
- Telnet does not provide the strong confidentiality and integrity
  protections provided by SSH.

## SSH vs Telnet

| Feature | SSH | Telnet |
|---|---|---|
| Encryption | Yes | No |
| Secure authentication | Yes | No |
| Confidentiality | Protected | Not protected |
| Recommended for ICS remote access | Yes | No |

## Security Conclusion

Telnet should not be used for secure remote administration of
ICS/SCADA systems.

SSH is preferred because it provides encrypted communication and
supports secure public-key authentication.

Status:

[PASS] Telnet security risks identified and compared with SSH.

---

# VPN Connectivity Test

## OpenVPN Server

The OpenVPN server was started using server.conf.

The VPN server created the tunnel interface and assigned:

Server VPN address: 10.8.0.1

## OpenVPN Client

The OpenVPN client was started using client.conf.

Result:

Initialization Sequence Completed

Client VPN address: 10.8.0.2

## Tunnel Verification

Command:

ip addr show tun0

Result:

tun0 interface was successfully created with VPN address 10.8.0.2.

## VPN Connectivity Test

Command:

ping -c 3 10.8.0.1

Result:

3 packets transmitted, 3 received, 0% packet loss.

Status:

[PASS] VPN tunnel successfully established and connectivity verified.

---

# Lab Conclusion

This lab demonstrated secure remote access concepts using SSH and OpenVPN.

SSH public-key authentication was successfully demonstrated.

The risks of Telnet plaintext communication were analyzed.

A basic OpenVPN server and client configuration was created and tested.

The VPN tunnel successfully established communication between
10.8.0.2 and 10.8.0.1.

[PASS] Secure remote access lab completed.
