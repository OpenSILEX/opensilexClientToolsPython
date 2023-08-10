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


class AnnotationCreationDTO(object):
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
        'description': 'str',
        'targets': 'list[str]',
        'motivation': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'description': 'description',
        'targets': 'targets',
        'motivation': 'motivation'
    }
    def __init__(self,
        description : 'str',
        targets : 'List[str]',
        motivation : 'str',
        uri : 'str' = None):  # noqa: E501
        """AnnotationCreationDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._description = None
        self._targets = None
        self._motivation = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        self.description = description
        self.targets = targets
        self.motivation = motivation

    @property
    def uri(self):
        """Gets the uri of this AnnotationCreationDTO.  # noqa: E501


        :return: The uri of this AnnotationCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this AnnotationCreationDTO.


        :param uri: The uri of this AnnotationCreationDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def description(self):
        """Gets the description of this AnnotationCreationDTO.  # noqa: E501


        :return: The description of this AnnotationCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AnnotationCreationDTO.


        :param description: The description of this AnnotationCreationDTO.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def targets(self):
        """Gets the targets of this AnnotationCreationDTO.  # noqa: E501


        :return: The targets of this AnnotationCreationDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this AnnotationCreationDTO.


        :param targets: The targets of this AnnotationCreationDTO.  # noqa: E501
        :type: list[str]
        """
        if targets is None:
            raise ValueError("Invalid value for `targets`, must not be `None`")  # noqa: E501

        self._targets = targets

    @property
    def motivation(self):
        """Gets the motivation of this AnnotationCreationDTO.  # noqa: E501


        :return: The motivation of this AnnotationCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._motivation

    @motivation.setter
    def motivation(self, motivation):
        """Sets the motivation of this AnnotationCreationDTO.


        :param motivation: The motivation of this AnnotationCreationDTO.  # noqa: E501
        :type: str
        """
        if motivation is None:
            raise ValueError("Invalid value for `motivation`, must not be `None`")  # noqa: E501

        self._motivation = motivation

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
        if issubclass(AnnotationCreationDTO, dict):
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
        if not isinstance(other, AnnotationCreationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




