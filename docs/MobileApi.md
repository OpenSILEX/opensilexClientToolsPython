# opensilexClientToolsPython.MobileApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_form**](MobileApi.md#create_form) | **POST** /mobile/forms | Add a form
[**delete_form**](MobileApi.md#delete_form) | **DELETE** /mobile/{uri} | Delete form
[**search_form_list**](MobileApi.md#search_form_list) | **GET** /mobile | Search forms
[**update1**](MobileApi.md#update1) | **PUT** /mobile | Update form


# **create_form**
> ObjectUriResponse create_form(authorization, body=body, accept_language=accept_language)

Add a form



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
api_instance = opensilexClientToolsPython.MobileApi(pythonClient)
body = opensilexClientToolsPython.FormCreationDTO() # FormCreationDTO | Form to save (optional)


try:
    # Add a form
    api_response = api_instance.create_form(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->create_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FormCreationDTO**](FormCreationDTO.md)| Form to save | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_form**
> ObjectUriResponse delete_form(uri, authorization, accept_language=accept_language)

Delete form



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
api_instance = opensilexClientToolsPython.MobileApi(pythonClient)
uri = 'uri_example' # str | Form URI


try:
    # Delete form
    api_response = api_instance.delete_form(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->delete_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Form URI | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_form_list**
> list[FormGetDTO] search_form_list(authorization, uris=uris, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Search forms



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
api_instance = opensilexClientToolsPython.MobileApi(pythonClient)
uris = ['uris_example'] # list[str] | Search by uris (optional)
order_by = ['date=desc'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search forms
    api_response = api_instance.search_form_list(uris=uris, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->search_form_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uris** | [**list[str]**](str.md)| Search by uris | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[FormGetDTO]**](FormGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update1**
> ObjectUriResponse update1(authorization, body=body, accept_language=accept_language)

Update form



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
api_instance = opensilexClientToolsPython.MobileApi(pythonClient)
body = opensilexClientToolsPython.FormUpdateDTO() # FormUpdateDTO | Form description (optional)


try:
    # Update form
    api_response = api_instance.update1(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->update1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FormUpdateDTO**](FormUpdateDTO.md)| Form description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

