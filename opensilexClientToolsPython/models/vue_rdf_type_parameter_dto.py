# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.00-rc+5.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict




class VueRDFTypeParameterDTO(object):
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
        'uri': 'str',
        'icon': 'str',
        'is_abstract': 'bool'
    }

    attribute_map = {
        'uri': 'uri',
        'icon': 'icon',
        'is_abstract': 'is_abstract'
    }
    def __init__(self, uri : 'str' = None, icon : 'str' = None, is_abstract : 'bool' = None):  # noqa: E501
        """VueRDFTypeParameterDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._icon = None
        self._is_abstract = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if icon is not None:
            self.icon = icon
        if is_abstract is not None:
            self.is_abstract = is_abstract

    @property
    def uri(self):
        """Gets the uri of this VueRDFTypeParameterDTO.  # noqa: E501


        :return: The uri of this VueRDFTypeParameterDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this VueRDFTypeParameterDTO.


        :param uri: The uri of this VueRDFTypeParameterDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def icon(self):
        """Gets the icon of this VueRDFTypeParameterDTO.  # noqa: E501


        :return: The icon of this VueRDFTypeParameterDTO.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this VueRDFTypeParameterDTO.


        :param icon: The icon of this VueRDFTypeParameterDTO.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def is_abstract(self):
        """Gets the is_abstract of this VueRDFTypeParameterDTO.  # noqa: E501


        :return: The is_abstract of this VueRDFTypeParameterDTO.  # noqa: E501
        :rtype: bool
        """
        return self._is_abstract

    @is_abstract.setter
    def is_abstract(self, is_abstract):
        """Sets the is_abstract of this VueRDFTypeParameterDTO.


        :param is_abstract: The is_abstract of this VueRDFTypeParameterDTO.  # noqa: E501
        :type: bool
        """

        self._is_abstract = is_abstract

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
        if issubclass(VueRDFTypeParameterDTO, dict):
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
        if not isinstance(other, VueRDFTypeParameterDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

