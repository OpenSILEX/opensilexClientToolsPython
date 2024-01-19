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
**routes** | [**list[RouteDTO]**](RouteDTO.md) | List of configured routes | 
**theme_module** | **str** | Theme module identifier | [optional] 
**theme_name** | **str** | Theme module name | [optional] 
**open_id_authentication_uri** | **str** | OpenID Authorization URI | [optional] 
**open_id_connection_title** | **str** |  | [optional] 
**saml_proxy_login_uri** | **str** |  | [optional] 
**saml_connection_title** | **str** |  | [optional] 
**activate_reset_password** | **bool** |  | [optional] 
**geocoding_service** | **str** | Geocoding service | [optional] 
**menu_exclusions** | **list[str]** | Menu exclusions | [optional] 
**version_label** | **str** | Version label to use in the header | [optional] 
**application_name** | **str** | Name of the application to display | [optional] 
**connect_as_guest** | **bool** | Ability to be logged as guest | [optional] 
**dashboard** | [**DashboardConfigDTO**](DashboardConfigDTO.md) |  | [optional] 
**gdpr_file_is_configured** | **bool** | GDPR PDF is configured | [optional] 
**matomo** | [**MatomoConfigDTO**](MatomoConfigDTO.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


