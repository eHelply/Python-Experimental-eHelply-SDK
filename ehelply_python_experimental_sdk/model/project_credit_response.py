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


class ProjectCreditResponse(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    _required_property_names = set((
        'uuid',
        'project_uuid',
        'credits_granted',
        'granted_by',
        'granted_reason',
        'granted_at',
    ))
    uuid = StrSchema
    project_uuid = StrSchema
    credits_granted = IntSchema
    credits_consumed = IntSchema
    granted_by = StrSchema
    granted_reason = StrSchema
    granted_at = StrSchema
    fully_consumed_at = StrSchema
    revoked_reason = StrSchema
    revoked_at = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        uuid: uuid,
        project_uuid: project_uuid,
        credits_granted: credits_granted,
        granted_by: granted_by,
        granted_reason: granted_reason,
        granted_at: granted_at,
        credits_consumed: typing.Union[credits_consumed, Unset] = unset,
        fully_consumed_at: typing.Union[fully_consumed_at, Unset] = unset,
        revoked_reason: typing.Union[revoked_reason, Unset] = unset,
        revoked_at: typing.Union[revoked_at, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'ProjectCreditResponse':
        return super().__new__(
            cls,
            *args,
            uuid=uuid,
            project_uuid=project_uuid,
            credits_granted=credits_granted,
            granted_by=granted_by,
            granted_reason=granted_reason,
            granted_at=granted_at,
            credits_consumed=credits_consumed,
            fully_consumed_at=fully_consumed_at,
            revoked_reason=revoked_reason,
            revoked_at=revoked_at,
            _configuration=_configuration,
            **kwargs,
        )
