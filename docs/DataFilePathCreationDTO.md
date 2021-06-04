# DataFilePathCreationDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** |  | [optional] 
**rdf_type** | **str** | file type | 
**_date** | **str** | date or datetime | [optional] 
**timezone** | **str** | to specify if the offset is not in the date and if the timezone is different from the default one | [optional] 
**scientific_object** | **str** | scientific objects URIs on which the data have been collected | [optional] 
**provenance** | [**DataProvenanceModel**](DataProvenanceModel.md) |  | 
**metadata** | **dict(str, object)** | key-value system to store additional information that can be used to query data | [optional] 
**relative_path** | **str** | path to the stored file | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


