# opensilexClientToolsPython.SecurityApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group**](SecurityApi.md#create_group) | **POST** /security/groups | Add a group
[**create_profile**](SecurityApi.md#create_profile) | **POST** /security/profiles | Add a profile
[**create_user**](SecurityApi.md#create_user) | **POST** /security/users | Add an user
[**delete_group**](SecurityApi.md#delete_group) | **DELETE** /security/groups/{uri} | Delete a group
[**delete_profile**](SecurityApi.md#delete_profile) | **DELETE** /security/profiles/{uri} | Delete a profile
[**delete_user**](SecurityApi.md#delete_user) | **DELETE** /security/users/{uri} | Delete an user
[**get_all_profiles**](SecurityApi.md#get_all_profiles) | **GET** /security/profiles/all | Get all profiles
[**get_group**](SecurityApi.md#get_group) | **GET** /security/groups/{uri} | Get a group
[**get_groups_by_uri**](SecurityApi.md#get_groups_by_uri) | **GET** /security/groups/by_uris | Get groups by their URIs
[**get_profile**](SecurityApi.md#get_profile) | **GET** /security/profiles/{uri} | Get a profile
[**get_user**](SecurityApi.md#get_user) | **GET** /security/users/{uri} | Get an user
[**get_user_groups**](SecurityApi.md#get_user_groups) | **GET** /security/users/{uri}/groups | Get groups of an user
[**get_users_by_uri**](SecurityApi.md#get_users_by_uri) | **GET** /security/users/by_uris | Get users by their URIs
[**search_groups**](SecurityApi.md#search_groups) | **GET** /security/groups | Search groups
[**search_profiles**](SecurityApi.md#search_profiles) | **GET** /security/profiles | Search profiles
[**search_users**](SecurityApi.md#search_users) | **GET** /security/users | Search users
[**update_group**](SecurityApi.md#update_group) | **PUT** /security/groups | Update a group
[**update_profile**](SecurityApi.md#update_profile) | **PUT** /security/profiles | Update a profile
[**update_user**](SecurityApi.md#update_user) | **PUT** /security/users | Update an user


# **create_group**
> create_group(authorization, body=body, accept_language=accept_language)

Add a group



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
body = opensilexClientToolsPython.GroupCreationDTO() # GroupCreationDTO | Group description (optional)


try:
    # Add a group
    api_instance.create_group(body=body, )
except ApiException as e:
    print("Exception when calling SecurityApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupCreationDTO**](GroupCreationDTO.md)| Group description | [optional] 


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_profile**
> create_profile(authorization, body=body, accept_language=accept_language)

Add a profile



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
body = opensilexClientToolsPython.ProfileCreationDTO() # ProfileCreationDTO | Profile description (optional)


try:
    # Add a profile
    api_instance.create_profile(body=body, )
except ApiException as e:
    print("Exception when calling SecurityApi->create_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProfileCreationDTO**](ProfileCreationDTO.md)| Profile description | [optional] 


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> create_user(authorization, body=body, accept_language=accept_language)

Add an user



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
body = opensilexClientToolsPython.UserCreationDTO() # UserCreationDTO | User description (optional)


try:
    # Add an user
    api_instance.create_user(body=body, )
except ApiException as e:
    print("Exception when calling SecurityApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserCreationDTO**](UserCreationDTO.md)| User description | [optional] 


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(uri, authorization, accept_language=accept_language)

Delete a group



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
uri = '\"http://example.com/\"' # str | Group URI


try:
    # Delete a group
    api_instance.delete_group(uri, )
except ApiException as e:
    print("Exception when calling SecurityApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Group URI | 


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_profile**
> delete_profile(uri, authorization, accept_language=accept_language)

Delete a profile



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
uri = '\"http://example.com/\"' # str | Profile URI


try:
    # Delete a profile
    api_instance.delete_profile(uri, )
except ApiException as e:
    print("Exception when calling SecurityApi->delete_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Profile URI | 


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(uri, authorization, accept_language=accept_language)

Delete an user



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
uri = '\"http://example.com/\"' # str | User URI


try:
    # Delete an user
    api_instance.delete_user(uri, )
except ApiException as e:
    print("Exception when calling SecurityApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| User URI | 


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_profiles**
> list[ProfileGetDTO] get_all_profiles(authorization, order_by=order_by, accept_language=accept_language)

Get all profiles



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
order_by = ['\"email=asc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)


try:
    # Get all profiles
    api_response = api_instance.get_all_profiles(order_by=order_by, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_all_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 


### Return type

[**list[ProfileGetDTO]**](ProfileGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> GroupDTO get_group(uri, authorization, accept_language=accept_language)

Get a group



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
uri = '\"dev-groups:admin_group\"' # str | Group URI


try:
    # Get a group
    api_response = api_instance.get_group(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Group URI | 


### Return type

[**GroupDTO**](GroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups_by_uri**
> list[GroupDTO] get_groups_by_uri(uris, authorization, accept_language=accept_language)

Get groups by their URIs



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
uris = ['uris_example'] # list[str] | Groups URIs


try:
    # Get groups by their URIs
    api_response = api_instance.get_groups_by_uri(uris, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_groups_by_uri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uris** | [**list[str]**](str.md)| Groups URIs | 


### Return type

[**list[GroupDTO]**](GroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile**
> ProfileGetDTO get_profile(uri, authorization, accept_language=accept_language)

Get a profile



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
uri = '\"dev-users:Admin_OpenSilex\"' # str | Profile URI


try:
    # Get a profile
    api_response = api_instance.get_profile(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Profile URI | 


### Return type

[**ProfileGetDTO**](ProfileGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserGetDTO get_user(uri, authorization, accept_language=accept_language)

Get an user



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
uri = '\"dev-users:Admin_OpenSilex\"' # str | User URI


try:
    # Get an user
    api_response = api_instance.get_user(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| User URI | 


### Return type

[**UserGetDTO**](UserGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_groups**
> list[NamedResourceDTO] get_user_groups(uri, authorization, accept_language=accept_language)

Get groups of an user



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
uri = '\"http://example.com/\"' # str | User URI


try:
    # Get groups of an user
    api_response = api_instance.get_user_groups(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_user_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| User URI | 


### Return type

[**list[NamedResourceDTO]**](NamedResourceDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_by_uri**
> list[UserGetDTO] get_users_by_uri(uris, authorization, accept_language=accept_language)

Get users by their URIs



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
uris = ['uris_example'] # list[str] | Users URIs


try:
    # Get users by their URIs
    api_response = api_instance.get_users_by_uri(uris, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_users_by_uri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uris** | [**list[str]**](str.md)| Users URIs | 


### Return type

[**list[UserGetDTO]**](UserGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_groups**
> list[GroupDTO] search_groups(authorization, name=name, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Search groups



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
name = '.*' # str | Regex pattern for filtering list by name (optional) (default to .*)
order_by = ['\"email=asc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search groups
    api_response = api_instance.search_groups(name=name, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->search_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Regex pattern for filtering list by name | [optional] [default to .*]
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[GroupDTO]**](GroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_profiles**
> list[ProfileGetDTO] search_profiles(authorization, name=name, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Search profiles



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
name = '.*' # str | Regex pattern for filtering list by name (optional) (default to .*)
order_by = ['\"email=asc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search profiles
    api_response = api_instance.search_profiles(name=name, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->search_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Regex pattern for filtering list by name | [optional] [default to .*]
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[ProfileGetDTO]**](ProfileGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users**
> list[UserGetDTO] search_users(authorization, name=name, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Search users



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
name = '.*' # str | Regex pattern for filtering list by name or email (optional) (default to .*)
order_by = ['\"email=asc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search users
    api_response = api_instance.search_users(name=name, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->search_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Regex pattern for filtering list by name or email | [optional] [default to .*]
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[UserGetDTO]**](UserGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> str update_group(authorization, body=body, accept_language=accept_language)

Update a group



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
body = opensilexClientToolsPython.GroupUpdateDTO() # GroupUpdateDTO | Group description (optional)


try:
    # Update a group
    api_response = api_instance.update_group(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->update_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupUpdateDTO**](GroupUpdateDTO.md)| Group description | [optional] 


### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile**
> str update_profile(authorization, body=body, accept_language=accept_language)

Update a profile



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
body = opensilexClientToolsPython.ProfileUpdateDTO() # ProfileUpdateDTO | Profile description (optional)


try:
    # Update a profile
    api_response = api_instance.update_profile(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->update_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProfileUpdateDTO**](ProfileUpdateDTO.md)| Profile description | [optional] 


### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> str update_user(authorization, body=body, accept_language=accept_language)

Update an user



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
body = opensilexClientToolsPython.UserUpdateDTO() # UserUpdateDTO | User description (optional)


try:
    # Update an user
    api_response = api_instance.update_user(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserUpdateDTO**](UserUpdateDTO.md)| User description | [optional] 


### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

