"""
    packages models
"""
from decorators.meansure_time import measure_time
from decorators.save_results_in_file import save_result_to_file
from models.delivery_drone import DeliveryDrone
from models.petrol_drone import PetrolDrone
from models.electric_drone import ElectricDrone
from models.underwater_drone import UnderwaterDrone


class DroneManager:
    """
        DroneManager class with list drones
    """

    def __init__(self):
        """
             Initializes a new instance of the DroneManager class.
        """
        self.drones = []

    def add_drone(self, input_drone):
        """
             Method add drone to list in DroneManager
        """
        self.drones.append(input_drone)

    def find_all_with_speed_greater_than(self, speed):
        """
             Find all with speed greater than ***
        """
        return list(filter(lambda needle_drone: needle_drone.current_speed > speed, self.drones))

    def find_all_with_altitude_greater_than(self, altitude):
        """
             Find all with altitude greater than ***
        """
        return filter(lambda needle_drone: needle_drone.current_altitude > altitude, self.drones)

    def print_drones(self):
        """
             Print list of Drones in DroneManager
        """
        for drone_object in self.drones:
            print(drone_object)

    def __len__(self):
        """
        Get the number of drones in the DroneManager.
        """
        return len(self.drones)

    def __getitem__(self, drone_object):
        """
        Get the drone at the specified index.
        """
        return self.drones[drone_object]

    def __iter__(self):
        """
        Return an iterator over the drones in the DroneManager.
        """
        return iter(self.drones)

    @save_result_to_file
    def get_max_flying_distances(self):
        """
        Returns a list of max flying distances for each drone in the manager.
        """
        # pylint: disable= line-too-long
        return [drone_object.calculate_max_flying_distance_at_current_speed() for drone_object in self.drones]

    @measure_time
    def get_drone_enumeration(self):
        """
        Returns a list of tuples containing the drone object and its index in the manager.
        """
        # pylint: disable= line-too-long
        return list((index_drone, drone_object) for index_drone, drone_object in enumerate(self.drones))

    def get_drone_method_value(self):
        # pylint: disable= line-too-long
        """
        Returns a list of tuples containing the drone object and the result of calling the do_something() method.
        """
        value = self.get_max_flying_distances()
        # pylint: disable= line-too-long
        return [f"{drone_object} Result: {result} " for drone_object, result in zip(self.drones, value)]

    def check_condition(self, condition):
        """
        Check the condition for objects in the manager.
        Returns a dictionary with "all" and "any" keys and corresponding boolean values.
        """
        all_condition = all(condition(drone_object) for drone_object in self.drones)
        any_condition = any(condition(drone_object) for drone_object in self.drones)
        return {"all": all_condition, "any": any_condition}


if __name__ == '__main__':
    manager = DroneManager()

    drones = [DeliveryDrone(10, 50, 50, 0, 0),
              DeliveryDrone(50, 100, 600, 400, 100),
              PetrolDrone(15, 50, 30, 70, 90),
              PetrolDrone(100, 200, 300, 400, 500),
              ElectricDrone(300, 400, 500, 100, 200),
              ElectricDrone(150, 178, 459, 493, 584),
              UnderwaterDrone(334, 345, 567, 678, 567),
              UnderwaterDrone(346, 132, 136, 678, 355), ]

    for drone in drones:
        drone.calculate_max_flying_distance_at_current_speed()
        manager.add_drone(drone)

    drones[1].charge_battery(2000)
    drones[4].charge_battery(5000)
    drones[5].use_battery(555)
