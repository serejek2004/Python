"""
    packages models
"""
from models.drone import AbstractDrone


class UnderwaterDrone(AbstractDrone):
    """
        Represents a drone with speed, altitude, battery capacity, and battery level attributes
    """

    # pylint: disable= too-many-arguments
    def __init__(self, current_speed, current_altitude, fuel_capacity,
                 current_fuel_level, consumption_fuel):
        """
            Initializes a new instance of the Drone class.
        """
        super().__init__(current_speed, current_altitude)
        self.fuel_capacity = fuel_capacity
        self.current_fuel_level = current_fuel_level
        self.consumption_fuel = consumption_fuel
        self.current_max_flying_distance = None
        self.best_cargo = {"Fuel", "Camera"}

    def __iter__(self):
        return iter(self.best_cargo)

    def use_fuel(self, amount):
        """
            Reduces the current battery level of the drone by the specified amount.
        """
        self.current_fuel_level -= amount

    def refuel(self, amount):
        """
            Increases the current battery level of the drone by the specified amount.
        """
        self.current_fuel_level += amount

    def calculate_max_flying_distance_at_current_speed(self):
        """
            Calculate max flying distance with current speed
        """
        self.current_max_flying_distance = (self.current_fuel_level / self.consumption_fuel) * 100
        return self.current_max_flying_distance

    def __str__(self):
        """
            Returns a string representation of the Drone object.
        """
        return f"{super().__str__()}" \
               f"battery_capacity={self.fuel_capacity}, " \
               f"current_battery_level={self.current_fuel_level}, " \
               f"consumption_battery={self.consumption_fuel}, " \
               f"max_flying_distance={self.current_max_flying_distance}, " \
               f"best_cargo={self.best_cargo}"
