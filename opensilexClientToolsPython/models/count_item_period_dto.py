# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.2.0-rdg
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict


class CountItemPeriodDTO(object):
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
        'difference_count': 'int',
        'uri': 'str',
        'type': 'str',
        'name': 'str',
        'count': 'int'
    }

    attribute_map = {
        'difference_count': 'difference_count',
        'uri': 'uri',
        'type': 'type',
        'name': 'name',
        'count': 'count'
    }
    def __init__(self,
        difference_count : 'int' = None,
        uri : 'str' = None,
        type : 'str' = None,
        name : 'str' = None,
        count : 'int' = None):  # noqa: E501
        """CountItemPeriodDTO - a model defined in Swagger"""  # noqa: E501

        self._difference_count = None
        self._uri = None
        self._type = None
        self._name = None
        self._count = None
        self.discriminator = None

        if difference_count is not None:
            self.difference_count = difference_count
        if uri is not None:
            self.uri = uri
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if count is not None:
            self.count = count

    @property
    def difference_count(self):
        """Gets the difference_count of this CountItemPeriodDTO.  # noqa: E501


        :return: The difference_count of this CountItemPeriodDTO.  # noqa: E501
        :rtype: int
        """
        return self._difference_count

    @difference_count.setter
    def difference_count(self, difference_count):
        """Sets the difference_count of this CountItemPeriodDTO.


        :param difference_count: The difference_count of this CountItemPeriodDTO.  # noqa: E501
        :type: int
        """

        self._difference_count = difference_count

    @property
    def uri(self):
        """Gets the uri of this CountItemPeriodDTO.  # noqa: E501


        :return: The uri of this CountItemPeriodDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this CountItemPeriodDTO.


        :param uri: The uri of this CountItemPeriodDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def type(self):
        """Gets the type of this CountItemPeriodDTO.  # noqa: E501


        :return: The type of this CountItemPeriodDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CountItemPeriodDTO.


        :param type: The type of this CountItemPeriodDTO.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this CountItemPeriodDTO.  # noqa: E501


        :return: The name of this CountItemPeriodDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CountItemPeriodDTO.


        :param name: The name of this CountItemPeriodDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def count(self):
        """Gets the count of this CountItemPeriodDTO.  # noqa: E501


        :return: The count of this CountItemPeriodDTO.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this CountItemPeriodDTO.


        :param count: The count of this CountItemPeriodDTO.  # noqa: E501
        :type: int
        """

        self._count = count

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
        if issubclass(CountItemPeriodDTO, dict):
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
        if not isinstance(other, CountItemPeriodDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




