# coding: utf-8

"""
    eHelply SDK - 1.1.100

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.100
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


class CatalogReturn(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    _required_property_names = set((
        'uuid',
        'project_uuid',
    ))
    meta_data = DictSchema
    name = StrSchema
    featured = DictSchema
    sub_catalogs = DictSchema
    uuid = StrSchema
    meta_uuid = StrSchema
    project_uuid = StrSchema
    
    
    class product_uuids(
        ListSchema
    ):
        _items = StrSchema
    created_at = StrSchema
    updated_at = StrSchema
    deleted_at = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        uuid: uuid,
        project_uuid: project_uuid,
        meta_data: typing.Union[meta_data, Unset] = unset,
        name: typing.Union[name, Unset] = unset,
        featured: typing.Union[featured, Unset] = unset,
        sub_catalogs: typing.Union[sub_catalogs, Unset] = unset,
        meta_uuid: typing.Union[meta_uuid, Unset] = unset,
        product_uuids: typing.Union[product_uuids, Unset] = unset,
        created_at: typing.Union[created_at, Unset] = unset,
        updated_at: typing.Union[updated_at, Unset] = unset,
        deleted_at: typing.Union[deleted_at, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'CatalogReturn':
        return super().__new__(
            cls,
            *args,
            uuid=uuid,
            project_uuid=project_uuid,
            meta_data=meta_data,
            name=name,
            featured=featured,
            sub_catalogs=sub_catalogs,
            meta_uuid=meta_uuid,
            product_uuids=product_uuids,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            _configuration=_configuration,
            **kwargs,
        )
