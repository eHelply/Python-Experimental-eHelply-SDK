# ehelply_python_experimental_sdk.AppointmentsApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_entity_to_appointment**](AppointmentsApi.md#add_entity_to_appointment) | **POST** /appointments/appointments/{appointment_uuid}/entities/{entity_uuid} | Addentitytoappointment
[**create_appointment**](AppointmentsApi.md#create_appointment) | **POST** /appointments/appointments | Createappointment
[**delete_appointment**](AppointmentsApi.md#delete_appointment) | **DELETE** /appointments/appointments/{appointment_uuid} | Deleteappointment
[**detach_entity_from_appointment**](AppointmentsApi.md#detach_entity_from_appointment) | **DELETE** /appointments/appointments/{appointment_uuid}/entities/{entity_uuid} | Removeentityfromappointment
[**get_appointment**](AppointmentsApi.md#get_appointment) | **GET** /appointments/appointments/{appointment_uuid} | Getappointment
[**search_appointment**](AppointmentsApi.md#search_appointment) | **GET** /appointments/appointments | Searchappointments
[**search_appointment_entities**](AppointmentsApi.md#search_appointment_entities) | **GET** /appointments/appointments/{appointment_uuid}/entities | Searchappointmententities
[**search_entity_appointments**](AppointmentsApi.md#search_entity_appointments) | **GET** /appointments/appointments/entities/{entity_uuid}/appointments | Getentityappointments
[**update_appointment**](AppointmentsApi.md#update_appointment) | **PUT** /appointments/appointments/{appointment_uuid} | Updateappointment

# **add_entity_to_appointment**
> bool add_entity_to_appointment(appointment_uuidentity_uuid)

Addentitytoappointment

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import appointments_api
from ehelply_python_experimental_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_experimental_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_experimental_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = appointments_api.AppointmentsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'appointment_uuid': "appointment_uuid_example",
        'entity_uuid': "entity_uuid_example",
    }
    header_params = {
    }
    try:
        # Addentitytoappointment
        api_response = api_instance.add_entity_to_appointment(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling AppointmentsApi->add_entity_to_appointment: %s\n" % e)

    # example passing only optional values
    path_params = {
        'appointment_uuid': "appointment_uuid_example",
        'entity_uuid': "entity_uuid_example",
    }
    header_params = {
        'x-access-token': "x-access-token_example",
        'x-secret-token': "x-secret-token_example",
        'authorization': "authorization_example",
        'ehelply-active-participant': "ehelply-active-participant_example",
        'ehelply-project': "ehelply-project_example",
        'ehelply-data': "ehelply-data_example",
    }
    try:
        # Addentitytoappointment
        api_response = api_instance.add_entity_to_appointment(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling AppointmentsApi->add_entity_to_appointment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
x-access-token | XAccessTokenSchema | | optional
x-secret-token | XSecretTokenSchema | | optional
authorization | AuthorizationSchema | | optional
ehelply-active-participant | EhelplyActiveParticipantSchema | | optional
ehelply-project | EhelplyProjectSchema | | optional
ehelply-data | EhelplyDataSchema | | optional

#### XAccessTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### XSecretTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AuthorizationSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyActiveParticipantSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyProjectSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyDataSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
appointment_uuid | AppointmentUuidSchema | | 
entity_uuid | EntityUuidSchema | | 

#### AppointmentUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EntityUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response
404 | ApiResponseFor404 | Not found
422 | ApiResponseFor422 | Validation Error

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_appointment**
> AppointmentResponse create_appointment(appointment_base)

Createappointment

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import appointments_api
from ehelply_python_experimental_sdk.model.appointment_response import AppointmentResponse
from ehelply_python_experimental_sdk.model.appointment_base import AppointmentBase
from ehelply_python_experimental_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_experimental_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_experimental_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = appointments_api.AppointmentsApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = AppointmentBase(
        project_uuid="project_uuid",
        place_uuid="place_uuid",
        review_group_uuid="review_group_uuid",
        expected_finish_at="2020-06-27T12:00:00.000000",
        expected_start_at="2020-06-27T12:00:00.000000",
        actual_start_at="2020-06-27T12:00:00.000000",
        actual_finish_at="2020-06-27T12:00:00.000000",
        products=dict(),
        meta_uuid="meta_uuid",
        status="Awaiting Approval",
        cancellation_at="2020-06-27T12:00:00.000000",
        cancellation_reason="Sick",
        cancellation_entity_uuid="user_uuid",
    )
    try:
        # Createappointment
        api_response = api_instance.create_appointment(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling AppointmentsApi->create_appointment: %s\n" % e)

    # example passing only optional values
    header_params = {
        'x-access-token': "x-access-token_example",
        'x-secret-token': "x-secret-token_example",
        'authorization': "authorization_example",
        'ehelply-active-participant': "ehelply-active-participant_example",
        'ehelply-project': "ehelply-project_example",
        'ehelply-data': "ehelply-data_example",
    }
    body = AppointmentBase(
        project_uuid="project_uuid",
        place_uuid="place_uuid",
        review_group_uuid="review_group_uuid",
        expected_finish_at="2020-06-27T12:00:00.000000",
        expected_start_at="2020-06-27T12:00:00.000000",
        actual_start_at="2020-06-27T12:00:00.000000",
        actual_finish_at="2020-06-27T12:00:00.000000",
        products=dict(),
        meta_uuid="meta_uuid",
        status="Awaiting Approval",
        cancellation_at="2020-06-27T12:00:00.000000",
        cancellation_reason="Sick",
        cancellation_entity_uuid="user_uuid",
    )
    try:
        # Createappointment
        api_response = api_instance.create_appointment(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling AppointmentsApi->create_appointment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AppointmentBase**](AppointmentBase.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
x-access-token | XAccessTokenSchema | | optional
x-secret-token | XSecretTokenSchema | | optional
authorization | AuthorizationSchema | | optional
ehelply-active-participant | EhelplyActiveParticipantSchema | | optional
ehelply-project | EhelplyProjectSchema | | optional
ehelply-data | EhelplyDataSchema | | optional

#### XAccessTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### XSecretTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AuthorizationSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyActiveParticipantSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyProjectSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyDataSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response
404 | ApiResponseFor404 | Not found
422 | ApiResponseFor422 | Validation Error

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AppointmentResponse**](AppointmentResponse.md) |  | 


#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



[**AppointmentResponse**](AppointmentResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_appointment**
> bool delete_appointment(appointment_uuid)

Deleteappointment

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import appointments_api
from ehelply_python_experimental_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_experimental_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_experimental_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = appointments_api.AppointmentsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'appointment_uuid': "appointment_uuid_example",
    }
    header_params = {
    }
    try:
        # Deleteappointment
        api_response = api_instance.delete_appointment(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling AppointmentsApi->delete_appointment: %s\n" % e)

    # example passing only optional values
    path_params = {
        'appointment_uuid': "appointment_uuid_example",
    }
    header_params = {
        'x-access-token': "x-access-token_example",
        'x-secret-token': "x-secret-token_example",
        'authorization': "authorization_example",
        'ehelply-active-participant': "ehelply-active-participant_example",
        'ehelply-project': "ehelply-project_example",
        'ehelply-data': "ehelply-data_example",
    }
    try:
        # Deleteappointment
        api_response = api_instance.delete_appointment(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling AppointmentsApi->delete_appointment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
x-access-token | XAccessTokenSchema | | optional
x-secret-token | XSecretTokenSchema | | optional
authorization | AuthorizationSchema | | optional
ehelply-active-participant | EhelplyActiveParticipantSchema | | optional
ehelply-project | EhelplyProjectSchema | | optional
ehelply-data | EhelplyDataSchema | | optional

#### XAccessTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### XSecretTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AuthorizationSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyActiveParticipantSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyProjectSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyDataSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
appointment_uuid | AppointmentUuidSchema | | 

#### AppointmentUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response
404 | ApiResponseFor404 | Not found
422 | ApiResponseFor422 | Validation Error

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_entity_from_appointment**
> bool detach_entity_from_appointment(appointment_uuidentity_uuid)

Removeentityfromappointment

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import appointments_api
from ehelply_python_experimental_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_experimental_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_experimental_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = appointments_api.AppointmentsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'appointment_uuid': "appointment_uuid_example",
        'entity_uuid': "entity_uuid_example",
    }
    header_params = {
    }
    try:
        # Removeentityfromappointment
        api_response = api_instance.detach_entity_from_appointment(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling AppointmentsApi->detach_entity_from_appointment: %s\n" % e)

    # example passing only optional values
    path_params = {
        'appointment_uuid': "appointment_uuid_example",
        'entity_uuid': "entity_uuid_example",
    }
    header_params = {
        'x-access-token': "x-access-token_example",
        'x-secret-token': "x-secret-token_example",
        'authorization': "authorization_example",
        'ehelply-active-participant': "ehelply-active-participant_example",
        'ehelply-project': "ehelply-project_example",
        'ehelply-data': "ehelply-data_example",
    }
    try:
        # Removeentityfromappointment
        api_response = api_instance.detach_entity_from_appointment(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling AppointmentsApi->detach_entity_from_appointment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
x-access-token | XAccessTokenSchema | | optional
x-secret-token | XSecretTokenSchema | | optional
authorization | AuthorizationSchema | | optional
ehelply-active-participant | EhelplyActiveParticipantSchema | | optional
ehelply-project | EhelplyProjectSchema | | optional
ehelply-data | EhelplyDataSchema | | optional

#### XAccessTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### XSecretTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AuthorizationSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyActiveParticipantSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyProjectSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyDataSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
appointment_uuid | AppointmentUuidSchema | | 
entity_uuid | EntityUuidSchema | | 

#### AppointmentUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EntityUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response
404 | ApiResponseFor404 | Not found
422 | ApiResponseFor422 | Validation Error

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appointment**
> AppointmentResponse get_appointment(appointment_uuid)

Getappointment

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import appointments_api
from ehelply_python_experimental_sdk.model.appointment_response import AppointmentResponse
from ehelply_python_experimental_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_experimental_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_experimental_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = appointments_api.AppointmentsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'appointment_uuid': "appointment_uuid_example",
    }
    header_params = {
    }
    try:
        # Getappointment
        api_response = api_instance.get_appointment(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling AppointmentsApi->get_appointment: %s\n" % e)

    # example passing only optional values
    path_params = {
        'appointment_uuid': "appointment_uuid_example",
    }
    header_params = {
        'x-access-token': "x-access-token_example",
        'x-secret-token': "x-secret-token_example",
        'authorization': "authorization_example",
        'ehelply-active-participant': "ehelply-active-participant_example",
        'ehelply-project': "ehelply-project_example",
        'ehelply-data': "ehelply-data_example",
    }
    try:
        # Getappointment
        api_response = api_instance.get_appointment(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling AppointmentsApi->get_appointment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
x-access-token | XAccessTokenSchema | | optional
x-secret-token | XSecretTokenSchema | | optional
authorization | AuthorizationSchema | | optional
ehelply-active-participant | EhelplyActiveParticipantSchema | | optional
ehelply-project | EhelplyProjectSchema | | optional
ehelply-data | EhelplyDataSchema | | optional

#### XAccessTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### XSecretTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AuthorizationSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyActiveParticipantSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyProjectSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyDataSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
appointment_uuid | AppointmentUuidSchema | | 

#### AppointmentUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response
403 | ApiResponseFor403 | Unauthorized - Denied by eHelply
404 | ApiResponseFor404 | Appointment does not exist
422 | ApiResponseFor422 | Validation Error

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AppointmentResponse**](AppointmentResponse.md) |  | 


#### ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor403ResponseBodyApplicationJson

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor404ResponseBodyApplicationJson

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



[**AppointmentResponse**](AppointmentResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_appointment**
> bool, date, datetime, dict, float, int, list, str, none_type search_appointment()

Searchappointments

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import appointments_api
from ehelply_python_experimental_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_experimental_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_experimental_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = appointments_api.AppointmentsApi(api_client)

    # example passing only optional values
    query_params = {
        'place_uuid': "place_uuid_example",
        'exclude_cancelled': False,
        'is_deleted': False,
        'start_range': "start_range_example",
        'end_range': "end_range_example",
        'page': 1,
        'page_size': 25,
        'sort_on': "sort_on_example",
        'sort_desc': False,
    }
    header_params = {
        'x-access-token': "x-access-token_example",
        'x-secret-token': "x-secret-token_example",
        'authorization': "authorization_example",
        'ehelply-active-participant': "ehelply-active-participant_example",
        'ehelply-project': "ehelply-project_example",
        'ehelply-data': "ehelply-data_example",
    }
    try:
        # Searchappointments
        api_response = api_instance.search_appointment(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling AppointmentsApi->search_appointment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
place_uuid | PlaceUuidSchema | | optional
exclude_cancelled | ExcludeCancelledSchema | | optional
is_deleted | IsDeletedSchema | | optional
start_range | StartRangeSchema | | optional
end_range | EndRangeSchema | | optional
page | PageSchema | | optional
page_size | PageSizeSchema | | optional
sort_on | SortOnSchema | | optional
sort_desc | SortDescSchema | | optional


#### PlaceUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ExcludeCancelledSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

#### IsDeletedSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

#### StartRangeSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EndRangeSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### PageSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 1

#### PageSizeSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 25

#### SortOnSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### SortDescSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
x-access-token | XAccessTokenSchema | | optional
x-secret-token | XSecretTokenSchema | | optional
authorization | AuthorizationSchema | | optional
ehelply-active-participant | EhelplyActiveParticipantSchema | | optional
ehelply-project | EhelplyProjectSchema | | optional
ehelply-data | EhelplyDataSchema | | optional

#### XAccessTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### XSecretTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AuthorizationSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyActiveParticipantSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyProjectSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyDataSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response
404 | ApiResponseFor404 | Not found
422 | ApiResponseFor422 | Validation Error

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_appointment_entities**
> bool, date, datetime, dict, float, int, list, str, none_type search_appointment_entities(appointment_uuid)

Searchappointmententities

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import appointments_api
from ehelply_python_experimental_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_experimental_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_experimental_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = appointments_api.AppointmentsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'appointment_uuid': "appointment_uuid_example",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # Searchappointmententities
        api_response = api_instance.search_appointment_entities(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling AppointmentsApi->search_appointment_entities: %s\n" % e)

    # example passing only optional values
    path_params = {
        'appointment_uuid': "appointment_uuid_example",
    }
    query_params = {
        'page': 1,
        'page_size': 25,
        'sort_on': "sort_on_example",
        'sort_desc': False,
        'search': "search_example",
        'search_on': "search_on_example",
    }
    header_params = {
        'x-access-token': "x-access-token_example",
        'x-secret-token': "x-secret-token_example",
        'authorization': "authorization_example",
        'ehelply-active-participant': "ehelply-active-participant_example",
        'ehelply-project': "ehelply-project_example",
        'ehelply-data': "ehelply-data_example",
    }
    try:
        # Searchappointmententities
        api_response = api_instance.search_appointment_entities(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling AppointmentsApi->search_appointment_entities: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page | PageSchema | | optional
page_size | PageSizeSchema | | optional
sort_on | SortOnSchema | | optional
sort_desc | SortDescSchema | | optional
search | SearchSchema | | optional
search_on | SearchOnSchema | | optional


#### PageSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 1

#### PageSizeSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 25

#### SortOnSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### SortDescSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

#### SearchSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### SearchOnSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
x-access-token | XAccessTokenSchema | | optional
x-secret-token | XSecretTokenSchema | | optional
authorization | AuthorizationSchema | | optional
ehelply-active-participant | EhelplyActiveParticipantSchema | | optional
ehelply-project | EhelplyProjectSchema | | optional
ehelply-data | EhelplyDataSchema | | optional

#### XAccessTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### XSecretTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AuthorizationSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyActiveParticipantSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyProjectSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyDataSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
appointment_uuid | AppointmentUuidSchema | | 

#### AppointmentUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response
404 | ApiResponseFor404 | Not found
422 | ApiResponseFor422 | Validation Error

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_entity_appointments**
> bool, date, datetime, dict, float, int, list, str, none_type search_entity_appointments(entity_uuid)

Getentityappointments

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import appointments_api
from ehelply_python_experimental_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_experimental_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_experimental_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = appointments_api.AppointmentsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'entity_uuid': "entity_uuid_example",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # Getentityappointments
        api_response = api_instance.search_entity_appointments(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling AppointmentsApi->search_entity_appointments: %s\n" % e)

    # example passing only optional values
    path_params = {
        'entity_uuid': "entity_uuid_example",
    }
    query_params = {
        'start_date': "start_date_example",
        'end_date': "end_date_example",
        'exclude_cancelled': False,
    }
    header_params = {
        'x-access-token': "x-access-token_example",
        'x-secret-token': "x-secret-token_example",
        'authorization': "authorization_example",
        'ehelply-active-participant': "ehelply-active-participant_example",
        'ehelply-project': "ehelply-project_example",
        'ehelply-data': "ehelply-data_example",
    }
    try:
        # Getentityappointments
        api_response = api_instance.search_entity_appointments(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling AppointmentsApi->search_entity_appointments: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
start_date | StartDateSchema | | optional
end_date | EndDateSchema | | optional
exclude_cancelled | ExcludeCancelledSchema | | optional


#### StartDateSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EndDateSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ExcludeCancelledSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
x-access-token | XAccessTokenSchema | | optional
x-secret-token | XSecretTokenSchema | | optional
authorization | AuthorizationSchema | | optional
ehelply-active-participant | EhelplyActiveParticipantSchema | | optional
ehelply-project | EhelplyProjectSchema | | optional
ehelply-data | EhelplyDataSchema | | optional

#### XAccessTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### XSecretTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AuthorizationSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyActiveParticipantSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyProjectSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyDataSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
entity_uuid | EntityUuidSchema | | 

#### EntityUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response
404 | ApiResponseFor404 | Not found
422 | ApiResponseFor422 | Validation Error

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_appointment**
> AppointmentResponse update_appointment(appointment_uuidappointment_base)

Updateappointment

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import appointments_api
from ehelply_python_experimental_sdk.model.appointment_response import AppointmentResponse
from ehelply_python_experimental_sdk.model.appointment_base import AppointmentBase
from ehelply_python_experimental_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_experimental_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_experimental_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = appointments_api.AppointmentsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'appointment_uuid': "appointment_uuid_example",
    }
    header_params = {
    }
    body = AppointmentBase(
        project_uuid="project_uuid",
        place_uuid="place_uuid",
        review_group_uuid="review_group_uuid",
        expected_finish_at="2020-06-27T12:00:00.000000",
        expected_start_at="2020-06-27T12:00:00.000000",
        actual_start_at="2020-06-27T12:00:00.000000",
        actual_finish_at="2020-06-27T12:00:00.000000",
        products=dict(),
        meta_uuid="meta_uuid",
        status="Awaiting Approval",
        cancellation_at="2020-06-27T12:00:00.000000",
        cancellation_reason="Sick",
        cancellation_entity_uuid="user_uuid",
    )
    try:
        # Updateappointment
        api_response = api_instance.update_appointment(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling AppointmentsApi->update_appointment: %s\n" % e)

    # example passing only optional values
    path_params = {
        'appointment_uuid': "appointment_uuid_example",
    }
    header_params = {
        'x-access-token': "x-access-token_example",
        'x-secret-token': "x-secret-token_example",
        'authorization': "authorization_example",
        'ehelply-active-participant': "ehelply-active-participant_example",
        'ehelply-project': "ehelply-project_example",
        'ehelply-data': "ehelply-data_example",
    }
    body = AppointmentBase(
        project_uuid="project_uuid",
        place_uuid="place_uuid",
        review_group_uuid="review_group_uuid",
        expected_finish_at="2020-06-27T12:00:00.000000",
        expected_start_at="2020-06-27T12:00:00.000000",
        actual_start_at="2020-06-27T12:00:00.000000",
        actual_finish_at="2020-06-27T12:00:00.000000",
        products=dict(),
        meta_uuid="meta_uuid",
        status="Awaiting Approval",
        cancellation_at="2020-06-27T12:00:00.000000",
        cancellation_reason="Sick",
        cancellation_entity_uuid="user_uuid",
    )
    try:
        # Updateappointment
        api_response = api_instance.update_appointment(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling AppointmentsApi->update_appointment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AppointmentBase**](AppointmentBase.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
x-access-token | XAccessTokenSchema | | optional
x-secret-token | XSecretTokenSchema | | optional
authorization | AuthorizationSchema | | optional
ehelply-active-participant | EhelplyActiveParticipantSchema | | optional
ehelply-project | EhelplyProjectSchema | | optional
ehelply-data | EhelplyDataSchema | | optional

#### XAccessTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### XSecretTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AuthorizationSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyActiveParticipantSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyProjectSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyDataSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
appointment_uuid | AppointmentUuidSchema | | 

#### AppointmentUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response
403 | ApiResponseFor403 | Unauthorized - Denied by eHelply
404 | ApiResponseFor404 | Appointment does not exist
422 | ApiResponseFor422 | Validation Error

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AppointmentResponse**](AppointmentResponse.md) |  | 


#### ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor403ResponseBodyApplicationJson

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor404ResponseBodyApplicationJson

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



[**AppointmentResponse**](AppointmentResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

