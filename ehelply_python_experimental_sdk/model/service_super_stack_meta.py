# coding: utf-8

"""
    eHelply SDK - 1.1.119

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.119
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


class ServiceSuperStackMeta(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    _required_property_names = set((
        'human_name',
        'route_name',
        'service_name',
        'advertise',
        'featured',
        'picture',
        'background_picture',
        'tag_line',
        'summary',
        'description',
        'features',
        'use_cases',
        'getting_started',
        'faqs',
    ))
    human_name = StrSchema
    route_name = StrSchema
    service_name = StrSchema
    advertise = BoolSchema
    featured = BoolSchema
    picture = StrSchema
    background_picture = StrSchema
    tag_line = StrSchema
    summary = StrSchema
    description = StrSchema
    
    
    class features(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['ServiceSuperStackMetaFeature']:
            return ServiceSuperStackMetaFeature
    
    
    class use_cases(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['ServiceSuperStackMetaUseCase']:
            return ServiceSuperStackMetaUseCase

    @classmethod
    @property
    def getting_started(cls) -> typing.Type['ServiceSuperStackMetaGettingStarted']:
        return ServiceSuperStackMetaGettingStarted
    
    
    class faqs(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['ServiceSuperStackMetaFaq']:
            return ServiceSuperStackMetaFaq


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        human_name: human_name,
        route_name: route_name,
        service_name: service_name,
        advertise: advertise,
        featured: featured,
        picture: picture,
        background_picture: background_picture,
        tag_line: tag_line,
        summary: summary,
        description: description,
        features: features,
        use_cases: use_cases,
        getting_started: getting_started,
        faqs: faqs,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'ServiceSuperStackMeta':
        return super().__new__(
            cls,
            *args,
            human_name=human_name,
            route_name=route_name,
            service_name=service_name,
            advertise=advertise,
            featured=featured,
            picture=picture,
            background_picture=background_picture,
            tag_line=tag_line,
            summary=summary,
            description=description,
            features=features,
            use_cases=use_cases,
            getting_started=getting_started,
            faqs=faqs,
            _configuration=_configuration,
            **kwargs,
        )

from ehelply_python_experimental_sdk.model.service_super_stack_meta_faq import ServiceSuperStackMetaFaq
from ehelply_python_experimental_sdk.model.service_super_stack_meta_feature import ServiceSuperStackMetaFeature
from ehelply_python_experimental_sdk.model.service_super_stack_meta_getting_started import ServiceSuperStackMetaGettingStarted
from ehelply_python_experimental_sdk.model.service_super_stack_meta_use_case import ServiceSuperStackMetaUseCase
