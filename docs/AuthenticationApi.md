# opensilexClientToolsPython.AuthenticationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate**](AuthenticationApi.md#authenticate) | **POST** /security/authenticate | Authenticate a user and return an access token
[**authenticate_open_id**](AuthenticationApi.md#authenticate_open_id) | **GET** /security/openid | Authenticate a user and return an access token
[**get_credentials_groups**](AuthenticationApi.md#get_credentials_groups) | **GET** /security/credentials | Get list of existing credentials indexed by Swagger @API concepts in the application
[**logout**](AuthenticationApi.md#logout) | **DELETE** /security/logout | Logout by discarding a user token
[**renew_token**](AuthenticationApi.md#renew_token) | **PUT** /security/renew-token | Send back a new token if the provided one is still valid


# **authenticate**
> TokenGetDTO authenticate(body=body)

Authenticate a user and return an access token



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
api_instance = opensilexClientToolsPython.AuthenticationApi(pythonClient)
body = opensilexClientToolsPython.AuthenticationDTO() # AuthenticationDTO | User authentication informations (optional)


try:
    # Authenticate a user and return an access token
    api_response = api_instance.authenticate(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authenticate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthenticationDTO**](AuthenticationDTO.md)| User authentication informations | [optional] 


### Return type

[**TokenGetDTO**](TokenGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authenticate_open_id**
> TokenGetDTO authenticate_open_id(code=code)

Authenticate a user and return an access token



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
api_instance = opensilexClientToolsPython.AuthenticationApi(pythonClient)
code = 'code_example' # str | Authorization code (optional)


try:
    # Authenticate a user and return an access token
    api_response = api_instance.authenticate_open_id(code=code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authenticate_open_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Authorization code | [optional] 


### Return type

[**TokenGetDTO**](TokenGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credentials_groups**
> list[CredentialsGroupDTO] get_credentials_groups()

Get list of existing credentials indexed by Swagger @API concepts in the application



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
api_instance = opensilexClientToolsPython.AuthenticationApi(pythonClient)


try:
    # Get list of existing credentials indexed by Swagger @API concepts in the application
    api_response = api_instance.get_credentials_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->get_credentials_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.


### Return type

[**list[CredentialsGroupDTO]**](CredentialsGroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> logout(authorization, accept_language=accept_language)

Logout by discarding a user token



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
api_instance = opensilexClientToolsPython.AuthenticationApi(pythonClient)


try:
    # Logout by discarding a user token
    api_instance.logout()
except ApiException as e:
    print("Exception when calling AuthenticationApi->logout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **renew_token**
> TokenGetDTO renew_token(authorization, accept_language=accept_language)

Send back a new token if the provided one is still valid



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
api_instance = opensilexClientToolsPython.AuthenticationApi(pythonClient)


try:
    # Send back a new token if the provided one is still valid
    api_response = api_instance.renew_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->renew_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**TokenGetDTO**](TokenGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

