# opensilexClientToolsPython.VueJsOntologyExtensionApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rdf_type**](VueJsOntologyExtensionApi.md#create_rdf_type) | **POST** /vuejs/owl_extension/rdf_type | Create a custom class
[**delete_rdf_type**](VueJsOntologyExtensionApi.md#delete_rdf_type) | **DELETE** /vuejs/owl_extension/rdf_type | Delete a RDF type
[**get_data_types1**](VueJsOntologyExtensionApi.md#get_data_types1) | **GET** /vuejs/owl_extension/data_types | Return literal datatypes definition
[**get_object_types**](VueJsOntologyExtensionApi.md#get_object_types) | **GET** /vuejs/owl_extension/object_types | Return object types definition
[**get_rdf_type1**](VueJsOntologyExtensionApi.md#get_rdf_type1) | **GET** /vuejs/owl_extension/rdf_type | Return rdf type model definition with properties
[**get_rdf_type_properties**](VueJsOntologyExtensionApi.md#get_rdf_type_properties) | **GET** /vuejs/owl_extension/rdf_type_properties | Return class model properties definitions
[**get_rdf_types_parameters**](VueJsOntologyExtensionApi.md#get_rdf_types_parameters) | **GET** /vuejs/owl_extension/rdf_types_parameters | Return RDF types parameters for Vue.js application
[**set_rdf_type_properties_order**](VueJsOntologyExtensionApi.md#set_rdf_type_properties_order) | **PUT** /vuejs/owl_extension/properties_order | Define properties order
[**update_rdf_type**](VueJsOntologyExtensionApi.md#update_rdf_type) | **PUT** /vuejs/owl_extension/rdf_type | Update a custom class


# **create_rdf_type**
> ObjectUriResponse create_rdf_type(authorization, body=body, accept_language=accept_language)

Create a custom class



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
api_instance = opensilexClientToolsPython.VueJsOntologyExtensionApi(pythonClient)
body = opensilexClientToolsPython.VueRDFTypeDTO() # VueRDFTypeDTO | Class description (optional)


try:
    # Create a custom class
    api_response = api_instance.create_rdf_type(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VueJsOntologyExtensionApi->create_rdf_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VueRDFTypeDTO**](VueRDFTypeDTO.md)| Class description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rdf_type**
> RDFPropertyDTO delete_rdf_type(authorization, rdf_type=rdf_type, accept_language=accept_language)

Delete a RDF type



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
api_instance = opensilexClientToolsPython.VueJsOntologyExtensionApi(pythonClient)
rdf_type = 'rdf_type_example' # str | RDF type (optional)


try:
    # Delete a RDF type
    api_response = api_instance.delete_rdf_type(rdf_type=rdf_type, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VueJsOntologyExtensionApi->delete_rdf_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rdf_type** | **str**| RDF type | [optional] 


### Return type

[**RDFPropertyDTO**](RDFPropertyDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_types1**
> list[VueDataTypeDTO] get_data_types1()

Return literal datatypes definition



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
api_instance = opensilexClientToolsPython.VueJsOntologyExtensionApi(pythonClient)


try:
    # Return literal datatypes definition
    api_response = api_instance.get_data_types1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VueJsOntologyExtensionApi->get_data_types1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.


### Return type

[**list[VueDataTypeDTO]**](VueDataTypeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_types**
> list[VueObjectTypeDTO] get_object_types()

Return object types definition



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
api_instance = opensilexClientToolsPython.VueJsOntologyExtensionApi(pythonClient)


try:
    # Return object types definition
    api_response = api_instance.get_object_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VueJsOntologyExtensionApi->get_object_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.


### Return type

[**list[VueObjectTypeDTO]**](VueObjectTypeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rdf_type1**
> VueRDFTypeDTO get_rdf_type1(rdf_type, authorization, parent_type=parent_type, accept_language=accept_language)

Return rdf type model definition with properties



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
api_instance = opensilexClientToolsPython.VueJsOntologyExtensionApi(pythonClient)
rdf_type = 'rdf_type_example' # str | RDF type URI
parent_type = 'parent_type_example' # str | Parent RDF class URI (optional)


try:
    # Return rdf type model definition with properties
    api_response = api_instance.get_rdf_type1(rdf_type, parent_type=parent_type, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VueJsOntologyExtensionApi->get_rdf_type1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rdf_type** | **str**| RDF type URI | 
 **parent_type** | **str**| Parent RDF class URI | [optional] 


### Return type

[**VueRDFTypeDTO**](VueRDFTypeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rdf_type_properties**
> VueRDFTypeDTO get_rdf_type_properties(rdf_type, parent_type, authorization, accept_language=accept_language)

Return class model properties definitions



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
api_instance = opensilexClientToolsPython.VueJsOntologyExtensionApi(pythonClient)
rdf_type = 'rdf_type_example' # str | RDF class URI
parent_type = 'parent_type_example' # str | Parent RDF class URI


try:
    # Return class model properties definitions
    api_response = api_instance.get_rdf_type_properties(rdf_type, parent_type, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VueJsOntologyExtensionApi->get_rdf_type_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rdf_type** | **str**| RDF class URI | 
 **parent_type** | **str**| Parent RDF class URI | 


### Return type

[**VueRDFTypeDTO**](VueRDFTypeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rdf_types_parameters**
> list[VueRDFTypeParameterDTO] get_rdf_types_parameters()

Return RDF types parameters for Vue.js application



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
api_instance = opensilexClientToolsPython.VueJsOntologyExtensionApi(pythonClient)


try:
    # Return RDF types parameters for Vue.js application
    api_response = api_instance.get_rdf_types_parameters()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VueJsOntologyExtensionApi->get_rdf_types_parameters: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.


### Return type

[**list[VueRDFTypeParameterDTO]**](VueRDFTypeParameterDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_rdf_type_properties_order**
> ObjectUriResponse set_rdf_type_properties_order(rdf_type, authorization, body=body, accept_language=accept_language)

Define properties order



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
api_instance = opensilexClientToolsPython.VueJsOntologyExtensionApi(pythonClient)
rdf_type = 'rdf_type_example' # str | RDF type
body = [opensilexClientToolsPython.list[str]()] # list[str] | Array of properties (optional)


try:
    # Define properties order
    api_response = api_instance.set_rdf_type_properties_order(rdf_type, body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VueJsOntologyExtensionApi->set_rdf_type_properties_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rdf_type** | **str**| RDF type | 
 **body** | **list[str]**| Array of properties | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rdf_type**
> ObjectUriResponse update_rdf_type(authorization, body=body, accept_language=accept_language)

Update a custom class



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
api_instance = opensilexClientToolsPython.VueJsOntologyExtensionApi(pythonClient)
body = opensilexClientToolsPython.VueRDFTypeDTO() # VueRDFTypeDTO | RDF type definition (optional)


try:
    # Update a custom class
    api_response = api_instance.update_rdf_type(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VueJsOntologyExtensionApi->update_rdf_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VueRDFTypeDTO**](VueRDFTypeDTO.md)| RDF type definition | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

