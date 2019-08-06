
class Movie:

    CHILDRENS = 2
    REGULAR = 0
    NEW_RELEASE = 1

    def __init__(self, title, price_code):
        self._title = title
        self._price_code = price_code

    def get_price_code(self):
        return self._price_code

    def set_price_code(self, arg):
        self._price_code = arg

    def get_title(self):
        return self._title

    def get_charge(self, daysRented):
        result = 0.0
        if self.get_price_code() == Movie.REGULAR:
            result += 2
            if daysRented > 2:
                result += (daysRented - 2) * 1.5

        elif self.get_price_code() == Movie.NEW_RELEASE:
            result += daysRented * 3

        elif self.get_price_code() == Movie.CHILDRENS:
            result += 1.5
            if daysRented > 3:
                result += (daysRented - 3) * 1.5

        return result