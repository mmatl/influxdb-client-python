# coding: utf-8

"""
Influx OSS API Service.

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six


class InvocableScriptsService(object):
    """NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):  # noqa: E501,D401,D403
        """InvocableScriptsService - a operation defined in OpenAPI."""
        if api_client is None:
            raise ValueError("Invalid value for `api_client`, must be defined.")
        self.api_client = api_client

    def delete_scripts_id(self, script_id, **kwargs):  # noqa: E501,D401,D403
        """Delete a script.

        Deletes a script and all associated records.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_scripts_id(script_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str script_id: The ID of the script to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_scripts_id_with_http_info(script_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_scripts_id_with_http_info(script_id, **kwargs)  # noqa: E501
            return data

    def delete_scripts_id_with_http_info(self, script_id, **kwargs):  # noqa: E501,D401,D403
        """Delete a script.

        Deletes a script and all associated records.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_scripts_id_with_http_info(script_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str script_id: The ID of the script to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params = locals()

        all_params = ['script_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('urlopen_kw')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_scripts_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'script_id' is set
        if ('script_id' not in local_var_params or
                local_var_params['script_id'] is None):
            raise ValueError("Missing the required parameter `script_id` when calling `delete_scripts_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'script_id' in local_var_params:
            path_params['scriptID'] = local_var_params['script_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        # urlopen optional setting
        urlopen_kw = None
        if 'urlopen_kw' in kwargs:
            urlopen_kw = kwargs['urlopen_kw']

        return self.api_client.call_api(
            '/api/v2/scripts/{scriptID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            urlopen_kw=urlopen_kw)

    def get_scripts(self, **kwargs):  # noqa: E501,D401,D403
        """List scripts.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scripts(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: The number of scripts to return.
        :param int offset: The offset for pagination.
        :return: Scripts
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_scripts_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_scripts_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_scripts_with_http_info(self, **kwargs):  # noqa: E501,D401,D403
        """List scripts.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scripts_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: The number of scripts to return.
        :param int offset: The offset for pagination.
        :return: Scripts
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params = locals()

        all_params = ['limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('urlopen_kw')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_scripts" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        # urlopen optional setting
        urlopen_kw = None
        if 'urlopen_kw' in kwargs:
            urlopen_kw = kwargs['urlopen_kw']

        return self.api_client.call_api(
            '/api/v2/scripts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Scripts',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            urlopen_kw=urlopen_kw)

    def get_scripts_id(self, script_id, **kwargs):  # noqa: E501,D401,D403
        """Retrieve a script.

        Uses script ID to retrieve details of an invocable script.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scripts_id(script_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str script_id: The script ID. (required)
        :return: Script
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_scripts_id_with_http_info(script_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_scripts_id_with_http_info(script_id, **kwargs)  # noqa: E501
            return data

    def get_scripts_id_with_http_info(self, script_id, **kwargs):  # noqa: E501,D401,D403
        """Retrieve a script.

        Uses script ID to retrieve details of an invocable script.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scripts_id_with_http_info(script_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str script_id: The script ID. (required)
        :return: Script
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params = locals()

        all_params = ['script_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('urlopen_kw')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_scripts_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'script_id' is set
        if ('script_id' not in local_var_params or
                local_var_params['script_id'] is None):
            raise ValueError("Missing the required parameter `script_id` when calling `get_scripts_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'script_id' in local_var_params:
            path_params['scriptID'] = local_var_params['script_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        # urlopen optional setting
        urlopen_kw = None
        if 'urlopen_kw' in kwargs:
            urlopen_kw = kwargs['urlopen_kw']

        return self.api_client.call_api(
            '/api/v2/scripts/{scriptID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Script',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            urlopen_kw=urlopen_kw)

    def patch_scripts_id(self, script_id, script_update_request, **kwargs):  # noqa: E501,D401,D403
        """Update a script.

        Updates properties (`name`, `description`, and `script`) of an invocable script.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_scripts_id(script_id, script_update_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str script_id: The script ID. (required)
        :param ScriptUpdateRequest script_update_request: Script update to apply (required)
        :return: Script
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_scripts_id_with_http_info(script_id, script_update_request, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_scripts_id_with_http_info(script_id, script_update_request, **kwargs)  # noqa: E501
            return data

    def patch_scripts_id_with_http_info(self, script_id, script_update_request, **kwargs):  # noqa: E501,D401,D403
        """Update a script.

        Updates properties (`name`, `description`, and `script`) of an invocable script.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_scripts_id_with_http_info(script_id, script_update_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str script_id: The script ID. (required)
        :param ScriptUpdateRequest script_update_request: Script update to apply (required)
        :return: Script
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params = locals()

        all_params = ['script_id', 'script_update_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('urlopen_kw')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_scripts_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'script_id' is set
        if ('script_id' not in local_var_params or
                local_var_params['script_id'] is None):
            raise ValueError("Missing the required parameter `script_id` when calling `patch_scripts_id`")  # noqa: E501
        # verify the required parameter 'script_update_request' is set
        if ('script_update_request' not in local_var_params or
                local_var_params['script_update_request'] is None):
            raise ValueError("Missing the required parameter `script_update_request` when calling `patch_scripts_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'script_id' in local_var_params:
            path_params['scriptID'] = local_var_params['script_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'script_update_request' in local_var_params:
            body_params = local_var_params['script_update_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        # urlopen optional setting
        urlopen_kw = None
        if 'urlopen_kw' in kwargs:
            urlopen_kw = kwargs['urlopen_kw']

        return self.api_client.call_api(
            '/api/v2/scripts/{scriptID}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Script',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            urlopen_kw=urlopen_kw)

    def post_scripts(self, script_create_request, **kwargs):  # noqa: E501,D401,D403
        """Create a script.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_scripts(script_create_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ScriptCreateRequest script_create_request: The script to create. (required)
        :return: Script
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_scripts_with_http_info(script_create_request, **kwargs)  # noqa: E501
        else:
            (data) = self.post_scripts_with_http_info(script_create_request, **kwargs)  # noqa: E501
            return data

    def post_scripts_with_http_info(self, script_create_request, **kwargs):  # noqa: E501,D401,D403
        """Create a script.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_scripts_with_http_info(script_create_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ScriptCreateRequest script_create_request: The script to create. (required)
        :return: Script
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params = locals()

        all_params = ['script_create_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('urlopen_kw')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_scripts" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'script_create_request' is set
        if ('script_create_request' not in local_var_params or
                local_var_params['script_create_request'] is None):
            raise ValueError("Missing the required parameter `script_create_request` when calling `post_scripts`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'script_create_request' in local_var_params:
            body_params = local_var_params['script_create_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        # urlopen optional setting
        urlopen_kw = None
        if 'urlopen_kw' in kwargs:
            urlopen_kw = kwargs['urlopen_kw']

        return self.api_client.call_api(
            '/api/v2/scripts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Script',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            urlopen_kw=urlopen_kw)

    def post_scripts_id_invoke(self, script_id, **kwargs):  # noqa: E501,D401,D403
        """Invoke a script.

        Invokes a script and substitutes `params` keys referenced in the script with `params` key-values sent in the request body.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_scripts_id_invoke(script_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str script_id: (required)
        :param ScriptInvocationParams script_invocation_params:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_scripts_id_invoke_with_http_info(script_id, **kwargs)  # noqa: E501
        else:
            (data) = self.post_scripts_id_invoke_with_http_info(script_id, **kwargs)  # noqa: E501
            return data

    def post_scripts_id_invoke_with_http_info(self, script_id, **kwargs):  # noqa: E501,D401,D403
        """Invoke a script.

        Invokes a script and substitutes `params` keys referenced in the script with `params` key-values sent in the request body.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_scripts_id_invoke_with_http_info(script_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str script_id: (required)
        :param ScriptInvocationParams script_invocation_params:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params = locals()

        all_params = ['script_id', 'script_invocation_params']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('urlopen_kw')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_scripts_id_invoke" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'script_id' is set
        if ('script_id' not in local_var_params or
                local_var_params['script_id'] is None):
            raise ValueError("Missing the required parameter `script_id` when calling `post_scripts_id_invoke`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'script_id' in local_var_params:
            path_params['scriptID'] = local_var_params['script_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'script_invocation_params' in local_var_params:
            body_params = local_var_params['script_invocation_params']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        # urlopen optional setting
        urlopen_kw = None
        if 'urlopen_kw' in kwargs:
            urlopen_kw = kwargs['urlopen_kw']

        return self.api_client.call_api(
            '/api/v2/scripts/{scriptID}/invoke', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            urlopen_kw=urlopen_kw)
