# opensilexClientToolsPython.VariablesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classic_export_variable_by_ur_is**](VariablesApi.md#classic_export_variable_by_ur_is) | **POST** /core/variables/export_classic_by_uris | export variable by list of uris
[**copy_from_shared_resource_instance**](VariablesApi.md#copy_from_shared_resource_instance) | **POST** /core/variables/copy_from_shared_resource_instance | Copy the selected variables from the shared resource instance
[**create_characteristic**](VariablesApi.md#create_characteristic) | **POST** /core/characteristics | Add a characteristic
[**create_entity**](VariablesApi.md#create_entity) | **POST** /core/entities | Add an entity
[**create_interest_entity**](VariablesApi.md#create_interest_entity) | **POST** /core/entities_of_interest | Add an entity of interest
[**create_method**](VariablesApi.md#create_method) | **POST** /core/methods | Add a method
[**create_unit**](VariablesApi.md#create_unit) | **POST** /core/units | Add an unit
[**create_variable**](VariablesApi.md#create_variable) | **POST** /core/variables | Add a variable
[**create_variables_group**](VariablesApi.md#create_variables_group) | **POST** /core/variables_group | Add a variables group
[**delete_characteristic**](VariablesApi.md#delete_characteristic) | **DELETE** /core/characteristics/{uri} | Delete a characteristic
[**delete_entity**](VariablesApi.md#delete_entity) | **DELETE** /core/entities/{uri} | Delete an entity
[**delete_interest_entity**](VariablesApi.md#delete_interest_entity) | **DELETE** /core/entities_of_interest/{uri} | Delete an entity of interest
[**delete_method**](VariablesApi.md#delete_method) | **DELETE** /core/methods/{uri} | Delete a method
[**delete_unit**](VariablesApi.md#delete_unit) | **DELETE** /core/units/{uri} | Delete an unit
[**delete_variable**](VariablesApi.md#delete_variable) | **DELETE** /core/variables/{uri} | Delete a variable
[**delete_variables_group**](VariablesApi.md#delete_variables_group) | **DELETE** /core/variables_group/{uri} | Delete a variables group
[**details_export_variable_by_ur_is**](VariablesApi.md#details_export_variable_by_ur_is) | **POST** /core/variables/export_details_by_uris | export detailed variable by list of uris
[**get_characteristic**](VariablesApi.md#get_characteristic) | **GET** /core/characteristics/{uri} | Get a characteristic
[**get_characteristics_by_ur_is**](VariablesApi.md#get_characteristics_by_ur_is) | **GET** /core/characteristics/by_uris | Get detailed characteristics by uris
[**get_datatypes**](VariablesApi.md#get_datatypes) | **GET** /core/variables/datatypes | Get variables datatypes
[**get_entities_by_ur_is**](VariablesApi.md#get_entities_by_ur_is) | **GET** /core/entities/by_uris | Get detailed entities by uris
[**get_entity**](VariablesApi.md#get_entity) | **GET** /core/entities/{uri} | Get an entity
[**get_interest_entities_by_ur_is**](VariablesApi.md#get_interest_entities_by_ur_is) | **GET** /core/entities_of_interest/by_uris | Get detailed entities of interest by uris
[**get_interest_entity**](VariablesApi.md#get_interest_entity) | **GET** /core/entities_of_interest/{uri} | Get an entity of interest
[**get_method**](VariablesApi.md#get_method) | **GET** /core/methods/{uri} | Get a method
[**get_methods_by_ur_is**](VariablesApi.md#get_methods_by_ur_is) | **GET** /core/methods/by_uris | Get detailed methods by uris
[**get_unit**](VariablesApi.md#get_unit) | **GET** /core/units/{uri} | Get an unit
[**get_units_by_ur_is**](VariablesApi.md#get_units_by_ur_is) | **GET** /core/units/by_uris | Get detailed units by uris
[**get_variable**](VariablesApi.md#get_variable) | **GET** /core/variables/{uri} | Get a variable
[**get_variables_by_ur_is**](VariablesApi.md#get_variables_by_ur_is) | **GET** /core/variables/by_uris | Get detailed variables by uris
[**get_variables_group**](VariablesApi.md#get_variables_group) | **GET** /core/variables_group/{uri} | Get a variables group
[**get_variables_group_by_ur_is**](VariablesApi.md#get_variables_group_by_ur_is) | **GET** /core/variables_group/by_uris | Get variables groups by their URIs
[**search_characteristics**](VariablesApi.md#search_characteristics) | **GET** /core/characteristics | Search characteristics by name
[**search_entities**](VariablesApi.md#search_entities) | **GET** /core/entities | Search entities by name
[**search_interest_entity**](VariablesApi.md#search_interest_entity) | **GET** /core/entities_of_interest | Search entities of interest by name
[**search_methods**](VariablesApi.md#search_methods) | **GET** /core/methods | Search methods by name
[**search_units**](VariablesApi.md#search_units) | **GET** /core/units | Search units by name
[**search_variables**](VariablesApi.md#search_variables) | **GET** /core/variables | Search variables
[**search_variables_details**](VariablesApi.md#search_variables_details) | **GET** /core/variables/details | Search detailed variables by name, long name, entity, characteristic, method or unit name
[**search_variables_groups**](VariablesApi.md#search_variables_groups) | **GET** /core/variables_group | Search variables groups
[**update_characteristic**](VariablesApi.md#update_characteristic) | **PUT** /core/characteristics | Update a characteristic
[**update_entity**](VariablesApi.md#update_entity) | **PUT** /core/entities | Update an entity
[**update_interest_entity**](VariablesApi.md#update_interest_entity) | **PUT** /core/entities_of_interest | Update an entity of interest
[**update_method**](VariablesApi.md#update_method) | **PUT** /core/methods | Update a method
[**update_unit**](VariablesApi.md#update_unit) | **PUT** /core/units | Update an unit
[**update_variable**](VariablesApi.md#update_variable) | **PUT** /core/variables | Update a variable
[**update_variables_group**](VariablesApi.md#update_variables_group) | **PUT** /core/variables_group | Update a variables group


# **classic_export_variable_by_ur_is**
> classic_export_variable_by_ur_is(authorization, body=body, accept_language=accept_language)

export variable by list of uris



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
body = opensilexClientToolsPython.URIsListPostDTO() # URIsListPostDTO | List of variable URI (optional)


try:
    # export variable by list of uris
    api_instance.classic_export_variable_by_ur_is(body=body, )
except ApiException as e:
    print("Exception when calling VariablesApi->classic_export_variable_by_ur_is: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**URIsListPostDTO**](URIsListPostDTO.md)| List of variable URI | [optional] 


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_from_shared_resource_instance**
> VariableCopyResponseDTO copy_from_shared_resource_instance(body, authorization, accept_language=accept_language)

Copy the selected variables from the shared resource instance



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
body = opensilexClientToolsPython.CopyResourceDTO() # CopyResourceDTO | List of variable URI to copy


try:
    # Copy the selected variables from the shared resource instance
    api_response = api_instance.copy_from_shared_resource_instance(body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->copy_from_shared_resource_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CopyResourceDTO**](CopyResourceDTO.md)| List of variable URI to copy | 


### Return type

[**VariableCopyResponseDTO**](VariableCopyResponseDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_characteristic**
> ObjectUriResponse create_characteristic(authorization, body=body, accept_language=accept_language)

Add a characteristic



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
body = opensilexClientToolsPython.CharacteristicCreationDTO() # CharacteristicCreationDTO | Characteristic description (optional)


try:
    # Add a characteristic
    api_response = api_instance.create_characteristic(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->create_characteristic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CharacteristicCreationDTO**](CharacteristicCreationDTO.md)| Characteristic description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_entity**
> ObjectUriResponse create_entity(authorization, body=body, accept_language=accept_language)

Add an entity



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
body = opensilexClientToolsPython.EntityCreationDTO() # EntityCreationDTO | Entity description (optional)


try:
    # Add an entity
    api_response = api_instance.create_entity(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->create_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntityCreationDTO**](EntityCreationDTO.md)| Entity description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_interest_entity**
> ObjectUriResponse create_interest_entity(authorization, body=body, accept_language=accept_language)

Add an entity of interest



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
body = opensilexClientToolsPython.InterestEntityCreationDTO() # InterestEntityCreationDTO | Entity of interest description (optional)


try:
    # Add an entity of interest
    api_response = api_instance.create_interest_entity(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->create_interest_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InterestEntityCreationDTO**](InterestEntityCreationDTO.md)| Entity of interest description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_method**
> ObjectUriResponse create_method(authorization, body=body, accept_language=accept_language)

Add a method



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
body = opensilexClientToolsPython.MethodCreationDTO() # MethodCreationDTO | Method description (optional)


try:
    # Add a method
    api_response = api_instance.create_method(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->create_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MethodCreationDTO**](MethodCreationDTO.md)| Method description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_unit**
> ObjectUriResponse create_unit(authorization, body=body, accept_language=accept_language)

Add an unit



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
body = opensilexClientToolsPython.UnitCreationDTO() # UnitCreationDTO | Unit description (optional)


try:
    # Add an unit
    api_response = api_instance.create_unit(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->create_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnitCreationDTO**](UnitCreationDTO.md)| Unit description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_variable**
> ObjectUriResponse create_variable(authorization, body=body, accept_language=accept_language)

Add a variable



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
body = opensilexClientToolsPython.VariableCreationDTO() # VariableCreationDTO | Variable description (optional)


try:
    # Add a variable
    api_response = api_instance.create_variable(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->create_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VariableCreationDTO**](VariableCreationDTO.md)| Variable description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_variables_group**
> ObjectUriResponse create_variables_group(authorization, body=body, accept_language=accept_language)

Add a variables group



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
body = opensilexClientToolsPython.VariablesGroupCreationDTO() # VariablesGroupCreationDTO | Variables group description (optional)


try:
    # Add a variables group
    api_response = api_instance.create_variables_group(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->create_variables_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VariablesGroupCreationDTO**](VariablesGroupCreationDTO.md)| Variables group description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_characteristic**
> ObjectUriResponse delete_characteristic(uri, authorization, accept_language=accept_language)

Delete a characteristic



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
uri = '\"http://opensilex.dev/set/variables/characteristic/Height\"' # str | Characteristic URI


try:
    # Delete a characteristic
    api_response = api_instance.delete_characteristic(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->delete_characteristic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Characteristic URI | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_entity**
> ObjectUriResponse delete_entity(uri, authorization, accept_language=accept_language)

Delete an entity



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
uri = '\"http://opensilex.dev/set/variables/entity/Plant\"' # str | Entity URI


try:
    # Delete an entity
    api_response = api_instance.delete_entity(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->delete_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Entity URI | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_interest_entity**
> ObjectUriResponse delete_interest_entity(uri, authorization, accept_language=accept_language)

Delete an entity of interest



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
uri = '\"http://opensilex.dev/set/variables/entity_of_interest/Plot\"' # str | Entity of interest URI


try:
    # Delete an entity of interest
    api_response = api_instance.delete_interest_entity(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->delete_interest_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Entity of interest URI | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_method**
> ObjectUriResponse delete_method(uri, authorization, accept_language=accept_language)

Delete a method



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
uri = '\"http://opensilex.dev/set/variables/method/ImageAnalysis\"' # str | Method URI


try:
    # Delete a method
    api_response = api_instance.delete_method(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->delete_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Method URI | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_unit**
> ObjectUriResponse delete_unit(uri, authorization, accept_language=accept_language)

Delete an unit



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
uri = '\"http://opensilex.dev/set/variables/unit/Centimeter\"' # str | Unit URI


try:
    # Delete an unit
    api_response = api_instance.delete_unit(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->delete_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Unit URI | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_variable**
> ObjectUriResponse delete_variable(uri, authorization, accept_language=accept_language)

Delete a variable



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
uri = '\"http://opensilex.dev/set/variables/Plant_Height\"' # str | Variable URI


try:
    # Delete a variable
    api_response = api_instance.delete_variable(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->delete_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Variable URI | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_variables_group**
> ObjectUriResponse delete_variables_group(uri, authorization, accept_language=accept_language)

Delete a variables group



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
uri = 'uri_example' # str | Variables group URI


try:
    # Delete a variables group
    api_response = api_instance.delete_variables_group(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->delete_variables_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Variables group URI | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **details_export_variable_by_ur_is**
> details_export_variable_by_ur_is(authorization, body=body, accept_language=accept_language)

export detailed variable by list of uris



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
body = opensilexClientToolsPython.URIsListPostDTO() # URIsListPostDTO | List of variable URI (optional)


try:
    # export detailed variable by list of uris
    api_instance.details_export_variable_by_ur_is(body=body, )
except ApiException as e:
    print("Exception when calling VariablesApi->details_export_variable_by_ur_is: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**URIsListPostDTO**](URIsListPostDTO.md)| List of variable URI | [optional] 


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characteristic**
> CharacteristicDetailsDTO get_characteristic(uri, authorization, accept_language=accept_language)

Get a characteristic



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
uri = '\"http://opensilex.dev/set/variables/characteristic/Height\"' # str | Characteristic URI


try:
    # Get a characteristic
    api_response = api_instance.get_characteristic(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->get_characteristic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Characteristic URI | 


### Return type

[**CharacteristicDetailsDTO**](CharacteristicDetailsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characteristics_by_ur_is**
> list[CharacteristicDetailsDTO] get_characteristics_by_ur_is(uris, authorization, shared_resource_instance=shared_resource_instance, accept_language=accept_language)

Get detailed characteristics by uris



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
uris = ['uris_example'] # list[str] | Characteristics URIs
shared_resource_instance = 'shared_resource_instance_example' # str | Shared resource instance (optional)


try:
    # Get detailed characteristics by uris
    api_response = api_instance.get_characteristics_by_ur_is(uris, shared_resource_instance=shared_resource_instance, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->get_characteristics_by_ur_is: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uris** | [**list[str]**](str.md)| Characteristics URIs | 
 **shared_resource_instance** | **str**| Shared resource instance | [optional] 


### Return type

[**list[CharacteristicDetailsDTO]**](CharacteristicDetailsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datatypes**
> list[VariableDatatypeDTO] get_datatypes()

Get variables datatypes



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)


try:
    # Get variables datatypes
    api_response = api_instance.get_datatypes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->get_datatypes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.


### Return type

[**list[VariableDatatypeDTO]**](VariableDatatypeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entities_by_ur_is**
> list[EntityDetailsDTO] get_entities_by_ur_is(uris, authorization, shared_resource_instance=shared_resource_instance, accept_language=accept_language)

Get detailed entities by uris



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
uris = ['uris_example'] # list[str] | Entities URIs
shared_resource_instance = 'shared_resource_instance_example' # str | Shared resource instance (optional)


try:
    # Get detailed entities by uris
    api_response = api_instance.get_entities_by_ur_is(uris, shared_resource_instance=shared_resource_instance, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->get_entities_by_ur_is: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uris** | [**list[str]**](str.md)| Entities URIs | 
 **shared_resource_instance** | **str**| Shared resource instance | [optional] 


### Return type

[**list[EntityDetailsDTO]**](EntityDetailsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity**
> EntityDetailsDTO get_entity(uri, authorization, accept_language=accept_language)

Get an entity



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
uri = '\"http://opensilex.dev/set/variables/entity/Plant\"' # str | Entity URI


try:
    # Get an entity
    api_response = api_instance.get_entity(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->get_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Entity URI | 


### Return type

[**EntityDetailsDTO**](EntityDetailsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_interest_entities_by_ur_is**
> list[InterestEntityDetailsDTO] get_interest_entities_by_ur_is(uris, authorization, shared_resource_instance=shared_resource_instance, accept_language=accept_language)

Get detailed entities of interest by uris



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
uris = ['uris_example'] # list[str] | Entities of interest URIs
shared_resource_instance = 'shared_resource_instance_example' # str | Shared resource instance (optional)


try:
    # Get detailed entities of interest by uris
    api_response = api_instance.get_interest_entities_by_ur_is(uris, shared_resource_instance=shared_resource_instance, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->get_interest_entities_by_ur_is: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uris** | [**list[str]**](str.md)| Entities of interest URIs | 
 **shared_resource_instance** | **str**| Shared resource instance | [optional] 


### Return type

[**list[InterestEntityDetailsDTO]**](InterestEntityDetailsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_interest_entity**
> InterestEntityDetailsDTO get_interest_entity(uri, authorization, accept_language=accept_language)

Get an entity of interest



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
uri = '\"http://opensilex.dev/set/variables/entity_of_interest/Plot\"' # str | Entity of interest URI


try:
    # Get an entity of interest
    api_response = api_instance.get_interest_entity(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->get_interest_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Entity of interest URI | 


### Return type

[**InterestEntityDetailsDTO**](InterestEntityDetailsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_method**
> MethodDetailsDTO get_method(uri, authorization, accept_language=accept_language)

Get a method



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
uri = '\"http://opensilex.dev/set/variables/method/ImageAnalysis\"' # str | Method URI


try:
    # Get a method
    api_response = api_instance.get_method(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->get_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Method URI | 


### Return type

[**MethodDetailsDTO**](MethodDetailsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_methods_by_ur_is**
> list[MethodDetailsDTO] get_methods_by_ur_is(uris, authorization, shared_resource_instance=shared_resource_instance, accept_language=accept_language)

Get detailed methods by uris



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
uris = ['uris_example'] # list[str] | Methods URIs
shared_resource_instance = 'shared_resource_instance_example' # str | Shared resource instance (optional)


try:
    # Get detailed methods by uris
    api_response = api_instance.get_methods_by_ur_is(uris, shared_resource_instance=shared_resource_instance, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->get_methods_by_ur_is: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uris** | [**list[str]**](str.md)| Methods URIs | 
 **shared_resource_instance** | **str**| Shared resource instance | [optional] 


### Return type

[**list[MethodDetailsDTO]**](MethodDetailsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unit**
> UnitDetailsDTO get_unit(uri, authorization, accept_language=accept_language)

Get an unit



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
uri = '\"http://opensilex.dev/set/variables/unit/Centimeter\"' # str | Unit URI


try:
    # Get an unit
    api_response = api_instance.get_unit(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->get_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Unit URI | 


### Return type

[**UnitDetailsDTO**](UnitDetailsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_units_by_ur_is**
> list[UnitDetailsDTO] get_units_by_ur_is(uris, authorization, shared_resource_instance=shared_resource_instance, accept_language=accept_language)

Get detailed units by uris



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
uris = ['uris_example'] # list[str] | Units URIs
shared_resource_instance = 'shared_resource_instance_example' # str | Shared resource instance (optional)


try:
    # Get detailed units by uris
    api_response = api_instance.get_units_by_ur_is(uris, shared_resource_instance=shared_resource_instance, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->get_units_by_ur_is: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uris** | [**list[str]**](str.md)| Units URIs | 
 **shared_resource_instance** | **str**| Shared resource instance | [optional] 


### Return type

[**list[UnitDetailsDTO]**](UnitDetailsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variable**
> VariableDetailsDTO get_variable(uri, authorization, shared_resource_instance=shared_resource_instance, accept_language=accept_language)

Get a variable



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
uri = '\"http://opensilex.dev/set/variables/Plant_Height\"' # str | Variable URI
shared_resource_instance = 'shared_resource_instance_example' # str | Shared resource instance (optional)


try:
    # Get a variable
    api_response = api_instance.get_variable(uri, shared_resource_instance=shared_resource_instance, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->get_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Variable URI | 
 **shared_resource_instance** | **str**| Shared resource instance | [optional] 


### Return type

[**VariableDetailsDTO**](VariableDetailsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variables_by_ur_is**
> list[VariableDetailsDTO] get_variables_by_ur_is(uris, authorization, accept_language=accept_language)

Get detailed variables by uris



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
uris = ['uris_example'] # list[str] | Variables URIs


try:
    # Get detailed variables by uris
    api_response = api_instance.get_variables_by_ur_is(uris, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->get_variables_by_ur_is: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uris** | [**list[str]**](str.md)| Variables URIs | 


### Return type

[**list[VariableDetailsDTO]**](VariableDetailsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variables_group**
> VariablesGroupGetDTO get_variables_group(uri, authorization, accept_language=accept_language)

Get a variables group



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
uri = 'uri_example' # str | Variables group URI


try:
    # Get a variables group
    api_response = api_instance.get_variables_group(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->get_variables_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Variables group URI | 


### Return type

[**VariablesGroupGetDTO**](VariablesGroupGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variables_group_by_ur_is**
> list[VariablesGroupGetDTO] get_variables_group_by_ur_is(uris, authorization, shared_resource_instance=shared_resource_instance, accept_language=accept_language)

Get variables groups by their URIs



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
uris = ['uris_example'] # list[str] | Variables group URIs
shared_resource_instance = 'shared_resource_instance_example' # str | Shared resource instance (optional)


try:
    # Get variables groups by their URIs
    api_response = api_instance.get_variables_group_by_ur_is(uris, shared_resource_instance=shared_resource_instance, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->get_variables_group_by_ur_is: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uris** | [**list[str]**](str.md)| Variables group URIs | 
 **shared_resource_instance** | **str**| Shared resource instance | [optional] 


### Return type

[**list[VariablesGroupGetDTO]**](VariablesGroupGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_characteristics**
> list[CharacteristicGetDTO] search_characteristics(authorization, name=name, order_by=order_by, page=page, page_size=page_size, shared_resource_instance=shared_resource_instance, accept_language=accept_language)

Search characteristics by name



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
name = '\"Height\"' # str | Name (regex) (optional)
order_by = ['\"uri=asc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional)
shared_resource_instance = 'shared_resource_instance_example' # str | Shared resource instance (optional)


try:
    # Search characteristics by name
    api_response = api_instance.search_characteristics(name=name, order_by=order_by, page=page, page_size=page_size, shared_resource_instance=shared_resource_instance, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->search_characteristics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name (regex) | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] 
 **shared_resource_instance** | **str**| Shared resource instance | [optional] 


### Return type

[**list[CharacteristicGetDTO]**](CharacteristicGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_entities**
> list[EntityGetDTO] search_entities(authorization, name=name, order_by=order_by, page=page, page_size=page_size, shared_resource_instance=shared_resource_instance, accept_language=accept_language)

Search entities by name



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
name = '\"plant\"' # str | Name (regex) (optional)
order_by = ['\"uri=asc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional)
shared_resource_instance = 'shared_resource_instance_example' # str | Shared resource instance (optional)


try:
    # Search entities by name
    api_response = api_instance.search_entities(name=name, order_by=order_by, page=page, page_size=page_size, shared_resource_instance=shared_resource_instance, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->search_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name (regex) | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] 
 **shared_resource_instance** | **str**| Shared resource instance | [optional] 


### Return type

[**list[EntityGetDTO]**](EntityGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_interest_entity**
> list[InterestEntityGetDTO] search_interest_entity(authorization, name=name, order_by=order_by, page=page, page_size=page_size, shared_resource_instance=shared_resource_instance, accept_language=accept_language)

Search entities of interest by name



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
name = '\"plot\"' # str | Name (regex) (optional)
order_by = ['\"uri=asc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional)
shared_resource_instance = 'shared_resource_instance_example' # str | Shared resource instance (optional)


try:
    # Search entities of interest by name
    api_response = api_instance.search_interest_entity(name=name, order_by=order_by, page=page, page_size=page_size, shared_resource_instance=shared_resource_instance, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->search_interest_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name (regex) | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] 
 **shared_resource_instance** | **str**| Shared resource instance | [optional] 


### Return type

[**list[InterestEntityGetDTO]**](InterestEntityGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_methods**
> list[MethodGetDTO] search_methods(authorization, name=name, order_by=order_by, page=page, page_size=page_size, shared_resource_instance=shared_resource_instance, accept_language=accept_language)

Search methods by name



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
name = '\"ImageAnalysis\"' # str | Name (regex) (optional)
order_by = ['\"uri=asc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional)
shared_resource_instance = 'shared_resource_instance_example' # str | Shared resource instance (optional)


try:
    # Search methods by name
    api_response = api_instance.search_methods(name=name, order_by=order_by, page=page, page_size=page_size, shared_resource_instance=shared_resource_instance, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->search_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name (regex) | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] 
 **shared_resource_instance** | **str**| Shared resource instance | [optional] 


### Return type

[**list[MethodGetDTO]**](MethodGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_units**
> list[UnitGetDTO] search_units(authorization, name=name, order_by=order_by, page=page, page_size=page_size, shared_resource_instance=shared_resource_instance, accept_language=accept_language)

Search units by name



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
name = '\"Centimeter\"' # str | Name (regex) (optional)
order_by = ['\"uri=asc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional)
shared_resource_instance = 'shared_resource_instance_example' # str | Shared resource instance (optional)


try:
    # Search units by name
    api_response = api_instance.search_units(name=name, order_by=order_by, page=page, page_size=page_size, shared_resource_instance=shared_resource_instance, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->search_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name (regex) | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] 
 **shared_resource_instance** | **str**| Shared resource instance | [optional] 


### Return type

[**list[UnitGetDTO]**](UnitGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_variables**
> list[VariableGetDTO] search_variables(authorization, name=name, entity=entity, entity_of_interest=entity_of_interest, characteristic=characteristic, method=method, unit=unit, group_of_variables=group_of_variables, data_type=data_type, time_interval=time_interval, species=species, with_associated_data=with_associated_data, experiments=experiments, scientific_objects=scientific_objects, devices=devices, order_by=order_by, page=page, page_size=page_size, shared_resource_instance=shared_resource_instance, accept_language=accept_language)

Search variables

The following fields could be used for sorting :    _entity_name/entityName : the name of the variable entity   _characteristic_name/characteristicName : the name of the variable characteristic   _method_name/methodName : the name of the variable method   _unit_name/unitName : the name of the variable unit  

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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
name = '\"plant_height\"' # str | Name regex pattern (optional)
entity = 'entity_example' # str | Entity filter (optional)
entity_of_interest = 'entity_of_interest_example' # str | Entity of interest filter (optional)
characteristic = 'characteristic_example' # str | Characteristic filter (optional)
method = 'method_example' # str | Method filter (optional)
unit = 'unit_example' # str | Unit filter (optional)
group_of_variables = 'group_of_variables_example' # str | Group filter (optional)
data_type = 'data_type_example' # str | Data type filter (optional)
time_interval = 'time_interval_example' # str | Time interval filter (optional)
species = ['species_example'] # list[str] | Species filter (optional)
with_associated_data = false # bool | Set this param to true to get associated data (optional) (default to false)
experiments = ['experiments_example'] # list[str] | Experiment filter (optional)
scientific_objects = ['scientific_objects_example'] # list[str] | Scientific object filter (optional)
devices = ['devices_example'] # list[str] | Device filter (optional)
order_by = ['\"uri=asc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)
shared_resource_instance = 'shared_resource_instance_example' # str | Shared resource instance (optional)


try:
    # Search variables
    api_response = api_instance.search_variables(name=name, entity=entity, entity_of_interest=entity_of_interest, characteristic=characteristic, method=method, unit=unit, group_of_variables=group_of_variables, data_type=data_type, time_interval=time_interval, species=species, with_associated_data=with_associated_data, experiments=experiments, scientific_objects=scientific_objects, devices=devices, order_by=order_by, page=page, page_size=page_size, shared_resource_instance=shared_resource_instance, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->search_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name regex pattern | [optional] 
 **entity** | **str**| Entity filter | [optional] 
 **entity_of_interest** | **str**| Entity of interest filter | [optional] 
 **characteristic** | **str**| Characteristic filter | [optional] 
 **method** | **str**| Method filter | [optional] 
 **unit** | **str**| Unit filter | [optional] 
 **group_of_variables** | **str**| Group filter | [optional] 
 **data_type** | **str**| Data type filter | [optional] 
 **time_interval** | **str**| Time interval filter | [optional] 
 **species** | [**list[str]**](str.md)| Species filter | [optional] 
 **with_associated_data** | **bool**| Set this param to true to get associated data | [optional] [default to false]
 **experiments** | [**list[str]**](str.md)| Experiment filter | [optional] 
 **scientific_objects** | [**list[str]**](str.md)| Scientific object filter | [optional] 
 **devices** | [**list[str]**](str.md)| Device filter | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]
 **shared_resource_instance** | **str**| Shared resource instance | [optional] 


### Return type

[**list[VariableGetDTO]**](VariableGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_variables_details**
> list[VariableDetailsDTO] search_variables_details(authorization, name=name, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Search detailed variables by name, long name, entity, characteristic, method or unit name

The following fields could be used for sorting :    _entity_name : the name of the variable entity   _characteristic_name : the name of the variable characteristic   _method_name : the name of the variable method   _unit_name : the name of the variable unit  

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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
name = '\"plant_height\"' # str | Name regex pattern (optional)
order_by = ['\"uri=asc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search detailed variables by name, long name, entity, characteristic, method or unit name
    api_response = api_instance.search_variables_details(name=name, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->search_variables_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name regex pattern | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[VariableDetailsDTO]**](VariableDetailsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_variables_groups**
> list[VariablesGroupGetDTO] search_variables_groups(authorization, name=name, variable_uri=variable_uri, order_by=order_by, page=page, page_size=page_size, shared_resource_instance=shared_resource_instance, accept_language=accept_language)

Search variables groups



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
name = 'name_example' # str | Regex pattern for filtering by name (optional)
variable_uri = 'variable_uri_example' # str | Variable URI (optional)
order_by = ['\"uri=asc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)
shared_resource_instance = 'shared_resource_instance_example' # str | Shared resource instance (optional)


try:
    # Search variables groups
    api_response = api_instance.search_variables_groups(name=name, variable_uri=variable_uri, order_by=order_by, page=page, page_size=page_size, shared_resource_instance=shared_resource_instance, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->search_variables_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Regex pattern for filtering by name | [optional] 
 **variable_uri** | **str**| Variable URI | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]
 **shared_resource_instance** | **str**| Shared resource instance | [optional] 


### Return type

[**list[VariablesGroupGetDTO]**](VariablesGroupGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_characteristic**
> ObjectUriResponse update_characteristic(authorization, body=body, accept_language=accept_language)

Update a characteristic



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
body = opensilexClientToolsPython.CharacteristicUpdateDTO() # CharacteristicUpdateDTO | Characteristic description (optional)


try:
    # Update a characteristic
    api_response = api_instance.update_characteristic(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->update_characteristic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CharacteristicUpdateDTO**](CharacteristicUpdateDTO.md)| Characteristic description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entity**
> ObjectUriResponse update_entity(authorization, body=body, accept_language=accept_language)

Update an entity



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
body = opensilexClientToolsPython.EntityUpdateDTO() # EntityUpdateDTO | Entity description (optional)


try:
    # Update an entity
    api_response = api_instance.update_entity(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->update_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntityUpdateDTO**](EntityUpdateDTO.md)| Entity description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_interest_entity**
> ObjectUriResponse update_interest_entity(authorization, body=body, accept_language=accept_language)

Update an entity of interest



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
body = opensilexClientToolsPython.InterestEntityUpdateDTO() # InterestEntityUpdateDTO | Entity of interest description (optional)


try:
    # Update an entity of interest
    api_response = api_instance.update_interest_entity(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->update_interest_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InterestEntityUpdateDTO**](InterestEntityUpdateDTO.md)| Entity of interest description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_method**
> ObjectUriResponse update_method(authorization, body=body, accept_language=accept_language)

Update a method



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
body = opensilexClientToolsPython.MethodUpdateDTO() # MethodUpdateDTO | Method description (optional)


try:
    # Update a method
    api_response = api_instance.update_method(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->update_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MethodUpdateDTO**](MethodUpdateDTO.md)| Method description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_unit**
> ObjectUriResponse update_unit(authorization, body=body, accept_language=accept_language)

Update an unit



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
body = opensilexClientToolsPython.UnitUpdateDTO() # UnitUpdateDTO | Unit description (optional)


try:
    # Update an unit
    api_response = api_instance.update_unit(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->update_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnitUpdateDTO**](UnitUpdateDTO.md)| Unit description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_variable**
> ObjectUriResponse update_variable(authorization, body=body, accept_language=accept_language)

Update a variable



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
body = opensilexClientToolsPython.VariableUpdateDTO() # VariableUpdateDTO | Variable description (optional)


try:
    # Update a variable
    api_response = api_instance.update_variable(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->update_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VariableUpdateDTO**](VariableUpdateDTO.md)| Variable description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_variables_group**
> ObjectUriResponse update_variables_group(authorization, body=body, accept_language=accept_language)

Update a variables group



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
api_instance = opensilexClientToolsPython.VariablesApi(pythonClient)
body = opensilexClientToolsPython.VariablesGroupUpdateDTO() # VariablesGroupUpdateDTO | Variables group description (optional)


try:
    # Update a variables group
    api_response = api_instance.update_variables_group(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->update_variables_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VariablesGroupUpdateDTO**](VariablesGroupUpdateDTO.md)| Variables group description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

