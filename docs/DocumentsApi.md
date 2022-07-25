# opensilexClientToolsPython.DocumentsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_document**](DocumentsApi.md#create_document) | **POST** /core/documents | Add a document
[**delete_document**](DocumentsApi.md#delete_document) | **DELETE** /core/documents/{uri} | Delete a document
[**get_document_file**](DocumentsApi.md#get_document_file) | **GET** /core/documents/{uri} | Get document
[**get_document_metadata**](DocumentsApi.md#get_document_metadata) | **GET** /core/documents/{uri}/description | Get document&#39;s description
[**search_documents**](DocumentsApi.md#search_documents) | **GET** /core/documents | Search documents
[**update_document**](DocumentsApi.md#update_document) | **PUT** /core/documents | Update document&#39;s description


# **create_document**
> ObjectUriResponse create_document(description, authorization, file=file, accept_language=accept_language)

Add a document

{ uri: http://opensilex.dev/set/documents#ProtocolExperimental, identifier: doi:10.1340/309registries, rdf_type: http://www.opensilex.org/vocabulary/oeso#ScientificDocument, title: title, date: 2020-06-01, description: description, targets: http://opensilex.dev/opensilex/id/variables/v001, authors: Author name, language: fr, format: jpg, deprecated: false, keywords: keywords}

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
api_instance = opensilexClientToolsPython.DocumentsApi(pythonClient)
description = 'description_example' # str | File description with metadata
file = '/path/to/file.txt' # file | file (optional)


try:
    # Add a document
    api_response = api_instance.create_document(description, file=file, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->create_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| File description with metadata | 
 **file** | **file**| file | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document**
> ObjectUriResponse delete_document(uri, authorization, accept_language=accept_language)

Delete a document



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
api_instance = opensilexClientToolsPython.DocumentsApi(pythonClient)
uri = 'uri_example' # str | Document URI


try:
    # Delete a document
    api_response = api_instance.delete_document(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->delete_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Document URI | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_file**
> get_document_file(uri, authorization, accept_language=accept_language)

Get document



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
api_instance = opensilexClientToolsPython.DocumentsApi(pythonClient)
uri = '\"http://opensilex.dev/set/documents/ZA17\"' # str | Document URI


try:
    # Get document
    api_instance.get_document_file(uri, )
except ApiException as e:
    print("Exception when calling DocumentsApi->get_document_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Document URI | 


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_metadata**
> DocumentGetDTO get_document_metadata(uri, authorization, accept_language=accept_language)

Get document's description



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
api_instance = opensilexClientToolsPython.DocumentsApi(pythonClient)
uri = '\"http://opensilex.dev/set/documents/ZA17\"' # str | Document URI


try:
    # Get document's description
    api_response = api_instance.get_document_metadata(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get_document_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Document URI | 


### Return type

[**DocumentGetDTO**](DocumentGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_documents**
> list[DocumentGetDTO] search_documents(authorization, rdf_type=rdf_type, title=title, _date=_date, targets=targets, authors=authors, keyword=keyword, multiple=multiple, deprecated=deprecated, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Search documents



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
api_instance = opensilexClientToolsPython.DocumentsApi(pythonClient)
rdf_type = '\"http://www.opensilex.org/vocabulary/oeso#ScientificDocument\"' # str | Search by type (optional)
title = '\"experimental_protocol_3\"' # str | Regex pattern for filtering list by title (optional)
_date = '\"2020\"' # str | Regex pattern for filtering list by date (optional)
targets = '\"dev-expe:za17\"' # str | Search by targets (optional)
authors = '\"Firstname Lastname\"' # str | Regex pattern for filtering list by author (optional)
keyword = '\"keyword\"' # str | Regex pattern for filtering list by keyword (optional)
multiple = '\"keyword or title\"' # str | Regex pattern for filtering list by keyword or title (optional)
deprecated = '\"true\"' # str | Search deprecated file (optional)
order_by = ['\"date=asc\"'] # list[str] | List of fields to sort as an array of fieldTitle=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search documents
    api_response = api_instance.search_documents(rdf_type=rdf_type, title=title, _date=_date, targets=targets, authors=authors, keyword=keyword, multiple=multiple, deprecated=deprecated, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->search_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rdf_type** | **str**| Search by type | [optional] 
 **title** | **str**| Regex pattern for filtering list by title | [optional] 
 **_date** | **str**| Regex pattern for filtering list by date | [optional] 
 **targets** | **str**| Search by targets | [optional] 
 **authors** | **str**| Regex pattern for filtering list by author | [optional] 
 **keyword** | **str**| Regex pattern for filtering list by keyword | [optional] 
 **multiple** | **str**| Regex pattern for filtering list by keyword or title | [optional] 
 **deprecated** | **str**| Search deprecated file | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldTitle&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[DocumentGetDTO]**](DocumentGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document**
> ObjectUriResponse update_document(description, authorization, accept_language=accept_language)

Update document's description



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
api_instance = opensilexClientToolsPython.DocumentsApi(pythonClient)
description = 'description_example' # str | description


try:
    # Update document's description
    api_response = api_instance.update_document(description, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->update_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| description | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

