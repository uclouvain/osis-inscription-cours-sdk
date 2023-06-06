# osis_inscription_cours_sdk.CoursApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/inscription_aux_cours*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inscriptions_cours**](CoursApi.md#inscriptions_cours) | **GET** /{code_programme}/inscriptions/ | 
[**prerequis_acquis**](CoursApi.md#prerequis_acquis) | **GET** /{code_programme}/prerequis_acquis/ | 


# **inscriptions_cours**
> ProgrammeAnnuelEtudiant inscriptions_cours(code_programme)



Return courses enrollments

### Example

* Api Key Authentication (Token):

```python
import time
import osis_inscription_cours_sdk
from osis_inscription_cours_sdk.api import cours_api
from osis_inscription_cours_sdk.model.error import Error
from osis_inscription_cours_sdk.model.programme_annuel_etudiant import ProgrammeAnnuelEtudiant
from osis_inscription_cours_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/inscription_aux_cours
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_inscription_cours_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/inscription_aux_cours"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_inscription_cours_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cours_api.CoursApi(api_client)
    code_programme = "LSINF100B" # str | The code of the offer
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.inscriptions_cours(code_programme)
        pprint(api_response)
    except osis_inscription_cours_sdk.ApiException as e:
        print("Exception when calling CoursApi->inscriptions_cours: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.inscriptions_cours(code_programme, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_inscription_cours_sdk.ApiException as e:
        print("Exception when calling CoursApi->inscriptions_cours: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_programme** | **str**| The code of the offer |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**ProgrammeAnnuelEtudiant**](ProgrammeAnnuelEtudiant.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prerequis_acquis**
> [UniteEnseignementAvecPrerequis] prerequis_acquis(code_programme)



Renvoie la liste des unité d'enseignement qui ont des prérequis en spécifiant si ces prérequis sont acquis ou non

### Example

* Api Key Authentication (Token):

```python
import time
import osis_inscription_cours_sdk
from osis_inscription_cours_sdk.api import cours_api
from osis_inscription_cours_sdk.model.error import Error
from osis_inscription_cours_sdk.model.unite_enseignement_avec_prerequis import UniteEnseignementAvecPrerequis
from osis_inscription_cours_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/inscription_aux_cours
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_inscription_cours_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/inscription_aux_cours"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_inscription_cours_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cours_api.CoursApi(api_client)
    code_programme = "LSINF100B" # str | Code du programme
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.prerequis_acquis(code_programme)
        pprint(api_response)
    except osis_inscription_cours_sdk.ApiException as e:
        print("Exception when calling CoursApi->prerequis_acquis: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.prerequis_acquis(code_programme, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_inscription_cours_sdk.ApiException as e:
        print("Exception when calling CoursApi->prerequis_acquis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_programme** | **str**| Code du programme |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**[UniteEnseignementAvecPrerequis]**](UniteEnseignementAvecPrerequis.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

