# coding: utf-8

"""
    eHelply SDK - 1.1.99

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.99
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""

from ehelply_python_experimental_sdk.api_client import ApiClient
from ehelply_python_experimental_sdk.api.billing_api_endpoints.create_billing_account import CreateBillingAccount
from ehelply_python_experimental_sdk.api.billing_api_endpoints.get_client_secret import GetClientSecret
from ehelply_python_experimental_sdk.api.billing_api_endpoints.has_payment import HasPayment
from ehelply_python_experimental_sdk.api.billing_api_endpoints.list_payment_methods import ListPaymentMethods
from ehelply_python_experimental_sdk.api.billing_api_endpoints.process_payment import ProcessPayment
from ehelply_python_experimental_sdk.api.billing_api_endpoints.reconcile_payment_method import ReconcilePaymentMethod
from ehelply_python_experimental_sdk.api.billing_api_endpoints.remove_payment_method import RemovePaymentMethod


class BillingApi(
    CreateBillingAccount,
    GetClientSecret,
    HasPayment,
    ListPaymentMethods,
    ProcessPayment,
    ReconcilePaymentMethod,
    RemovePaymentMethod,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
