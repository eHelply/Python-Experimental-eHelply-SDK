# coding: utf-8

"""
    eHelply SDK - 1.1.117

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.117
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""

from ehelply_python_experimental_sdk.api_client import ApiClient
from ehelply_python_experimental_sdk.api.places_api_endpoints.advanced_search_places import AdvancedSearchPlaces
from ehelply_python_experimental_sdk.api.places_api_endpoints.create_place_places_places_post import CreatePlacePlacesPlacesPost
from ehelply_python_experimental_sdk.api.places_api_endpoints.delete_place import DeletePlace
from ehelply_python_experimental_sdk.api.places_api_endpoints.forward_geocoding_places_geocoding_forward_get import ForwardGeocodingPlacesGeocodingForwardGet
from ehelply_python_experimental_sdk.api.places_api_endpoints.get_place import GetPlace
from ehelply_python_experimental_sdk.api.places_api_endpoints.reverse_geocoding_places_geocoding_reverse_get import ReverseGeocodingPlacesGeocodingReverseGet
from ehelply_python_experimental_sdk.api.places_api_endpoints.search_places import SearchPlaces
from ehelply_python_experimental_sdk.api.places_api_endpoints.update_place import UpdatePlace


class PlacesApi(
    AdvancedSearchPlaces,
    CreatePlacePlacesPlacesPost,
    DeletePlace,
    ForwardGeocodingPlacesGeocodingForwardGet,
    GetPlace,
    ReverseGeocodingPlacesGeocodingReverseGet,
    SearchPlaces,
    UpdatePlace,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
