# opensilexClientToolsPython.MetricsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_experiment_summary_history**](MetricsApi.md#get_experiment_summary_history) | **GET** /core/metrics/experiment/{uri} | Get an experiment summary history
[**get_running_experiments_summary**](MetricsApi.md#get_running_experiments_summary) | **GET** /core/metrics/running_experiments | Get running experiments metrics
[**get_system_metrics**](MetricsApi.md#get_system_metrics) | **GET** /core/metrics/system | Get system metrics
[**get_system_metrics_summary**](MetricsApi.md#get_system_metrics_summary) | **GET** /core/metrics/system/summary | Get system metrics summary


# **get_experiment_summary_history**
> MetricDTO get_experiment_summary_history(uri, authorization, start_date=start_date, end_date=end_date, page=page, page_size=page_size, accept_language=accept_language)

Get an experiment summary history



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
api_instance = opensilexClientToolsPython.MetricsApi(pythonClient)
uri = '\"http://opensilex/set/experiments/ZA17\"' # str | Metrics URI
start_date = '\"2020-08-21T00:00:00+01:00\"' # str | Search by minimal date (optional)
end_date = '\"2020-09-21T00:00:00+01:00\"' # str | Search by maximal date (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Get an experiment summary history
    api_response = api_instance.get_experiment_summary_history(uri, start_date=start_date, end_date=end_date, page=page, page_size=page_size, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling MetricsApi->get_experiment_summary_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Metrics URI | 
 **start_date** | **str**| Search by minimal date | [optional] 
 **end_date** | **str**| Search by maximal date | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**MetricDTO**](MetricDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_running_experiments_summary**
> MetricDTO get_running_experiments_summary(authorization, start_date=start_date, end_date=end_date, page=page, page_size=page_size, accept_language=accept_language)

Get running experiments metrics



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
api_instance = opensilexClientToolsPython.MetricsApi(pythonClient)
start_date = '\"2020-08-21T00:00:00+01:00\"' # str | Search by minimal date (optional)
end_date = '\"2020-09-21T00:00:00+01:00\"' # str | Search by maximal date (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Get running experiments metrics
    api_response = api_instance.get_running_experiments_summary(start_date=start_date, end_date=end_date, page=page, page_size=page_size, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling MetricsApi->get_running_experiments_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Search by minimal date | [optional] 
 **end_date** | **str**| Search by maximal date | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**MetricDTO**](MetricDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_metrics**
> list[MetricDTO] get_system_metrics(authorization, start_date=start_date, end_date=end_date, page=page, page_size=page_size, accept_language=accept_language)

Get system metrics



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
api_instance = opensilexClientToolsPython.MetricsApi(pythonClient)
start_date = '\"2020-08-21T00:00:00+01:00\"' # str | Search by minimal date (optional)
end_date = '\"2020-09-21T00:00:00+01:00\"' # str | Search by maximal date (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Get system metrics
    api_response = api_instance.get_system_metrics(start_date=start_date, end_date=end_date, page=page, page_size=page_size, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling MetricsApi->get_system_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Search by minimal date | [optional] 
 **end_date** | **str**| Search by maximal date | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[MetricDTO]**](MetricDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_metrics_summary**
> MetricPeriodDTO get_system_metrics_summary(authorization, period=period, page=page, page_size=page_size, accept_language=accept_language)

Get system metrics summary



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
api_instance = opensilexClientToolsPython.MetricsApi(pythonClient)
period = '\"DAY, WEEK, MONTH, YEAR\"' # str | Search by minimal date (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Get system metrics summary
    api_response = api_instance.get_system_metrics_summary(period=period, page=page, page_size=page_size, )
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling MetricsApi->get_system_metrics_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **str**| Search by minimal date | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**MetricPeriodDTO**](MetricPeriodDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

