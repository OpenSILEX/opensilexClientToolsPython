# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.00-rc+5.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import opensilexClientToolsPython
from opensilexClientToolsPython.api.positions_api import PositionsApi  # noqa: E501
from opensilexClientToolsPython.rest import ApiException


class TestPositionsApi(unittest.TestCase):
    """PositionsApi unit test stubs"""

    def setUp(self):
        self.api = opensilexClientToolsPython.api.positions_api.PositionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_position(self):
        """Test case for get_position

        Get the position of an object  # noqa: E501
        """
        pass

    def test_search_position_history(self):
        """Test case for search_position_history

        Search history of position of an object  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
