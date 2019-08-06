
class Movie:

    CHILDRENS = 2
    REGULAR = 0
    NEW_RELEASE = 1

    def __init__(self, title, price_code):
        self._title = title
        self.set_price_code(price_code)

    def get_price_code(self):
        return self._price.get_price_code()

    def set_price_code(self, arg):
        if arg == self.REGULAR:
            from RegularPrice import RegularPrice
            self._price = RegularPrice()
        elif arg == self.CHILDRENS:
            from ChildrensPrice import ChildrensPrice
            self._price = ChildrensPrice()
        elif arg == self.NEW_RELEASE:
            from NewReleasePrice import NewReleasePrice
            self._price = NewReleasePrice()
        else:
            print('invalid price code!')

    def get_title(self):
        return self._title

    def get_charge(self, daysRented):
        return self._price.get_charge(daysRented)

    def get_frequent_renter_points(self, daysRented):
        return self._price.get_frequent_renter_points(daysRented)