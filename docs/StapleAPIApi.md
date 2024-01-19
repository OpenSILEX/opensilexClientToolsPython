# opensilexClientToolsPython.StapleAPIApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_ontology_file**](StapleAPIApi.md#export_ontology_file) | **GET** /staple/ontology_file | Export ontology file for Staple API as turtle syntax


# **export_ontology_file**
> export_ontology_file()

Export ontology file for Staple API as turtle syntax



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
api_instance = opensilexClientToolsPython.StapleAPIApi(pythonClient)


try:
    # Export ontology file for Staple API as turtle syntax
    api_instance.export_ontology_file()
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling StapleAPIApi->export_ontology_file: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-turtle

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

