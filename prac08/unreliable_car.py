"""
CP1404/CP5632 Practical
unreliable_car class
"""
from random import uniform

from prac08.car import Car


class UnreliableCar(Car):
    """an UnreliableCar that inherits from Car"""
    price_per_km = 1.23

    def __init__(self, name, fuel, reliability=0):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability
        self.current_fare_distance = 0

    def __str__(self):
        return "{}, reliability number is {}".format(super().__str__(),
                                                     self.reliability, )

    def drive(self, distance):
        """Drive the car, only sometimes, based on reliability."""
        random_number = uniform(1, 100)
        if random_number <= self.reliability:
            print("The number is {}, less than car's reliability, you can drive.".format(random_number))
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
            print("The number is {}, bigger than car's reliability, you can not drive.".format(random_number))
        return distance_driven
