# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.2.7-rdg
    
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


class ProjectsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        
    def create_project(
        self,
        body : 'ProjectCreationDTO' = None,
        **kwargs
    ):  # noqa: E501
        """Add a project  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_project(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param ProjectCreationDTO body: Project description
        :param str accept_language: Request accepted language
        :return: str
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

        
        
        if not isinstance(body, ProjectCreationDTO) and body != None:
            raise ValueError("Invalid value for parameter `body`. This parameter couldn't be cast to type `ProjectCreationDTO`")
                 


        if kwargs.get('async_req'):
            return self.create_project_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.create_project_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
            return data

    def create_project_with_http_info(self, **kwargs):  # noqa: E501
        """Add a project  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_project_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param ProjectCreationDTO body: Project description
        :param str accept_language: Request accepted language
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_project" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        #if 'authorization' in params:
        #    header_params['Authorization'] = params['authorization']  # noqa: E501
        #if 'accept_language' in params:
        #    header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/core/projects', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        
    def delete_project(
        self,
        uri : 'str',
        **kwargs
    ):  # noqa: E501
        """Delete a project  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_project(uri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uri: Project URI (required)
        :param str authorization: Authentication token (required)
        :param str accept_language: Request accepted language
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        frame = inspect.currentframe()
        keys, _, _, values = inspect.getargvalues(frame)
        passed_arguments = {}
        for key in keys:
            if key != 'self' and key not in ["uri", ] and values[key] != None:
                passed_arguments[key] = values[key]
        kwargs['_return_http_data_only'] = True

        
        
        if not isinstance(uri, str) and uri != None:
            raise ValueError("Invalid value for parameter `uri`. This parameter couldn't be cast to type `str`")
             


        if kwargs.get('async_req'):
            return self.delete_project_with_http_info(uri, **passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_project_with_http_info(uri, **passed_arguments, **kwargs)  # noqa: E501
            return data

    def delete_project_with_http_info(self, uri, **kwargs):  # noqa: E501
        """Delete a project  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_project_with_http_info(uri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uri: Project URI (required)
        :param str authorization: Authentication token (required)
        :param str accept_language: Request accepted language
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uri', ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uri' is set
        if ('uri' not in params or
                params['uri'] is None):
            raise ValueError("Missing the required parameter `uri` when calling `delete_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uri' in params:
            path_params['uri'] = params['uri']  # noqa: E501

        query_params = []

        header_params = {}
        #if 'authorization' in params:
        #    header_params['Authorization'] = params['authorization']  # noqa: E501
        #if 'accept_language' in params:
        #    header_params['Accept-Language'] = params['accept_language']  # noqa: E501

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
            '/core/projects/{uri}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        
    def get_project(
        self,
        uri : 'str',
        **kwargs
    ):  # noqa: E501
        """Get a project  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project(uri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uri: Project URI (required)
        :param str authorization: Authentication token (required)
        :param str accept_language: Request accepted language
        :return: ProjectGetDetailDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        frame = inspect.currentframe()
        keys, _, _, values = inspect.getargvalues(frame)
        passed_arguments = {}
        for key in keys:
            if key != 'self' and key not in ["uri", ] and values[key] != None:
                passed_arguments[key] = values[key]
        kwargs['_return_http_data_only'] = True

        
        
        if not isinstance(uri, str) and uri != None:
            raise ValueError("Invalid value for parameter `uri`. This parameter couldn't be cast to type `str`")
             


        if kwargs.get('async_req'):
            return self.get_project_with_http_info(uri, **passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.get_project_with_http_info(uri, **passed_arguments, **kwargs)  # noqa: E501
            return data

    def get_project_with_http_info(self, uri, **kwargs):  # noqa: E501
        """Get a project  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_with_http_info(uri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uri: Project URI (required)
        :param str authorization: Authentication token (required)
        :param str accept_language: Request accepted language
        :return: ProjectGetDetailDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uri', ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uri' is set
        if ('uri' not in params or
                params['uri'] is None):
            raise ValueError("Missing the required parameter `uri` when calling `get_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uri' in params:
            path_params['uri'] = params['uri']  # noqa: E501

        query_params = []

        header_params = {}
        #if 'authorization' in params:
        #    header_params['Authorization'] = params['authorization']  # noqa: E501
        #if 'accept_language' in params:
        #    header_params['Accept-Language'] = params['accept_language']  # noqa: E501

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
            '/core/projects/{uri}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProjectGetDetailDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        
    def get_projects_by_uri(
        self,
        uris : 'List[str]',
        **kwargs
    ):  # noqa: E501
        """Get projects by their URIs  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_projects_by_uri(uris, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] uris: Projects URIs (required)
        :param str authorization: Authentication token (required)
        :param str accept_language: Request accepted language
        :return: list[ProjectGetDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        frame = inspect.currentframe()
        keys, _, _, values = inspect.getargvalues(frame)
        passed_arguments = {}
        for key in keys:
            if key != 'self' and key not in ["uris", ] and values[key] != None:
                passed_arguments[key] = values[key]
        kwargs['_return_http_data_only'] = True

        
        
        if (not isinstance(uris, list) or not isinstance(uris[0], str)) and uris != None:
            raise ValueError("Invalid value for parameter `uris`. This parameter couldn't be cast to type `List[str]`")
             


        if kwargs.get('async_req'):
            return self.get_projects_by_uri_with_http_info(uris, **passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.get_projects_by_uri_with_http_info(uris, **passed_arguments, **kwargs)  # noqa: E501
            return data

    def get_projects_by_uri_with_http_info(self, uris, **kwargs):  # noqa: E501
        """Get projects by their URIs  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_projects_by_uri_with_http_info(uris, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] uris: Projects URIs (required)
        :param str authorization: Authentication token (required)
        :param str accept_language: Request accepted language
        :return: list[ProjectGetDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uris', ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_projects_by_uri" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uris' is set
        if ('uris' not in params or
                params['uris'] is None):
            raise ValueError("Missing the required parameter `uris` when calling `get_projects_by_uri`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uris' in params:
            query_params.append(('uris', params['uris']))  # noqa: E501
            collection_formats['uris'] = 'multi'  # noqa: E501

        header_params = {}
        #if 'authorization' in params:
        #    header_params['Authorization'] = params['authorization']  # noqa: E501
        #if 'accept_language' in params:
        #    header_params['Accept-Language'] = params['accept_language']  # noqa: E501

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
            '/core/projects/by_uris', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ProjectGetDTO]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        
    def search_projects(
        self,
        name : 'str' = None,
        year : 'int' = None,
        keyword : 'str' = None,
        financial_funding : 'str' = None,
        order_by : 'List[str]' = None,
        page : 'int' = None,
        page_size : 'int' = None,
        **kwargs
    ):  # noqa: E501
        """Search projects  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_projects(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param str name: Regex pattern for filtering by name or shortname
        :param int year: Search by year
        :param str keyword: Regex pattern for filtering on description or objective
        :param str financial_funding: Regex pattern for filtering by financial funding
        :param list[str] order_by: List of fields to sort as an array of fieldName=asc|desc
        :param int page: Page number
        :param int page_size: Page size
        :param str accept_language: Request accepted language
        :return: list[ProjectGetDTO]
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

        
        
        if not isinstance(name, str) and name != None:
            raise ValueError("Invalid value for parameter `name`. This parameter couldn't be cast to type `str`")
                 
        if not isinstance(year, int) and year != None:
            raise ValueError("Invalid value for parameter `year`. This parameter couldn't be cast to type `int`")
                 
        if not isinstance(keyword, str) and keyword != None:
            raise ValueError("Invalid value for parameter `keyword`. This parameter couldn't be cast to type `str`")
                 
        if not isinstance(financial_funding, str) and financial_funding != None:
            raise ValueError("Invalid value for parameter `financial_funding`. This parameter couldn't be cast to type `str`")
                 
        if (not isinstance(order_by, list) or not isinstance(order_by[0], str)) and order_by != None:
            raise ValueError("Invalid value for parameter `order_by`. This parameter couldn't be cast to type `List[str]`")
                 
        if not isinstance(page, int) and page != None:
            raise ValueError("Invalid value for parameter `page`. This parameter couldn't be cast to type `int`")
                 
        if not isinstance(page_size, int) and page_size != None:
            raise ValueError("Invalid value for parameter `page_size`. This parameter couldn't be cast to type `int`")
                 


        if kwargs.get('async_req'):
            return self.search_projects_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.search_projects_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
            return data

    def search_projects_with_http_info(self, **kwargs):  # noqa: E501
        """Search projects  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_projects_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param str name: Regex pattern for filtering by name or shortname
        :param int year: Search by year
        :param str keyword: Regex pattern for filtering on description or objective
        :param str financial_funding: Regex pattern for filtering by financial funding
        :param list[str] order_by: List of fields to sort as an array of fieldName=asc|desc
        :param int page: Page number
        :param int page_size: Page size
        :param str accept_language: Request accepted language
        :return: list[ProjectGetDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'year', 'keyword', 'financial_funding', 'order_by', 'page', 'page_size', ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_projects" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page' in params and params['page'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `search_projects`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'page_size' in params and params['page_size'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `search_projects`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'financial_funding' in params:
            query_params.append(('financial_funding', params['financial_funding']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))  # noqa: E501
            collection_formats['order_by'] = 'multi'  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501

        header_params = {}
        #if 'authorization' in params:
        #    header_params['Authorization'] = params['authorization']  # noqa: E501
        #if 'accept_language' in params:
        #    header_params['Accept-Language'] = params['accept_language']  # noqa: E501

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
            '/core/projects', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ProjectGetDTO]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        
    def update_project(
        self,
        body : 'ProjectCreationDTO' = None,
        **kwargs
    ):  # noqa: E501
        """Update a project  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_project(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param ProjectCreationDTO body: Project description
        :param str accept_language: Request accepted language
        :return: str
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

        
        
        if not isinstance(body, ProjectCreationDTO) and body != None:
            raise ValueError("Invalid value for parameter `body`. This parameter couldn't be cast to type `ProjectCreationDTO`")
                 


        if kwargs.get('async_req'):
            return self.update_project_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.update_project_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
            return data

    def update_project_with_http_info(self, **kwargs):  # noqa: E501
        """Update a project  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_project_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param ProjectCreationDTO body: Project description
        :param str accept_language: Request accepted language
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_project" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        #if 'authorization' in params:
        #    header_params['Authorization'] = params['authorization']  # noqa: E501
        #if 'accept_language' in params:
        #    header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/core/projects', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
