# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.2.7-rdg
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict


class UnitUpdateDTO(object):
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
        'description': 'str',
        'symbol': 'str',
        'alternative_symbol': 'str',
        'exact_match': 'list[str]',
        'close_match': 'list[str]',
        'broad_match': 'list[str]',
        'narrow_match': 'list[str]'
    }

    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'description': 'description',
        'symbol': 'symbol',
        'alternative_symbol': 'alternative_symbol',
        'exact_match': 'exact_match',
        'close_match': 'close_match',
        'broad_match': 'broad_match',
        'narrow_match': 'narrow_match'
    }
    def __init__(self,
        uri : 'str',
        name : 'str',
        description : 'str' = None,
        symbol : 'str' = None,
        alternative_symbol : 'str' = None,
        exact_match : 'List[str]' = None,
        close_match : 'List[str]' = None,
        broad_match : 'List[str]' = None,
        narrow_match : 'List[str]' = None):  # noqa: E501
        """UnitUpdateDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._name = None
        self._description = None
        self._symbol = None
        self._alternative_symbol = None
        self._exact_match = None
        self._close_match = None
        self._broad_match = None
        self._narrow_match = None
        self.discriminator = None

        self.uri = uri
        self.name = name
        if description is not None:
            self.description = description
        if symbol is not None:
            self.symbol = symbol
        if alternative_symbol is not None:
            self.alternative_symbol = alternative_symbol
        if exact_match is not None:
            self.exact_match = exact_match
        if close_match is not None:
            self.close_match = close_match
        if broad_match is not None:
            self.broad_match = broad_match
        if narrow_match is not None:
            self.narrow_match = narrow_match

    @property
    def uri(self):
        """Gets the uri of this UnitUpdateDTO.  # noqa: E501


        :return: The uri of this UnitUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this UnitUpdateDTO.


        :param uri: The uri of this UnitUpdateDTO.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def name(self):
        """Gets the name of this UnitUpdateDTO.  # noqa: E501


        :return: The name of this UnitUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UnitUpdateDTO.


        :param name: The name of this UnitUpdateDTO.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this UnitUpdateDTO.  # noqa: E501


        :return: The description of this UnitUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UnitUpdateDTO.


        :param description: The description of this UnitUpdateDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def symbol(self):
        """Gets the symbol of this UnitUpdateDTO.  # noqa: E501


        :return: The symbol of this UnitUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this UnitUpdateDTO.


        :param symbol: The symbol of this UnitUpdateDTO.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def alternative_symbol(self):
        """Gets the alternative_symbol of this UnitUpdateDTO.  # noqa: E501


        :return: The alternative_symbol of this UnitUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._alternative_symbol

    @alternative_symbol.setter
    def alternative_symbol(self, alternative_symbol):
        """Sets the alternative_symbol of this UnitUpdateDTO.


        :param alternative_symbol: The alternative_symbol of this UnitUpdateDTO.  # noqa: E501
        :type: str
        """

        self._alternative_symbol = alternative_symbol

    @property
    def exact_match(self):
        """Gets the exact_match of this UnitUpdateDTO.  # noqa: E501


        :return: The exact_match of this UnitUpdateDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._exact_match

    @exact_match.setter
    def exact_match(self, exact_match):
        """Sets the exact_match of this UnitUpdateDTO.


        :param exact_match: The exact_match of this UnitUpdateDTO.  # noqa: E501
        :type: list[str]
        """

        self._exact_match = exact_match

    @property
    def close_match(self):
        """Gets the close_match of this UnitUpdateDTO.  # noqa: E501


        :return: The close_match of this UnitUpdateDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._close_match

    @close_match.setter
    def close_match(self, close_match):
        """Sets the close_match of this UnitUpdateDTO.


        :param close_match: The close_match of this UnitUpdateDTO.  # noqa: E501
        :type: list[str]
        """

        self._close_match = close_match

    @property
    def broad_match(self):
        """Gets the broad_match of this UnitUpdateDTO.  # noqa: E501


        :return: The broad_match of this UnitUpdateDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._broad_match

    @broad_match.setter
    def broad_match(self, broad_match):
        """Sets the broad_match of this UnitUpdateDTO.


        :param broad_match: The broad_match of this UnitUpdateDTO.  # noqa: E501
        :type: list[str]
        """

        self._broad_match = broad_match

    @property
    def narrow_match(self):
        """Gets the narrow_match of this UnitUpdateDTO.  # noqa: E501


        :return: The narrow_match of this UnitUpdateDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._narrow_match

    @narrow_match.setter
    def narrow_match(self, narrow_match):
        """Sets the narrow_match of this UnitUpdateDTO.


        :param narrow_match: The narrow_match of this UnitUpdateDTO.  # noqa: E501
        :type: list[str]
        """

        self._narrow_match = narrow_match

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
        if issubclass(UnitUpdateDTO, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_api_formated_dict(self):
        """Returns a dict of properties as named in the API rather than in the model itself"""
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
        if issubclass(UnitUpdateDTO, dict):
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
        if not isinstance(other, UnitUpdateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




