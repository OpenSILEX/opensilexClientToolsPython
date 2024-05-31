# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.2.7-rdg
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict


class MetricPeriodDTO(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'start_date': 'int',
        'end_date': 'int',
        'scientific_object_list': 'CountListItemPeriodDTO',
        'experiment_list': 'CountListItemPeriodDTO',
        'data_list': 'CountListItemPeriodDTO',
        'device_list': 'CountListItemPeriodDTO',
        'germplasm_list': 'CountListItemPeriodDTO'
    }

    attribute_map = {
        'start_date': 'start_date',
        'end_date': 'end_date',
        'scientific_object_list': 'scientific_object_list',
        'experiment_list': 'experiment_list',
        'data_list': 'data_list',
        'device_list': 'device_list',
        'germplasm_list': 'germplasm_list'
    }
    def __init__(self,
        start_date : 'int' = None,
        end_date : 'int' = None,
        scientific_object_list : 'CountListItemPeriodDTO' = None,
        experiment_list : 'CountListItemPeriodDTO' = None,
        data_list : 'CountListItemPeriodDTO' = None,
        device_list : 'CountListItemPeriodDTO' = None,
        germplasm_list : 'CountListItemPeriodDTO' = None):  # noqa: E501
        """MetricPeriodDTO - a model defined in Swagger"""  # noqa: E501

        self._start_date = None
        self._end_date = None
        self._scientific_object_list = None
        self._experiment_list = None
        self._data_list = None
        self._device_list = None
        self._germplasm_list = None
        self.discriminator = None

        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if scientific_object_list is not None:
            self.scientific_object_list = scientific_object_list
        if experiment_list is not None:
            self.experiment_list = experiment_list
        if data_list is not None:
            self.data_list = data_list
        if device_list is not None:
            self.device_list = device_list
        if germplasm_list is not None:
            self.germplasm_list = germplasm_list

    @property
    def start_date(self):
        """Gets the start_date of this MetricPeriodDTO.  # noqa: E501


        :return: The start_date of this MetricPeriodDTO.  # noqa: E501
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this MetricPeriodDTO.


        :param start_date: The start_date of this MetricPeriodDTO.  # noqa: E501
        :type: int
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this MetricPeriodDTO.  # noqa: E501


        :return: The end_date of this MetricPeriodDTO.  # noqa: E501
        :rtype: int
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this MetricPeriodDTO.


        :param end_date: The end_date of this MetricPeriodDTO.  # noqa: E501
        :type: int
        """

        self._end_date = end_date

    @property
    def scientific_object_list(self):
        """Gets the scientific_object_list of this MetricPeriodDTO.  # noqa: E501


        :return: The scientific_object_list of this MetricPeriodDTO.  # noqa: E501
        :rtype: CountListItemPeriodDTO
        """
        return self._scientific_object_list

    @scientific_object_list.setter
    def scientific_object_list(self, scientific_object_list):
        """Sets the scientific_object_list of this MetricPeriodDTO.


        :param scientific_object_list: The scientific_object_list of this MetricPeriodDTO.  # noqa: E501
        :type: CountListItemPeriodDTO
        """

        self._scientific_object_list = scientific_object_list

    @property
    def experiment_list(self):
        """Gets the experiment_list of this MetricPeriodDTO.  # noqa: E501


        :return: The experiment_list of this MetricPeriodDTO.  # noqa: E501
        :rtype: CountListItemPeriodDTO
        """
        return self._experiment_list

    @experiment_list.setter
    def experiment_list(self, experiment_list):
        """Sets the experiment_list of this MetricPeriodDTO.


        :param experiment_list: The experiment_list of this MetricPeriodDTO.  # noqa: E501
        :type: CountListItemPeriodDTO
        """

        self._experiment_list = experiment_list

    @property
    def data_list(self):
        """Gets the data_list of this MetricPeriodDTO.  # noqa: E501


        :return: The data_list of this MetricPeriodDTO.  # noqa: E501
        :rtype: CountListItemPeriodDTO
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        """Sets the data_list of this MetricPeriodDTO.


        :param data_list: The data_list of this MetricPeriodDTO.  # noqa: E501
        :type: CountListItemPeriodDTO
        """

        self._data_list = data_list

    @property
    def device_list(self):
        """Gets the device_list of this MetricPeriodDTO.  # noqa: E501


        :return: The device_list of this MetricPeriodDTO.  # noqa: E501
        :rtype: CountListItemPeriodDTO
        """
        return self._device_list

    @device_list.setter
    def device_list(self, device_list):
        """Sets the device_list of this MetricPeriodDTO.


        :param device_list: The device_list of this MetricPeriodDTO.  # noqa: E501
        :type: CountListItemPeriodDTO
        """

        self._device_list = device_list

    @property
    def germplasm_list(self):
        """Gets the germplasm_list of this MetricPeriodDTO.  # noqa: E501


        :return: The germplasm_list of this MetricPeriodDTO.  # noqa: E501
        :rtype: CountListItemPeriodDTO
        """
        return self._germplasm_list

    @germplasm_list.setter
    def germplasm_list(self, germplasm_list):
        """Sets the germplasm_list of this MetricPeriodDTO.


        :param germplasm_list: The germplasm_list of this MetricPeriodDTO.  # noqa: E501
        :type: CountListItemPeriodDTO
        """

        self._germplasm_list = germplasm_list

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MetricPeriodDTO, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_api_formated_dict(self):
        """Returns a dict of properties as named in the API rather than in the model itself"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map[attr]] = list(map(
                    lambda x: x.to_api_formated_dict() if hasattr(x, "to_api_formated_dict") else x,
                    value
                ))
            elif hasattr(value, "to_api_formated_dict"):
                result[self.attribute_map[attr]] = value.to_api_formated_dict()
            elif isinstance(value, dict):
                result[self.attribute_map[attr]] = dict(map(
                    lambda item: (item[0], item[1].to_api_formated_dict())
                    if hasattr(item[1], "to_api_formated_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map[attr]] = value
        if issubclass(MetricPeriodDTO, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MetricPeriodDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.count_list_item_period_dto import CountListItemPeriodDTO
from opensilexClientToolsPython.models.count_list_item_period_dto import CountListItemPeriodDTO
from opensilexClientToolsPython.models.count_list_item_period_dto import CountListItemPeriodDTO
from opensilexClientToolsPython.models.count_list_item_period_dto import CountListItemPeriodDTO
from opensilexClientToolsPython.models.count_list_item_period_dto import CountListItemPeriodDTO


