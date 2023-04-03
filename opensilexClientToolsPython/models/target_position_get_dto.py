# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0-rc+7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict

from opensilexClientToolsPython.models.position_get_detail_dto import PositionGetDetailDTO



class TargetPositionGetDTO(object):
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
        'target': 'str',
        'position': 'PositionGetDetailDTO'
    }

    attribute_map = {
        'target': 'target',
        'position': 'position'
    }
    def __init__(self,
        target : 'str' = None,
        position : 'PositionGetDetailDTO' = None):  # noqa: E501
        """TargetPositionGetDTO - a model defined in Swagger"""  # noqa: E501

        self._target = None
        self._position = None
        self.discriminator = None

        if target is not None:
            self.target = target
        if position is not None:
            self.position = position

    @property
    def target(self):
        """Gets the target of this TargetPositionGetDTO.  # noqa: E501


        :return: The target of this TargetPositionGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this TargetPositionGetDTO.


        :param target: The target of this TargetPositionGetDTO.  # noqa: E501
        :type: str
        """

        self._target = target

    @property
    def position(self):
        """Gets the position of this TargetPositionGetDTO.  # noqa: E501


        :return: The position of this TargetPositionGetDTO.  # noqa: E501
        :rtype: PositionGetDetailDTO
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this TargetPositionGetDTO.


        :param position: The position of this TargetPositionGetDTO.  # noqa: E501
        :type: PositionGetDetailDTO
        """

        self._position = position

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
        if issubclass(TargetPositionGetDTO, dict):
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
        if not isinstance(other, TargetPositionGetDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

