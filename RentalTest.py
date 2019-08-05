import unittest
from Movie import Movie
from Rental import Rental

class RentalTest(unittest.TestCase):

    def test_rental(self):
        rental = Rental(Movie("2001: A Space Odyssey", Movie.REGULAR), 14)
        self.assertEqual(rental.get_days_rented(), 14)
        self.assertEqual(rental.get_movie().get_title(), "2001: A Space Odyssey")
        self.assertEqual(rental.get_movie().get_price_code(), Movie.REGULAR)