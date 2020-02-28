# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from sib_api_v3_sdk.api_client import ApiClient


class FoldersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_folder(self, create_folder, **kwargs):  # noqa: E501
        """Create a folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass _async=True
        >>> thread = api.create_folder(create_folder, _async=True)
        >>> result = thread.get()

        :param async bool
        :param CreateUpdateFolder create_folder: Name of the folder (required)
        :return: CreateModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_folder_with_http_info(create_folder, **kwargs)  # noqa: E501
        else:
            (data) = self.create_folder_with_http_info(create_folder, **kwargs)  # noqa: E501
            return data

    def create_folder_with_http_info(self, create_folder, **kwargs):  # noqa: E501
        """Create a folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass _async=True
        >>> thread = api.create_folder_with_http_info(create_folder, _async=True)
        >>> result = thread.get()

        :param async bool
        :param CreateUpdateFolder create_folder: Name of the folder (required)
        :return: CreateModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_folder']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_folder' is set
        if ('create_folder' not in params or
                params['create_folder'] is None):
            raise ValueError("Missing the required parameter `create_folder` when calling `create_folder`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_folder' in params:
            body_params = params['create_folder']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/contacts/folders', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateModel',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_folder(self, folder_id, **kwargs):  # noqa: E501
        """Delete a folder (and all its lists)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass _async=True
        >>> thread = api.delete_folder(folder_id, _async=True)
        >>> result = thread.get()

        :param async bool
        :param int folder_id: Id of the folder (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_folder_with_http_info(folder_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_folder_with_http_info(folder_id, **kwargs)  # noqa: E501
            return data

    def delete_folder_with_http_info(self, folder_id, **kwargs):  # noqa: E501
        """Delete a folder (and all its lists)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass _async=True
        >>> thread = api.delete_folder_with_http_info(folder_id, _async=True)
        >>> result = thread.get()

        :param async bool
        :param int folder_id: Id of the folder (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folder_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folder_id' is set
        if ('folder_id' not in params or
                params['folder_id'] is None):
            raise ValueError("Missing the required parameter `folder_id` when calling `delete_folder`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'folder_id' in params:
            path_params['folderId'] = params['folder_id']  # noqa: E501

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
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/contacts/folders/{folderId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_folder(self, folder_id, **kwargs):  # noqa: E501
        """Returns folder details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass _async=True
        >>> thread = api.get_folder(folder_id, _async=True)
        >>> result = thread.get()

        :param async bool
        :param int folder_id: id of the folder (required)
        :return: GetFolder
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_folder_with_http_info(folder_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_folder_with_http_info(folder_id, **kwargs)  # noqa: E501
            return data

    def get_folder_with_http_info(self, folder_id, **kwargs):  # noqa: E501
        """Returns folder details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass _async=True
        >>> thread = api.get_folder_with_http_info(folder_id, _async=True)
        >>> result = thread.get()

        :param async bool
        :param int folder_id: id of the folder (required)
        :return: GetFolder
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folder_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folder_id' is set
        if ('folder_id' not in params or
                params['folder_id'] is None):
            raise ValueError("Missing the required parameter `folder_id` when calling `get_folder`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'folder_id' in params:
            path_params['folderId'] = params['folder_id']  # noqa: E501

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
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/contacts/folders/{folderId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetFolder',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_folder_lists(self, folder_id, **kwargs):  # noqa: E501
        """Get the lists in a folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass _async=True
        >>> thread = api.get_folder_lists(folder_id, _async=True)
        >>> result = thread.get()

        :param async bool
        :param int folder_id: Id of the folder (required)
        :param int limit: Number of documents per page
        :param int offset: Index of the first document of the page
        :return: GetFolderLists
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_folder_lists_with_http_info(folder_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_folder_lists_with_http_info(folder_id, **kwargs)  # noqa: E501
            return data

    def get_folder_lists_with_http_info(self, folder_id, **kwargs):  # noqa: E501
        """Get the lists in a folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass _async=True
        >>> thread = api.get_folder_lists_with_http_info(folder_id, _async=True)
        >>> result = thread.get()

        :param async bool
        :param int folder_id: Id of the folder (required)
        :param int limit: Number of documents per page
        :param int offset: Index of the first document of the page
        :return: GetFolderLists
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folder_id', 'limit', 'offset']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_folder_lists" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folder_id' is set
        if ('folder_id' not in params or
                params['folder_id'] is None):
            raise ValueError("Missing the required parameter `folder_id` when calling `get_folder_lists`")  # noqa: E501

        if 'limit' in params and params['limit'] > 50:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_folder_lists`, must be a value less than or equal to `50`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'folder_id' in params:
            path_params['folderId'] = params['folder_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

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
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/contacts/folders/{folderId}/lists', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetFolderLists',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_folders(self, limit, offset, **kwargs):  # noqa: E501
        """Get all the folders  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass _async=True
        >>> thread = api.get_folders(limit, offset, _async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: Number of documents per page (required)
        :param int offset: Index of the first document of the page (required)
        :return: GetFolders
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_folders_with_http_info(limit, offset, **kwargs)  # noqa: E501
        else:
            (data) = self.get_folders_with_http_info(limit, offset, **kwargs)  # noqa: E501
            return data

    def get_folders_with_http_info(self, limit, offset, **kwargs):  # noqa: E501
        """Get all the folders  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass _async=True
        >>> thread = api.get_folders_with_http_info(limit, offset, _async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: Number of documents per page (required)
        :param int offset: Index of the first document of the page (required)
        :return: GetFolders
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_folders" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'limit' is set
        if ('limit' not in params or
                params['limit'] is None):
            raise ValueError("Missing the required parameter `limit` when calling `get_folders`")  # noqa: E501
        # verify the required parameter 'offset' is set
        if ('offset' not in params or
                params['offset'] is None):
            raise ValueError("Missing the required parameter `offset` when calling `get_folders`")  # noqa: E501

        if 'limit' in params and params['limit'] > 50:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_folders`, must be a value less than or equal to `50`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

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
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/contacts/folders', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetFolders',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_folder(self, folder_id, update_folder, **kwargs):  # noqa: E501
        """Update a contact folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass _async=True
        >>> thread = api.update_folder(folder_id, update_folder, _async=True)
        >>> result = thread.get()

        :param async bool
        :param int folder_id: Id of the folder (required)
        :param CreateUpdateFolder update_folder: Name of the folder (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_folder_with_http_info(folder_id, update_folder, **kwargs)  # noqa: E501
        else:
            (data) = self.update_folder_with_http_info(folder_id, update_folder, **kwargs)  # noqa: E501
            return data

    def update_folder_with_http_info(self, folder_id, update_folder, **kwargs):  # noqa: E501
        """Update a contact folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass _async=True
        >>> thread = api.update_folder_with_http_info(folder_id, update_folder, _async=True)
        >>> result = thread.get()

        :param async bool
        :param int folder_id: Id of the folder (required)
        :param CreateUpdateFolder update_folder: Name of the folder (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folder_id', 'update_folder']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folder_id' is set
        if ('folder_id' not in params or
                params['folder_id'] is None):
            raise ValueError("Missing the required parameter `folder_id` when calling `update_folder`")  # noqa: E501
        # verify the required parameter 'update_folder' is set
        if ('update_folder' not in params or
                params['update_folder'] is None):
            raise ValueError("Missing the required parameter `update_folder` when calling `update_folder`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'folder_id' in params:
            path_params['folderId'] = params['folder_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_folder' in params:
            body_params = params['update_folder']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/contacts/folders/{folderId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
