from abc import ABC
from dateutils import timedelta

class Battery(ABC):
    def needs_service(self):
        pass

class nubbinbattery(ABC):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        servicepoint = self.current_date - timedelta(days=(4*365.24)) #4 year service interval

        if self.last_service_date < servicepoint:
            return True
        
        return False

class spindlerbattery(ABC):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        servicepoint = self.current_date - timedelta(days=(3*365.24)) #2 year service interval

        if self.last_service_date < servicepoint:
            return True
        
        return False
