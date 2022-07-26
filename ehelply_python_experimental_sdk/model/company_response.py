# coding: utf-8

"""
    eHelply SDK - 1.1.96

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.96
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


class CompanyResponse(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    **:param** name                                **type:** string
**:param** summary                             **type:** string or None

**:param** public                              **type:** bool or None

**:param** meta                                **type:** dict or None

**:param** contact                             **type:** ContactBase or None
    """
    _required_property_names = set((
        'uuid',
    ))
    name = StrSchema
    summary = StrSchema
    public = BoolSchema
    meta = DictSchema

    @classmethod
    @property
    def contact(cls) -> typing.Type['ContactBase']:
        return ContactBase
    uuid = StrSchema
    project_uuid = StrSchema
    meta_uuid = StrSchema
    
    
    class tags(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['TagBase']:
            return TagBase
    
    
    class categories(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['CategoryBase']:
            return CategoryBase
    
    
    class places(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['PlaceBase']:
            return PlaceBase
    created_at = StrSchema
    updated_at = StrSchema
    deleted_at = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        uuid: uuid,
        name: typing.Union[name, Unset] = unset,
        summary: typing.Union[summary, Unset] = unset,
        public: typing.Union[public, Unset] = unset,
        meta: typing.Union[meta, Unset] = unset,
        contact: typing.Union['ContactBase', Unset] = unset,
        project_uuid: typing.Union[project_uuid, Unset] = unset,
        meta_uuid: typing.Union[meta_uuid, Unset] = unset,
        tags: typing.Union[tags, Unset] = unset,
        categories: typing.Union[categories, Unset] = unset,
        places: typing.Union[places, Unset] = unset,
        created_at: typing.Union[created_at, Unset] = unset,
        updated_at: typing.Union[updated_at, Unset] = unset,
        deleted_at: typing.Union[deleted_at, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'CompanyResponse':
        return super().__new__(
            cls,
            *args,
            uuid=uuid,
            name=name,
            summary=summary,
            public=public,
            meta=meta,
            contact=contact,
            project_uuid=project_uuid,
            meta_uuid=meta_uuid,
            tags=tags,
            categories=categories,
            places=places,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            _configuration=_configuration,
            **kwargs,
        )

from ehelply_python_experimental_sdk.model.category_base import CategoryBase
from ehelply_python_experimental_sdk.model.contact_base import ContactBase
from ehelply_python_experimental_sdk.model.place_base import PlaceBase
from ehelply_python_experimental_sdk.model.tag_base import TagBase
