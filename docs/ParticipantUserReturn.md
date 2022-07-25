# ParticipantUserReturn

Contains all fields required when doing a Participant GET but also has user fields (name, location, ect). This is what is returned from all participant endpoints.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**user_uuid** | **str** |  | [optional] 
**participant_meta** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**gps_location** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**picture** | **str** |  | [optional] 
**last_login** | **datetime** |  | [optional] 
**verified_legal_terms** | **bool** |  | [optional] 
**date_created** | **datetime** |  | [optional] 
**date_updated** | **datetime** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

