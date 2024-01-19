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


class ProfileCreationDTO(object):
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
        'name': 'str',
        'credentials': 'list[str]'
    }

    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'credentials': 'credentials'
    }
    def __init__(self,
        uri : 'str',
        name : 'str',
        credentials : 'List[str]'):  # noqa: E501
        """ProfileCreationDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._name = None
        self._credentials = None
        self.discriminator = None

        self.uri = uri
        self.name = name
        self.credentials = credentials

    @property
    def uri(self):
        """Gets the uri of this ProfileCreationDTO.  # noqa: E501

        User URI  # noqa: E501

        :return: The uri of this ProfileCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ProfileCreationDTO.

        User URI  # noqa: E501

        :param uri: The uri of this ProfileCreationDTO.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def name(self):
        """Gets the name of this ProfileCreationDTO.  # noqa: E501

        Profile name  # noqa: E501

        :return: The name of this ProfileCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProfileCreationDTO.

        Profile name  # noqa: E501

        :param name: The name of this ProfileCreationDTO.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def credentials(self):
        """Gets the credentials of this ProfileCreationDTO.  # noqa: E501

        Profile credentials  # noqa: E501

        :return: The credentials of this ProfileCreationDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this ProfileCreationDTO.

        Profile credentials  # noqa: E501

        :param credentials: The credentials of this ProfileCreationDTO.  # noqa: E501
        :type: list[str]
        """
        if credentials is None:
            raise ValueError("Invalid value for `credentials`, must not be `None`")  # noqa: E501

        self._credentials = credentials

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
        if issubclass(ProfileCreationDTO, dict):
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
        if not isinstance(other, ProfileCreationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




