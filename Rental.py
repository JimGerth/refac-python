from Movie import Movie

class Rental:

    def __init__(self, movie, days_rented):
        self._movie = movie
        self._days_rented = days_rented

    def get_days_rented(self):
        return self._days_rented

    def get_movie(self):
        return self._movie

    def get_charge(self):
        result = 0.0
        if self.get_movie().get_price_code() == Movie.REGULAR:
            result += 2
            if self.get_days_rented() > 2:
                result += (self.get_days_rented() - 2) * 1.5

        elif self.get_movie().get_price_code() == Movie.NEW_RELEASE:
            result += self.get_days_rented() * 3

        elif self.get_movie().get_price_code() == Movie.CHILDRENS:
            result += 1.5
            if self.get_days_rented() > 3:
                result += (self.get_days_rented() - 3) * 1.5

        return result

    def get_frequent_renter_points(self):
        if self.get_movie().get_price_code() == Movie.NEW_RELEASE and self.get_days_rented() > 1:
            return 2
        else:
            return 1