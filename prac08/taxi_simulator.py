"""
CP1404/CP5632 Practical
Taxi simulator
"""
from prac08.taxi import Taxi
from prac08.silver_service_taxi import SilverServiceTaxi

menu = """
    q)uit
    c)hoose
    d)rive
    """


def main():
    current_taxi = None
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!", menu)
    choice_of_menu = input(">>>").upper()
    while choice_of_menu != "Q":
        if choice_of_menu == 'C':
            current_taxi = taxi_choose_system(taxis)
        elif choice_of_menu == 'D':
            total_bill = drive_system(current_taxi, total_bill)
        else:
            print("Invalid menu choice")
        print("Bill to date: ${:.2f}".format(total_bill))
        print(menu)
        choice_of_menu = input(">>>").upper()
    if choice_of_menu == "Q":
        quit_system(total_bill, taxis)


def taxi_choose_system(taxis):
    print("Taxis available :")
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))
    taxi_choice = int(input("Choose taxi: "))
    current_taxi = taxis[taxi_choice]
    return current_taxi


def drive_system(current_taxi, total_bill):
    current_taxi.start_fare()
    distance_to_drive = int(input("Drive how far?"))
    current_taxi.drive(distance_to_drive)
    cost_of_trip = current_taxi.get_fare()
    print("Your {} trip cost you ${:.2f}".format(current_taxi.name,
                                                 cost_of_trip))
    total_bill += cost_of_trip
    return total_bill


def quit_system(total_bill, taxis):
    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


if __name__ == '__main__':
    main()