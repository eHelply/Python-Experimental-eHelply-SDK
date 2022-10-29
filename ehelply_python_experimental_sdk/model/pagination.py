# coding: utf-8

"""
    eHelply SDK - 1.1.119

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.119
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


class Pagination(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Pagination state
    """
    _required_property_names = set((
        'current_page',
        'page_size',
        'total_items',
        'total_pages',
        'has_previous_page',
        'has_next_page',
    ))
    current_page = IntSchema
    page_size = IntSchema
    total_items = IntSchema
    total_pages = IntSchema
    has_previous_page = BoolSchema
    has_next_page = BoolSchema
    previous_page = IntSchema
    next_page = IntSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        current_page: current_page,
        page_size: page_size,
        total_items: total_items,
        total_pages: total_pages,
        has_previous_page: has_previous_page,
        has_next_page: has_next_page,
        previous_page: typing.Union[previous_page, Unset] = unset,
        next_page: typing.Union[next_page, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'Pagination':
        return super().__new__(
            cls,
            *args,
            current_page=current_page,
            page_size=page_size,
            total_items=total_items,
            total_pages=total_pages,
            has_previous_page=has_previous_page,
            has_next_page=has_next_page,
            previous_page=previous_page,
            next_page=next_page,
            _configuration=_configuration,
            **kwargs,
        )
