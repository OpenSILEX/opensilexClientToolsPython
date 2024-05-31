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


class CountListItemDTO(object):
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
        'type': 'str',
        'name': 'str',
        'total_items_count': 'int',
        'items': 'list[CountItemDTO]'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'total_items_count': 'total_items_count',
        'items': 'items'
    }
    def __init__(self,
        type : 'str' = None,
        name : 'str' = None,
        total_items_count : 'int' = None,
        items : 'List[CountItemDTO]' = None):  # noqa: E501
        """CountListItemDTO - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._name = None
        self._total_items_count = None
        self._items = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if total_items_count is not None:
            self.total_items_count = total_items_count
        if items is not None:
            self.items = items

    @property
    def type(self):
        """Gets the type of this CountListItemDTO.  # noqa: E501


        :return: The type of this CountListItemDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CountListItemDTO.


        :param type: The type of this CountListItemDTO.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this CountListItemDTO.  # noqa: E501


        :return: The name of this CountListItemDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CountListItemDTO.


        :param name: The name of this CountListItemDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def total_items_count(self):
        """Gets the total_items_count of this CountListItemDTO.  # noqa: E501


        :return: The total_items_count of this CountListItemDTO.  # noqa: E501
        :rtype: int
        """
        return self._total_items_count

    @total_items_count.setter
    def total_items_count(self, total_items_count):
        """Sets the total_items_count of this CountListItemDTO.


        :param total_items_count: The total_items_count of this CountListItemDTO.  # noqa: E501
        :type: int
        """

        self._total_items_count = total_items_count

    @property
    def items(self):
        """Gets the items of this CountListItemDTO.  # noqa: E501


        :return: The items of this CountListItemDTO.  # noqa: E501
        :rtype: list[CountItemDTO]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this CountListItemDTO.


        :param items: The items of this CountListItemDTO.  # noqa: E501
        :type: list[CountItemDTO]
        """

        self._items = items

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
        if issubclass(CountListItemDTO, dict):
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
        if issubclass(CountListItemDTO, dict):
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
        if not isinstance(other, CountListItemDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.count_item_dto import CountItemDTO


