from abc import ABC

class Tires(ABC):
    def needs_service(self):
        pass

class carrigantires(ABC):
    def __init__(self, wear_sensors):
        self.wear_sensors = wear_sensors

    def needs_service(self):
        #check for wear sensors with wear > .9
        for i in self.wear_sensors:
            if i > 0.9:
                return True
        
        return False

class octoprimetires(ABC):
    def __init__(self, wear_sensors):
        self.wear_sensors = wear_sensors

    def needs_service(self):
        wear_sensor_sum = float(0.0)

        #generate sum of wear sensors
        for i in self.wear_sensors:
            wear_sensor_sum += i
        
        if wear_sensor_sum >= 3.0:
            return True
        
        return False