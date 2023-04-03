# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0-rc+7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import opensilexClientToolsPython
from opensilexClientToolsPython.api.devices_api import DevicesApi  # noqa: E501
from opensilexClientToolsPython.rest import ApiException


class TestDevicesApi(unittest.TestCase):
    """DevicesApi unit test stubs"""

    def setUp(self):
        self.api = opensilexClientToolsPython.api.devices_api.DevicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_count_device_data(self):
        """Test case for count_device_data

        Count device data  # noqa: E501
        """
        pass

    def test_create_device(self):
        """Test case for create_device

        Create a device  # noqa: E501
        """
        pass

    def test_delete_device(self):
        """Test case for delete_device

        Delete a device  # noqa: E501
        """
        pass

    def test_export_devices(self):
        """Test case for export_devices

        export devices  # noqa: E501
        """
        pass

    def test_export_list(self):
        """Test case for export_list

        export devices  # noqa: E501
        """
        pass

    def test_get_device(self):
        """Test case for get_device

        Get device detail  # noqa: E501
        """
        pass

    def test_get_device_by_uris(self):
        """Test case for get_device_by_uris

        Get devices by uris  # noqa: E501
        """
        pass

    def test_get_device_data_files_provenances(self):
        """Test case for get_device_data_files_provenances

        Get provenances of datafiles linked to this device  # noqa: E501
        """
        pass

    def test_get_device_data_provenances(self):
        """Test case for get_device_data_provenances

        Get provenances of data that have been measured on this device  # noqa: E501
        """
        pass

    def test_get_device_facility(self):
        """Test case for get_device_facility

        Get device facility  # noqa: E501
        """
        pass

    def test_get_device_variables(self):
        """Test case for get_device_variables

        Get variables linked to the device  # noqa: E501
        """
        pass

    def test_import_csv(self):
        """Test case for import_csv

        Import a CSV file with one device per line  # noqa: E501
        """
        pass

    def test_search_device_data(self):
        """Test case for search_device_data

        Search device data  # noqa: E501
        """
        pass

    def test_search_device_datafiles(self):
        """Test case for search_device_datafiles

        Search device datafiles descriptions  # noqa: E501
        """
        pass

    def test_search_devices(self):
        """Test case for search_devices

        Search devices  # noqa: E501
        """
        pass

    def test_update_device(self):
        """Test case for update_device

        Update a device  # noqa: E501
        """
        pass

    def test_validate_csv1(self):
        """Test case for validate_csv1

        Validate the import of a CSV file with one device per line  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
