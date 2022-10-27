# NoteDynamoHistoryResponse

A note from Dynamo DB including n amount of version history of that note

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**content** | **str** |  | 
**time** | **str** |  | 
**meta** | [**NoteMeta**](NoteMeta.md) |  | 
**history** | **[NoteDynamoResponse]** |  | [optional]  if omitted the server will use the default value of []
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

