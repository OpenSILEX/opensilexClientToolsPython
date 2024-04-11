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


class GeometryDTO(object):
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
        'geometry': 'GeoJsonObject'
    }

    attribute_map = {
        'uri': 'uri',
        'geometry': 'geometry'
    }
    def __init__(self,
        uri : 'str' = None,
        geometry : 'GeoJsonObject' = None):  # noqa: E501
        """GeometryDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._geometry = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if geometry is not None:
            self.geometry = geometry

    @property
    def uri(self):
        """Gets the uri of this GeometryDTO.  # noqa: E501

        Object URI  # noqa: E501

        :return: The uri of this GeometryDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this GeometryDTO.

        Object URI  # noqa: E501

        :param uri: The uri of this GeometryDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def geometry(self):
        """Gets the geometry of this GeometryDTO.  # noqa: E501


        :return: The geometry of this GeometryDTO.  # noqa: E501
        :rtype: GeoJsonObject
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this GeometryDTO.


        :param geometry: The geometry of this GeometryDTO.  # noqa: E501
        :type: GeoJsonObject
        """

        self._geometry = geometry

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
        if issubclass(GeometryDTO, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_api_formated_dict(self):
        """Returns the model properties as a dict"""
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
        if issubclass(GeometryDTO, dict):
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
        if not isinstance(other, GeometryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.geo_json_object import GeoJsonObject


