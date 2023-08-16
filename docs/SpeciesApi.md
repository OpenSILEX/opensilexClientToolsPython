# opensilexClientToolsPython.SpeciesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_species**](SpeciesApi.md#get_all_species) | **GET** /core/species | get species (no pagination)


# **get_all_species**
> list[SpeciesDTO] get_all_species(shared_resource_instance=shared_resource_instance, accept_language=accept_language)

get species (no pagination)



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
api_instance = opensilexClientToolsPython.SpeciesApi(pythonClient)
shared_resource_instance = 'shared_resource_instance_example' # str | Shared resource instance URI (optional)


try:
    # get species (no pagination)
    api_response = api_instance.get_all_species(shared_resource_instance=shared_resource_instance, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling SpeciesApi->get_all_species: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_resource_instance** | **str**| Shared resource instance URI | [optional] 


### Return type

[**list[SpeciesDTO]**](SpeciesDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

