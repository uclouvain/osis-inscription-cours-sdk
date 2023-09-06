"""
    Course enrollments service

    A set of API endpoints that allow you to enroll students to courses  # noqa: E501

    The version of the OpenAPI document: 1.13
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from osis_inscription_cours_sdk.api_client import ApiClient, Endpoint as _Endpoint
from osis_inscription_cours_sdk.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from osis_inscription_cours_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_inscription_cours_sdk.model.contact_faculte import ContactFaculte
from osis_inscription_cours_sdk.model.error import Error


class ContactApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.contact_facultes_get_endpoint = _Endpoint(
            settings={
                'response_type': (ContactFaculte,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/contacts/faculte/',
                'operation_id': 'contact_facultes_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'formation',
                    'annee',
                    'premiere_annee',
                    'accept_language',
                    'x_user_first_name',
                    'x_user_last_name',
                    'x_user_email',
                    'x_user_global_id',
                ],
                'required': [
                    'formation',
                    'annee',
                    'premiere_annee',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'formation':
                        (str,),
                    'annee':
                        (int,),
                    'premiere_annee':
                        (bool,),
                    'accept_language':
                        (AcceptedLanguageEnum,),
                    'x_user_first_name':
                        (str,),
                    'x_user_last_name':
                        (str,),
                    'x_user_email':
                        (str,),
                    'x_user_global_id':
                        (str,),
                },
                'attribute_map': {
                    'formation': 'formation',
                    'annee': 'annee',
                    'premiere_annee': 'premiere_annee',
                    'accept_language': 'Accept-Language',
                    'x_user_first_name': 'X-User-FirstName',
                    'x_user_last_name': 'X-User-LastName',
                    'x_user_email': 'X-User-Email',
                    'x_user_global_id': 'X-User-GlobalID',
                },
                'location_map': {
                    'formation': 'query',
                    'annee': 'query',
                    'premiere_annee': 'query',
                    'accept_language': 'header',
                    'x_user_first_name': 'header',
                    'x_user_last_name': 'header',
                    'x_user_email': 'header',
                    'x_user_global_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def contact_facultes_get(
        self,
        formation,
        annee,
        premiere_annee,
        **kwargs
    ):
        """contact_facultes_get  # noqa: E501

        Retourne les details de contact d'une faculté'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.contact_facultes_get(formation, annee, premiere_annee, async_req=True)
        >>> result = thread.get()

        Args:
            formation (str): Acronyme de la formation
            annee (int): Annee academique
            premiere_annee (bool): Indique si on veut les contact pour une premiere annee de bachelier

        Keyword Args:
            accept_language (AcceptedLanguageEnum): The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) . [optional]
            x_user_first_name (str): [optional]
            x_user_last_name (str): [optional]
            x_user_email (str): [optional]
            x_user_global_id (str): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ContactFaculte
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['formation'] = \
            formation
        kwargs['annee'] = \
            annee
        kwargs['premiere_annee'] = \
            premiere_annee
        return self.contact_facultes_get_endpoint.call_with_http_info(**kwargs)

