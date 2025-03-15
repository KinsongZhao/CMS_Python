# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.inline_object import InlineObject  # noqa: E501
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_article_add_post(self):
        """Test case for article_add_post

        新增文章
        """
        inline_object = {}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/article/add',
            method='POST',
            headers=headers,
            data=json.dumps(inline_object),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_article_content_get(self):
        """Test case for article_content_get

        获取文章内容
        """
        query_string = [('article_id', 56)]
        headers = { 
        }
        response = self.client.open(
            '/article/content',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_article_del_post(self):
        """Test case for article_del_post

        删除文章
        """
        query_string = [('article_id', 56)]
        headers = { 
        }
        response = self.client.open(
            '/article/del',
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_article_divide_post(self):
        """Test case for article_divide_post

        划分文章到栏目
        """
        query_string = [('article_id', 56),
                        ('category_id', 56)]
        headers = { 
        }
        response = self.client.open(
            '/article/divide',
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_article_list_get(self):
        """Test case for article_list_get

        获取栏目内文章列表
        """
        query_string = [('category_id', 56)]
        headers = { 
        }
        response = self.client.open(
            '/article/list',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_category_add_post(self):
        """Test case for category_add_post

        新增栏目
        """
        query_string = [('category', 'category_example')]
        headers = { 
        }
        response = self.client.open(
            '/category/add',
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_category_del_post(self):
        """Test case for category_del_post

        删除栏目
        """
        query_string = [('category_id', 56)]
        headers = { 
        }
        response = self.client.open(
            '/category/del',
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_category_list_get(self):
        """Test case for category_list_get

        获取栏目列表
        """
        headers = { 
        }
        response = self.client.open(
            '/category/list',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_file_download_post(self):
        """Test case for file_download_post

        文件下载
        """
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'multipart/form-data',
        }
        response = self.client.open(
            '/file/download',
            method='POST',
            headers=headers,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_file_upload_post(self):
        """Test case for file_upload_post

        文件上传
        """
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'multipart/form-data',
        }
        data = dict(file=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/file/upload',
            method='POST',
            headers=headers,
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_system_add_post(self):
        """Test case for system_add_post

        新增系统字段
        """
        query_string = [('key', 'key_example'),
                        ('value', 'value_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/system/add',
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_system_del_post(self):
        """Test case for system_del_post

        删除系统字段
        """
        query_string = [('key', 'key_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/system/del',
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_system_list_get(self):
        """Test case for system_list_get

        获取系统字段
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/system/list',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_system_update_post(self):
        """Test case for system_update_post

        修改系统字段
        """
        query_string = [('key', 'key_example'),
                        ('value', 'value_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/system/update',
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
