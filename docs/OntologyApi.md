# opensilexClientToolsPython.OntologyApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_class_property_restriction**](OntologyApi.md#add_class_property_restriction) | **POST** /ontology/rdf_type_property_restriction | Add a rdf type property restriction
[**check_ur_is_types**](OntologyApi.md#check_ur_is_types) | **POST** /ontology/check_rdf_types | Check the given rdf-types on the given uris
[**create_property**](OntologyApi.md#create_property) | **POST** /ontology/property | Create a RDF property
[**delete_class_property_restriction**](OntologyApi.md#delete_class_property_restriction) | **DELETE** /ontology/rdf_type_property_restriction | Delete a rdf type property restriction
[**delete_property**](OntologyApi.md#delete_property) | **DELETE** /ontology/property | Delete a property
[**get_classes**](OntologyApi.md#get_classes) | **GET** /ontology/rdf_types | Return classes models definitions with properties for a list of rdf types
[**get_data_properties**](OntologyApi.md#get_data_properties) | **GET** /ontology/data_properties | Search data properties tree
[**get_linkable_properties**](OntologyApi.md#get_linkable_properties) | **GET** /ontology/linkable_properties | Search properties linkable to a domain
[**get_name_space**](OntologyApi.md#get_name_space) | **GET** /ontology/name_space | Return namespaces
[**get_object_properties**](OntologyApi.md#get_object_properties) | **GET** /ontology/object_properties | Search object properties tree
[**get_properties**](OntologyApi.md#get_properties) | **GET** /ontology/properties/{domain} | Search properties tree
[**get_property**](OntologyApi.md#get_property) | **GET** /ontology/property | Return property model definition detail
[**get_rdf_type**](OntologyApi.md#get_rdf_type) | **GET** /ontology/rdf_type | Return class model definition with properties
[**get_shared_resource_instances**](OntologyApi.md#get_shared_resource_instances) | **GET** /ontology/shared_resource_instances | Return the list of shared resource instances
[**get_sub_classes_of**](OntologyApi.md#get_sub_classes_of) | **GET** /ontology/subclasses_of | Search sub-classes tree of an RDF class
[**get_uri_label**](OntologyApi.md#get_uri_label) | **GET** /ontology/uri_label | Return associated rdfs:label of an uri if exists
[**get_uri_labels_list**](OntologyApi.md#get_uri_labels_list) | **GET** /ontology/uris_labels | Return associated rdfs:label of uris if they exist
[**get_uri_types**](OntologyApi.md#get_uri_types) | **GET** /ontology/uri_types | Return all rdf types of an uri
[**rename_uri**](OntologyApi.md#rename_uri) | **PUT** /ontology/{uri}/rename | Rename all occurrences of the given URI
[**search_sub_classes_of**](OntologyApi.md#search_sub_classes_of) | **GET** /ontology/subclasses_of/search | Search sub-classes tree of an RDF class
[**update_class_property_restriction**](OntologyApi.md#update_class_property_restriction) | **PUT** /ontology/rdf_type_property_restriction | Update a rdf type property restriction
[**update_property**](OntologyApi.md#update_property) | **PUT** /ontology/property | Update a RDF property


# **add_class_property_restriction**
> str add_class_property_restriction(authorization, body=body, accept_language=accept_language)

Add a rdf type property restriction



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
api_instance = opensilexClientToolsPython.OntologyApi(pythonClient)
body = opensilexClientToolsPython.OWLClassPropertyRestrictionDTO() # OWLClassPropertyRestrictionDTO | Property description (optional)


try:
    # Add a rdf type property restriction
    api_response = api_instance.add_class_property_restriction(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->add_class_property_restriction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OWLClassPropertyRestrictionDTO**](OWLClassPropertyRestrictionDTO.md)| Property description | [optional] 


### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_ur_is_types**
> list[URITypesDTO] check_ur_is_types(rdf_types, authorization, body=body, accept_language=accept_language)

Check the given rdf-types on the given uris



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
api_instance = opensilexClientToolsPython.OntologyApi(pythonClient)
rdf_types = ['rdf_types_example'] # list[str] | rdf_types list you want to check on the given uris list
body = opensilexClientToolsPython.URIsListPostDTO() # URIsListPostDTO | URIs list (optional)


try:
    # Check the given rdf-types on the given uris
    api_response = api_instance.check_ur_is_types(rdf_types, body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->check_ur_is_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rdf_types** | [**list[str]**](str.md)| rdf_types list you want to check on the given uris list | 
 **body** | [**URIsListPostDTO**](URIsListPostDTO.md)| URIs list | [optional] 


### Return type

[**list[URITypesDTO]**](URITypesDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_property**
> str create_property(authorization, body=body, accept_language=accept_language)

Create a RDF property



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
api_instance = opensilexClientToolsPython.OntologyApi(pythonClient)
body = opensilexClientToolsPython.RDFPropertyDTO() # RDFPropertyDTO | Property description (optional)


try:
    # Create a RDF property
    api_response = api_instance.create_property(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->create_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RDFPropertyDTO**](RDFPropertyDTO.md)| Property description | [optional] 


### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_class_property_restriction**
> str delete_class_property_restriction(rdf_type, property_uri, authorization, accept_language=accept_language)

Delete a rdf type property restriction



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
api_instance = opensilexClientToolsPython.OntologyApi(pythonClient)
rdf_type = 'rdf_type_example' # str | RDF type
property_uri = 'property_uri_example' # str | Property URI


try:
    # Delete a rdf type property restriction
    api_response = api_instance.delete_class_property_restriction(rdf_type, property_uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->delete_class_property_restriction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rdf_type** | **str**| RDF type | 
 **property_uri** | **str**| Property URI | 


### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_property**
> str delete_property(uri, rdf_type, authorization, accept_language=accept_language)

Delete a property



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
api_instance = opensilexClientToolsPython.OntologyApi(pythonClient)
uri = 'uri_example' # str | Property URI
rdf_type = 'rdf_type_example' # str | Property type


try:
    # Delete a property
    api_response = api_instance.delete_property(uri, rdf_type, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->delete_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Property URI | 
 **rdf_type** | **str**| Property type | 


### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_classes**
> list[RDFTypeDTO] get_classes(rdf_type, authorization, parent_type=parent_type, accept_language=accept_language)

Return classes models definitions with properties for a list of rdf types



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
api_instance = opensilexClientToolsPython.OntologyApi(pythonClient)
rdf_type = ['rdf_type_example'] # list[str] | RDF classes URI
parent_type = 'parent_type_example' # str | Parent RDF class URI (optional)


try:
    # Return classes models definitions with properties for a list of rdf types
    api_response = api_instance.get_classes(rdf_type, parent_type=parent_type, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->get_classes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rdf_type** | [**list[str]**](str.md)| RDF classes URI | 
 **parent_type** | **str**| Parent RDF class URI | [optional] 


### Return type

[**list[RDFTypeDTO]**](RDFTypeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_properties**
> list[ResourceTreeDTO] get_data_properties(authorization, domain=domain, name=name, accept_language=accept_language)

Search data properties tree



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
api_instance = opensilexClientToolsPython.OntologyApi(pythonClient)
domain = 'domain_example' # str | Domain URI (optional)
name = '\"plant_height\"' # str | Name regex pattern (optional)


try:
    # Search data properties tree
    api_response = api_instance.get_data_properties(domain=domain, name=name, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->get_data_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain URI | [optional] 
 **name** | **str**| Name regex pattern | [optional] 


### Return type

[**list[ResourceTreeDTO]**](ResourceTreeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linkable_properties**
> list[ResourceTreeDTO] get_linkable_properties(domain, authorization, parent=parent, accept_language=accept_language)

Search properties linkable to a domain



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
api_instance = opensilexClientToolsPython.OntologyApi(pythonClient)
domain = 'domain_example' # str | Domain URI
parent = 'parent_example' # str | Domain parent URI (optional)


try:
    # Search properties linkable to a domain
    api_response = api_instance.get_linkable_properties(domain, parent=parent, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->get_linkable_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain URI | 
 **parent** | **str**| Domain parent URI | [optional] 


### Return type

[**list[ResourceTreeDTO]**](ResourceTreeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_name_space**
> str get_name_space()

Return namespaces



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
api_instance = opensilexClientToolsPython.OntologyApi(pythonClient)


try:
    # Return namespaces
    api_response = api_instance.get_name_space()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->get_name_space: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.


### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_properties**
> list[ResourceTreeDTO] get_object_properties(authorization, domain=domain, name=name, accept_language=accept_language)

Search object properties tree



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
api_instance = opensilexClientToolsPython.OntologyApi(pythonClient)
domain = 'domain_example' # str | Domain URI (optional)
name = '\"plant_height\"' # str | Name regex pattern (optional)


try:
    # Search object properties tree
    api_response = api_instance.get_object_properties(domain=domain, name=name, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->get_object_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain URI | [optional] 
 **name** | **str**| Name regex pattern | [optional] 


### Return type

[**list[ResourceTreeDTO]**](ResourceTreeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_properties**
> list[ResourceTreeDTO] get_properties(domain, authorization, name=name, include_sub_classes=include_sub_classes, accept_language=accept_language)

Search properties tree



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
api_instance = opensilexClientToolsPython.OntologyApi(pythonClient)
domain = 'domain_example' # str | Domain URI
name = '\"plant_height\"' # str | Name regex pattern (optional)
include_sub_classes = true # bool | Return all properties from sub-classes (optional) (default to true)


try:
    # Search properties tree
    api_response = api_instance.get_properties(domain, name=name, include_sub_classes=include_sub_classes, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->get_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain URI | 
 **name** | **str**| Name regex pattern | [optional] 
 **include_sub_classes** | **bool**| Return all properties from sub-classes | [optional] [default to true]


### Return type

[**list[ResourceTreeDTO]**](ResourceTreeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_property**
> RDFPropertyGetDTO get_property(authorization, uri=uri, rdf_type=rdf_type, domain_rdf_type=domain_rdf_type, accept_language=accept_language)

Return property model definition detail



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
api_instance = opensilexClientToolsPython.OntologyApi(pythonClient)
uri = 'uri_example' # str | Property URI (optional)
rdf_type = 'rdf_type_example' # str | Property type (optional)
domain_rdf_type = 'domain_rdf_type_example' # str | Property type (optional)


try:
    # Return property model definition detail
    api_response = api_instance.get_property(uri=uri, rdf_type=rdf_type, domain_rdf_type=domain_rdf_type, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->get_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Property URI | [optional] 
 **rdf_type** | **str**| Property type | [optional] 
 **domain_rdf_type** | **str**| Property type | [optional] 


### Return type

[**RDFPropertyGetDTO**](RDFPropertyGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rdf_type**
> RDFTypeDTO get_rdf_type(rdf_type, authorization, parent_type=parent_type, accept_language=accept_language)

Return class model definition with properties



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
api_instance = opensilexClientToolsPython.OntologyApi(pythonClient)
rdf_type = 'rdf_type_example' # str | RDF type URI
parent_type = 'parent_type_example' # str | Parent RDF class URI (optional)


try:
    # Return class model definition with properties
    api_response = api_instance.get_rdf_type(rdf_type, parent_type=parent_type, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->get_rdf_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rdf_type** | **str**| RDF type URI | 
 **parent_type** | **str**| Parent RDF class URI | [optional] 


### Return type

[**RDFTypeDTO**](RDFTypeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_resource_instances**
> list[SharedResourceInstanceDTO] get_shared_resource_instances(authorization, accept_language=accept_language)

Return the list of shared resource instances



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
api_instance = opensilexClientToolsPython.OntologyApi(pythonClient)


try:
    # Return the list of shared resource instances
    api_response = api_instance.get_shared_resource_instances()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->get_shared_resource_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**list[SharedResourceInstanceDTO]**](SharedResourceInstanceDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sub_classes_of**
> list[ResourceTreeDTO] get_sub_classes_of(authorization, parent_type=parent_type, ignore_root_classes=ignore_root_classes, accept_language=accept_language)

Search sub-classes tree of an RDF class



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
api_instance = opensilexClientToolsPython.OntologyApi(pythonClient)
parent_type = 'parent_type_example' # str | Parent RDF class URI (optional)
ignore_root_classes = false # bool | Flag to determine if only sub-classes must be include in result (optional) (default to false)


try:
    # Search sub-classes tree of an RDF class
    api_response = api_instance.get_sub_classes_of(parent_type=parent_type, ignore_root_classes=ignore_root_classes, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->get_sub_classes_of: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_type** | **str**| Parent RDF class URI | [optional] 
 **ignore_root_classes** | **bool**| Flag to determine if only sub-classes must be include in result | [optional] [default to false]


### Return type

[**list[ResourceTreeDTO]**](ResourceTreeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_uri_label**
> str get_uri_label(uri, authorization, accept_language=accept_language)

Return associated rdfs:label of an uri if exists



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
api_instance = opensilexClientToolsPython.OntologyApi(pythonClient)
uri = 'uri_example' # str | URI to get label from


try:
    # Return associated rdfs:label of an uri if exists
    api_response = api_instance.get_uri_label(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->get_uri_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| URI to get label from | 


### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_uri_labels_list**
> list[NamedResourceDTO] get_uri_labels_list(uri, authorization, context=context, accept_language=accept_language)

Return associated rdfs:label of uris if they exist



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
api_instance = opensilexClientToolsPython.OntologyApi(pythonClient)
uri = ['uri_example'] # list[str] | URIs to get label from
context = 'context_example' # str | Context URI (optional)


try:
    # Return associated rdfs:label of uris if they exist
    api_response = api_instance.get_uri_labels_list(uri, context=context, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->get_uri_labels_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | [**list[str]**](str.md)| URIs to get label from | 
 **context** | **str**| Context URI | [optional] 


### Return type

[**list[NamedResourceDTO]**](NamedResourceDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_uri_types**
> URITypesDTO get_uri_types(uri, authorization, accept_language=accept_language)

Return all rdf types of an uri



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
api_instance = opensilexClientToolsPython.OntologyApi(pythonClient)
uri = ['uri_example'] # list[str] | URIs to get types from


try:
    # Return all rdf types of an uri
    api_response = api_instance.get_uri_types(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->get_uri_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | [**list[str]**](str.md)| URIs to get types from | 


### Return type

[**URITypesDTO**](URITypesDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_uri**
> rename_uri(uri, new_uri, authorization, accept_language=accept_language)

Rename all occurrences of the given URI

**This method should not be used unless you are fully understanding what you are doing, as it may have side-effects for external ontologies. Please note that occurrences of the URI will NOT be changed in the NoSQL database (MongoDB).**

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
api_instance = opensilexClientToolsPython.OntologyApi(pythonClient)
uri = 'uri_example' # str | The URI to rename
new_uri = 'new_uri_example' # str | The new URI


try:
    # Rename all occurrences of the given URI
    api_instance.rename_uri(uri, new_uri, )
except ApiException as e:
    print("Exception when calling OntologyApi->rename_uri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| The URI to rename | 
 **new_uri** | **str**| The new URI | 


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_sub_classes_of**
> list[ResourceTreeDTO] search_sub_classes_of(parent_type, authorization, name=name, ignore_root_classes=ignore_root_classes, accept_language=accept_language)

Search sub-classes tree of an RDF class



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
api_instance = opensilexClientToolsPython.OntologyApi(pythonClient)
parent_type = 'parent_type_example' # str | Parent RDF class URI
name = '\"plant_height\"' # str | Name regex pattern (optional)
ignore_root_classes = false # bool | Flag to determine if only sub-classes must be include in result (optional) (default to false)


try:
    # Search sub-classes tree of an RDF class
    api_response = api_instance.search_sub_classes_of(parent_type, name=name, ignore_root_classes=ignore_root_classes, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->search_sub_classes_of: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_type** | **str**| Parent RDF class URI | 
 **name** | **str**| Name regex pattern | [optional] 
 **ignore_root_classes** | **bool**| Flag to determine if only sub-classes must be include in result | [optional] [default to false]


### Return type

[**list[ResourceTreeDTO]**](ResourceTreeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_class_property_restriction**
> str update_class_property_restriction(authorization, body=body, accept_language=accept_language)

Update a rdf type property restriction



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
api_instance = opensilexClientToolsPython.OntologyApi(pythonClient)
body = opensilexClientToolsPython.OWLClassPropertyRestrictionDTO() # OWLClassPropertyRestrictionDTO | Property description (optional)


try:
    # Update a rdf type property restriction
    api_response = api_instance.update_class_property_restriction(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->update_class_property_restriction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OWLClassPropertyRestrictionDTO**](OWLClassPropertyRestrictionDTO.md)| Property description | [optional] 


### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_property**
> str update_property(authorization, body=body, accept_language=accept_language)

Update a RDF property



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
api_instance = opensilexClientToolsPython.OntologyApi(pythonClient)
body = opensilexClientToolsPython.RDFPropertyDTO() # RDFPropertyDTO | Property description (optional)


try:
    # Update a RDF property
    api_response = api_instance.update_property(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->update_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RDFPropertyDTO**](RDFPropertyDTO.md)| Property description | [optional] 


### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

