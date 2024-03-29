import grpc
from api import get_top_250_movies, get_top_250_series, search_movie, search_series
import movie_service_pb2
import movie_service_pb2_grpc
from concurrent import futures


class MovieService(movie_service_pb2_grpc.TopMoviesServicer):
    def GetTop250Movies(self, request, context):
        api_key = request.api_key

        movies = get_top_250_movies(api_key)
        return movie_service_pb2.MovieArray(movies=movies)
    
    def GetTop250Series(self, request, context):
        api_key = request.api_key

        series = get_top_250_series(api_key)
        return movie_service_pb2.SeriesArray(series=series)
    
    def SearchMovie(self, request, context):
        api_key = request.api_key
        expression = request.expression

        results = search_movie(api_key, expression)
        return movie_service_pb2.SearchMovieArray(searchMovie=results)

    def SearchSeries(self, request, context):
        api_key = request.api_key
        expression = request.expression

        results = search_series(api_key, expression)
        return movie_service_pb2.SearchSeriesArray(series_array=results)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    movie_service_pb2_grpc.add_TopMoviesServicer_to_server(
        MovieService(),
        server
    )
    server.add_insecure_port("127.0.0.1:50051")
    server.start()
    server.wait_for_termination()


def main():
    if __name__ == "__main__":
        print("server is up and running on port 50051:\n")
        serve()

main()