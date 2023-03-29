import requests
from typing import List, Dict


TOP_250_MOVIES_URL = "https://imdb-api.com/en/API/Top250Movies/"
TOP_250_SERIES_URL = "https://imdb-api.com/en/API/Top250TVs/"
SEARCH_MOVIE_URL = "https://imdb-api.com/en/API/SearchMovie/"
SEARCH_SERIES_URL = "https://imdb-api.com/en/API/SearchSeries/"

def _get(url, api_key, expression = ''):
    response = requests.get(f'{url}{api_key}/{expression}')
    response.raise_for_status()
    return response.json()
 
def get_top_250_movies(api_key: str) -> List[Dict]:
    '''
    This function takes a single argument as api_key
    and returns a list of dicts --> top 250 movies

    Args:
        api_key: str

    Returns: List(Dict)
    '''

    data = []
    for movie in _get(TOP_250_MOVIES_URL, api_key)['items']:
        movie_info = {
            'id' : movie.get('id'),
            'rank': movie.get('rank'),
            'title': movie.get('title'),
            'fullTitle': movie.get('fullTitle'),
            'year': movie.get('year'),
            'image': movie.get('image'),
            'crew': movie.get('crew'),
            'imDbRating': movie.get('imDbRating'),
            'imDbRatingCount': movie.get('imDbRatingCount'),
        }
        data.append(movie_info)

    return data

def get_top_250_series(api_key: str) -> List[Dict]:
    '''
    This function takes a single argument as api_key
    and returns a list of dicts --> top 250 series

    Args:
        api_key: str
    
    Returns: List(Dict)
    '''

    data = []
    for series in _get(TOP_250_SERIES_URL, api_key)['items']:
        series_info = {
            'id' : series.get('id'),
            'rank': series.get('rank'),
            'title': series.get('title'),
            'fullTitle': series.get('fullTitle'),
            'year': series.get('year'),
            'image': series.get('image'),
            'crew': series.get('crew'),
            'imDbRating': series.get('imDbRating'),
            'imDbRatingCount': series.get('imDbRatingCount'), 
        }
        data.append(series_info)
    
    return data

def search_movie(api_key: str, expression: str) -> List[Dict]:
    '''
    This function get a single argument as an api-key
    then returns the list of movies based on search keyword.

    Args:
        api_key: str

    Returns: List[Dict]
    '''

    data = []
    for movie in _get(SEARCH_MOVIE_URL, api_key, expression)['results']:
        movie_info = {
            'Id': movie.get('id'),
            'ResultType': movie.get('resultType'),
            'Image': movie.get('image'),
            'Title': movie.get('title'),
            'Description': movie.get('description'),
        }
        data.append(movie_info)
    
    return data

def search_series(api_key: str, expression: str) -> List[Dict]:
    '''
    This function get a single argument as an api-key
    then returns the list of series based on search keyword.

    Args:
        api_key: str

    Returns: List[Dict]
    '''

    data = []
    for series in _get(SEARCH_SERIES_URL, api_key, expression)['results']:
        series_info = {
            'Id': series.get('id'),
            'ResultType': series.get('resultType'),
            'Image': series.get('image'),
            'Title': series.get('title'),
            'Description': series.get('description'),
        }
        data.append(series_info)
    
    return data