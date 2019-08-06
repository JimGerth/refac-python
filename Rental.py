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
        return self._movie.get_charge(self._days_rented)

    def get_frequent_renter_points(self):
        if self.get_movie().get_price_code() == Movie.NEW_RELEASE and self.get_days_rented() > 1:
            return 2
        else:
            return 1