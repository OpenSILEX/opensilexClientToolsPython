# opensilexClientToolsPython.SecurityApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_favorite**](SecurityApi.md#add_favorite) | **POST** /security/accounts/favorites | Add a favorite
[**add_favorite1**](SecurityApi.md#add_favorite1) | **POST** /security/users/favorites | Add a favorite
[**create_account**](SecurityApi.md#create_account) | **POST** /security/accounts | Add an account
[**create_group**](SecurityApi.md#create_group) | **POST** /security/groups | Add a group
[**create_person**](SecurityApi.md#create_person) | **POST** /security/persons | Add a person
[**create_profile**](SecurityApi.md#create_profile) | **POST** /security/profiles | Add a profile
[**create_user**](SecurityApi.md#create_user) | **POST** /security/users | Add a user
[**delete_account**](SecurityApi.md#delete_account) | **DELETE** /security/accounts/{accountURI} | Delete an account
[**delete_favorite**](SecurityApi.md#delete_favorite) | **DELETE** /security/accounts/favorites/{uriFavorite} | Delete a favorite
[**delete_favorite1**](SecurityApi.md#delete_favorite1) | **DELETE** /security/users/favorites/{uriFavorite} | Delete a favorite
[**delete_group**](SecurityApi.md#delete_group) | **DELETE** /security/groups/{uri} | Delete a group
[**delete_profile**](SecurityApi.md#delete_profile) | **DELETE** /security/profiles/{uri} | Delete a profile
[**get_account**](SecurityApi.md#get_account) | **GET** /security/accounts/{uri} | Get an account
[**get_accounts_by_uri**](SecurityApi.md#get_accounts_by_uri) | **GET** /security/accounts/by_uris | Get accounts by their URIs
[**get_all_profiles**](SecurityApi.md#get_all_profiles) | **GET** /security/profiles/all | Get all profiles
[**get_favorites**](SecurityApi.md#get_favorites) | **GET** /security/accounts/favorites | Get list of favorites for a user
[**get_favorites1**](SecurityApi.md#get_favorites1) | **GET** /security/users/favorites | Get list of favorites for a user
[**get_gdpr_file**](SecurityApi.md#get_gdpr_file) | **GET** /security/persons/GDPR | Get RGPD PDF
[**get_group**](SecurityApi.md#get_group) | **GET** /security/groups/{uri} | Get a group
[**get_groups_by_uri**](SecurityApi.md#get_groups_by_uri) | **GET** /security/groups/by_uris | Get groups by their URIs
[**get_orcid_record**](SecurityApi.md#get_orcid_record) | **GET** /security/persons/orcid_record | Get infos from an ORCID
[**get_person**](SecurityApi.md#get_person) | **GET** /security/persons/{uri} | Get a Person
[**get_persons_by_uri**](SecurityApi.md#get_persons_by_uri) | **GET** /security/persons/by_uris | Get persons by their URIs
[**get_profile**](SecurityApi.md#get_profile) | **GET** /security/profiles/{uri} | Get a profile
[**get_user**](SecurityApi.md#get_user) | **GET** /security/users/{uri} | Get a user
[**get_user_groups**](SecurityApi.md#get_user_groups) | **GET** /security/accounts/{uri}/groups | Get groups of a user
[**get_user_groups1**](SecurityApi.md#get_user_groups1) | **GET** /security/users/{uri}/groups | Get groups of a user
[**get_users_by_uri**](SecurityApi.md#get_users_by_uri) | **GET** /security/users/by_uris | Get users by their URIs
[**search_accounts**](SecurityApi.md#search_accounts) | **GET** /security/accounts | Search accounts
[**search_groups**](SecurityApi.md#search_groups) | **GET** /security/groups | Search groups
[**search_persons**](SecurityApi.md#search_persons) | **GET** /security/persons | Search persons
[**search_profiles**](SecurityApi.md#search_profiles) | **GET** /security/profiles | Search profiles
[**search_users**](SecurityApi.md#search_users) | **GET** /security/users | Search users
[**update_account**](SecurityApi.md#update_account) | **PUT** /security/accounts | Update an account
[**update_group**](SecurityApi.md#update_group) | **PUT** /security/groups | Update a group
[**update_person**](SecurityApi.md#update_person) | **PUT** /security/persons | Update a person
[**update_profile**](SecurityApi.md#update_profile) | **PUT** /security/profiles | Update a profile
[**update_user**](SecurityApi.md#update_user) | **PUT** /security/users | Update a user


# **add_favorite**
> add_favorite(authorization, body=body, accept_language=accept_language)

Add a favorite



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
body = opensilexClientToolsPython.FavoriteCreationDTO() # FavoriteCreationDTO | Favorite object URI (optional)


try:
    # Add a favorite
    api_instance.add_favorite(body=body, )
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling SecurityApi->add_favorite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FavoriteCreationDTO**](FavoriteCreationDTO.md)| Favorite object URI | [optional] 


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_favorite1**
> add_favorite1(authorization, body=body, accept_language=accept_language)

Add a favorite



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
body = opensilexClientToolsPython.FavoriteCreationDTO() # FavoriteCreationDTO | Favorite object URI (optional)


try:
    # Add a favorite
    api_instance.add_favorite1(body=body, )
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling SecurityApi->add_favorite1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FavoriteCreationDTO**](FavoriteCreationDTO.md)| Favorite object URI | [optional] 


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account**
> create_account(authorization, body=body, accept_language=accept_language)

Add an account



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
body = opensilexClientToolsPython.AccountCreationDTO() # AccountCreationDTO | Account description (optional)


try:
    # Add an account
    api_instance.create_account(body=body, )
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling SecurityApi->create_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountCreationDTO**](AccountCreationDTO.md)| Account description | [optional] 


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
body = opensilexClientToolsPython.GroupCreationDTO() # GroupCreationDTO | Group description (optional)


try:
    # Add a group
    api_instance.create_group(body=body, )
except opensilexClientToolsPython.rest.ApiException as e:
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

# **create_person**
> create_person(authorization, body=body, accept_language=accept_language)

Add a person



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
body = opensilexClientToolsPython.PersonDTO() # PersonDTO | Person description (optional)


try:
    # Add a person
    api_instance.create_person(body=body, )
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling SecurityApi->create_person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PersonDTO**](PersonDTO.md)| Person description | [optional] 


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
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
body = opensilexClientToolsPython.ProfileCreationDTO() # ProfileCreationDTO | Profile description (optional)


try:
    # Add a profile
    api_instance.create_profile(body=body, )
except opensilexClientToolsPython.rest.ApiException as e:
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

Add a user



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
body = opensilexClientToolsPython.UserCreationDTO() # UserCreationDTO | User description (optional)


try:
    # Add a user
    api_instance.create_user(body=body, )
except opensilexClientToolsPython.rest.ApiException as e:
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

# **delete_account**
> str delete_account(account_uri, authorization, accept_language=accept_language)

Delete an account



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
account_uri = 'account_uri_example' # str | Account URI


try:
    # Delete an account
    api_response = api_instance.delete_account(account_uri, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling SecurityApi->delete_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_uri** | **str**| Account URI | 


### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_favorite**
> delete_favorite(uri_favorite, authorization, accept_language=accept_language)

Delete a favorite



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
uri_favorite = '\"http://example.com/\"' # str | Favorite URI


try:
    # Delete a favorite
    api_instance.delete_favorite(uri_favorite, )
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling SecurityApi->delete_favorite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri_favorite** | **str**| Favorite URI | 


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_favorite1**
> delete_favorite1(uri_favorite, authorization, accept_language=accept_language)

Delete a favorite



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
uri_favorite = '\"http://example.com/\"' # str | Favorite URI


try:
    # Delete a favorite
    api_instance.delete_favorite1(uri_favorite, )
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling SecurityApi->delete_favorite1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri_favorite** | **str**| Favorite URI | 


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
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
uri = '\"http://example.com/\"' # str | Group URI


try:
    # Delete a group
    api_instance.delete_group(uri, )
except opensilexClientToolsPython.rest.ApiException as e:
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
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
uri = '\"http://example.com/\"' # str | Profile URI


try:
    # Delete a profile
    api_instance.delete_profile(uri, )
except opensilexClientToolsPython.rest.ApiException as e:
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

# **get_account**
> AccountGetDTO get_account(uri, authorization, accept_language=accept_language)

Get an account



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
uri = '\"http://opensilex.dev/users#jean.michel.inrae\"' # str | Account URI


try:
    # Get an account
    api_response = api_instance.get_account(uri, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling SecurityApi->get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Account URI | 


### Return type

[**AccountGetDTO**](AccountGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts_by_uri**
> list[AccountGetDTO] get_accounts_by_uri(uris, authorization, accept_language=accept_language)

Get accounts by their URIs



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
uris = ['uris_example'] # list[str] | Accounts URIs


try:
    # Get accounts by their URIs
    api_response = api_instance.get_accounts_by_uri(uris, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling SecurityApi->get_accounts_by_uri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uris** | [**list[str]**](str.md)| Accounts URIs | 


### Return type

[**list[AccountGetDTO]**](AccountGetDTO.md)

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
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
order_by = ['\"email=asc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)


try:
    # Get all profiles
    api_response = api_instance.get_all_profiles(order_by=order_by, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
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

# **get_favorites**
> list[FavoriteGetDTO] get_favorites(types, authorization, accept_language=accept_language)

Get list of favorites for a user



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
types = ['types_example'] # list[str] | Types


try:
    # Get list of favorites for a user
    api_response = api_instance.get_favorites(types, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling SecurityApi->get_favorites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types** | [**list[str]**](str.md)| Types | 


### Return type

[**list[FavoriteGetDTO]**](FavoriteGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favorites1**
> list[FavoriteGetDTO] get_favorites1(types, authorization, accept_language=accept_language)

Get list of favorites for a user



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
types = ['types_example'] # list[str] | Types


try:
    # Get list of favorites for a user
    api_response = api_instance.get_favorites1(types, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling SecurityApi->get_favorites1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types** | [**list[str]**](str.md)| Types | 


### Return type

[**list[FavoriteGetDTO]**](FavoriteGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gdpr_file**
> get_gdpr_file(language=language)

Get RGPD PDF



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
language = '\"fr\"' # str | preferred language of the file (optional)


try:
    # Get RGPD PDF
    api_instance.get_gdpr_file(language=language)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling SecurityApi->get_gdpr_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| preferred language of the file | [optional] 


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

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
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
uri = '\"dev-groups:admin_group\"' # str | Group URI


try:
    # Get a group
    api_response = api_instance.get_group(uri, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
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
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
uris = ['uris_example'] # list[str] | Groups URIs


try:
    # Get groups by their URIs
    api_response = api_instance.get_groups_by_uri(uris, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
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

# **get_orcid_record**
> OrcidRecordDTO get_orcid_record(orcid)

Get infos from an ORCID



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
orcid = 'orcid_example' # str | orcid


try:
    # Get infos from an ORCID
    api_response = api_instance.get_orcid_record(orcid)
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling SecurityApi->get_orcid_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orcid** | **str**| orcid | 


### Return type

[**OrcidRecordDTO**](OrcidRecordDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person**
> PersonDTO get_person(uri, authorization, accept_language=accept_language)

Get a Person



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
uri = '\"http://opensilex.dev/person#harold.haddock.mistea\"' # str | Person URI


try:
    # Get a Person
    api_response = api_instance.get_person(uri, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling SecurityApi->get_person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Person URI | 


### Return type

[**PersonDTO**](PersonDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_persons_by_uri**
> list[PersonDTO] get_persons_by_uri(uris, authorization, accept_language=accept_language)

Get persons by their URIs



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
uris = ['uris_example'] # list[str] | Persons URIs


try:
    # Get persons by their URIs
    api_response = api_instance.get_persons_by_uri(uris, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling SecurityApi->get_persons_by_uri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uris** | [**list[str]**](str.md)| Persons URIs | 


### Return type

[**list[PersonDTO]**](PersonDTO.md)

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
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
uri = '\"dev-users:Admin_OpenSilex\"' # str | Profile URI


try:
    # Get a profile
    api_response = api_instance.get_profile(uri, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
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

Get a user



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
uri = '\"http://opensilex.dev/users#jean.michel.inrae\"' # str | User URI


try:
    # Get a user
    api_response = api_instance.get_user(uri, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
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

Get groups of a user



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
uri = '\"http://example.com/\"' # str | User URI


try:
    # Get groups of a user
    api_response = api_instance.get_user_groups(uri, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
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

# **get_user_groups1**
> list[NamedResourceDTO] get_user_groups1(uri, authorization, accept_language=accept_language)

Get groups of a user



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
uri = '\"http://example.com/\"' # str | User URI


try:
    # Get groups of a user
    api_response = api_instance.get_user_groups1(uri, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling SecurityApi->get_user_groups1: %s\n" % e)
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
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
uris = ['uris_example'] # list[str] | Users URIs


try:
    # Get users by their URIs
    api_response = api_instance.get_users_by_uri(uris, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
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

# **search_accounts**
> list[AccountGetDTO] search_accounts(authorization, name=name, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Search accounts



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
name = '.*' # str | Regex pattern for filtering list by name or email (optional) (default to .*)
order_by = ['\"email=asc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search accounts
    api_response = api_instance.search_accounts(name=name, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling SecurityApi->search_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Regex pattern for filtering list by name or email | [optional] [default to .*]
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[AccountGetDTO]**](AccountGetDTO.md)

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
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
name = '.*' # str | Regex pattern for filtering list by name (optional) (default to .*)
order_by = ['\"email=asc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search groups
    api_response = api_instance.search_groups(name=name, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
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

# **search_persons**
> list[PersonDTO] search_persons(authorization, name=name, only_without_account=only_without_account, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Search persons



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
name = '.*' # str | Regex pattern for filtering list by name or email (optional) (default to .*)
only_without_account = false # bool | set 'true' if you want to select only persons without account (optional) (default to false)
order_by = ['\"email=asc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search persons
    api_response = api_instance.search_persons(name=name, only_without_account=only_without_account, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling SecurityApi->search_persons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Regex pattern for filtering list by name or email | [optional] [default to .*]
 **only_without_account** | **bool**| set &#39;true&#39; if you want to select only persons without account | [optional] [default to false]
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[PersonDTO]**](PersonDTO.md)

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
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
name = '.*' # str | Regex pattern for filtering list by name (optional) (default to .*)
order_by = ['\"email=asc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search profiles
    api_response = api_instance.search_profiles(name=name, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
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
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
name = '.*' # str | Regex pattern for filtering list by name or email (optional) (default to .*)
order_by = ['\"email=asc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search users
    api_response = api_instance.search_users(name=name, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
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

# **update_account**
> str update_account(authorization, body=body, accept_language=accept_language)

Update an account



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
body = opensilexClientToolsPython.AccountUpdateDTO() # AccountUpdateDTO | Account description (optional)


try:
    # Update an account
    api_response = api_instance.update_account(body=body, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling SecurityApi->update_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountUpdateDTO**](AccountUpdateDTO.md)| Account description | [optional] 


### Return type

**str**

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
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
body = opensilexClientToolsPython.GroupUpdateDTO() # GroupUpdateDTO | Group description (optional)


try:
    # Update a group
    api_response = api_instance.update_group(body=body, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
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

# **update_person**
> str update_person(authorization, body=body, accept_language=accept_language)

Update a person



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
body = opensilexClientToolsPython.PersonDTO() # PersonDTO | Person description (optional)


try:
    # Update a person
    api_response = api_instance.update_person(body=body, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling SecurityApi->update_person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PersonDTO**](PersonDTO.md)| Person description | [optional] 


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
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
body = opensilexClientToolsPython.ProfileUpdateDTO() # ProfileUpdateDTO | Profile description (optional)


try:
    # Update a profile
    api_response = api_instance.update_profile(body=body, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
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

Update a user



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.SecurityApi(pythonClient)
body = opensilexClientToolsPython.UserUpdateDTO() # UserUpdateDTO | User description (optional)


try:
    # Update a user
    api_response = api_instance.update_user(body=body, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
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

