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


class DetailedMetaGet(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Detailed meta based on Notes
    """
    summary = StrSchema
    description = StrSchema
    
    
    class summary_history(
        ListSchema
    ):
        _items = StrSchema
    
    
    class description_history(
        ListSchema
    ):
        _items = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        summary: typing.Union[summary, Unset] = unset,
        description: typing.Union[description, Unset] = unset,
        summary_history: typing.Union[summary_history, Unset] = unset,
        description_history: typing.Union[description_history, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'DetailedMetaGet':
        return super().__new__(
            cls,
            *args,
            summary=summary,
            description=description,
            summary_history=summary_history,
            description_history=description_history,
            _configuration=_configuration,
            **kwargs,
        )
