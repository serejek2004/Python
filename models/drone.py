from abc import ABC, abstractmethod

"""
    Represents a drone with speed, altitude, battery capacity, and battery level attributes.
"""


class AbstractDrone(ABC):
    def __init__(self, current_speed, current_altitude):
        """
            Initializes a new instance of the Drone class.
        """
        self.current_speed = current_speed
        self.current_altitude = current_altitude

    @abstractmethod
    def calculate_max_flying_distance_at_current_speed(self):
        """
            Calculate max flying distance with current speed
        """
        pass

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
