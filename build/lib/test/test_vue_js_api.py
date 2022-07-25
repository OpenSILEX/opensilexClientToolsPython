# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: INSTANCE-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import opensilexClientToolsPython
from opensilexClientToolsPython.api.vue_js_api import VueJsApi  # noqa: E501
from opensilexClientToolsPython.rest import ApiException


class TestVueJsApi(unittest.TestCase):
    """VueJsApi unit test stubs"""

    def setUp(self):
        self.api = opensilexClientToolsPython.api.vue_js_api.VueJsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_config(self):
        """Test case for get_config

        Return the current configuration  # noqa: E501
        """
        pass

    def test_get_extension(self):
        """Test case for get_extension

        Return the front Vue JS extension file to include  # noqa: E501
        """
        pass

    def test_get_extension_style(self):
        """Test case for get_extension_style

        Return the front Vue JS extension css file to include  # noqa: E501
        """
        pass

    def test_get_theme_config(self):
        """Test case for get_theme_config

        Return the front Vue JS theme configuration  # noqa: E501
        """
        pass

    def test_get_theme_css(self):
        """Test case for get_theme_css

        Return the theme css file  # noqa: E501
        """
        pass

    def test_get_theme_resource(self):
        """Test case for get_theme_resource

        Return the theme requested resource  # noqa: E501
        """
        pass

    def test_get_user_config(self):
        """Test case for get_user_config

        Return the user-specific configuration  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
