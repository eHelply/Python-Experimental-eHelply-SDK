# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import re  # noqa: F401
import sys  # noqa: F401
import typing
import urllib3
import functools  # noqa: F401
from urllib3._collections import HTTPHeaderDict

from ehelply_python_experimental_sdk import api_client, exceptions
import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from ehelply_python_experimental_sdk.schemas import (  # noqa: F401
    AnyTypeSchema,
    ComposedSchema,
    DictSchema,
    ListSchema,
    StrSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    NumberSchema,
    UUIDSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    Configuration,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    Int32Base,
    Int64Base,
    Float32Base,
    Float64Base,
    NumberBase,
    UUIDBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)

from ehelply_python_experimental_sdk.model.projects_usage_type_create import ProjectsUsageTypeCreate
from ehelply_python_experimental_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_experimental_sdk.model.projects_usage_type_db import ProjectsUsageTypeDB

# header params
XAccessTokenSchema = StrSchema
XSecretTokenSchema = StrSchema
AuthorizationSchema = StrSchema
EhelplyActiveParticipantSchema = StrSchema
EhelplyProjectSchema = StrSchema
EhelplyDataSchema = StrSchema
RequestRequiredHeaderParams = typing.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'x-access-token': XAccessTokenSchema,
        'x-secret-token': XSecretTokenSchema,
        'authorization': AuthorizationSchema,
        'ehelply-active-participant': EhelplyActiveParticipantSchema,
        'ehelply-project': EhelplyProjectSchema,
        'ehelply-data': EhelplyDataSchema,
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_x_access_token = api_client.HeaderParameter(
    name="x-access-token",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XAccessTokenSchema,
)
request_header_x_secret_token = api_client.HeaderParameter(
    name="x-secret-token",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XSecretTokenSchema,
)
request_header_authorization = api_client.HeaderParameter(
    name="authorization",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AuthorizationSchema,
)
request_header_ehelply_active_participant = api_client.HeaderParameter(
    name="ehelply-active-participant",
    style=api_client.ParameterStyle.SIMPLE,
    schema=EhelplyActiveParticipantSchema,
)
request_header_ehelply_project = api_client.HeaderParameter(
    name="ehelply-project",
    style=api_client.ParameterStyle.SIMPLE,
    schema=EhelplyProjectSchema,
)
request_header_ehelply_data = api_client.HeaderParameter(
    name="ehelply-data",
    style=api_client.ParameterStyle.SIMPLE,
    schema=EhelplyDataSchema,
)
# body param
SchemaForRequestBodyApplicationJson = ProjectsUsageTypeCreate


request_body_projects_usage_type_create = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_path = '/sam/projects/usage/types'
_method = 'POST'
SchemaFor200ResponseBodyApplicationJson = ProjectsUsageTypeDB


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
    ]
    headers: Unset = unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


class SchemaFor403ResponseBodyApplicationJson(
    DictSchema
):
    message = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        message: typing.Union[message, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'SchemaFor403ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            message=message,
            _configuration=_configuration,
            **kwargs,
        )


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor403ResponseBodyApplicationJson,
    ]
    headers: Unset = unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: Unset = unset
    headers: Unset = unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
)
SchemaFor422ResponseBodyApplicationJson = HTTPValidationError


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor422ResponseBodyApplicationJson,
    ]
    headers: Unset = unset


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '403': _response_for_403,
    '404': _response_for_404,
    '422': _response_for_422,
}
_all_accept_content_types = (
    'application/json',
)


class CreateUsageType(api_client.Api):

    def create_usage_type(
        self: api_client.Api,
        body: typing.Union[SchemaForRequestBodyApplicationJson],
        header_params: RequestHeaderParams = frozendict(),
        content_type: str = 'application/json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
        Createusagetype
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs(RequestHeaderParams, header_params)
        used_path = _path

        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_x_access_token,
            request_header_x_secret_token,
            request_header_authorization,
            request_header_ehelply_active_participant,
            request_header_ehelply_project,
            request_header_ehelply_data,
        ):
            parameter_data = header_params.get(parameter.name, unset)
            if parameter_data is unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        if body is unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        serialized_data = request_body_projects_usage_type_create.serialize(body, content_type)
        _headers.add('Content-Type', content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method=_method,
            headers=_headers,
            fields=_fields,
            body=_body,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response
