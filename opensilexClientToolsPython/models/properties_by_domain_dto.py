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


class PropertiesByDomainDTO(object):
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
        'domain': 'str',
        'properties': 'list[ResourceTreeDTO]'
    }

    attribute_map = {
        'domain': 'domain',
        'properties': 'properties'
    }
    def __init__(self,
        domain : 'str' = None,
        properties : 'List[ResourceTreeDTO]' = None):  # noqa: E501
        """PropertiesByDomainDTO - a model defined in Swagger"""  # noqa: E501

        self._domain = None
        self._properties = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if properties is not None:
            self.properties = properties

    @property
    def domain(self):
        """Gets the domain of this PropertiesByDomainDTO.  # noqa: E501


        :return: The domain of this PropertiesByDomainDTO.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this PropertiesByDomainDTO.


        :param domain: The domain of this PropertiesByDomainDTO.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def properties(self):
        """Gets the properties of this PropertiesByDomainDTO.  # noqa: E501


        :return: The properties of this PropertiesByDomainDTO.  # noqa: E501
        :rtype: list[ResourceTreeDTO]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this PropertiesByDomainDTO.


        :param properties: The properties of this PropertiesByDomainDTO.  # noqa: E501
        :type: list[ResourceTreeDTO]
        """

        self._properties = properties

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
        if issubclass(PropertiesByDomainDTO, dict):
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
        if issubclass(PropertiesByDomainDTO, dict):
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
        if not isinstance(other, PropertiesByDomainDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.resource_tree_dto import ResourceTreeDTO


