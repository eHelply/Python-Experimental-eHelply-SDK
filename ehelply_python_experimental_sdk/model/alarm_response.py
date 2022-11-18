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


class AlarmResponse(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    uuid = StrSchema
    service_uuid = StrSchema
    count = IntSchema
    stage = StrSchema
    process = StrSchema
    severity = StrSchema
    ticket_uuid = StrSchema
    name = StrSchema
    summary = StrSchema
    description = StrSchema
    
    
    class note(
        ListSchema
    ):
        _items = DictSchema
    created_at = StrSchema
    latest_at = StrSchema
    acknowledged_at = StrSchema
    ignored_at = StrSchema
    cleared_at = StrSchema
    terminated_at = StrSchema
    assignee_uuid = StrSchema
    acknowledger_uuid = StrSchema
    ignorer_uuid = StrSchema
    terminater_uuid = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        uuid: typing.Union[uuid, Unset] = unset,
        service_uuid: typing.Union[service_uuid, Unset] = unset,
        count: typing.Union[count, Unset] = unset,
        stage: typing.Union[stage, Unset] = unset,
        process: typing.Union[process, Unset] = unset,
        severity: typing.Union[severity, Unset] = unset,
        ticket_uuid: typing.Union[ticket_uuid, Unset] = unset,
        name: typing.Union[name, Unset] = unset,
        summary: typing.Union[summary, Unset] = unset,
        description: typing.Union[description, Unset] = unset,
        note: typing.Union[note, Unset] = unset,
        created_at: typing.Union[created_at, Unset] = unset,
        latest_at: typing.Union[latest_at, Unset] = unset,
        acknowledged_at: typing.Union[acknowledged_at, Unset] = unset,
        ignored_at: typing.Union[ignored_at, Unset] = unset,
        cleared_at: typing.Union[cleared_at, Unset] = unset,
        terminated_at: typing.Union[terminated_at, Unset] = unset,
        assignee_uuid: typing.Union[assignee_uuid, Unset] = unset,
        acknowledger_uuid: typing.Union[acknowledger_uuid, Unset] = unset,
        ignorer_uuid: typing.Union[ignorer_uuid, Unset] = unset,
        terminater_uuid: typing.Union[terminater_uuid, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'AlarmResponse':
        return super().__new__(
            cls,
            *args,
            uuid=uuid,
            service_uuid=service_uuid,
            count=count,
            stage=stage,
            process=process,
            severity=severity,
            ticket_uuid=ticket_uuid,
            name=name,
            summary=summary,
            description=description,
            note=note,
            created_at=created_at,
            latest_at=latest_at,
            acknowledged_at=acknowledged_at,
            ignored_at=ignored_at,
            cleared_at=cleared_at,
            terminated_at=terminated_at,
            assignee_uuid=assignee_uuid,
            acknowledger_uuid=acknowledger_uuid,
            ignorer_uuid=ignorer_uuid,
            terminater_uuid=terminater_uuid,
            _configuration=_configuration,
            **kwargs,
        )
