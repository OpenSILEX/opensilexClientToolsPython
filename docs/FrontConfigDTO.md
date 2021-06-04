# FrontConfigDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path_prefix** | **str** | Application url path prefix | 
**home_component** | **str** | Home component identifier | 
**not_found_component** | **str** | Not found component identifier | 
**header_component** | **str** | Header component identifier | 
**login_component** | **str** | Login component identifier | 
**menu_component** | **str** | Menu component identifier | 
**footer_component** | **str** | Footer component identifier | 
**menu** | [**list[MenuItemDTO]**](MenuItemDTO.md) | Application menu with routes | 
**routes** | [**list[RouteDTO]**](RouteDTO.md) | List of configured routes | 
**theme_module** | **str** | Theme module identifier | [optional] 
**theme_name** | **str** | Theme module name | [optional] 
**open_id_authentication_uri** | **str** | OpenID Authorization URI | [optional] 
**open_id_connection_title** | **str** |  | [optional] 
**activate_reset_password** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


