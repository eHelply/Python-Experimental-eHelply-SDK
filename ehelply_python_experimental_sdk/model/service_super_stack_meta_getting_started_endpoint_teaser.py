# coding: utf-8

"""
    eHelply SDK - 1.1.116

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.116
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


class ServiceSuperStackMetaGettingStartedEndpointTeaser(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    _required_property_names = set((
        'path',
        'method',
        'description',
    ))
    path = StrSchema
    method = StrSchema
    description = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        path: path,
        method: method,
        description: description,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'ServiceSuperStackMetaGettingStartedEndpointTeaser':
        return super().__new__(
            cls,
            *args,
            path=path,
            method=method,
            description=description,
            _configuration=_configuration,
            **kwargs,
        )
