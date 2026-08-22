#!/bin/bash

LAB_DIR="$(cd "$(dirname "$0")/.." && pwd)"
DB="$LAB_DIR/cmdb/config_management.db"

echo "========================================"
echo "LAB 39 - CONFIGURATION REVIEW"
echo "========================================"
echo
date -u
echo

PLC_FILE="$LAB_DIR/configurations/plc/plc_config.txt"
HMI_FILE="$LAB_DIR/configurations/hmi/hmi_config.xml"

PLC_HASH=$(sha256sum "$PLC_FILE" | awk '{print $1}')
HMI_HASH=$(sha256sum "$HMI_FILE" | awk '{print $1}')

echo "===== CURRENT CONFIGURATION HASHES ====="
echo "PLC: $PLC_HASH"
echo "HMI: $HMI_HASH"

echo
echo "===== APPROVED BASELINE COMPARISON ====="

PLC_BASELINE=$(sqlite3 "$DB" \
"SELECT SHA256 FROM ConfigChanges
 WHERE FileName='configurations/plc/plc_config.txt'
 ORDER BY ID ASC LIMIT 1;")

HMI_BASELINE=$(sqlite3 "$DB" \
"SELECT SHA256 FROM ConfigChanges
 WHERE FileName='configurations/hmi/hmi_config.xml'
 ORDER BY ID ASC LIMIT 1;")

echo "PLC approved baseline: $PLC_BASELINE"
echo "HMI approved baseline: $HMI_BASELINE"

echo
echo "===== REVIEW RESULTS ====="

PLC_STATUS="MISMATCH"
HMI_STATUS="MISMATCH"

if [ "$PLC_HASH" = "$PLC_BASELINE" ]; then
    PLC_STATUS="MATCH"
fi

if [ "$HMI_HASH" = "$HMI_BASELINE" ]; then
    HMI_STATUS="MATCH"
fi

echo "PLC configuration: $PLC_STATUS"
echo "HMI configuration: $HMI_STATUS"

echo
if [ "$PLC_STATUS" = "MATCH" ] && [ "$HMI_STATUS" = "MATCH" ]; then
    echo "REVIEW RESULT: CONFIGURATIONS MATCH APPROVED BASELINE"
    exit 0
else
    echo "REVIEW RESULT: DISCREPANCY DETECTED"
    exit 1
fi
