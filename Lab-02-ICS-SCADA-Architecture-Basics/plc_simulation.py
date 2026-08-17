LED = False

print("PLC LED Toggle Simulation")
print("-------------------------")

for scan in range(1, 6):
    LED = not LED
    print(f"PLC Scan {scan}: LED = {LED}")

