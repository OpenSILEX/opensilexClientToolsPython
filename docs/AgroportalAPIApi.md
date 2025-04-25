# opensilexClientToolsPython.AgroportalAPIApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agroportal_ontologies**](AgroportalAPIApi.md#get_agroportal_ontologies) | **GET** /core/agroportal/ontologies | Get ontologies from agroportal
[**ping_agroportal**](AgroportalAPIApi.md#ping_agroportal) | **GET** /core/agroportal/ping | Ping agroportal server
[**search_through_agroportal**](AgroportalAPIApi.md#search_through_agroportal) | **GET** /core/agroportal/search | Search through agroportal


# **get_agroportal_ontologies**
> list[OntologyAgroportalDTO] get_agroportal_ontologies(authorization, name=name, ontologies=ontologies, accept_language=accept_language)

Get ontologies from agroportal



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
api_instance = opensilexClientToolsPython.AgroportalAPIApi(pythonClient)
name = '.*' # str | Name (regex) (optional) (default to .*)
ontologies = ['AGROVOC'] # list[str] | List of ontologies to get (acronyms) (optional)


try:
    # Get ontologies from agroportal
    api_response = api_instance.get_agroportal_ontologies(name=name, ontologies=ontologies, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling AgroportalAPIApi->get_agroportal_ontologies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name (regex) | [optional] [default to .*]
 **ontologies** | [**list[str]**](str.md)| List of ontologies to get (acronyms) | [optional] 


### Return type

[**list[OntologyAgroportalDTO]**](OntologyAgroportalDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_agroportal**
> bool ping_agroportal(authorization, timeout=timeout, accept_language=accept_language)

Ping agroportal server



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
api_instance = opensilexClientToolsPython.AgroportalAPIApi(pythonClient)
timeout = 1000 # int | Timeout (optional)


try:
    # Ping agroportal server
    api_response = api_instance.ping_agroportal(timeout=timeout, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling AgroportalAPIApi->ping_agroportal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout | [optional] 


### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_through_agroportal**
> list[AgroportalTermDTO] search_through_agroportal(authorization, name=name, ontologies=ontologies, accept_language=accept_language)

Search through agroportal



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
api_instance = opensilexClientToolsPython.AgroportalAPIApi(pythonClient)
name = 'plant' # str | Name (regex) (optional)
ontologies = ['AGROVOC'] # list[str] | List of ontologies (acronym) (optional)


try:
    # Search through agroportal
    api_response = api_instance.search_through_agroportal(name=name, ontologies=ontologies, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling AgroportalAPIApi->search_through_agroportal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name (regex) | [optional] 
 **ontologies** | [**list[str]**](str.md)| List of ontologies (acronym) | [optional] 


### Return type

[**list[AgroportalTermDTO]**](AgroportalTermDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

