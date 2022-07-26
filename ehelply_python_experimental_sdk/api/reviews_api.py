# coding: utf-8

"""
    eHelply SDK - 1.1.118

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.118
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""

from ehelply_python_experimental_sdk.api_client import ApiClient
from ehelply_python_experimental_sdk.api.reviews_api_endpoints.create_review import CreateReview
from ehelply_python_experimental_sdk.api.reviews_api_endpoints.delete_review import DeleteReview
from ehelply_python_experimental_sdk.api.reviews_api_endpoints.get_review import GetReview
from ehelply_python_experimental_sdk.api.reviews_api_endpoints.search_reviews import SearchReviews
from ehelply_python_experimental_sdk.api.reviews_api_endpoints.update_review import UpdateReview


class ReviewsApi(
    CreateReview,
    DeleteReview,
    GetReview,
    SearchReviews,
    UpdateReview,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
