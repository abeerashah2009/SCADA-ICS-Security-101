# Lab 10 - ICS/SCADA Data Flow Diagram

## Simplified Architecture

```text
+----------------+
|    Sensors     |
|----------------|
| Temperature    |
| Pressure       |
| Flow           |
+-------+--------+
        |
        | Process Data
        v
+----------------+
|      PLC       |
|----------------|
| Control Logic  |
| Data Processing|
+-------+--------+
        |
        | Industrial Protocol
        | Example: Modbus
        v
+----------------+
|  SCADA Server  |
|----------------|
| Monitoring     |
| Data Collection|
| Alarms         |
+-------+--------+
        |
        | Supervisory Information
        v
+----------------+
| HMI / Operator |
|----------------|
| Process Values |
| Alarms         |
| Status         |
+----------------+
Data Direction
Sensors
   |
   v
PLC
   |
   v
SCADA Server
   |
   v
HMI / Operator
Security Weak Points

Potential weak points include:

Network latency
Packet loss
Limited bandwidth
Poor segmentation
Weak authentication
Unencrypted industrial protocols
Single points of failure
Excessive network exposure
Security Controls

Potential controls include:

Network segmentation
Industrial firewalls
Access control
Monitoring
Secure remote access
Backup and recovery
Change management
Controlled maintenance
Protocol

The laboratory uses a conceptual/simulated representation of industrial
communication.

No real industrial protocol traffic is generated toward external devices.

Safety

This diagram represents a laboratory simulation only.

No real PLC, SCADA server, HMI, or industrial process was contacted.
