# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: BUILD-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict


class PrefixMapping(object):
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
        'ns_prefix_map': 'dict(str, str)'
    }

    attribute_map = {
        'ns_prefix_map': 'nsPrefixMap'
    }
    def __init__(self,
        ns_prefix_map : 'Dict[str, str]' = None):  # noqa: E501
        """PrefixMapping - a model defined in Swagger"""  # noqa: E501

        self._ns_prefix_map = None
        self.discriminator = None

        if ns_prefix_map is not None:
            self.ns_prefix_map = ns_prefix_map

    @property
    def ns_prefix_map(self):
        """Gets the ns_prefix_map of this PrefixMapping.  # noqa: E501


        :return: The ns_prefix_map of this PrefixMapping.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._ns_prefix_map

    @ns_prefix_map.setter
    def ns_prefix_map(self, ns_prefix_map):
        """Sets the ns_prefix_map of this PrefixMapping.


        :param ns_prefix_map: The ns_prefix_map of this PrefixMapping.  # noqa: E501
        :type: dict(str, str)
        """

        self._ns_prefix_map = ns_prefix_map

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
        if issubclass(PrefixMapping, dict):
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
        if not isinstance(other, PrefixMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




