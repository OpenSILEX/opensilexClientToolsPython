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


class FontConfigDTO(object):
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
        'family': 'str',
        'style': 'str',
        'weight': 'str',
        'url': 'str',
        'src': 'dict(str, str)'
    }

    attribute_map = {
        'family': 'family',
        'style': 'style',
        'weight': 'weight',
        'url': 'url',
        'src': 'src'
    }

    def __init__(self, family=None, style=None, weight=None, url=None, src=None):  # noqa: E501
        """FontConfigDTO - a model defined in Swagger"""  # noqa: E501

        self._family = None
        self._style = None
        self._weight = None
        self._url = None
        self._src = None
        self.discriminator = None

        if family is not None:
            self.family = family
        if style is not None:
            self.style = style
        if weight is not None:
            self.weight = weight
        if url is not None:
            self.url = url
        if src is not None:
            self.src = src

    @property
    def family(self):
        """Gets the family of this FontConfigDTO.  # noqa: E501


        :return: The family of this FontConfigDTO.  # noqa: E501
        :rtype: str
        """
        return self._family

    @family.setter
    def family(self, family):
        """Sets the family of this FontConfigDTO.


        :param family: The family of this FontConfigDTO.  # noqa: E501
        :type: str
        """

        self._family = family

    @property
    def style(self):
        """Gets the style of this FontConfigDTO.  # noqa: E501


        :return: The style of this FontConfigDTO.  # noqa: E501
        :rtype: str
        """
        return self._style

    @style.setter
    def style(self, style):
        """Sets the style of this FontConfigDTO.


        :param style: The style of this FontConfigDTO.  # noqa: E501
        :type: str
        """

        self._style = style

    @property
    def weight(self):
        """Gets the weight of this FontConfigDTO.  # noqa: E501


        :return: The weight of this FontConfigDTO.  # noqa: E501
        :rtype: str
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this FontConfigDTO.


        :param weight: The weight of this FontConfigDTO.  # noqa: E501
        :type: str
        """

        self._weight = weight

    @property
    def url(self):
        """Gets the url of this FontConfigDTO.  # noqa: E501


        :return: The url of this FontConfigDTO.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this FontConfigDTO.


        :param url: The url of this FontConfigDTO.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def src(self):
        """Gets the src of this FontConfigDTO.  # noqa: E501


        :return: The src of this FontConfigDTO.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._src

    @src.setter
    def src(self, src):
        """Sets the src of this FontConfigDTO.


        :param src: The src of this FontConfigDTO.  # noqa: E501
        :type: dict(str, str)
        """

        self._src = src

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
        if issubclass(FontConfigDTO, dict):
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
        if not isinstance(other, FontConfigDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
