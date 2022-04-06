import unittest
from datetime import datetime
import os, sys

p = os.path.abspath('.'); sys.path.insert(1, p) #update path to account for modules being part of root package

from CarFactory import carfactory
from engine import CapuletEngine \
    ,SternmanEngine \
    ,WilloughbyEngine

from battery import nubbinbattery \
    ,spindlerbattery

from tires import carrigantires \
    ,octoprimetires

today = datetime.today().date()
current_date = today

#smoke car factory
class test_models_needs_service(unittest.TestCase):
    def test_calliope_should_be_services(self):
        last_service_date = today.replace(year=today.year-3)
        last_service_mileage = 0
        current_mileage = 30001

        car = carfactory.create_calliope(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_calliope_not_needs_service(self):
        last_service_date = today.replace(year=today.year-2)
        last_service_mileage = 0
        current_mileage = 2999

        car = carfactory.create_calliope(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertFalse(car.needs_service())

class test_battery(unittest.TestCase):
    #nubbin Battery
    def test_nubbin_battery_needs_service(self):
        last_service_date = today.replace(year=today.year-5)
        battery = nubbinbattery(current_date,last_service_date)
        
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_not_needs_service(self):
        last_service_date = today.replace(year=today.year-3)
        battery = nubbinbattery(current_date,last_service_date)
        
        self.assertFalse(battery.needs_service())

    #spindler Battery
    def test_spindler_battery_needs_service(self):
        last_service_date = today.replace(year=today.year-3)
        battery = spindlerbattery(current_date,last_service_date)
        
        self.assertTrue(battery.needs_service())

    def test_spindler_battery_not_needs_service(self):
        last_service_date = today.replace(year=today.year-2)
        battery = spindlerbattery(current_date,last_service_date)
        
        self.assertFalse(battery.needs_service())

class test_engine(unittest.TestCase):
    #Capulet Engine
    def test_capulet_engine_needs_service(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage,last_service_mileage)

        self.assertTrue(engine.needs_service())
        
    def test_capulet_engine_not_needs_service(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage,last_service_mileage)

        self.assertFalse(engine.needs_service())

    #Willoughby Engine
    def test_willoughby_engine_needs_service(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage,last_service_mileage)

        self.assertTrue(engine.needs_service())
        
    def test_willoughby_engine_not_needs_service(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage,last_service_mileage)

        self.assertFalse(engine.needs_service())

    #Sternman Engine
    def test_sternman_engine_needs_service(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)

        self.assertTrue(engine.needs_service())
        
    def test_sternman_engine_not_needs_service(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)

        self.assertFalse(engine.needs_service())

class test_wear_sensors(unittest.TestCase):
    #carrigan tires
    def test_carrigan_needs_service(self):
        wear_sensors = (0.91, 0.3, 0.3, 0.4)
        tires = carrigantires(wear_sensors)

        self.assertTrue(tires.needs_service())

    def test_carrigan_not_needs_service(self):
        wear_sensors = (0.89, 0.3, 0.3, 0.4)
        tires = carrigantires(wear_sensors)

        self.assertFalse(tires.needs_service())

    #octoprime tires
    def test_octoprime_needs_service(self):
        wear_sensors = (0.91, 0.94, 0.81, 0.5)
        tires = octoprimetires(wear_sensors)

        self.assertTrue(tires.needs_service())

    def test_octoprimetires_not_needs_service(self):
        wear_sensors = (0.89, 0.3, 0.3, 0.4)
        tires = octoprimetires(wear_sensors)

        self.assertFalse(tires.needs_service())

if __name__ == '__main__':
    unittest.main()
