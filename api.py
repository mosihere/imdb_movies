import requests

URL = "https://imdb-api.com/en/API/Top250Movies/"

def _get(url, api_key):
    response = requests.get(f'{url}{api_key}')
    response.raise_for_status()
    return response.json()
 
def get_top_250_movies(api_key):
    data = []
    for movie in _get(URL, api_key)['items']:
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
