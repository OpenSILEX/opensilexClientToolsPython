# opensilexClientToolsPython.OrganisationsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_infrastructure**](OrganisationsApi.md#create_infrastructure) | **POST** /core/organisations | Create an organisation
[**create_infrastructure_facility**](OrganisationsApi.md#create_infrastructure_facility) | **POST** /core/facilities | Create a facility
[**create_infrastructure_team**](OrganisationsApi.md#create_infrastructure_team) | **POST** /core/teams | Create a team
[**delete_infrastructure**](OrganisationsApi.md#delete_infrastructure) | **DELETE** /core/organisations/{uri} | Delete an organisation
[**delete_infrastructure_facility**](OrganisationsApi.md#delete_infrastructure_facility) | **DELETE** /core/facilities/{uri} | Delete a facility
[**delete_infrastructure_team**](OrganisationsApi.md#delete_infrastructure_team) | **DELETE** /core/teams/{uri} | Delete a team
[**get_all_facilities**](OrganisationsApi.md#get_all_facilities) | **GET** /core/facilities/all_facilities | Get all facilities
[**get_facilities_by_uri**](OrganisationsApi.md#get_facilities_by_uri) | **GET** /core/facilities/by_uris | Get facilities by their URIs
[**get_infrastructure**](OrganisationsApi.md#get_infrastructure) | **GET** /core/organisations/{uri} | Get an organisation 
[**get_infrastructure_facility**](OrganisationsApi.md#get_infrastructure_facility) | **GET** /core/facilities/{uri} | Get a facility
[**get_infrastructure_team**](OrganisationsApi.md#get_infrastructure_team) | **GET** /core/teams/{uri} | Get a team
[**search_infrastructure_facilities**](OrganisationsApi.md#search_infrastructure_facilities) | **GET** /core/facilities | Search facilities
[**search_infrastructures_tree**](OrganisationsApi.md#search_infrastructures_tree) | **GET** /core/organisations | Search organisations
[**update_infrastructure**](OrganisationsApi.md#update_infrastructure) | **PUT** /core/organisations | Update an organisation
[**update_infrastructure_facility**](OrganisationsApi.md#update_infrastructure_facility) | **PUT** /core/facilities | Update a facility
[**update_infrastructure_team**](OrganisationsApi.md#update_infrastructure_team) | **PUT** /core/teams | Update a team


# **create_infrastructure**
> ObjectUriResponse create_infrastructure(authorization, body=body, accept_language=accept_language)

Create an organisation



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
api_instance = opensilexClientToolsPython.OrganisationsApi(pythonClient)
body = opensilexClientToolsPython.InfrastructureCreationDTO() # InfrastructureCreationDTO | Organisation description (optional)


try:
    # Create an organisation
    api_response = api_instance.create_infrastructure(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->create_infrastructure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfrastructureCreationDTO**](InfrastructureCreationDTO.md)| Organisation description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_infrastructure_facility**
> ObjectUriResponse create_infrastructure_facility(authorization, body=body, accept_language=accept_language)

Create a facility



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
api_instance = opensilexClientToolsPython.OrganisationsApi(pythonClient)
body = opensilexClientToolsPython.InfrastructureFacilityCreationDTO() # InfrastructureFacilityCreationDTO | Facility description (optional)


try:
    # Create a facility
    api_response = api_instance.create_infrastructure_facility(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->create_infrastructure_facility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfrastructureFacilityCreationDTO**](InfrastructureFacilityCreationDTO.md)| Facility description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_infrastructure_team**
> ObjectUriResponse create_infrastructure_team(authorization, body=body, accept_language=accept_language)

Create a team



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
api_instance = opensilexClientToolsPython.OrganisationsApi(pythonClient)
body = opensilexClientToolsPython.InfrastructureTeamDTO() # InfrastructureTeamDTO | Team description (optional)


try:
    # Create a team
    api_response = api_instance.create_infrastructure_team(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->create_infrastructure_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfrastructureTeamDTO**](InfrastructureTeamDTO.md)| Team description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_infrastructure**
> ObjectUriResponse delete_infrastructure(uri, authorization, accept_language=accept_language)

Delete an organisation



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
api_instance = opensilexClientToolsPython.OrganisationsApi(pythonClient)
uri = 'http://example.com/' # str | Organisation URI


try:
    # Delete an organisation
    api_response = api_instance.delete_infrastructure(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->delete_infrastructure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Organisation URI | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_infrastructure_facility**
> ObjectUriResponse delete_infrastructure_facility(uri, authorization, accept_language=accept_language)

Delete a facility



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
api_instance = opensilexClientToolsPython.OrganisationsApi(pythonClient)
uri = 'http://example.com/' # str | Facility URI


try:
    # Delete a facility
    api_response = api_instance.delete_infrastructure_facility(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->delete_infrastructure_facility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Facility URI | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_infrastructure_team**
> ObjectUriResponse delete_infrastructure_team(uri, authorization, accept_language=accept_language)

Delete a team



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
api_instance = opensilexClientToolsPython.OrganisationsApi(pythonClient)
uri = 'http://example.com/' # str | Team URI


try:
    # Delete a team
    api_response = api_instance.delete_infrastructure_team(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->delete_infrastructure_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Team URI | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_facilities**
> list[NamedResourceDTO] get_all_facilities(authorization, accept_language=accept_language)

Get all facilities



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
api_instance = opensilexClientToolsPython.OrganisationsApi(pythonClient)


try:
    # Get all facilities
    api_response = api_instance.get_all_facilities()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->get_all_facilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**list[NamedResourceDTO]**](NamedResourceDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facilities_by_uri**
> list[InfrastructureFacilityNamedDTO] get_facilities_by_uri(uris, authorization, accept_language=accept_language)

Get facilities by their URIs



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
api_instance = opensilexClientToolsPython.OrganisationsApi(pythonClient)
uris = ['uris_example'] # list[str] | Facilities URIs


try:
    # Get facilities by their URIs
    api_response = api_instance.get_facilities_by_uri(uris, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->get_facilities_by_uri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uris** | [**list[str]**](str.md)| Facilities URIs | 


### Return type

[**list[InfrastructureFacilityNamedDTO]**](InfrastructureFacilityNamedDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_infrastructure**
> InfrastructureGetDTO get_infrastructure(uri, authorization, accept_language=accept_language)

Get an organisation 



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
api_instance = opensilexClientToolsPython.OrganisationsApi(pythonClient)
uri = 'http://opensilex.dev/organisation/phenoarch' # str | Organisation URI


try:
    # Get an organisation 
    api_response = api_instance.get_infrastructure(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->get_infrastructure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Organisation URI | 


### Return type

[**InfrastructureGetDTO**](InfrastructureGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_infrastructure_facility**
> InfrastructureFacilityGetDTO get_infrastructure_facility(uri, authorization, accept_language=accept_language)

Get a facility



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
api_instance = opensilexClientToolsPython.OrganisationsApi(pythonClient)
uri = 'http://opensilex.dev/organisations/facility/phenoarch' # str | facility URI


try:
    # Get a facility
    api_response = api_instance.get_infrastructure_facility(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->get_infrastructure_facility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| facility URI | 


### Return type

[**InfrastructureFacilityGetDTO**](InfrastructureFacilityGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_infrastructure_team**
> InfrastructureTeamDTO get_infrastructure_team(uri, authorization, accept_language=accept_language)

Get a team



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
api_instance = opensilexClientToolsPython.OrganisationsApi(pythonClient)
uri = 'http://example.com/' # str | Team URI


try:
    # Get a team
    api_response = api_instance.get_infrastructure_team(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->get_infrastructure_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Team URI | 


### Return type

[**InfrastructureTeamDTO**](InfrastructureTeamDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_infrastructure_facilities**
> list[InfrastructureFacilityNamedDTO] search_infrastructure_facilities(authorization, pattern=pattern, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Search facilities



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
api_instance = opensilexClientToolsPython.OrganisationsApi(pythonClient)
pattern = '.*' # str | Regex pattern for filtering facilities by names (optional) (default to .*)
order_by = ['order_by_example'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 56 # int | Page number (optional)
page_size = 56 # int | Page size (optional)


try:
    # Search facilities
    api_response = api_instance.search_infrastructure_facilities(pattern=pattern, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->search_infrastructure_facilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern** | **str**| Regex pattern for filtering facilities by names | [optional] [default to .*]
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] 
 **page_size** | **int**| Page size | [optional] 


### Return type

[**list[InfrastructureFacilityNamedDTO]**](InfrastructureFacilityNamedDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_infrastructures_tree**
> list[ResourceTreeDTO] search_infrastructures_tree(authorization, pattern=pattern, organisation_uris=organisation_uris, accept_language=accept_language)

Search organisations



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
api_instance = opensilexClientToolsPython.OrganisationsApi(pythonClient)
pattern = '.*' # str | Regex pattern for filtering list by names (optional) (default to .*)
organisation_uris = ['organisation_uris_example'] # list[str] |  organisation URIs (optional)


try:
    # Search organisations
    api_response = api_instance.search_infrastructures_tree(pattern=pattern, organisation_uris=organisation_uris, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->search_infrastructures_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern** | **str**| Regex pattern for filtering list by names | [optional] [default to .*]
 **organisation_uris** | [**list[str]**](str.md)|  organisation URIs | [optional] 


### Return type

[**list[ResourceTreeDTO]**](ResourceTreeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_infrastructure**
> ObjectUriResponse update_infrastructure(authorization, body=body, accept_language=accept_language)

Update an organisation



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
api_instance = opensilexClientToolsPython.OrganisationsApi(pythonClient)
body = opensilexClientToolsPython.InfrastructureUpdateDTO() # InfrastructureUpdateDTO | Organisation description (optional)


try:
    # Update an organisation
    api_response = api_instance.update_infrastructure(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->update_infrastructure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfrastructureUpdateDTO**](InfrastructureUpdateDTO.md)| Organisation description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_infrastructure_facility**
> ObjectUriResponse update_infrastructure_facility(authorization, body=body, accept_language=accept_language)

Update a facility



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
api_instance = opensilexClientToolsPython.OrganisationsApi(pythonClient)
body = opensilexClientToolsPython.InfrastructureFacilityUpdateDTO() # InfrastructureFacilityUpdateDTO | Facility description (optional)


try:
    # Update a facility
    api_response = api_instance.update_infrastructure_facility(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->update_infrastructure_facility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfrastructureFacilityUpdateDTO**](InfrastructureFacilityUpdateDTO.md)| Facility description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_infrastructure_team**
> ObjectUriResponse update_infrastructure_team(authorization, body=body, accept_language=accept_language)

Update a team



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
api_instance = opensilexClientToolsPython.OrganisationsApi(pythonClient)
body = opensilexClientToolsPython.InfrastructureTeamDTO() # InfrastructureTeamDTO | Team description (optional)


try:
    # Update a team
    api_response = api_instance.update_infrastructure_team(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->update_infrastructure_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InfrastructureTeamDTO**](InfrastructureTeamDTO.md)| Team description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

