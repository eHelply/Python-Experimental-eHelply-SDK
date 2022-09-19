# coding: utf-8

"""
    eHelply SDK - 1.1.108

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.108
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


class PlaceResponse(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    **:param** name                                **type:** string
**:param** summary                             **type:** string or None

**:param** public                              **type:** bool or None

**:param** meta                                **type:** dict or None

**:param** addresses                           **type:** PlaceAddress or None

**:param** contact                             **type:** ContactBase or None
    """
    _required_property_names = set((
        'name',
        'uuid',
    ))
    name = StrSchema
    summary = StrSchema
    public = BoolSchema
    meta = DictSchema
    
    
    class addresses(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['AddressBase']:
            return AddressBase

    @classmethod
    @property
    def contact(cls) -> typing.Type['ContactBase']:
        return ContactBase
    picture = StrSchema
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
    
    
    class company(
        ComposedSchema
    ):
    
        @classmethod
        @property
        @functools.cache
        def _composed_schemas(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return {
                'allOf': [
                    CompanyBase,
                ],
                'oneOf': [
                ],
                'anyOf': [
                ],
                'not':
                    None
            }
    
        def __new__(
            cls,
            *args: typing.Union[dict, frozendict, str, date, datetime, int, float, decimal.Decimal, None, list, tuple, bytes],
            _configuration: typing.Optional[Configuration] = None,
            **kwargs: typing.Type[Schema],
        ) -> 'company':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
                **kwargs,
            )
    created_at = StrSchema
    updated_at = StrSchema
    deleted_at = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        name: name,
        uuid: uuid,
        summary: typing.Union[summary, Unset] = unset,
        public: typing.Union[public, Unset] = unset,
        meta: typing.Union[meta, Unset] = unset,
        addresses: typing.Union[addresses, Unset] = unset,
        contact: typing.Union['ContactBase', Unset] = unset,
        picture: typing.Union[picture, Unset] = unset,
        project_uuid: typing.Union[project_uuid, Unset] = unset,
        meta_uuid: typing.Union[meta_uuid, Unset] = unset,
        tags: typing.Union[tags, Unset] = unset,
        categories: typing.Union[categories, Unset] = unset,
        company: typing.Union[company, Unset] = unset,
        created_at: typing.Union[created_at, Unset] = unset,
        updated_at: typing.Union[updated_at, Unset] = unset,
        deleted_at: typing.Union[deleted_at, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'PlaceResponse':
        return super().__new__(
            cls,
            *args,
            name=name,
            uuid=uuid,
            summary=summary,
            public=public,
            meta=meta,
            addresses=addresses,
            contact=contact,
            picture=picture,
            project_uuid=project_uuid,
            meta_uuid=meta_uuid,
            tags=tags,
            categories=categories,
            company=company,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            _configuration=_configuration,
            **kwargs,
        )

from ehelply_python_experimental_sdk.model.address_base import AddressBase
from ehelply_python_experimental_sdk.model.category_base import CategoryBase
from ehelply_python_experimental_sdk.model.company_base import CompanyBase
from ehelply_python_experimental_sdk.model.contact_base import ContactBase
from ehelply_python_experimental_sdk.model.tag_base import TagBase
