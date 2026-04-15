# opensilexClientToolsPython.LocationsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_locations**](LocationsApi.md#count_locations) | **GET** /core/locations/count | Count locations
[**search_location_history**](LocationsApi.md#search_location_history) | **GET** /core/locations/history | Search location history of an object
[**search_target_locations**](LocationsApi.md#search_target_locations) | **POST** /core/locations/targetLocations | Search the last geospatialized location of a target


# **count_locations**
> int count_locations(authorization, target=target, accept_language=accept_language)

Count locations



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
api_instance = opensilexClientToolsPython.LocationsApi(pythonClient)
target = 'http://www.opensilex.org/demo/2018/o18000076' # str | Target URI (optional)


try:
    # Count locations
    api_response = api_instance.count_locations(target=target, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling LocationsApi->count_locations: %s\n" % e)
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

# **search_location_history**
> list[LocationObservationDTO] search_location_history(target, authorization, start_date=start_date, end_date=end_date, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Search location history of an object



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
api_instance = opensilexClientToolsPython.LocationsApi(pythonClient)
target = 'http://www.opensilex.org/demo/2018/o18000076' # str | Target URI
start_date = '2019-09-08T12:00:00+01:00' # str | Start date : match position affected after the given start date (optional)
end_date = '2021-09-08T12:00:00+01:00' # str | End date : match position affected before the given end date (optional)
order_by = ['name=asc'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search location history of an object
    api_response = api_instance.search_location_history(target, start_date=start_date, end_date=end_date, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling LocationsApi->search_location_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | **str**| Target URI | 
 **start_date** | **str**| Start date : match position affected after the given start date | [optional] 
 **end_date** | **str**| End date : match position affected before the given end date | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[LocationObservationDTO]**](LocationObservationDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_target_locations**
> list[LocationObservationDTO] search_target_locations(authorization, body=body, base_type=base_type, end_date_time=end_date_time, accept_language=accept_language)

Search the last geospatialized location of a target



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
api_instance = opensilexClientToolsPython.LocationsApi(pythonClient)
body = opensilexClientToolsPython.GeoJsonObject() # GeoJsonObject | geometry GeoJSON (optional)
base_type = 'base_type_example' # str | target RDF Type URI (optional)
end_date_time = '2021-09-08T12:00:00+01:00' # str | End date : match position affected before the given end date (optional)


try:
    # Search the last geospatialized location of a target
    api_response = api_instance.search_target_locations(body=body, base_type=base_type, end_date_time=end_date_time, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling LocationsApi->search_target_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GeoJsonObject**](GeoJsonObject.md)| geometry GeoJSON | [optional] 
 **base_type** | **str**| target RDF Type URI | [optional] 
 **end_date_time** | **str**| End date : match position affected before the given end date | [optional] 


### Return type

[**list[LocationObservationDTO]**](LocationObservationDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

