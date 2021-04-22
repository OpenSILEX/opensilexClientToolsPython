# opensilexClientToolsPython.ProjectsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectsApi.md#create_project) | **POST** /core/projects | Add a project
[**delete_project**](ProjectsApi.md#delete_project) | **DELETE** /core/projects/{uri} | Delete a project
[**get_project**](ProjectsApi.md#get_project) | **GET** /core/projects/{uri} | Get a project
[**get_projects_by_uri**](ProjectsApi.md#get_projects_by_uri) | **GET** /core/projects/by_uris | Get projects by their URIs
[**search_projects**](ProjectsApi.md#search_projects) | **GET** /core/projects | Search projects
[**update_project**](ProjectsApi.md#update_project) | **PUT** /core/projects | Update a project


# **create_project**
> ObjectUriResponse create_project(authorization, body=body, accept_language=accept_language)

Add a project



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.ProjectsApi(pythonClient)
body = opensilexClientToolsPython.ProjectCreationDTO() # ProjectCreationDTO | Project description (optional)


try:
    # Add a project
    api_response = api_instance.create_project(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectCreationDTO**](ProjectCreationDTO.md)| Project description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> ObjectUriResponse delete_project(uri, authorization, accept_language=accept_language)

Delete a project



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.ProjectsApi(pythonClient)
uri = '\"http://opensilex/set/project/BW1\"' # str | Project URI


try:
    # Delete a project
    api_response = api_instance.delete_project(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Project URI | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> ProjectGetDetailDTO get_project(uri, authorization, accept_language=accept_language)

Get a project



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.ProjectsApi(pythonClient)
uri = '\"http://example.com/\"' # str | Project URI


try:
    # Get a project
    api_response = api_instance.get_project(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Project URI | 


### Return type

[**ProjectGetDetailDTO**](ProjectGetDetailDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects_by_uri**
> list[ProjectGetDTO] get_projects_by_uri(uris, authorization, accept_language=accept_language)

Get projects by their URIs



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.ProjectsApi(pythonClient)
uris = ['uris_example'] # list[str] | Projects URIs


try:
    # Get projects by their URIs
    api_response = api_instance.get_projects_by_uri(uris, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_projects_by_uri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uris** | [**list[str]**](str.md)| Projects URIs | 


### Return type

[**list[ProjectGetDTO]**](ProjectGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_projects**
> list[ProjectGetDTO] search_projects(authorization, name=name, year=year, keyword=keyword, financial_funding=financial_funding, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Search projects



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.ProjectsApi(pythonClient)
name = '\"PJ17\"' # str | Regex pattern for filtering by name or shortname (optional)
year = 2017 # int | Search by year (optional)
keyword = '\"climate\"' # str | Regex pattern for filtering on description or objective (optional)
financial_funding = '\"ANR\"' # str | Regex pattern for filtering by financial funding (optional)
order_by = ['\"name=asc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search projects
    api_response = api_instance.search_projects(name=name, year=year, keyword=keyword, financial_funding=financial_funding, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->search_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Regex pattern for filtering by name or shortname | [optional] 
 **year** | **int**| Search by year | [optional] 
 **keyword** | **str**| Regex pattern for filtering on description or objective | [optional] 
 **financial_funding** | **str**| Regex pattern for filtering by financial funding | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[ProjectGetDTO]**](ProjectGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> ObjectUriResponse update_project(authorization, body=body, accept_language=accept_language)

Update a project



### Example
```python
from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.ProjectsApi(pythonClient)
body = opensilexClientToolsPython.ProjectCreationDTO() # ProjectCreationDTO | Project description (optional)


try:
    # Update a project
    api_response = api_instance.update_project(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectCreationDTO**](ProjectCreationDTO.md)| Project description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

