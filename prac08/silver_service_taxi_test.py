"""
CP1404/CP5632 Practical - Suggested Solution
SilverServiceTaxi class tests
"""
# to see that your SilverServiceTaxi calculates fares correctly
# For an 18km trip in a SilverServiceTaxi with fanciness of 2, the fare should be $48.78 (yikes!)
from prac08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    print(hummer)
    hummer.start_fare()
    hummer = SilverServiceTaxi("Hummer", 200, 2)
    hummer.drive(18)
    print(hummer)


if __name__ == '__main__':
    main()
