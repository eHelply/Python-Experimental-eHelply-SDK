# coding: utf-8

"""
    eHelply SDK - 1.1.118

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.118
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""

from ehelply_python_experimental_sdk.api_client import ApiClient
from ehelply_python_experimental_sdk.api.companies_api_endpoints.create_company_places_companies_post import CreateCompanyPlacesCompaniesPost
from ehelply_python_experimental_sdk.api.companies_api_endpoints.delete_place_places_companies_company_uuid_delete import DeletePlacePlacesCompaniesCompanyUuidDelete
from ehelply_python_experimental_sdk.api.companies_api_endpoints.get_company_places_companies_company_uuid_get import GetCompanyPlacesCompaniesCompanyUuidGet
from ehelply_python_experimental_sdk.api.companies_api_endpoints.search_companies_places_companies_get import SearchCompaniesPlacesCompaniesGet
from ehelply_python_experimental_sdk.api.companies_api_endpoints.update_company_places_companies_company_uuid_put import UpdateCompanyPlacesCompaniesCompanyUuidPut


class CompaniesApi(
    CreateCompanyPlacesCompaniesPost,
    DeletePlacePlacesCompaniesCompanyUuidDelete,
    GetCompanyPlacesCompaniesCompanyUuidGet,
    SearchCompaniesPlacesCompaniesGet,
    UpdateCompanyPlacesCompaniesCompanyUuidPut,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
