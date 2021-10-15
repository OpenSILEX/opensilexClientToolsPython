# opensilexClientToolsPython.ExperimentsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_experiment**](ExperimentsApi.md#create_experiment) | **POST** /core/experiments | Add an experiment
[**delete_experiment**](ExperimentsApi.md#delete_experiment) | **DELETE** /core/experiments/{uri} | Delete an experiment
[**export_experiment_data_list**](ExperimentsApi.md#export_experiment_data_list) | **GET** /core/experiments/{uri}/data/export | export experiment data
[**get_available_facilities**](ExperimentsApi.md#get_available_facilities) | **GET** /core/experiments/{uri}/available_facilities | Get facilities available for an experiment
[**get_available_factors**](ExperimentsApi.md#get_available_factors) | **GET** /core/experiments/{uri}/factors | Get factors with their levels associated to an experiment
[**get_available_species**](ExperimentsApi.md#get_available_species) | **GET** /core/experiments/{uri}/species | Get species present in an experiment
[**get_experiment**](ExperimentsApi.md#get_experiment) | **GET** /core/experiments/{uri} | Get an experiment
[**get_experiments_by_ur_is**](ExperimentsApi.md#get_experiments_by_ur_is) | **GET** /core/experiments/by_uris | Get experiments URIs
[**get_facilities**](ExperimentsApi.md#get_facilities) | **GET** /core/experiments/{uri}/facilities | Get facilities involved in an experiment
[**get_used_variables1**](ExperimentsApi.md#get_used_variables1) | **GET** /core/experiments/{uri}/variables | Get variables involved in an experiment
[**import_csv_data1**](ExperimentsApi.md#import_csv_data1) | **POST** /core/experiments/{uri}/data/import | Import a CSV file for the given experiment URI and scientific object type.
[**search_experiment_data_list**](ExperimentsApi.md#search_experiment_data_list) | **GET** /core/experiments/{uri}/data | Search data
[**search_experiment_provenances**](ExperimentsApi.md#search_experiment_provenances) | **GET** /core/experiments/{uri}/provenances | Get provenances involved in an experiment
[**search_experiments**](ExperimentsApi.md#search_experiments) | **GET** /core/experiments | Search experiments
[**update_experiment**](ExperimentsApi.md#update_experiment) | **PUT** /core/experiments | Update an experiment
[**validate_csv1**](ExperimentsApi.md#validate_csv1) | **POST** /core/experiments/{uri}/data/import_validation | Import a CSV file for the given experiment URI and scientific object type.


# **create_experiment**
> ObjectUriResponse create_experiment(authorization, body=body, accept_language=accept_language)

Add an experiment



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
api_instance = opensilexClientToolsPython.ExperimentsApi(pythonClient)
body = opensilexClientToolsPython.ExperimentCreationDTO() # ExperimentCreationDTO | Experiment description (optional)


try:
    # Add an experiment
    api_response = api_instance.create_experiment(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentsApi->create_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExperimentCreationDTO**](ExperimentCreationDTO.md)| Experiment description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_experiment**
> ObjectUriResponse delete_experiment(uri, authorization, accept_language=accept_language)

Delete an experiment



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
api_instance = opensilexClientToolsPython.ExperimentsApi(pythonClient)
uri = 'http://opensilex/set/experiments/ZA17' # str | Experiment URI


try:
    # Delete an experiment
    api_response = api_instance.delete_experiment(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentsApi->delete_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Experiment URI | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_experiment_data_list**
> export_experiment_data_list(uri, authorization, start_date=start_date, end_date=end_date, timezone=timezone, scientific_objects=scientific_objects, variables=variables, min_confidence=min_confidence, max_confidence=max_confidence, provenance=provenance, metadata=metadata, mode=mode, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

export experiment data



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
api_instance = opensilexClientToolsPython.ExperimentsApi(pythonClient)
uri = 'http://opensilex/set/experiments/ZA17' # str | Experiment URI
start_date = '2020-08-21T00:00:00+01:00' # str | Search by minimal date (optional)
end_date = '2020-09-21T00:00:00+01:00' # str | Search by maximal date (optional)
timezone = 'Europe/Paris' # str | Precise the timezone corresponding to the given dates (optional)
scientific_objects = ['http://opensilex.dev/opensilex/2020/o20000345'] # list[str] | Search by objects (optional)
variables = ['http://opensilex.dev/variable#variable.2020-08-21_11-21-23entity6_method6_quality6_unit6'] # list[str] | Search by variables (optional)
min_confidence = 0.5 # float | Search by minimal confidence index (optional)
max_confidence = 0.5 # float | Search by maximal confidence index (optional)
provenance = 'http://opensilex.dev/provenance/1598001689415' # str | Search by provenance uri (optional)
metadata = '{ \"LabelView\" : \"side90\", \"paramA\" : \"90\"}' # str | Search by metadata (optional)
mode = 'wide' # str | Format wide or long (optional) (default to wide)
order_by = ['date=desc'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # export experiment data
    api_instance.export_experiment_data_list(uri, start_date=start_date, end_date=end_date, timezone=timezone, scientific_objects=scientific_objects, variables=variables, min_confidence=min_confidence, max_confidence=max_confidence, provenance=provenance, metadata=metadata, mode=mode, order_by=order_by, page=page, page_size=page_size, )
except ApiException as e:
    print("Exception when calling ExperimentsApi->export_experiment_data_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Experiment URI | 
 **start_date** | **str**| Search by minimal date | [optional] 
 **end_date** | **str**| Search by maximal date | [optional] 
 **timezone** | **str**| Precise the timezone corresponding to the given dates | [optional] 
 **scientific_objects** | [**list[str]**](str.md)| Search by objects | [optional] 
 **variables** | [**list[str]**](str.md)| Search by variables | [optional] 
 **min_confidence** | **float**| Search by minimal confidence index | [optional] 
 **max_confidence** | **float**| Search by maximal confidence index | [optional] 
 **provenance** | **str**| Search by provenance uri | [optional] 
 **metadata** | **str**| Search by metadata | [optional] 
 **mode** | **str**| Format wide or long | [optional] [default to wide]
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_facilities**
> list[InfrastructureFacilityGetDTO] get_available_facilities(uri, authorization, accept_language=accept_language)

Get facilities available for an experiment



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
api_instance = opensilexClientToolsPython.ExperimentsApi(pythonClient)
uri = 'http://opensilex/set/experiments/ZA17' # str | Experiment URI


try:
    # Get facilities available for an experiment
    api_response = api_instance.get_available_facilities(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentsApi->get_available_facilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Experiment URI | 


### Return type

[**list[InfrastructureFacilityGetDTO]**](InfrastructureFacilityGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_factors**
> list[FactorDetailsGetDTO] get_available_factors(uri, authorization, accept_language=accept_language)

Get factors with their levels associated to an experiment



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
api_instance = opensilexClientToolsPython.ExperimentsApi(pythonClient)
uri = 'http://opensilex/set/experiments/ZA17' # str | Experiment URI


try:
    # Get factors with their levels associated to an experiment
    api_response = api_instance.get_available_factors(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentsApi->get_available_factors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Experiment URI | 


### Return type

[**list[FactorDetailsGetDTO]**](FactorDetailsGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_species**
> list[SpeciesDTO] get_available_species(uri, authorization, accept_language=accept_language)

Get species present in an experiment



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
api_instance = opensilexClientToolsPython.ExperimentsApi(pythonClient)
uri = 'http://opensilex/set/experiments/ZA17' # str | Experiment URI


try:
    # Get species present in an experiment
    api_response = api_instance.get_available_species(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentsApi->get_available_species: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Experiment URI | 


### Return type

[**list[SpeciesDTO]**](SpeciesDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_experiment**
> ExperimentGetDTO get_experiment(uri, authorization, accept_language=accept_language)

Get an experiment



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
api_instance = opensilexClientToolsPython.ExperimentsApi(pythonClient)
uri = 'http://opensilex/set/experiments/ZA17' # str | Experiment URI


try:
    # Get an experiment
    api_response = api_instance.get_experiment(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentsApi->get_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Experiment URI | 


### Return type

[**ExperimentGetDTO**](ExperimentGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_experiments_by_ur_is**
> list[ExperimentGetListDTO] get_experiments_by_ur_is(uris, authorization, accept_language=accept_language)

Get experiments URIs



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
api_instance = opensilexClientToolsPython.ExperimentsApi(pythonClient)
uris = ['uris_example'] # list[str] | Experiments URIs


try:
    # Get experiments URIs
    api_response = api_instance.get_experiments_by_ur_is(uris, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentsApi->get_experiments_by_ur_is: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uris** | [**list[str]**](str.md)| Experiments URIs | 


### Return type

[**list[ExperimentGetListDTO]**](ExperimentGetListDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facilities**
> list[InfrastructureFacilityGetDTO] get_facilities(uri, authorization, accept_language=accept_language)

Get facilities involved in an experiment



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
api_instance = opensilexClientToolsPython.ExperimentsApi(pythonClient)
uri = 'http://opensilex/set/experiments/ZA17' # str | Experiment URI


try:
    # Get facilities involved in an experiment
    api_response = api_instance.get_facilities(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentsApi->get_facilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Experiment URI | 


### Return type

[**list[InfrastructureFacilityGetDTO]**](InfrastructureFacilityGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_used_variables1**
> list[NamedResourceDTO] get_used_variables1(uri, authorization, scientific_objects=scientific_objects, accept_language=accept_language)

Get variables involved in an experiment



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
api_instance = opensilexClientToolsPython.ExperimentsApi(pythonClient)
uri = 'http://opensilex/set/experiments/ZA17' # str | Experiment URI
scientific_objects = ['http://opensilex.dev/opensilex/2020/o20000345'] # list[str] | Search by objects uris (optional)


try:
    # Get variables involved in an experiment
    api_response = api_instance.get_used_variables1(uri, scientific_objects=scientific_objects, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentsApi->get_used_variables1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Experiment URI | 
 **scientific_objects** | [**list[str]**](str.md)| Search by objects uris | [optional] 


### Return type

[**list[NamedResourceDTO]**](NamedResourceDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_csv_data1**
> DataCSVValidationDTO import_csv_data1(uri, provenance, file, authorization, accept_language=accept_language)

Import a CSV file for the given experiment URI and scientific object type.



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
api_instance = opensilexClientToolsPython.ExperimentsApi(pythonClient)
uri = 'http://opensilex/set/experiments/ZA17' # str | Experiment URI
provenance = 'http://opensilex.dev/id/provenance/provenancelabel' # str | Provenance URI
file = '/path/to/file.txt' # file | Data file


try:
    # Import a CSV file for the given experiment URI and scientific object type.
    api_response = api_instance.import_csv_data1(uri, provenance, file, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentsApi->import_csv_data1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Experiment URI | 
 **provenance** | **str**| Provenance URI | 
 **file** | **file**| Data file | 


### Return type

[**DataCSVValidationDTO**](DataCSVValidationDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_experiment_data_list**
> list[DataGetDTO] search_experiment_data_list(uri, authorization, start_date=start_date, end_date=end_date, timezone=timezone, scientific_objects=scientific_objects, variables=variables, min_confidence=min_confidence, max_confidence=max_confidence, provenances=provenances, metadata=metadata, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Search data



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
api_instance = opensilexClientToolsPython.ExperimentsApi(pythonClient)
uri = 'http://opensilex/set/experiments/ZA17' # str | Experiment URI
start_date = '2020-08-21T00:00:00+01:00' # str | Search by minimal date (optional)
end_date = '2020-09-21T00:00:00+01:00' # str | Search by maximal date (optional)
timezone = 'Europe/Paris' # str | Precise the timezone corresponding to the given dates (optional)
scientific_objects = ['http://opensilex.dev/opensilex/2020/o20000345'] # list[str] | Search by objects (optional)
variables = ['http://opensilex.dev/variable#variable.2020-08-21_11-21-23entity6_method6_quality6_unit6'] # list[str] | Search by variables (optional)
min_confidence = 0.5 # float | Search by minimal confidence index (optional)
max_confidence = 0.5 # float | Search by maximal confidence index (optional)
provenances = ['http://opensilex.dev/provenance/1598001689415'] # list[str] | Search by provenance uri (optional)
metadata = '{ \"LabelView\" : \"side90\", \"paramA\" : \"90\"}' # str | Search by metadata (optional)
order_by = ['date=desc'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search data
    api_response = api_instance.search_experiment_data_list(uri, start_date=start_date, end_date=end_date, timezone=timezone, scientific_objects=scientific_objects, variables=variables, min_confidence=min_confidence, max_confidence=max_confidence, provenances=provenances, metadata=metadata, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentsApi->search_experiment_data_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Experiment URI | 
 **start_date** | **str**| Search by minimal date | [optional] 
 **end_date** | **str**| Search by maximal date | [optional] 
 **timezone** | **str**| Precise the timezone corresponding to the given dates | [optional] 
 **scientific_objects** | [**list[str]**](str.md)| Search by objects | [optional] 
 **variables** | [**list[str]**](str.md)| Search by variables | [optional] 
 **min_confidence** | **float**| Search by minimal confidence index | [optional] 
 **max_confidence** | **float**| Search by maximal confidence index | [optional] 
 **provenances** | [**list[str]**](str.md)| Search by provenance uri | [optional] 
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

# **search_experiment_provenances**
> list[ProvenanceGetDTO] search_experiment_provenances(uri, authorization, name=name, description=description, activity=activity, activity_type=activity_type, agent=agent, agent_type=agent_type, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Get provenances involved in an experiment



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
api_instance = opensilexClientToolsPython.ExperimentsApi(pythonClient)
uri = 'http://opensilex/set/experiments/ZA17' # str | Experiment URI
name = 'name_example' # str | Regex pattern for filtering by name (optional)
description = 'description_example' # str | Search by description (optional)
activity = 'activity_example' # str | Search by activity URI (optional)
activity_type = 'activity_type_example' # str | Search by activity type (optional)
agent = 'agent_example' # str | Search by agent URI (optional)
agent_type = 'agent_type_example' # str | Search by agent type (optional)
order_by = ['date=desc'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Get provenances involved in an experiment
    api_response = api_instance.search_experiment_provenances(uri, name=name, description=description, activity=activity, activity_type=activity_type, agent=agent, agent_type=agent_type, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentsApi->search_experiment_provenances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Experiment URI | 
 **name** | **str**| Regex pattern for filtering by name | [optional] 
 **description** | **str**| Search by description | [optional] 
 **activity** | **str**| Search by activity URI | [optional] 
 **activity_type** | **str**| Search by activity type | [optional] 
 **agent** | **str**| Search by agent URI | [optional] 
 **agent_type** | **str**| Search by agent type | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[ProvenanceGetDTO]**](ProvenanceGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_experiments**
> list[ExperimentGetListDTO] search_experiments(authorization, name=name, year=year, is_ended=is_ended, species=species, factors=factors, projects=projects, is_public=is_public, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Search experiments



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
api_instance = opensilexClientToolsPython.ExperimentsApi(pythonClient)
name = 'ZA17' # str | Regex pattern for filtering by name (optional)
year = 2017 # int | Search by year (optional)
is_ended = true # bool | Search ended(false) or active experiments(true) (optional)
species = ['http://www.phenome-fppn.fr/id/species/zeamays'] # list[str] | Search by involved species (optional)
factors = ['http://purl.obolibrary.org/obo/CHEBI_25555'] # list[str] | Search by studied effect (optional)
projects = ['http://www.phenome-fppn.fr/projects/ZA17 http://www.phenome-fppn.fr/id/projects/ZA18'] # list[str] | Search by related project uri (optional)
is_public = true # bool | Search private(false) or public experiments(true) (optional)
order_by = ['uri=asc'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search experiments
    api_response = api_instance.search_experiments(name=name, year=year, is_ended=is_ended, species=species, factors=factors, projects=projects, is_public=is_public, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentsApi->search_experiments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Regex pattern for filtering by name | [optional] 
 **year** | **int**| Search by year | [optional] 
 **is_ended** | **bool**| Search ended(false) or active experiments(true) | [optional] 
 **species** | [**list[str]**](str.md)| Search by involved species | [optional] 
 **factors** | [**list[str]**](str.md)| Search by studied effect | [optional] 
 **projects** | [**list[str]**](str.md)| Search by related project uri | [optional] 
 **is_public** | **bool**| Search private(false) or public experiments(true) | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[ExperimentGetListDTO]**](ExperimentGetListDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_experiment**
> ObjectUriResponse update_experiment(authorization, body=body, accept_language=accept_language)

Update an experiment



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
api_instance = opensilexClientToolsPython.ExperimentsApi(pythonClient)
body = opensilexClientToolsPython.ExperimentCreationDTO() # ExperimentCreationDTO | Experiment description (optional)


try:
    # Update an experiment
    api_response = api_instance.update_experiment(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentsApi->update_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExperimentCreationDTO**](ExperimentCreationDTO.md)| Experiment description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_csv1**
> DataCSVValidationDTO validate_csv1(uri, provenance, file, authorization, accept_language=accept_language)

Import a CSV file for the given experiment URI and scientific object type.



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
api_instance = opensilexClientToolsPython.ExperimentsApi(pythonClient)
uri = 'http://opensilex/set/experiments/ZA17' # str | Experiment URI
provenance = 'http://opensilex.dev/id/provenance/provenancelabel' # str | Provenance URI
file = '/path/to/file.txt' # file | Data file


try:
    # Import a CSV file for the given experiment URI and scientific object type.
    api_response = api_instance.validate_csv1(uri, provenance, file, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentsApi->validate_csv1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Experiment URI | 
 **provenance** | **str**| Provenance URI | 
 **file** | **file**| Data file | 


### Return type

[**DataCSVValidationDTO**](DataCSVValidationDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

