# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    OpenAPI spec version: 0.7.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..api_client import ApiClient


class WarsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_wars(self, **kwargs):
        """
        List wars
        Return a list of wars  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_wars(async=True)
        >>> result = thread.get()

        :param async bool
        :param str datasource: The server name you would like data from
        :param int max_war_id: Only return wars with ID smaller than this.
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_wars_with_http_info(**kwargs)
        else:
            (data) = self.get_wars_with_http_info(**kwargs)
            return data

    def get_wars_with_http_info(self, **kwargs):
        """
        List wars
        Return a list of wars  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_wars_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str datasource: The server name you would like data from
        :param int max_war_id: Only return wars with ID smaller than this.
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['datasource', 'max_war_id', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_wars" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'max_war_id' in params:
            query_params.append(('max_war_id', params['max_war_id']))
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
        auth_settings = []

        return self.api_client.call_api('/v1/wars/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[int]',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_wars_war_id(self, war_id, **kwargs):
        """
        Get war information
        Return details about a war  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_wars_war_id(war_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int war_id: ID for a war (required)
        :param str datasource: The server name you would like data from
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: GetWarsWarIdOk
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_wars_war_id_with_http_info(war_id, **kwargs)
        else:
            (data) = self.get_wars_war_id_with_http_info(war_id, **kwargs)
            return data

    def get_wars_war_id_with_http_info(self, war_id, **kwargs):
        """
        Get war information
        Return details about a war  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_wars_war_id_with_http_info(war_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int war_id: ID for a war (required)
        :param str datasource: The server name you would like data from
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: GetWarsWarIdOk
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['war_id', 'datasource', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_wars_war_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'war_id' is set
        if ('war_id' not in params) or (params['war_id'] is None):
            raise ValueError("Missing the required parameter `war_id` when calling `get_wars_war_id`")


        collection_formats = {}

        path_params = {}
        if 'war_id' in params:
            path_params['war_id'] = params['war_id']

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
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
        auth_settings = []

        return self.api_client.call_api('/v1/wars/{war_id}/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='GetWarsWarIdOk',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_wars_war_id_killmails(self, war_id, **kwargs):
        """
        List kills for a war
        Return a list of kills related to a war  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_wars_war_id_killmails(war_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int war_id: A valid war ID (required)
        :param str datasource: The server name you would like data from
        :param int page: Which page of results to return
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetWarsWarIdKillmails200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_wars_war_id_killmails_with_http_info(war_id, **kwargs)
        else:
            (data) = self.get_wars_war_id_killmails_with_http_info(war_id, **kwargs)
            return data

    def get_wars_war_id_killmails_with_http_info(self, war_id, **kwargs):
        """
        List kills for a war
        Return a list of kills related to a war  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_wars_war_id_killmails_with_http_info(war_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int war_id: A valid war ID (required)
        :param str datasource: The server name you would like data from
        :param int page: Which page of results to return
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetWarsWarIdKillmails200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['war_id', 'datasource', 'page', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_wars_war_id_killmails" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'war_id' is set
        if ('war_id' not in params) or (params['war_id'] is None):
            raise ValueError("Missing the required parameter `war_id` when calling `get_wars_war_id_killmails`")


        collection_formats = {}

        path_params = {}
        if 'war_id' in params:
            path_params['war_id'] = params['war_id']

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'page' in params:
            query_params.append(('page', params['page']))
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
        auth_settings = []

        return self.api_client.call_api('/v1/wars/{war_id}/killmails/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[GetWarsWarIdKillmails200Ok]',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
