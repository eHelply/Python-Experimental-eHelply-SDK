# coding: utf-8

"""
    eHelply SDK - 1.1.104

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.104
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


class SecurityEncryptionKeyResponse(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    _required_property_names = set((
        'uuid',
        'key',
        'category',
        'deleted_at',
        'created_at',
        'retrieved_at',
    ))
    uuid = StrSchema
    key = BinarySchema
    category = StrSchema
    deleted_at = StrSchema
    created_at = StrSchema
    retrieved_at = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        uuid: uuid,
        key: key,
        category: category,
        deleted_at: deleted_at,
        created_at: created_at,
        retrieved_at: retrieved_at,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'SecurityEncryptionKeyResponse':
        return super().__new__(
            cls,
            *args,
            uuid=uuid,
            key=key,
            category=category,
            deleted_at=deleted_at,
            created_at=created_at,
            retrieved_at=retrieved_at,
            _configuration=_configuration,
            **kwargs,
        )
