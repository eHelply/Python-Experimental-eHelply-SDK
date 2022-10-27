# coding: utf-8

"""
    eHelply SDK - 1.1.114

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.114
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""

from ehelply_python_experimental_sdk.api_client import ApiClient
from ehelply_python_experimental_sdk.api.meta_api_endpoints.create_meta import CreateMeta
from ehelply_python_experimental_sdk.api.meta_api_endpoints.create_slug import CreateSlug
from ehelply_python_experimental_sdk.api.meta_api_endpoints.delete_meta import DeleteMeta
from ehelply_python_experimental_sdk.api.meta_api_endpoints.delete_meta_from_parts import DeleteMetaFromParts
from ehelply_python_experimental_sdk.api.meta_api_endpoints.get_meta import GetMeta
from ehelply_python_experimental_sdk.api.meta_api_endpoints.get_meta_from_parts import GetMetaFromParts
from ehelply_python_experimental_sdk.api.meta_api_endpoints.touch_meta import TouchMeta
from ehelply_python_experimental_sdk.api.meta_api_endpoints.update_meta import UpdateMeta
from ehelply_python_experimental_sdk.api.meta_api_endpoints.update_meta_from_parts import UpdateMetaFromParts


class MetaApi(
    CreateMeta,
    CreateSlug,
    DeleteMeta,
    DeleteMetaFromParts,
    GetMeta,
    GetMetaFromParts,
    TouchMeta,
    UpdateMeta,
    UpdateMetaFromParts,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
