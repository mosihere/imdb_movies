# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import movie_service_pb2 as movie__service__pb2


class TopMoviesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTop250Movies = channel.unary_unary(
                '/TopMovies/GetTop250Movies',
                request_serializer=movie__service__pb2.MovieRequest.SerializeToString,
                response_deserializer=movie__service__pb2.MovieArray.FromString,
                )
        self.GetTop250Series = channel.unary_unary(
                '/TopMovies/GetTop250Series',
                request_serializer=movie__service__pb2.SeriesRequest.SerializeToString,
                response_deserializer=movie__service__pb2.SeriesArray.FromString,
                )
        self.SearchMovie = channel.unary_unary(
                '/TopMovies/SearchMovie',
                request_serializer=movie__service__pb2.SearchMovieRequest.SerializeToString,
                response_deserializer=movie__service__pb2.SearchMovieArray.FromString,
                )
        self.SearchSeries = channel.unary_unary(
                '/TopMovies/SearchSeries',
                request_serializer=movie__service__pb2.SearchSeriesRequest.SerializeToString,
                response_deserializer=movie__service__pb2.SearchSeriesArray.FromString,
                )


class TopMoviesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTop250Movies(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTop250Series(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchMovie(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchSeries(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TopMoviesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTop250Movies': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTop250Movies,
                    request_deserializer=movie__service__pb2.MovieRequest.FromString,
                    response_serializer=movie__service__pb2.MovieArray.SerializeToString,
            ),
            'GetTop250Series': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTop250Series,
                    request_deserializer=movie__service__pb2.SeriesRequest.FromString,
                    response_serializer=movie__service__pb2.SeriesArray.SerializeToString,
            ),
            'SearchMovie': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchMovie,
                    request_deserializer=movie__service__pb2.SearchMovieRequest.FromString,
                    response_serializer=movie__service__pb2.SearchMovieArray.SerializeToString,
            ),
            'SearchSeries': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchSeries,
                    request_deserializer=movie__service__pb2.SearchSeriesRequest.FromString,
                    response_serializer=movie__service__pb2.SearchSeriesArray.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TopMovies', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TopMovies(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTop250Movies(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TopMovies/GetTop250Movies',
            movie__service__pb2.MovieRequest.SerializeToString,
            movie__service__pb2.MovieArray.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTop250Series(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TopMovies/GetTop250Series',
            movie__service__pb2.SeriesRequest.SerializeToString,
            movie__service__pb2.SeriesArray.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchMovie(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TopMovies/SearchMovie',
            movie__service__pb2.SearchMovieRequest.SerializeToString,
            movie__service__pb2.SearchMovieArray.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchSeries(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TopMovies/SearchSeries',
            movie__service__pb2.SearchSeriesRequest.SerializeToString,
            movie__service__pb2.SearchSeriesArray.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
