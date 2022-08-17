# coding: utf-8

"""
    eHelply SDK - 1.1.102

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.102
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


class UserFlags(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Flags that may be attached to a user
    """
    requires_tour = BoolSchema
    missing_data = BoolSchema
    legal_updates = BoolSchema
    newsletters = BoolSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        requires_tour: typing.Union[requires_tour, Unset] = unset,
        missing_data: typing.Union[missing_data, Unset] = unset,
        legal_updates: typing.Union[legal_updates, Unset] = unset,
        newsletters: typing.Union[newsletters, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'UserFlags':
        return super().__new__(
            cls,
            *args,
            requires_tour=requires_tour,
            missing_data=missing_data,
            legal_updates=legal_updates,
            newsletters=newsletters,
            _configuration=_configuration,
            **kwargs,
        )
