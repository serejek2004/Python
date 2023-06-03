"""
    packages models
"""
import time

from decorators import meansure_time
from decorators.logging import logged
from models.drone import AbstractDrone
from exceptions.exit_from_fuel_zone import ExitFromTheFuelAccessZone


class DeliveryDrone(AbstractDrone):
    """
        Represents a drone with speed, altitude, battery capacity, and battery level attributes.
    """

    # pylint: disable= too-many-arguments
    def __init__(self, current_speed, current_altitude, battery_capacity,
                 current_battery_level, consumption_battery):
        """
            Initializes a new instance of the Drone class.
        """
        super().__init__(current_speed, current_altitude)
        self.battery_capacity = battery_capacity
        self.current_battery_level = current_battery_level
        self.consumption_battery = consumption_battery
        self.current_max_flying_distance = None
        self.best_cargo = {"Food", "Drinks"}

    def __iter__(self):
        return iter(self.best_cargo)

    @logged(ExitFromTheFuelAccessZone, "file")
    def use_battery(self, amount):
        """
            Reduces the current battery level of the drone by the specified amount.
        """
        if self.current_battery_level - amount > 0:
            self.current_battery_level -= amount
        else:
            raise ExitFromTheFuelAccessZone

    @logged(ExitFromTheFuelAccessZone, "console")
    def charge_battery(self, amount):
        """
            Increases the current battery level of the drone by the specified amount.
        """
        if amount+self.current_battery_level <= self.battery_capacity:
            self.current_battery_level += amount
        else:
            raise ExitFromTheFuelAccessZone

    def calculate_max_flying_distance_at_current_speed(self):
        """
            Calculate max flying distance with current speed
        """
        # pylint: disable= line-too-long
        try:
            self.current_max_flying_distance = (self.current_battery_level / self.consumption_battery) * 100
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
               f"battery_capacity={self.battery_capacity}, " \
               f"current_battery_level={self.current_battery_level}, " \
               f"consumption_battery={self.consumption_battery}, " \
               f"max_flying_distance={self.current_max_flying_distance}, " \
               f"best_cargo={self.best_cargo}"
