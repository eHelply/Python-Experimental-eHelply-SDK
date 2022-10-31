# coding: utf-8

"""
    eHelply SDK - 1.1.116

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.116
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""

from ehelply_python_experimental_sdk.api_client import ApiClient
from ehelply_python_experimental_sdk.api.catalogs_api_endpoints.attach_product_to_catalog import AttachProductToCatalog
from ehelply_python_experimental_sdk.api.catalogs_api_endpoints.create_catalog import CreateCatalog
from ehelply_python_experimental_sdk.api.catalogs_api_endpoints.delete_catalog import DeleteCatalog
from ehelply_python_experimental_sdk.api.catalogs_api_endpoints.detach_product_from_catalog import DetachProductFromCatalog
from ehelply_python_experimental_sdk.api.catalogs_api_endpoints.get_catalog import GetCatalog
from ehelply_python_experimental_sdk.api.catalogs_api_endpoints.search_catalog_products import SearchCatalogProducts
from ehelply_python_experimental_sdk.api.catalogs_api_endpoints.search_catalogs import SearchCatalogs
from ehelply_python_experimental_sdk.api.catalogs_api_endpoints.update_catalog import UpdateCatalog


class CatalogsApi(
    AttachProductToCatalog,
    CreateCatalog,
    DeleteCatalog,
    DetachProductFromCatalog,
    GetCatalog,
    SearchCatalogProducts,
    SearchCatalogs,
    UpdateCatalog,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
