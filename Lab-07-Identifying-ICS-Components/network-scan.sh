#!/bin/bash

echo "ICS Network Discovery Scan"
echo "========================================"
echo

echo "Target: 127.0.0.1"
echo

echo "1. Host Discovery"
echo "----------------------------------------"
nmap -sn 127.0.0.1

echo
echo "2. Service and Version Detection"
echo "----------------------------------------"
nmap -sV 127.0.0.1

echo
echo "========================================"
echo "Network discovery scan completed."
echo "Target was localhost only."
echo "No external or real ICS systems were scanned."
