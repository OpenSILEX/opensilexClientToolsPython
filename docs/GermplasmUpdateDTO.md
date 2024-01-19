# GermplasmUpdateDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | Germplasm URI | 
**rdf_type** | **str** | Germplasm type | 
**name** | **str** | Germplasm name | 
**synonyms** | **list[str]** |  | [optional] 
**code** | **str** | Germplasm code (accessionNumber, varietyCode...) | [optional] 
**production_year** | **int** | production year | [optional] 
**description** | **str** | comment | [optional] 
**species** | **str** | species URI | [optional] 
**variety** | **str** | variety URI | [optional] 
**accession** | **str** | accession URI | [optional] 
**institute** | **str** | institute | [optional] 
**website** | **str** | website | [optional] 
**relations** | [**list[RDFObjectRelationDTO]**](RDFObjectRelationDTO.md) |  | [optional] 
**metadata** | **dict(str, str)** |  | [optional] 
**publisher** | [**UserGetDTO**](UserGetDTO.md) |  | [optional] 
**publication_date** | **datetime** |  | [optional] 
**last_updated_date** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


