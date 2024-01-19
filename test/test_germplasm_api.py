# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.2.0-rdg
    
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

    def test_create_germplasm_group(self):
        """Test case for create_germplasm_group

        Add a germplasm group  # noqa: E501
        """
        pass

    def test_delete_germplasm(self):
        """Test case for delete_germplasm

        Delete a germplasm  # noqa: E501
        """
        pass

    def test_delete_germplasm_group(self):
        """Test case for delete_germplasm_group

        Delete a germplasm group  # noqa: E501
        """
        pass

    def test_export_germplasm(self):
        """Test case for export_germplasm

        export germplasm  # noqa: E501
        """
        pass

    def test_get_germplasm(self):
        """Test case for get_germplasm

        Get a germplasm  # noqa: E501
        """
        pass

    def test_get_germplasm_attribute_values(self):
        """Test case for get_germplasm_attribute_values

        Get attribute values of all germplasm for a given attribute  # noqa: E501
        """
        pass

    def test_get_germplasm_attributes(self):
        """Test case for get_germplasm_attributes

        Get attributes of all germplasm  # noqa: E501
        """
        pass

    def test_get_germplasm_experiments(self):
        """Test case for get_germplasm_experiments

        Get experiments where a germplasm has been used  # noqa: E501
        """
        pass

    def test_get_germplasm_group(self):
        """Test case for get_germplasm_group

        Get a germplasm group  # noqa: E501
        """
        pass

    def test_get_germplasm_group_by_ur_is(self):
        """Test case for get_germplasm_group_by_ur_is

        Get germplasm groups by their URIs  # noqa: E501
        """
        pass

    def test_get_germplasm_group_content(self):
        """Test case for get_germplasm_group_content

        Get a germplasm group's germplasm, paginated  # noqa: E501
        """
        pass

    def test_get_germplasm_group_with_germplasms(self):
        """Test case for get_germplasm_group_with_germplasms

        Get a germplasm group with nested germplasm details  # noqa: E501
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

    def test_search_germplasm_groups(self):
        """Test case for search_germplasm_groups

        Search germplasm groups  # noqa: E501
        """
        pass

    def test_update_germplasm(self):
        """Test case for update_germplasm

        Update a germplasm  # noqa: E501
        """
        pass

    def test_update_germplasm_group(self):
        """Test case for update_germplasm_group

        Update a germplasm group  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
