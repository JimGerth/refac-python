from Movie import Movie

class RegularPrice:

    def get_price_code(self):
        return Movie.REGULAR

    def get_charge(self, daysRented):
        result = 2.0
        if daysRented > 2:
            result += (daysRented - 2) * 1.5
        return result

    def get_frequent_renter_points(self, daysRented):
        return 1