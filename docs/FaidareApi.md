# opensilexClientToolsPython.FaidareApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_calls1**](FaidareApi.md#get_calls1) | **GET** /faidare/v1/calls | Check the available faidare calls
[**get_germplasms_by_search**](FaidareApi.md#get_germplasms_by_search) | **GET** /faidare/v1/germplasm | Submit a search request for germplasm
[**get_locations_list**](FaidareApi.md#get_locations_list) | **GET** /faidare/v1/locations | Faidarev1CallDTO to retrieve a list of locations available in the system
[**get_studies_list**](FaidareApi.md#get_studies_list) | **GET** /faidare/v1/studies | Retrieve studies information
[**get_trials_list**](FaidareApi.md#get_trials_list) | **GET** /faidare/v1/trials | Faidarev1CallDTO to retrieve a list of trials available in the system
[**get_variables_list1**](FaidareApi.md#get_variables_list1) | **GET** /faidare/v1/variables | Faidarev1CallDTO to retrieve a list of observationVariables available in the system


# **get_calls1**
> Faidarev1CallListResponse get_calls1(authorization, page=page, page_size=page_size, accept_language=accept_language)

Check the available faidare calls

Check the available faidare calls

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
api_instance = opensilexClientToolsPython.FaidareApi(pythonClient)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Check the available faidare calls
    api_response = api_instance.get_calls1(page=page, page_size=page_size, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling FaidareApi->get_calls1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**Faidarev1CallListResponse**](Faidarev1CallListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_germplasms_by_search**
> Faidarev1GermplasmListResponse get_germplasms_by_search(authorization, germplasm_db_id=germplasm_db_id, germplasm_pui=germplasm_pui, germplasm_name=germplasm_name, page=page, page_size=page_size, accept_language=accept_language)

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
api_instance = opensilexClientToolsPython.FaidareApi(pythonClient)
germplasm_db_id = 'germplasm_db_id_example' # str | Search by germplasmDbId (optional)
germplasm_pui = 'germplasm_pui_example' # str | Search by germplasmPUI (optional)
germplasm_name = 'germplasm_name_example' # str | Search by germplasmName (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Submit a search request for germplasm
    api_response = api_instance.get_germplasms_by_search(germplasm_db_id=germplasm_db_id, germplasm_pui=germplasm_pui, germplasm_name=germplasm_name, page=page, page_size=page_size, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling FaidareApi->get_germplasms_by_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **germplasm_db_id** | **str**| Search by germplasmDbId | [optional] 
 **germplasm_pui** | **str**| Search by germplasmPUI | [optional] 
 **germplasm_name** | **str**| Search by germplasmName | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**Faidarev1GermplasmListResponse**](Faidarev1GermplasmListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_locations_list**
> Faidarev1LocationListResponse get_locations_list(authorization, location_db_id=location_db_id, page=page, page_size=page_size, accept_language=accept_language)

Faidarev1CallDTO to retrieve a list of locations available in the system

retrieve locations information

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
api_instance = opensilexClientToolsPython.FaidareApi(pythonClient)
location_db_id = 'location_db_id_example' # str | Search by Location (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Faidarev1CallDTO to retrieve a list of locations available in the system
    api_response = api_instance.get_locations_list(location_db_id=location_db_id, page=page, page_size=page_size, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling FaidareApi->get_locations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_db_id** | **str**| Search by Location | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**Faidarev1LocationListResponse**](Faidarev1LocationListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_studies_list**
> Faidarev1StudyListResponse get_studies_list(authorization, study_db_id=study_db_id, page=page, page_size=page_size, accept_language=accept_language)

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
api_instance = opensilexClientToolsPython.FaidareApi(pythonClient)
study_db_id = 'study_db_id_example' # str | Search by studyDbId (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Retrieve studies information
    api_response = api_instance.get_studies_list(study_db_id=study_db_id, page=page, page_size=page_size, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling FaidareApi->get_studies_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_db_id** | **str**| Search by studyDbId | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**Faidarev1StudyListResponse**](Faidarev1StudyListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trials_list**
> Faidarev1TrialListResponse get_trials_list(authorization, page_size=page_size, page=page, accept_language=accept_language)

Faidarev1CallDTO to retrieve a list of trials available in the system

retrieve trials information

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
api_instance = opensilexClientToolsPython.FaidareApi(pythonClient)
page_size = 20 # int | pageSize (optional) (default to 20)
page = 0 # int | page (optional) (default to 0)


try:
    # Faidarev1CallDTO to retrieve a list of trials available in the system
    api_response = api_instance.get_trials_list(page_size=page_size, page=page, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling FaidareApi->get_trials_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| pageSize | [optional] [default to 20]
 **page** | **int**| page | [optional] [default to 0]


### Return type

[**Faidarev1TrialListResponse**](Faidarev1TrialListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variables_list1**
> Faidarev1ObservationVariableListResponse get_variables_list1(authorization, observation_variable_db_id=observation_variable_db_id, page_size=page_size, page=page, accept_language=accept_language)

Faidarev1CallDTO to retrieve a list of observationVariables available in the system

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
api_instance = opensilexClientToolsPython.FaidareApi(pythonClient)
observation_variable_db_id = 'observation_variable_db_id_example' # str | observationVariableDbId (optional)
page_size = 20 # int | pageSize (optional) (default to 20)
page = 0 # int | page (optional) (default to 0)


try:
    # Faidarev1CallDTO to retrieve a list of observationVariables available in the system
    api_response = api_instance.get_variables_list1(observation_variable_db_id=observation_variable_db_id, page_size=page_size, page=page, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling FaidareApi->get_variables_list1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observation_variable_db_id** | **str**| observationVariableDbId | [optional] 
 **page_size** | **int**| pageSize | [optional] [default to 20]
 **page** | **int**| page | [optional] [default to 0]


### Return type

[**Faidarev1ObservationVariableListResponse**](Faidarev1ObservationVariableListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

