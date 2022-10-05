# coding: utf-8

"""
    eHelply SDK - 1.1.110

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.110
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""

from ehelply_python_experimental_sdk.api_client import ApiClient
from ehelply_python_experimental_sdk.api.meta_api_endpoints.create_field import CreateField
from ehelply_python_experimental_sdk.api.meta_api_endpoints.create_meta import CreateMeta
from ehelply_python_experimental_sdk.api.meta_api_endpoints.delete_field import DeleteField
from ehelply_python_experimental_sdk.api.meta_api_endpoints.delete_meta import DeleteMeta
from ehelply_python_experimental_sdk.api.meta_api_endpoints.delete_meta_from_uuid import DeleteMetaFromUuid
from ehelply_python_experimental_sdk.api.meta_api_endpoints.get_field import GetField
from ehelply_python_experimental_sdk.api.meta_api_endpoints.get_meta import GetMeta
from ehelply_python_experimental_sdk.api.meta_api_endpoints.get_meta_from_uuid import GetMetaFromUuid
from ehelply_python_experimental_sdk.api.meta_api_endpoints.make_slug import MakeSlug
from ehelply_python_experimental_sdk.api.meta_api_endpoints.touch_meta import TouchMeta
from ehelply_python_experimental_sdk.api.meta_api_endpoints.update_field import UpdateField
from ehelply_python_experimental_sdk.api.meta_api_endpoints.update_meta import UpdateMeta
from ehelply_python_experimental_sdk.api.meta_api_endpoints.update_meta_from_uuid import UpdateMetaFromUuid


class MetaApi(
    CreateField,
    CreateMeta,
    DeleteField,
    DeleteMeta,
    DeleteMetaFromUuid,
    GetField,
    GetMeta,
    GetMetaFromUuid,
    MakeSlug,
    TouchMeta,
    UpdateField,
    UpdateMeta,
    UpdateMetaFromUuid,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
