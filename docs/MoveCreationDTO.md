# MoveCreationDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** |  | [optional] 
**rdf_type** | **str** | Event type URI | [optional] 
**start** | **str** |  | [optional] 
**end** | **str** |  | [optional] 
**is_instant** | **bool** | Indicate if the event is instant | 
**description** | **str** |  | [optional] 
**targets** | **list[str]** | URI(s) of items concerned by this event | 
**relations** | [**list[RDFObjectRelationDTO]**](RDFObjectRelationDTO.md) |  | [optional] 
**location** | [**LocationObservationDTO**](LocationObservationDTO.md) |  | [optional] 
**_from** | **str** | DEPRECATED: use &#39;location&#39; instead | [optional] 
**to** | **str** | DEPRECATED: use &#39;location&#39; instead | [optional] 
**targets_positions** | [**list[TargetPositionCreationDTO]**](TargetPositionCreationDTO.md) | DEPRECATED: use &#39;location&#39; instead | [optional] 
**publisher** | [**UserGetDTO**](UserGetDTO.md) |  | [optional] 
**publication_date** | **datetime** |  | [optional] 
**last_updated_date** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


