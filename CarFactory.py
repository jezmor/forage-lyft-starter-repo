from datetime import date
import battery
import engine
from car import Car as car
from abc import ABC, abstractmethod


class CarFactory(ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, warning_light_on):

        self.current_date = date.today()
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.warning_light_on = warning_light_on

    @abstractmethod
    def create_calliope(self):
        self.engine = engine.CapuletEngine
        self.battery = battery.spindlerbattery

        return car
    
    @abstractmethod
    def create_glissade(self):
        self.engine = engine.WilloughbyEngine
        self.battery = battery.spindlerbattery

        return car

    @abstractmethod
    def create_palindrome(self):
        self.engine = engine.SternmanEngine
        self.battery = battery.spindlerbattery

        return car

    @abstractmethod
    def create_rorschach(self):
        self.engine = engine.WilloughbyEngine
        self.battery = battery.nubbinbattery
    
        return car
        
    @abstractmethod
    def create_thovex(self):
        self.engine = engine.CapuletEngine
        self.battery = battery.nubbinbattery
        
        return car
