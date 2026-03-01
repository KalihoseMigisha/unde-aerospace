from dronekit import connect, VehicleMode

class DroneCommander:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.vehicle = None

    def establish_connection(self):
        print(f"Unde Aerospace: Connecting to Giant at {self.connection_string}")
        # vehicle = connect(self.connection_string, wait_ready=True)
        # self.vehicle = vehicle