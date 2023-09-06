# osis-inscription-cours-sdk
A set of API endpoints that allow you to enroll students to courses

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.13
- Package version: 1.13
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import osis_inscription_cours_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import osis_inscription_cours_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import osis_inscription_cours_sdk
from pprint import pprint
from osis_inscription_cours_sdk.api import activites_aide_reussite_api
from osis_inscription_cours_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_inscription_cours_sdk.model.activites_aide_reussite import ActivitesAideReussite
from osis_inscription_cours_sdk.model.demande_activites_aide_reussite import DemandeActivitesAideReussite
from osis_inscription_cours_sdk.model.error import Error
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
    api_instance = activites_aide_reussite_api.ActivitesAideReussiteApi(api_client)
    code_programme = "LSINF100B" # str | The code of the offer
accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
x_user_first_name = "X-User-FirstName_example" # str |  (optional)
x_user_last_name = "X-User-LastName_example" # str |  (optional)
x_user_email = "X-User-Email_example" # str |  (optional)
x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    try:
        api_response = api_instance.get_activites_aide_reussite(code_programme, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_inscription_cours_sdk.ApiException as e:
        print("Exception when calling ActivitesAideReussiteApi->get_activites_aide_reussite: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/inscription_aux_cours*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ActivitesAideReussiteApi* | [**get_activites_aide_reussite**](docs/ActivitesAideReussiteApi.md#get_activites_aide_reussite) | **GET** /{code_programme}/activites_aide_reussite/ | 
*ActivitesAideReussiteApi* | [**post_activites_aide_reussite**](docs/ActivitesAideReussiteApi.md#post_activites_aide_reussite) | **POST** /{code_programme}/activites_aide_reussite/ | 
*ActivitesAideReussiteApi* | [**post_completer_inscription_par_activites_aide_reussite**](docs/ActivitesAideReussiteApi.md#post_completer_inscription_par_activites_aide_reussite) | **POST** /{code_programme}/activites_aide_reussite/completer_inscription | 
*ActivitesAideReussiteApi* | [**post_ne_pas_completer_inscription_par_activites_aide_reussite**](docs/ActivitesAideReussiteApi.md#post_ne_pas_completer_inscription_par_activites_aide_reussite) | **POST** /{code_programme}/activites_aide_reussite/pas_completer_inscription | 
*AutorisationApi* | [**get_est_autorise**](docs/AutorisationApi.md#get_est_autorise) | **GET** /{code_programme}/autorise/ | 
*ComplementDeFormationApi* | [**get_complement_de_formation**](docs/ComplementDeFormationApi.md#get_complement_de_formation) | **GET** /{code_programme}/complement_de_formation | 
*ContactApi* | [**contact_facultes_get**](docs/ContactApi.md#contact_facultes_get) | **GET** /contacts/faculte/ | 
*CoursApi* | [**inscriptions_cours**](docs/CoursApi.md#inscriptions_cours) | **GET** /{code_programme}/inscriptions/ | 
*CoursApi* | [**prerequis_acquis**](docs/CoursApi.md#prerequis_acquis) | **GET** /{code_programme}/prerequis_acquis/ | 
*DemandeParticuliereApi* | [**get_demande_particuliere**](docs/DemandeParticuliereApi.md#get_demande_particuliere) | **GET** /{code_programme}/demande_particuliere/ | 
*FormulaireApi* | [**enregistrer_formulaire_proposition_pae**](docs/FormulaireApi.md#enregistrer_formulaire_proposition_pae) | **POST** /{code_programme}/formulaire/ | 
*FormulaireApi* | [**get_formulaire**](docs/FormulaireApi.md#get_formulaire) | **GET** /{code_programme}/formulaire/ | 
*FormulaireApi* | [**marquer_formulaire_inscription_comme_lu**](docs/FormulaireApi.md#marquer_formulaire_inscription_comme_lu) | **POST** /{code_programme}/formulaire/marquer_lu | 
*MiniFormationApi* | [**enroll_mini_formation**](docs/MiniFormationApi.md#enroll_mini_formation) | **POST** /{code_programme}/mini_formations/inscriptions/ | 
*MiniFormationApi* | [**inscriptions_mini_formations**](docs/MiniFormationApi.md#inscriptions_mini_formations) | **GET** /{code_programme}/mini_formations/inscriptions/ | 
*MiniFormationApi* | [**mini_formations_inscriptibles**](docs/MiniFormationApi.md#mini_formations_inscriptibles) | **GET** /{code_programme}/mini_formations/inscriptibles/ | 
*MiniFormationApi* | [**unenroll_mini_formation**](docs/MiniFormationApi.md#unenroll_mini_formation) | **DELETE** /{code_programme}/mini_formations/inscriptions/ | 
*PaeValideJuryApi* | [**mon_pae_valide_jury**](docs/PaeValideJuryApi.md#mon_pae_valide_jury) | **GET** /{code_programme}/mon_pae_valide_jury/ | 
*PeriodeInscriptionEtudiantApi* | [**get_periode**](docs/PeriodeInscriptionEtudiantApi.md#get_periode) | **GET** /{code_programme}/periode_inscription_etudiant/ | 
*PropositionProgrammeApi* | [**ma_proposition_de_pae**](docs/PropositionProgrammeApi.md#ma_proposition_de_pae) | **GET** /{code_programme}/ma_proposition_de_pae/ | 
*PropositionProgrammeApi* | [**soumettre_proposition_programme**](docs/PropositionProgrammeApi.md#soumettre_proposition_programme) | **POST** /{code_programme}/soumettre/ | 


## Documentation For Models

 - [AcceptedLanguageEnum](docs/AcceptedLanguageEnum.md)
 - [ActivitesAideReussite](docs/ActivitesAideReussite.md)
 - [AutoriseInscrireAuxCours](docs/AutoriseInscrireAuxCours.md)
 - [ComplementDeFormation](docs/ComplementDeFormation.md)
 - [ContactFaculte](docs/ContactFaculte.md)
 - [Cours](docs/Cours.md)
 - [DemandeActivitesAideReussite](docs/DemandeActivitesAideReussite.md)
 - [DemandeParticuliere](docs/DemandeParticuliere.md)
 - [Error](docs/Error.md)
 - [FormulaireInscriptionCours](docs/FormulaireInscriptionCours.md)
 - [FormulairePropositionProgrammeAnnuel](docs/FormulairePropositionProgrammeAnnuel.md)
 - [FormulairePropositionProgrammeAnnuelDemandesParticulieresDansMiniFormations](docs/FormulairePropositionProgrammeAnnuelDemandesParticulieresDansMiniFormations.md)
 - [FormulairePropositionProgrammeAnnuelInscriptionsDansMiniFormations](docs/FormulairePropositionProgrammeAnnuelInscriptionsDansMiniFormations.md)
 - [Groupement](docs/Groupement.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InscriptionAUnCours](docs/InscriptionAUnCours.md)
 - [InscriptionMiniFormation](docs/InscriptionMiniFormation.md)
 - [InscriptionsAUnPartenariat](docs/InscriptionsAUnPartenariat.md)
 - [InscriptionsPourUneMiniFormation](docs/InscriptionsPourUneMiniFormation.md)
 - [InscrireAUneMiniFormation](docs/InscrireAUneMiniFormation.md)
 - [ListeMiniFormations](docs/ListeMiniFormations.md)
 - [MiniFormation](docs/MiniFormation.md)
 - [PaeValideJury](docs/PaeValideJury.md)
 - [PaeValideJuryLinks](docs/PaeValideJuryLinks.md)
 - [PdfEnCours](docs/PdfEnCours.md)
 - [PeriodeInscriptionEtudiant](docs/PeriodeInscriptionEtudiant.md)
 - [ProgrammeAnnuelEtudiant](docs/ProgrammeAnnuelEtudiant.md)
 - [PropositionPae](docs/PropositionPae.md)
 - [PropositionPaeLinks](docs/PropositionPaeLinks.md)
 - [UniteEnseignementAvecPrerequis](docs/UniteEnseignementAvecPrerequis.md)


## Documentation For Authorization


## Token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in osis_inscription_cours_sdk.apis and osis_inscription_cours_sdk.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from osis_inscription_cours_sdk.api.default_api import DefaultApi`
- `from osis_inscription_cours_sdk.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import osis_inscription_cours_sdk
from osis_inscription_cours_sdk.apis import *
from osis_inscription_cours_sdk.models import *
```

