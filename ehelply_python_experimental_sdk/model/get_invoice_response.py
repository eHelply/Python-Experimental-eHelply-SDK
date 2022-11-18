# coding: utf-8

"""
    eHelply SDK - 1.1.122

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.122
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


class GetInvoiceResponse(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    _required_property_names = set((
        'invoice_uuid',
        'line_items',
        'subtotal',
        'discounts',
        'taxes',
        'total',
        'notes',
        'created_at',
        'update_at',
    ))
    invoice_uuid = StrSchema
    
    
    class line_items(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['LineItem']:
            return LineItem
    subtotal = IntSchema
    
    
    class discounts(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['Discount']:
            return Discount
    
    
    class taxes(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['Tax']:
            return Tax
    total = IntSchema
    
    
    class notes(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['Note']:
            return Note
    paid = BoolSchema
    created_at = StrSchema
    update_at = StrSchema
    deleted_at = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        invoice_uuid: invoice_uuid,
        line_items: line_items,
        subtotal: subtotal,
        discounts: discounts,
        taxes: taxes,
        total: total,
        notes: notes,
        created_at: created_at,
        update_at: update_at,
        paid: typing.Union[paid, Unset] = unset,
        deleted_at: typing.Union[deleted_at, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'GetInvoiceResponse':
        return super().__new__(
            cls,
            *args,
            invoice_uuid=invoice_uuid,
            line_items=line_items,
            subtotal=subtotal,
            discounts=discounts,
            taxes=taxes,
            total=total,
            notes=notes,
            created_at=created_at,
            update_at=update_at,
            paid=paid,
            deleted_at=deleted_at,
            _configuration=_configuration,
            **kwargs,
        )

from ehelply_python_experimental_sdk.model.discount import Discount
from ehelply_python_experimental_sdk.model.line_item import LineItem
from ehelply_python_experimental_sdk.model.note import Note
from ehelply_python_experimental_sdk.model.tax import Tax
