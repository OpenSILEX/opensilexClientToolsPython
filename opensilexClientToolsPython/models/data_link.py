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


class DataLink(object):
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
        'data_link_name': 'str',
        'name': 'str',
        'type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'data_link_name': 'dataLinkName',
        'name': 'name',
        'type': 'type',
        'url': 'url'
    }

    def __init__(self, data_link_name=None, name=None, type=None, url=None):  # noqa: E501
        """DataLink - a model defined in Swagger"""  # noqa: E501

        self._data_link_name = None
        self._name = None
        self._type = None
        self._url = None
        self.discriminator = None

        if data_link_name is not None:
            self.data_link_name = data_link_name
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url

    @property
    def data_link_name(self):
        """Gets the data_link_name of this DataLink.  # noqa: E501


        :return: The data_link_name of this DataLink.  # noqa: E501
        :rtype: str
        """
        return self._data_link_name

    @data_link_name.setter
    def data_link_name(self, data_link_name):
        """Sets the data_link_name of this DataLink.


        :param data_link_name: The data_link_name of this DataLink.  # noqa: E501
        :type: str
        """

        self._data_link_name = data_link_name

    @property
    def name(self):
        """Gets the name of this DataLink.  # noqa: E501


        :return: The name of this DataLink.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataLink.


        :param name: The name of this DataLink.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this DataLink.  # noqa: E501


        :return: The type of this DataLink.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DataLink.


        :param type: The type of this DataLink.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def url(self):
        """Gets the url of this DataLink.  # noqa: E501


        :return: The url of this DataLink.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DataLink.


        :param url: The url of this DataLink.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(DataLink, dict):
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
        if not isinstance(other, DataLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
