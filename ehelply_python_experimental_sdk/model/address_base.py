# coding: utf-8

"""
    eHelply SDK - 1.1.98

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.98
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


class AddressBase(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    **:param** address_type                        **type:** string or None

**:param** address_line_1                      **type:** string or None

**:param** address_line_2                      **type:** string or None

**:param** postal_zip_code                     **type:** string or None

**:param** city                                **type:** string or None

**:param** province_state                      **type:** string or None

**:param** country                             **type:** string or None

**:param** lat                                 **type:** string or None

**:param** lng                                 **type:** string or None
    """
    address_type = StrSchema
    address_line_1 = StrSchema
    address_line_2 = StrSchema
    postal_zip_code = StrSchema
    city = StrSchema
    province_state = StrSchema
    country = StrSchema
    lat = StrSchema
    lng = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        address_type: typing.Union[address_type, Unset] = unset,
        address_line_1: typing.Union[address_line_1, Unset] = unset,
        address_line_2: typing.Union[address_line_2, Unset] = unset,
        postal_zip_code: typing.Union[postal_zip_code, Unset] = unset,
        city: typing.Union[city, Unset] = unset,
        province_state: typing.Union[province_state, Unset] = unset,
        country: typing.Union[country, Unset] = unset,
        lat: typing.Union[lat, Unset] = unset,
        lng: typing.Union[lng, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'AddressBase':
        return super().__new__(
            cls,
            *args,
            address_type=address_type,
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            postal_zip_code=postal_zip_code,
            city=city,
            province_state=province_state,
            country=country,
            lat=lat,
            lng=lng,
            _configuration=_configuration,
            **kwargs,
        )
