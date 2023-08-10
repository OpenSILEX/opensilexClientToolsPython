# opensilexClientToolsPython.GermplasmApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_germplasm**](GermplasmApi.md#create_germplasm) | **POST** /core/germplasm | Add a germplasm
[**create_germplasm_group**](GermplasmApi.md#create_germplasm_group) | **POST** /core/germplasm_group | Add a germplasm group
[**delete_germplasm**](GermplasmApi.md#delete_germplasm) | **DELETE** /core/germplasm/{uri} | Delete a germplasm
[**delete_germplasm_group**](GermplasmApi.md#delete_germplasm_group) | **DELETE** /core/germplasm_group/{uri} | Delete a germplasm group
[**export_germplasm**](GermplasmApi.md#export_germplasm) | **POST** /core/germplasm/export | export germplasm
[**get_germplasm**](GermplasmApi.md#get_germplasm) | **GET** /core/germplasm/{uri} | Get a germplasm
[**get_germplasm_attribute_values**](GermplasmApi.md#get_germplasm_attribute_values) | **GET** /core/germplasm/attributes/{attribute} | Get attribute values of all germplasm for a given attribute
[**get_germplasm_attributes**](GermplasmApi.md#get_germplasm_attributes) | **GET** /core/germplasm/attributes | Get attributes of all germplasm
[**get_germplasm_experiments**](GermplasmApi.md#get_germplasm_experiments) | **GET** /core/germplasm/{uri}/experiments | Get experiments where a germplasm has been used
[**get_germplasm_group**](GermplasmApi.md#get_germplasm_group) | **GET** /core/germplasm_group/{uri} | Get a germplasm group
[**get_germplasm_group_by_ur_is**](GermplasmApi.md#get_germplasm_group_by_ur_is) | **GET** /core/germplasm_group/by-uris | Get germplasm groups by their URIs
[**get_germplasm_group_content**](GermplasmApi.md#get_germplasm_group_content) | **GET** /core/germplasm_group/{uri}/germplasm | Get a germplasm group&#39;s germplasm, paginated
[**get_germplasm_group_with_germplasms**](GermplasmApi.md#get_germplasm_group_with_germplasms) | **GET** /core/germplasm_group/with-germplasm/{uri} | Get a germplasm group with nested germplasm details
[**get_germplasms_by_uri**](GermplasmApi.md#get_germplasms_by_uri) | **POST** /core/germplasm/by_uris | Get a list of germplasms by their URIs
[**search_germplasm**](GermplasmApi.md#search_germplasm) | **GET** /core/germplasm | Search germplasm
[**search_germplasm_groups**](GermplasmApi.md#search_germplasm_groups) | **POST** /core/germplasm_group/search | Search germplasm groups
[**update_germplasm**](GermplasmApi.md#update_germplasm) | **PUT** /core/germplasm | Update a germplasm
[**update_germplasm_group**](GermplasmApi.md#update_germplasm_group) | **PUT** /core/germplasm_group | Update a germplasm group


# **create_germplasm**
> str create_germplasm(authorization, body=body, check_only=check_only, accept_language=accept_language)

Add a germplasm



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
api_instance = opensilexClientToolsPython.GermplasmApi(pythonClient)
body = opensilexClientToolsPython.GermplasmCreationDTO() # GermplasmCreationDTO | Germplasm description (optional)
check_only = false # bool | Checking only (optional) (default to false)


try:
    # Add a germplasm
    api_response = api_instance.create_germplasm(body=body, check_only=check_only, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GermplasmApi->create_germplasm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GermplasmCreationDTO**](GermplasmCreationDTO.md)| Germplasm description | [optional] 
 **check_only** | **bool**| Checking only | [optional] [default to false]


### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_germplasm_group**
> str create_germplasm_group(authorization, body=body, accept_language=accept_language)

Add a germplasm group



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
api_instance = opensilexClientToolsPython.GermplasmApi(pythonClient)
body = opensilexClientToolsPython.GermplasmGroupCreationDTO() # GermplasmGroupCreationDTO | Germplasm group description (optional)


try:
    # Add a germplasm group
    api_response = api_instance.create_germplasm_group(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GermplasmApi->create_germplasm_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GermplasmGroupCreationDTO**](GermplasmGroupCreationDTO.md)| Germplasm group description | [optional] 


### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_germplasm**
> delete_germplasm(uri, authorization, accept_language=accept_language)

Delete a germplasm



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
api_instance = opensilexClientToolsPython.GermplasmApi(pythonClient)
uri = '\"http://example.com/\"' # str | Germplasm URI


try:
    # Delete a germplasm
    api_instance.delete_germplasm(uri, )
except ApiException as e:
    print("Exception when calling GermplasmApi->delete_germplasm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Germplasm URI | 


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_germplasm_group**
> ObjectUriResponse delete_germplasm_group(uri, authorization, accept_language=accept_language)

Delete a germplasm group



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
api_instance = opensilexClientToolsPython.GermplasmApi(pythonClient)
uri = 'uri_example' # str | Germplasm group URI


try:
    # Delete a germplasm group
    api_response = api_instance.delete_germplasm_group(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GermplasmApi->delete_germplasm_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Germplasm group URI | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_germplasm**
> export_germplasm(authorization, body=body, accept_language=accept_language)

export germplasm



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
api_instance = opensilexClientToolsPython.GermplasmApi(pythonClient)
body = opensilexClientToolsPython.GermplasmSearchFilter() # GermplasmSearchFilter | CSV export configuration (optional)


try:
    # export germplasm
    api_instance.export_germplasm(body=body, )
except ApiException as e:
    print("Exception when calling GermplasmApi->export_germplasm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GermplasmSearchFilter**](GermplasmSearchFilter.md)| CSV export configuration | [optional] 


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_germplasm**
> GermplasmGetSingleDTO get_germplasm(uri, authorization, accept_language=accept_language)

Get a germplasm



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
api_instance = opensilexClientToolsPython.GermplasmApi(pythonClient)
uri = '\"http://www.phenome-fppn.fr/id/species/zeamays\"' # str | germplasm URI


try:
    # Get a germplasm
    api_response = api_instance.get_germplasm(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GermplasmApi->get_germplasm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| germplasm URI | 


### Return type

[**GermplasmGetSingleDTO**](GermplasmGetSingleDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_germplasm_attribute_values**
> list[str] get_germplasm_attribute_values(attribute, authorization, attribute_value=attribute_value, page=page, page_size=page_size, accept_language=accept_language)

Get attribute values of all germplasm for a given attribute



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
api_instance = opensilexClientToolsPython.GermplasmApi(pythonClient)
attribute = 'attribute_example' # str | 
attribute_value = '\".*\"' # str | Regex pattern for filtering attribute value (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Get attribute values of all germplasm for a given attribute
    api_response = api_instance.get_germplasm_attribute_values(attribute, attribute_value=attribute_value, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GermplasmApi->get_germplasm_attribute_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute** | **str**|  | 
 **attribute_value** | **str**| Regex pattern for filtering attribute value | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_germplasm_attributes**
> list[str] get_germplasm_attributes(authorization, accept_language=accept_language)

Get attributes of all germplasm



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
api_instance = opensilexClientToolsPython.GermplasmApi(pythonClient)


try:
    # Get attributes of all germplasm
    api_response = api_instance.get_germplasm_attributes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GermplasmApi->get_germplasm_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_germplasm_experiments**
> list[ExperimentGetListDTO] get_germplasm_experiments(uri, authorization, attribute_value=attribute_value, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Get experiments where a germplasm has been used



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
api_instance = opensilexClientToolsPython.GermplasmApi(pythonClient)
uri = '\"dev-germplasm:g01\"' # str | germplasm URI
attribute_value = '.*' # str | Regex pattern for filtering experiments by name (optional) (default to .*)
order_by = ['\"name=asc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Get experiments where a germplasm has been used
    api_response = api_instance.get_germplasm_experiments(uri, attribute_value=attribute_value, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GermplasmApi->get_germplasm_experiments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| germplasm URI | 
 **attribute_value** | **str**| Regex pattern for filtering experiments by name | [optional] [default to .*]
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[ExperimentGetListDTO]**](ExperimentGetListDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_germplasm_group**
> GermplasmGroupGetDTO get_germplasm_group(uri, authorization, accept_language=accept_language)

Get a germplasm group



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
api_instance = opensilexClientToolsPython.GermplasmApi(pythonClient)
uri = 'uri_example' # str | Germplasm group URI


try:
    # Get a germplasm group
    api_response = api_instance.get_germplasm_group(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GermplasmApi->get_germplasm_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Germplasm group URI | 


### Return type

[**GermplasmGroupGetDTO**](GermplasmGroupGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_germplasm_group_by_ur_is**
> list[GermplasmGroupGetDTO] get_germplasm_group_by_ur_is(uris, authorization, accept_language=accept_language)

Get germplasm groups by their URIs



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
api_instance = opensilexClientToolsPython.GermplasmApi(pythonClient)
uris = ['uris_example'] # list[str] | Germplasm group URIs


try:
    # Get germplasm groups by their URIs
    api_response = api_instance.get_germplasm_group_by_ur_is(uris, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GermplasmApi->get_germplasm_group_by_ur_is: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uris** | [**list[str]**](str.md)| Germplasm group URIs | 


### Return type

[**list[GermplasmGroupGetDTO]**](GermplasmGroupGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_germplasm_group_content**
> list[GermplasmGetAllDTO] get_germplasm_group_content(uri, authorization, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Get a germplasm group's germplasm, paginated



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
api_instance = opensilexClientToolsPython.GermplasmApi(pythonClient)
uri = 'uri_example' # str | Germplasm group URI
order_by = ['\"uri=asc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Get a germplasm group's germplasm, paginated
    api_response = api_instance.get_germplasm_group_content(uri, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GermplasmApi->get_germplasm_group_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Germplasm group URI | 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[GermplasmGetAllDTO]**](GermplasmGetAllDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_germplasm_group_with_germplasms**
> GermplasmGroupGetWithDetailsDTO get_germplasm_group_with_germplasms(uri, authorization, accept_language=accept_language)

Get a germplasm group with nested germplasm details



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
api_instance = opensilexClientToolsPython.GermplasmApi(pythonClient)
uri = 'uri_example' # str | Germplasm group URI


try:
    # Get a germplasm group with nested germplasm details
    api_response = api_instance.get_germplasm_group_with_germplasms(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GermplasmApi->get_germplasm_group_with_germplasms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Germplasm group URI | 


### Return type

[**GermplasmGroupGetWithDetailsDTO**](GermplasmGroupGetWithDetailsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_germplasms_by_uri**
> list[GermplasmGetAllDTO] get_germplasms_by_uri(authorization, body=body, accept_language=accept_language)

Get a list of germplasms by their URIs



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
api_instance = opensilexClientToolsPython.GermplasmApi(pythonClient)
body = [opensilexClientToolsPython.list[str]()] # list[str] | Germplasms URIs (optional)


try:
    # Get a list of germplasms by their URIs
    api_response = api_instance.get_germplasms_by_uri(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GermplasmApi->get_germplasms_by_uri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[str]**| Germplasms URIs | [optional] 


### Return type

[**list[GermplasmGetAllDTO]**](GermplasmGetAllDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_germplasm**
> list[GermplasmGetAllDTO] search_germplasm(authorization, uri=uri, rdf_type=rdf_type, name=name, code=code, production_year=production_year, species=species, variety=variety, accession=accession, group_of_germplasm=group_of_germplasm, institute=institute, experiment=experiment, metadata=metadata, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Search germplasm



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
api_instance = opensilexClientToolsPython.GermplasmApi(pythonClient)
uri = '\"http://opensilex/set/experiments/ZA17\"' # str | Regex pattern for filtering list by uri (optional)
rdf_type = '\"http://www.opensilex.org/vocabulary/oeso#Variety\"' # str | Search by type (optional)
name = '.*' # str | Regex pattern for filtering list by name and synonyms (optional) (default to .*)
code = '.*' # str | Regex pattern for filtering list by code (optional) (default to .*)
production_year = 2020 # int | Search by production year (optional)
species = '\"http://www.phenome-fppn.fr/id/species/zeamays\"' # str | Search by species (optional)
variety = 'variety_example' # str | Search by variety (optional)
accession = 'accession_example' # str | Search by accession (optional)
group_of_germplasm = 'group_of_germplasm_example' # str | Group filter (optional)
institute = '\"INRA\"' # str | Search by institute (optional)
experiment = 'experiment_example' # str | Search by experiment (optional)
metadata = '\"{ \\\"water_stress\\\" : \\\"resistant\\\",\\n\\\"yield\\\" : \\\"moderate\\\"}\"' # str | Search by metadata (optional)
order_by = ['\"uri=asc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search germplasm
    api_response = api_instance.search_germplasm(uri=uri, rdf_type=rdf_type, name=name, code=code, production_year=production_year, species=species, variety=variety, accession=accession, group_of_germplasm=group_of_germplasm, institute=institute, experiment=experiment, metadata=metadata, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GermplasmApi->search_germplasm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Regex pattern for filtering list by uri | [optional] 
 **rdf_type** | **str**| Search by type | [optional] 
 **name** | **str**| Regex pattern for filtering list by name and synonyms | [optional] [default to .*]
 **code** | **str**| Regex pattern for filtering list by code | [optional] [default to .*]
 **production_year** | **int**| Search by production year | [optional] 
 **species** | **str**| Search by species | [optional] 
 **variety** | **str**| Search by variety | [optional] 
 **accession** | **str**| Search by accession | [optional] 
 **group_of_germplasm** | **str**| Group filter | [optional] 
 **institute** | **str**| Search by institute | [optional] 
 **experiment** | **str**| Search by experiment | [optional] 
 **metadata** | **str**| Search by metadata | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[GermplasmGetAllDTO]**](GermplasmGetAllDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_germplasm_groups**
> list[GermplasmGroupGetDTO] search_germplasm_groups(authorization, name=name, germplasm=germplasm, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Search germplasm groups



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
api_instance = opensilexClientToolsPython.GermplasmApi(pythonClient)
name = 'name_example' # str | Regex pattern for filtering by name (optional)
germplasm = ['\"http://aims.fao.org/aos/agrovoc/c_1066\"'] # list[str] | Germplasm URIs (optional)
order_by = ['\"uri=asc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search germplasm groups
    api_response = api_instance.search_germplasm_groups(name=name, germplasm=germplasm, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GermplasmApi->search_germplasm_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Regex pattern for filtering by name | [optional] 
 **germplasm** | [**list[str]**](str.md)| Germplasm URIs | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[GermplasmGroupGetDTO]**](GermplasmGroupGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_germplasm**
> str update_germplasm(authorization, body=body, accept_language=accept_language)

Update a germplasm



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
api_instance = opensilexClientToolsPython.GermplasmApi(pythonClient)
body = opensilexClientToolsPython.GermplasmUpdateDTO() # GermplasmUpdateDTO | Germplasm description (optional)


try:
    # Update a germplasm
    api_response = api_instance.update_germplasm(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GermplasmApi->update_germplasm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GermplasmUpdateDTO**](GermplasmUpdateDTO.md)| Germplasm description | [optional] 


### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_germplasm_group**
> str update_germplasm_group(authorization, body=body, accept_language=accept_language)

Update a germplasm group



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
api_instance = opensilexClientToolsPython.GermplasmApi(pythonClient)
body = opensilexClientToolsPython.GermplasmGroupUpdateDTO() # GermplasmGroupUpdateDTO | Germplasm group description (optional)


try:
    # Update a germplasm group
    api_response = api_instance.update_germplasm_group(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GermplasmApi->update_germplasm_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GermplasmGroupUpdateDTO**](GermplasmGroupUpdateDTO.md)| Germplasm group description | [optional] 


### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

