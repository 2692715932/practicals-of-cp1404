"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("literals", 319)
    my_car.drive(277)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("{self.name}, {self.fuel}, {self.odometer}".format(self=my_car))

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(limo.fuel)
    limo.drive(115)
    print(limo.odometer)


main()