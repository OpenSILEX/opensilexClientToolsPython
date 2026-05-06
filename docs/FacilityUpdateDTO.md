# FacilityUpdateDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** |  | 
**rdf_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**organizations** | **list[str]** |  | [optional] 
**address** | [**FacilityAddressDTO**](FacilityAddressDTO.md) |  | [optional] 
**description** | **str** |  | [optional] 
**locations** | [**list[LocationObservationDTO]**](LocationObservationDTO.md) |  | [optional] 
**publisher** | [**UserGetDTO**](UserGetDTO.md) |  | [optional] 
**publication_date** | **datetime** |  | [optional] 
**last_updated_date** | **datetime** |  | [optional] 
**relations** | [**list[RDFObjectRelationDTO]**](RDFObjectRelationDTO.md) |  | [optional] 
**rdf_type_name** | **str** |  | [optional] 
**sites** | **list[str]** |  | [optional] 
**variable_groups** | **list[str]** |  | [optional] 
**geometry** | [**GeoJsonObject**](GeoJsonObject.md) | Deprecated. Please use the locations property to attach geospatial info to the facility. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


