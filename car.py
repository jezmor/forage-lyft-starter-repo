from abc import ABC, abstractmethod
from CarFactory import CarFactory
from serviceable import serviceable

class Car(CarFactory, ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        serviceable.needs_service()