import unittest
from api import get_top_250_movies, get_top_250_series, search_movie


API_KEY = input('insert your api_key:\n')

class TestMovies(unittest.TestCase):
    def test_top_movies(self):
        '''
        Check response type is list or not.
        '''

        result = get_top_250_movies(API_KEY)
        self.assertIsInstance(result, list)

    def test_top_series(self):
        '''
        Check response type is list or not.
        '''

        result = get_top_250_series(API_KEY)
        self.assertIsInstance(result, list)

    def test_search_movie(self):
        '''
        Check response type is list or not.
        '''

        result = search_movie(API_KEY, 'inception')
        self.assertIsInstance(result, list)