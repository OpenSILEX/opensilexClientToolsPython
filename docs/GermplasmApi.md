# opensilexClientToolsPython.GermplasmApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_germplasm**](GermplasmApi.md#create_germplasm) | **POST** /core/germplasm | Add a germplasm
[**delete_germplasm**](GermplasmApi.md#delete_germplasm) | **DELETE** /core/germplasm/{uri} | Delete a germplasm
[**export_germplasm**](GermplasmApi.md#export_germplasm) | **GET** /core/germplasm/export | export germplasm
[**export_germplasm_by_ur_is**](GermplasmApi.md#export_germplasm_by_ur_is) | **POST** /core/germplasm/export_by_uris | export germplasm by list of uris
[**get_germplasm**](GermplasmApi.md#get_germplasm) | **GET** /core/germplasm/{uri} | Get a germplasm
[**get_germplasm_experiments**](GermplasmApi.md#get_germplasm_experiments) | **GET** /core/germplasm/{uri}/experiments | Get experiments where a germplasm has been used
[**get_germplasms_by_uri**](GermplasmApi.md#get_germplasms_by_uri) | **GET** /core/germplasm/by_uris | Get a list of germplasms by their URIs
[**search_germplasm**](GermplasmApi.md#search_germplasm) | **GET** /core/germplasm | Search germplasm
[**update_germplasm**](GermplasmApi.md#update_germplasm) | **PUT** /core/germplasm | Update a germplasm


# **create_germplasm**
> ObjectUriResponse create_germplasm(authorization, body=body, check_only=check_only, accept_language=accept_language)

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

[**ObjectUriResponse**](ObjectUriResponse.md)

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
uri = 'http://example.com/' # str | Germplasm URI


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

# **export_germplasm**
> export_germplasm(authorization, uri=uri, rdf_type=rdf_type, name=name, code=code, production_year=production_year, species=species, variety=variety, accession=accession, institute=institute, experiment=experiment, metadata=metadata, order_by=order_by, accept_language=accept_language)

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
uri = 'http://opensilex/set/experiments/ZA17' # str | Regex pattern for filtering list by uri (optional)
rdf_type = 'http://www.opensilex.org/vocabulary/oeso#Variety' # str | Search by type (optional)
name = '.*' # str | Regex pattern for filtering list by name and synonyms (optional) (default to .*)
code = '.*' # str | Regex pattern for filtering list by code (optional) (default to .*)
production_year = 2020 # int | Search by productionYear (optional)
species = 'http://www.phenome-fppn.fr/id/species/zeamays' # str | Search by species (optional)
variety = 'variety_example' # str | Search by variety (optional)
accession = 'accession_example' # str | Search by accession (optional)
institute = 'INRA' # str | Search by institute (optional)
experiment = 'experiment_example' # str | Search by experiment (optional)
metadata = '{ \"water_stress\" : \"resistant\", \"yield\" : \"moderate\"}' # str | Search by metadata (optional)
order_by = ['name=asc'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)


try:
    # export germplasm
    api_instance.export_germplasm(uri=uri, rdf_type=rdf_type, name=name, code=code, production_year=production_year, species=species, variety=variety, accession=accession, institute=institute, experiment=experiment, metadata=metadata, order_by=order_by, )
except ApiException as e:
    print("Exception when calling GermplasmApi->export_germplasm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Regex pattern for filtering list by uri | [optional] 
 **rdf_type** | **str**| Search by type | [optional] 
 **name** | **str**| Regex pattern for filtering list by name and synonyms | [optional] [default to .*]
 **code** | **str**| Regex pattern for filtering list by code | [optional] [default to .*]
 **production_year** | **int**| Search by productionYear | [optional] 
 **species** | **str**| Search by species | [optional] 
 **variety** | **str**| Search by variety | [optional] 
 **accession** | **str**| Search by accession | [optional] 
 **institute** | **str**| Search by institute | [optional] 
 **experiment** | **str**| Search by experiment | [optional] 
 **metadata** | **str**| Search by metadata | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_germplasm_by_ur_is**
> export_germplasm_by_ur_is(authorization, body=body, accept_language=accept_language)

export germplasm by list of uris



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
body = opensilexClientToolsPython.URIsListPostDTO() # URIsListPostDTO | List of germplasm URI (optional)


try:
    # export germplasm by list of uris
    api_instance.export_germplasm_by_ur_is(body=body, )
except ApiException as e:
    print("Exception when calling GermplasmApi->export_germplasm_by_ur_is: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**URIsListPostDTO**](URIsListPostDTO.md)| List of germplasm URI | [optional] 


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
uri = 'http://www.phenome-fppn.fr/id/species/zeamays' # str | germplasm URI


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

# **get_germplasm_experiments**
> list[ExperimentGetListDTO] get_germplasm_experiments(uri, authorization, name=name, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

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
uri = 'dev-germplasm:g01' # str | germplasm URI
name = '.*' # str | Regex pattern for filtering experiments by name (optional) (default to .*)
order_by = ['name=asc'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Get experiments where a germplasm has been used
    api_response = api_instance.get_germplasm_experiments(uri, name=name, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GermplasmApi->get_germplasm_experiments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| germplasm URI | 
 **name** | **str**| Regex pattern for filtering experiments by name | [optional] [default to .*]
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

# **get_germplasms_by_uri**
> list[GermplasmGetAllDTO] get_germplasms_by_uri(uris, authorization, accept_language=accept_language)

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
uris = ['uris_example'] # list[str] | Germplasms URIs


try:
    # Get a list of germplasms by their URIs
    api_response = api_instance.get_germplasms_by_uri(uris, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GermplasmApi->get_germplasms_by_uri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uris** | [**list[str]**](str.md)| Germplasms URIs | 


### Return type

[**list[GermplasmGetAllDTO]**](GermplasmGetAllDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_germplasm**
> list[GermplasmGetAllDTO] search_germplasm(authorization, uri=uri, rdf_type=rdf_type, name=name, code=code, production_year=production_year, species=species, variety=variety, accession=accession, institute=institute, experiment=experiment, metadata=metadata, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

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
uri = 'http://opensilex/set/experiments/ZA17' # str | Regex pattern for filtering list by uri (optional)
rdf_type = 'http://www.opensilex.org/vocabulary/oeso#Variety' # str | Search by type (optional)
name = '.*' # str | Regex pattern for filtering list by name and synonyms (optional) (default to .*)
code = '.*' # str | Regex pattern for filtering list by code (optional) (default to .*)
production_year = 2020 # int | Search by production year (optional)
species = 'http://www.phenome-fppn.fr/id/species/zeamays' # str | Search by species (optional)
variety = 'variety_example' # str | Search by variety (optional)
accession = 'accession_example' # str | Search by accession (optional)
institute = 'INRA' # str | Search by institute (optional)
experiment = 'experiment_example' # str | Search by experiment (optional)
metadata = '{ \"water_stress\" : \"resistant\", \"yield\" : \"moderate\"}' # str | Search by metadata (optional)
order_by = ['name=asc'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search germplasm
    api_response = api_instance.search_germplasm(uri=uri, rdf_type=rdf_type, name=name, code=code, production_year=production_year, species=species, variety=variety, accession=accession, institute=institute, experiment=experiment, metadata=metadata, order_by=order_by, page=page, page_size=page_size, )
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

# **update_germplasm**
> ObjectUriResponse update_germplasm(authorization, body=body, accept_language=accept_language)

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

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

