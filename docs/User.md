# User

User object, contains all required parameters

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cognito_id** | **str** |  | [optional] 
**cognito_data** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**picture** | **str** |  | [optional] 
**gps_location** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**verified_legal_terms** | **bool** |  | [optional]  if omitted the server will use the default value of False
**date_created** | **datetime** |  | [optional] 
**date_updated** | **datetime** |  | [optional] 
**date_deleted** | **datetime** |  | [optional] 
**uuid** | **str** |  | 
**last_login** | **datetime** |  | [optional] 
**first_login** | **bool** |  | [optional]  if omitted the server will use the default value of True
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

