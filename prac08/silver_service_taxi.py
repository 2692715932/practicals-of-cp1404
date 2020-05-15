from prac08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness=0):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.current_fare_distance = 0
        self.price_per_km = self.price_per_km * fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return "{} plus flagfall of ${}. Total fare is {}".format(super().__str__(),
                                                                  self.flagfall,
                                                                  self.get_fare())

    def get_fare(self):
        """Get the current fare."""
        return self.flagfall + super().get_fare()