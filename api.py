import requests

TOP_250_MOVIES_URL = "https://imdb-api.com/en/API/Top250Movies/"
TOP_250_SERIES_URL = "https://imdb-api.com/en/API/Top250TVs/"


def _get(url, api_key):
    response = requests.get(f'{url}{api_key}')
    response.raise_for_status()
    return response.json()
 
def get_top_250_movies(api_key: str) -> list(dict):

    '''
    This function takes a single argument as api_key
    and returns a list of dicts --> top 250 movies

    Args:
        api_key: str
        
    Returns: list(dict)
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

def get_top_250_series(api_key: str) -> list(dict):
    
    '''
    This function takes a single argument as api_key
    and returns a list of dicts --> top 250 series

    Args:
        api_key: str
    
    Returns: list(dict)
    '''

    data = []
    for series in _get(TOP_250_SERIES_URL, api_key):
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