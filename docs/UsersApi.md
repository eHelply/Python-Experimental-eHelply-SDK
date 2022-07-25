# ehelply_python_experimental_sdk.UsersApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_signup**](UsersApi.md#confirm_signup) | **POST** /sam/users/auth/signup/confirm | Confirmsignup
[**create_participant**](UsersApi.md#create_participant) | **POST** /sam/users/participants | Createparticipant
[**create_user**](UsersApi.md#create_user) | **POST** /sam/users | Createuser
[**delete_participant**](UsersApi.md#delete_participant) | **DELETE** /sam/users/participants/{participant_id} | Deleteparticipant
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /sam/users/{user_id} | Deleteuser
[**get_participant**](UsersApi.md#get_participant) | **GET** /sam/users/participants/{participant_id} | Getparticipant
[**get_user**](UsersApi.md#get_user) | **GET** /sam/users/{user_id} | Getuser
[**login**](UsersApi.md#login) | **POST** /sam/users/auth/login | Login
[**refresh_token**](UsersApi.md#refresh_token) | **POST** /sam/users/auth/{app_client}/refresh-token | Refreshtoken
[**reset_password**](UsersApi.md#reset_password) | **POST** /sam/users/auth/password/reset | Resetpassword
[**reset_password_confirmation**](UsersApi.md#reset_password_confirmation) | **POST** /sam/users/auth/password/reset/confirm | Resetpasswordconfirmation
[**search_participants**](UsersApi.md#search_participants) | **GET** /sam/users/participants | Searchparticipants
[**signup**](UsersApi.md#signup) | **POST** /sam/users/auth/signup | Signup
[**update_participant**](UsersApi.md#update_participant) | **PUT** /sam/users/participants/{participant_id} | Updateparticipant
[**update_user**](UsersApi.md#update_user) | **PUT** /sam/users/{user_id} | Updateuser
[**user_validations**](UsersApi.md#user_validations) | **POST** /sam/users/validations/{field} | Uservalidations

# **confirm_signup**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} confirm_signup(user_confirmation)

Confirmsignup

Validates a user signup with a given confirmation

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import users_api
from ehelply_python_experimental_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_experimental_sdk.model.user_confirmation import UserConfirmation
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_experimental_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_experimental_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)

    # example passing only required values which don't have defaults set
    body = UserConfirmation(
        email="email_example",
        verification_code="verification_code_example",
    )
    try:
        # Confirmsignup
        api_response = api_instance.confirm_signup(
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling UsersApi->confirm_signup: %s\n" % e)
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
[**UserConfirmation**](UserConfirmation.md) |  | 


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

# **create_participant**
> ParticipantUserReturn create_participant(participant_create)

Createparticipant

Creates a participant given the participant info (meta and user_id)

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import users_api
from ehelply_python_experimental_sdk.model.participant_user_return import ParticipantUserReturn
from ehelply_python_experimental_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_experimental_sdk.model.participant_create import ParticipantCreate
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_experimental_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_experimental_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = ParticipantCreate(
        meta=dict(),
        user_uuid="user_uuid_example",
    )
    try:
        # Createparticipant
        api_response = api_instance.create_participant(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling UsersApi->create_participant: %s\n" % e)

    # example passing only optional values
    header_params = {
        'x-access-token': "x-access-token_example",
        'x-secret-token': "x-secret-token_example",
        'authorization': "authorization_example",
        'ehelply-active-participant': "ehelply-active-participant_example",
        'ehelply-project': "ehelply-project_example",
        'ehelply-data': "ehelply-data_example",
    }
    body = ParticipantCreate(
        meta=dict(),
        user_uuid="user_uuid_example",
    )
    try:
        # Createparticipant
        api_response = api_instance.create_participant(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling UsersApi->create_participant: %s\n" % e)
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
[**ParticipantCreate**](ParticipantCreate.md) |  | 


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
[**ParticipantUserReturn**](ParticipantUserReturn.md) |  | 


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



[**ParticipantUserReturn**](ParticipantUserReturn.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> UserResponse create_user()

Createuser

Usually ran after login and will do the following: - If no user exists (AKA signed in with social media) it will create a new user and default participant - If a user exists, sync Cognito data from Cognito to the user - Determine missing fields that SHOULD be filled

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import users_api
from ehelply_python_experimental_sdk.model.user_response import UserResponse
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
    api_instance = users_api.UsersApi(api_client)

    # example passing only optional values
    header_params = {
        'authorization': "authorization_example",
    }
    try:
        # Createuser
        api_response = api_instance.create_user(
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
authorization | AuthorizationSchema | | optional

#### AuthorizationSchema

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
[**UserResponse**](UserResponse.md) |  | 


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



[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_participant**
> bool delete_participant(participant_id)

Deleteparticipant

Delete participants related to the given participant_id, returns True if successful

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import users_api
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
    api_instance = users_api.UsersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'participant_id': "participant_id_example",
    }
    header_params = {
    }
    try:
        # Deleteparticipant
        api_response = api_instance.delete_participant(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling UsersApi->delete_participant: %s\n" % e)

    # example passing only optional values
    path_params = {
        'participant_id': "participant_id_example",
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
        # Deleteparticipant
        api_response = api_instance.delete_participant(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling UsersApi->delete_participant: %s\n" % e)
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
participant_id | ParticipantIdSchema | | 

#### ParticipantIdSchema

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

# **delete_user**
> bool delete_user(user_id)

Deleteuser

Soft deletes the user with the provided user id, granted the deleter is the same person or an admin. Returns True if successful

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import users_api
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
    api_instance = users_api.UsersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user_id': "user_id_example",
    }
    header_params = {
    }
    try:
        # Deleteuser
        api_response = api_instance.delete_user(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)

    # example passing only optional values
    path_params = {
        'user_id': "user_id_example",
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
        # Deleteuser
        api_response = api_instance.delete_user(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
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
user_id | UserIdSchema | | 

#### UserIdSchema

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

# **get_participant**
> ParticipantUserReturn get_participant(participant_id)

Getparticipant

Gets a participant given their participant ID

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import users_api
from ehelply_python_experimental_sdk.model.participant_user_return import ParticipantUserReturn
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
    api_instance = users_api.UsersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'participant_id': "participant_id_example",
    }
    header_params = {
    }
    try:
        # Getparticipant
        api_response = api_instance.get_participant(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling UsersApi->get_participant: %s\n" % e)

    # example passing only optional values
    path_params = {
        'participant_id': "participant_id_example",
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
        # Getparticipant
        api_response = api_instance.get_participant(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling UsersApi->get_participant: %s\n" % e)
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
participant_id | ParticipantIdSchema | | 

#### ParticipantIdSchema

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
[**ParticipantUserReturn**](ParticipantUserReturn.md) |  | 


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



[**ParticipantUserReturn**](ParticipantUserReturn.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserResponse get_user(user_id)

Getuser

Gets the user object given user id (uuid) or cognito id (cognito)

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import users_api
from ehelply_python_experimental_sdk.model.user_response import UserResponse
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
    api_instance = users_api.UsersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user_id': "user_id_example",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # Getuser
        api_response = api_instance.get_user(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)

    # example passing only optional values
    path_params = {
        'user_id': "user_id_example",
    }
    query_params = {
        'id_type': "cognito OR uuid",
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
        # Getuser
        api_response = api_instance.get_user(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
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
id_type | IdTypeSchema | | optional


#### IdTypeSchema

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
user_id | UserIdSchema | | 

#### UserIdSchema

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
[**UserResponse**](UserResponse.md) |  | 


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



[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> UserLoginReturn login(user_login)

Login

Login endpoint, returns tokens. EMAIL NEEDS TO BE VERIFIED (can be done through the email the user received).

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import users_api
from ehelply_python_experimental_sdk.model.user_login import UserLogin
from ehelply_python_experimental_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_experimental_sdk.model.user_login_return import UserLoginReturn
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_experimental_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_experimental_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)

    # example passing only required values which don't have defaults set
    body = UserLogin(
        username="username_example",
        password="password_example",
    )
    try:
        # Login
        api_response = api_instance.login(
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling UsersApi->login: %s\n" % e)
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
[**UserLogin**](UserLogin.md) |  | 


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
[**UserLoginReturn**](UserLoginReturn.md) |  | 


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



[**UserLoginReturn**](UserLoginReturn.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_token**
> UserTokenReturn refresh_token(app_clientbody)

Refreshtoken

Refreshes tokens given a refresh token.

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import users_api
from ehelply_python_experimental_sdk.model.user_token_return import UserTokenReturn
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
    api_instance = users_api.UsersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'app_client': "app_client_example",
    }
    body = "body_example"
    try:
        # Refreshtoken
        api_response = api_instance.refresh_token(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling UsersApi->refresh_token: %s\n" % e)
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

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
app_client | AppClientSchema | | 

#### AppClientSchema

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
[**UserTokenReturn**](UserTokenReturn.md) |  | 


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



[**UserTokenReturn**](UserTokenReturn.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} reset_password(user_password_reset)

Resetpassword

Sends the user an email with a confirmation code so they can reset their password

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import users_api
from ehelply_python_experimental_sdk.model.user_password_reset import UserPasswordReset
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
    api_instance = users_api.UsersApi(api_client)

    # example passing only required values which don't have defaults set
    body = UserPasswordReset(
        email="email_example",
    )
    try:
        # Resetpassword
        api_response = api_instance.reset_password(
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling UsersApi->reset_password: %s\n" % e)
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
[**UserPasswordReset**](UserPasswordReset.md) |  | 


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

# **reset_password_confirmation**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} reset_password_confirmation(user_password_reset_confirmation)

Resetpasswordconfirmation

Resets the given user's password to the given password when the proper code is provided

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import users_api
from ehelply_python_experimental_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_experimental_sdk.model.user_password_reset_confirmation import UserPasswordResetConfirmation
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_experimental_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_experimental_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)

    # example passing only required values which don't have defaults set
    body = UserPasswordResetConfirmation(
        email="email_example",
        confirmation_code="confirmation_code_example",
        password="password_example",
    )
    try:
        # Resetpasswordconfirmation
        api_response = api_instance.reset_password_confirmation(
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling UsersApi->reset_password_confirmation: %s\n" % e)
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
[**UserPasswordResetConfirmation**](UserPasswordResetConfirmation.md) |  | 


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

# **search_participants**
> Page search_participants()

Searchparticipants

Search participants using a user uuid, returns pagination information and list of `items` (ParticipantUserReturn from GET Participant). Can search on \"user_uuid\", and sort on any field. To search enter search value into \"search\" query param and the field into \"search on\" (currently only \"user\"uuid\"). For sorting fill out \"sort_desc\" field with either true/false and the \"sort_on\" query parameter with column you want to sort on (ex: date_created). Max pagination items per page is 50.

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import users_api
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
    api_instance = users_api.UsersApi(api_client)

    # example passing only optional values
    query_params = {
        'page': 1,
        'page_size': 25,
        'search': "search_example",
        'search_on': "search_on_example",
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
        # Searchparticipants
        api_response = api_instance.search_participants(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling UsersApi->search_participants: %s\n" % e)
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

# **signup**
> UserSignupReturn signup(user_signup)

Signup

Signup to eHelply, creates a user and default participant behind the scenes. Does not verify email.

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import users_api
from ehelply_python_experimental_sdk.model.user_signup import UserSignup
from ehelply_python_experimental_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_experimental_sdk.model.user_signup_return import UserSignupReturn
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_experimental_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_experimental_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)

    # example passing only required values which don't have defaults set
    body = UserSignup(
        username="username_example",
        password="password_example",
        email="email_example",
        first_name="first_name_example",
        last_name="last_name_example",
        phone_number="phone_number_example",
        country="country_example",
        lat="lat_example",
        lng="lng_example",
        verified_legal_terms=False,
        picture="picture_example",
        newsletters=True,
    )
    try:
        # Signup
        api_response = api_instance.signup(
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling UsersApi->signup: %s\n" % e)
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
[**UserSignup**](UserSignup.md) |  | 


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
[**UserSignupReturn**](UserSignupReturn.md) |  | 


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



[**UserSignupReturn**](UserSignupReturn.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_participant**
> ParticipantUserReturn update_participant(participant_idparticipant_update)

Updateparticipant

Update participant data given

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import users_api
from ehelply_python_experimental_sdk.model.participant_update import ParticipantUpdate
from ehelply_python_experimental_sdk.model.participant_user_return import ParticipantUserReturn
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
    api_instance = users_api.UsersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'participant_id': "participant_id_example",
    }
    header_params = {
    }
    body = ParticipantUpdate(
        meta=dict(),
        user_uuid="user_uuid_example",
        uuid="uuid_example",
    )
    try:
        # Updateparticipant
        api_response = api_instance.update_participant(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling UsersApi->update_participant: %s\n" % e)

    # example passing only optional values
    path_params = {
        'participant_id': "participant_id_example",
    }
    header_params = {
        'x-access-token': "x-access-token_example",
        'x-secret-token': "x-secret-token_example",
        'authorization': "authorization_example",
        'ehelply-active-participant': "ehelply-active-participant_example",
        'ehelply-project': "ehelply-project_example",
        'ehelply-data': "ehelply-data_example",
    }
    body = ParticipantUpdate(
        meta=dict(),
        user_uuid="user_uuid_example",
        uuid="uuid_example",
    )
    try:
        # Updateparticipant
        api_response = api_instance.update_participant(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling UsersApi->update_participant: %s\n" % e)
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
[**ParticipantUpdate**](ParticipantUpdate.md) |  | 


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
participant_id | ParticipantIdSchema | | 

#### ParticipantIdSchema

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
[**ParticipantUserReturn**](ParticipantUserReturn.md) |  | 


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



[**ParticipantUserReturn**](ParticipantUserReturn.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> UserResponse update_user(user_iduser)

Updateuser

Update the given user and sync the cognito data

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import users_api
from ehelply_python_experimental_sdk.model.user import User
from ehelply_python_experimental_sdk.model.user_response import UserResponse
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
    api_instance = users_api.UsersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user_id': "user_id_example",
    }
    header_params = {
    }
    body = User(
        cognito_id="cognito_id_example",
        cognito_data=dict(),
        first_name="first_name_example",
        last_name="last_name_example",
        email="email_example",
        phone_number="phone_number_example",
        country="country_example",
        picture="picture_example",
        gps_location=dict(),
        verified_legal_terms=False,
        date_created="1970-01-01T00:00:00.00Z",
        date_updated="1970-01-01T00:00:00.00Z",
        date_deleted="1970-01-01T00:00:00.00Z",
        uuid="uuid_example",
        last_login="1970-01-01T00:00:00.00Z",
        first_login=True,
    )
    try:
        # Updateuser
        api_response = api_instance.update_user(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)

    # example passing only optional values
    path_params = {
        'user_id': "user_id_example",
    }
    header_params = {
        'x-access-token': "x-access-token_example",
        'x-secret-token': "x-secret-token_example",
        'authorization': "authorization_example",
        'ehelply-active-participant': "ehelply-active-participant_example",
        'ehelply-project': "ehelply-project_example",
        'ehelply-data': "ehelply-data_example",
    }
    body = User(
        cognito_id="cognito_id_example",
        cognito_data=dict(),
        first_name="first_name_example",
        last_name="last_name_example",
        email="email_example",
        phone_number="phone_number_example",
        country="country_example",
        picture="picture_example",
        gps_location=dict(),
        verified_legal_terms=False,
        date_created="1970-01-01T00:00:00.00Z",
        date_updated="1970-01-01T00:00:00.00Z",
        date_deleted="1970-01-01T00:00:00.00Z",
        uuid="uuid_example",
        last_login="1970-01-01T00:00:00.00Z",
        first_login=True,
    )
    try:
        # Updateuser
        api_response = api_instance.update_user(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)
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
[**User**](User.md) |  | 


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
user_id | UserIdSchema | | 

#### UserIdSchema

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
[**UserResponse**](UserResponse.md) |  | 


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



[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_validations**
> bool user_validations(fielduser_validations)

Uservalidations

Validates a certain field.

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import users_api
from ehelply_python_experimental_sdk.model.user_validations import UserValidations
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
    api_instance = users_api.UsersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'field': "email",
    }
    header_params = {
    }
    body = UserValidations(
        value="value_example",
        validation_type="validation_type_example",
    )
    try:
        # Uservalidations
        api_response = api_instance.user_validations(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling UsersApi->user_validations: %s\n" % e)

    # example passing only optional values
    path_params = {
        'field': "email",
    }
    header_params = {
        'x-access-token': "x-access-token_example",
        'x-secret-token': "x-secret-token_example",
        'authorization': "authorization_example",
        'ehelply-active-participant': "ehelply-active-participant_example",
        'ehelply-project': "ehelply-project_example",
        'ehelply-data': "ehelply-data_example",
    }
    body = UserValidations(
        value="value_example",
        validation_type="validation_type_example",
    )
    try:
        # Uservalidations
        api_response = api_instance.user_validations(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling UsersApi->user_validations: %s\n" % e)
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
[**UserValidations**](UserValidations.md) |  | 


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
field | FieldSchema | | 

#### FieldSchema

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

