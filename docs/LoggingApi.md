# ehelply_python_experimental_sdk.LoggingApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_logs**](LoggingApi.md#get_logs) | **GET** /sam/logging/logs | Getlogs
[**get_service_logs**](LoggingApi.md#get_service_logs) | **GET** /sam/logging/logs/services/{service} | Getservicelogs
[**get_subject_logs**](LoggingApi.md#get_subject_logs) | **GET** /sam/logging/logs/services/{service}/subjects/{subject} | Getsubjectlogs

# **get_logs**
> [LoggingDynamo] get_logs()

Getlogs

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import logging_api
from ehelply_python_experimental_sdk.model.logging_dynamo import LoggingDynamo
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
    api_instance = logging_api.LoggingApi(api_client)

    # example passing only optional values
    query_params = {
        'service': "service_example",
        'date_start': "date_start_example",
        'date_end': "date_end_example",
        'desc': True,
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
        # Getlogs
        api_response = api_instance.get_logs(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling LoggingApi->get_logs: %s\n" % e)
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
service | ServiceSchema | | optional
date_start | DateStartSchema | | optional
date_end | DateEndSchema | | optional
desc | DescSchema | | optional


#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### DateStartSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### DateEndSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### DescSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to True

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
**[LoggingDynamo]** |  | 

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



[**[LoggingDynamo]**](LoggingDynamo.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_logs**
> [LoggingDynamo] get_service_logs(service)

Getservicelogs

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import logging_api
from ehelply_python_experimental_sdk.model.logging_dynamo import LoggingDynamo
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
    api_instance = logging_api.LoggingApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # Getservicelogs
        api_response = api_instance.get_service_logs(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling LoggingApi->get_service_logs: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service': "service_example",
    }
    query_params = {
        'date_start': "date_start_example",
        'date_end': "date_end_example",
        'desc': True,
        'limit': 50,
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
        # Getservicelogs
        api_response = api_instance.get_service_logs(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling LoggingApi->get_service_logs: %s\n" % e)
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
date_start | DateStartSchema | | optional
date_end | DateEndSchema | | optional
desc | DescSchema | | optional
limit | LimitSchema | | optional


#### DateStartSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### DateEndSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### DescSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to True

#### LimitSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 50

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
**[LoggingDynamo]** |  | 

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



[**[LoggingDynamo]**](LoggingDynamo.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subject_logs**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_subject_logs(servicesubject)

Getsubjectlogs

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import logging_api
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
    api_instance = logging_api.LoggingApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'subject': "subject_example",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # Getsubjectlogs
        api_response = api_instance.get_subject_logs(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling LoggingApi->get_subject_logs: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service': "service_example",
        'subject': "subject_example",
    }
    query_params = {
        'date_start': "date_start_example",
        'date_end': "date_end_example",
        'desc': True,
        'limit': 50,
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
        # Getsubjectlogs
        api_response = api_instance.get_subject_logs(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling LoggingApi->get_subject_logs: %s\n" % e)
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
date_start | DateStartSchema | | optional
date_end | DateEndSchema | | optional
desc | DescSchema | | optional
limit | LimitSchema | | optional


#### DateStartSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### DateEndSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### DescSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to True

#### LimitSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 50

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
service | ServiceSchema | | 
subject | SubjectSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### SubjectSchema

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

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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



**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

