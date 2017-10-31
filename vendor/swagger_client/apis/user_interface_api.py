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


class UserInterfaceApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def post_ui_autopilot_waypoint(self, add_to_beginning, clear_other_waypoints, destination_id, **kwargs):
        """
        Set Autopilot Waypoint
        Set a solar system as autopilot waypoint  --- 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_ui_autopilot_waypoint(add_to_beginning, clear_other_waypoints, destination_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param bool add_to_beginning: Whether this solar system should be added to the beginning of all waypoints (required)
        :param bool clear_other_waypoints: Whether clean other waypoints beforing adding this one (required)
        :param int destination_id: The destination to travel to, can be solar system, station or structure's id (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_ui_autopilot_waypoint_with_http_info(add_to_beginning, clear_other_waypoints, destination_id, **kwargs)
        else:
            (data) = self.post_ui_autopilot_waypoint_with_http_info(add_to_beginning, clear_other_waypoints, destination_id, **kwargs)
            return data

    def post_ui_autopilot_waypoint_with_http_info(self, add_to_beginning, clear_other_waypoints, destination_id, **kwargs):
        """
        Set Autopilot Waypoint
        Set a solar system as autopilot waypoint  --- 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_ui_autopilot_waypoint_with_http_info(add_to_beginning, clear_other_waypoints, destination_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param bool add_to_beginning: Whether this solar system should be added to the beginning of all waypoints (required)
        :param bool clear_other_waypoints: Whether clean other waypoints beforing adding this one (required)
        :param int destination_id: The destination to travel to, can be solar system, station or structure's id (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['add_to_beginning', 'clear_other_waypoints', 'destination_id', 'datasource', 'token', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_ui_autopilot_waypoint" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'add_to_beginning' is set
        if ('add_to_beginning' not in params) or (params['add_to_beginning'] is None):
            raise ValueError("Missing the required parameter `add_to_beginning` when calling `post_ui_autopilot_waypoint`")
        # verify the required parameter 'clear_other_waypoints' is set
        if ('clear_other_waypoints' not in params) or (params['clear_other_waypoints'] is None):
            raise ValueError("Missing the required parameter `clear_other_waypoints` when calling `post_ui_autopilot_waypoint`")
        # verify the required parameter 'destination_id' is set
        if ('destination_id' not in params) or (params['destination_id'] is None):
            raise ValueError("Missing the required parameter `destination_id` when calling `post_ui_autopilot_waypoint`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'add_to_beginning' in params:
            query_params.append(('add_to_beginning', params['add_to_beginning']))
        if 'clear_other_waypoints' in params:
            query_params.append(('clear_other_waypoints', params['clear_other_waypoints']))
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'destination_id' in params:
            query_params.append(('destination_id', params['destination_id']))
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

        return self.api_client.call_api('/v2/ui/autopilot/waypoint/', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_ui_openwindow_contract(self, contract_id, **kwargs):
        """
        Open Contract Window
        Open the contract window inside the client  --- 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_ui_openwindow_contract(contract_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int contract_id: The contract to open (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_ui_openwindow_contract_with_http_info(contract_id, **kwargs)
        else:
            (data) = self.post_ui_openwindow_contract_with_http_info(contract_id, **kwargs)
            return data

    def post_ui_openwindow_contract_with_http_info(self, contract_id, **kwargs):
        """
        Open Contract Window
        Open the contract window inside the client  --- 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_ui_openwindow_contract_with_http_info(contract_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int contract_id: The contract to open (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['contract_id', 'datasource', 'token', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_ui_openwindow_contract" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'contract_id' is set
        if ('contract_id' not in params) or (params['contract_id'] is None):
            raise ValueError("Missing the required parameter `contract_id` when calling `post_ui_openwindow_contract`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'contract_id' in params:
            query_params.append(('contract_id', params['contract_id']))
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

        return self.api_client.call_api('/v1/ui/openwindow/contract/', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_ui_openwindow_information(self, target_id, **kwargs):
        """
        Open Information Window
        Open the information window for a character, corporation or alliance inside the client  --- 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_ui_openwindow_information(target_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int target_id: The target to open (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_ui_openwindow_information_with_http_info(target_id, **kwargs)
        else:
            (data) = self.post_ui_openwindow_information_with_http_info(target_id, **kwargs)
            return data

    def post_ui_openwindow_information_with_http_info(self, target_id, **kwargs):
        """
        Open Information Window
        Open the information window for a character, corporation or alliance inside the client  --- 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_ui_openwindow_information_with_http_info(target_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int target_id: The target to open (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['target_id', 'datasource', 'token', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_ui_openwindow_information" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'target_id' is set
        if ('target_id' not in params) or (params['target_id'] is None):
            raise ValueError("Missing the required parameter `target_id` when calling `post_ui_openwindow_information`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'target_id' in params:
            query_params.append(('target_id', params['target_id']))
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

        return self.api_client.call_api('/v1/ui/openwindow/information/', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_ui_openwindow_marketdetails(self, type_id, **kwargs):
        """
        Open Market Details
        Open the market details window for a specific typeID inside the client  --- 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_ui_openwindow_marketdetails(type_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int type_id: The item type to open in market window (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_ui_openwindow_marketdetails_with_http_info(type_id, **kwargs)
        else:
            (data) = self.post_ui_openwindow_marketdetails_with_http_info(type_id, **kwargs)
            return data

    def post_ui_openwindow_marketdetails_with_http_info(self, type_id, **kwargs):
        """
        Open Market Details
        Open the market details window for a specific typeID inside the client  --- 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_ui_openwindow_marketdetails_with_http_info(type_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int type_id: The item type to open in market window (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type_id', 'datasource', 'token', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_ui_openwindow_marketdetails" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'type_id' is set
        if ('type_id' not in params) or (params['type_id'] is None):
            raise ValueError("Missing the required parameter `type_id` when calling `post_ui_openwindow_marketdetails`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'token' in params:
            query_params.append(('token', params['token']))
        if 'type_id' in params:
            query_params.append(('type_id', params['type_id']))
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

        return self.api_client.call_api('/v1/ui/openwindow/marketdetails/', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_ui_openwindow_newmail(self, new_mail, **kwargs):
        """
        Open New Mail Window
        Open the New Mail window, according to settings from the request if applicable  --- 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_ui_openwindow_newmail(new_mail, async=True)
        >>> result = thread.get()

        :param async bool
        :param PostUiOpenwindowNewmailNewMail new_mail: The details of mail to create (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_ui_openwindow_newmail_with_http_info(new_mail, **kwargs)
        else:
            (data) = self.post_ui_openwindow_newmail_with_http_info(new_mail, **kwargs)
            return data

    def post_ui_openwindow_newmail_with_http_info(self, new_mail, **kwargs):
        """
        Open New Mail Window
        Open the New Mail window, according to settings from the request if applicable  --- 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_ui_openwindow_newmail_with_http_info(new_mail, async=True)
        >>> result = thread.get()

        :param async bool
        :param PostUiOpenwindowNewmailNewMail new_mail: The details of mail to create (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['new_mail', 'datasource', 'token', 'user_agent', 'x_user_agent']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_ui_openwindow_newmail" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'new_mail' is set
        if ('new_mail' not in params) or (params['new_mail'] is None):
            raise ValueError("Missing the required parameter `new_mail` when calling `post_ui_openwindow_newmail`")


        collection_formats = {}

        path_params = {}

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
        if 'new_mail' in params:
            body_params = params['new_mail']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['evesso']

        return self.api_client.call_api('/v1/ui/openwindow/newmail/', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
