# opensilexClientToolsPython.DataverseApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**available_dataset_languages**](DataverseApi.md#available_dataset_languages) | **GET** /dataverse/datasetLanguages | Get the available dataset languages
[**available_dataset_metadata_languages**](DataverseApi.md#available_dataset_metadata_languages) | **GET** /dataverse/datasetMetadataLanguages | Get the available dataset metadata languages
[**create_dataset**](DataverseApi.md#create_dataset) | **POST** /dataverse | Create experiment as a Dataset
[**recherche_data_gouv_base_path**](DataverseApi.md#recherche_data_gouv_base_path) | **GET** /dataverse/RechercheDataGouvBasePath | Get the Recherche Data Gouv url from the instance configuration


# **available_dataset_languages**
> dict(str, object) available_dataset_languages(authorization, accept_language=accept_language)

Get the available dataset languages



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
api_instance = opensilexClientToolsPython.DataverseApi(pythonClient)


try:
    # Get the available dataset languages
    api_response = api_instance.available_dataset_languages()
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling DataverseApi->available_dataset_languages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **available_dataset_metadata_languages**
> dict(str, object) available_dataset_metadata_languages(authorization, accept_language=accept_language)

Get the available dataset metadata languages



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
api_instance = opensilexClientToolsPython.DataverseApi(pythonClient)


try:
    # Get the available dataset metadata languages
    api_response = api_instance.available_dataset_metadata_languages()
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling DataverseApi->available_dataset_metadata_languages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dataset**
> str create_dataset(experiment_uri, dataset_title, dataset_authors, dataset_contacts, dataset_language, dataset_metadata_language, dataset_rdf_type, authorization, production_date=production_date, dataset_uri=dataset_uri, dataset_deprecated=dataset_deprecated, dataverse_base_path=dataverse_base_path, dataverse_alias=dataverse_alias, external_api_key=external_api_key, accept_language=accept_language)

Create experiment as a Dataset

To consult the document created use the Document API

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
api_instance = opensilexClientToolsPython.DataverseApi(pythonClient)
experiment_uri = '\"dev:id/experiment/bc-test-release\"' # str | Experiment URI
dataset_title = '\"Test_dataset\"' # str | Dataset Title
dataset_authors = ['\"dev:id/user/person.test.dataverse\"'] # list[str] | Dataset Authors
dataset_contacts = ['\"dev:id/user/person.test.dataverse\"'] # list[str] | Dataset Contacts
dataset_language = '\"en\"' # str | Dataset Language from list of values : [en, fr]
dataset_metadata_language = '\"en\"' # str | Dataset Metadata Language from list of values : [en, fr]
dataset_rdf_type = '\"http://www.opensilex.org/vocabulary/oeso-dataverse#RechercheDataGouvDataset\"' # str | URI of the rdf_type of the dataset
production_date = '\"2020-02-20\"' # str | Dataset Production Date (optional)
dataset_uri = 'dataset_uri_example' # str | Dataset URI (optional)
dataset_deprecated = false # bool | Dataset deprecated (optional)
dataverse_base_path = 'dataverse_base_path_example' # str | Dataverse API base path (optional)
dataverse_alias = 'dataverse_alias_example' # str | Parent dataverse alias (optional)
external_api_key = 'external_api_key_example' # str | Dataverse API key (optional)


try:
    # Create experiment as a Dataset
    api_response = api_instance.create_dataset(experiment_uri, dataset_title, dataset_authors, dataset_contacts, dataset_language, dataset_metadata_language, dataset_rdf_type, production_date=production_date, dataset_uri=dataset_uri, dataset_deprecated=dataset_deprecated, dataverse_base_path=dataverse_base_path, dataverse_alias=dataverse_alias, external_api_key=external_api_key, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling DataverseApi->create_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_uri** | **str**| Experiment URI | 
 **dataset_title** | **str**| Dataset Title | 
 **dataset_authors** | [**list[str]**](str.md)| Dataset Authors | 
 **dataset_contacts** | [**list[str]**](str.md)| Dataset Contacts | 
 **dataset_language** | **str**| Dataset Language from list of values : [en, fr] | 
 **dataset_metadata_language** | **str**| Dataset Metadata Language from list of values : [en, fr] | 
 **dataset_rdf_type** | **str**| URI of the rdf_type of the dataset | 
 **production_date** | **str**| Dataset Production Date | [optional] 
 **dataset_uri** | **str**| Dataset URI | [optional] 
 **dataset_deprecated** | **bool**| Dataset deprecated | [optional] 
 **dataverse_base_path** | **str**| Dataverse API base path | [optional] 
 **dataverse_alias** | **str**| Parent dataverse alias | [optional] 
 **external_api_key** | **str**| Dataverse API key | [optional] 


### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recherche_data_gouv_base_path**
> str recherche_data_gouv_base_path(authorization, accept_language=accept_language)

Get the Recherche Data Gouv url from the instance configuration



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
api_instance = opensilexClientToolsPython.DataverseApi(pythonClient)


try:
    # Get the Recherche Data Gouv url from the instance configuration
    api_response = api_instance.recherche_data_gouv_base_path()
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling DataverseApi->recherche_data_gouv_base_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

