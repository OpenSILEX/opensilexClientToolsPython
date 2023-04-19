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




class URITypesDTO(object):
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
        'rdf_types': 'list[str]'
    }

    attribute_map = {
        'uri': 'uri',
        'rdf_types': 'rdf_types'
    }
    def __init__(self,
        uri : 'str' = None,
        rdf_types : 'List[str]' = None):  # noqa: E501
        """URITypesDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._rdf_types = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if rdf_types is not None:
            self.rdf_types = rdf_types

    @property
    def uri(self):
        """Gets the uri of this URITypesDTO.  # noqa: E501


        :return: The uri of this URITypesDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this URITypesDTO.


        :param uri: The uri of this URITypesDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def rdf_types(self):
        """Gets the rdf_types of this URITypesDTO.  # noqa: E501


        :return: The rdf_types of this URITypesDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._rdf_types

    @rdf_types.setter
    def rdf_types(self, rdf_types):
        """Sets the rdf_types of this URITypesDTO.


        :param rdf_types: The rdf_types of this URITypesDTO.  # noqa: E501
        :type: list[str]
        """

        self._rdf_types = rdf_types

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
        if issubclass(URITypesDTO, dict):
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
        if not isinstance(other, URITypesDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

