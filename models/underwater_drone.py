"""
    packages models
"""
from decorators.logging import logged
from exceptions.exit_from_fuel_zone import ExitFromTheFuelAccessZone
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

    @logged(ExitFromTheFuelAccessZone, "file")
    def use_fuel(self, amount):
        """
            Reduces the current battery level of the drone by the specified amount.
        """
        if self.current_fuel_level - amount > 0:
            self.current_fuel_level -= amount
        else:
            raise ExitFromTheFuelAccessZone

    @logged(ExitFromTheFuelAccessZone, "file")
    def refuel(self, amount):
        """
            Increases the current battery level of the drone by the specified amount.
        """
        if amount + self.current_fuel_level <= self.fuel_capacity:
            self.current_fuel_level += amount
        else:
            raise ExitFromTheFuelAccessZone

    def calculate_max_flying_distance_at_current_speed(self):
        """
            Calculate max flying distance with current speed
        """
        try:
            self.current_max_flying_distance = (self.current_fuel_level / self.consumption_fuel) * 100
        except ZeroDivisionError:
            self.current_max_flying_distance = 0
            with open("result_exception", 'a') as file:
                file.write(f"delivery_drone rise exception ZeroDivisionError " + '\n')
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
