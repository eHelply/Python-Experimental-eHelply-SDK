# coding: utf-8

"""
    eHelply SDK - 1.1.120

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.120
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


class StaffResponse(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    _required_property_names = set((
        'entity_uuid',
        'uuid',
    ))
    entity_uuid = StrSchema
    project_uuid = StrSchema
    schedule_uuid = StrSchema
    catalog_uuid = StrSchema
    review_group_uuid = StrSchema
    uuid = StrSchema
    entity = StrSchema
    place = DictSchema
    
    
    class place_roles(
        ListSchema
    ):
        _items = StrSchema
    company = DictSchema
    
    
    class company_roles(
        ListSchema
    ):
        _items = StrSchema
    schedule = DictSchema
    catalog = DictSchema
    reviews = DictSchema
    created_at = StrSchema
    updated_at = StrSchema
    deleted_at = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        entity_uuid: entity_uuid,
        uuid: uuid,
        project_uuid: typing.Union[project_uuid, Unset] = unset,
        schedule_uuid: typing.Union[schedule_uuid, Unset] = unset,
        catalog_uuid: typing.Union[catalog_uuid, Unset] = unset,
        review_group_uuid: typing.Union[review_group_uuid, Unset] = unset,
        entity: typing.Union[entity, Unset] = unset,
        place: typing.Union[place, Unset] = unset,
        place_roles: typing.Union[place_roles, Unset] = unset,
        company: typing.Union[company, Unset] = unset,
        company_roles: typing.Union[company_roles, Unset] = unset,
        schedule: typing.Union[schedule, Unset] = unset,
        catalog: typing.Union[catalog, Unset] = unset,
        reviews: typing.Union[reviews, Unset] = unset,
        created_at: typing.Union[created_at, Unset] = unset,
        updated_at: typing.Union[updated_at, Unset] = unset,
        deleted_at: typing.Union[deleted_at, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'StaffResponse':
        return super().__new__(
            cls,
            *args,
            entity_uuid=entity_uuid,
            uuid=uuid,
            project_uuid=project_uuid,
            schedule_uuid=schedule_uuid,
            catalog_uuid=catalog_uuid,
            review_group_uuid=review_group_uuid,
            entity=entity,
            place=place,
            place_roles=place_roles,
            company=company,
            company_roles=company_roles,
            schedule=schedule,
            catalog=catalog,
            reviews=reviews,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            _configuration=_configuration,
            **kwargs,
        )
