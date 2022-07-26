# coding: utf-8

"""
    eHelply SDK - 1.1.118

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.118
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


class AppointmentBase(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    project_uuid = StrSchema
    place_uuid = StrSchema
    review_group_uuid = StrSchema
    expected_finish_at = StrSchema
    expected_start_at = StrSchema
    actual_start_at = StrSchema
    actual_finish_at = StrSchema
    products = DictSchema
    meta_uuid = StrSchema
    status = StrSchema
    cancellation_at = StrSchema
    cancellation_reason = StrSchema
    cancellation_entity_uuid = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        project_uuid: typing.Union[project_uuid, Unset] = unset,
        place_uuid: typing.Union[place_uuid, Unset] = unset,
        review_group_uuid: typing.Union[review_group_uuid, Unset] = unset,
        expected_finish_at: typing.Union[expected_finish_at, Unset] = unset,
        expected_start_at: typing.Union[expected_start_at, Unset] = unset,
        actual_start_at: typing.Union[actual_start_at, Unset] = unset,
        actual_finish_at: typing.Union[actual_finish_at, Unset] = unset,
        products: typing.Union[products, Unset] = unset,
        meta_uuid: typing.Union[meta_uuid, Unset] = unset,
        status: typing.Union[status, Unset] = unset,
        cancellation_at: typing.Union[cancellation_at, Unset] = unset,
        cancellation_reason: typing.Union[cancellation_reason, Unset] = unset,
        cancellation_entity_uuid: typing.Union[cancellation_entity_uuid, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'AppointmentBase':
        return super().__new__(
            cls,
            *args,
            project_uuid=project_uuid,
            place_uuid=place_uuid,
            review_group_uuid=review_group_uuid,
            expected_finish_at=expected_finish_at,
            expected_start_at=expected_start_at,
            actual_start_at=actual_start_at,
            actual_finish_at=actual_finish_at,
            products=products,
            meta_uuid=meta_uuid,
            status=status,
            cancellation_at=cancellation_at,
            cancellation_reason=cancellation_reason,
            cancellation_entity_uuid=cancellation_entity_uuid,
            _configuration=_configuration,
            **kwargs,
        )
