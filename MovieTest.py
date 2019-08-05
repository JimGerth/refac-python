import unittest
from Movie import Movie

class MovieTest(unittest.TestCase):

    def test_movie(self):
        fullMetalJacket = Movie("Full Metal Jacket", Movie.REGULAR)
        self.assertEqual(fullMetalJacket.get_title(), "Full Metal Jacket")
        self.assertEqual(fullMetalJacket.get_price_code(), Movie.REGULAR)