# coding: utf-8

"""
    eHelply SDK - 1.1.96

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.96
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""

from ehelply_python_experimental_sdk.api_client import ApiClient
from ehelply_python_experimental_sdk.api.products_api_endpoints.create_product import CreateProduct
from ehelply_python_experimental_sdk.api.products_api_endpoints.delete_product import DeleteProduct
from ehelply_python_experimental_sdk.api.products_api_endpoints.get_product import GetProduct
from ehelply_python_experimental_sdk.api.products_api_endpoints.search_product_catalog import SearchProductCatalog
from ehelply_python_experimental_sdk.api.products_api_endpoints.search_products import SearchProducts
from ehelply_python_experimental_sdk.api.products_api_endpoints.update_product import UpdateProduct


class ProductsApi(
    CreateProduct,
    DeleteProduct,
    GetProduct,
    SearchProductCatalog,
    SearchProducts,
    UpdateProduct,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass