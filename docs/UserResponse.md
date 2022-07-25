# UserResponse

When retrieving a user

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**picture** | **str** |  | [optional] 
**gps_location** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**verified_legal_terms** | **bool** |  | [optional]  if omitted the server will use the default value of False
**date_created** | **datetime** |  | [optional] 
**date_updated** | **datetime** |  | [optional] 
**date_deleted** | **datetime** |  | [optional] 
**email** | [**UserEmail**](UserEmail.md) |  | [optional] 
**missing** | **[str]** |  | [optional] 
**uuid** | **str** |  | [optional] 
**participants** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** |  | [optional] 
**flags** | [**UserFlags**](UserFlags.md) |  | [optional] 
**last_login** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

