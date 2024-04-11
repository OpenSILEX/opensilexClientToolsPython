# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: BUILD-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import opensilexClientToolsPython
from opensilexClientToolsPython.api.metrics_api import MetricsApi  # noqa: E501
from opensilexClientToolsPython.rest import ApiException


class TestMetricsApi(unittest.TestCase):
    """MetricsApi unit test stubs"""

    def setUp(self):
        self.api = opensilexClientToolsPython.api.metrics_api.MetricsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_experiment_summary_history(self):
        """Test case for get_experiment_summary_history

        Get an experiment summary history  # noqa: E501
        """
        pass

    def test_get_running_experiments_summary(self):
        """Test case for get_running_experiments_summary

        Get running experiments metrics  # noqa: E501
        """
        pass

    def test_get_system_metrics(self):
        """Test case for get_system_metrics

        Get system metrics  # noqa: E501
        """
        pass

    def test_get_system_metrics_summary(self):
        """Test case for get_system_metrics_summary

        Get system metrics summary  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
