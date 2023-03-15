# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: movie_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13movie_service.proto\"\x1f\n\x0cMovieRequest\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\"\x9b\x01\n\x05Movie\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04rank\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x11\n\tfullTitle\x18\x04 \x01(\t\x12\x0c\n\x04year\x18\x05 \x01(\t\x12\r\n\x05image\x18\x06 \x01(\t\x12\x0c\n\x04\x63rew\x18\x07 \x01(\t\x12\x12\n\nimDbRating\x18\x08 \x01(\t\x12\x17\n\x0fimDbRatingCount\x18\t \x01(\t\"$\n\nMovieArray\x12\x16\n\x06movies\x18\x01 \x03(\x0b\x32\x06.Movie\" \n\rSeriesRequest\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\"\x9c\x01\n\x06Series\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04rank\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x11\n\tfullTitle\x18\x04 \x01(\t\x12\x0c\n\x04year\x18\x05 \x01(\t\x12\r\n\x05image\x18\x06 \x01(\t\x12\x0c\n\x04\x63rew\x18\x07 \x01(\t\x12\x12\n\nimDbRating\x18\x08 \x01(\t\x12\x17\n\x0fimDbRatingCount\x18\t \x01(\t\"\'\n\x0cSerriesArray\x12\x17\n\x06series\x18\x01 \x03(\x0b\x32\x07.Series2p\n\tTopMovies\x12/\n\x0fGetTop250Movies\x12\r.MovieRequest\x1a\x0b.MovieArray\"\x00\x12\x32\n\x0fGetTop250Series\x12\x0e.SeriesRequest\x1a\r.SerriesArray\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'movie_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MOVIEREQUEST._serialized_start=23
  _MOVIEREQUEST._serialized_end=54
  _MOVIE._serialized_start=57
  _MOVIE._serialized_end=212
  _MOVIEARRAY._serialized_start=214
  _MOVIEARRAY._serialized_end=250
  _SERIESREQUEST._serialized_start=252
  _SERIESREQUEST._serialized_end=284
  _SERIES._serialized_start=287
  _SERIES._serialized_end=443
  _SERRIESARRAY._serialized_start=445
  _SERRIESARRAY._serialized_end=484
  _TOPMOVIES._serialized_start=486
  _TOPMOVIES._serialized_end=598
# @@protoc_insertion_point(module_scope)
