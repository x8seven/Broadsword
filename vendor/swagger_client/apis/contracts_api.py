# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    OpenAPI spec version: 0.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..api_client import ApiClient


class ContractsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_characters_character_id_contracts(self, character_id, **kwargs):
        """
        Get contracts
        Returns contracts available to a character, only if the character is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is \"in_progress\".  ---  This route is cached for up to 300 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_characters_character_id_contracts(character_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetCharactersCharacterIdContracts200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_characters_character_id_contracts_with_http_info(character_id, **kwargs)
        else:
            (data) = self.get_characters_character_id_contracts_with_http_info(character_id, **kwargs)
            return data

    def get_characters_character_id_contracts_with_http_info(self, character_id, **kwargs):
        """
        Get contracts
        Returns contracts available to a character, only if the character is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is \"in_progress\".  ---  This route is cached for up to 300 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_characters_character_id_contracts_with_http_info(character_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetCharactersCharacterIdContracts200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['character_id', 'datasource', 'token', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_characters_character_id_contracts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if ('character_id' not in params) or (params['character_id'] is None):
            raise ValueError("Missing the required parameter `character_id` when calling `get_characters_character_id_contracts`")


        collection_formats = {}

        path_params = {}
        if 'character_id' in params:
            path_params['character_id'] = params['character_id']

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'token' in params:
            query_params.append(('token', params['token']))
        if 'user_agent' in params:
            query_params.append(('user_agent', params['user_agent']))

        header_params = {}
        if 'x_user_agent' in params:
            header_params['X-User-Agent'] = params['x_user_agent']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['evesso']

        return self.api_client.call_api('/v1/characters/{character_id}/contracts/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[GetCharactersCharacterIdContracts200Ok]',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_characters_character_id_contracts_contract_id_bids(self, character_id, contract_id, **kwargs):
        """
        Get contract bids
        Lists bids on a particular auction contract  ---  This route is cached for up to 300 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_characters_character_id_contracts_contract_id_bids(character_id, contract_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int character_id: An EVE character ID (required)
        :param int contract_id: ID of a contract (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetCharactersCharacterIdContractsContractIdBids200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_characters_character_id_contracts_contract_id_bids_with_http_info(character_id, contract_id, **kwargs)
        else:
            (data) = self.get_characters_character_id_contracts_contract_id_bids_with_http_info(character_id, contract_id, **kwargs)
            return data

    def get_characters_character_id_contracts_contract_id_bids_with_http_info(self, character_id, contract_id, **kwargs):
        """
        Get contract bids
        Lists bids on a particular auction contract  ---  This route is cached for up to 300 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_characters_character_id_contracts_contract_id_bids_with_http_info(character_id, contract_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int character_id: An EVE character ID (required)
        :param int contract_id: ID of a contract (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetCharactersCharacterIdContractsContractIdBids200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['character_id', 'contract_id', 'datasource', 'token', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_characters_character_id_contracts_contract_id_bids" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if ('character_id' not in params) or (params['character_id'] is None):
            raise ValueError("Missing the required parameter `character_id` when calling `get_characters_character_id_contracts_contract_id_bids`")
        # verify the required parameter 'contract_id' is set
        if ('contract_id' not in params) or (params['contract_id'] is None):
            raise ValueError("Missing the required parameter `contract_id` when calling `get_characters_character_id_contracts_contract_id_bids`")


        collection_formats = {}

        path_params = {}
        if 'character_id' in params:
            path_params['character_id'] = params['character_id']
        if 'contract_id' in params:
            path_params['contract_id'] = params['contract_id']

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'token' in params:
            query_params.append(('token', params['token']))
        if 'user_agent' in params:
            query_params.append(('user_agent', params['user_agent']))

        header_params = {}
        if 'x_user_agent' in params:
            header_params['X-User-Agent'] = params['x_user_agent']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['evesso']

        return self.api_client.call_api('/v1/characters/{character_id}/contracts/{contract_id}/bids/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[GetCharactersCharacterIdContractsContractIdBids200Ok]',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_characters_character_id_contracts_contract_id_items(self, character_id, contract_id, **kwargs):
        """
        Get contract items
        Lists items of a particular contract  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_characters_character_id_contracts_contract_id_items(character_id, contract_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int character_id: An EVE character ID (required)
        :param int contract_id: ID of a contract (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetCharactersCharacterIdContractsContractIdItems200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_characters_character_id_contracts_contract_id_items_with_http_info(character_id, contract_id, **kwargs)
        else:
            (data) = self.get_characters_character_id_contracts_contract_id_items_with_http_info(character_id, contract_id, **kwargs)
            return data

    def get_characters_character_id_contracts_contract_id_items_with_http_info(self, character_id, contract_id, **kwargs):
        """
        Get contract items
        Lists items of a particular contract  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_characters_character_id_contracts_contract_id_items_with_http_info(character_id, contract_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int character_id: An EVE character ID (required)
        :param int contract_id: ID of a contract (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetCharactersCharacterIdContractsContractIdItems200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['character_id', 'contract_id', 'datasource', 'token', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_characters_character_id_contracts_contract_id_items" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if ('character_id' not in params) or (params['character_id'] is None):
            raise ValueError("Missing the required parameter `character_id` when calling `get_characters_character_id_contracts_contract_id_items`")
        # verify the required parameter 'contract_id' is set
        if ('contract_id' not in params) or (params['contract_id'] is None):
            raise ValueError("Missing the required parameter `contract_id` when calling `get_characters_character_id_contracts_contract_id_items`")


        collection_formats = {}

        path_params = {}
        if 'character_id' in params:
            path_params['character_id'] = params['character_id']
        if 'contract_id' in params:
            path_params['contract_id'] = params['contract_id']

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'token' in params:
            query_params.append(('token', params['token']))
        if 'user_agent' in params:
            query_params.append(('user_agent', params['user_agent']))

        header_params = {}
        if 'x_user_agent' in params:
            header_params['X-User-Agent'] = params['x_user_agent']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['evesso']

        return self.api_client.call_api('/v1/characters/{character_id}/contracts/{contract_id}/items/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[GetCharactersCharacterIdContractsContractIdItems200Ok]',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_corporations_corporation_id_contracts(self, corporation_id, **kwargs):
        """
        Get coporation contracts
        Returns contracts available to a coporation, only if the corporation is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is \"in_progress\".  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_corporations_corporation_id_contracts(corporation_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int corporation_id: An EVE corporation ID (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetCorporationsCorporationIdContracts200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_corporations_corporation_id_contracts_with_http_info(corporation_id, **kwargs)
        else:
            (data) = self.get_corporations_corporation_id_contracts_with_http_info(corporation_id, **kwargs)
            return data

    def get_corporations_corporation_id_contracts_with_http_info(self, corporation_id, **kwargs):
        """
        Get coporation contracts
        Returns contracts available to a coporation, only if the corporation is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is \"in_progress\".  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_corporations_corporation_id_contracts_with_http_info(corporation_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int corporation_id: An EVE corporation ID (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetCorporationsCorporationIdContracts200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['corporation_id', 'datasource', 'token', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_corporations_corporation_id_contracts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'corporation_id' is set
        if ('corporation_id' not in params) or (params['corporation_id'] is None):
            raise ValueError("Missing the required parameter `corporation_id` when calling `get_corporations_corporation_id_contracts`")


        collection_formats = {}

        path_params = {}
        if 'corporation_id' in params:
            path_params['corporation_id'] = params['corporation_id']

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'token' in params:
            query_params.append(('token', params['token']))
        if 'user_agent' in params:
            query_params.append(('user_agent', params['user_agent']))

        header_params = {}
        if 'x_user_agent' in params:
            header_params['X-User-Agent'] = params['x_user_agent']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['evesso']

        return self.api_client.call_api('/v1/corporations/{corporation_id}/contracts/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[GetCorporationsCorporationIdContracts200Ok]',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_corporations_corporation_id_contracts_contract_id_bids(self, contract_id, corporation_id, **kwargs):
        """
        Get corporation contract bids
        Lists bids on a particular auction contract  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_corporations_corporation_id_contracts_contract_id_bids(contract_id, corporation_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int contract_id: ID of a contract (required)
        :param int corporation_id: An EVE corporation ID (required)
        :param str datasource: The server name you would like data from
        :param int page: Which page of results to return
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetCorporationsCorporationIdContractsContractIdBids200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_corporations_corporation_id_contracts_contract_id_bids_with_http_info(contract_id, corporation_id, **kwargs)
        else:
            (data) = self.get_corporations_corporation_id_contracts_contract_id_bids_with_http_info(contract_id, corporation_id, **kwargs)
            return data

    def get_corporations_corporation_id_contracts_contract_id_bids_with_http_info(self, contract_id, corporation_id, **kwargs):
        """
        Get corporation contract bids
        Lists bids on a particular auction contract  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_corporations_corporation_id_contracts_contract_id_bids_with_http_info(contract_id, corporation_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int contract_id: ID of a contract (required)
        :param int corporation_id: An EVE corporation ID (required)
        :param str datasource: The server name you would like data from
        :param int page: Which page of results to return
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetCorporationsCorporationIdContractsContractIdBids200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['contract_id', 'corporation_id', 'datasource', 'page', 'token', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_corporations_corporation_id_contracts_contract_id_bids" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'contract_id' is set
        if ('contract_id' not in params) or (params['contract_id'] is None):
            raise ValueError("Missing the required parameter `contract_id` when calling `get_corporations_corporation_id_contracts_contract_id_bids`")
        # verify the required parameter 'corporation_id' is set
        if ('corporation_id' not in params) or (params['corporation_id'] is None):
            raise ValueError("Missing the required parameter `corporation_id` when calling `get_corporations_corporation_id_contracts_contract_id_bids`")


        collection_formats = {}

        path_params = {}
        if 'contract_id' in params:
            path_params['contract_id'] = params['contract_id']
        if 'corporation_id' in params:
            path_params['corporation_id'] = params['corporation_id']

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'page' in params:
            query_params.append(('page', params['page']))
        if 'token' in params:
            query_params.append(('token', params['token']))
        if 'user_agent' in params:
            query_params.append(('user_agent', params['user_agent']))

        header_params = {}
        if 'x_user_agent' in params:
            header_params['X-User-Agent'] = params['x_user_agent']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['evesso']

        return self.api_client.call_api('/v1/corporations/{corporation_id}/contracts/{contract_id}/bids/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[GetCorporationsCorporationIdContractsContractIdBids200Ok]',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_corporations_corporation_id_contracts_contract_id_items(self, contract_id, corporation_id, **kwargs):
        """
        Get corporation contract items
        Lists items of a particular contract  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_corporations_corporation_id_contracts_contract_id_items(contract_id, corporation_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int contract_id: ID of a contract (required)
        :param int corporation_id: An EVE corporation ID (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetCorporationsCorporationIdContractsContractIdItems200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_corporations_corporation_id_contracts_contract_id_items_with_http_info(contract_id, corporation_id, **kwargs)
        else:
            (data) = self.get_corporations_corporation_id_contracts_contract_id_items_with_http_info(contract_id, corporation_id, **kwargs)
            return data

    def get_corporations_corporation_id_contracts_contract_id_items_with_http_info(self, contract_id, corporation_id, **kwargs):
        """
        Get corporation contract items
        Lists items of a particular contract  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_corporations_corporation_id_contracts_contract_id_items_with_http_info(contract_id, corporation_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int contract_id: ID of a contract (required)
        :param int corporation_id: An EVE corporation ID (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetCorporationsCorporationIdContractsContractIdItems200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['contract_id', 'corporation_id', 'datasource', 'token', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_corporations_corporation_id_contracts_contract_id_items" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'contract_id' is set
        if ('contract_id' not in params) or (params['contract_id'] is None):
            raise ValueError("Missing the required parameter `contract_id` when calling `get_corporations_corporation_id_contracts_contract_id_items`")
        # verify the required parameter 'corporation_id' is set
        if ('corporation_id' not in params) or (params['corporation_id'] is None):
            raise ValueError("Missing the required parameter `corporation_id` when calling `get_corporations_corporation_id_contracts_contract_id_items`")


        collection_formats = {}

        path_params = {}
        if 'contract_id' in params:
            path_params['contract_id'] = params['contract_id']
        if 'corporation_id' in params:
            path_params['corporation_id'] = params['corporation_id']

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'token' in params:
            query_params.append(('token', params['token']))
        if 'user_agent' in params:
            query_params.append(('user_agent', params['user_agent']))

        header_params = {}
        if 'x_user_agent' in params:
            header_params['X-User-Agent'] = params['x_user_agent']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['evesso']

        return self.api_client.call_api('/v1/corporations/{corporation_id}/contracts/{contract_id}/items/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[GetCorporationsCorporationIdContractsContractIdItems200Ok]',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
