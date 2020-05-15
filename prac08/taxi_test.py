# Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km

# Drive the taxi 40km

# Print the taxi's details and the current fare

# Restart the meter (start a new fare) and then drive the car 100km

# Print the details and the current fare

from prac08.taxi import Taxi


def main():
    prius_taxi = Taxi("Prius 1", 100)

    prius_taxi.drive(40)

    print(prius_taxi)

    print("Current fare : $ {:.2f}".format(prius_taxi.get_fare))

    prius_taxi.start_fare()
    prius_taxi.drive(100)

    print(prius_taxi)
    print("Current fare: $ {:.2f}".format(prius_taxi.get_fare))


if __name__ == '__main__':
    main()