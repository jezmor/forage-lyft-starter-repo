from abc import ABC, abstractmethod
from CarFactory import CarFactory
from serviceable import serviceable

class Car(CarFactory, ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()