# coding: utf-8

"""
    eHelply SDK - 1.1.110

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.110
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""

from ehelply_python_experimental_sdk.api_client import ApiClient
from ehelply_python_experimental_sdk.api.appointments_api_endpoints.add_entity_to_appointment import AddEntityToAppointment
from ehelply_python_experimental_sdk.api.appointments_api_endpoints.create_appointment import CreateAppointment
from ehelply_python_experimental_sdk.api.appointments_api_endpoints.delete_appointment import DeleteAppointment
from ehelply_python_experimental_sdk.api.appointments_api_endpoints.detach_entity_from_appointment import DetachEntityFromAppointment
from ehelply_python_experimental_sdk.api.appointments_api_endpoints.get_appointment import GetAppointment
from ehelply_python_experimental_sdk.api.appointments_api_endpoints.search_appointment import SearchAppointment
from ehelply_python_experimental_sdk.api.appointments_api_endpoints.search_appointment_entities import SearchAppointmentEntities
from ehelply_python_experimental_sdk.api.appointments_api_endpoints.search_entity_appointments import SearchEntityAppointments
from ehelply_python_experimental_sdk.api.appointments_api_endpoints.update_appointment import UpdateAppointment


class AppointmentsApi(
    AddEntityToAppointment,
    CreateAppointment,
    DeleteAppointment,
    DetachEntityFromAppointment,
    GetAppointment,
    SearchAppointment,
    SearchAppointmentEntities,
    SearchEntityAppointments,
    UpdateAppointment,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
