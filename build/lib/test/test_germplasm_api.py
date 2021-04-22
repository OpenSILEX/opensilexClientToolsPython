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
from opensilexClientToolsPython.api.germplasm_api import GermplasmApi  # noqa: E501
from opensilexClientToolsPython.rest import ApiException


class TestGermplasmApi(unittest.TestCase):
    """GermplasmApi unit test stubs"""

    def setUp(self):
        self.api = opensilexClientToolsPython.api.germplasm_api.GermplasmApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_germplasm(self):
        """Test case for create_germplasm

        Add a germplasm  # noqa: E501
        """
        pass

    def test_delete_germplasm(self):
        """Test case for delete_germplasm

        Delete a germplasm  # noqa: E501
        """
        pass

    def test_export_germplasm(self):
        """Test case for export_germplasm

        export germplasm  # noqa: E501
        """
        pass

    def test_export_germplasm_by_ur_is(self):
        """Test case for export_germplasm_by_ur_is

        export germplasm by list of uris  # noqa: E501
        """
        pass

    def test_get_germplasm(self):
        """Test case for get_germplasm

        Get a germplasm  # noqa: E501
        """
        pass

    def test_get_germplasm_experiments(self):
        """Test case for get_germplasm_experiments

        Get experiments where a germplasm has been used  # noqa: E501
        """
        pass

    def test_get_germplasms_by_uri(self):
        """Test case for get_germplasms_by_uri

        Get a list of germplasms by their URIs  # noqa: E501
        """
        pass

    def test_search_germplasm(self):
        """Test case for search_germplasm

        Search germplasm  # noqa: E501
        """
        pass

    def test_update_germplasm(self):
        """Test case for update_germplasm

        Update a germplasm  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
