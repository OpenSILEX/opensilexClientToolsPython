# opensilexClientToolsPython.UriSearchApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_by_uri**](UriSearchApi.md#search_by_uri) | **GET** /core/uri_search/{uri} | Get a list of objects that match the passed URI


# **search_by_uri**
> URIGlobalSearchDTO search_by_uri(uri, authorization, accept_language=accept_language)

Get a list of objects that match the passed URI



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
api_instance = opensilexClientToolsPython.UriSearchApi(pythonClient)
uri = 'http://www.phenome-fppn.fr/id/species/zeamays' # str | URI


try:
    # Get a list of objects that match the passed URI
    api_response = api_instance.search_by_uri(uri, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling UriSearchApi->search_by_uri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| URI | 


### Return type

[**URIGlobalSearchDTO**](URIGlobalSearchDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

