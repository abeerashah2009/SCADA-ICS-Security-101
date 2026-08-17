# Lab 06 Network Diagram: Segmented ICS and Enterprise Network

## 1. Network Architecture

The following diagram represents a basic segmented enterprise and ICS network.

```text
                         INTERNET
                            |
                            |
                      [ Edge Firewall ]
                            |
                 +----------+----------+
                 |                     |
                 v                     v
                DMZ             Corporate Network
                 |                     |
           +-----+-----+        +------+------+
           |           |        |             |
       Web Server   App Server  PCs       File Server
           |           |
           +-----+-----+
                 |
                 |
          [ Internal Firewall ]
                 |
                 v
             ICS Network
                 |
        +--------+--------+
        |        |        |
       HMI      SCADA     PLC
                         |
                    Industrial
                     Process
