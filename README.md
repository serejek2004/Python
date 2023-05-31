# Python

its a classes implement from AbstractDrone that have next fields

* current_speed -- the current speed of the drone.
* current_altitude -- the current altitude of the drone.
* battery_capacity -- drone battery capacity./fuel_capacity -- drone fuel capacity.
* current_battery_level -- the current battery level of the drone./current_fuel_level -- the current fuel level of the drone.

The AbstractDrone class have next methods

* fly_at method that puts the drone in flight at the given speed and altitude 
* calculate_current_max_flying_distance method that give max flying distance

The DroneManager class have next methods & fields

* drones (list objects AbstractDrone)
* Many magic methods
* Method add drone to list
* Method print all drones of list

The SetManager class have next methods & fields

* drone_manager field (object DroneManager)
* Many magic methods

Two decorator 

* Measure time decorator - measure time done method
* Save result to file decorator - save logs to file