from abc import ABC, abstractmethod
from car import Car

class serviceable(Car, ABC):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)
        
    @abstractmethod
    def needs_service(self):
        if self.battery.needs_service() == True:
            return True
        elif self.engine.needs_service() == True:
            return True

        return False