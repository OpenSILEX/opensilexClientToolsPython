# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: INSTANCE-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MultiPolygon(object):
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
        'bbox': 'list[float]',
        'coordinates': 'list[list[list[LngLatAlt]]]'
    }

    attribute_map = {
        'type': 'type',
        'bbox': 'bbox',
        'coordinates': 'coordinates'
    }

    def __init__(self, type=None, bbox=None, coordinates=None):  # noqa: E501
        """MultiPolygon - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._bbox = None
        self._coordinates = None
        self.discriminator = None

        self.type = type
        if bbox is not None:
            self.bbox = bbox
        if coordinates is not None:
            self.coordinates = coordinates

    @property
    def type(self):
        """Gets the type of this MultiPolygon.  # noqa: E501


        :return: The type of this MultiPolygon.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MultiPolygon.


        :param type: The type of this MultiPolygon.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Feature", "Polygon", "MultiPolygon", "FeatureCollection", "Point", "MultiPoint", "MultiLineString", "LineString", "GeometryCollection"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def bbox(self):
        """Gets the bbox of this MultiPolygon.  # noqa: E501


        :return: The bbox of this MultiPolygon.  # noqa: E501
        :rtype: list[float]
        """
        return self._bbox

    @bbox.setter
    def bbox(self, bbox):
        """Sets the bbox of this MultiPolygon.


        :param bbox: The bbox of this MultiPolygon.  # noqa: E501
        :type: list[float]
        """

        self._bbox = bbox

    @property
    def coordinates(self):
        """Gets the coordinates of this MultiPolygon.  # noqa: E501


        :return: The coordinates of this MultiPolygon.  # noqa: E501
        :rtype: list[list[list[LngLatAlt]]]
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this MultiPolygon.


        :param coordinates: The coordinates of this MultiPolygon.  # noqa: E501
        :type: list[list[list[LngLatAlt]]]
        """

        self._coordinates = coordinates

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
        if issubclass(MultiPolygon, dict):
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
        if not isinstance(other, MultiPolygon):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
