# ehelply_python_experimental_sdk.MetaApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_field**](MetaApi.md#create_field) | **POST** /meta/field | Create Field
[**create_meta**](MetaApi.md#create_meta) | **POST** /meta/meta/service/{service}/type/{type_str}/entity/{entity_uuid} | Create Meta
[**delete_field**](MetaApi.md#delete_field) | **DELETE** /meta/field/{field_uuid} | Delete Field
[**delete_meta**](MetaApi.md#delete_meta) | **DELETE** /meta/meta/service/{service}/type/{type_str}/entity/{entity_uuid} | Delete Meta
[**delete_meta_from_uuid**](MetaApi.md#delete_meta_from_uuid) | **DELETE** /meta/meta/{meta_uuid} | Delete Meta From Uuid
[**get_field**](MetaApi.md#get_field) | **GET** /meta/field/{field_uuid} | Get Field
[**get_meta**](MetaApi.md#get_meta) | **GET** /meta/meta/service/{service}/type/{type_str}/entity/{entity_uuid} | Get Meta
[**get_meta_from_uuid**](MetaApi.md#get_meta_from_uuid) | **GET** /meta/meta/{meta_uuid} | Get Meta From Uuid
[**make_slug**](MetaApi.md#make_slug) | **POST** /meta/meta/slug | Make Slug
[**touch_meta**](MetaApi.md#touch_meta) | **POST** /meta/meta/service/{service}/type/{type_str}/entity/{entity_uuid}/touch | Touch Meta
[**update_field**](MetaApi.md#update_field) | **PUT** /meta/field/{field_uuid} | Update Field
[**update_meta**](MetaApi.md#update_meta) | **PUT** /meta/meta/service/{service}/type/{type_str}/entity/{entity_uuid} | Update Meta
[**update_meta_from_uuid**](MetaApi.md#update_meta_from_uuid) | **PUT** /meta/meta/{meta_uuid} | Update Meta From Uuid

# **create_field**
> FieldDynamo create_field(field)

Create Field

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import meta_api
from ehelply_python_experimental_sdk.model.field_dynamo import FieldDynamo
from ehelply_python_experimental_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_experimental_sdk.model.field import Field
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_experimental_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_experimental_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meta_api.MetaApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = Field(
        uuid="uuid_example",
        type=1,
        placeholder="placeholder_example",
        validations=Validations(
            value=[
                "value_example"
            ],
        ),
        hint="hint_example",
        icon="icon_example",
        label="label_example",
        options=Options(
            required=True,
            label="label_example",
            inset_label="inset_label_example",
            placeholder="placeholder_example",
            hint="hint_example",
            icon="icon_example",
            max_length=3.14,
            counter=True,
            caption="caption_example",
            color="color_example",
            size="size_example",
            type="type_example",
            icon_position="icon_position_example",
            selections=[
                OptionGroup(
                    name="name_example",
                    type="type_example",
                    selections=[
                        Selection(
                            name="name_example",
                            value=3.14,
                            icon="icon_example",
                        )
                    ],
                )
            ],
        ),
    )
    try:
        # Create Field
        api_response = api_instance.create_field(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MetaApi->create_field: %s\n" % e)

    # example passing only optional values
    header_params = {
        'x-access-token': "x-access-token_example",
        'x-secret-token': "x-secret-token_example",
        'authorization': "authorization_example",
        'ehelply-active-participant': "ehelply-active-participant_example",
        'ehelply-project': "ehelply-project_example",
        'ehelply-data': "ehelply-data_example",
    }
    body = Field(
        uuid="uuid_example",
        type=1,
        placeholder="placeholder_example",
        validations=Validations(
            value=[
                "value_example"
            ],
        ),
        hint="hint_example",
        icon="icon_example",
        label="label_example",
        options=Options(
            required=True,
            label="label_example",
            inset_label="inset_label_example",
            placeholder="placeholder_example",
            hint="hint_example",
            icon="icon_example",
            max_length=3.14,
            counter=True,
            caption="caption_example",
            color="color_example",
            size="size_example",
            type="type_example",
            icon_position="icon_position_example",
            selections=[
                OptionGroup(
                    name="name_example",
                    type="type_example",
                    selections=[
                        Selection(
                            name="name_example",
                            value=3.14,
                            icon="icon_example",
                        )
                    ],
                )
            ],
        ),
    )
    try:
        # Create Field
        api_response = api_instance.create_field(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MetaApi->create_field: %s\n" % e)
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
[**Field**](Field.md) |  | 


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
[**FieldDynamo**](FieldDynamo.md) |  | 


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



[**FieldDynamo**](FieldDynamo.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_meta**
> MetaDynamo create_meta(servicetype_strentity_uuidmeta_create)

Create Meta

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import meta_api
from ehelply_python_experimental_sdk.model.meta_create import MetaCreate
from ehelply_python_experimental_sdk.model.meta_dynamo import MetaDynamo
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
    api_instance = meta_api.MetaApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'type_str': "type_str_example",
        'entity_uuid': "entity_uuid_example",
    }
    header_params = {
    }
    body = MetaCreate(
        basic=BasicMetaCreate(
            name="name_example",
            slug=True,
        ),
        detailed=DetailedMetaCreate(
            summary="summary_example",
            description="description_example",
        ),
        custom=MetaCustom(
            name="name_example",
            description="description_example",
            _list=[
                CustomList(
                    name="name_example",
                    description="description_example",
                )
            ],
        ),
        fields=[
            Field(
                uuid="uuid_example",
                type=1,
                placeholder="placeholder_example",
                validations=Validations(
                    value=[
                        "value_example"
                    ],
                ),
                hint="hint_example",
                icon="icon_example",
                label="label_example",
                options=Options(
                    required=True,
                    label="label_example",
                    inset_label="inset_label_example",
                    placeholder="placeholder_example",
                    hint="hint_example",
                    icon="icon_example",
                    max_length=3.14,
                    counter=True,
                    caption="caption_example",
                    color="color_example",
                    size="size_example",
                    type="type_example",
                    icon_position="icon_position_example",
                    selections=[
                        OptionGroup(
                            name="name_example",
                            type="type_example",
                            selections=[
                                Selection(
                                    name="name_example",
                                    value=3.14,
                                    icon="icon_example",
                                )
                            ],
                        )
                    ],
                ),
            )
        ],
        children=[
            MetaChildren(
                child_name="child_name_example",
                child_description="child_description_example",
                child_uuid="child_uuid_example",
            )
        ],
        parent_uuid="parent_uuid_example",
    )
    try:
        # Create Meta
        api_response = api_instance.create_meta(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MetaApi->create_meta: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service': "service_example",
        'type_str': "type_str_example",
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
    body = MetaCreate(
        basic=BasicMetaCreate(
            name="name_example",
            slug=True,
        ),
        detailed=DetailedMetaCreate(
            summary="summary_example",
            description="description_example",
        ),
        custom=MetaCustom(
            name="name_example",
            description="description_example",
            _list=[
                CustomList(
                    name="name_example",
                    description="description_example",
                )
            ],
        ),
        fields=[
            Field(
                uuid="uuid_example",
                type=1,
                placeholder="placeholder_example",
                validations=Validations(
                    value=[
                        "value_example"
                    ],
                ),
                hint="hint_example",
                icon="icon_example",
                label="label_example",
                options=Options(
                    required=True,
                    label="label_example",
                    inset_label="inset_label_example",
                    placeholder="placeholder_example",
                    hint="hint_example",
                    icon="icon_example",
                    max_length=3.14,
                    counter=True,
                    caption="caption_example",
                    color="color_example",
                    size="size_example",
                    type="type_example",
                    icon_position="icon_position_example",
                    selections=[
                        OptionGroup(
                            name="name_example",
                            type="type_example",
                            selections=[
                                Selection(
                                    name="name_example",
                                    value=3.14,
                                    icon="icon_example",
                                )
                            ],
                        )
                    ],
                ),
            )
        ],
        children=[
            MetaChildren(
                child_name="child_name_example",
                child_description="child_description_example",
                child_uuid="child_uuid_example",
            )
        ],
        parent_uuid="parent_uuid_example",
    )
    try:
        # Create Meta
        api_response = api_instance.create_meta(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MetaApi->create_meta: %s\n" % e)
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
[**MetaCreate**](MetaCreate.md) |  | 


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
type_str | TypeStrSchema | | 
entity_uuid | EntityUuidSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### TypeStrSchema

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
Type | Description  | Notes
------------- | ------------- | -------------
[**MetaDynamo**](MetaDynamo.md) |  | 


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



[**MetaDynamo**](MetaDynamo.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_field**
> bool, date, datetime, dict, float, int, list, str, none_type delete_field(field_uuid)

Delete Field

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import meta_api
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
    api_instance = meta_api.MetaApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'field_uuid': "field_uuid_example",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # Delete Field
        api_response = api_instance.delete_field(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MetaApi->delete_field: %s\n" % e)

    # example passing only optional values
    path_params = {
        'field_uuid': "field_uuid_example",
    }
    query_params = {
        'soft_delete': True,
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
        # Delete Field
        api_response = api_instance.delete_field(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MetaApi->delete_field: %s\n" % e)
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
soft_delete | SoftDeleteSchema | | optional


#### SoftDeleteSchema

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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
field_uuid | FieldUuidSchema | | 

#### FieldUuidSchema

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

# **delete_meta**
> bool, date, datetime, dict, float, int, list, str, none_type delete_meta(servicetype_strentity_uuid)

Delete Meta

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import meta_api
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
    api_instance = meta_api.MetaApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'type_str': "type_str_example",
        'entity_uuid': "entity_uuid_example",
    }
    header_params = {
    }
    try:
        # Delete Meta
        api_response = api_instance.delete_meta(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MetaApi->delete_meta: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service': "service_example",
        'type_str': "type_str_example",
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
        # Delete Meta
        api_response = api_instance.delete_meta(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MetaApi->delete_meta: %s\n" % e)
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
service | ServiceSchema | | 
type_str | TypeStrSchema | | 
entity_uuid | EntityUuidSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### TypeStrSchema

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

# **delete_meta_from_uuid**
> bool, date, datetime, dict, float, int, list, str, none_type delete_meta_from_uuid(meta_uuid)

Delete Meta From Uuid

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import meta_api
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
    api_instance = meta_api.MetaApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'meta_uuid': "meta_uuid_example",
    }
    header_params = {
    }
    try:
        # Delete Meta From Uuid
        api_response = api_instance.delete_meta_from_uuid(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MetaApi->delete_meta_from_uuid: %s\n" % e)

    # example passing only optional values
    path_params = {
        'meta_uuid': "meta_uuid_example",
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
        # Delete Meta From Uuid
        api_response = api_instance.delete_meta_from_uuid(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MetaApi->delete_meta_from_uuid: %s\n" % e)
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
meta_uuid | MetaUuidSchema | | 

#### MetaUuidSchema

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

# **get_field**
> FieldDynamo get_field(field_uuid)

Get Field

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import meta_api
from ehelply_python_experimental_sdk.model.field_dynamo import FieldDynamo
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
    api_instance = meta_api.MetaApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'field_uuid': "field_uuid_example",
    }
    header_params = {
    }
    try:
        # Get Field
        api_response = api_instance.get_field(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MetaApi->get_field: %s\n" % e)

    # example passing only optional values
    path_params = {
        'field_uuid': "field_uuid_example",
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
        # Get Field
        api_response = api_instance.get_field(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MetaApi->get_field: %s\n" % e)
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
field_uuid | FieldUuidSchema | | 

#### FieldUuidSchema

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
[**FieldDynamo**](FieldDynamo.md) |  | 


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



[**FieldDynamo**](FieldDynamo.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meta**
> MetaDynamo get_meta(servicetype_strentity_uuid)

Get Meta

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import meta_api
from ehelply_python_experimental_sdk.model.meta_dynamo import MetaDynamo
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
    api_instance = meta_api.MetaApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'type_str': "type_str_example",
        'entity_uuid': "entity_uuid_example",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # Get Meta
        api_response = api_instance.get_meta(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MetaApi->get_meta: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service': "service_example",
        'type_str': "type_str_example",
        'entity_uuid': "entity_uuid_example",
    }
    query_params = {
        'detailed': False,
        'custom': False,
        'dates': False,
        'history': 0,
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
        # Get Meta
        api_response = api_instance.get_meta(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MetaApi->get_meta: %s\n" % e)
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
detailed | DetailedSchema | | optional
custom | CustomSchema | | optional
dates | DatesSchema | | optional
history | HistorySchema | | optional


#### DetailedSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

#### CustomSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

#### DatesSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

#### HistorySchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 0

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
type_str | TypeStrSchema | | 
entity_uuid | EntityUuidSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### TypeStrSchema

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
Type | Description  | Notes
------------- | ------------- | -------------
[**MetaDynamo**](MetaDynamo.md) |  | 


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



[**MetaDynamo**](MetaDynamo.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meta_from_uuid**
> MetaDynamo get_meta_from_uuid(meta_uuid)

Get Meta From Uuid

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import meta_api
from ehelply_python_experimental_sdk.model.meta_dynamo import MetaDynamo
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
    api_instance = meta_api.MetaApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'meta_uuid': "meta_uuid_example",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # Get Meta From Uuid
        api_response = api_instance.get_meta_from_uuid(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MetaApi->get_meta_from_uuid: %s\n" % e)

    # example passing only optional values
    path_params = {
        'meta_uuid': "meta_uuid_example",
    }
    query_params = {
        'detailed': False,
        'custom': False,
        'dates': False,
        'history': 0,
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
        # Get Meta From Uuid
        api_response = api_instance.get_meta_from_uuid(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MetaApi->get_meta_from_uuid: %s\n" % e)
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
detailed | DetailedSchema | | optional
custom | CustomSchema | | optional
dates | DatesSchema | | optional
history | HistorySchema | | optional


#### DetailedSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

#### CustomSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

#### DatesSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

#### HistorySchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 0

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
meta_uuid | MetaUuidSchema | | 

#### MetaUuidSchema

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
[**MetaDynamo**](MetaDynamo.md) |  | 


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



[**MetaDynamo**](MetaDynamo.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **make_slug**
> bool, date, datetime, dict, float, int, list, str, none_type make_slug(meta_slugger)

Make Slug

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import meta_api
from ehelply_python_experimental_sdk.model.meta_slugger import MetaSlugger
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
    api_instance = meta_api.MetaApi(api_client)

    # example passing only required values which don't have defaults set
    body = MetaSlugger(
        name="name_example",
    )
    try:
        # Make Slug
        api_response = api_instance.make_slug(
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MetaApi->make_slug: %s\n" % e)
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
[**MetaSlugger**](MetaSlugger.md) |  | 


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

# **touch_meta**
> MetaDynamo touch_meta(servicetype_strentity_uuid)

Touch Meta

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import meta_api
from ehelply_python_experimental_sdk.model.meta_dynamo import MetaDynamo
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
    api_instance = meta_api.MetaApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'type_str': "type_str_example",
        'entity_uuid': "entity_uuid_example",
    }
    header_params = {
    }
    try:
        # Touch Meta
        api_response = api_instance.touch_meta(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MetaApi->touch_meta: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service': "service_example",
        'type_str': "type_str_example",
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
        # Touch Meta
        api_response = api_instance.touch_meta(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MetaApi->touch_meta: %s\n" % e)
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
service | ServiceSchema | | 
type_str | TypeStrSchema | | 
entity_uuid | EntityUuidSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### TypeStrSchema

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
Type | Description  | Notes
------------- | ------------- | -------------
[**MetaDynamo**](MetaDynamo.md) |  | 


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



[**MetaDynamo**](MetaDynamo.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_field**
> bool, date, datetime, dict, float, int, list, str, none_type update_field(field_uuidfield)

Update Field

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import meta_api
from ehelply_python_experimental_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_experimental_sdk.model.field import Field
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_experimental_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_experimental_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meta_api.MetaApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'field_uuid': "field_uuid_example",
    }
    header_params = {
    }
    body = Field(
        uuid="uuid_example",
        type=1,
        placeholder="placeholder_example",
        validations=Validations(
            value=[
                "value_example"
            ],
        ),
        hint="hint_example",
        icon="icon_example",
        label="label_example",
        options=Options(
            required=True,
            label="label_example",
            inset_label="inset_label_example",
            placeholder="placeholder_example",
            hint="hint_example",
            icon="icon_example",
            max_length=3.14,
            counter=True,
            caption="caption_example",
            color="color_example",
            size="size_example",
            type="type_example",
            icon_position="icon_position_example",
            selections=[
                OptionGroup(
                    name="name_example",
                    type="type_example",
                    selections=[
                        Selection(
                            name="name_example",
                            value=3.14,
                            icon="icon_example",
                        )
                    ],
                )
            ],
        ),
    )
    try:
        # Update Field
        api_response = api_instance.update_field(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MetaApi->update_field: %s\n" % e)

    # example passing only optional values
    path_params = {
        'field_uuid': "field_uuid_example",
    }
    header_params = {
        'x-access-token': "x-access-token_example",
        'x-secret-token': "x-secret-token_example",
        'authorization': "authorization_example",
        'ehelply-active-participant': "ehelply-active-participant_example",
        'ehelply-project': "ehelply-project_example",
        'ehelply-data': "ehelply-data_example",
    }
    body = Field(
        uuid="uuid_example",
        type=1,
        placeholder="placeholder_example",
        validations=Validations(
            value=[
                "value_example"
            ],
        ),
        hint="hint_example",
        icon="icon_example",
        label="label_example",
        options=Options(
            required=True,
            label="label_example",
            inset_label="inset_label_example",
            placeholder="placeholder_example",
            hint="hint_example",
            icon="icon_example",
            max_length=3.14,
            counter=True,
            caption="caption_example",
            color="color_example",
            size="size_example",
            type="type_example",
            icon_position="icon_position_example",
            selections=[
                OptionGroup(
                    name="name_example",
                    type="type_example",
                    selections=[
                        Selection(
                            name="name_example",
                            value=3.14,
                            icon="icon_example",
                        )
                    ],
                )
            ],
        ),
    )
    try:
        # Update Field
        api_response = api_instance.update_field(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MetaApi->update_field: %s\n" % e)
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
[**Field**](Field.md) |  | 


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
field_uuid | FieldUuidSchema | | 

#### FieldUuidSchema

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

# **update_meta**
> MetaDynamo update_meta(servicetype_strentity_uuidmeta_create)

Update Meta

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import meta_api
from ehelply_python_experimental_sdk.model.meta_create import MetaCreate
from ehelply_python_experimental_sdk.model.meta_dynamo import MetaDynamo
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
    api_instance = meta_api.MetaApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'type_str': "type_str_example",
        'entity_uuid': "entity_uuid_example",
    }
    header_params = {
    }
    body = MetaCreate(
        basic=BasicMetaCreate(
            name="name_example",
            slug=True,
        ),
        detailed=DetailedMetaCreate(
            summary="summary_example",
            description="description_example",
        ),
        custom=MetaCustom(
            name="name_example",
            description="description_example",
            _list=[
                CustomList(
                    name="name_example",
                    description="description_example",
                )
            ],
        ),
        fields=[
            Field(
                uuid="uuid_example",
                type=1,
                placeholder="placeholder_example",
                validations=Validations(
                    value=[
                        "value_example"
                    ],
                ),
                hint="hint_example",
                icon="icon_example",
                label="label_example",
                options=Options(
                    required=True,
                    label="label_example",
                    inset_label="inset_label_example",
                    placeholder="placeholder_example",
                    hint="hint_example",
                    icon="icon_example",
                    max_length=3.14,
                    counter=True,
                    caption="caption_example",
                    color="color_example",
                    size="size_example",
                    type="type_example",
                    icon_position="icon_position_example",
                    selections=[
                        OptionGroup(
                            name="name_example",
                            type="type_example",
                            selections=[
                                Selection(
                                    name="name_example",
                                    value=3.14,
                                    icon="icon_example",
                                )
                            ],
                        )
                    ],
                ),
            )
        ],
        children=[
            MetaChildren(
                child_name="child_name_example",
                child_description="child_description_example",
                child_uuid="child_uuid_example",
            )
        ],
        parent_uuid="parent_uuid_example",
    )
    try:
        # Update Meta
        api_response = api_instance.update_meta(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MetaApi->update_meta: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service': "service_example",
        'type_str': "type_str_example",
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
    body = MetaCreate(
        basic=BasicMetaCreate(
            name="name_example",
            slug=True,
        ),
        detailed=DetailedMetaCreate(
            summary="summary_example",
            description="description_example",
        ),
        custom=MetaCustom(
            name="name_example",
            description="description_example",
            _list=[
                CustomList(
                    name="name_example",
                    description="description_example",
                )
            ],
        ),
        fields=[
            Field(
                uuid="uuid_example",
                type=1,
                placeholder="placeholder_example",
                validations=Validations(
                    value=[
                        "value_example"
                    ],
                ),
                hint="hint_example",
                icon="icon_example",
                label="label_example",
                options=Options(
                    required=True,
                    label="label_example",
                    inset_label="inset_label_example",
                    placeholder="placeholder_example",
                    hint="hint_example",
                    icon="icon_example",
                    max_length=3.14,
                    counter=True,
                    caption="caption_example",
                    color="color_example",
                    size="size_example",
                    type="type_example",
                    icon_position="icon_position_example",
                    selections=[
                        OptionGroup(
                            name="name_example",
                            type="type_example",
                            selections=[
                                Selection(
                                    name="name_example",
                                    value=3.14,
                                    icon="icon_example",
                                )
                            ],
                        )
                    ],
                ),
            )
        ],
        children=[
            MetaChildren(
                child_name="child_name_example",
                child_description="child_description_example",
                child_uuid="child_uuid_example",
            )
        ],
        parent_uuid="parent_uuid_example",
    )
    try:
        # Update Meta
        api_response = api_instance.update_meta(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MetaApi->update_meta: %s\n" % e)
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
[**MetaCreate**](MetaCreate.md) |  | 


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
type_str | TypeStrSchema | | 
entity_uuid | EntityUuidSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### TypeStrSchema

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
Type | Description  | Notes
------------- | ------------- | -------------
[**MetaDynamo**](MetaDynamo.md) |  | 


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



[**MetaDynamo**](MetaDynamo.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_meta_from_uuid**
> MetaDynamo update_meta_from_uuid(meta_uuidmeta_create)

Update Meta From Uuid

### Example

```python
import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api import meta_api
from ehelply_python_experimental_sdk.model.meta_create import MetaCreate
from ehelply_python_experimental_sdk.model.meta_dynamo import MetaDynamo
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
    api_instance = meta_api.MetaApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'meta_uuid': "meta_uuid_example",
    }
    header_params = {
    }
    body = MetaCreate(
        basic=BasicMetaCreate(
            name="name_example",
            slug=True,
        ),
        detailed=DetailedMetaCreate(
            summary="summary_example",
            description="description_example",
        ),
        custom=MetaCustom(
            name="name_example",
            description="description_example",
            _list=[
                CustomList(
                    name="name_example",
                    description="description_example",
                )
            ],
        ),
        fields=[
            Field(
                uuid="uuid_example",
                type=1,
                placeholder="placeholder_example",
                validations=Validations(
                    value=[
                        "value_example"
                    ],
                ),
                hint="hint_example",
                icon="icon_example",
                label="label_example",
                options=Options(
                    required=True,
                    label="label_example",
                    inset_label="inset_label_example",
                    placeholder="placeholder_example",
                    hint="hint_example",
                    icon="icon_example",
                    max_length=3.14,
                    counter=True,
                    caption="caption_example",
                    color="color_example",
                    size="size_example",
                    type="type_example",
                    icon_position="icon_position_example",
                    selections=[
                        OptionGroup(
                            name="name_example",
                            type="type_example",
                            selections=[
                                Selection(
                                    name="name_example",
                                    value=3.14,
                                    icon="icon_example",
                                )
                            ],
                        )
                    ],
                ),
            )
        ],
        children=[
            MetaChildren(
                child_name="child_name_example",
                child_description="child_description_example",
                child_uuid="child_uuid_example",
            )
        ],
        parent_uuid="parent_uuid_example",
    )
    try:
        # Update Meta From Uuid
        api_response = api_instance.update_meta_from_uuid(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MetaApi->update_meta_from_uuid: %s\n" % e)

    # example passing only optional values
    path_params = {
        'meta_uuid': "meta_uuid_example",
    }
    header_params = {
        'x-access-token': "x-access-token_example",
        'x-secret-token': "x-secret-token_example",
        'authorization': "authorization_example",
        'ehelply-active-participant': "ehelply-active-participant_example",
        'ehelply-project': "ehelply-project_example",
        'ehelply-data': "ehelply-data_example",
    }
    body = MetaCreate(
        basic=BasicMetaCreate(
            name="name_example",
            slug=True,
        ),
        detailed=DetailedMetaCreate(
            summary="summary_example",
            description="description_example",
        ),
        custom=MetaCustom(
            name="name_example",
            description="description_example",
            _list=[
                CustomList(
                    name="name_example",
                    description="description_example",
                )
            ],
        ),
        fields=[
            Field(
                uuid="uuid_example",
                type=1,
                placeholder="placeholder_example",
                validations=Validations(
                    value=[
                        "value_example"
                    ],
                ),
                hint="hint_example",
                icon="icon_example",
                label="label_example",
                options=Options(
                    required=True,
                    label="label_example",
                    inset_label="inset_label_example",
                    placeholder="placeholder_example",
                    hint="hint_example",
                    icon="icon_example",
                    max_length=3.14,
                    counter=True,
                    caption="caption_example",
                    color="color_example",
                    size="size_example",
                    type="type_example",
                    icon_position="icon_position_example",
                    selections=[
                        OptionGroup(
                            name="name_example",
                            type="type_example",
                            selections=[
                                Selection(
                                    name="name_example",
                                    value=3.14,
                                    icon="icon_example",
                                )
                            ],
                        )
                    ],
                ),
            )
        ],
        children=[
            MetaChildren(
                child_name="child_name_example",
                child_description="child_description_example",
                child_uuid="child_uuid_example",
            )
        ],
        parent_uuid="parent_uuid_example",
    )
    try:
        # Update Meta From Uuid
        api_response = api_instance.update_meta_from_uuid(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_experimental_sdk.ApiException as e:
        print("Exception when calling MetaApi->update_meta_from_uuid: %s\n" % e)
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
[**MetaCreate**](MetaCreate.md) |  | 


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
meta_uuid | MetaUuidSchema | | 

#### MetaUuidSchema

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
[**MetaDynamo**](MetaDynamo.md) |  | 


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



[**MetaDynamo**](MetaDynamo.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

