# opensilexClientToolsPython.BRAPIApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_calls**](BRAPIApi.md#get_calls) | **GET** /brapi/v1/calls | Check the available BrAPI calls
[**get_germplasm_by_search**](BRAPIApi.md#get_germplasm_by_search) | **GET** /brapi/v1/germplasm | Submit a search request for germplasm
[**get_observation_units**](BRAPIApi.md#get_observation_units) | **GET** /brapi/v1/studies/{studyDbId}/observationunits | List all the observation units measured in the study.
[**get_observation_variables**](BRAPIApi.md#get_observation_variables) | **GET** /brapi/v1/studies/{studyDbId}/observationvariables | List all the observation variables measured in the study.
[**get_observations**](BRAPIApi.md#get_observations) | **GET** /brapi/v1/studies/{studyDbId}/observations | Get the observations associated to a specific study
[**get_studies**](BRAPIApi.md#get_studies) | **GET** /brapi/v1/studies | Retrieve studies information
[**get_studies_search**](BRAPIApi.md#get_studies_search) | **GET** /brapi/v1/studies-search | Retrieve studies information
[**get_study_details**](BRAPIApi.md#get_study_details) | **GET** /brapi/v1/studies/{studyDbId} | Retrieve study details
[**get_variable_details**](BRAPIApi.md#get_variable_details) | **GET** /brapi/v1/variables/{observationVariableDbId} | Retrieve variable details by id
[**get_variables_list**](BRAPIApi.md#get_variables_list) | **GET** /brapi/v1/variables | Call to retrieve a list of observationVariables available in the system


# **get_calls**
> list[Call] get_calls(page=page, page_size=page_size, data_type=data_type)

Check the available BrAPI calls

Check the available BrAPI calls

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
api_instance = opensilexClientToolsPython.BRAPIApi(pythonClient)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)
data_type = '\"json\"' # str | datatype (optional)


try:
    # Check the available BrAPI calls
    api_response = api_instance.get_calls(page=page, page_size=page_size, data_type=data_type)
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling BRAPIApi->get_calls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]
 **data_type** | **str**| datatype | [optional] 


### Return type

[**list[Call]**](Call.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_germplasm_by_search**
> GermplasmDTO get_germplasm_by_search(authorization, germplasm_db_id=germplasm_db_id, germplasm_pui=germplasm_pui, germplasm_name=germplasm_name, common_crop_name=common_crop_name, page=page, page_size=page_size, accept_language=accept_language)

Submit a search request for germplasm



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
api_instance = opensilexClientToolsPython.BRAPIApi(pythonClient)
germplasm_db_id = 'germplasm_db_id_example' # str | Search by germplasmDbId (optional)
germplasm_pui = 'germplasm_pui_example' # str | Search by germplasmPUI (optional)
germplasm_name = 'germplasm_name_example' # str | Search by germplasmName (optional)
common_crop_name = 'common_crop_name_example' # str | Search by commonCropName (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Submit a search request for germplasm
    api_response = api_instance.get_germplasm_by_search(germplasm_db_id=germplasm_db_id, germplasm_pui=germplasm_pui, germplasm_name=germplasm_name, common_crop_name=common_crop_name, page=page, page_size=page_size, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling BRAPIApi->get_germplasm_by_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **germplasm_db_id** | **str**| Search by germplasmDbId | [optional] 
 **germplasm_pui** | **str**| Search by germplasmPUI | [optional] 
 **germplasm_name** | **str**| Search by germplasmName | [optional] 
 **common_crop_name** | **str**| Search by commonCropName | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**GermplasmDTO**](GermplasmDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_observation_units**
> list[ObservationUnitDTO] get_observation_units(study_db_id, authorization, observation_level=observation_level, page_size=page_size, page=page, accept_language=accept_language)

List all the observation units measured in the study.

List all the observation units measured in the study.

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
api_instance = opensilexClientToolsPython.BRAPIApi(pythonClient)
study_db_id = 'study_db_id_example' # str | studyDbId
observation_level = '\"Plot\"' # str | observationLevel (optional)
page_size = 20 # int | pageSize (optional) (default to 20)
page = 0 # int | page (optional) (default to 0)


try:
    # List all the observation units measured in the study.
    api_response = api_instance.get_observation_units(study_db_id, observation_level=observation_level, page_size=page_size, page=page, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling BRAPIApi->get_observation_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_db_id** | **str**| studyDbId | 
 **observation_level** | **str**| observationLevel | [optional] 
 **page_size** | **int**| pageSize | [optional] [default to 20]
 **page** | **int**| page | [optional] [default to 0]


### Return type

[**list[ObservationUnitDTO]**](ObservationUnitDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_observation_variables**
> list[ObservationVariableDTO] get_observation_variables(study_db_id, authorization, page_size=page_size, page=page, accept_language=accept_language)

List all the observation variables measured in the study.

List all the observation variables measured in the study.

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
api_instance = opensilexClientToolsPython.BRAPIApi(pythonClient)
study_db_id = 'study_db_id_example' # str | studyDbId
page_size = 20 # int | pageSize (optional) (default to 20)
page = 0 # int | page (optional) (default to 0)


try:
    # List all the observation variables measured in the study.
    api_response = api_instance.get_observation_variables(study_db_id, page_size=page_size, page=page, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling BRAPIApi->get_observation_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_db_id** | **str**| studyDbId | 
 **page_size** | **int**| pageSize | [optional] [default to 20]
 **page** | **int**| page | [optional] [default to 0]


### Return type

[**list[ObservationVariableDTO]**](ObservationVariableDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_observations**
> list[ObservationDTO] get_observations(study_db_id, authorization, observation_variable_db_ids=observation_variable_db_ids, page_size=page_size, page=page, accept_language=accept_language)

Get the observations associated to a specific study

Get the observations associated to a specific study

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
api_instance = opensilexClientToolsPython.BRAPIApi(pythonClient)
study_db_id = 'study_db_id_example' # str | studyDbId
observation_variable_db_ids = ['observation_variable_db_ids_example'] # list[str] | observationVariableDbIds (optional)
page_size = 20 # int | pageSize (optional) (default to 20)
page = 0 # int | page (optional) (default to 0)


try:
    # Get the observations associated to a specific study
    api_response = api_instance.get_observations(study_db_id, observation_variable_db_ids=observation_variable_db_ids, page_size=page_size, page=page, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling BRAPIApi->get_observations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_db_id** | **str**| studyDbId | 
 **observation_variable_db_ids** | [**list[str]**](str.md)| observationVariableDbIds | [optional] 
 **page_size** | **int**| pageSize | [optional] [default to 20]
 **page** | **int**| page | [optional] [default to 0]


### Return type

[**list[ObservationDTO]**](ObservationDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_studies**
> list[StudyDTO] get_studies(authorization, study_db_id=study_db_id, active=active, sort_by=sort_by, sort_order=sort_order, page=page, page_size=page_size, accept_language=accept_language)

Retrieve studies information

Retrieve studies information

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
api_instance = opensilexClientToolsPython.BRAPIApi(pythonClient)
study_db_id = 'study_db_id_example' # str | Search by studyDbId (optional)
active = 'active_example' # str | Filter active status true/false (optional)
sort_by = 'sort_by_example' # str | Name of the field to sort by: studyDbId, active (optional)
sort_order = 'sort_order_example' # str | Sort order direction - ASC or DESC (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Retrieve studies information
    api_response = api_instance.get_studies(study_db_id=study_db_id, active=active, sort_by=sort_by, sort_order=sort_order, page=page, page_size=page_size, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling BRAPIApi->get_studies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_db_id** | **str**| Search by studyDbId | [optional] 
 **active** | **str**| Filter active status true/false | [optional] 
 **sort_by** | **str**| Name of the field to sort by: studyDbId, active | [optional] 
 **sort_order** | **str**| Sort order direction - ASC or DESC | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[StudyDTO]**](StudyDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_studies_search**
> list[StudyDTO] get_studies_search(authorization, study_db_id=study_db_id, active=active, sort_by=sort_by, sort_order=sort_order, page_size=page_size, page=page, accept_language=accept_language)

Retrieve studies information

Retrieve studies information

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
api_instance = opensilexClientToolsPython.BRAPIApi(pythonClient)
study_db_id = 'study_db_id_example' # str | Search by studyDbId (optional)
active = 'active_example' # str | Filter active status true/false (optional)
sort_by = 'sort_by_example' # str | Name of the field to sort by: studyDbId or seasonDbId (optional)
sort_order = 'sort_order_example' # str | Sort order direction - ASC or DESC (optional)
page_size = 20 # int | pageSize (optional) (default to 20)
page = 0 # int | page (optional) (default to 0)


try:
    # Retrieve studies information
    api_response = api_instance.get_studies_search(study_db_id=study_db_id, active=active, sort_by=sort_by, sort_order=sort_order, page_size=page_size, page=page, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling BRAPIApi->get_studies_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_db_id** | **str**| Search by studyDbId | [optional] 
 **active** | **str**| Filter active status true/false | [optional] 
 **sort_by** | **str**| Name of the field to sort by: studyDbId or seasonDbId | [optional] 
 **sort_order** | **str**| Sort order direction - ASC or DESC | [optional] 
 **page_size** | **int**| pageSize | [optional] [default to 20]
 **page** | **int**| page | [optional] [default to 0]


### Return type

[**list[StudyDTO]**](StudyDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study_details**
> list[StudyDetailsDTO] get_study_details(study_db_id, authorization, accept_language=accept_language)

Retrieve study details

Retrieve study details

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
api_instance = opensilexClientToolsPython.BRAPIApi(pythonClient)
study_db_id = 'study_db_id_example' # str | Search by studyDbId


try:
    # Retrieve study details
    api_response = api_instance.get_study_details(study_db_id, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling BRAPIApi->get_study_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_db_id** | **str**| Search by studyDbId | 


### Return type

[**list[StudyDetailsDTO]**](StudyDetailsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variable_details**
> list[ObservationVariableDTO] get_variable_details(observation_variable_db_id, authorization, accept_language=accept_language)

Retrieve variable details by id

Retrieve variable details by id

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
api_instance = opensilexClientToolsPython.BRAPIApi(pythonClient)
observation_variable_db_id = 'observation_variable_db_id_example' # str | A variable URI (Unique Resource Identifier)


try:
    # Retrieve variable details by id
    api_response = api_instance.get_variable_details(observation_variable_db_id, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling BRAPIApi->get_variable_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observation_variable_db_id** | **str**| A variable URI (Unique Resource Identifier) | 


### Return type

[**list[ObservationVariableDTO]**](ObservationVariableDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variables_list**
> list[ObservationVariableDTO] get_variables_list(authorization, observation_variable_db_id=observation_variable_db_id, page_size=page_size, page=page, accept_language=accept_language)

Call to retrieve a list of observationVariables available in the system

retrieve variables information

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
api_instance = opensilexClientToolsPython.BRAPIApi(pythonClient)
observation_variable_db_id = 'observation_variable_db_id_example' # str | observationVariableDbId (optional)
page_size = 20 # int | pageSize (optional) (default to 20)
page = 0 # int | page (optional) (default to 0)


try:
    # Call to retrieve a list of observationVariables available in the system
    api_response = api_instance.get_variables_list(observation_variable_db_id=observation_variable_db_id, page_size=page_size, page=page, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling BRAPIApi->get_variables_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observation_variable_db_id** | **str**| observationVariableDbId | [optional] 
 **page_size** | **int**| pageSize | [optional] [default to 20]
 **page** | **int**| page | [optional] [default to 0]


### Return type

[**list[ObservationVariableDTO]**](ObservationVariableDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

