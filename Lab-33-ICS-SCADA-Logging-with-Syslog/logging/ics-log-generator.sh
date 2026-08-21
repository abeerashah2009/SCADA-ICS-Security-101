#!/bin/bash

# Lab 33 - Controlled ICS/SCADA Syslog Generator

logger -t ics-simulator "PLC-01: Process started"
logger -t ics-simulator "PLC-01: Temperature=72C"
logger -t ics-simulator "PLC-01: Pressure=4.2bar"
logger -t ics-simulator "HMI-01: Operator login successful"
logger -t ics-simulator "SCADA-01: Communication with PLC-01 established"
logger -t ics-simulator "PLC-01: Digital input changed"
logger -t ics-simulator "SCADA-01: Process monitoring active"

echo "ICS/SCADA test events generated."
