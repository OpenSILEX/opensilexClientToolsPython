# opensilexClientToolsPython.SystemApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_version_info**](SystemApi.md#get_version_info) | **GET** /core/system/info | get system information


# **get_version_info**
> VersionInfoDTO get_version_info()

get system information



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
api_instance = opensilexClientToolsPython.SystemApi(pythonClient)


try:
    # get system information
    api_response = api_instance.get_version_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->get_version_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.


### Return type

[**VersionInfoDTO**](VersionInfoDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

