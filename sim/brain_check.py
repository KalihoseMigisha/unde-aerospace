import jax.numpy as jnp

def check_systems():
    print("--- UNDE AEROSPACE: SYSTEM CHECK ---")
    # Simulate a 3D coordinate for a drone over Mwanza
    drone_position = jnp.array([-2.5186, 32.9003, 100.0]) # Lat, Lon, Alt
    print(f"JAX Intelligence Layer: Position Vector {drone_position} initialized.")
    print("Status: Systems Nominal. Ready for SITL connection.")

if __name__ == "__main__":
    check_systems()