# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0-rc+7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from typing import List
from opensilexClientToolsPython.models import *
from datetime import date
import inspect
from opensilexClientToolsPython.api_client import ApiClient


class SystemApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        
    def get_version_info(
        self,
        **kwargs
    ):  # noqa: E501
        """get system information  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_version_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: VersionInfoDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        frame = inspect.currentframe()
        keys, _, _, values = inspect.getargvalues(frame)
        passed_arguments = {}
        for key in keys:
            if key != 'self' and key not in [] and values[key] != None:
                passed_arguments[key] = values[key]
        kwargs['_return_http_data_only'] = True

        
        


        if kwargs.get('async_req'):
            return self.get_version_info_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.get_version_info_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
            return data

    def get_version_info_with_http_info(self, **kwargs):  # noqa: E501
        """get system information  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_version_info_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: VersionInfoDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_version_info" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/core/system/info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VersionInfoDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
