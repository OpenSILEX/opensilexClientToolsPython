# RDFPropertyGetDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | URI of property | 
**domain** | **str** | Domain of the property : the rdf:type of any concept concerned by this property. | 
**range** | **str** | Range of the property : the rdf:type of any value(can be a literal type or a concept type) concerned by this property. | 
**parent** | **str** | Parent of the property. | [optional] 
**name** | **str** | Default property name according language | [optional] 
**comment** | **str** | Default property description according language | [optional] 
**rdf_type** | **str** | The type of property | 
**name_translations** | **dict(str, str)** | Name by languages, at least one name/language is required. Use &#39;&#39; as language if no language is specified | 
**comment_translations** | **dict(str, str)** | Description by languages, at least one description/language is required. Use &#39;&#39; as language if no language is specified | 
**publisher** | [**UserGetDTO**](UserGetDTO.md) |  | [optional] 
**publication_date** | **datetime** |  | [optional] 
**last_updated_date** | **datetime** |  | [optional] 
**domain_label** | **str** |  | [optional] 
**range_label** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


