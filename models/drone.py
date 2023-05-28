"""
    packages models
"""
from abc import ABC, abstractmethod


class AbstractDrone(ABC):
    """
         Create AbstractDrone class.
    """
    def __init__(self, current_speed, current_altitude):
        """
            Initializes a new instance of the Drone class.
        """
        self.current_speed = current_speed
        self.current_altitude = current_altitude
        self.best_cargo = {}

    @abstractmethod
    def calculate_max_flying_distance_at_current_speed(self):
        """
            Calculate max flying distance with current speed
        """

    def fly_at(self, speed_in_meters_per_second, altitude_in_meters):
        """
            Sets the current speed and altitude of the drone.
        """
        self.current_speed = speed_in_meters_per_second
        self.current_altitude = altitude_in_meters

    def __str__(self):
        """
            Returns a string representation of the Drone object.
        """
        return f"current_speed={self.current_speed}, current_altitude={self.current_altitude}, "

    def get_attributes_by_data_type(self, data_type):
        # pylint: disable= line-too-long
        """
        Returns a dictionary with attributes and values of the object that match the specified data type.
        """
        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}

    def __iter__(self):
        return iter(self.best_cargo)
