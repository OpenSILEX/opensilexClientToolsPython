# opensilexClientToolsPython.DevicesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_device_data**](DevicesApi.md#count_device_data) | **GET** /core/devices/{uri}/data/count | Count device data
[**create_device**](DevicesApi.md#create_device) | **POST** /core/devices | Create a device
[**delete_device**](DevicesApi.md#delete_device) | **DELETE** /core/devices/{uri} | Delete a device
[**export_devices**](DevicesApi.md#export_devices) | **GET** /core/devices/export | export devices
[**export_geospatial1**](DevicesApi.md#export_geospatial1) | **POST** /core/devices/export_geospatial | Export a given list of devices URIs to shapefile
[**export_list**](DevicesApi.md#export_list) | **POST** /core/devices/export_by_uris | export devices
[**get_device**](DevicesApi.md#get_device) | **GET** /core/devices/{uri} | Get device detail
[**get_device_by_uris**](DevicesApi.md#get_device_by_uris) | **GET** /core/devices/by_uris | Get devices by uris
[**get_device_data_files_provenances**](DevicesApi.md#get_device_data_files_provenances) | **GET** /core/devices/{uri}/datafiles/provenances | Get provenances of datafiles linked to this device
[**get_device_data_provenances**](DevicesApi.md#get_device_data_provenances) | **GET** /core/devices/{uri}/data/provenances | Get provenances of data that have been measured on this device
[**get_device_variables**](DevicesApi.md#get_device_variables) | **GET** /core/devices/{uri}/variables | Get variables linked to the device
[**get_devices_by_facility**](DevicesApi.md#get_devices_by_facility) | **GET** /core/devices/{uri}/facility | Get devices by facility
[**import_csv**](DevicesApi.md#import_csv) | **POST** /core/devices/import | Import a CSV file with one device per line
[**search_device_data**](DevicesApi.md#search_device_data) | **GET** /core/devices/{uri}/data | Search device data
[**search_device_datafiles**](DevicesApi.md#search_device_datafiles) | **GET** /core/devices/{uri}/datafiles | Search device datafiles descriptions
[**search_devices**](DevicesApi.md#search_devices) | **GET** /core/devices | Search devices
[**update_device**](DevicesApi.md#update_device) | **PUT** /core/devices | Update a device
[**validate_csv1**](DevicesApi.md#validate_csv1) | **POST** /core/devices/import_validation | Validate the import of a CSV file with one device per line


# **count_device_data**
> int count_device_data(uri, authorization, start_date=start_date, end_date=end_date, timezone=timezone, experiment=experiment, variable=variable, min_confidence=min_confidence, max_confidence=max_confidence, provenance=provenance, metadata=metadata, operators=operators, accept_language=accept_language)

Count device data



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
api_instance = opensilexClientToolsPython.DevicesApi(pythonClient)
uri = 'http://example.com/' # str | Device URI
start_date = '2020-08-21T00:00:00+01:00' # str | Search by minimal date (optional)
end_date = '2020-09-21T00:00:00+01:00' # str | Search by maximal date (optional)
timezone = 'Europe/Paris' # str | Precise the timezone corresponding to the given dates (optional)
experiment = ['http://opensilex/experiment/id/ZA17'] # list[str] | Search by experiment uris (optional)
variable = ['http://opensilex.dev/variable#variable.2020-08-21_11-21-23entity6_method6_quality6_unit6'] # list[str] | Search by variables (optional)
min_confidence = 0.5 # float | Search by minimal confidence index (optional)
max_confidence = 0.5 # float | Search by maximal confidence index (optional)
provenance = ['http://opensilex.dev/provenance/1598001689415'] # list[str] | Search by provenance uri (optional)
metadata = '{ \"LabelView\" : \"side90\", \"paramA\" : \"90\"}' # str | Search by metadata (optional)
operators = ['dev:id/user/isa.droits'] # list[str] | Search by operators (optional)


try:
    # Count device data
    api_response = api_instance.count_device_data(uri, start_date=start_date, end_date=end_date, timezone=timezone, experiment=experiment, variable=variable, min_confidence=min_confidence, max_confidence=max_confidence, provenance=provenance, metadata=metadata, operators=operators, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling DevicesApi->count_device_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Device URI | 
 **start_date** | **str**| Search by minimal date | [optional] 
 **end_date** | **str**| Search by maximal date | [optional] 
 **timezone** | **str**| Precise the timezone corresponding to the given dates | [optional] 
 **experiment** | [**list[str]**](str.md)| Search by experiment uris | [optional] 
 **variable** | [**list[str]**](str.md)| Search by variables | [optional] 
 **min_confidence** | **float**| Search by minimal confidence index | [optional] 
 **max_confidence** | **float**| Search by maximal confidence index | [optional] 
 **provenance** | [**list[str]**](str.md)| Search by provenance uri | [optional] 
 **metadata** | **str**| Search by metadata | [optional] 
 **operators** | [**list[str]**](str.md)| Search by operators | [optional] 


### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device**
> str create_device(authorization, body=body, check_only=check_only, accept_language=accept_language)

Create a device



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
api_instance = opensilexClientToolsPython.DevicesApi(pythonClient)
body = opensilexClientToolsPython.DeviceCreationDTO() # DeviceCreationDTO | Device description (optional)
check_only = false # bool | Checking only (optional) (default to false)


try:
    # Create a device
    api_response = api_instance.create_device(body=body, check_only=check_only, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling DevicesApi->create_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceCreationDTO**](DeviceCreationDTO.md)| Device description | [optional] 
 **check_only** | **bool**| Checking only | [optional] [default to false]


### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device**
> str delete_device(uri, authorization, accept_language=accept_language)

Delete a device



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
api_instance = opensilexClientToolsPython.DevicesApi(pythonClient)
uri = 'http://opensilex.dev/set/device/sensingdevice-sensor_01' # str | Device URI


try:
    # Delete a device
    api_response = api_instance.delete_device(uri, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling DevicesApi->delete_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Device URI | 


### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_devices**
> export_devices(authorization, rdf_type=rdf_type, include_subtypes=include_subtypes, name=name, year=year, existence_date=existence_date, brand=brand, model=model, serial_number=serial_number, metadata=metadata, accept_language=accept_language)

export devices



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
api_instance = opensilexClientToolsPython.DevicesApi(pythonClient)
rdf_type = 'vocabulary:SensingDevice' # str | RDF type filter (optional)
include_subtypes = false # bool | Set this param to true when filtering on rdf_type to also retrieve sub-types (optional) (default to false)
name = '.*' # str | Regex pattern for filtering by name (optional) (default to .*)
year = 2017 # int | Search by year (optional)
existence_date = '2013-10-20' # date | Date to filter device existence (optional)
brand = '.*' # str | Regex pattern for filtering by brand (optional)
model = '.*' # str | Regex pattern for filtering by model (optional)
serial_number = '.*' # str | Regex pattern for filtering by serial number (optional)
metadata = '{ \"Group\" : \"weather station\", \"Group2\" : \"A\"}' # str | Search by metadata (optional)


try:
    # export devices
    api_instance.export_devices(rdf_type=rdf_type, include_subtypes=include_subtypes, name=name, year=year, existence_date=existence_date, brand=brand, model=model, serial_number=serial_number, metadata=metadata, )
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling DevicesApi->export_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rdf_type** | **str**| RDF type filter | [optional] 
 **include_subtypes** | **bool**| Set this param to true when filtering on rdf_type to also retrieve sub-types | [optional] [default to false]
 **name** | **str**| Regex pattern for filtering by name | [optional] [default to .*]
 **year** | **int**| Search by year | [optional] 
 **existence_date** | **date**| Date to filter device existence | [optional] 
 **brand** | **str**| Regex pattern for filtering by brand | [optional] 
 **model** | **str**| Regex pattern for filtering by model | [optional] 
 **serial_number** | **str**| Regex pattern for filtering by serial number | [optional] 
 **metadata** | **str**| Search by metadata | [optional] 


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_geospatial1**
> export_geospatial1(authorization, body=body, selected_props=selected_props, format=format, page_size=page_size, accept_language=accept_language)

Export a given list of devices URIs to shapefile



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
api_instance = opensilexClientToolsPython.DevicesApi(pythonClient)
body = [opensilexClientToolsPython.GeometryDTO()] # list[GeometryDTO] | Devices (optional)
selected_props = ['test'] # list[str] | properties selected (optional)
format = 'shp' # str | export format (shp/geojson) (optional)
page_size = 10000 # int | Page size limited to 10,000 objects (optional)


try:
    # Export a given list of devices URIs to shapefile
    api_instance.export_geospatial1(body=body, selected_props=selected_props, format=format, page_size=page_size, )
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling DevicesApi->export_geospatial1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[GeometryDTO]**](GeometryDTO.md)| Devices | [optional] 
 **selected_props** | [**list[str]**](str.md)| properties selected | [optional] 
 **format** | **str**| export format (shp/geojson) | [optional] 
 **page_size** | **int**| Page size limited to 10,000 objects | [optional] 


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_list**
> export_list(authorization, body=body, accept_language=accept_language)

export devices



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
api_instance = opensilexClientToolsPython.DevicesApi(pythonClient)
body = opensilexClientToolsPython.URIsListPostDTO() # URIsListPostDTO | List of device URI (optional)


try:
    # export devices
    api_instance.export_list(body=body, )
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling DevicesApi->export_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**URIsListPostDTO**](URIsListPostDTO.md)| List of device URI | [optional] 


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device**
> DeviceGetDetailsDTO get_device(uri, authorization, accept_language=accept_language)

Get device detail



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
api_instance = opensilexClientToolsPython.DevicesApi(pythonClient)
uri = 'http://opensilex.dev/set/device/sensingdevice-sensor_01' # str | device URI


try:
    # Get device detail
    api_response = api_instance.get_device(uri, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling DevicesApi->get_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| device URI | 


### Return type

[**DeviceGetDetailsDTO**](DeviceGetDetailsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_by_uris**
> list[DeviceGetDTO] get_device_by_uris(uris, authorization, accept_language=accept_language)

Get devices by uris



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
api_instance = opensilexClientToolsPython.DevicesApi(pythonClient)
uris = ['uris_example'] # list[str] | Device URIs


try:
    # Get devices by uris
    api_response = api_instance.get_device_by_uris(uris, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling DevicesApi->get_device_by_uris: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uris** | [**list[str]**](str.md)| Device URIs | 


### Return type

[**list[DeviceGetDTO]**](DeviceGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_data_files_provenances**
> list[ProvenanceGetDTO] get_device_data_files_provenances(uri, authorization, accept_language=accept_language)

Get provenances of datafiles linked to this device



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
api_instance = opensilexClientToolsPython.DevicesApi(pythonClient)
uri = 'http://example.com/' # str | Device URI


try:
    # Get provenances of datafiles linked to this device
    api_response = api_instance.get_device_data_files_provenances(uri, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling DevicesApi->get_device_data_files_provenances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Device URI | 


### Return type

[**list[ProvenanceGetDTO]**](ProvenanceGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_data_provenances**
> list[ProvenanceGetDTO] get_device_data_provenances(uri, authorization, accept_language=accept_language)

Get provenances of data that have been measured on this device



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
api_instance = opensilexClientToolsPython.DevicesApi(pythonClient)
uri = 'http://example.com/' # str | Device URI


try:
    # Get provenances of data that have been measured on this device
    api_response = api_instance.get_device_data_provenances(uri, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling DevicesApi->get_device_data_provenances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Device URI | 


### Return type

[**list[ProvenanceGetDTO]**](ProvenanceGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_variables**
> list[NamedResourceDTO] get_device_variables(uri, authorization, accept_language=accept_language)

Get variables linked to the device



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
api_instance = opensilexClientToolsPython.DevicesApi(pythonClient)
uri = 'http://opensilex.dev/set/device/sensingdevice-sensor_01' # str | Device URI


try:
    # Get variables linked to the device
    api_response = api_instance.get_device_variables(uri, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling DevicesApi->get_device_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Device URI | 


### Return type

[**list[NamedResourceDTO]**](NamedResourceDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices_by_facility**
> list[DeviceGetDTO] get_devices_by_facility(uri, authorization, accept_language=accept_language)

Get devices by facility



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
api_instance = opensilexClientToolsPython.DevicesApi(pythonClient)
uri = 'http://example.com/' # str | target URI


try:
    # Get devices by facility
    api_response = api_instance.get_devices_by_facility(uri, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling DevicesApi->get_devices_by_facility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| target URI | 


### Return type

[**list[DeviceGetDTO]**](DeviceGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_csv**
> CSVValidationDTO import_csv(description, file, authorization, accept_language=accept_language)

Import a CSV file with one device per line



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
api_instance = opensilexClientToolsPython.DevicesApi(pythonClient)
description = opensilexClientToolsPython.Object() # Object | CSV import settings
file = '/path/to/file.txt' # file | Device file


try:
    # Import a CSV file with one device per line
    api_response = api_instance.import_csv(description, file, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling DevicesApi->import_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | [**Object**](.md)| CSV import settings | 
 **file** | **file**| Device file | 


### Return type

[**CSVValidationDTO**](CSVValidationDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_device_data**
> list[DataGetDTO] search_device_data(uri, authorization, start_date=start_date, end_date=end_date, timezone=timezone, experiment=experiment, variable=variable, min_confidence=min_confidence, max_confidence=max_confidence, provenance=provenance, metadata=metadata, operators=operators, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Search device data



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
api_instance = opensilexClientToolsPython.DevicesApi(pythonClient)
uri = 'http://example.com/' # str | Device URI
start_date = '2020-08-21T00:00:00+01:00' # str | Search by minimal date (optional)
end_date = '2020-09-21T00:00:00+01:00' # str | Search by maximal date (optional)
timezone = 'Europe/Paris' # str | Precise the timezone corresponding to the given dates (optional)
experiment = ['http://opensilex/experiment/id/ZA17'] # list[str] | Search by experiment uris (optional)
variable = ['http://opensilex.dev/variable#variable.2020-08-21_11-21-23entity6_method6_quality6_unit6'] # list[str] | Search by variables (optional)
min_confidence = 0.5 # float | Search by minimal confidence index (optional)
max_confidence = 0.5 # float | Search by maximal confidence index (optional)
provenance = ['http://opensilex.dev/provenance/1598001689415'] # list[str] | Search by provenance uri (optional)
metadata = '{ \"LabelView\" : \"side90\", \"paramA\" : \"90\"}' # str | Search by metadata (optional)
operators = ['dev:id/user/isa.droits'] # list[str] | Search by operators (optional)
order_by = ['date=desc'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search device data
    api_response = api_instance.search_device_data(uri, start_date=start_date, end_date=end_date, timezone=timezone, experiment=experiment, variable=variable, min_confidence=min_confidence, max_confidence=max_confidence, provenance=provenance, metadata=metadata, operators=operators, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling DevicesApi->search_device_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Device URI | 
 **start_date** | **str**| Search by minimal date | [optional] 
 **end_date** | **str**| Search by maximal date | [optional] 
 **timezone** | **str**| Precise the timezone corresponding to the given dates | [optional] 
 **experiment** | [**list[str]**](str.md)| Search by experiment uris | [optional] 
 **variable** | [**list[str]**](str.md)| Search by variables | [optional] 
 **min_confidence** | **float**| Search by minimal confidence index | [optional] 
 **max_confidence** | **float**| Search by maximal confidence index | [optional] 
 **provenance** | [**list[str]**](str.md)| Search by provenance uri | [optional] 
 **metadata** | **str**| Search by metadata | [optional] 
 **operators** | [**list[str]**](str.md)| Search by operators | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[DataGetDTO]**](DataGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_device_datafiles**
> list[DataGetDTO] search_device_datafiles(uri, authorization, rdf_type=rdf_type, start_date=start_date, end_date=end_date, timezone=timezone, experiment=experiment, scientific_objects=scientific_objects, provenances=provenances, metadata=metadata, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Search device datafiles descriptions



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
api_instance = opensilexClientToolsPython.DevicesApi(pythonClient)
uri = 'http://example.com/' # str | Device URI
rdf_type = 'rdf_type_example' # str | Search by rdf type uri (optional)
start_date = '2020-08-21T00:00:00+01:00' # str | Search by minimal date (optional)
end_date = '2020-09-21T00:00:00+01:00' # str | Search by maximal date (optional)
timezone = 'Europe/Paris' # str | Precise the timezone corresponding to the given dates (optional)
experiment = ['http://opensilex/experiment/id/ZA17'] # list[str] | Search by experiments (optional)
scientific_objects = ['http://opensilex.dev/opensilex/2020/o20000345'] # list[str] | Search by object uris list (optional)
provenances = ['http://opensilex.dev/provenance/1598001689415'] # list[str] | Search by provenance uris list (optional)
metadata = '{ \"LabelView\" : \"side90\", \"paramA\" : \"90\"}' # str | Search by metadata (optional)
order_by = ['date=desc'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search device datafiles descriptions
    api_response = api_instance.search_device_datafiles(uri, rdf_type=rdf_type, start_date=start_date, end_date=end_date, timezone=timezone, experiment=experiment, scientific_objects=scientific_objects, provenances=provenances, metadata=metadata, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling DevicesApi->search_device_datafiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Device URI | 
 **rdf_type** | **str**| Search by rdf type uri | [optional] 
 **start_date** | **str**| Search by minimal date | [optional] 
 **end_date** | **str**| Search by maximal date | [optional] 
 **timezone** | **str**| Precise the timezone corresponding to the given dates | [optional] 
 **experiment** | [**list[str]**](str.md)| Search by experiments | [optional] 
 **scientific_objects** | [**list[str]**](str.md)| Search by object uris list | [optional] 
 **provenances** | [**list[str]**](str.md)| Search by provenance uris list | [optional] 
 **metadata** | **str**| Search by metadata | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[DataGetDTO]**](DataGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_devices**
> list[DeviceGetDTO] search_devices(authorization, rdf_type=rdf_type, include_subtypes=include_subtypes, name=name, variable=variable, year=year, existence_date=existence_date, facility=facility, brand=brand, model=model, serial_number=serial_number, metadata=metadata, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Search devices



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
api_instance = opensilexClientToolsPython.DevicesApi(pythonClient)
rdf_type = 'vocabulary:SensingDevice' # str | RDF type filter (optional)
include_subtypes = false # bool | Set this param to true when filtering on rdf_type to also retrieve sub-types (optional) (default to false)
name = '.*' # str | Regex pattern for filtering by name (optional) (default to .*)
variable = 'test:set/variables#air_temperature_thermocouple_degree-celsius' # str | Variable (optional)
year = 2017 # int | Search by year (optional)
existence_date = '2013-10-20' # date | Date to filter device existence (optional)
facility = 'http://example.com' # str | Search by facility (optional)
brand = '.*' # str | Regex pattern for filtering by brand (optional)
model = '.*' # str | Regex pattern for filtering by model (optional)
serial_number = '.*' # str | Regex pattern for filtering by serial number (optional)
metadata = '{ \"Group\" : \"weather station\", \"Group2\" : \"A\"}' # str | Search by metadata (optional)
order_by = ['uri=asc'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search devices
    api_response = api_instance.search_devices(rdf_type=rdf_type, include_subtypes=include_subtypes, name=name, variable=variable, year=year, existence_date=existence_date, facility=facility, brand=brand, model=model, serial_number=serial_number, metadata=metadata, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling DevicesApi->search_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rdf_type** | **str**| RDF type filter | [optional] 
 **include_subtypes** | **bool**| Set this param to true when filtering on rdf_type to also retrieve sub-types | [optional] [default to false]
 **name** | **str**| Regex pattern for filtering by name | [optional] [default to .*]
 **variable** | **str**| Variable | [optional] 
 **year** | **int**| Search by year | [optional] 
 **existence_date** | **date**| Date to filter device existence | [optional] 
 **facility** | **str**| Search by facility | [optional] 
 **brand** | **str**| Regex pattern for filtering by brand | [optional] 
 **model** | **str**| Regex pattern for filtering by model | [optional] 
 **serial_number** | **str**| Regex pattern for filtering by serial number | [optional] 
 **metadata** | **str**| Search by metadata | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[DeviceGetDTO]**](DeviceGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device**
> str update_device(body, authorization, accept_language=accept_language)

Update a device



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
api_instance = opensilexClientToolsPython.DevicesApi(pythonClient)
body = opensilexClientToolsPython.DeviceCreationDTO() # DeviceCreationDTO | Device description


try:
    # Update a device
    api_response = api_instance.update_device(body, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling DevicesApi->update_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceCreationDTO**](DeviceCreationDTO.md)| Device description | 


### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_csv1**
> CSVValidationDTO validate_csv1(description, file, authorization, accept_language=accept_language)

Validate the import of a CSV file with one device per line



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
api_instance = opensilexClientToolsPython.DevicesApi(pythonClient)
description = opensilexClientToolsPython.Object() # Object | CSV import settings
file = '/path/to/file.txt' # file | Device file


try:
    # Validate the import of a CSV file with one device per line
    api_response = api_instance.validate_csv1(description, file, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling DevicesApi->validate_csv1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | [**Object**](.md)| CSV import settings | 
 **file** | **file**| Device file | 


### Return type

[**CSVValidationDTO**](CSVValidationDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

