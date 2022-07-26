# coding: utf-8

"""
    eHelply SDK - 1.1.118

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.118
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401
import functools  # noqa: F401

from frozendict import frozendict  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from ehelply_python_experimental_sdk.schemas import (  # noqa: F401
    AnyTypeSchema,
    ComposedSchema,
    DictSchema,
    ListSchema,
    StrSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    NumberSchema,
    UUIDSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    Configuration,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    Int32Base,
    Int64Base,
    Float32Base,
    Float64Base,
    NumberBase,
    UUIDBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)


class NoteMeta(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Metadata associated to a note
    """
    _required_property_names = set((
        'author',
    ))
    original_author = StrSchema
    author = StrSchema
    previous_version = StrSchema
    next_version = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        author: author,
        original_author: typing.Union[original_author, Unset] = unset,
        previous_version: typing.Union[previous_version, Unset] = unset,
        next_version: typing.Union[next_version, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'NoteMeta':
        return super().__new__(
            cls,
            *args,
            author=author,
            original_author=original_author,
            previous_version=previous_version,
            next_version=next_version,
            _configuration=_configuration,
            **kwargs,
        )
