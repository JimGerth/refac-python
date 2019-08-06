from Movie import Movie

class ChildrensPrice:

    def get_price_code(self):
        return Movie.CHILDRENS

    def get_charge(self, daysRented):
        result = 1.5
        if daysRented > 3:
            result += (daysRented - 3) * 1.5
        return result

    def get_frequent_renter_points(self, daysRented):
        return 1