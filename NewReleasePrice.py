from Movie import Movie

class NewReleasePrice:

    def get_price_code(self):
        return Movie.NEW_RELEASE

    def get_charge(self, daysRented):
        return daysRented * 3

    def get_frequent_renter_points(self, daysRented):
        if daysRented > 1:
            return 2
        else:
            return 1