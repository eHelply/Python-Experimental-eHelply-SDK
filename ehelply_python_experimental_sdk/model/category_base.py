# coding: utf-8

"""
    eHelply SDK - 1.1.112

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.112
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


class CategoryBase(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    **:param** name                                **type:** string
**:param** meta                                **type:** dict or None

**:param** project_uuid                        **type:** string or None
    """
    _required_property_names = set((
        'name',
    ))
    name = StrSchema
    meta_uuid = StrSchema
    meta = DictSchema
    project_uuid = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        name: name,
        meta_uuid: typing.Union[meta_uuid, Unset] = unset,
        meta: typing.Union[meta, Unset] = unset,
        project_uuid: typing.Union[project_uuid, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'CategoryBase':
        return super().__new__(
            cls,
            *args,
            name=name,
            meta_uuid=meta_uuid,
            meta=meta,
            project_uuid=project_uuid,
            _configuration=_configuration,
            **kwargs,
        )
