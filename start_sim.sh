#!/bin/bash
# 1. Clear ghost processes to avoid port conflicts [cite: 2026-02-15]
echo "Cleaning up old sessions..."
killall -9 apm mavproxy.py 2>/dev/null

# 2. Start SITL in the background [cite: 2026-02-15]
echo "Starting Drone Brain (Mwanza)..."
uv run dronekit-sitl copter-3.3 --home=-2.516,32.901,0,0 &
sleep 7

# 3. Start MAVProxy Bridge using your specific WSL IP [cite: 2026-02-15]
echo "Starting MAVLink Bridge on 172.19.186.143:14550..."
uv run mavproxy.py --master=tcp:127.0.0.1:5760 --out=udp:172.19.186.143:14550
