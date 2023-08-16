# opensilexClientToolsPython.AuthenticationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate**](AuthenticationApi.md#authenticate) | **POST** /security/authenticate | Authenticate a user and return an access token
[**authenticate_open_id**](AuthenticationApi.md#authenticate_open_id) | **GET** /security/openid | Authenticate a user and return an access token
[**authenticate_saml**](AuthenticationApi.md#authenticate_saml) | **GET** /security/saml | Authenticate a user and return an access token from SAML response
[**forgot_password**](AuthenticationApi.md#forgot_password) | **POST** /security/forgot-password | Send an e-mail confirmation
[**get_credentials_groups**](AuthenticationApi.md#get_credentials_groups) | **GET** /security/credentials | Get list of existing credentials indexed by Swagger @API concepts in the application
[**logout**](AuthenticationApi.md#logout) | **DELETE** /security/logout | Logout by discarding a user token
[**renew_password**](AuthenticationApi.md#renew_password) | **PUT** /security/renew-password | Update user password
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
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.AuthenticationApi(pythonClient)
body = opensilexClientToolsPython.AuthenticationDTO() # AuthenticationDTO | User authentication informations (optional)


try:
    # Authenticate a user and return an access token
    api_response = api_instance.authenticate(body=body)
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
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
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.AuthenticationApi(pythonClient)
code = 'code_example' # str | Authorization code (optional)


try:
    # Authenticate a user and return an access token
    api_response = api_instance.authenticate_open_id(code=code)
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
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

# **authenticate_saml**
> authenticate_saml()

Authenticate a user and return an access token from SAML response



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
api_instance = opensilexClientToolsPython.AuthenticationApi(pythonClient)


try:
    # Authenticate a user and return an access token from SAML response
    api_instance.authenticate_saml()
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling AuthenticationApi->authenticate_saml: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forgot_password**
> forgot_password(identifier)

Send an e-mail confirmation



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
api_instance = opensilexClientToolsPython.AuthenticationApi(pythonClient)
identifier = 'identifier_example' # str | User e-mail or uri


try:
    # Send an e-mail confirmation
    api_instance.forgot_password(identifier)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling AuthenticationApi->forgot_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| User e-mail or uri | 


### Return type

void (empty response body)

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
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.AuthenticationApi(pythonClient)


try:
    # Get list of existing credentials indexed by Swagger @API concepts in the application
    api_response = api_instance.get_credentials_groups()
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
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
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.AuthenticationApi(pythonClient)


try:
    # Logout by discarding a user token
    api_instance.logout()
except opensilexClientToolsPython.rest.ApiException as e:
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

# **renew_password**
> TokenGetDTO renew_password(renew_token, check_only=check_only, password=password)

Update user password



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
api_instance = opensilexClientToolsPython.AuthenticationApi(pythonClient)
renew_token = 'renew_token_example' # str | User renew token
check_only = false # bool | Check only renew token (optional) (default to false)
password = 'password_example' # str | User password (optional)


try:
    # Update user password
    api_response = api_instance.renew_password(renew_token, check_only=check_only, password=password)
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling AuthenticationApi->renew_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **renew_token** | **str**| User renew token | 
 **check_only** | **bool**| Check only renew token | [optional] [default to false]
 **password** | **str**| User password | [optional] 


### Return type

[**TokenGetDTO**](TokenGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

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
pythonClient.connect_to_opensilex_ws(identifier="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientToolsPython.AuthenticationApi(pythonClient)


try:
    # Send back a new token if the provided one is still valid
    api_response = api_instance.renew_token()
    pprint(api_response)
except opensilexClientToolsPython.rest.ApiException as e:
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

