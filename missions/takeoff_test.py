import collections
import collections.abc
collections.MutableMapping = collections.abc.MutableMapping

from dronekit import connect, VehicleMode
import time

def arm_and_takeoff(target_altitude):
    print("--- UNDE AEROSPACE: FORCED TAKEOFF ---")
    
    # We connect DIRECTLY to the drone's primary port
    print("Connecting to SITL on 5760...")
    vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)

    # HONORS FIX: We set the parameters via code instead of the MAV console
    print("Sending Safety Overrides...")
    vehicle.parameters['ARMING_CHECK'] = 0
    
    print("Switching to GUIDED mode...")
    vehicle.mode = VehicleMode("GUIDED")

    print("Arming motors...")
    vehicle.armed = True

    while not vehicle.armed:
        print(" Waiting for arming signal...")
        # If it hangs here, we force it again
        vehicle.armed = True 
        time.sleep(1)

    print(f"TAKEOFF INITIATED: Climbing to {target_altitude}m")
    vehicle.simple_takeoff(target_altitude)

    while True:
        alt = vehicle.location.global_relative_frame.alt
        print(f" Altitude: {alt:.1f}m")
        if alt >= target_altitude * 0.95:
            print("Target reached! Mission Success.")
            break
        time.sleep(1)

    return vehicle

if __name__ == "__main__":
    v = arm_and_takeoff(10)
    time.sleep(5)
    print("Landing...")
    v.mode = VehicleMode("LAND")
    v.close()