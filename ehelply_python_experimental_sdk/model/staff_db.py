# coding: utf-8

"""
    eHelply SDK - 1.1.114

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.114
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


class StaffDb(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    **:param** uuid                                **type:** string
**:param** project_uuid                        **type:** string or None

**:param** entity_uuid                         **type:** string or None

**:param** schedule_uuid                       **type:** string or None

**:param** catalog_uuid                        **type:** string or None

**:param** review_group_uuid                   **type:** string or None

**:param** created_at                          **type:** string or None

**:param** updated_at                          **type:** string or None

**:param** deleted_at                          **type:** string or None
    """
    _required_property_names = set((
        'uuid',
    ))
    uuid = StrSchema
    project_uuid = StrSchema
    entity_uuid = StrSchema
    schedule_uuid = StrSchema
    catalog_uuid = StrSchema
    review_group_uuid = StrSchema
    created_at = StrSchema
    updated_at = StrSchema
    deleted_at = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        uuid: uuid,
        project_uuid: typing.Union[project_uuid, Unset] = unset,
        entity_uuid: typing.Union[entity_uuid, Unset] = unset,
        schedule_uuid: typing.Union[schedule_uuid, Unset] = unset,
        catalog_uuid: typing.Union[catalog_uuid, Unset] = unset,
        review_group_uuid: typing.Union[review_group_uuid, Unset] = unset,
        created_at: typing.Union[created_at, Unset] = unset,
        updated_at: typing.Union[updated_at, Unset] = unset,
        deleted_at: typing.Union[deleted_at, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'StaffDb':
        return super().__new__(
            cls,
            *args,
            uuid=uuid,
            project_uuid=project_uuid,
            entity_uuid=entity_uuid,
            schedule_uuid=schedule_uuid,
            catalog_uuid=catalog_uuid,
            review_group_uuid=review_group_uuid,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            _configuration=_configuration,
            **kwargs,
        )
