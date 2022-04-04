from datetime import date,timedelta
from abc import ABC, abstractmethod
from car import Car

class nubbinbattery(Car, ABC):    
    def __init__(self, last_service_date):
        super().__init__(last_service_date)

    @abstractmethod
    def needs_service(self):
        servicepoint = date.today() - timedelta(days=(4*365.24)) #4 year service interval

        if self.last_service_date <= servicepoint:
            return True
        
        return False

class spindlerbattery(Car, ABC):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)

    @abstractmethod
    def needs_service(self):
        servicepoint = date.today() - timedelta(days=(2*365.24)) #2 year service interval

        if self.last_service_date <= servicepoint:
            return True
        
        return False
