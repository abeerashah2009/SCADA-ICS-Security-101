#!/bin/bash

SOURCE="/home/ubuntu/SCADA-ICS-Security-101/Lab-26-ICS-SCADA-Backup-and-Recovery-Fundamentals/scada-data/"
DEST="/home/ubuntu/SCADA-ICS-Security-101/Lab-26-ICS-SCADA-Backup-and-Recovery-Fundamentals/backup/scada/"

echo "======================================"
echo " ICS/SCADA Backup Started"
echo "======================================"

rsync -av "$SOURCE" "$DEST"

if [ $? -eq 0 ]; then
    echo "[PASS] ICS/SCADA backup completed successfully."
else
    echo "[FAIL] ICS/SCADA backup failed."
    exit 1
fi

echo "======================================"
echo " Backup Completed"
echo "======================================"
