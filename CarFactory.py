from battery import spindlerbattery\
    ,nubbinbattery
    
from engine import WilloughbyEngine \
    ,SternmanEngine \
    ,CapuletEngine
from car import Car


class carfactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = spindlerbattery(current_date,last_service_date)
        car = Car(engine,battery)
        
        return car
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = spindlerbattery(current_date,last_service_date)
        car = Car(engine,battery)

        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        battery = spindlerbattery(current_date,last_service_date)
        car = Car(engine,battery)

        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = nubbinbattery(current_date,last_service_date)
        car = Car(engine,battery)

        return car
        
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = nubbinbattery(current_date,last_service_date)
        car = Car(engine,battery)

        return car
