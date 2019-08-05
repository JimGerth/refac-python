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
        total_amount = 0.0
        frequent_renter_points = 0
        result = f"Rental Recor for {self.get_name()}\n"
        for rental in self._rentals:
            this_amount = 0.0

            # determine amounts for each line
            if rental.get_movie().get_price_code() == Movie.REGULAR:
                this_amount += 2
                if rental.get_days_rented() > 2:
                    this_amount += (rental.get_days_rented() - 2) * 1.5

            elif rental.get_movie().get_price_code() == Movie.NEW_RELEASE:
                this_amount += rental.get_days_rented() * 3

            elif rental.get_movie().get_price_code() == Movie.CHILDRENS:
                this_amount += 1.5
                if rental.get_days_rented() > 3:
                    this_amount += (rental.get_days_rented() - 3) * 1.5

            # add frequent renter points
            frequent_renter_points += 1
            # add bonus for a two day new release rental
            if rental.get_movie().get_price_code() == Movie.NEW_RELEASE and rental.get_days_rented() > 1:
                frequent_renter_points += 1

            # show figures for this rental
            result += f"\t{rental.get_movie().get_title()}\t{this_amount}\n"
            total_amount += this_amount

        # add footer lines
        result += f"Amount owed is {total_amount}\n"
        result += f"You earned {frequent_renter_points} frequent renter points"
        return result