from abc import ABC, abstractmethod
from car import Car

class serviceable(Car, ABC):        
    def needs_service(self):
        pass