# opensilexClientToolsPython.AnnotationsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_annotations**](AnnotationsApi.md#count_annotations) | **GET** /core/annotations/count | Count annotations
[**create_annotation**](AnnotationsApi.md#create_annotation) | **POST** /core/annotations | Create an annotation
[**delete_annotation**](AnnotationsApi.md#delete_annotation) | **DELETE** /core/annotations/{uri} | Delete an annotation
[**get_annotation**](AnnotationsApi.md#get_annotation) | **GET** /core/annotations/{uri} | Get an annotation
[**search_annotations**](AnnotationsApi.md#search_annotations) | **GET** /core/annotations | Search annotations
[**search_motivations**](AnnotationsApi.md#search_motivations) | **GET** /core/annotations/motivations | Search motivations
[**update_annotation**](AnnotationsApi.md#update_annotation) | **PUT** /core/annotations | Update an annotation


# **count_annotations**
> int count_annotations(authorization, target=target, accept_language=accept_language)

Count annotations



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
api_instance = opensilexClientToolsPython.AnnotationsApi(pythonClient)
target = 'http://www.opensilex.org/demo/2018/o18000076' # str | Target URI (optional)


try:
    # Count annotations
    api_response = api_instance.count_annotations(target=target, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->count_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | **str**| Target URI | [optional] 


### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_annotation**
> ObjectUriResponse create_annotation(authorization, body=body, accept_language=accept_language)

Create an annotation



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
api_instance = opensilexClientToolsPython.AnnotationsApi(pythonClient)
body = opensilexClientToolsPython.AnnotationCreationDTO() # AnnotationCreationDTO |  (optional)


try:
    # Create an annotation
    api_response = api_instance.create_annotation(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->create_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnnotationCreationDTO**](AnnotationCreationDTO.md)|  | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_annotation**
> ObjectUriResponse delete_annotation(uri, authorization, accept_language=accept_language)

Delete an annotation



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
api_instance = opensilexClientToolsPython.AnnotationsApi(pythonClient)
uri = 'http://www.opensilex.org/annotations/12590c87-1c34-426b-a231-beb7acb33415' # str | Annotation URI


try:
    # Delete an annotation
    api_response = api_instance.delete_annotation(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->delete_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Annotation URI | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_annotation**
> AnnotationGetDTO get_annotation(uri, authorization, accept_language=accept_language)

Get an annotation



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
api_instance = opensilexClientToolsPython.AnnotationsApi(pythonClient)
uri = 'http://www.opensilex.org/annotations/12590c87-1c34-426b-a231-beb7acb33415' # str | Event URI


try:
    # Get an annotation
    api_response = api_instance.get_annotation(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->get_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Event URI | 


### Return type

[**AnnotationGetDTO**](AnnotationGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_annotations**
> list[AnnotationGetDTO] search_annotations(authorization, description=description, target=target, motivation=motivation, author=author, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Search annotations



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
api_instance = opensilexClientToolsPython.AnnotationsApi(pythonClient)
description = 'The pest attack' # str | Description (regex) (optional)
target = 'http://www.opensilex.org/demo/2018/o18000076' # str | Target URI (optional)
motivation = 'http://www.w3.org/ns/oa#describing' # str | Motivation URI (optional)
author = 'http://opensilex.dev/users#Admin.OpenSilex' # str | Author URI (optional)
order_by = ['name=asc'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search annotations
    api_response = api_instance.search_annotations(description=description, target=target, motivation=motivation, author=author, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->search_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| Description (regex) | [optional] 
 **target** | **str**| Target URI | [optional] 
 **motivation** | **str**| Motivation URI | [optional] 
 **author** | **str**| Author URI | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[AnnotationGetDTO]**](AnnotationGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_motivations**
> list[MotivationGetDTO] search_motivations(authorization, name=name, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Search motivations



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
api_instance = opensilexClientToolsPython.AnnotationsApi(pythonClient)
name = 'describing' # str | Motivation name regex pattern (optional)
order_by = ['name=asc'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search motivations
    api_response = api_instance.search_motivations(name=name, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->search_motivations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Motivation name regex pattern | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[MotivationGetDTO]**](MotivationGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_annotation**
> ObjectUriResponse update_annotation(authorization, body=body, accept_language=accept_language)

Update an annotation



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
api_instance = opensilexClientToolsPython.AnnotationsApi(pythonClient)
body = opensilexClientToolsPython.AnnotationUpdateDTO() # AnnotationUpdateDTO | Annotation description (optional)


try:
    # Update an annotation
    api_response = api_instance.update_annotation(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnotationsApi->update_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnnotationUpdateDTO**](AnnotationUpdateDTO.md)| Annotation description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

