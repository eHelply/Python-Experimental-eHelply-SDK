# coding: utf-8

"""
    eHelply SDK - 1.1.99

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.99
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""

from ehelply_python_experimental_sdk.api_client import ApiClient
from ehelply_python_experimental_sdk.api.staff_api_endpoints.create_staff import CreateStaff
from ehelply_python_experimental_sdk.api.staff_api_endpoints.delete_staff import DeleteStaff
from ehelply_python_experimental_sdk.api.staff_api_endpoints.get_staff import GetStaff
from ehelply_python_experimental_sdk.api.staff_api_endpoints.search_staff import SearchStaff
from ehelply_python_experimental_sdk.api.staff_api_endpoints.update_staff import UpdateStaff


class StaffApi(
    CreateStaff,
    DeleteStaff,
    GetStaff,
    SearchStaff,
    UpdateStaff,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
