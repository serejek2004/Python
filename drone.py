"""
    Represents a drone with speed, altitude, battery capacity, and battery level attributes.
"""


class Drone:
    """
        Represents a drone with speed, altitude, battery capacity, and battery level attributes.
    """

    __instance = None

    def __init__(self, current_speed=0, current_altitude=0, battery_capacity=0, current_battery_level=0):
        """
            Initializes a new instance of the Drone class.
        """
        self.__current_speed = current_speed
        self.current_altitude = current_altitude
        self.battery_capacity = battery_capacity
        self.current_battery_level = current_battery_level

    def fly_at(self, speed_in_meters_per_second, altitude_in_meters):
        """
            Sets the current speed and altitude of the drone.
        """
        self.__current_speed = speed_in_meters_per_second
        self.current_altitude = altitude_in_meters

    def use_battery(self, amount):
        """
            Reduces the current battery level of the drone by the specified amount.
        """
        self.current_battery_level -= amount

    def charge_battery(self, amount):
        """
            Increases the current battery level of the drone by the specified amount.
        """
        self.current_battery_level += amount

    @property
    def current_speed(self):
        return self.__current_speed

    @current_speed.setter
    def current_speed(self, amount):
        self.__current_speed = amount

    @staticmethod
    def get_instance():
        """
            Returns the singleton instance of the Drone class. If the instance does not exist, it creates a new one.
        """
        if Drone.__instance is None:
            Drone.__instance = Drone()
        return Drone.__instance

    def __str__(self):
        """
            Returns a string representation of the Drone object.
        """
        return f"current_speed={self.__current_speed}, current_altitude={self.current_altitude}, " \
               f"battery_capacity={self.battery_capacity}, current_battery_level={self.current_battery_level}"

    @staticmethod
    def pair_number_in_square(given_list):
        """
            Modifies the given list by squaring each even number in it.
        """
        new_list = []
        for index in range(len(given_list)):
            if given_list[index] % 2 == 0:
                new_list.append(given_list[index] ** 2)
        return new_list


if __name__ == '__main__':
    drones = [Drone(100, 200, 1000, 2000), Drone(), Drone.get_instance(), Drone.get_instance()]

    for drone in drones:
        print(drone)

    drones[0].current_speed = 50
    print(drones[0].current_speed)

    my_list = []

    for number in range(50):
        my_list.append(number + 1)

    print(Drone.pair_number_in_square(my_list))
