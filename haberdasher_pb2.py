# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: haberdasher.proto
# Protobuf Python Version: 5.29.0-rc3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    0,
    '',
    'haberdasher.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11haberdasher.proto\x12\x19twirp.example.haberdasher\"\x16\n\x08ValuteId\x12\n\n\x02id\x18\x01 \x01(\t\"<\n\nDollarRate\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tchar_code\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x02\x32j\n\x0bHaberdasher\x12[\n\rGetDollarRate\x12#.twirp.example.haberdasher.ValuteId\x1a%.twirp.example.haberdasher.DollarRateB$Z\"github.com/example/rpc/haberdasherb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'haberdasher_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\"github.com/example/rpc/haberdasher'
  _globals['_VALUTEID']._serialized_start=48
  _globals['_VALUTEID']._serialized_end=70
  _globals['_DOLLARRATE']._serialized_start=72
  _globals['_DOLLARRATE']._serialized_end=132
  _globals['_HABERDASHER']._serialized_start=134
  _globals['_HABERDASHER']._serialized_end=240
# @@protoc_insertion_point(module_scope)