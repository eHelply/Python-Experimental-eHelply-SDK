# coding: utf-8

"""
    eHelply SDK - 1.1.122

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.122
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""

from ehelply_python_experimental_sdk.api_client import ApiClient
from ehelply_python_experimental_sdk.api.support_api_endpoints.create_contact import CreateContact
from ehelply_python_experimental_sdk.api.support_api_endpoints.create_ticket import CreateTicket
from ehelply_python_experimental_sdk.api.support_api_endpoints.list_tickets import ListTickets
from ehelply_python_experimental_sdk.api.support_api_endpoints.update_ticket import UpdateTicket
from ehelply_python_experimental_sdk.api.support_api_endpoints.view_ticket import ViewTicket


class SupportApi(
    CreateContact,
    CreateTicket,
    ListTickets,
    UpdateTicket,
    ViewTicket,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
