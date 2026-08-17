# Lab 06 Notes: Basic Network Segmentation Concepts

## 1. What is Network Segmentation?

Network segmentation means dividing a network into smaller, separate security zones.

Instead of allowing every device to communicate freely, traffic between zones is controlled.

### Simple Example

```text
Large Network
     |
     +--- Corporate Network
     |
     +--- DMZ
     |
     +--- ICS Network
2. Why is Network Segmentation Important?

Segmentation helps reduce the impact of a security incident.

If one system is compromised, segmentation can make it harder for an attacker to move to other systems.

Main Benefits
Limits unauthorized access
Reduces lateral movement
Protects critical systems
Controls network traffic
Makes monitoring easier
Separates different security requirements
3. What is a DMZ?

DMZ stands for Demilitarized Zone.

A DMZ is a separate network zone used for systems that need controlled communication with external or less-trusted networks.

Example
Internet
    |
    v
 Firewall
    |
    v
   DMZ
    |
 Web Server

The web server can be reachable from the Internet while remaining separated from sensitive internal systems.

4. Corporate Network

A corporate network normally contains business systems.

Examples:

Employee computers
File servers
Printers
Business applications
Email systems

Corporate networks generally support business operations.

5. ICS Network

ICS stands for Industrial Control System.

An ICS network contains systems used to monitor or control physical industrial processes.

Examples:

PLCs
HMIs
SCADA servers
Sensors
Actuators
Industrial controllers

ICS environments have special requirements because availability and safety are extremely important.

6. Corporate Network vs ICS Network
Corporate Network	ICS Network
Employee PCs	PLCs
File servers	HMIs
Business applications	SCADA servers
Email systems	Sensors
General IT services	Industrial controllers

These networks should not have unrestricted communication with each other.

7. Firewalls

A firewall can control traffic between network zones.

Example:

Corporate Network
       |
       v
   [Firewall]
       |
       v
   ICS Network

The firewall can allow only authorized traffic.

For example:

Corporate → ICS
Allowed: Specific authorized connection
Blocked: Unnecessary traffic
8. VLANs

VLAN means Virtual Local Area Network.

VLANs allow logical network separation using shared network infrastructure.

Example:

Switch
 |
 +--- VLAN 10 → Corporate
 |
 +--- VLAN 20 → DMZ
 |
 +--- VLAN 30 → ICS

VLANs provide logical separation, but they should not be treated as a complete security boundary by themselves.

Additional security controls such as firewalls and access controls may still be required.

9. Air-Gapping

An air-gapped network is isolated from another network.

Example:

Corporate Network


        X


      ICS Network

There is no normal direct network connection between the two environments.

Air-gapping can reduce remote attack paths, although it does not eliminate every possible security risk.

10. Example ICS Network Architecture
                       Internet
                          |
                          v
                     [ Firewall ]
                          |
                +---------+---------+
                |                   |
               DMZ            Corporate Network
                |                   |
           Web Server          PCs / Servers
                |
                |
          [ ICS Firewall ]
                |
                v
            ICS Network
                |
          +-----+-----+
          |           |
         HMI       PLC/SCADA
11. Security Rules

A properly segmented ICS environment should follow principles such as:

Least Privilege

Allow only the access that is required.

Controlled Communication

Do not allow unnecessary traffic between zones.

Monitoring

Monitor important network traffic and security events.

Defense in Depth

Use multiple security controls rather than relying on a single control.

Isolation

Keep critical ICS systems separated from general-purpose IT systems where appropriate.

12. Possible Attack Path

Without segmentation:

Internet
   |
Corporate PC
   |
   |
ICS Network
   |
   +--- SCADA
   |
   +--- PLC

A compromised corporate computer could potentially become a starting point for further attacks.

With segmentation:

Internet
   |
Corporate Network
   |
 Firewall
   |
Controlled Access
   |
 ICS Network

The firewall and other controls can limit what traffic reaches the ICS environment.

13. Important ICS Security Principle

ICS security is not simply about keeping systems connected or disconnected.

The goal is to provide:

Safety
Availability
Controlled access
Network visibility
Segmentation
Defense in depth

Security controls should also consider the operational requirements of industrial processes.

14. Key Terms
Segmentation

Dividing a network into separate security zones.

DMZ

A separate zone for systems requiring controlled external communication.

Firewall

A security device or software that controls network traffic according to rules.

VLAN

A logical network separation mechanism.

Air-Gap

Physical or logical isolation between networks.

Lateral Movement

Movement from one compromised system toward other systems within a network.

15. Key Takeaways

Remember:

Segmentation = Divide the network into security zones.

DMZ = Controlled zone between less-trusted and internal networks.

Firewall = Controls traffic between zones.

VLAN = Logical network separation.

Air-Gap = Strong network isolation.

ICS Network = Critical industrial systems requiring controlled access.

A well-designed ICS environment should use segmentation and defense-in-depth to reduce unnecessary communication and limit the impact of security incidents.
