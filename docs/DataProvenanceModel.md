# DataProvenanceModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | provenance uri | 
**prov_used** | [**list[ProvEntityModel]**](ProvEntityModel.md) | list of inputs of the process described in the provenance | [optional] 
**prov_was_associated_with** | [**list[ProvEntityModel]**](ProvEntityModel.md) | allow an activity to be linked to an agent | [optional] 
**settings** | **dict(str, object)** | a key-value system to store specific information | [optional] 
**experiments** | **list[str]** | experiments uris on which the data has been produced | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


