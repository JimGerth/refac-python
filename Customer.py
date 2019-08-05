from Movie import Movie

class Customer:

    def __init__(self, name):
        self._name = name
        self._rentals = []

    def add_rental(self, arg):
        self._rentals.append(arg)

    def get_name(self):
        return self._name

    def statement(self):
        result = f"Rental Record for {self.get_name()}\n"
        for rental in self._rentals:

            # show figures for this rental
            result += f"\t{rental.get_movie().get_title()}\t{rental.get_charge()}\n"

        # add footer lines
        result += f"Amount owed is {self.get_total_charge()}\n"
        result += f"You earned {self.get_total_frequent_renter_points()} frequent renter points"
        return result

    def html_statement(self):
        result = f"<h1>Rentals for <em>{self.get_name()}</em></h1><p>\n"
        for rental in self._rentals:

            # show figures for this rental
            result += f"{rental.get_movie().get_title()}: {rental.get_charge()}<br>\n"

        # add footer lines
        result += f"<p>You owe <em>{self.get_total_charge()}</em></p>\n"
        result += f"On this rental you earned <em>{self.get_total_frequent_renter_points()}</em> frequent renter points<p>"
        return result

    def get_total_charge(self):
        result = 0.0
        for rental in self._rentals:
            result += rental.get_charge()
        return result

    def get_total_frequent_renter_points(self):
        result = 0
        for rental in self._rentals:
            result += rental.get_frequent_renter_points()
        return result