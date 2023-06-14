"""
    DroneManager class with list drones
"""


class SetManager:
    """
         DroneManager class with list drones
    """
    def __init__(self, drone_manager):
        self.drone_manager = drone_manager
        self.index = 0
        self.index_cargo_list = 0

    def __len__(self):
        return sum(len(drone.best_cargo) for drone in self.drone_manager)

    def __iter__(self):
        return self

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError("Index out of range")

        for drone in self.drone_manager:
            if index < len(drone.best_cargo):
                return drone.best_cargo[index]
            index -= len(drone.best_cargo)

    def __next__(self):
        if self.index >= len(self.drone_manager):
            raise StopIteration

        drone = self.drone_manager[self.index]
        cargo_list = list(drone.best_cargo)

        if self.index_cargo_list >= len(cargo_list):
            self.index += 1
            self.index_cargo_list = 0
            return self.__next__()
        item = cargo_list[self.index_cargo_list]
        self.index_cargo_list += 1
        return item
