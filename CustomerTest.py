import unittest
from Customer import Customer
from Rental import Rental
from Movie import Movie

class CustomerTest(unittest.TestCase):

    def test_customer(self):
        jerry = Customer("Jerry")
        self.assertEqual(jerry.get_name(), "Jerry")

    def test_statement(self):
        tom = Customer("Tom")
        tom.add_rental(Rental(Movie("Shutter Island", Movie.REGULAR), 5))
        tom.add_rental(Rental(Movie("Inception", Movie.REGULAR), 3))
        tom.add_rental(Rental(Movie("The Shining", Movie.REGULAR), 9))
        self.assertEqual(tom.statement(), "Rental Record for Tom\n\tShutter Island\t6.5\n\tInception\t3.5\n\tThe Shining\t12.5\nAmount owed is 22.5\nYou earned 3 frequent renter points")
