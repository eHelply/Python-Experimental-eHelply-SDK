# ehelply_python_experimental_sdk.MonitorApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acknowledge_alarm**](MonitorApi.md#acknowledge_alarm) | **POST** /sam/monitor/services/{service}/stages/{stage}/alarms/{alarm_uuid}/acknowledge | Acknowledgealarm
[**assign_alarm**](MonitorApi.md#assign_alarm) | **POST** /sam/monitor/services/{service}/stages/{stage}/alarms/{alarm_uuid}/assign | Assignalarm
[**attach_alarm_note**](MonitorApi.md#attach_alarm_note) | **POST** /sam/monitor/services/{service}/stages/{stage}/alarms/{alarm_uuid}/note | Attachalarmnote
[**attach_alarm_ticket**](MonitorApi.md#attach_alarm_ticket) | **POST** /sam/monitor/services/{service}/stages/{stage}/alarms/{alarm_uuid}/ticket | Attachalarmticket
[**clear_alarm**](MonitorApi.md#clear_alarm) | **POST** /sam/monitor/services/{service}/stages/{stage}/alarms/{alarm_uuid}/clear | Clearalarm
[**get_service**](MonitorApi.md#get_service) | **GET** /sam/monitor/services/{service} | Getservice
[**get_service_alarm**](MonitorApi.md#get_service_alarm) | **GET** /sam/monitor/services/{service}/stages/{stage}/alarms/{alarm_uuid} | Getservicealarm
[**get_service_alarms**](MonitorApi.md#get_service_alarms) | **GET** /sam/monitor/services/{service}/stages/{stage}/alarms | Getservicealarms
[**get_service_heartbeat**](MonitorApi.md#get_service_heartbeat) | **GET** /sam/monitor/services/{service}/stages/{stage}/heartbeats | Getserviceheartbeat
[**get_service_kpis**](MonitorApi.md#get_service_kpis) | **GET** /sam/monitor/services/{service}/kpis | Getservicekpis
[**get_service_spec**](MonitorApi.md#get_service_spec) | **GET** /sam/monitor/services/{service}/specs/{spec} | Getservicespec
[**get_service_specs**](MonitorApi.md#get_service_specs) | **GET** /sam/monitor/services/{service}/specs | Getservicespecs
[**get_service_vitals**](MonitorApi.md#get_service_vitals) | **GET** /sam/monitor/services/{service}/stages/{stage}/vitals | Getservicevitals
[**get_services**](MonitorApi.md#get_services) | **GET** /sam/monitor/services | Getservices
[**get_services_with_specs**](MonitorApi.md#get_services_with_specs) | **GET** /sam/monitor/specs/services | Getserviceswithspecs
[**hide_service**](MonitorApi.md#hide_service) | **POST** /sam/monitor/services/{service}/stages/{stage}/hide | Hideservice
[**ignore_alarm**](MonitorApi.md#ignore_alarm) | **POST** /sam/monitor/services/{service}/stages/{stage}/alarms/{alarm_uuid}/ignore | Ignorealarm
[**register_service**](MonitorApi.md#register_service) | **POST** /sam/monitor/services | Registerservice
[**search_alarms**](MonitorApi.md#search_alarms) | **GET** /sam/monitor/services/{service}/alarms | Searchalarms
[**show_service**](MonitorApi.md#show_service) | **POST** /sam/monitor/services/{service}/stages/{stage}/show | Showservice
[**terminate_alarm**](MonitorApi.md#terminate_alarm) | **POST** /sam/monitor/services/{service}/stages/{stage}/alarms/{alarm_uuid}/terminate | Terminatealarm
[**trigger_alarm**](MonitorApi.md#trigger_alarm) | **POST** /sam/monitor/services/{service}/stages/{stage}/alarms | Triggeralarm

# **acknowledge_alarm**
> AlarmResponse acknowledge_alarm(servicestagealarm_uuidalarm_acknowledge)

Acknowledgealarm

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import monitor_api
from ehelply_python_experimental_sdk.model.alarm_acknowledge import AlarmAcknowledge
from ehelply_python_experimental_sdk.model.alarm_response import AlarmResponse
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
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
        'alarm_uuid': "alarm_uuid_example",
    }
    body = AlarmAcknowledge(
        acknowledger_uuid="acknowledger_uuid_example",
    )
    try:
        # Acknowledgealarm
        api_response = api_instance.acknowledge_alarm(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->acknowledge_alarm: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
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
[**AlarmAcknowledge**](AlarmAcknowledge.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 
alarm_uuid | AlarmUuidSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AlarmUuidSchema

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
[**AlarmResponse**](AlarmResponse.md) |  | 


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



[**AlarmResponse**](AlarmResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_alarm**
> AlarmResponse assign_alarm(servicestagealarm_uuidalarm_assign)

Assignalarm

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import monitor_api
from ehelply_python_experimental_sdk.model.alarm_assign import AlarmAssign
from ehelply_python_experimental_sdk.model.alarm_response import AlarmResponse
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
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
        'alarm_uuid': "alarm_uuid_example",
    }
    body = AlarmAssign(
        assignee_uuid="assignee_uuid_example",
    )
    try:
        # Assignalarm
        api_response = api_instance.assign_alarm(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->assign_alarm: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
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
[**AlarmAssign**](AlarmAssign.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 
alarm_uuid | AlarmUuidSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AlarmUuidSchema

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
[**AlarmResponse**](AlarmResponse.md) |  | 


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



[**AlarmResponse**](AlarmResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_alarm_note**
> AlarmResponse attach_alarm_note(servicestagealarm_uuidalarm_note)

Attachalarmnote

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import monitor_api
from ehelply_python_experimental_sdk.model.alarm_note import AlarmNote
from ehelply_python_experimental_sdk.model.alarm_response import AlarmResponse
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
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
        'alarm_uuid': "alarm_uuid_example",
    }
    body = AlarmNote(
        author_uuid="author_uuid_example",
        message="message_example",
    )
    try:
        # Attachalarmnote
        api_response = api_instance.attach_alarm_note(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->attach_alarm_note: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
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
[**AlarmNote**](AlarmNote.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 
alarm_uuid | AlarmUuidSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AlarmUuidSchema

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
[**AlarmResponse**](AlarmResponse.md) |  | 


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



[**AlarmResponse**](AlarmResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_alarm_ticket**
> AlarmResponse attach_alarm_ticket(servicestagealarm_uuidalarm_ticket)

Attachalarmticket

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import monitor_api
from ehelply_python_experimental_sdk.model.alarm_response import AlarmResponse
from ehelply_python_experimental_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_experimental_sdk.model.alarm_ticket import AlarmTicket
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_experimental_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_experimental_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
        'alarm_uuid': "alarm_uuid_example",
    }
    body = AlarmTicket(
        ticket_uuid="ticket_uuid_example",
    )
    try:
        # Attachalarmticket
        api_response = api_instance.attach_alarm_ticket(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->attach_alarm_ticket: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
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
[**AlarmTicket**](AlarmTicket.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 
alarm_uuid | AlarmUuidSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AlarmUuidSchema

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
[**AlarmResponse**](AlarmResponse.md) |  | 


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



[**AlarmResponse**](AlarmResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_alarm**
> AlarmResponse clear_alarm(servicestagealarm_uuid)

Clearalarm

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import monitor_api
from ehelply_python_experimental_sdk.model.alarm_response import AlarmResponse
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
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
        'alarm_uuid': "alarm_uuid_example",
    }
    try:
        # Clearalarm
        api_response = api_instance.clear_alarm(
            path_params=path_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->clear_alarm: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 
alarm_uuid | AlarmUuidSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AlarmUuidSchema

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
[**AlarmResponse**](AlarmResponse.md) |  | 


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



[**AlarmResponse**](AlarmResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service**
> ServiceResponse get_service(service)

Getservice

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import monitor_api
from ehelply_python_experimental_sdk.model.service_response import ServiceResponse
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
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
    }
    query_params = {
    }
    try:
        # Getservice
        api_response = api_instance.get_service(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service': "service_example",
    }
    query_params = {
        'heartbeats': False,
        'heartbeat_limit': 5,
        'alarms': False,
        'alarm_limit': 5,
        'stage': "stage_example",
    }
    try:
        # Getservice
        api_response = api_instance.get_service(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
heartbeats | HeartbeatsSchema | | optional
heartbeat_limit | HeartbeatLimitSchema | | optional
alarms | AlarmsSchema | | optional
alarm_limit | AlarmLimitSchema | | optional
stage | StageSchema | | optional


#### HeartbeatsSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

#### HeartbeatLimitSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 5

#### AlarmsSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

#### AlarmLimitSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 5

#### StageSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 

#### ServiceSchema

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
[**ServiceResponse**](ServiceResponse.md) |  | 


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



[**ServiceResponse**](ServiceResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_alarm**
> AlarmResponse get_service_alarm(servicestagealarm_uuid)

Getservicealarm

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import monitor_api
from ehelply_python_experimental_sdk.model.alarm_response import AlarmResponse
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
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
        'alarm_uuid': "alarm_uuid_example",
    }
    try:
        # Getservicealarm
        api_response = api_instance.get_service_alarm(
            path_params=path_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_alarm: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 
alarm_uuid | AlarmUuidSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AlarmUuidSchema

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
[**AlarmResponse**](AlarmResponse.md) |  | 


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



[**AlarmResponse**](AlarmResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_alarms**
> [AlarmResponse] get_service_alarms(servicestage)

Getservicealarms

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import monitor_api
from ehelply_python_experimental_sdk.model.alarm_response import AlarmResponse
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
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
    }
    query_params = {
    }
    try:
        # Getservicealarms
        api_response = api_instance.get_service_alarms(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_alarms: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
    }
    query_params = {
        'history': 5,
        'include_terminated': False,
        'include_cleared': False,
    }
    try:
        # Getservicealarms
        api_response = api_instance.get_service_alarms(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_alarms: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
history | HistorySchema | | optional
include_terminated | IncludeTerminatedSchema | | optional
include_cleared | IncludeClearedSchema | | optional


#### HistorySchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 5

#### IncludeTerminatedSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

#### IncludeClearedSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

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
**[AlarmResponse]** |  | 

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



[**[AlarmResponse]**](AlarmResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_heartbeat**
> [HeartbeatResponse] get_service_heartbeat(servicestage)

Getserviceheartbeat

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import monitor_api
from ehelply_python_experimental_sdk.model.heartbeat_response import HeartbeatResponse
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
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
    }
    query_params = {
    }
    try:
        # Getserviceheartbeat
        api_response = api_instance.get_service_heartbeat(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_heartbeat: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
    }
    query_params = {
        'history': 5,
    }
    try:
        # Getserviceheartbeat
        api_response = api_instance.get_service_heartbeat(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_heartbeat: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
history | HistorySchema | | optional


#### HistorySchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 5

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

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
**[HeartbeatResponse]** |  | 

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



[**[HeartbeatResponse]**](HeartbeatResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_kpis**
> [KpiResponse] get_service_kpis(service)

Getservicekpis

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import monitor_api
from ehelply_python_experimental_sdk.model.kpi_response import KpiResponse
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
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
    }
    query_params = {
    }
    try:
        # Getservicekpis
        api_response = api_instance.get_service_kpis(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_kpis: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service': "service_example",
    }
    query_params = {
        'history': 5,
    }
    try:
        # Getservicekpis
        api_response = api_instance.get_service_kpis(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_kpis: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
history | HistorySchema | | optional


#### HistorySchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 5

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 

#### ServiceSchema

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
**[KpiResponse]** |  | 

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



[**[KpiResponse]**](KpiResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_spec**
> GetServiceSpecResponse get_service_spec(servicespec)

Getservicespec

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import monitor_api
from ehelply_python_experimental_sdk.model.get_service_spec_response import GetServiceSpecResponse
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
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'spec': "spec_example",
    }
    try:
        # Getservicespec
        api_response = api_instance.get_service_spec(
            path_params=path_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_spec: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
spec | SpecSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### SpecSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response
403 | ApiResponseFor403 | Unauthorized - Denied by eHelply
404 | ApiResponseFor404 | Not found
422 | ApiResponseFor422 | Validation Error

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

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



[**GetServiceSpecResponse**](GetServiceSpecResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_specs**
> GetServiceSpecsResponse get_service_specs(service)

Getservicespecs

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import monitor_api
from ehelply_python_experimental_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_experimental_sdk.model.get_service_specs_response import GetServiceSpecsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_experimental_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_experimental_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
    }
    try:
        # Getservicespecs
        api_response = api_instance.get_service_specs(
            path_params=path_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_specs: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response
403 | ApiResponseFor403 | Unauthorized - Denied by eHelply
404 | ApiResponseFor404 | Not found
422 | ApiResponseFor422 | Validation Error

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

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



[**GetServiceSpecsResponse**](GetServiceSpecsResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_vitals**
> [StatsVitalsResponse] get_service_vitals(servicestage)

Getservicevitals

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import monitor_api
from ehelply_python_experimental_sdk.model.stats_vitals_response import StatsVitalsResponse
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
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
    }
    query_params = {
    }
    try:
        # Getservicevitals
        api_response = api_instance.get_service_vitals(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_vitals: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
    }
    query_params = {
        'history': 5,
    }
    try:
        # Getservicevitals
        api_response = api_instance.get_service_vitals(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_vitals: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
history | HistorySchema | | optional


#### HistorySchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 5

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

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
**[StatsVitalsResponse]** |  | 

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



[**[StatsVitalsResponse]**](StatsVitalsResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_services**
> [ServiceResponse] get_services()

Getservices

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import monitor_api
from ehelply_python_experimental_sdk.model.service_response import ServiceResponse
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
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only optional values
    query_params = {
        'heartbeats': False,
        'heartbeat_limit': 5,
        'alarms': False,
        'alarm_limit': 5,
        'include_hidden': False,
        'stage': "stage_example",
        'key': "key_example",
    }
    try:
        # Getservices
        api_response = api_instance.get_services(
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_services: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
heartbeats | HeartbeatsSchema | | optional
heartbeat_limit | HeartbeatLimitSchema | | optional
alarms | AlarmsSchema | | optional
alarm_limit | AlarmLimitSchema | | optional
include_hidden | IncludeHiddenSchema | | optional
stage | StageSchema | | optional
key | KeySchema | | optional


#### HeartbeatsSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

#### HeartbeatLimitSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 5

#### AlarmsSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

#### AlarmLimitSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 5

#### IncludeHiddenSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

#### StageSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### KeySchema

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
**[ServiceResponse]** |  | 

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



[**[ServiceResponse]**](ServiceResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_services_with_specs**
> GetServiceServiceWithSpecsResponse get_services_with_specs()

Getserviceswithspecs

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import monitor_api
from ehelply_python_experimental_sdk.model.get_service_service_with_specs_response import GetServiceServiceWithSpecsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_experimental_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_experimental_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Getserviceswithspecs
        api_response = api_instance.get_services_with_specs()
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_services_with_specs: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response
403 | ApiResponseFor403 | Unauthorized - Denied by eHelply
404 | ApiResponseFor404 | Not found

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

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
body | Unset | body was not defined |
headers | Unset | headers were not defined |


[**GetServiceServiceWithSpecsResponse**](GetServiceServiceWithSpecsResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hide_service**
> ServiceMessageResponse hide_service(servicestage)

Hideservice

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import monitor_api
from ehelply_python_experimental_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_experimental_sdk.model.service_message_response import ServiceMessageResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_experimental_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_experimental_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
    }
    try:
        # Hideservice
        api_response = api_instance.hide_service(
            path_params=path_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->hide_service: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

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
[**ServiceMessageResponse**](ServiceMessageResponse.md) |  | 


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



[**ServiceMessageResponse**](ServiceMessageResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ignore_alarm**
> AlarmResponse ignore_alarm(servicestagealarm_uuidalarm_ignore)

Ignorealarm

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import monitor_api
from ehelply_python_experimental_sdk.model.alarm_response import AlarmResponse
from ehelply_python_experimental_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_experimental_sdk.model.alarm_ignore import AlarmIgnore
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_experimental_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_experimental_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
        'alarm_uuid': "alarm_uuid_example",
    }
    body = AlarmIgnore(
        ignorer_uuid="ignorer_uuid_example",
    )
    try:
        # Ignorealarm
        api_response = api_instance.ignore_alarm(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->ignore_alarm: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
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
[**AlarmIgnore**](AlarmIgnore.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 
alarm_uuid | AlarmUuidSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AlarmUuidSchema

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
[**AlarmResponse**](AlarmResponse.md) |  | 


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



[**AlarmResponse**](AlarmResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_service**
> ServiceResponse register_service(service_create)

Registerservice

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import monitor_api
from ehelply_python_experimental_sdk.model.service_response import ServiceResponse
from ehelply_python_experimental_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_experimental_sdk.model.service_create import ServiceCreate
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_experimental_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_experimental_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    body = ServiceCreate(
        name="name_example",
        key="key_example",
        version="version_example",
        summary="summary_example",
        authors=[
            "authors_example"
        ],
        author_emails=[
            "author_emails_example"
        ],
    )
    try:
        # Registerservice
        api_response = api_instance.register_service(
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->register_service: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServiceCreate**](ServiceCreate.md) |  | 


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
[**ServiceResponse**](ServiceResponse.md) |  | 


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



[**ServiceResponse**](ServiceResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_alarms**
> Page search_alarms(service)

Searchalarms

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import monitor_api
from ehelply_python_experimental_sdk.model.page import Page
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
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
    }
    query_params = {
    }
    try:
        # Searchalarms
        api_response = api_instance.search_alarms(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->search_alarms: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service': "service_example",
    }
    query_params = {
        'page': 1,
        'page_size': 25,
        'search': "search_example",
        'search_on': "search_on_example",
        'sort_on': "sort_on_example",
        'sort_desc': False,
    }
    try:
        # Searchalarms
        api_response = api_instance.search_alarms(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->search_alarms: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
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
search | SearchSchema | | optional
search_on | SearchOnSchema | | optional
sort_on | SortOnSchema | | optional
sort_desc | SortDescSchema | | optional


#### PageSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 1

#### PageSizeSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 25

#### SearchSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### SearchOnSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### SortOnSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### SortDescSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 

#### ServiceSchema

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
[**Page**](Page.md) |  | 


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



[**Page**](Page.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_service**
> ServiceMessageResponse show_service(servicestage)

Showservice

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import monitor_api
from ehelply_python_experimental_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_experimental_sdk.model.service_message_response import ServiceMessageResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_experimental_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_experimental_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
    }
    try:
        # Showservice
        api_response = api_instance.show_service(
            path_params=path_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->show_service: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

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
[**ServiceMessageResponse**](ServiceMessageResponse.md) |  | 


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



[**ServiceMessageResponse**](ServiceMessageResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_alarm**
> AlarmResponse terminate_alarm(servicestagealarm_uuidalarm_terminate)

Terminatealarm

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import monitor_api
from ehelply_python_experimental_sdk.model.alarm_terminate import AlarmTerminate
from ehelply_python_experimental_sdk.model.alarm_response import AlarmResponse
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
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
        'alarm_uuid': "alarm_uuid_example",
    }
    body = AlarmTerminate(
        terminater_uuid="terminater_uuid_example",
    )
    try:
        # Terminatealarm
        api_response = api_instance.terminate_alarm(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->terminate_alarm: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
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
[**AlarmTerminate**](AlarmTerminate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 
alarm_uuid | AlarmUuidSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AlarmUuidSchema

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
[**AlarmResponse**](AlarmResponse.md) |  | 


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



[**AlarmResponse**](AlarmResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_alarm**
> AlarmResponse trigger_alarm(servicestagealarm_create)

Triggeralarm

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import monitor_api
from ehelply_python_experimental_sdk.model.alarm_create import AlarmCreate
from ehelply_python_experimental_sdk.model.alarm_response import AlarmResponse
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
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
    }
    body = AlarmCreate(
        process="process_example",
        severity="severity_example",
        name="name_example",
        summary="summary_example",
        description="description_example",
    )
    try:
        # Triggeralarm
        api_response = api_instance.trigger_alarm(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MonitorApi->trigger_alarm: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
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
[**AlarmCreate**](AlarmCreate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

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
[**AlarmResponse**](AlarmResponse.md) |  | 


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



[**AlarmResponse**](AlarmResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

