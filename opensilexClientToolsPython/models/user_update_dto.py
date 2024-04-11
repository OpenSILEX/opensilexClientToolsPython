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


class UserUpdateDTO(object):
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
        'first_name': 'str',
        'language': 'str',
        'password': 'str',
        'admin': 'bool',
        'last_name': 'str',
        'email': 'str',
        'enable': 'bool',
        'favorites': 'list[str]',
        'linked_person': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'first_name': 'first_name',
        'language': 'language',
        'password': 'password',
        'admin': 'admin',
        'last_name': 'last_name',
        'email': 'email',
        'enable': 'enable',
        'favorites': 'favorites',
        'linked_person': 'linked_person'
    }
    def __init__(self,
        uri : 'str',
        first_name : 'str',
        language : 'str',
        admin : 'bool',
        last_name : 'str',
        email : 'str',
        password : 'str' = None,
        enable : 'bool' = None,
        favorites : 'List[str]' = None,
        linked_person : 'str' = None):  # noqa: E501
        """UserUpdateDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._first_name = None
        self._language = None
        self._password = None
        self._admin = None
        self._last_name = None
        self._email = None
        self._enable = None
        self._favorites = None
        self._linked_person = None
        self.discriminator = None

        self.uri = uri
        self.first_name = first_name
        self.language = language
        if password is not None:
            self.password = password
        self.admin = admin
        self.last_name = last_name
        self.email = email
        if enable is not None:
            self.enable = enable
        if favorites is not None:
            self.favorites = favorites
        if linked_person is not None:
            self.linked_person = linked_person

    @property
    def uri(self):
        """Gets the uri of this UserUpdateDTO.  # noqa: E501

        User URI  # noqa: E501

        :return: The uri of this UserUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this UserUpdateDTO.

        User URI  # noqa: E501

        :param uri: The uri of this UserUpdateDTO.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def first_name(self):
        """Gets the first_name of this UserUpdateDTO.  # noqa: E501

        User first name  # noqa: E501

        :return: The first_name of this UserUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserUpdateDTO.

        User first name  # noqa: E501

        :param first_name: The first_name of this UserUpdateDTO.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def language(self):
        """Gets the language of this UserUpdateDTO.  # noqa: E501

        User language  # noqa: E501

        :return: The language of this UserUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this UserUpdateDTO.

        User language  # noqa: E501

        :param language: The language of this UserUpdateDTO.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def password(self):
        """Gets the password of this UserUpdateDTO.  # noqa: E501

        Optional user password  # noqa: E501

        :return: The password of this UserUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserUpdateDTO.

        Optional user password  # noqa: E501

        :param password: The password of this UserUpdateDTO.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def admin(self):
        """Gets the admin of this UserUpdateDTO.  # noqa: E501

        User admin flag  # noqa: E501

        :return: The admin of this UserUpdateDTO.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this UserUpdateDTO.

        User admin flag  # noqa: E501

        :param admin: The admin of this UserUpdateDTO.  # noqa: E501
        :type: bool
        """
        if admin is None:
            raise ValueError("Invalid value for `admin`, must not be `None`")  # noqa: E501

        self._admin = admin

    @property
    def last_name(self):
        """Gets the last_name of this UserUpdateDTO.  # noqa: E501

        User last name  # noqa: E501

        :return: The last_name of this UserUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserUpdateDTO.

        User last name  # noqa: E501

        :param last_name: The last_name of this UserUpdateDTO.  # noqa: E501
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this UserUpdateDTO.  # noqa: E501

        User email  # noqa: E501

        :return: The email of this UserUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserUpdateDTO.

        User email  # noqa: E501

        :param email: The email of this UserUpdateDTO.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def enable(self):
        """Gets the enable of this UserUpdateDTO.  # noqa: E501

        User is enable  # noqa: E501

        :return: The enable of this UserUpdateDTO.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this UserUpdateDTO.

        User is enable  # noqa: E501

        :param enable: The enable of this UserUpdateDTO.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def favorites(self):
        """Gets the favorites of this UserUpdateDTO.  # noqa: E501


        :return: The favorites of this UserUpdateDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._favorites

    @favorites.setter
    def favorites(self, favorites):
        """Sets the favorites of this UserUpdateDTO.


        :param favorites: The favorites of this UserUpdateDTO.  # noqa: E501
        :type: list[str]
        """

        self._favorites = favorites

    @property
    def linked_person(self):
        """Gets the linked_person of this UserUpdateDTO.  # noqa: E501

        URI of the Person linked to this account  # noqa: E501

        :return: The linked_person of this UserUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._linked_person

    @linked_person.setter
    def linked_person(self, linked_person):
        """Sets the linked_person of this UserUpdateDTO.

        URI of the Person linked to this account  # noqa: E501

        :param linked_person: The linked_person of this UserUpdateDTO.  # noqa: E501
        :type: str
        """

        self._linked_person = linked_person

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
        if issubclass(UserUpdateDTO, dict):
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
        if issubclass(UserUpdateDTO, dict):
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
        if not isinstance(other, UserUpdateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




