# opensilexClientToolsPython.DataApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_list_data**](DataApi.md#add_list_data) | **POST** /core/data | Add data
[**create_provenance**](DataApi.md#create_provenance) | **POST** /core/provenances | Add a provenance
[**delete_data**](DataApi.md#delete_data) | **DELETE** /core/data/{uri} | Delete data
[**delete_data_on_search**](DataApi.md#delete_data_on_search) | **DELETE** /core/data | Delete data on criteria
[**delete_provenance**](DataApi.md#delete_provenance) | **DELETE** /core/provenances/{uri} | Delete a provenance that doesn&#39;t describe data
[**get_data**](DataApi.md#get_data) | **GET** /core/data/{uri} | Get data
[**get_data_file**](DataApi.md#get_data_file) | **GET** /core/datafiles/{uri} | Get a data file
[**get_data_file_description**](DataApi.md#get_data_file_description) | **GET** /core/datafiles/{uri}/description | Get a data file description
[**get_data_file_descriptions_by_search**](DataApi.md#get_data_file_descriptions_by_search) | **GET** /core/datafiles | Search data files
[**get_pictures_thumbnails**](DataApi.md#get_pictures_thumbnails) | **GET** /core/datafiles/{uri}/thumbnail | Get a picture thumbnail
[**get_provenance**](DataApi.md#get_provenance) | **GET** /core/provenances/{uri} | Get a provenance
[**get_provenances_by_ur_is**](DataApi.md#get_provenances_by_ur_is) | **GET** /core/provenances/by_uris | Get a list of provenances by their URIs
[**post_data_file**](DataApi.md#post_data_file) | **POST** /core/datafiles | Add a data file
[**post_data_file_paths**](DataApi.md#post_data_file_paths) | **POST** /core/datafiles/description | Describe datafiles and give their relative paths in the configured storage system. In the case of already stored datafiles.
[**search_data_list**](DataApi.md#search_data_list) | **GET** /core/data | Search data
[**search_provenance**](DataApi.md#search_provenance) | **GET** /core/provenances | Get provenances
[**update**](DataApi.md#update) | **PUT** /core/data | Update data
[**update1**](DataApi.md#update1) | **PUT** /core/provenances | Update a provenance
[**update_confidence**](DataApi.md#update_confidence) | **PUT** /core/data/{uri}/confidence | Update confidence index


# **add_list_data**
> ObjectUriResponse add_list_data(authorization, body=body, accept_language=accept_language)

Add data



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.DataApi(pythonClient)
body = [opensilexClientToolsPython.DataCreationDTO()] # list[DataCreationDTO] | Data description (optional)


try:
    # Add data
    api_response = api_instance.add_list_data(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->add_list_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[DataCreationDTO]**](DataCreationDTO.md)| Data description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_provenance**
> ObjectUriResponse create_provenance(authorization, body=body, accept_language=accept_language)

Add a provenance



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.DataApi(pythonClient)
body = opensilexClientToolsPython.ProvenanceCreationDTO() # ProvenanceCreationDTO | Provenance description (optional)


try:
    # Add a provenance
    api_response = api_instance.create_provenance(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->create_provenance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProvenanceCreationDTO**](ProvenanceCreationDTO.md)| Provenance description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data**
> ObjectUriResponse delete_data(uri, authorization, accept_language=accept_language)

Delete data



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.DataApi(pythonClient)
uri = '\"http://opensilex.dev/id/data/1598857852858\"' # str | Data URI


try:
    # Delete data
    api_response = api_instance.delete_data(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->delete_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Data URI | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data_on_search**
> ObjectUriResponse delete_data_on_search(authorization, experiment=experiment, scientific_object=scientific_object, variable=variable, provenance=provenance, accept_language=accept_language)

Delete data on criteria



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.DataApi(pythonClient)
experiment = '\"http://opensilex/set/experiments/ZA17\"' # str | Search by experiment uri (optional)
scientific_object = '\"http://opensilex.dev/opensilex/2020/o20000345\"' # str | Search by object uri (optional)
variable = '\"http://opensilex.dev/variable#variable.2020-08-21_11-21-23entity6_method6_quality6_unit6\"' # str | Search by variable uri (optional)
provenance = '\"http://opensilex.dev/provenance/1598001689415\"' # str | Search by provenance uri (optional)


try:
    # Delete data on criteria
    api_response = api_instance.delete_data_on_search(experiment=experiment, scientific_object=scientific_object, variable=variable, provenance=provenance, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->delete_data_on_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment** | **str**| Search by experiment uri | [optional] 
 **scientific_object** | **str**| Search by object uri | [optional] 
 **variable** | **str**| Search by variable uri | [optional] 
 **provenance** | **str**| Search by provenance uri | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_provenance**
> ObjectUriResponse delete_provenance(uri, authorization, accept_language=accept_language)

Delete a provenance that doesn't describe data



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.DataApi(pythonClient)
uri = '\"http://opensilex.dev/id/provenance/provenancelabel\"' # str | Provenance URI


try:
    # Delete a provenance that doesn't describe data
    api_response = api_instance.delete_provenance(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->delete_provenance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Provenance URI | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data**
> DataGetDTO get_data(uri, authorization, accept_language=accept_language)

Get data



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.DataApi(pythonClient)
uri = 'uri_example' # str | Data URI


try:
    # Get data
    api_response = api_instance.get_data(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Data URI | 


### Return type

[**DataGetDTO**](DataGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_file**
> get_data_file(uri, authorization, accept_language=accept_language)

Get a data file



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.DataApi(pythonClient)
uri = 'uri_example' # str | Search by fileUri


try:
    # Get a data file
    api_instance.get_data_file(uri, )
except ApiException as e:
    print("Exception when calling DataApi->get_data_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Search by fileUri | 


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_file_description**
> DataFileGetDTO get_data_file_description(uri, authorization, accept_language=accept_language)

Get a data file description



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.DataApi(pythonClient)
uri = 'uri_example' # str | Search by fileUri


try:
    # Get a data file description
    api_response = api_instance.get_data_file_description(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_data_file_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Search by fileUri | 


### Return type

[**DataFileGetDTO**](DataFileGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_file_descriptions_by_search**
> list[DataFileGetDTO] get_data_file_descriptions_by_search(authorization, rdf_type=rdf_type, start_date=start_date, end_date=end_date, timezone=timezone, experiment=experiment, scientific_objects=scientific_objects, provenances=provenances, metadata=metadata, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Search data files



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.DataApi(pythonClient)
rdf_type = 'rdf_type_example' # str | Search by rdf type uri (optional)
start_date = '\"2020-08-21T00:00:00+01:00\"' # str | Search by minimal date (optional)
end_date = '\"2020-09-21T00:00:00+01:00\"' # str | Search by maximal date (optional)
timezone = '\"Europe/Paris\"' # str | Precise the timezone corresponding to the given dates (optional)
experiment = ['\"http://opensilex/set/experiments/ZA17\"'] # list[str] | Search by experiments (optional)
scientific_objects = ['\"http://opensilex.dev/opensilex/2020/o20000345\"'] # list[str] | Search by object uris list (optional)
provenances = ['\"http://opensilex.dev/provenance/1598001689415\"'] # list[str] | Search by provenance uris list (optional)
metadata = '\"{ \\\"LabelView\\\" : \\\"side90\\\",\\n\\\"paramA\\\" : \\\"90\\\"}\"' # str | Search by metadata (optional)
order_by = ['\"date=desc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search data files
    api_response = api_instance.get_data_file_descriptions_by_search(rdf_type=rdf_type, start_date=start_date, end_date=end_date, timezone=timezone, experiment=experiment, scientific_objects=scientific_objects, provenances=provenances, metadata=metadata, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_data_file_descriptions_by_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rdf_type** | **str**| Search by rdf type uri | [optional] 
 **start_date** | **str**| Search by minimal date | [optional] 
 **end_date** | **str**| Search by maximal date | [optional] 
 **timezone** | **str**| Precise the timezone corresponding to the given dates | [optional] 
 **experiment** | [**list[str]**](str.md)| Search by experiments | [optional] 
 **scientific_objects** | [**list[str]**](str.md)| Search by object uris list | [optional] 
 **provenances** | [**list[str]**](str.md)| Search by provenance uris list | [optional] 
 **metadata** | **str**| Search by metadata | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[DataFileGetDTO]**](DataFileGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pictures_thumbnails**
> get_pictures_thumbnails(uri, authorization, scaled_width=scaled_width, scaled_height=scaled_height, accept_language=accept_language)

Get a picture thumbnail



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.DataApi(pythonClient)
uri = 'uri_example' # str | Search by fileUri
scaled_width = 640 # int | Thumbnail width (optional) (default to 640)
scaled_height = 360 # int | Thumbnail height (optional) (default to 360)


try:
    # Get a picture thumbnail
    api_instance.get_pictures_thumbnails(uri, scaled_width=scaled_width, scaled_height=scaled_height, )
except ApiException as e:
    print("Exception when calling DataApi->get_pictures_thumbnails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Search by fileUri | 
 **scaled_width** | **int**| Thumbnail width | [optional] [default to 640]
 **scaled_height** | **int**| Thumbnail height | [optional] [default to 360]


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provenance**
> ProvenanceGetDTO get_provenance(uri, authorization, accept_language=accept_language)

Get a provenance



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.DataApi(pythonClient)
uri = 'uri_example' # str | Provenance URI


try:
    # Get a provenance
    api_response = api_instance.get_provenance(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_provenance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Provenance URI | 


### Return type

[**ProvenanceGetDTO**](ProvenanceGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provenances_by_ur_is**
> list[ProvenanceGetDTO] get_provenances_by_ur_is(uris, authorization, accept_language=accept_language)

Get a list of provenances by their URIs



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.DataApi(pythonClient)
uris = ['uris_example'] # list[str] | Provenances URIs


try:
    # Get a list of provenances by their URIs
    api_response = api_instance.get_provenances_by_ur_is(uris, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_provenances_by_ur_is: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uris** | [**list[str]**](str.md)| Provenances URIs | 


### Return type

[**list[ProvenanceGetDTO]**](ProvenanceGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_data_file**
> ObjectUriResponse post_data_file(description, file, authorization, accept_language=accept_language)

Add a data file

{\"rdf_type\":\"http://www.opensilex.org/vocabulary/oeso#Image\", \"date\":\"2020-08-21T00:00:00+01:00\", \"timezone\":\"Europe/Paris\", \"scientific_objects\":[\"http://plot01\"], \"provenance\": { \"uri\":\"http://opensilex.dev/provenance/1598001689415\" }, \"metadata\":{ \"LabelView\" : \"side90\", \"paramA\" : \"90\"}}

### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.DataApi(pythonClient)
description = 'description_example' # str | File description with metadata
file = '/path/to/file.txt' # file | Data file


try:
    # Add a data file
    api_response = api_instance.post_data_file(description, file, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->post_data_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| File description with metadata | 
 **file** | **file**| Data file | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_data_file_paths**
> ObjectUriResponse post_data_file_paths(body, authorization, accept_language=accept_language)

Describe datafiles and give their relative paths in the configured storage system. In the case of already stored datafiles.



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.DataApi(pythonClient)
body = [opensilexClientToolsPython.DataFilePathCreationDTO()] # list[DataFilePathCreationDTO] | Metadata of the file


try:
    # Describe datafiles and give their relative paths in the configured storage system. In the case of already stored datafiles.
    api_response = api_instance.post_data_file_paths(body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->post_data_file_paths: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[DataFilePathCreationDTO]**](DataFilePathCreationDTO.md)| Metadata of the file | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_data_list**
> list[DataGetDTO] search_data_list(authorization, start_date=start_date, end_date=end_date, timezone=timezone, experiment=experiment, scientific_objects=scientific_objects, variables=variables, min_confidence=min_confidence, max_confidence=max_confidence, provenances=provenances, metadata=metadata, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Search data



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.DataApi(pythonClient)
start_date = '\"2020-08-21T00:00:00+01:00\"' # str | Search by minimal date (optional)
end_date = '\"2020-09-21T00:00:00+01:00\"' # str | Search by maximal date (optional)
timezone = '\"Europe/Paris\"' # str | Precise the timezone corresponding to the given dates (optional)
experiment = ['\"http://opensilex/set/experiments/ZA17\"'] # list[str] | Search by experiment uris (optional)
scientific_objects = ['\"http://opensilex.dev/opensilex/2020/o20000345\"'] # list[str] | Search by objects uris (optional)
variables = ['\"http://opensilex.dev/variable#variable.2020-08-21_11-21-23entity6_method6_quality6_unit6\"'] # list[str] | Search by variables uris (optional)
min_confidence = 0.5 # float | Search by minimal confidence index (optional)
max_confidence = 1.0 # float | Search by maximal confidence index (optional)
provenances = ['\"http://opensilex.dev/provenance/1598001689415\"'] # list[str] | Search by provenances (optional)
metadata = '\"{ \\\"LabelView\\\" : \\\"side90\\\",\\n\\\"paramA\\\" : \\\"90\\\"}\"' # str | Search by metadata (optional)
order_by = ['\"date=desc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search data
    api_response = api_instance.search_data_list(start_date=start_date, end_date=end_date, timezone=timezone, experiment=experiment, scientific_objects=scientific_objects, variables=variables, min_confidence=min_confidence, max_confidence=max_confidence, provenances=provenances, metadata=metadata, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->search_data_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Search by minimal date | [optional] 
 **end_date** | **str**| Search by maximal date | [optional] 
 **timezone** | **str**| Precise the timezone corresponding to the given dates | [optional] 
 **experiment** | [**list[str]**](str.md)| Search by experiment uris | [optional] 
 **scientific_objects** | [**list[str]**](str.md)| Search by objects uris | [optional] 
 **variables** | [**list[str]**](str.md)| Search by variables uris | [optional] 
 **min_confidence** | **float**| Search by minimal confidence index | [optional] 
 **max_confidence** | **float**| Search by maximal confidence index | [optional] 
 **provenances** | [**list[str]**](str.md)| Search by provenances | [optional] 
 **metadata** | **str**| Search by metadata | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[DataGetDTO]**](DataGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_provenance**
> list[ProvenanceGetDTO] search_provenance(authorization, name=name, description=description, activity=activity, activity_type=activity_type, agent=agent, agent_type=agent_type, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Get provenances



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.DataApi(pythonClient)
name = 'name_example' # str | Regex pattern for filtering by name (optional)
description = 'description_example' # str | Search by description (optional)
activity = 'activity_example' # str | Search by activity URI (optional)
activity_type = 'activity_type_example' # str | Search by activity type (optional)
agent = 'agent_example' # str | Search by agent URI (optional)
agent_type = 'agent_type_example' # str | Search by agent type (optional)
order_by = ['\"date=asc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Get provenances
    api_response = api_instance.search_provenance(name=name, description=description, activity=activity, activity_type=activity_type, agent=agent, agent_type=agent_type, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->search_provenance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Regex pattern for filtering by name | [optional] 
 **description** | **str**| Search by description | [optional] 
 **activity** | **str**| Search by activity URI | [optional] 
 **activity_type** | **str**| Search by activity type | [optional] 
 **agent** | **str**| Search by agent URI | [optional] 
 **agent_type** | **str**| Search by agent type | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[ProvenanceGetDTO]**](ProvenanceGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> ObjectUriResponse update(authorization, body=body, accept_language=accept_language)

Update data



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.DataApi(pythonClient)
body = opensilexClientToolsPython.DataUpdateDTO() # DataUpdateDTO | Data description (optional)


try:
    # Update data
    api_response = api_instance.update(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DataUpdateDTO**](DataUpdateDTO.md)| Data description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update1**
> ObjectUriResponse update1(authorization, body=body, accept_language=accept_language)

Update a provenance



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.DataApi(pythonClient)
body = opensilexClientToolsPython.ProvenanceUpdateDTO() # ProvenanceUpdateDTO | Provenance description (optional)


try:
    # Update a provenance
    api_response = api_instance.update1(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->update1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProvenanceUpdateDTO**](ProvenanceUpdateDTO.md)| Provenance description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_confidence**
> ObjectUriResponse update_confidence(uri, authorization, body=body, accept_language=accept_language)

Update confidence index



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.DataApi(pythonClient)
uri = 'uri_example' # str | Data URI
body = opensilexClientToolsPython.DataConfidenceDTO() # DataConfidenceDTO | Data description (optional)


try:
    # Update confidence index
    api_response = api_instance.update_confidence(uri, body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->update_confidence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Data URI | 
 **body** | [**DataConfidenceDTO**](DataConfidenceDTO.md)| Data description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

