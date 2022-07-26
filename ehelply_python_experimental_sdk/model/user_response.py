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


class UserResponse(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    When retrieving a user
    """
    first_name = StrSchema
    last_name = StrSchema
    phone_number = StrSchema
    country = StrSchema
    picture = StrSchema
    gps_location = DictSchema
    verified_legal_terms = BoolSchema
    date_created = DateTimeSchema
    date_updated = DateTimeSchema
    date_deleted = DateTimeSchema

    @classmethod
    @property
    def email(cls) -> typing.Type['UserEmail']:
        return UserEmail
    
    
    class missing(
        ListSchema
    ):
        _items = StrSchema
    uuid = StrSchema
    
    
    class participants(
        ListSchema
    ):
        _items = DictSchema

    @classmethod
    @property
    def flags(cls) -> typing.Type['UserFlags']:
        return UserFlags
    last_login = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        first_name: typing.Union[first_name, Unset] = unset,
        last_name: typing.Union[last_name, Unset] = unset,
        phone_number: typing.Union[phone_number, Unset] = unset,
        country: typing.Union[country, Unset] = unset,
        picture: typing.Union[picture, Unset] = unset,
        gps_location: typing.Union[gps_location, Unset] = unset,
        verified_legal_terms: typing.Union[verified_legal_terms, Unset] = unset,
        date_created: typing.Union[date_created, Unset] = unset,
        date_updated: typing.Union[date_updated, Unset] = unset,
        date_deleted: typing.Union[date_deleted, Unset] = unset,
        email: typing.Union['UserEmail', Unset] = unset,
        missing: typing.Union[missing, Unset] = unset,
        uuid: typing.Union[uuid, Unset] = unset,
        participants: typing.Union[participants, Unset] = unset,
        flags: typing.Union['UserFlags', Unset] = unset,
        last_login: typing.Union[last_login, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'UserResponse':
        return super().__new__(
            cls,
            *args,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            country=country,
            picture=picture,
            gps_location=gps_location,
            verified_legal_terms=verified_legal_terms,
            date_created=date_created,
            date_updated=date_updated,
            date_deleted=date_deleted,
            email=email,
            missing=missing,
            uuid=uuid,
            participants=participants,
            flags=flags,
            last_login=last_login,
            _configuration=_configuration,
            **kwargs,
        )

from ehelply_python_experimental_sdk.model.user_email import UserEmail
from ehelply_python_experimental_sdk.model.user_flags import UserFlags
