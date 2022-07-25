# opensilexClientToolsPython.MobileApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_form**](MobileApi.md#create_form) | **POST** /mobile/forms | Add a form
[**create_section**](MobileApi.md#create_section) | **POST** /mobile/sections | Add a section
[**delete_form**](MobileApi.md#delete_form) | **DELETE** /mobile/forms/{uri} | Delete form
[**delete_section**](MobileApi.md#delete_section) | **DELETE** /mobile/sections/{uri} | Delete section
[**import_csv_codes**](MobileApi.md#import_csv_codes) | **POST** /mobile/forms/import | Import a CSV file containing parent and child code-lots
[**search_forms**](MobileApi.md#search_forms) | **GET** /mobile/forms | Search forms
[**search_sections**](MobileApi.md#search_sections) | **GET** /mobile/sections | Search sections
[**update_form**](MobileApi.md#update_form) | **PUT** /mobile/forms | Update form
[**update_section**](MobileApi.md#update_section) | **PUT** /mobile/sections | Update section


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

# **create_section**
> ObjectUriResponse create_section(authorization, body=body, accept_language=accept_language)

Add a section



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
body = opensilexClientToolsPython.SectionCreationDTO() # SectionCreationDTO | Section to save (optional)


try:
    # Add a section
    api_response = api_instance.create_section(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->create_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SectionCreationDTO**](SectionCreationDTO.md)| Section to save | [optional] 


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
uri = 'uri_example' # str | CodeLot URI


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
 **uri** | **str**| CodeLot URI | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_section**
> ObjectUriResponse delete_section(uri, authorization, accept_language=accept_language)

Delete section



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
uri = 'uri_example' # str | Section URI


try:
    # Delete section
    api_response = api_instance.delete_section(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->delete_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Section URI | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_csv_codes**
> CodeLotCSVValidationDTO import_csv_codes(file, authorization, accept_language=accept_language)

Import a CSV file containing parent and child code-lots



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
file = '/path/to/file.txt' # file | File


try:
    # Import a CSV file containing parent and child code-lots
    api_response = api_instance.import_csv_codes(file, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->import_csv_codes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| File | 


### Return type

[**CodeLotCSVValidationDTO**](CodeLotCSVValidationDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_forms**
> list[FormGetDTO] search_forms(authorization, uris=uris, rdf_types=rdf_types, by_root=by_root, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

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
rdf_types = ['\"http://www.opensilex.org/vocabulary/iado#Harvest\"'] # list[str] | RDF types (optional)
by_root = true # bool | Get root forms only (optional)
order_by = ['\"date=desc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search forms
    api_response = api_instance.search_forms(uris=uris, rdf_types=rdf_types, by_root=by_root, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->search_forms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uris** | [**list[str]**](str.md)| Search by uris | [optional] 
 **rdf_types** | [**list[str]**](str.md)| RDF types | [optional] 
 **by_root** | **bool**| Get root forms only | [optional] 
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

# **search_sections**
> list[SectionGetDTO] search_sections(authorization, uris=uris, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Search sections



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
order_by = ['\"date=desc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search sections
    api_response = api_instance.search_sections(uris=uris, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->search_sections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uris** | [**list[str]**](str.md)| Search by uris | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[SectionGetDTO]**](SectionGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_form**
> ObjectUriResponse update_form(authorization, body=body, accept_language=accept_language)

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
    api_response = api_instance.update_form(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->update_form: %s\n" % e)
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

# **update_section**
> ObjectUriResponse update_section(authorization, body=body, accept_language=accept_language)

Update section



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
body = opensilexClientToolsPython.SectionUpdateDTO() # SectionUpdateDTO | Section description (optional)


try:
    # Update section
    api_response = api_instance.update_section(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->update_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SectionUpdateDTO**](SectionUpdateDTO.md)| Section description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

