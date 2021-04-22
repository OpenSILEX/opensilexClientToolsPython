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


class CredentialsGroupDTO(object):
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
        'group_id': 'str',
        'group_key_name': 'str',
        'credentials': 'list[CredentialDTO]'
    }

    attribute_map = {
        'group_id': 'group_id',
        'group_key_name': 'group_key_name',
        'credentials': 'credentials'
    }

    def __init__(self, group_id=None, group_key_name=None, credentials=None):  # noqa: E501
        """CredentialsGroupDTO - a model defined in Swagger"""  # noqa: E501

        self._group_id = None
        self._group_key_name = None
        self._credentials = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if group_key_name is not None:
            self.group_key_name = group_key_name
        if credentials is not None:
            self.credentials = credentials

    @property
    def group_id(self):
        """Gets the group_id of this CredentialsGroupDTO.  # noqa: E501

        Credential group identifier  # noqa: E501

        :return: The group_id of this CredentialsGroupDTO.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this CredentialsGroupDTO.

        Credential group identifier  # noqa: E501

        :param group_id: The group_id of this CredentialsGroupDTO.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def group_key_name(self):
        """Gets the group_key_name of this CredentialsGroupDTO.  # noqa: E501

        Credential group key label  # noqa: E501

        :return: The group_key_name of this CredentialsGroupDTO.  # noqa: E501
        :rtype: str
        """
        return self._group_key_name

    @group_key_name.setter
    def group_key_name(self, group_key_name):
        """Sets the group_key_name of this CredentialsGroupDTO.

        Credential group key label  # noqa: E501

        :param group_key_name: The group_key_name of this CredentialsGroupDTO.  # noqa: E501
        :type: str
        """

        self._group_key_name = group_key_name

    @property
    def credentials(self):
        """Gets the credentials of this CredentialsGroupDTO.  # noqa: E501

        Credentials Map  # noqa: E501

        :return: The credentials of this CredentialsGroupDTO.  # noqa: E501
        :rtype: list[CredentialDTO]
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this CredentialsGroupDTO.

        Credentials Map  # noqa: E501

        :param credentials: The credentials of this CredentialsGroupDTO.  # noqa: E501
        :type: list[CredentialDTO]
        """

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
        if issubclass(CredentialsGroupDTO, dict):
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
        if not isinstance(other, CredentialsGroupDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
